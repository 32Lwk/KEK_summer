# Lecture: therapy/RidgeFilter

SOURCE_FOLDER: D:/NEAgit/lecture/therapy/RidgeFilter
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: RidgeFilter
LECTURE_PATH_INDEX: lecture/therapy/RidgeFilter
PPTX_FILES: RidgeFilter.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: phits, ridge, ridge-cell, ridge-cell-proton, ridge-surface
SECTION_KEYWORDS: (none)

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/therapy/RidgeFilter
LECTURE_PATH_INDEX: lecture/therapy/RidgeFilter
PPTX_FILES: RidgeFilter.pptx
INPUT_DIR_COUNT: 0
MAIN_INPUT_COUNT: 7
SLIDE_COUNT: 14
EXERCISE_SLIDE_COUNT: 0
BONUS_INPUT_COUNT: 0
BONUS_TEXT_COUNT: 0

[MAIN_INPUT_FILES]
- adjustment/phits.inp
- adjustment/ridge-cell.inp
- adjustment/ridge-surface.inp
- ridge-cell-proton.inp
- ridge-cell.inp
- ridge-surface.inp
- ridge.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: リッジフィルタ作り方メモ
- SLIDE 02: リッジフィルタとは？
- SLIDE 03: 基本設計
- SLIDE 04: 体系の確認
- SLIDE 05: 基本ユニットを作る
- SLIDE 06: リッジフィルタ全体を作る
- SLIDE 07: リッジフィルタを置く
- SLIDE 08: 線量・深さ分布の確認
- SLIDE 09: 陽子用リッジフィルタ特有*の設計
- SLIDE 10: 陽子用フィルタの基本ユニットを作る①
- SLIDE 11: 陽子用フィルタの基本ユニットを作る②
- SLIDE 12: 線量・深さ分布の比較
- SLIDE 13: 実際のリッジフィルタに適用した例
- SLIDE 14: 実際のリッジフィルタの構造が分からない場合はadjustmentフォルダを参照

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: adjustment/phits.inp
FILE: adjustment/ridge-cell.inp
FILE: adjustment/ridge-surface.inp
FILE: ridge-cell-proton.inp
FILE: ridge-cell.inp
FILE: ridge-surface.inp
FILE: ridge.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
リッジフィルタ作り方メモ
title
2014年8月改訂
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
リッジフィルタとは？
散乱体
リッジ
フィルタ
陽子線
もしくは
粒子線
コリメータ
http://www.info.pmda.go.jp/ygo/pack/650051/22200BZX00124000_A_04_01/
くさび形の金属フィルタで陽子線や重粒子線のエネルギーを段階的に変化させ，様々な飛程が混在したビームを作ることにより，腫瘍部での治療効果が一定となるようにする
患者

--- SLIDE 03 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
基本設計
深さの異なる直方体の集合体で１つのユニットを表現する
Lattice機能を使ってユニットを並べて全体を表現する

--- SLIDE 04 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
体系の確認
ridge.inp
file=ridge.inp
[ T i t l e ]
Sample input for Ridge Filter
...

[ C e l l ]
infl: {ridge-cell.inp}
$infl: {ridge-cell-proton.inp}
…

[ S u r f a c e ]
infl: {ridge-surface.inp}
…
ridge-cell.inp
c  Cell of Ridge Filter
c  unit rigde filter, Air Regions
 1000      4 -1.2100000E-03  200 -201 102 -103 104      u=1001
 1001      4 -1.2100000E-03  201 -202 102 -103 104 -301  u=1001
…
ridge-surface.inp
c  Ridge Filter Area
set: c1[-50.0] $ Z position of ridge filter
 100          px   -10.0
…
MENTIONED_INPUT_NAMES: ridge-cell-proton.inp, ridge-cell.inp, ridge-surface.inp, ridge.inp

--- SLIDE 05 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
基本ユニットを作る
Universe 1001の中に作る (u=1001)
ridge-cell.inp
$  unit ridge filter, Gap Region
 1100 4 -1.21E-03  200 -201 102 -103      u=1001
$  unit ridge filete, Air Regions
 1101 4 -1.21E-03  201 -202 102 -103 -301  u=1001
 1102 4 -1.21E-03  202 -203 102 -103 -302  u=1001
…
$ Unit Ridge Filger, Al region
 1201 2 -2.70      201 -202 102 -103  301  u=1001
 1202 2 -2.70      202 -203 102 -103  302  u=1001
 1203 2 -2.70      203 -204 102 -103  303  u=1001
…
1100
1101
1201
Air
Al
Cell 1100はリッジフィルタのGap領域
Cell 1101 ~ 1113は空気の領域
Cell 1201 ~ 1213はアルミの領域
Surface 200 ~ 214はリッジフィルタの幅を表現
Surface 301 ~ 307はリッジフィルタの高さを表現
Univserse 1001
MENTIONED_INPUT_NAMES: ridge-cell.inp

--- SLIDE 06 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
リッジフィルタ全体を作る
Lattice Universe 1002を定義し，
その中に基本ユニット（universe 1001)を並べる
ridge-cell.inp
2001 0 -214 200 -103 102 -105 104  lat=1  u=1002
      fill= -5:4 0:0 0:0
      1001 1001 1001 1001 1001 1001 1001 1001 1001 1001
…
Universe1002は，直方体のLattice空間であると定義
基本Lattice（中央のリッジフィルタ）を定義
リッジフィルタを並べる個数（x軸方向に-5～+4まで10個）を指定
Univserse 1002
MENTIONED_INPUT_NAMES: ridge-cell.inp

--- SLIDE 07 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
リッジフィルタを置く
メイン空間の一部にリッジフィルタ(universe 1002)を埋め込む
ridge.inp
[ C e l l ]
infl: {ridge-cell.inp} $ Surfaces for Ridge Filter
 1  3 -19.6   1 -2 -11                   $ Scatterer
 2  2 -2.7    3 -4  11 -12               $ Collimator
 3  1 -1.0    5 -6 -11                   $ Target
 4  0         1100 -1101 1102 -1103 1104 -1105 fill=1002
98  4 -1.21e-3     #1 #2 #3 #4  -999     $ Air
99 -1         999                        $ Outer region
…
リッジフィルタの外枠を定義し，universe 1002で満たす（fill = 1002)
その際，物質はvoid (=0)とする。その際、外枠は実際のリッジフィルタよりも少しだけ小さくする*
Cell 4: リッジフィルタの領域
（よほど分解能を良くしない限りきれいには表示されない）
*回転させた際に、桁落ちの問題で発生するlost particleを防ぐため
MENTIONED_INPUT_NAMES: ridge-cell.inp, ridge.inp

--- SLIDE 08 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
線量・深さ分布の確認
ridge.inp
[ P a r a m e t e r s ]
 icntl    =           0
 maxcas   =        5000
 maxbch   =          10
...
delt0    = 1.000000000E-02
e-mode   =           2
 nedisp   =           1
 nspred   =           2
 ascat1   =  13.6000000
 ascat2   = 8.800000000E-02
…
[ T - Deposit ]
    title = depth-dose
     mesh =  r-z
   r-type =    2
     rmin =   0.000000
     rmax =   1.000000
       nr =    1
...
dose.eps
リッジフィルタの詳しい構造は非公開のため
このサンプルでは正しいSOBPになっていない
delt0は，散乱体の1/10の厚さに設定する。
それ以外の基本的なパラメータ設定は
\recommendation\particletherapy.inpと同じ
タリー半径により線量-深さ分布が大きく変化する
ので注意が必要
MENTIONED_INPUT_NAMES: ridge.inp

--- SLIDE 09 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
陽子用リッジフィルタ特有*の設計
陽子線の場合，クーロン角度分散の影響が大きいため，
アルミを細かく分割し，散乱によりフィルタの外に出ていないか
頻繁にチェックする必要がある
無限媒質中での飛跡
本当の飛跡
Al
Air
PHITSの飛跡
無限媒質中での飛跡
本当の飛跡
Al
Air
PHITSの飛跡
領域を区切らない場合
領域を細かく区切った場合
PHITSの飛跡
フィルタ内を長距離飛んでしまい，飛程が短い粒子が増える
領域境界でフィルタ内外を判定するため，途中で抜ける粒子を正しく考慮可能

--- SLIDE 10 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
陽子用フィルタの基本ユニットを作る①
アルミを0.05cm間隔に細かく区切ったuniverse 1003を作る
ridge-cell-proton.inp
2003  0  100 -101 102 -103 -106 104 lat=1 u=1003  $ Universe for Lattice Al
      fill = 0:0 0:0 0:99
      1004 1004 1004 1004 1004 1004 1004 1004 1004 1004
…
2004  2  -2.70 -999 u=1004 $ Universe filled with Al in whole ridge filter area
Universe1004は，全てアルミで満たされた世界
Universe1003は，z方向に0.05cm間隔で100等分されたアルミのLattice領域
…
 104          pz    c1
 105          pz    c1+5.0
 106          pz    c1+0.05
…
ridge-surface.inp
MENTIONED_INPUT_NAMES: ridge-cell-proton.inp, ridge-surface.inp

--- SLIDE 11 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
陽子用フィルタの基本ユニットを作る②
リッジフィルタの領域をアルミの代わりに
Universe 1003（100等分したアルミ）で満たす
ridge-cell.inp
…
$ Unit Ridge Filger, Al region
 1201 2 -2.70      201 -202 102 -103  301  u=1001
 1202 2 -2.70      202 -203 102 -103  302  u=1001
…
Univserse 1001
ridge-cell-proton.inp
…
$ Unit Ridge Filger, Al region
 1201 0  201 -202 102 -103  301  u=1001  fill=1003
 1202 0  202 -203 102 -103  302  u=1001  fill=1003
…
Alの部分がZ方向に分割されている
Air
Al
Air
Al
MENTIONED_INPUT_NAMES: ridge-cell-proton.inp, ridge-cell.inp

--- SLIDE 12 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
線量・深さ分布の比較
ridge.inp
...
[ C e l l ]
infl: {ridge-cell.inp}
$infl: {ridge-cell-proton.inp}
…
フィルタを区切らない場合
...
[ C e l l ]
$infl: {ridge-cell.inp}
infl: {ridge-cell-proton.inp}
…
フィルタを区切った場合
ridge.inp
dose.eps
dose.eps
長飛程の陽子が少し増えた
MENTIONED_INPUT_NAMES: ridge-cell-proton.inp, ridge-cell.inp, ridge.inp

--- SLIDE 13 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
実際のリッジフィルタに適用した例
フィルタを区切らない場合
フィルタを区切った場合
フィルタを区切ることにより，より平坦なSOBP領域を作ることができる
Courtesy of Dr. Matsumoto @ NIRS

--- SLIDE 14 ---
PPTX_FILE: RidgeFilter.pptx
SLIDE_TEXT:
実際のリッジフィルタの構造が分からない場合はadjustmentフォルダを参照

[BONUS_INPUT_FILES]
NOTE: None

[BONUS_TEXT_FILES]
NOTE: None
