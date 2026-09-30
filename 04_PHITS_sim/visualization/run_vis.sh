#!/bin/bash
# 断面図用の計算をローカルの PHITS で並列に流す。終了済みのフォルダは飛ばす。
# 使い方: bash run_vis.sh [並列数]
set -u
cd "$(dirname "$0")"
PAR=${1:-12}
export EXE=/Users/yuto/PHITS335/phits/bin/phits335_mac.exe

jobs=()
for s in $(seq 11 22); do jobs+=("site PS mum $((100 + s)) 5000" "site PF mum $((200 + s)) 5000"); done
for s in 1 2; do jobs+=("site PS had $((300 + s)) 20000" "site PF had $((400 + s)) 20000"); done
jobs+=("det 1.0 501 1000000" "det 2.53e-8 502 1000000")

run_one() {
  set -- $1
  if [ "$1" = site ]; then
    d=$(python3 make_vis.py site "$2" "$3" "$4" --maxcas "$5")
  else
    d=$(python3 make_vis.py det "$2" "$3" --maxcas "$4")
  fi
  cd "$d" || exit 1
  if grep -q "total cpu time" phits.out 2>/dev/null; then exit 0; fi
  echo file=main.inp | "$EXE" > run.log 2>&1
  echo "$d done"
}
export -f run_one

printf '%s\n' "${jobs[@]}" | xargs -P "$PAR" -I{} bash -c 'run_one "{}"'
