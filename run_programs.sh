#!/usr/bin/env bash
set -euo pipefail

# Simple runner to execute hello_world.py from the repository root
cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then
    # Run hello_world.py
    python3 hello_world.py

    # Run branch1.py if it exists
    if [ -f "branch1.py" ]; then
        python3 branch1.py
    else
        echo "branch1.py not found, skipping." >&2
    fi
else
    echo "python3 not found in PATH. Please install Python 3 or adjust the script." >&2
    exit 1
fi
