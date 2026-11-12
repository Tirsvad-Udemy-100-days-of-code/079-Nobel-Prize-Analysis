#!/usr/bin/env bash
# Scan the tracked files with opengrep before pushing.
# Usage:  bash scripts/scan.sh
# Env:    OPENGREP  path to the binary (default ~/.opengrep/cli/latest/opengrep.exe)
# Exit:   0 no finding; non-zero a finding or a tool error
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
opengrep="${OPENGREP:-$HOME/.opengrep/cli/latest/opengrep.exe}"
exec "$opengrep" scan --config p/python --config p/secrets --error src tests scripts docs
