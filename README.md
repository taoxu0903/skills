# This Repository's Skill Folders

| Folder | Description |
|--------|-------------|
| [custom-skills](./custom-skills/) | Skills created by the repo owner |
| [other-skills](./other-skills/) | Popular skills downloaded from third-party sources (see [other-skills/README.md](./other-skills/README.md) for sources) |
| [skills](./skills/) | Official Anthropic skills (forked). Synced with upstream regularly |

## Installing All Skills Locally

Run the provided install script to copy all three skill folders into the OS global agent skills directory (note: .agent folder is not well supported by GHCP so far so use .claude for now):

| OS | Target Directory |
|----|-----------------|
| macOS / Linux | `~/.claude/skills` |
| Windows | `%USERPROFILE%\.claude\skills` |

### macOS / Linux

`rsync` is pre-installed. Open a terminal in the repo root and run:

```bash
./install-skills.sh
```

If you get a permission error, make the script executable first:

```bash
chmod +x install-skills.sh
./install-skills.sh
```

### Windows

The script requires a Bash environment. Use one of the following options:

**Option 1 — Git Bash** (recommended, ships with [Git for Windows](https://git-scm.com/download/win)):

1. Open **Git Bash** in the repo root (right-click the folder → *Git Bash Here*).
2. Run:

```bash
./install-skills.sh
```

**Option 2 — WSL (Windows Subsystem for Linux)**:

1. Open a WSL terminal and navigate to the repo root (e.g. `/mnt/c/Users/<you>/Downloads/git/skills`).
2. Install `rsync` if needed: `sudo apt install rsync`
3. Run:

```bash
./install-skills.sh
```

> **Note:** After running on Windows, skills are installed to `%USERPROFILE%\.claude\skills` (e.g. `C:\Users\<you>\.claude\skills`).

---
