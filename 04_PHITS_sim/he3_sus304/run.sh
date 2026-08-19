#!/usr/bin/env bash
# He-3 / SUS304 を Web PHITS で実行し、結果をこのフォルダへ落とす。
set -euo pipefail
cd "$(dirname "$0")"
KIT="$(cd ../.. && pwd)/phits-agent-kit/phits_web_run.py"
if [[ ! -f "$KIT" ]]; then
  echo "phits_web_run.py が見つかりません: $KIT" >&2
  exit 1
fi
exec python3 "$KIT" he3_sus304.inp "$@"
