# Research and writing workspace

This folder is a browser writing space for one student. The work is a short sourced brief about an AI idea for a **fictional** small organization. The files are Markdown. You do not need to write code, install a programming language, or run Docker on your own computer.

When your GitHub account has an agent allowance, one AI agent can help you research and draft. You still choose the question, accept or reject the plan, check the sources, edit the final brief, and write the reflection. The files do not sign you up for that agent.

[Open the first-run checklist](START_HERE.md)

## Where these files are

These files are on `main` in the private GitHub template repository `michaelcarterhere/ai-in-the-workplace-test-repo`.

There is no launch badge in this README. Create your own private repository with **Use this template**, then open a codespace from that copy. Classmates do not edit one shared live document.

An Origin address cannot open GitHub Codespaces. The earlier authoring copy was a private unpublished Origin draft. It is not a live mirror of this repository. Codespaces starts from a repository on github.com. Setup notes are in [INSTRUCTOR.md](INSTRUCTOR.md). These files do not turn on billing.

## Create your own copy

Each student gets an independent copy. You are not editing a shared live document with classmates.

1. Sign in to GitHub in the browser with your own account.
2. Open the template repository `michaelcarterhere/ai-in-the-workplace-test-repo` on github.com.
3. Choose **Use this template**, then **Create a new repository**.
4. Make that repository **private**. It belongs to your account.
5. On your new repository, choose **Code**, then the **Codespaces** tab, then **Create codespace on main**.
6. If GitHub asks you to pick a machine, choose the smallest one, usually **2-core**.
7. Wait for the editor. It is Visual Studio Code in the browser. [START_HERE.md](START_HERE.md) is set to open the first time in that web editor.
8. Signing in so the codespace can open is a GitHub sign-in. Copilot sign-in is a later, separate step. These files do not grant Copilot.

Your private repository is your own copy. Classmates do not edit your files.

## What is in the folder

| Path | What it is for |
| --- | --- |
| [START_HERE.md](START_HERE.md) | First-run checklist |
| [brief/question.md](brief/question.md) | Your question and your plan decision |
| [brief/criteria.md](brief/criteria.md) | What a finished brief includes |
| [sources/citation-notes.md](sources/citation-notes.md) | How to keep public sources |
| [sources/source-log.md](sources/source-log.md) | The source table you fill in |
| [notes/working-notes.md](notes/working-notes.md) | Notes while you read |
| [drafts/brief-draft.md](drafts/brief-draft.md) | Draft you can change freely |
| [outputs/final-brief.md](outputs/final-brief.md) | The brief you stand behind |
| [reflection/activity-log.md](reflection/activity-log.md) | What you decided and what any agent did |
| [slides/README.md](slides/README.md) | How to preview slides written as Markdown |
| [slides/slides.md](slides/slides.md) | Starter deck, fictional, ready to replace |
| [AGENTS.md](AGENTS.md) | Rules for an agent |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Points Copilot at those rules |
| [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json) | Small preconfigured editor environment |
| [.vscode/](.vscode/settings.json) | Word wrap and extension suggestions |

The instructor's later setup and the free-account test live in [INSTRUCTOR.md](INSTRUCTOR.md) and [ACCEPTANCE.md](ACCEPTANCE.md).

## Allowances, in plain language

A codespace uses compute time while it runs and storage while it exists. GitHub personal accounts include a monthly amount. The number is on your GitHub billing page and in [GitHub's Codespaces billing documentation](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces). This folder does not state a dollar price and does not add a payment method.

Copilot, when an account has it, uses a separate allowance. Codespaces time and an agent allowance are different. One can be available when the other is missing. Read [Copilot billing for individuals](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing) before you rely on a limit. This folder does not promise a request count.

Installing or recommending the Copilot extension does not start a plan. A sign-in button in the editor can enroll an eligible account in Copilot Free. That is a sign-up. It is not a paid plan, and it is not something this folder does for you. Do not enter a payment card. Do not start a paid trial from a prompt.

A prebuild is an optional later choice that can make a new codespace start faster. It uses GitHub Actions time and storage. This folder does not turn a prebuild on.

This environment uses a small pinned image so the editor is a writing space rather than a large science stack. GitHub's storage rules for a custom image are different from the rules for GitHub's default image. The instructor note links that documentation. No exact storage bill is promised here.

## If there is no agent

You can still finish. Read the files, look up public pages yourself, and write the brief and the reflection. That is a writing workspace in the browser. It is not an agentic experience.

## Check the files

The static check reads this folder. It does not sign in, create a codespace, or enroll a plan.

```bash
python3 tests/check_template.py
```

Students doing the writing assignment can skip that command. Details are in [tests/README.md](tests/README.md).
