# Lecture: advanced/paraview

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/paraview
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: paraview
LECTURE_PATH_INDEX: lecture/advanced/paraview
PPTX_FILES: phits-paraview-en.pptx, phits-paraview-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: paraview, paraview-final, paraview_sample
SECTION_KEYWORDS: (none)

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/paraview
LECTURE_PATH_INDEX: lecture/advanced/paraview
PPTX_FILES: phits-paraview-en.pptx, phits-paraview-jp.pptx
INPUT_DIR_COUNT: 0
MAIN_INPUT_COUNT: 3
SLIDE_COUNT: 58
EXERCISE_SLIDE_COUNT: 0
BONUS_INPUT_COUNT: 0
BONUS_TEXT_COUNT: 0

[MAIN_INPUT_FILES]
- old/paraview-final.inp
- old/paraview.inp
- paraview_sample.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Visualization of PHITS tally results using ParaView
- SLIDE 02: Table of Contents
- SLIDE 03: Check and run paraview_sample.inp
- SLIDE 04: Tally Setting
- SLIDE 05: Table of Contents
- SLIDE 06: Installation of ParaView
- SLIDE 07: Launch ParaView
- SLIDE 08: Main Screen of ParaView
- SLIDE 09: Read VTK file
- SLIDE 10: Visualize Geometry
- SLIDE 11: Table of Contents
- SLIDE 12: Set Slice to Show Photon Flux
- SLIDE 13: Visualize Flux on the Slice
- SLIDE 14: Set the Range of the Color Map
- SLIDE 15: (Supplement) Switching cross sections and changing colors
- SLIDE 16: Scroll 2D Flux ①
- SLIDE 17: Select “Slice1” & “Slice Offset Values” in “Animation” line and Press “+” button on the right.
- SLIDE 18: Save Animation File in MP4 Format
- SLIDE 19: Table of Contents
- SLIDE 20: Add the Threshold Flux for Visualization
- SLIDE 21: Change the Color Map
- SLIDE 22: Visualize Time-Dependent 3D Flux ①
- SLIDE 23: Confirm “track-xz-time_1.vtk*” in Pipeline Browser
- SLIDE 24: Press “Apply” in Properties
- SLIDE 25: ④
- SLIDE 26: Save and Load State
- SLIDE 27: Table of Contents
- SLIDE 28: Summary
- SLIDE 29: Acknowledgement
- SLIDE 01: ParaViewを用いた
- SLIDE 02: 実習内容
- SLIDE 03: Paraview_sample.inpの確認と実行
- SLIDE 04: Tallyの設定
- SLIDE 05: 実習内容
- SLIDE 06: ParaViewのインストール
- SLIDE 07: ParaViewの起動
- SLIDE 08: ParaView画面の名称
- SLIDE 09: VTKファイルの読み込みと表示
- SLIDE 10: 体系の表示
- SLIDE 11: 実習内容
- SLIDE 12: Fluxを表示する断面（Slice）を設定
- SLIDE 13: 設定した断面にfluxを表示
- SLIDE 14: 表示するfluxの下限・上限値を設定
- SLIDE 15: （補足）断面の切替えとカラーの変更
- SLIDE 16: 2次元flux分布の自動スクロール①
- SLIDE 17: 2次元flux分布の自動スクロール②
- SLIDE 18: MP4形式での動画ファイル保存
- SLIDE 19: 実習内容
- SLIDE 20: 表示するfluxのしきい値を設定
- SLIDE 21: Color Mapを変更
- SLIDE 22: 時間別flux分布の表示①
- SLIDE 23: 時間別flux分布の表示②
- SLIDE 24: 時間別flux分布の表示③
- SLIDE 25: 時間別flux分布の表示④
- SLIDE 26: 設定の保存と読込
- SLIDE 27: 実習内容
- SLIDE 28: まとめ
- SLIDE 29: 謝辞

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: old/paraview-final.inp
FILE: old/paraview.inp
FILE: paraview_sample.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Visualization of PHITS tally results using ParaView
Last Revised Mar. 2025

--- SLIDE 02 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Table of Contents
PHITS Input File Setting
Installation and Basic Usage of ParaView
Visualization of 2-D Flux
Visualization of 3-D Flux
Summary

--- SLIDE 03 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Check and run paraview_sample.inp
Generate cone-beam 40 keV X-rays from the origin (0,0,0)
Source is surrounded by a Fe cover with square hole (2 cm x 2 cm)
Water phantom (24 cm×24 cm×15 cm) is located at 35 cm from the source
Air
Water
Xray generator
Collimator
Irradiate 40 keV X-rays collimated by Fe to the water phantom
track_xz.eps (21th page)
track_xz.eps (icntl=8)
Fundamental settings
MENTIONED_INPUT_NAMES: paraview_sample.inp

--- SLIDE 04 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Tally Setting
ParaView can read VTK file

PHITS can generate VTK file when mesh = xyz, axis = xy, xz, or yz, and vtkout=1

If you want to visualize time-dependent tally results, you must set the time mesh with nt > 1
[ T - T r a c k ]
part = photon
     mesh =  xyz
    x-type =   2
       nx =  40
     xmin = -20
     xmax =  20
…
    t-type = 2
      nt  = 5
    tmin  = 0
    tmax  = 3
…
    axis =   xz
    file = track-xz-time.out
…
     vtkout = 1

--- SLIDE 05 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Table of Contents
PHITS Input File Setting
Installation and Basic Usage of ParaView
Visualization of 2-D Flux
Visualization of 3-D Flux
Summary

--- SLIDE 06 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Installation of ParaView
Download the installation file for your machine environment from the link below: https://www.paraview.org/download/
For Windows
Download “ParaView-5.13.2-Windows-Python3.10-msvc2017-AMD64.msi”*
Double click the file and install ParaView by following the dialog
＊In Mar. 2025, the latest version is v5.13.2

--- SLIDE 07 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Launch ParaView
Launch ParaView
Press “Close” in the Window shown on the right
Check this box to “don’t show this Windows again”

--- SLIDE 08 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Main Screen of ParaView
① Menu bar
② Tool bar
④ Properties
⑤ Viewport*
③ Pipeline
  Browser
＊Press “Color palette” button in tool bar to change the background color of Viewport

--- SLIDE 09 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Read VTK file

--- SLIDE 10 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Visualize Geometry
Select “region”* in Scalars in Properties
Set “Lower Threshold” to 3 and “Upper Threshold” to 4, and press “Apply”.
You can see Cell 3 (X-ray generator) and Cell 4 (water phantom) in Viewport
＊The concept of “region” is the same as that of “cell” in PHITS

--- SLIDE 11 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Table of Contents
PHITS Input File Setting
Installation and Basic Usage of ParaView
Visualization of 2-D Flux
Visualization of 3-D Flux
Summary

--- SLIDE 12 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Set Slice to Show Photon Flux
③

--- SLIDE 13 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Visualize Flux on the Slice
Change “Solid color” to “all” in Coloring column in the middle of Properties
Check the ２D flux on the slice
Press “Edit” in Coloring column to show “Color Map Editor”
Check “Use Log Scale When Mapping Data To Colors” box in Color Map Editor*. Then, the color-bar scale is changed to log expression
①
＊You can ignore warning message (see next page)

--- SLIDE 14 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Set the Range of the Color Map
Close the warning window for suggesting 0 in the log-scale color map
Press “Rescale to Custom range” in the Coloring column
Input 1e-5 and 1e-1 and press “Apply” to set the range of fluxes shown in the color map
③
①
②

--- SLIDE 15 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
(Supplement) Switching cross sections and changing colors
In the Plane Parameters section of Properties, switch between any planes by entering a value. X Normal switches to YZ plane, Y Normal switches to XZ plane, and Z Normal switches to XY plane.
Add a Slice in the same way as in the previous section and display it at the same time.
Change the color bar by selecting “Choose preset”    in Coloring of Properties.
②

--- SLIDE 16 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Scroll 2D Flux ①
Select “Slice 1” in Pipeline Browser
Click “View” in Menu bar
Select “Time Manager”
Check “Time Manager Panel” below Viewport
①
④

--- SLIDE 17 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Select “Slice1” & “Slice Offset Values” in “Animation” line and Press “+” button on the right.
Double-click the number below and set 12 and -12 in the “Value” column shown in the new Window. Then press “Apply” → “OK”
Change “Number of frames” to 50
Press “Play” button, then Y-axis of the slice is moved from +12 to -12
Scroll 2D Flux ②

--- SLIDE 18 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Save Animation File in MP4 Format
Press “File” in the Menu bar and select “Save Animation”
Input “slice” as File name, select “MP4 files(*.mp4)” in Files of Type, and “OK”
Press     button on the upper right of “Save Animation Option” Window
Input 10 in Frame Rate, 1 and 50 in Frame Window in “Animation Options”
Press “OK” and check “slice.mp4” file in the specified folder*
①
②
③
④
*In default, the same folder where VTK file exists

--- SLIDE 19 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Table of Contents
PHITS Input File Setting
Installation and Basic Usage of ParaView
Visualization of 2-D Flux
Visualization of 3-D Flux
Summary

--- SLIDE 20 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Add the Threshold Flux for Visualization
Click “Eye” icon     on the left of “Slice1” in Pipeline Browser to disable the visualization of 2D flux
Select “track-xz.vtk” in Pipeline Browser
Press “Threshold” button      in the Tool Bar and “Apply”
Input 5e-5 in “Lower Threshold” in Properties and press “Apply”
Check the grey boxes with fluxes above 5e-5 in Viewport
④

--- SLIDE 21 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Change the Color Map
Change “Solid color” to “all” in Coloring column in the middle of Properties
Change “Opacity” to 0.5 in Styling
Check the opacity of 3D flux distribution
Set 0.005 in “Lower Threshold” to visualize lower flux regions
①
②

--- SLIDE 22 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Visualize Time-Dependent 3D Flux ①
Click “File” in the Menu bar
Select “track-xz-time..vtk” and “OK”
①
②
(from 0 to 3 ns by 5 steps)
[ T - T r a c k ]
part = photon
…
    t-type = 2
    nt  = 5
    tmin  = 0
    tmax  = 3
…
    file = track-xz-time.out
…
     vtkout = 1

--- SLIDE 23 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Confirm “track-xz-time_1.vtk*” in Pipeline Browser
Click “Eye” icon     on the left of “Threshold2” to disable its visualization
Select “track-xz-time_1vtk*” in Pipeline Browser
Press Threshold button     in the Tool bar
Select “Threshold3” in Pipeline Browser
Set Lower Threshold to 2.5e-5 and Upper Threshold to 2.5e-1 in Properties
Change “Solid color” to “all” in Coloring column in the middle of Properties
Click “Rescale to Custom range” in Coloring
Set 2.5e-5 and 2.5e-1, and press “Apply” & “OK”
⑥
⑦
Visualize Time-Dependent 3D Flux ②

--- SLIDE 24 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Press “Apply” in Properties
Control animation with icons in the Tool bar
 *From left: Back to 1st frame, 1 frame back, backward play, play, 1 frame forward, forward to the last frame
①
Animate Time-Dependent 3D Flux

--- SLIDE 25 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
④
③
Save Animation File in MP4 Format
Press “File” in the Menu bar and select “Save Animation”
Input “time” as File name, select “MP4 files(*.mp4)” in Files of Type, and “OK”
Press     button on the upper right of “Save Animation Option” Window
Input 10 in Frame Rate, 0 and 4 in Frame Window in “Animation Options”
Press “OK” and check “time.mp4” file in the specified folder*
*In default, the same folder where VTK file exists

--- SLIDE 26 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Save and Load State
①
Press “File” and select “Save State”, then save as *.pvsm
You can load the state by “Load State”

--- SLIDE 27 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Table of Contents
PHITS Input File Setting
Installation and Basic Usage of ParaView
Visualization of 2-D Flux
Visualization of 3-D Flux
Summary

--- SLIDE 28 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Summary
By using ParaView, you can visualize PHITS geometry and tally results in three dimensions.
It also supports complex lattice structures, such as voxel phantoms, which cannot be rendered with the current PHIG-3D (see the right figure).
If you create high-quality images or videos using PHITS + ParaView, please share them on YouTube, Facebook, or the PHITS forum!
Deposition energy in bones of the ICRP phantom

--- SLIDE 29 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Acknowledgement
This lecture note is created under collaboration with Prof. T. Fujibuchi at Kyushu University

Fujibuchi Laboratory has released various videos combining PHITS and ParaView. Please check them out!
https://www.youtube.com/@labfujibuchi8974

--- SLIDE 01 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
ParaViewを用いた
PHITSタリー結果の可視化
2025年3月改訂

--- SLIDE 02 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
実習内容
PHITS入力ファイル設定
ParaViewのインストールと基本的な使い方
2次元Flux分布の表示
3次元Flux分布の表示
まとめ

--- SLIDE 03 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Paraview_sample.inpの確認と実行
原点（0,0,0）から40 keVのコーンビームX線を照射
鉄で囲われたX ray generator（2 cm×2 cmの射出口）
線源から35 ｃｍの距離に24 cm×24 cm×15 cmの水ファントム
基本設定
Air
Water
phantom
Xray generator
Collimator
X線管から40 keVの四角錘光子を水ファントムに照射
track_xz.eps（21ページ目）
track_xz.eps （icntl=8）

--- SLIDE 04 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Tallyの設定
ParaViewに出力結果を表示するには、vtkファイルが必要

Tallyでｘｙｚメッシュ、2次元分布出力（axis=xz等）としたうえで、“vtkout=1”を含めることで、vtkファイルを出力可能

時間変化を可視化するにはnt > 1として時間メッシュを定義する
[ T - T r a c k ]
part = photon
     mesh =  xyz
    x-type =   2
       nx =  40
     xmin = -20
     xmax =  20
…
    t-type = 2
      nt  = 5
    tmin  = 0
    tmax  = 3
…
    axis =   xz
    file = track-xz-time.out
…
     vtkout = 1

--- SLIDE 05 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
実習内容
PHITS入力ファイル設定
ParaViewのインストールと基本的な使い方
2次元Flux分布の表示
3次元Flux分布の表示
まとめ

--- SLIDE 06 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
ParaViewのインストール
下記のURLから使用するPCのOSに対応したParaViewのインストールファイルをダウンロード
https://www.paraview.org/download/
例：Windowsの場合
「ParaView-5.13.2-Windows-Python3.10-msvc2017-AMD64.msi」をダウンロード
保存したファイルをダブルクリックし、ウィザードダイアログに従ってインストール
＊資料作成時（2025.3）は、v5.13.2が最新版

--- SLIDE 07 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
ParaViewの起動
1．ParaViewを起動する。
 2．起動時に右画面が表示されるが、Closeで閉じる。
チェックを入れることで次回から非表示

--- SLIDE 08 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
ParaView画面の名称
① メニューバー
 （Menu bar）
② ツールバー
 （Tool bar）
④ プロパティ
 （Properties）
⑤ 描画域*
 （Viewport）
③ パイプライン
  ブラウザ
 （Pipeline
  Browser）
＊ツールバーにあるColor paletteボタンを押すことによりViewportの背景色を変更可能

--- SLIDE 09 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
VTKファイルの読み込みと表示

--- SLIDE 10 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
体系の表示
左下PropertiesでScalarsから“region”を選択（inputファイルのcellと同義）
Lower Threshold：3、Upper Threshold：4を入力し、Apply（cell 3から4を表示させるという意味）
右の3次元空間画面で左ドラッグすると、Xray generatorとWater phantomが確認できる

--- SLIDE 11 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
実習内容
PHITS入力ファイル設定
ParaViewのインストールと基本的な使い方
2次元Flux分布の表示
3次元Flux分布の表示
まとめ

--- SLIDE 12 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Fluxを表示する断面（Slice）を設定
③

--- SLIDE 13 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
設定した断面にfluxを表示
Properties中段 Coloringの“Solid color”を“all”に変更
Sliceに色が付き、カラーバーが表示される
ColoringのEditをクリックすると右側に、 “Color Map editor”が表示される
“Color Map editor”下方の“Use Log Scale When Mapping Data To Colors”をチェック*。カラーバーのスケールがlogになる
①
*警告が表示されても無視してよい（次項参照）

--- SLIDE 14 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
表示するfluxの下限・上限値を設定
“Use Log Scale When Mapping Data To Colors”を押すと、Output Messagesが表示されるが、分布中に0のスカラーあることの警告であり、そのまま閉じる
Coloringの“Rescale to Custom range” でカラーバーのレンジを調整できる
最小値を1e-5、最大値を1e-1としてApplyすると、低い領域のfluxが確認できる
③
①
②

--- SLIDE 15 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
（補足）断面の切替えとカラーの変更
PropertiesのPlane Parametersの項目で、数値を入力することにより任意の断面の切替えが可能。X NormalでYZ断面、Y NormalでXZ断面、Z Normal でXY断面に切り替え
前項と同様の手順Sliceを追加して、同時に表示することも可能
PropertiesのColoringの“Choose preset”   で、カラーバーの変更が可能
②

--- SLIDE 16 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
2次元flux分布の自動スクロール①
Pipeline BrowserでSlice1を選択
Menu barのViewをクリック
Time Managerを選択
画面右下にTime Manager Panelが表示される
①
④

--- SLIDE 17 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
2次元flux分布の自動スクロール②
Animation列で”Slice1”及び“Slice Offset Values”を選択し、右の＋ボタンをクリック
下段の数値をダブルクリックし、新しく表示された枠の“Value”に12、-12を入力（XZ断面、y軸の位置を意味）。入力後、Apply→OK
“Number of frames”を50と入力(50 frameに分割する意味)
再生ボタンを押すとスライスがy軸の12から‐12までスクロールされる

--- SLIDE 18 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
MP4形式での動画ファイル保存
Menu barのFile→Save Animationクリック
File nameを“slice”、Files of typeを“MP4 files(*)” として、OK
Save Animation Option ウィンドウが表示され、右上の歯車ボタンをクリック
Animation OptionsのFrame Rate 10、Frame Windowに1，50を入力、OK
指定したフォルダ(defaultは.vtkと同フォルダ)にmp4ファイルが保存される
①
②
③
④

--- SLIDE 19 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
実習内容
PHITS入力ファイル設定
ParaVIiewのインストールと基本的な使い方
2次元Flux分布の表示
3次元Flux分布の表示
まとめ

--- SLIDE 20 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
表示するfluxのしきい値を設定
Pipeline Browserで、 Slice1の左の目のマークを    クリックし、2次元分布を非表示にする
“track-xz.vtk”を選択した状態にする（文字の背景を青）
 Tool barの(Threshold)      をクリックし、Applyを押す
Properties上段のLower Threshold：5e-5と入力し、Applyを押す
ViewportにLower Thresholdの等値面（fluxが5e-5の領域）が表示される
Viewport
④

--- SLIDE 21 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
Color Mapを変更
Properties中段のColoringの“Solid color”を“all”に変更
Styling のOpacityを0.5にする
3次元flux分布の透明度が50%になる
Lower Threshold：0.005を入力し、Apply。
 等値面を調整する
①
②

--- SLIDE 22 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
時間別flux分布の表示①
Menu barのFileをクリック
track-xz-time..vtkを選択しOK
①
②
0から3 nsまでを5分割して出力という意味
[ T - T r a c k ]
part = photon
…
    t-type = 2
    nt  = 5
    tmin  = 0
    tmax  = 3
…
    file = track-xz-time.out
…
     vtkout = 1

--- SLIDE 23 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
時間別flux分布の表示②
Pipeline Browserにtrack-xz-time_1.vtk*が表示される
Threshod2を非表示にする（目のマーク     をクリックし、閉じた状態にする）
track-xz-time_1vtk*を選択
Tool barのThresholdボタン     をクリック
Pipeline BrowserのThreshold3を選択
PropertiesのLower Threshold：2.5e-5、 Upper Threshold：2.5e-1と入力
Properties中段のColoringの“Solid color”を“all”に変更
Coloringの“Rescale to Custom range”をクリック
最小値を2.5e-5、最大値を2.5e-1としてApply→OK
⑥
⑦

--- SLIDE 24 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
時間別flux分布の表示③
PropertiesのApplyをクリック
Tool barの右記アイコンで各コマの等値面を表示、切り替え
 *左から、最初のコマ、1コマ戻る、逆再生、再生、1コマ進む、最後のコマ、繰り返し
①

--- SLIDE 25 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
時間別flux分布の表示④
Menu barのFile→Save Animationクリック
File nameを“time”、Files of typeを“MP4 files(*)” としてOK
Save Animation Option ウィンドウが表示され、右上の歯車ボタンをクリック
Animation OptionsのFrame Rate 1、Frame Windowに0，4を入力、OKとすると各フレームの変化を動画保存できる
④
③

--- SLIDE 26 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
設定の保存と読込
Fileを選択して「Save State」を選択し，*.pvsmファイルとして保存
読み込む場合は「Load State」。ただし，現在の設定に追加されるので注意
①

--- SLIDE 27 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
実習内容
PHITS入力ファイル設定
ParaVIEWのインストールと基本的な使い方
2次元Flux分布の表示
3次元Flux分布の表示
まとめ

--- SLIDE 28 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
まとめ
ParaViewを使うことによりPHITSのジオメトリやタリー結果を３次元的に可視化できる

現状のPHIG-3Dでは描画できないボクセルファントムなど複雑なLattice形状にも対応可能（右図参照）

きれいな画像や動画を作成した場合は、ぜひYoutube、Facebook、PHITS forum等で共有お願いします！
ICRPファントムの骨領域のみの
吸収線量を表示させた結果

--- SLIDE 29 ---
PPTX_FILE: phits-paraview-en.pptx
SLIDE_TEXT:
謝辞
本講習会資料は、九州大学大学院医学研究院 保健学部門 藤淵 俊王教授のご協力により作成しました

藤淵研究室では、PHITSとParaViewを組み合わせた様々な動画を公開していますので、ぜひチェックしてみてください
https://www.youtube.com/@labfujibuchi8974

[BONUS_INPUT_FILES]
NOTE: None

[BONUS_TEXT_FILES]
NOTE: None
