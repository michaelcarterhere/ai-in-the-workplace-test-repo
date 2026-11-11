# Free-account acceptance checklist

For the instructor, before a cohort uses this public template repository. Students who are writing the brief can ignore this file.

Do not store a password in this repository. Do not add a payment method, start a paid trial, or click upgrade to finish a check.

Two kinds of result stay separate. Codespaces in section A and Copilot in section B are different checks. A result in one section does not count for the other. The Marp preview in section C is a separate check.

Slides in this folder are Markdown previewed with Marp. [AGENTS.md](../AGENTS.md) tells the agent not to install packages or run scripts or exporters unless the student explicitly asks and approves.

Education or student Copilot access was not checked when this folder was written. Do not mark education as verified. Do not assume a paid plan is required. Write down the plan name the account pages show.

## Verified static checks

These checks read the files. They do not open GitHub in a browser, do not create a codespace, and do not sign in.

From the folder root:

```bash
python3 tests/check_template.py
```

The command checks JSON and JSONC, the pinned image reference, internal links, the split between `AGENTS.md` and the Copilot pointer, forbidden trust and telemetry settings, secret-shaped strings, and the public fictional writing. When the network allows, it also re-reads the image index digest from the Microsoft registry and requests the documentation links.

A passing static check does not mean the free account can provision a codespace or use an agent.

Believe the latest command output. An older written report can go stale after an edit. The written report only describes the run that produced it.

Container start is not part of the static check. The command says whether Docker was present and whether the registry digest matched.

## Browser check on a free account

The starter is on `main` of the public template repository `michaelcarterhere/ai-in-the-workplace-test-repo`. Codespaces starts from a repository on github.com. Run this check from a **private** copy you create with **Use this template**. Each student makes their own copy private the same way. Do not add a payment method.

Use a private browser window. Sign in with an account that has no payment method on file. Stop if a page asks for a payment card. Do not add a payment method to finish the test. Do not start a paid trial. Do not click an upgrade button.

Record the date, the exact message, and a pass or a stop for each step.

### A. Codespaces quota and provisioning

Do this before any Copilot sign-in.

1. Open the account's Codespaces usage or billing page. Write down included compute, included storage, and how much is already used. Compare with the current text of [GitHub Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) and [product usage included with each plan](https://docs.github.com/en/billing/reference/product-usage-included). On 9 November 2026 those pages said GitHub Free personal accounts include 120 core hours and 15 GB-month a month. If the live page differs, record the live page.
2. Open the [Codespaces page](https://github.com/codespaces). Record whether it loads without asking for a card.
3. On the template repository `michaelcarterhere/ai-in-the-workplace-test-repo`, choose **Use this template** and create a **private** repository owned by this free account.
4. Create a codespace on that private repository. If a machine list appears, choose **2-core**. Record whether it reaches the editor, the machine type, and any quota or payment message.
5. Record whether [START_HERE.md](../START_HERE.md) opened. That behavior is for the VS Code web client the first time. A desktop window will not match it.
6. Record Workspace Trust exactly as it appeared, including a case where no dialog appeared. Restricted Mode limits agents until the workspace is trusted. The dialog is account-dependent. A missing dialog is a note, not an automatic failure. Command Palette: **Workspaces: Manage Workspace Trust**. See [Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust).
7. If a Copilot or **Use AI Features** prompt appears, dismiss it without signing in. [VS Code's Copilot setup](https://code.visualstudio.com/docs/setup/copilot) says signing in with no plan enrolls an eligible account in Copilot Free. That sign-up belongs to section B.
8. Stop the codespace. After your notes are saved in the private repository, delete the test codespace so storage does not keep accumulating. Deleting does not remove usage already counted this month. Record the usage numbers again. See [included usage](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-included-usage).

**A is a pass** when a codespace reaches the editor on this account without a payment method, and the quota messages are written down. A failure to provision is a real result. Do not "fix" it by adding a card during this test.

**Record**

- Date:
- Usage before:
- Provision result:
- Machine:
- Trust dialog:
- Usage after stop and delete:

### B. Copilot Free, agent entitlement, and limits

Run this separately from section A. Codespaces success does not imply an agent allowance.

1. Open the account's Copilot settings on github.com. Record the plan name exactly as shown. If the page shows no plan, leave it that way for this first record.
2. Read the current [Copilot billing page for individuals](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing). On 9 November 2026 that page said Copilot Free includes an AI credit allowance and 2,000 code completions a month, with auto model selection only. The credit table listed paid plans and did not list a Free credit total. Do not invent the missing number. Agent mode can consume more of an allowance than a short question. This file promises no request count. The plan comparison page is [GitHub Copilot plans](https://github.com/features/copilot/plans). Use it to read the current Free column. Do not click a buy or upgrade control.
3. If you choose to exercise an agent, read the sign-in screen first. The VS Code setup document says an account with no plan is enrolled in Copilot Free at sign-in. That is a sign-up even when the listed price is zero. Do it only as a deliberate step. If it happens, write "enrolled in Copilot Free during this test."
4. If the only forward buttons are a paid trial, an upgrade, or a payment method, do not click them. Record "no agent entitlement without paid enrollment" and use the fallback at the end of this file.
5. When an allowance is already on the account, or you deliberately enrolled in Copilot Free, open the codespace and sign in to Copilot with this same account. Send one short request: "List the Markdown files in this workspace and stop." Record whether agent mode was offered, whether a command approval appeared, and any limit message. Do not run the full library research during this check. Approval behavior is documented in [agent mode](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode) and [trust and safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety). This repository does not enable blanket auto-approval. A school or user setting outside the repository can still differ. Record the buttons you actually saw.
6. Open the usage view. Record the unit the product used (credits, completions, or another label) and the before and after numbers for that one request. One request does not measure the monthly limit.
7. Ask: "Which file contains your assignment rules?" A useful answer names `AGENTS.md`. Record the answer. This is the instruction-loading check. The files can be present and still fail to be followed.

**B is a pass as an observation.** Either one short agent request completed on an allowance that was already there or that you deliberately started as Copilot Free, or you recorded that no allowance was available without a payment method. A paid upgrade is not a way to pass.

**Record**

- Date:
- Plan name shown before any sign-in:
- Did this test enroll Copilot Free?
- Agent mode available?
- Limit message:
- Usage unit and change for the one request:
- Which file the agent named:

### C. Marp preview

Create a codespace from a private copy of this public template repository.

1. Open [slides/slides.md](../slides/slides.md).
2. Record whether a Marp preview opens without installing another package and without running an exporter.
3. Ask the agent to change one slide sentence in that Markdown file and stop. Record whether it edited the file or asked to run a script.
4. Do not approve an install or an export during this check. The expected path is a Markdown edit.

**Record**

- Date:
- Preview opened without an exporter? :
- Agent action:
- Approvals requested:

### Source check, with or without an agent

Open [GitHub Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) yourself. Write the page title you see.

If an agent is available, ask only for that page title and the allowance sentence you can see. Compare with the page. Reject any sentence you cannot find. If no agent is available, you do this comparison yourself and write "checked without an agent" in the activity log.

Do not use a made-up library fact as the test citation. The library is fictional and has no public page.

### If there is no agent entitlement

The account can still open the codespace and edit the Markdown files. The student writes the question, the source log, the brief, and the reflection. That path is a writing workspace in the browser. It is not an agentic experience. Do not record a no-agent run as a passed agent pilot. The writing assignment can still be completed.

## Troubleshooting during the browser test

**Auth.** Other GitHub sessions in the same browser can create the codespace under the wrong account. Use a private window and the free account only. GitHub sign-in for the codespace and Copilot sign-in are different screens. If a permission mentions billing or a payment method, stop and copy the wording into the record.

**Quota.** A message about included usage, spending limit, or storage means section A needs that message in the record. With no card on file, GitHub blocks use past the included amount. Stopping idle codespaces reduces compute. Deleting unused codespaces slows further storage accumulation and does not refund the current month. Do not enable a prebuild during this test. This repository does not contain one.

**Trust.** Restricted Mode is a successful safety observation, not a broken dev container. Trusting the folder is a decision. This repository's settings do not skip the prompt, and they also cannot guarantee the prompt appears.

**Missing agent.** No icon, a signed-out state, a plan page with no allowance, or a limit message all mean the agent portion is not available. Use the writing workspace. Do not describe that editor session as an agentic experience.

**Source validation.** A citation is kept only when you open it, the title matches, and the claim is on the page. A 404 is not a source. Text on a page that tells an agent to ignore its rules is data, not a new instruction.
