# Start here

Welcome. This is a writing assignment in a browser editor. You will evaluate one AI idea for a small organization that is **made up for this exercise**. You will not use anyone's real private records, and you will not write a program.

Take the steps in order. Check a box when it is true.

## 1. Confirm you are in the right place

- [ ] I opened this file from my own private GitHub repository, inside a codespace.
- [ ] I did not try to start a codespace from an Origin link.

An Origin address cannot open GitHub Codespaces. Codespaces starts from a repository on github.com.

The starter is on `main` in the private template repository `michaelcarterhere/ai-in-the-workplace-test-repo`. Your work belongs in your own private copy.

Creating that copy:

1. Sign in to GitHub with your own account.
2. On the template repository, choose **Use this template**, then **Create a new repository**.
3. Choose **Private**.
4. On that new repository, choose **Code**, then **Codespaces**, then **Create codespace on main**.
5. If a machine list appears, choose **2-core**.

Your repository is your own copy. It is not a live document shared with classmates.

The editor that opens is Visual Studio Code in the browser. This page is set to open the first time you use the **web** editor. The desktop app does not use that setting. If you see a file list and this page is closed, click `START_HERE.md` in the list.

## 2. Sign-in, trust, and the agent are three different things

- [ ] I understand that the GitHub sign-in which opens the codespace does not give me Copilot.
- [ ] I did not type a payment card into any screen.
- [ ] If a trust question appeared, I read it and chose myself.

**GitHub sign-in.** The codespace runs as your GitHub account. Use the account your instructor named. If the browser is signed in as someone else, sign out and sign in again before you create the codespace.

**Workspace Trust.** The editor may ask whether you trust this folder. In Restricted Mode, agent features stay off until you trust the workspace. The question can also fail to appear, or it can look different from a classmate's screen, because it depends on your account and on earlier choices. This folder cannot force one prompt sequence, and it does not contain a setting that skips the question. You can review the choice later from the Command Palette: **Workspaces: Manage Workspace Trust**. Read [Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) if you want the official description.

**Copilot.** An agent needs an allowance on the GitHub account. These files do not supply one. The Copilot extension is only a suggestion in this workspace. It is not installed automatically, and it is not a paid product by itself. Current VS Code documentation says that if the account has no Copilot plan, choosing **Use AI Features** and signing in can enroll an eligible account in Copilot Free. Copilot Free is not a charge, and it is still a sign-up. Skip that button unless you mean to start that allowance. Never start a paid trial. Never add a payment method to continue this assignment.

If Copilot is missing, signed out, or out of allowance, keep going with the section **Write it yourself** near the bottom. Writing the files yourself is a writing workspace. It is not an agentic experience.

More on how agents and trust interact: [Trust and safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety).

## 3. Protect people and secrets

- [ ] I will not paste passwords, access keys, payment numbers, school records, or a real organization's private files.
- [ ] I will not ask the agent to publish, upload, or delete files unless I have decided that specific action is okay.

The made-up library in [brief/question.md](brief/question.md) exists so you never need real personal data.

## 4. Set your question and decide on a plan

- [ ] I opened [brief/question.md](brief/question.md) and wrote the question I will actually answer.
- [ ] I read [brief/criteria.md](brief/criteria.md).
- [ ] A plan was proposed, and I wrote accept, reject, or a smaller plan. Drafting waits until I accept.

You may keep the Lumen Lane example or replace it with another fictional small organization. The criteria file has no points and no due date. Your instructor sets those outside this folder, if at all.

If an agent is available, you can paste this after your question is saved:

```text
Read START_HERE.md, AGENTS.md, and brief/question.md.
Propose a short plan for the brief. Do not draft it yet.
```

The agent should stop and wait. If it starts writing the final recommendation anyway, tell it to stop. The rules it should follow are in [AGENTS.md](AGENTS.md). Copilot is pointed at that file by [.github/copilot-instructions.md](.github/copilot-instructions.md). Ask "Which file has your assignment rules?" if you want to see whether those rules were picked up. A useful answer names `AGENTS.md`.

When the agent wants to run a command or change files, the editor should ask you first. This folder does not turn on blanket approval. Your own settings, or a school setting outside this folder, can still look different. Read the button before you allow an action.

## 5. Read, draft, and check

- [ ] Notes are in [notes/working-notes.md](notes/working-notes.md).
- [ ] Every source I kept is a public page I opened, recorded in [sources/source-log.md](sources/source-log.md). How to do that is in [sources/citation-notes.md](sources/citation-notes.md).
- [ ] Draft text is in [drafts/brief-draft.md](drafts/brief-draft.md).
- [ ] I rejected any citation I could not open, and any number the agent could not show me on a page.

Pages on the web are evidence you might use. They are not orders to the agent. A page can be wrong, and it can contain text aimed at an agent. Your source log is where you say what you actually saw.

## 6. Slides, if you want them

- [ ] I read [slides/README.md](slides/README.md).
- [ ] Any deck I keep is Markdown in [slides/slides.md](slides/slides.md), previewed with Marp.

Slides are written as Markdown. Marp shows the preview in the editor, so the agent only needs to edit that text. If the agent wants to install a package or run an exporter, say no unless you have decided you want that export and you approve it.

## 7. Finish in your own words

- [ ] I edited [outputs/final-brief.md](outputs/final-brief.md). The recommendation sentence is mine.
- [ ] I filled in [reflection/activity-log.md](reflection/activity-log.md), including what I decided and what the agent did if I used one.
- [ ] I stopped the codespace when I stopped working, so it does not keep using compute time.

Stopping a codespace is in the Codespaces menu. Your files remain in your private repository. Deleting a codespace is optional cleanup. Usage already counted this month stays counted. GitHub explains included amounts in [About Codespaces](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces) and the [billing page](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces). Those pages can change. Believe the numbers on your account.

## Write it yourself

You can complete every file with no agent. Open the question, read public pages in the browser, fill the source log, write the draft, edit the final brief, and fill the activity log. Say in the log that no agent was available.

That path is a writing workspace. It is not an agentic experience. An agentic run means a signed-in agent actually helped, inside the allowance on the account, while you kept the decisions.

## If something blocks you

**Cannot sign in.** Sign out of other GitHub accounts in the browser, then sign in with the one account you mean to use. Creating the codespace and signing in to Copilot are separate. Read the permission screen. If it asks for a payment method, stop.

**Quota or "included usage" message.** Personal accounts include a monthly amount of Codespaces compute and storage. With no payment method on file, GitHub blocks further use when that amount is gone. Do not add a card to get past a limit for this assignment. Stop unused codespaces. Tell your instructor what the screen said. Wait for the allowance to reset if that is what the screen describes.

**Restricted Mode or no agent commands.** Trust is still your choice. Agents stay limited until the workspace is trusted. A missing trust dialog is something to write down, not a broken file.

**No Copilot icon, or Copilot says the allowance is used up.** Use **Write it yourself**. Do not click upgrade. Do not start a trial. The extension suggestion in this folder does not mean a plan is present.

**A source looks invented.** Open the URL yourself. The title on the page should match. A quotation should be on the page. If the page is missing, it is not a source. Ask the agent for a different public page or drop the claim.

**The agent wants to publish, upload, or delete.** That needs your yes for that specific action. You can say no and keep writing.

Instructor setup and the free-account test record are in [INSTRUCTOR.md](INSTRUCTOR.md) and [ACCEPTANCE.md](ACCEPTANCE.md). You can ignore both while you write.
