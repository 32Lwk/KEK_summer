#!/bin/bash
# 地点ごとの体系（PF, BT, KEKB, KEKBdry）を Web PHITS に投げる。終了済みのフォルダは飛ばす。
# KEKBdry のハドロンは寄与が小さいので計算しない（KEKB の値で代用）。
# 使い方: bash run_sites.sh [並列数]
set -u
cd "$(dirname "$0")"
PAR=${1:-10}

jobs=()
for site in KEKB BT PF KEKBdry; do
  for s in $(seq 1 24); do jobs+=("$site mum $((1000 + s)) 450"); done
  for s in $(seq 1 12); do jobs+=("$site mup $((2000 + s)) 450"); done
done
for s in $(seq 1 8); do jobs+=("PF had $((3000 + s)) 700"); done
for s in $(seq 1 8); do jobs+=("BT had $((3000 + s)) 1000"); done
for s in $(seq 1 8); do jobs+=("KEKB had $((3000 + s)) 1500"); done

run_one() {
  set -- $1
  d="runs/$1/$2_s$3"
  if grep -q "finished normally" "$d/run.log" 2>/dev/null; then exit 0; fi
  python3 make_site.py "$1" "$2" "$3" --maxcas "$4" > /dev/null
  cd "$d" || exit 1
  perl -e 'alarm shift; exec @ARGV' 420 \
    python3 ../../../../../phits-agent-kit/phits_web_run.py main.inp source.inp --version phits336 > run.log 2>&1
  echo "$d exit=$?"
}
export -f run_one

printf '%s\n' "${jobs[@]}" | xargs -P "$PAR" -I{} bash -c 'run_one "{}"'
