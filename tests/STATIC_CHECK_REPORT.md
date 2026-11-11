# Static check report

Date: 11 November 2026

Repository: public GitHub template repository `michaelcarterhere/ai-in-the-workplace-test-repo`, default branch `main`. Students make their own copy private. Do not add a payment method.

## What was run

Command, from the repository root:

```bash
python3 tests/check_template.py
```

Exit code 0.

Command notes from that run:

- Image pin matches `2.2.5-bookworm`.
- Registry confirmed tag `2.2.5-bookworm` digest `sha256:99f5250dd2d5f8b11046d5662dd94c1e3c1dae56b560c7caad5ceb7edf349046`.
- The `example.com` row was skipped as a placeholder.
- Seventeen documentation URLs responded below HTTP 400.
- Docker is not installed and `/var/run/docker.sock` is absent. The container was not pulled or started.

The same command was run again after this file was saved. It exited 0 with those same notes.

## Verified static checks

- JSON and JSONC parsed for `.devcontainer/devcontainer.json`, `.vscode/settings.json`, `.vscode/extensions.json`, `.markdownlint.json`, and `cspell.json`.
- `marp-team.marp-vscode` is in the dev container auto-install list, together with markdownlint and the spell checker. `GitHub.copilot` stays a recommendation and is not auto-installed.
- `markdown.marp.html` is `off`. The deprecated HTML switch is unset. Export, browser, and theme keys are unset.
- Image pin, `remoteUser` `vscode`, `openFiles` `START_HERE.md`, and the absence of install commands, ports, mounts, and privilege flags still match.
- Workspace settings enable word wrap and Markdown link checks. They do not disable Workspace Trust, change telemetry, disable AI features, or set an auto-approve flag.
- Internal Markdown links resolve, including the instructor notes in [instructor/INSTRUCTOR.md](../instructor/INSTRUCTOR.md).
- `AGENTS.md` still holds the citation, trust, and subscription rules, and it tells the agent to write or edit Markdown Marp files only. It must not install packages or run scripts or exporters unless the student explicitly asks and approves. `.github/copilot-instructions.md` still only points at `AGENTS.md`.
- README, START_HERE, and [instructor/ACCEPTANCE.md](../instructor/ACCEPTANCE.md) still describe the no-agent path as a writing workspace and include the phrase "not an agentic experience."
- README and START_HERE describe this public template repository and tell each student to make their own copy private.
- Starter slide text is fictional and marked `marp: true`.

A passing static check does not mean the Marp preview was opened in a Codespace.

## Not done in this run

- The command does not sign in, create a codespace, or enroll a plan.
- Quota, machine type, trust-dialog wording, plan name, and usage units are browser checks in [instructor/ACCEPTANCE.md](../instructor/ACCEPTANCE.md). They were not run here.
- Marp preview was not opened. That check stays in the browser checklist.
- The container was not started.
- Visibility, collaborators, billing, and the template setting were not changed.

## Facilitator note

Instructor setup is in [instructor/INSTRUCTOR.md](../instructor/INSTRUCTOR.md). The browser checklist is in [instructor/ACCEPTANCE.md](../instructor/ACCEPTANCE.md). Do not add a payment method, start a paid trial, or click upgrade as part of that check.
