#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

run_step() {
  echo "[release-smoke] running: $*"
  "$@"
}

run_step python3 -m kora --help
run_step python3 -m kora examples list
run_step python3 -m kora run hello_kora
run_step python3 -m kora run retry_demo
run_step python3 -m kora run direct_vs_kora -- --offline
run_step python3 -m kora telemetry --input docs/reports/sample_telemetry_input.json

echo "[release-smoke] completed"
