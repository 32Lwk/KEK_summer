#!/usr/bin/env bash
# d1 / d2 / D1 / D2 全地点を Web PHITS で順次実行
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
RUNNER="$ROOT/../../phits-agent-kit/phits_web_run.py"
SOURCE="$ROOT/source_ceiling.inp"

python3 "$ROOT/build_ceiling_main.py"

for det in d1 d2 D1 D2; do
  subdir=$(python3 -c "from detector_specs import DETECTOR_SUBDIR; print(DETECTOR_SUBDIR['$det'])")
  for site in 00_ground 01_PF 02_linac 03_BT 04_KEKB; do
    dir="$ROOT/$subdir/$site"
    echo "=== $det/$site ($subdir) ==="
    (cd "$dir" && python3 "$RUNNER" main.inp "$SOURCE" --version phits336 --new-session)
  done
done

for det in d1 d2 D1 D2; do
  python3 "$ROOT/summarize_relative.py" --detector "$det"
  python3 "$ROOT/plot_3d_sites.py" --detector "$det"
done

echo "done."
