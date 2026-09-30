#!/bin/bash
# 全ケースを乱数シード違いで Web PHITS に投げる（Web 版は 1 ジョブ 3 分で打ち切られるため分割）。
# 終了済みのフォルダは飛ばすので、時間切れのランは再実行するだけでよい。
# 使い方: bash run_all.sh [並列数]
set -u
cd "$(dirname "$0")"
PAR=${1:-10}

jobs=()
for s in $(seq 11 30); do jobs+=("mum $s 800"); done
for s in $(seq 31 42); do jobs+=("mup $s 800"); done
for s in $(seq 51 56); do jobs+=("had $s 1700"); done
for s in $(seq 61 70); do jobs+=("mumT $s 800"); done
for s in $(seq 71 76); do jobs+=("hadT $s 700"); done

run_one() {
  set -- $1
  d="runs/$1_s$2"
  if grep -q "finished normally" "$d/run.log" 2>/dev/null; then exit 0; fi
  python3 make_inputs.py "$1" "$2" --maxcas "$3" --maxbch 1 > /dev/null
  cd "$d" || exit 1
  # 応答が途絶えたジョブで全体が止まらないよう 7 分で打ち切る
  perl -e 'alarm shift; exec @ARGV' 420 \
    python3 ../../../../phits-agent-kit/phits_web_run.py main.inp source.inp --version phits336 > run.log 2>&1
  echo "$d exit=$?"
}
export -f run_one

printf '%s\n' "${jobs[@]}" | xargs -P "$PAR" -I{} bash -c 'run_one "{}"'
