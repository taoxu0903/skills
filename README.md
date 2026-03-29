# This Repository's Skill Folders

| Folder | Description |
|--------|-------------|
| [custom-skills](./custom-skills/) | Skills created by the repo owner |
| [other-skills](./other-skills/) | Popular skills downloaded from third-party sources (see [other-skills/README.md](./other-skills/README.md) for sources) |
| [skills](./skills/) | Official Anthropic skills (forked). Synced with upstream regularly |

## Installing All Skills Locally

Run the provided install script to copy all three skill folders into the OS global agent skills directory:

| OS | Target Directory |
|----|-----------------|
| macOS / Linux | `~/.agent/skills` |
| Windows (Git Bash / MSYS2 / Cygwin) | `%USERPROFILE%\.agent\skills` |

```bash
./install-skills.sh
```

The script requires `rsync` (pre-installed on macOS and most Linux distributions). On Windows, run it from Git Bash.

---
