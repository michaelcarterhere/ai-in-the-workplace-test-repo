# Static check report

Date: 9 November 2026

Repository: private GitHub template repository `michaelcarterhere/ai-in-the-workplace-test-repo`, default branch `main`.

The report from the first import is historical. The sections below are from the rerun after the Marp Markdown change.

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
- Seventeen documentation URLs responded below HTTP 400, including the Marp for VS Code repository linked from the instructor notes and the slide guide.
- Docker was present, so the checker printed that it does not build the image. This rerun did not start a container.

The same command was run again after this file was saved. It exited 0 with those same notes.

## Verified static checks

- JSON and JSONC parsed for `.devcontainer/devcontainer.json`, `.vscode/settings.json`, `.vscode/extensions.json`, `.markdownlint.json`, and `cspell.json`.
- `marp-team.marp-vscode` is in the dev container auto-install list, together with markdownlint and the spell checker. `GitHub.copilot` stays a recommendation and is not auto-installed.
- `markdown.marp.html` is `off`. The deprecated HTML switch is unset. Export, browser, and theme keys are unset.
- Image pin, `remoteUser` `vscode`, `openFiles` `START_HERE.md`, and the absence of install commands, ports, mounts, and privilege flags still match.
- Workspace settings enable word wrap and Markdown link checks. They do not disable Workspace Trust, change telemetry, disable AI features, or set an auto-approve flag.
- Internal Markdown links resolve, including the new slide guide.
- `AGENTS.md` still holds the citation, trust, and subscription rules, and it now tells the agent to write or edit Markdown Marp files only. It must not install packages or run scripts or exporters unless the student explicitly asks and approves. `.github/copilot-instructions.md` still only points at `AGENTS.md`.
- README, START_HERE, and ACCEPTANCE still describe the no-agent path as a writing workspace and include the phrase "not an agentic experience."
- Starter slide text is fictional and marked `marp: true`.

A passing static check does not mean the Marp preview was opened in a Codespace.

## Unpaid-account session, reported

Recorded in [ACCEPTANCE.md](../ACCEPTANCE.md) from Michael's report on 9 November 2026. This command did not sign in and did not repeat that session.

- A Codespace opened on the unpaid student account.
- The agent answered.
- The agent created a Markdown file in `drafts/`.
- A request for a slide deck needed several approvals to run scripts.

## Not done in this rerun

- Marp preview was not opened. That check stays pending.
- Quota numbers, machine type, trust-dialog wording, plan name, and usage units were not in the report and stay blank.
- The earlier local Docker start of the pinned image was not repeated. Docker being installed here only changed the checker's note. It did not start the image.
- Visibility, collaborators, billing, and the template setting were not changed.

## Next setup

Merge is a separate decision. After this change is on `main`, the remaining unpaid-account check is the Marp preview in [ACCEPTANCE.md](../ACCEPTANCE.md). Do not add a payment method, start a paid trial, or click upgrade as part of that test.
