#!/bin/bash
# 応答関数: 19 エネルギー × 2 シードを Web PHITS に投げる。終了済みのフォルダは飛ばす。
# 使い方: bash run_resp.sh [並列数]
set -u
cd "$(dirname "$0")"
PAR=${1:-8}
ENERGIES="5.0e-9 2.53e-8 1.0e-7 1.0e-6 1.0e-5 1.0e-4 1.0e-3 1.0e-2 3.0e-2 0.1 0.3 1.0 2.0 5.0 10.0 20.0 50.0 200.0 1000.0"

jobs=()
i=0
for e in $ENERGIES; do
  i=$((i + 1))
  for s in 1 2; do jobs+=("E${i}_s${s} $e $((100 * i + s)) 150000"); done
done

run_one() {
  set -- $1
  d="runs/$1"
  if grep -q "finished normally" "$d/run.log" 2>/dev/null; then exit 0; fi
  python3 make_resp.py "$1" "$2" "$3" --maxcas "$4" > /dev/null
  cd "$d" || exit 1
  perl -e 'alarm shift; exec @ARGV' 400 \
    python3 ../../../../phits-agent-kit/phits_web_run.py main.inp --version phits336 > run.log 2>&1
  echo "$d exit=$?"
}
export -f run_one

printf '%s\n' "${jobs[@]}" | xargs -P "$PAR" -I{} bash -c 'run_one "{}"'
