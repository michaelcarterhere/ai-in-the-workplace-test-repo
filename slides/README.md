# Slides

Slides in this workspace are Markdown. [Marp for VS Code](https://github.com/marp-team/marp-vscode) previews that Markdown in the editor. You do not need a separate slide program, and you do not need to export a PowerPoint file to finish.

## How to preview

1. Open [slides.md](slides.md).
2. The file starts with `marp: true`. That tells Marp this Markdown is a deck.
3. Open the preview from the Marp icon in the editor toolbar, or from the Command Palette: **Markdown: Open Preview to the Side**.

A line that contains only `---` starts the next slide.

## What to ask an agent

Ask the agent to edit `slides.md`. The preview reads that text. The agent should not install packages or run an exporter to make the deck.

Exporting to PDF, PowerPoint, HTML, or images can ask you to approve scripts, and it needs a browser that this workspace does not install. If you explicitly want an export, you approve that yourself. Until then, the Markdown file is the deck.

The story in the starter deck is fictional. It is the same made-up library as the brief. Replace the slides with your own words.

HTML inside slides is turned off in this workspace. Write the slides in Markdown.
