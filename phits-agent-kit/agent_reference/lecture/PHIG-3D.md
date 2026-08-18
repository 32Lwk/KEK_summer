# Lecture: advanced/PHIG-3D

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/PHIG-3D
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: PHIG-3D
LECTURE_PATH_INDEX: lecture/advanced/PHIG-3D
PPTX_FILES: phits-lec-PHIG-3D-en.pptx, phits-lec-PHIG-3D-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: test
SECTION_KEYWORDS: t-4dtrack

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/PHIG-3D
LECTURE_PATH_INDEX: lecture/advanced/PHIG-3D
PPTX_FILES: phits-lec-PHIG-3D-en.pptx, phits-lec-PHIG-3D-jp.pptx
INPUT_DIR_COUNT: 0
MAIN_INPUT_COUNT: 1
SLIDE_COUNT: 52
EXERCISE_SLIDE_COUNT: 0
BONUS_INPUT_COUNT: 0
BONUS_TEXT_COUNT: 1

[MAIN_INPUT_FILES]
- test.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: How to use PHIG-3D
- SLIDE 02: Load the input file into PHIG-3D
- SLIDE 03: Display Geometry
- SLIDE 04: Rotation & Translation
- SLIDE 05: Change viewpoint to fixed angle
- SLIDE 06: Copy viewpoint coordinates.
- SLIDE 07: When shadows are displayed
- SLIDE 08: Display grid
- SLIDE 09: Cut with a plane
- SLIDE 10: Cut on the Z-plane
- SLIDE 11: GeometryCheck (Region Error Check)
- SLIDE 12: Important: This Auto save mode is useful when creating a PHITS system.
- SLIDE 13: Opacity
- SLIDE 14: Object with Applied opacity
- SLIDE 15: Pane (Left-side Window)
- SLIDE 16: Cell
- SLIDE 17: Setting
- SLIDE 18: Particle tracks
- SLIDE 19: Particle tracks
- SLIDE 20: Particle tracks
- SLIDE 21: Particle tracks
- SLIDE 22: Particle tracks
- SLIDE 23: Supplementary Information
- SLIDE 24: Color and Background Settings
- SLIDE 25: Color and Background Settings
- SLIDE 26: t: 2112
- SLIDE 01: PHIG-3D の使い方
- SLIDE 02: 入力ファイルをPHIG-3Dに読み込ませる
- SLIDE 03: 体系の表示
- SLIDE 04: 回転・移動
- SLIDE 05: 固定アングルに視点を変更
- SLIDE 06: 上の視点情報の数値をコピーする
- SLIDE 07: 影を表示させた場合（光源は真上に配置）
- SLIDE 08: グリッドの表示
- SLIDE 09: 平面でカットする場合
- SLIDE 10: Z平面でカット
- SLIDE 11: （２）ウィンドウが開く
- SLIDE 12: 重要： この Auto save モードは、PHITS 体系を作成する際に便利
- SLIDE 13: 透明化
- SLIDE 14: 透明化
- SLIDE 15: ペイン（左側のウィンドウ）
- SLIDE 16: Cell
- SLIDE 17: Setting
- SLIDE 18: Particle tracks
- SLIDE 19: Particle tracks
- SLIDE 20: Particle tracks
- SLIDE 21: Particle tracks
- SLIDE 22: Particle tracks
- SLIDE 23: 補足
- SLIDE 24: 色と背景の設定
- SLIDE 25: 色と背景の設定
- SLIDE 26: t: 2112

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: test.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
How to use PHIG-3D
Oct. 2024 Revised
phits/lecture/advanced /PHIG-3D

--- SLIDE 02 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Load the input file into PHIG-3D
Windows: Right-click on test.inp, select “Send to” → “PHIG-3D”.
macOS: Drag and drop test.inp onto “PHIG-3D” in the Dock.
Linux: In the folder containing test.inp, execute phig3d.sh test.inp.
MENTIONED_INPUT_NAMES: test.inp

--- SLIDE 03 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Display Geometry
Click to Display

--- SLIDE 04 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Rotation & Translation
Move object:
Left-click and drag
Translate (move parallel):
Shift + drag
or
Middle-click + drag
Rotate parallel to screen:
Ctrl + drag
Command + drag (macOS)

--- SLIDE 05 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Change viewpoint to fixed angle
Rotate 90 degrees
Changing Viewpoint

--- SLIDE 06 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Copy viewpoint coordinates.
Useful for specifying camera angles when creating videos.
Refer to page 22, "Particle tracks Camera movement”.
Light position and Shadow Settings.
The light position is set at the current viewpoint position.
Example: To place the light source above, display the system from above and press the camera button.
Check
Detailed View Settings, Light position, Shadow
(2) Dialog opens
(  x,  y,  z,
  Fx, Fy, Fz,
  Ux, Uy, Uz )
Viewpoint coordinates
(1) Click

--- SLIDE 07 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
When shadows are displayed
(Light source positioned directly above)
Detailed View Settings, Light position, Shadow

--- SLIDE 08 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Display grid
Display coordinate axes
Enable cell selection by mouse click
Display material legend
Place markers
Various Settings

--- SLIDE 09 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Cut with a plane
Cut with a box
Display Cross-Section
(2) Dialog opens
(1) Click

--- SLIDE 10 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Cut on the Z-plane
Cut with a box
Cut region
0 < X < 100
0 < Y < 100
0 < Z < 100

--- SLIDE 11 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
GeometryCheck (Region Error Check)
No errors
(2) Dialog opens
(1) Click
(3) Click
Errors

--- SLIDE 12 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Important: This Auto save mode is useful when creating a PHITS system.
→ You can modify the input file, “Reload” it, and check for updates.
Save state
Click here to enable “Auto save” mode
Shortcut for Reload
ctrl + shift + R
command + shift + R
Perform one of the following actions:
     Reload the input file (File → Reload)
     or  Save the state (File → Save State)
     or  Close PHIG-3D
A test.inp.phg file will be created in the same folder as test.inp.
Next time PHIG-3D is opened, you can restore the state by loading the test.inp.phg file (File → Load State).
MENTIONED_INPUT_NAMES: test.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Opacity
Method 2:
Right-click on the object
Set the object’s opacity
Method 1:
In the “Cell Pane”, multiple cell numbers can be selected (Shift or Ctrl/Command + Click)
→ Right-click on the selected numbers.

--- SLIDE 14 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Object with Applied opacity
Opacity

--- SLIDE 15 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Pane (Left-side Window)
“Cell” pane
“Setting” pane
“Particle tracks” pane
Click on each name to expand

--- SLIDE 16 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Cell
Toggle visibility of selected cells.
Apply opacity.

Multiple cell numbers can be selected.
(Shift or Ctrl/Command + Click)

Low-density materials, such as air (0.0015 g/cm3 or less), are hidden by default.

--- SLIDE 17 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Setting
Increase the value to smooth rendering.
Fixed viewport size
(e.g.: 1920 x 1080 pixels)
Useful for outputting still images and videos!
After entering values, click the “Draw” button twice.
Click after changing values
Drawing region setting
After making changes to the input, if the geometry is not fully displayed, click the “Recalc” button, then reload to ensure full display.

--- SLIDE 18 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
Load the output file for the [ t-4Dtrack ] tally.
In this case, load the track.out file generated by running test.inp.
Click
MENTIONED_INPUT_NAMES: test.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
Track of injected electrons
(10 histories)
Clear the track file
Color & Thickness
Toggle visibility
To limit displayed histories (by default, all are shown)
e.g. Display only track histories with numbers 2, 4, and 6 to 10
→ [ 2, 4, 6-10 ]
(Basic)

--- SLIDE 20 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
Start Time
End Time
Number of Frames
Play
(Video Control Panel)
Record

--- SLIDE 21 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
(Recording Settings)
(1) Click
 Record button
Select video format
Note: PNG, OGV, and WebM formats are available. It can be easily converted to formats like MP4. Search for “OGV to MP4 conversion.”
Conversion using the ffmpeg command:
     ffmpeg -i test.ogv test.mp4
Specify output name
Camera movement (optional)
→ Details on the next page
Start recording
(2) Dialog opens

--- SLIDE 22 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
Camera movement (optional)
While recording, you can specify viewpoint information at a particular time.
Method 1: Press "Add new line" and manually enter the time (in nanoseconds) and nine viewpoint coordinates.
Method 2: Prepare a text file with time and (at least) nine viewpoint coordinates separated by spaces. Use "Import from file" to load the file.
Sample file: camera.txt
For information on obtaining viewpoint coordinates, refer to "Detailed View Settings, Light position, Shadow" on page 6.
Camera button       at the bottom of the main window → Copy to clipboard
When you press the “Camera movement” button on the previous page, the following dialog opens.

--- SLIDE 23 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Supplementary Information
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 24 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Color and Background Settings
Customize material colors and names.
Adjust brightness, colors, and background images for display.

--- SLIDE 25 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Color and Background Settings
(Example: An image is set as the background)
picture from DALL-E

--- SLIDE 26 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
t: 2112
  0.000E+00  0.000E+00 -3.136E+00  2.444E+00  4.453E+01  1.000E+00
  2.867E+00  2.863E+00 -3.488E-01  2.996E+00  4.453E+01  1.000E+00
  4.510E+00  5.029E+00  2.294E+00  3.421E+00  4.450E+01  1.000E+00
  6.057E+00  6.608E+00  3.495E+00  3.704E+00  4.444E+01  1.000E+00
  6.636E+00  8.019E+00  4.512E+00  4.122E+00  1.020E+01  1.000E+00
t: 中性子
  0.000E+00  0.000E+00 -3.136E+00  2.444E+00  4.453E+01  1.000E+00
  2.867E+00  2.863E+00 -3.488E-01  2.996E+00  4.453E+01  1.000E+00
  4.510E+00  5.029E+00  2.294E+00  3.421E+00  4.450E+01  1.000E+00
  6.057E+00  6.608E+00  3.495E+00  3.704E+00  4.444E+01  1.000E+00
  6.636E+00  8.019E+00  4.512E+00  4.122E+00  1.020E+01  1.000E+00
Replace the kf-code in the [t-4Dtrack] output file with an arbitrary string.
Load the file in PHIG-3D
The string will be displayed as a legend in PHIG-3D
See： phits/utility/t-4Dtrack/T4D-format

--- SLIDE 01 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
PHIG-3D の使い方
2024年10月改訂
phits/lecture/advanced /PHIG-3D

--- SLIDE 02 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
入力ファイルをPHIG-3Dに読み込ませる
Windows: test.inp を右クリックし、「送る」→「PHIG-3D」を選択
macOS: test.inp を Dock にある PHIG-3D にドラッグ&ドロップ
Linux: test.inp があるフォルダで、「phig3d.sh test.inp」を実行
MENTIONED_INPUT_NAMES: test.inp

--- SLIDE 03 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
体系の表示
クリックして表示

--- SLIDE 04 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
回転・移動
回転
物体を左クリックして移動
平行移動
Shift ＋ 移動
または
中クリック ＋ 移動
画面と平行に回転
Ctrl + 移動
command + 移動 (macOS)

--- SLIDE 05 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
固定アングルに視点を変更
90度回転
視点の変更

--- SLIDE 06 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
上の視点情報の数値をコピーする
動画を作る際のカメラアングルの指定に便利
ページ２２「Particle tracks カメラ動作」を参照
光源と影の設定
現在の視点の位置に光源がセットされる
例：上に光源を置きたい場合は、上から体系を表示させた状態でカメラボタンを押す
チェック
視点の詳細設定・光源・影
（２）ダイアログが開く
(  x,  y,  z,
  Fx, Fy, Fz,
  Ux, Uy, Uz )
視点座標
（１） クリック

--- SLIDE 07 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
影を表示させた場合（光源は真上に配置）
視点の詳細設定・光源・影

--- SLIDE 08 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
グリッドの表示
座標軸の表示
マウスクリックによるセル選択の有効化
材料凡例の表示
マーカーの設置
様々な設定

--- SLIDE 09 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
平面でカットする場合
ボックスでカットする場合
（２）ダイアログが開く
断面の表示
（１） クリック

--- SLIDE 10 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Z平面でカット
ボックスでカット
カット領域
0 < X < 100
0 < Y < 100
0 < Z < 100

--- SLIDE 11 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
（２）ウィンドウが開く
体系のチェック（領域エラーチェック）
（３）クリック
エラーなし
エラーあり
（１） クリック

--- SLIDE 12 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
重要： この Auto save モードは、PHITS 体系を作成する際に便利
→ 入力ファイルを修正し、それを「再読込」して確認できる
状態を保存
ここをクリックして「Auto save」モードにする
以下の動作のいずれかを行う：
     入力ファイルを再読み込みする（ファイル → 再読込）
     or  状態を保存する（ファイル → 状態を保存）
     or  PHIG-3Dを閉じる
test.inp.phg ファイルが test.inp のフォルダに作られる
次回に PHIG-3D を開いた時、test.inp.phg ファイルを読み込むことで、状態を復元できる（ファイル → 状態を復元）
再読込のショートカット
ctrl + shift + R
command + shift + R
MENTIONED_INPUT_NAMES: test.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
透明化
方法２：
物体を右クリック
方法１：
「 Cell ペイン」 でセル番号を複数選択可能
（shift または ctrl/command + クリック）
→ 選択した番号を右クリック
物体の透明度を設定

--- SLIDE 14 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
透明化
例：物体を透明化した場合

--- SLIDE 15 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
ペイン（左側のウィンドウ）
Cell ペイン
Setting ペイン
Particle tracks ペイン
それぞれの名前を
クリックして開く

--- SLIDE 16 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Cell
選択したセルの表示/非表示にする。
透明化する。

セル番号は、複数選択可能。
（shift または ctrl/command + クリック）

空気などの低密度の物質（0.0015 g/cm3 以下）はデフォルトでは非表示。

--- SLIDE 17 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Setting
描画を滑らかにしたい時
数値を増やす
表示サイズの固定
（例：1920 x 1080 ピクセル）
静止画や動画を出力する際に便利！
数値入力後、描画ボタンを
２回クリック
数値の変更後にクリック
表示領域の設定（自動）
体系を大きく変更後、表示されない領域がある場合は、「再計算」ボタンを押してから再読込することで表示できるようになる。

--- SLIDE 18 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
[ t-4Dtrack ] タリーの出力ファイルを読み込む
この場合は、test.inp を実行して出力された track.out を読み込む
MENTIONED_INPUT_NAMES: test.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
電子を入射した場合の飛跡
（10 ヒストリー）
飛跡ファイルのクリア
色と太さ
表示/非表示
表示するヒストリーを制限する場合（デフォルトでは全て表示）
例： 2, 4, 6から10のヒストリー番号の飛跡だけを表示
→ [ 2, 4, 6-10 ]
（基本操作）

--- SLIDE 20 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
開始時刻
終了時刻
フレーム数
再生
（動画制御パネル）
録画

--- SLIDE 21 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
（録画設定）
（１）録画ボタン
をクリック
（２）ダイアログが開く
動画フォーマットの選択
※ 動画フォーマットではpng, ogv webmが選べます。 mp4 など他フォーマットへの変換は容易に行えます。
「ogv mp4 変換」などで検索。
ffmpeg コマンドを用いた変換：
     ffmpeg -i test.ogv test.mp4
出力名の指定
カメラ動作（オプショナル）
→ 詳細は次ページ
録画開始

--- SLIDE 22 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
Particle tracks
カメラ動作（オプショナル）
録画する時、ある時刻における視点情報を指定できます
方法１：「新しい行を追加」を押して、時刻（単位はナノ秒）と、９つの視点座標を手動で入力する。
方法２：時刻と（最低）９つの視点座標がスペース区切りで書かれたテキストファイルを用意する。 「ファイルからインポート」からそのファイルを読み込む
サンプルファイル： camera.txt
視点座標の取得方法は、６ページの「視点の詳細設定・光源・影」を参照してください。
メインウィンドウ下のカメラボタン        → Copy to clipboard
前ページの「カメラ動作」ボタンを押すと以下のダイアログが開く

--- SLIDE 23 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
補足
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 24 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
色と背景の設定
物質の色や材料名などを変更可能
表示の明るさや色、背景画像などを設定できる

--- SLIDE 25 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
色と背景の設定
（例：画像を背景に設定した場合）
picture from DALL-E

--- SLIDE 26 ---
PPTX_FILE: phits-lec-PHIG-3D-en.pptx
SLIDE_TEXT:
t: 2112
  0.000E+00  0.000E+00 -3.136E+00  2.444E+00  4.453E+01  1.000E+00
  2.867E+00  2.863E+00 -3.488E-01  2.996E+00  4.453E+01  1.000E+00
  4.510E+00  5.029E+00  2.294E+00  3.421E+00  4.450E+01  1.000E+00
  6.057E+00  6.608E+00  3.495E+00  3.704E+00  4.444E+01  1.000E+00
  6.636E+00  8.019E+00  4.512E+00  4.122E+00  1.020E+01  1.000E+00
t: 中性子
  0.000E+00  0.000E+00 -3.136E+00  2.444E+00  4.453E+01  1.000E+00
  2.867E+00  2.863E+00 -3.488E-01  2.996E+00  4.453E+01  1.000E+00
  4.510E+00  5.029E+00  2.294E+00  3.421E+00  4.450E+01  1.000E+00
  6.057E+00  6.608E+00  3.495E+00  3.704E+00  4.444E+01  1.000E+00
  6.636E+00  8.019E+00  4.512E+00  4.122E+00  1.020E+01  1.000E+00
参考: phits/utility/t-4Dtrack/T4D-format
[t-4Dtrack] の出力ファイルのkf-codeの箇所を任意の文字列に置き換える
PHIG-3Dでそのファイルを読み込む
凡例にその文字列が表示される

[BONUS_INPUT_FILES]
NOTE: None

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: camera.txt
