#!/usr/bin/env bash
set -euo pipefail

# Simple runner to execute hello_world.py from the repository root
cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then
    python3 hello_world.py
else
    echo "python3 not found in PATH. Please install Python 3 or adjust the script." >&2
    exit 1
fi
