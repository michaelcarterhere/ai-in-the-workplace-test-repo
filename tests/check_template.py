#!/usr/bin/env python3
"""Static checks for the research-and-writing template.

Reads the repository. Does not sign in, create a codespace, or enroll a plan.
A missing Docker daemon is reported and does not fail the file checks.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

IMAGE = (
    "mcr.microsoft.com/devcontainers/base:2.2.5-bookworm"
    "@sha256:99f5250dd2d5f8b11046d5662dd94c1e3c1dae56b560c7caad5ceb7edf349046"
)
IMAGE_TAG = "2.2.5-bookworm"

REQUIRED_PATHS = [
    "README.md",
    "START_HERE.md",
    "INSTRUCTOR.md",
    "ACCEPTANCE.md",
    "AGENTS.md",
    ".github/copilot-instructions.md",
    ".devcontainer/devcontainer.json",
    ".vscode/settings.json",
    ".vscode/extensions.json",
    ".markdownlint.json",
    "cspell.json",
    ".gitignore",
    "brief/question.md",
    "brief/criteria.md",
    "sources/citation-notes.md",
    "sources/source-log.md",
    "notes/working-notes.md",
    "drafts/brief-draft.md",
    "outputs/final-brief.md",
    "reflection/activity-log.md",
    "slides/README.md",
    "slides/slides.md",
    "tests/README.md",
    "tests/check_template.py",
]

ALLOWED_DEVCONTAINER_EXTENSIONS = {
    "DavidAnson.vscode-markdownlint",
    "streetsidesoftware.code-spell-checker",
    "marp-team.marp-vscode",
}
ALLOWED_RECOMMENDATIONS = ALLOWED_DEVCONTAINER_EXTENSIONS | {"GitHub.copilot"}
ALLOWED_UNWANTED = {"ms-python.python", "ms-toolsai.jupyter"}

FORBIDDEN_SETTING_KEYS = {
    "security.workspace.trust.enabled",
    "security.workspace.trust.startupPrompt",
    "security.workspace.trust.banner",
    "security.workspace.trust.untrustedFiles",
    "telemetry.telemetryLevel",
    "telemetry.feedback.enabled",
    "chat.disableAIFeatures",
    "chat.tools.autoApprove",
    "chat.tools.terminal.autoApprove",
    "github.copilot.chat.agent.autoFix",
    "github.copilot.chat.tools.terminal.autoApprove",
}

FORBIDDEN_PHRASES = [
    "telemetry is disabled",
    "always shows a trust prompt",
    "copilot is included with this template",
    "payment is required",
    "education access is verified",
    "guaranteed prompt",
    "auto-approve every",
]

SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
]

DOC_URLS = [
    "https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces",
    "https://docs.github.com/en/billing/concepts/product-billing/github-codespaces",
    "https://docs.github.com/en/billing/reference/product-usage-included",
    "https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-included-usage",
    "https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/setting-up-a-template-repository-for-github-codespaces",
    "https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository",
    "https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds",
    "https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing",
    "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode",
    "https://docs.github.com/en/copilot/reference/custom-instructions-support",
    "https://code.visualstudio.com/docs/setup/copilot",
    "https://code.visualstudio.com/docs/editing/workspaces/workspace-trust",
    "https://code.visualstudio.com/docs/agents/concepts/trust-and-safety",
    "https://code.visualstudio.com/docs/agents/reference/custom-instructions-reference",
    "https://github.com/features/copilot/plans",
    "https://cursor.com/canvas/store-efcea722-aba4-4bd4-b35f-3a03022c7217/57d9ba4a-3b60-4ebc-b972-b838ad954191",
]


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.notes: list[str] = []

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def note(self, message: str) -> None:
        self.notes.append(message)


def strip_jsonc(text: str) -> str:
    out: list[str] = []
    i = 0
    n = len(text)
    in_string = False
    escape = False
    while i < n:
        ch = text[i]
        if in_string:
            out.append(ch)
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            i += 1
            continue
        if ch == '"':
            in_string = True
            out.append(ch)
            i += 1
            continue
        if ch == "/" and i + 1 < n and text[i + 1] == "/":
            i += 2
            while i < n and text[i] not in "\r\n":
                i += 1
            continue
        if ch == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i = min(n, i + 2)
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def load_json(path: Path, report: Report):
    try:
        return json.loads(strip_jsonc(path.read_text(encoding="utf-8")))
    except json.JSONDecodeError as exc:
        report.fail(f"{path.relative_to(ROOT)} is not valid JSON/JSONC: {exc}")
        return None


def walk_keys(value, found: list[str], trail: str = "") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            found.append(str(key))
            walk_keys(child, found, trail + "/" + str(key))
            if str(key) in FORBIDDEN_SETTING_KEYS and child not in (None, {}, []):
                found.append(f"SET:{key}={child!r}")
    elif isinstance(value, list):
        for child in value:
            walk_keys(child, found, trail)


def markdown_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "agent-tools"} for part in path.parts):
            continue
        files.append(path)
    return files


def check_required(report: Report) -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).is_file():
            report.fail(f"missing required file {rel}")
    for directory in [
        "brief",
        "sources",
        "notes",
        "drafts",
        "outputs",
        "reflection",
        "slides",
        ".devcontainer",
        ".vscode",
        ".github",
    ]:
        path = ROOT / directory
        if not path.is_dir():
            report.fail(f"missing directory {directory}")
            continue
        visible = [child for child in path.iterdir() if child.name != ".gitkeep"]
        if not visible:
            report.fail(f"{directory} has no starter files")


def check_devcontainer(report: Report) -> dict | None:
    path = ROOT / ".devcontainer" / "devcontainer.json"
    data = load_json(path, report)
    if not isinstance(data, dict):
        return None
    if data.get("image") != IMAGE:
        report.fail(f"image pin mismatch: {data.get('image')!r}")
    else:
        report.note(f"image pin matches {IMAGE_TAG} digest")
    if data.get("remoteUser") != "vscode":
        report.fail("remoteUser must be vscode, not root")
    for key in (
        "features",
        "forwardPorts",
        "postCreateCommand",
        "postStartCommand",
        "postAttachCommand",
        "onCreateCommand",
        "updateContentCommand",
        "initializeCommand",
        "runArgs",
        "capAdd",
        "privileged",
        "mounts",
    ):
        if key in data:
            report.fail(f"devcontainer.json should not set {key}")
    custom = data.get("customizations") or {}
    extensions = ((custom.get("vscode") or {}).get("extensions")) or []
    if set(extensions) != ALLOWED_DEVCONTAINER_EXTENSIONS:
        report.fail(f"unexpected devcontainer extensions: {extensions}")
    if "GitHub.copilot" in extensions or "GitHub.copilot-chat" in extensions:
        report.fail("Copilot must not be auto-installed by the devcontainer")
    open_files = ((custom.get("codespaces") or {}).get("openFiles")) or []
    if open_files != ["START_HERE.md"]:
        report.fail(f"openFiles mismatch: {open_files}")
    if "settings" in (custom.get("vscode") or {}):
        report.fail("editor settings belong only in .vscode/settings.json")
    return data


def check_vscode(report: Report) -> None:
    settings = load_json(ROOT / ".vscode" / "settings.json", report)
    extensions = load_json(ROOT / ".vscode" / "extensions.json", report)
    if isinstance(settings, dict):
        if settings.get("editor.wordWrap") != "on":
            report.fail("workspace settings should enable editor.wordWrap")
        if settings.get("markdown.marp.html") != "off":
            report.fail(
                "markdown.marp.html must be off so Marp does not render HTML"
            )
        if settings.get("markdown.marp.enableHtml") not in (None, False):
            report.fail("deprecated markdown.marp.enableHtml must not be enabled")
        for key in (
            "markdown.marp.browser",
            "markdown.marp.browserPath",
            "markdown.marp.chromePath",
            "markdown.marp.exportType",
            "markdown.marp.exportAutoOpen",
            "markdown.marp.openExportedHtmlInIntegratedBrowser",
            "markdown.marp.themes",
            "markdown.marp.pptx.editable",
        ):
            if key in settings:
                report.fail(f"do not configure Marp export or themes: {key}")
        keys: list[str] = []
        walk_keys(settings, keys)
        for key in keys:
            if key.startswith("SET:"):
                report.fail(f"forbidden setting in .vscode/settings.json: {key}")
    if isinstance(extensions, dict):
        recommendations = set(extensions.get("recommendations") or [])
        unwanted = set(extensions.get("unwantedRecommendations") or [])
        if recommendations != ALLOWED_RECOMMENDATIONS:
            report.fail(f"unexpected recommendations: {sorted(recommendations)}")
        if unwanted != ALLOWED_UNWANTED:
            report.fail(f"unexpected unwantedRecommendations: {sorted(unwanted)}")
    for name in (".markdownlint.json", "cspell.json"):
        load_json(ROOT / name, report)


def check_forbidden_settings_everywhere(report: Report) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "agent-tools", "tests"} for part in path.parts):
            continue
        if path.suffix not in {".json", ".jsonc"}:
            continue
        data = load_json(path, report)
        if data is None:
            continue
        keys: list[str] = []
        walk_keys(data, keys)
        for key in keys:
            if key.startswith("SET:"):
                report.fail(f"{path.relative_to(ROOT)} sets {key}")


def check_links(report: Report) -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in link_re.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                continue
            path_part, _, anchor = target.partition("#")
            if not path_part:
                continue
            resolved = (path.parent / path_part).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                report.fail(f"{path.relative_to(ROOT)} links outside the repo: {target}")
                continue
            if not resolved.is_file():
                report.fail(f"{path.relative_to(ROOT)} broken link: {target}")
            if anchor and resolved.suffix == ".md":
                heading_text = anchor.replace("-", " ").lower()
                headings = []
                for line in resolved.read_text(encoding="utf-8").splitlines():
                    if line.startswith("#"):
                        title = re.sub(r"[^a-z0-9 ]+", "", line.lstrip("#").strip().lower())
                        headings.append("-".join(title.split()))
                if anchor.lower() not in headings and heading_text not in [
                    h.replace("-", " ") for h in headings
                ]:
                    # GitHub heading anchors are a best effort. Fail only when
                    # no heading slug is close to the anchor.
                    if anchor.lower() not in headings:
                        report.fail(
                            f"{path.relative_to(ROOT)} anchor not found: {target}"
                        )


def check_instructions(report: Report) -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    copilot = (ROOT / ".github" / "copilot-instructions.md").read_text(encoding="utf-8")
    required_bits = [
        "Never fabricate a citation",
        "untrusted data",
        "destructive change",
        "secrets",
        "Do not start a subscription",
        "Workspace Trust",
        "telemetry",
        "outputs/final-brief.md",
    ]
    for bit in required_bits:
        if bit not in agents:
            report.fail(f"AGENTS.md missing required rule text: {bit}")
    for bit in (
        "Write or edit Markdown Marp files only",
        "do not install packages or run scripts or exporters",
        "unless the student explicitly asks and approves",
    ):
        if bit not in agents:
            report.fail(f"AGENTS.md missing slide rule text: {bit}")
    if "cursor/import-research-writing-template-c934" in "\n".join(
        path.read_text(encoding="utf-8") for path in markdown_files()
    ):
        report.fail("stale review-branch name is still in a Markdown file")
    slides = (ROOT / "slides" / "slides.md").read_text(encoding="utf-8")
    if "marp: true" not in slides or "fictional" not in slides.lower():
        report.fail("slides/slides.md must be a fictional Marp Markdown deck")
    if "AGENTS.md" not in copilot:
        report.fail("copilot-instructions.md must point at AGENTS.md")
    if "Never fabricate a citation" in copilot:
        report.fail("copilot-instructions.md duplicates AGENTS.md rules")
    if len(copilot.split()) > 220:
        report.fail("copilot-instructions.md is long enough to drift from AGENTS.md")
    for rel in ("README.md", "START_HERE.md", "ACCEPTANCE.md"):
        text = (ROOT / rel).read_text(encoding="utf-8").lower()
        if "not an agentic experience" not in text:
            report.fail(f"{rel} must describe the no-agent path as not an agentic experience")
    acceptance = (ROOT / "ACCEPTANCE.md").read_text(encoding="utf-8")
    for bit in (
        "Verified static checks",
        "Pending: Michael's free-account browser test",
        "### A. Codespaces quota and provisioning",
        "### B. Copilot Free, agent entitlement, and limits",
        "payment method",
        "paid trial",
        "Copilot Free",
    ):
        if bit not in acceptance:
            report.fail(f"ACCEPTANCE.md missing section text: {bit}")
    start = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
    if "Origin address cannot open GitHub Codespaces" not in start:
        report.fail("START_HERE.md must say an Origin address cannot open Codespaces")
    question = (ROOT / "brief" / "question.md").read_text(encoding="utf-8")
    if "fictional" not in question.lower() or "Lumen Lane" not in question:
        report.fail("brief/question.md must keep the fictional Lumen Lane frame")
    source_log = (ROOT / "sources" / "source-log.md").read_text(encoding="utf-8")
    if "example.com" in source_log and "not a real source" not in source_log.lower():
        report.fail("example.com appears without a not-a-real-source label")
    joined = "\n".join(path.read_text(encoding="utf-8") for path in markdown_files())
    lowered = joined.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in lowered:
            report.fail(f"overclaim phrase present: {phrase}")
    if "shields.io" in lowered or "[![ " in joined:
        report.fail("launch badge markup is present")


def check_secrets_and_privacy(report: Report) -> None:
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for needle in (".env", "secrets/", "*.pem"):
        if needle not in gitignore:
            report.fail(f".gitignore missing {needle}")
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "agent-tools"} for part in path.parts):
            continue
        if path.suffix in {".png", ".jpg", ".zip"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                report.fail(f"secret-shaped string in {path.relative_to(ROOT)}")
    workflows = ROOT / ".github" / "workflows"
    if workflows.exists():
        report.fail("a GitHub Actions workflow is present; prebuilds must stay opt-in")


def fetch(url: str, accept: str | None = None, timeout: int = 30):
    headers = {"User-Agent": "research-writing-template-check"}
    if accept:
        headers["Accept"] = accept
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.status, dict(response.headers), response.read()


def check_registry(report: Report) -> None:
    url = f"https://mcr.microsoft.com/v2/devcontainers/base/manifests/{IMAGE_TAG}"
    accept = (
        "application/vnd.oci.image.index.v1+json, "
        "application/vnd.docker.distribution.manifest.list.v2+json"
    )
    try:
        status, headers, _body = fetch(url, accept=accept)
    except Exception as exc:  # noqa: BLE001 - report the network failure as a check
        report.fail(f"registry manifest request failed: {exc}")
        return
    digest = headers.get("Docker-Content-Digest") or headers.get("docker-content-digest")
    expected = IMAGE.split("@", 1)[1]
    if status != 200 or digest != expected:
        report.fail(f"registry digest mismatch: status {status} digest {digest}")
    else:
        report.note(f"registry confirmed {IMAGE_TAG} digest {digest}")


def check_doc_urls(report: Report) -> None:
    linked: set[str] = set()
    link_re = re.compile(r"https://[^\s)>\"\]]+")
    for path in markdown_files():
        for match in link_re.findall(path.read_text(encoding="utf-8")):
            linked.add(match.rstrip(".,"))
    missing = sorted(set(DOC_URLS) - linked)
    for url in missing:
        report.fail(f"documented URL is not linked from the template: {url}")
    ok = 0
    for url in sorted(linked):
        if not url.startswith("https://"):
            continue
        if url.startswith("https://example.com"):
            report.note(f"skipped live fetch for placeholder source: {url}")
            continue
        try:
            status, _headers, _body = fetch(url, timeout=25)
        except urllib.error.HTTPError as exc:
            if exc.code in {401, 403}:
                report.note(f"doc URL returned {exc.code}, left inconclusive: {url}")
                continue
            report.fail(f"doc URL {url} returned HTTP {exc.code}")
            continue
        except Exception as exc:  # noqa: BLE001
            report.fail(f"doc URL request failed for {url}: {exc}")
            continue
        if status >= 400:
            report.fail(f"doc URL {url} returned HTTP {status}")
        else:
            ok += 1
    report.note(f"documentation URLs responded below HTTP 400: {ok}")


def check_docker(report: Report) -> None:
    if shutil.which("docker") or os.path.exists("/var/run/docker.sock"):
        report.note("Docker appears present; this script does not build the image")
    else:
        report.note(
            "Docker is not installed and /var/run/docker.sock is absent. "
            "The container was not pulled or started."
        )


def main() -> int:
    report = Report()
    check_required(report)
    check_devcontainer(report)
    check_vscode(report)
    check_forbidden_settings_everywhere(report)
    check_links(report)
    check_instructions(report)
    check_secrets_and_privacy(report)
    check_registry(report)
    check_doc_urls(report)
    check_docker(report)
    print("Static check root:", ROOT)
    for note in report.notes:
        print("NOTE", note)
    if report.failures:
        print(f"FAILURES {len(report.failures)}")
        for failure in report.failures:
            print("FAIL", failure)
        return 1
    print("PASS static checks")
    print(
        "REPORTED in ACCEPTANCE.md: unpaid-account Codespace opened, "
        "agent answered, agent created a Markdown file in drafts/"
    )
    print(
        "PENDING Marp preview, plus quota, trust, plan, and usage lines "
        "left blank (this command does not sign in)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
