# Static check report

Date: 9 November 2026

Repository: private GitHub repository `michaelcarterhere/ai-in-the-workplace-test-repo`, review branch `cursor/import-research-writing-template-c934`.

The report that arrived in the starter ZIP described an earlier Origin-draft run. It is historical. It was not reused as the result of this import. The sections below are from the rerun on this branch.

## What was rerun

Command, from the repository root:

```bash
python3 tests/check_template.py
```

Exit code 0.

Command notes from that run:

- Image pin matches `2.2.5-bookworm`.
- Registry confirmed tag `2.2.5-bookworm` digest `sha256:99f5250dd2d5f8b11046d5662dd94c1e3c1dae56b560c7caad5ceb7edf349046`.
- The approved design page linked from [INSTRUCTOR.md](../INSTRUCTOR.md) returned HTTP 403. The checker left that URL inconclusive and did not read the page body.
- The `example.com` row was skipped as a placeholder.
- Sixteen documentation URLs responded below HTTP 400.
- Docker was present, so the checker printed that it does not build the image. The container start in the next section is a separate command, not part of this script.

The same command was run again after this file was saved. It exited 0 with those same notes.

The private repository address is written as a name, not as a web link. The checker requests every web URL in these Markdown files. An unauthenticated request to this private repository would be a 404 and would fail the check. The repository is still the one named above.

## Verified static checks

- JSON and JSONC parsed for `.devcontainer/devcontainer.json`, `.vscode/settings.json`, `.vscode/extensions.json`, `.markdownlint.json`, and `cspell.json`.
- Image pin is `mcr.microsoft.com/devcontainers/base:2.2.5-bookworm` with index digest `sha256:99f5250dd2d5f8b11046d5662dd94c1e3c1dae56b560c7caad5ceb7edf349046`. A live Microsoft registry read of tag `2.2.5-bookworm` returned that digest.
- `remoteUser` is `vscode`. Copilot is not in the auto-install extension list. Auto-installed extensions are markdownlint and the spell checker only. `GitHub.copilot` is a recommendation.
- `openFiles` is `START_HERE.md`. No features, install commands, ports, mounts, or privilege flags are set. No GitHub Actions workflow is present.
- Workspace settings enable word wrap and Markdown link checks. They do not disable Workspace Trust, change telemetry, disable AI features, or set an auto-approve flag. The checker walks JSON and JSONC keys for those settings.
- Internal Markdown links resolve to files in the template. Required starter files exist and are not empty directories.
- `AGENTS.md` holds the assignment rules, including no fabricated citations, untrusted external text, student approval for upload, publish, and destructive changes, and no subscription or trial enrollment. `.github/copilot-instructions.md` points at `AGENTS.md` and does not copy those rules.
- README, START_HERE, and ACCEPTANCE describe the no-agent path as a writing workspace and include the phrase "not an agentic experience."
- ACCEPTANCE separates "Verified static checks" from "Pending: Michael's free-account browser test," with Codespaces quota and Copilot Free limits in different sections.
- The Lumen Lane story is labeled fictional. The source-log example uses `example.com` and is labeled "not a real source."
- No secret-shaped tokens were found. `.gitignore` ignores `.env`, `secrets/`, and `*.pem`.

A passing static check does not mean the unpaid account can provision a codespace or use an agent.

## Local container start, actually tested

This is not the static check. Docker was installed in this environment only so the pinned image could be started. That install is not part of the template, and no GitHub Codespace was created.

- Host architecture: `x86_64`.
- `docker pull` of the pinned digest finished with digest `sha256:99f5250dd2d5f8b11046d5662dd94c1e3c1dae56b560c7caad5ceb7edf349046`.
- `docker image inspect` reported `Config.User` `root`, architecture `amd64`, and size `360034967` bytes. The image label `devcontainer.metadata` includes `"remoteUser":"vscode"`.
- `docker run` with no user override printed `uid=0(root)` and `git version 2.56.0`.
- `docker run --user vscode` printed `uid=1000(vscode)`, wrote a file in `/home/vscode`, and printed `git version 2.56.0`.
- `@devcontainers/cli` 0.80.0 read `.devcontainer/devcontainer.json` and started a container from this config. Its log contains `Container started`. The CLI stayed attached to that container and did not exit with a finished JSON result during this run, so extension installation and a remote-user session inside that CLI container were not observed. The container was removed after the observation.

This local start does not show Workspace Trust, Copilot sign-in, quota, or the VS Code web editor.

## Not done

- The unpaid student account was not signed in. Real-account authentication remains pending. The premise that this account has no paid access was not re-checked in a browser.
- Codespaces provisioning was not run. Section A of [ACCEPTANCE.md](../ACCEPTANCE.md) is still blank.
- Copilot Free enrollment, agent mode, and request limits were not observed. Section B is still blank. Education or student Copilot access was not verified.
- The repository template setting was left off. Visibility was left private. No collaborator, payment method, prebuild, or codespace was added.
- `main` was not given these files. The branch was opened from the existing initial commit. No extra empty commit was added.

## Next setup

Merge is a separate decision and was not done. After a merge into `main`, the remaining steps are in [INSTRUCTOR.md](../INSTRUCTOR.md): mark the repository as a template, then run ACCEPTANCE sections A and B separately on the unpaid account. Do not add a payment method, start a paid trial, or click upgrade as part of that test. Do not turn the template setting on while `main` still has only the placeholder README.
