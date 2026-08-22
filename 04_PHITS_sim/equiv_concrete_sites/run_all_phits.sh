#!/usr/bin/env bash
# d1 / d2 / D1 / D2 全地点を Web PHITS で順次実行（3分制限内・失敗時も続行・完走済みスキップ）
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
RUNNER="$ROOT/../../phits-agent-kit/phits_web_run.py"
SOURCE="$ROOT/source_ceiling.inp"
LOG="$ROOT/run_all_phits.log"

python3 "$ROOT/build_ceiling_main.py" >> "$LOG" 2>&1

job_ok() {
  local phits="$1/phits.out"
  local de="$1/de.out"
  [ -f "$phits" ] || return 1
  [ -f "$de" ] || return 1
  grep -q "stop number =   802\|stop number =   601" "$phits" && return 1
  grep -qE "Program is finished|^ END " "$phits" || return 1
  return 0
}

FAILED=0
SKIPPED=0
DONE=0
TOTAL=0
for det in d1 d2 D1 D2; do
  subdir=$(python3 -c "from detector_specs import DETECTOR_SUBDIR; print(DETECTOR_SUBDIR['$det'])")
  for site in 00_ground 01_PF 02_linac 03_BT 04_KEKB; do
    TOTAL=$((TOTAL + 1))
    dir="$ROOT/$subdir/$site"
    if job_ok "$dir"; then
      echo "SKIP (OK): $det/$site" | tee -a "$LOG"
      SKIPPED=$((SKIPPED + 1))
      continue
    fi
    echo "=== $det/$site ($subdir) ===" | tee -a "$LOG"
    rm -f "$dir/.phits_web_session" "$dir/.phits_web_result.zip"
    if (cd "$dir" && python3 "$RUNNER" main.inp "$SOURCE" --version phits336 --new-session 2>&1 | tee -a "$LOG"); then
      if job_ok "$dir"; then
        DONE=$((DONE + 1))
        echo "OK: $det/$site" | tee -a "$LOG"
      else
        FAILED=$((FAILED + 1))
        echo "FAILED (bad exit): $det/$site" | tee -a "$LOG"
      fi
    else
      FAILED=$((FAILED + 1))
      echo "FAILED: $det/$site" | tee -a "$LOG"
    fi
  done
done

for det in d1 d2 D1 D2; do
  python3 "$ROOT/summarize_relative.py" --detector "$det" 2>&1 | tee -a "$LOG" || true
  python3 "$ROOT/plot_3d_sites.py" --detector "$det" 2>&1 | tee -a "$LOG" || true
done

echo "summary: total=$TOTAL skipped=$SKIPPED new_ok=$DONE failed=$FAILED" | tee -a "$LOG"
[ "$FAILED" -eq 0 ] || exit 1
