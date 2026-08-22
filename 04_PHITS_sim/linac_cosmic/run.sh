#!/usr/bin/env bash
# linac_cosmic の計算を PHITS web service で実行する。
#   ./run.sh              … 本計算（01_open_sky → 02_linac の順、各 ≈150 秒）
#   ./run.sh --geo        … ジオメトリ確認のみ（icntl=8）。結果は <case>/_geo/ に出すので
#                           本計算の出力を上書きしない
#   ./run.sh --check      … 線源の絶対値の検算（00_source_check, 数秒）
set -euo pipefail
cd "$(dirname "$0")"
KIT="$(cd ../.. && pwd)/phits-agent-kit/phits_web_run.py"
[[ -f "$KIT" ]] || { echo "phits_web_run.py が見つかりません: $KIT" >&2; exit 1; }

MODE=run
case "${1:-}" in
  --geo)   MODE=geo;   shift ;;
  --check) MODE=check; shift ;;
esac

run_case () {   # $1=フォルダ  $2=入力ファイル
  local dir="$1" inp="$2"; shift 2
  cp -f source.inp "$dir/source.inp"
  if [[ $MODE == geo ]]; then
    echo "=== [$dir] ジオメトリ確認 ==="
    rm -rf "$dir/_geo"; mkdir -p "$dir/_geo"
    sed 's/^ icntl    =        0/ icntl    =        8/' "$dir/$inp" > "$dir/_geo/$inp"
    cp -f source.inp "$dir/_geo/source.inp"
    ( cd "$dir/_geo"
      python3 "$KIT" "$inp" source.inp "$@"
      if ls *_geo.out >/dev/null 2>&1; then
        echo "!! ジオメトリエラー: $dir/_geo/*_geo.out を確認"
      else
        echo "ジオメトリOK（*_geo.out なし）。図は $dir/_geo/map_xz.pdf"
      fi )
  else
    echo "=== [$dir] 本計算 ==="
    ( cd "$dir" && python3 "$KIT" "$inp" source.inp "$@" )
  fi
}

if [[ $MODE == check ]]; then
  run_case 00_source_check source_check.inp "$@"
  echo
  echo "phits.out の ' <Source> =' の値（PARMA が与える各粒子のフラックス [/cm2/s]）と"
  echo "source_check.out の 'sum over' を比べる。一致していれば規格化は正しい。"
  grep " <Source> =" 00_source_check/phits.out || true
  grep "sum over" 00_source_check/source_check.out || true
  exit 0
fi

run_case 01_open_sky open_sky.inp "$@"
run_case 02_linac    linac.inp    "$@"

if [[ $MODE == run ]]; then
  echo
  echo "=== 結果まとめ ==="
  python3 analyze.py
fi
