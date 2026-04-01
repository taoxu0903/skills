#!/usr/bin/env bash
# install-skills.sh
# Copies all skills from custom-skills/, other-skills/, and skills/ into the
# OS global agent skills folder (~/.claude/skills on macOS/Linux,
# %USERPROFILE%\.claude\skills on Windows via Git Bash/MSYS2/Cygwin).

set -euo pipefail

# ---------------------------------------------------------------------------
# Resolve target directory based on OS
# ---------------------------------------------------------------------------
OS="$(uname -s 2>/dev/null || echo "unknown")"

case "$OS" in
    Darwin*)
        TARGET_DIR="$HOME/.claude/skills"
        ;;
    Linux*)
        TARGET_DIR="$HOME/.claude/skills"
        ;;
    MINGW*|MSYS*|CYGWIN*)
        # Git Bash / MSYS2 / Cygwin on Windows
        TARGET_DIR="${USERPROFILE:-$HOME}/.claude/skills"
        # Normalise backslashes to forward slashes for bash
        TARGET_DIR="${TARGET_DIR//\\//}"
        ;;
    *)
        echo "ERROR: Unsupported OS '$OS'. Exiting." >&2
        exit 1
        ;;
esac

# ---------------------------------------------------------------------------
# Resolve the directory that contains this script (source root)
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Source root : $SCRIPT_DIR"
echo "Target      : $TARGET_DIR"
echo ""

# ---------------------------------------------------------------------------
# Create target directory if it doesn't exist
# ---------------------------------------------------------------------------
mkdir -p "$TARGET_DIR"

# ---------------------------------------------------------------------------
# Copy each source folder's contents into the target
# Each of the three folders (custom-skills, other-skills, skills) contains
# individual skill sub-directories; we copy those sub-directories directly
# into $TARGET_DIR so skills are available as $TARGET_DIR/<skill-name>/.
# ---------------------------------------------------------------------------
SOURCE_FOLDERS=("custom-skills" "other-skills" "skills")
copied=0
skipped=0

# ---------------------------------------------------------------------------
# Portable recursive copy: prefer rsync (macOS/Linux) and fall back to cp
# (Git Bash / MSYS2 / Cygwin on Windows where rsync is not always installed).
# ---------------------------------------------------------------------------
copy_dir() {
    local src="$1" dst="$2"
    if command -v rsync &>/dev/null; then
        # -a : archive (recursive + preserve permissions/times)
        # --links          : copy symlinks as symlinks
        # --ignore-errors  : skip unreadable files instead of aborting
        rsync -a --links --ignore-errors "$src/" "$dst/"
    else
        # cp fallback — works on Git Bash / MSYS2 / Cygwin without rsync
        cp -r "$src/." "$dst/"
    fi
}

for folder in "${SOURCE_FOLDERS[@]}"; do
    src="$SCRIPT_DIR/$folder"

    if [ ! -d "$src" ]; then
        echo "  [SKIP] '$folder' not found — skipping."
        (( skipped++ )) || true
        continue
    fi

    echo "  [COPY] $folder/ -> $TARGET_DIR/"
    copy_dir "$src" "$TARGET_DIR"
    (( copied++ )) || true
done

echo ""
echo "Done. Copied $copied folder(s), skipped $skipped folder(s)."
echo "Skills are now available at: $TARGET_DIR"
