# Instructor notes

These files are the research-and-writing starter for GENE94, on `main` in the public GitHub template repository `michaelcarterhere/ai-in-the-workplace-test-repo`. Students use [START_HERE.md](../START_HERE.md). This page is the GitHub setup, the cost boundaries, and how agent instructions are loaded.

## This repository

Codespaces starts from a repository on github.com. There is no launch badge. Editing these files does not change visibility, collaborators, billing, or the template setting.

GitHub documents the codespace side of a template in [Setting up a template repository for GitHub Codespaces](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/setting-up-a-template-repository-for-github-codespaces).

Tell each student to choose **Use this template**, create a **private** repository under their own account, and then create a codespace from **their** repository. Ask them to pick the **2-core** machine when GitHub offers a choice. Tell them not to add a payment method. This `devcontainer.json` does not request a larger machine.

Students then have independent copies. They are not live co-editors on one shared codespace. A codespace opened directly on the shared template is a poor fit for student work, because those students would be aiming their commits at the same repository.

The template repository is public so the starter files are easy to copy. Each student makes their own copy private. The starter files are fictional and contain no student records. Student writing belongs in that private copy.

### Later: an optional prebuild

A prebuild can shorten the wait when a codespace is created. It also uses GitHub Actions time and storage. GitHub describes that in [About GitHub Codespaces prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds).

This repository does not add a prebuild workflow. Do not enable a prebuild unless you have already decided the Actions and storage use is acceptable. Do not add a payment method as part of finishing setup.

## Environment that is preconfigured

[.devcontainer/devcontainer.json](../.devcontainer/devcontainer.json) pins a small Debian image with Git:

`mcr.microsoft.com/devcontainers/base:2.2.5-bookworm`

The image also carries the index digest recorded in that file. On 9 November 2026 the Microsoft registry reported `2.2.5-bookworm` as the newest stable bookworm tag, and the floating `bookworm` tag shared that same index digest. Recheck the tag list before a cohort. The pin will go stale on purpose until you move it.

The image's devcontainer metadata sets `remoteUser` to `vscode`. The OCI image config still lists `User` as `root`, so this file sets `remoteUser` to `vscode` explicitly and does not request a root session. A local container start on 9 November 2026 confirmed both facts: with no user override the process was root, and `--user vscode` ran as uid 1000. That start was not a GitHub Codespace. The static checker does not start the container. The latest command output is in [tests/STATIC_CHECK_REPORT.md](../tests/STATIC_CHECK_REPORT.md).

Extensions installed when the codespace is created:

- `DavidAnson.vscode-markdownlint` (marketplace version observed 9 November 2026: 0.62.1, not pinned)
- `streetsidesoftware.code-spell-checker` (observed: 4.10.0, not pinned)
- `marp-team.marp-vscode` (Marp for VS Code 3.5.2, read from the extension package on 9 November 2026, not pinned)

Versions are not pinned because the codespace installs a build that matches the editor host. A stale version pin can block creation. No Python, Jupyter, or science-stack features are installed. This folder does not add a separate browser package or a separate Marp CLI install. The extension bundles its own preview. Its export command can still call the CLI that ships inside the extension.

## Slides and Marp settings

Students who want slides edit [slides/slides.md](../slides/slides.md). The guide is [slides/README.md](../slides/README.md). [AGENTS.md](../AGENTS.md) tells the agent to write or edit Markdown Marp files only, and not to install packages or run scripts or exporters unless the student explicitly asks and approves.

Checked against [Marp for VS Code](https://github.com/marp-team/marp-vscode) 3.5.2 on 9 November 2026:

- `markdown.marp.html` defaults to `default`, which enables a selective HTML allowlist in a trusted workspace. `all` allows arbitrary HTML, and the extension description says that can make rendering insecure. This workspace sets `markdown.marp.html` to `off` in [.vscode/settings.json](../.vscode/settings.json). In an untrusted workspace the extension already treats HTML as off.
- The deprecated `markdown.marp.enableHtml` defaults to false and turns on all HTML when true. This workspace does not set it.
- The preview options in that version keep `script` false. This folder does not add a setting that runs slide scripts.
- Export to PDF, PowerPoint, and images uses a browser through `markdown.marp.browser` (default `auto`) and can open the file afterward (`markdown.marp.exportAutoOpen` defaults to true). `markdown.marp.openExportedHtmlInIntegratedBrowser` defaults to `off`. This workspace does not set any of those export keys, does not set a browser path, and does not add theme CSS.
- The same version contributes an `export_marp` language-model tool and an export command. Those are part of the extension. This folder does not turn them on with a setting. The assignment path is the Markdown preview. The agent rule forbids the exporter unless the student explicitly asks and approves.

`GitHub.copilot` is only a workspace recommendation in [.vscode/extensions.json](../.vscode/extensions.json). It is not in the auto-install list. On 9 November 2026 the marketplace also listed `GitHub.copilot-chat` 0.48.1. This folder does not recommend that second extension. A visible Copilot icon, if GitHub shows one inside a codespace, is still not an allowance.

[.vscode/settings.json](../.vscode/settings.json) turns on word wrap and Markdown link checking. It does not disable Workspace Trust, does not auto-approve agent commands, and does not change telemetry. This folder makes no privacy claim about model providers. A private repository does not describe how an AI product handles prompts. Telemetry settings are left at the product default. Official Copilot setup notes mention that people can change telemetry themselves. This template does not do that for them.

`customizations.codespaces.openFiles` opens [START_HERE.md](../START_HERE.md) the first time a codespace is opened in the VS Code **web** client. GitHub documents that property in [Automatically opening files](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository). The desktop app ignores it.

The base image's Git feature adds a one-line Copilot code-generation note that Git is installed. That note is inside the image, not in this folder. It is not an assignment rule. [AGENTS.md](../AGENTS.md) remains the assignment rule set.

## How agent instructions load

Checked against GitHub and VS Code documentation on 9 November 2026:

- VS Code Copilot Chat discovers repository instructions in `.github/copilot-instructions.md` and agent instructions in `AGENTS.md`, and combines applicable files. There is no general precedence that lets one silently win. See [custom instruction support](https://docs.github.com/en/copilot/reference/custom-instructions-support) and the [custom instructions reference](https://code.visualstudio.com/docs/agents/reference/custom-instructions-reference).
- A Markdown link does not guarantee that the linked file is copied into the request. Essential rules therefore live in `AGENTS.md`, which Copilot discovers directly.
- `.github/copilot-instructions.md` only tells Copilot to open `AGENTS.md` and not to invent a second policy. The rules are not duplicated, so the files cannot diverge.
- Whether a particular account's session actually followed the file is part of the free-account test. Static checks cannot see a model request.

Copilot Free's marketing page, on the day those docs were read, listed custom instructions for agent mode in the IDE as included on the Free column. Code review is a different feature and is not part of this pilot. Recheck before you rely on that table. This folder does not assert that a paid plan is required, and it does not assert that an education plan is present.

## Allowances

Two meters, checked separately. Figures below are what the official pages said on 9 November 2026. They are not a price quote and they are not a promise that a future page will match.

**Codespaces, personal accounts.** [GitHub Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) and [product usage included with each plan](https://docs.github.com/en/billing/reference/product-usage-included) said GitHub Free for personal accounts includes 120 core hours and 15 GB-month of Codespaces storage a month. Core hours scale with machine size. A 2-core machine counts two core hours for each hour it is running. [What are GitHub Codespaces?](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces) said a personal account can start using Codespaces without a payment method. When the included amount is gone and no payment method is on file, use is blocked. [Getting the most out of your included usage](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-included-usage) explains compute, storage, and the fact that deleting a codespace does not erase usage already counted in the current month.

**Custom image storage.** The same included-usage article says storage for GitHub's default dev container image is not counted the way a custom image is. This pilot uses the small pinned base image so students are not placed in a large language-and-science image. The container can count toward Codespaces storage. That is a deliberate tradeoff. The linux/amd64 image manifest listed about 360 MB of compressed layers on 9 November 2026. GitHub's billed storage figure will differ. Do not treat 360 MB as a bill.

**Copilot.** [Usage-based billing for individuals](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing) said Copilot Free and Copilot Student have an AI credit allowance and auto model selection only, and that Copilot Free includes 2,000 code completions a month. The credit table on that page listed paid plans and did not publish a Free credit total. Do not fill in a number the page omits. Agent mode can use more of an allowance than a short chat. [VS Code's Copilot setup](https://code.visualstudio.com/docs/setup/copilot) said that signing in without a plan enrolls an eligible account in Copilot Free. This folder does not perform that sign-in, does not start a paid trial, and does not add a payment method.

Education or student entitlement was not verified for any cohort. [ACCEPTANCE.md](ACCEPTANCE.md) is the checklist for recording what one free account can do. One account does not generalize to a class.

## Acceptance checklist

[ACCEPTANCE.md](ACCEPTANCE.md) is the facilitator checklist: a codespace on a private copy, a separate note of any agent allowance, and a Marp preview in the browser. Do not store a password in this folder. Do not add a payment method, start a paid trial, or click upgrade to finish a check. The static checker confirms the registry digest and does not itself start the container. Its latest output is in [tests/STATIC_CHECK_REPORT.md](../tests/STATIC_CHECK_REPORT.md).

Run the checker from the folder root:

```bash
python3 tests/check_template.py
```

Students do not need that command for the writing assignment.
