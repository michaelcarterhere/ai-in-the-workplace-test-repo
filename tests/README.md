# Static checks

This folder is for the instructor or the person maintaining the template. Students writing the brief can ignore it. The check does not install course software, create a codespace, sign in, or enroll a plan.

From the repository root:

```bash
python3 tests/check_template.py
```

The command exits 0 when the static checks pass. It prints one line when Docker is absent, which is a disclosed limitation, not a failed file check. A live registry or documentation request can fail when the network is blocked. That failure is real and should be rerun from a network that can reach Microsoft and GitHub.

[STATIC_CHECK_REPORT.md](STATIC_CHECK_REPORT.md) records one run. The report that arrived with the starter ZIP is historical. Believe the latest command output. Replace the written report after you rerun the command if you need the file to match.

What the command does not do:

- It does not sign in as the unpaid test account.
- It does not prove Codespaces quota or Copilot Free limits.
- It does not start the container when Docker is missing.

The browser record for that account is [../ACCEPTANCE.md](../ACCEPTANCE.md).
