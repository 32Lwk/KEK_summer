#!/bin/bash
# 追加分: テストホール（57 cm）と PS（480 cm）の部屋、KEKB の mu- の統計追加。終了済みのフォルダは飛ばす。
# 使い方: bash run_sites2.sh [並列数]
set -u
cd "$(dirname "$0")"
PAR=${1:-10}

jobs=()
for s in $(seq 25 48); do jobs+=("KEKB mum $((1000 + s)) 450"); done
for site in PS TH; do
  for s in $(seq 1 24); do jobs+=("$site mum $((1000 + s)) 450"); done
  for s in $(seq 1 8); do jobs+=("$site mup $((2000 + s)) 450"); done
done
for s in $(seq 1 8); do jobs+=("PS had $((3000 + s)) 1000"); done
for s in $(seq 1 8); do jobs+=("TH had $((3000 + s)) 700"); done

run_one() {
  set -- $1
  d="runs/$1/$2_s$3"
  if grep -q "finished normally" "$d/run.log" 2>/dev/null; then exit 0; fi
  rm -rf "$d"
  python3 make_site.py "$1" "$2" "$3" --maxcas "$4" > /dev/null
  cd "$d" || exit 1
  perl -e 'alarm shift; exec @ARGV' 420 \
    python3 ../../../../../phits-agent-kit/phits_web_run.py main.inp source.inp --version phits336 > run.log 2>&1
  echo "$d exit=$?"
}
export -f run_one

printf '%s\n' "${jobs[@]}" | xargs -P "$PAR" -I{} bash -c 'run_one "{}"'
