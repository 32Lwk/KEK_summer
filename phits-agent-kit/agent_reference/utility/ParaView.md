# Utility: ParaView

SOURCE_FOLDER: D:/NEAgit/utility/ParaView
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: ParaView
UTILITY_PATH_INDEX: utility/ParaView
UTILITY_FOLDER_NAME: ParaView

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/ParaView
BASIC_FILE_COUNT: 1
BASIC_FILE: PHITS-3Dvisualization-manual.docx
BASIC_FILE_TYPE: docx
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 1

[BASIC_FILES]
FILE: PHITS-3Dvisualization-manual.docx
BEGIN_BASIC_TEXT
PHITSの出力結果を
ParaViewで三次元可視化する方法
マニュアル
平成28年7月
PHITSの出力結果をParaViewで三次元可視化する方法
マニュアル
目 次
1. はじめに	1-1
1.1. 目的	1-1
1.2. 本書の内容	1-1
2. PHITSの入出力ファイル	2-1
2.1. 三次元可視化用PHITSインプットパラメータ	2-1
2.2. 出力ファイル名	2-1
2.3. 三次元可視化用出力ファイルの形式	2-2
3. ParaViewのインストール	3-1
3.1. インストールファイルのダウンロード	3-1
3.2. インストール	3-3
4. 三次元可視化の実行例	4-1
4.1. サンプル入力ファイル(sample.inp)	4-1
4.2. PHITSコードの実行	4-2
4.3. ParaViewによる表示	4-2
はじめに
目的
三次元複雑形状の構築および線量結果の詳細な解析を効率的に行うための機能として、PHITSのタリー結果を三次元可視化ソフトウェアParaViewのファイル形式で出力する機能を導入した。本書では、この使い方について解説する。また、本書では簡単な例で実際にParaViewを使った三次元可視化の一例を示す。詳しいParaViewの使い方については、ParaViewチュートリアル
http://www.paraview.org/Wiki/images/0/03/ParaViewTutorial38-jp.pdf
等を参照していただきたい。
本書の内容
本機能を仕様するためのPHITSインプットパラメータ
PHITSのタリー出力結果及び幾何形状をParaViewファイル形式に出力するためのPHITSインプットパラメータについて記述する。
ParaViewのインストール
三次元可視化ソフトウェアParaViewのインストール方法について記述する。
三次元可視化の実行例
サンプルファイルを用いて、三次元可視化の実行例を示す。
PHITSの入出力ファイル
三次元可視化用PHITSインプットパラメータ
PHITSのタリー結果をParaViewで可視化するためには,可視化したいタリーに表 2-1 に示すパラメータを追加する必要がある。
表 2-1三次元可視化用PHITSインプットパラメータ
ただし,これらのタリーパラメータは以下の8つの物理量タリーもしくは2つの幾何形状タリーでXYZメッシュが選択された場合のみ有効となる。
・[T-Track]
・[T-Heat]
・[T-Deposit]
・[T-Yield]
・[T-Product]
・[T-Dpa]
・[T-Time]
・[T-Star]
・[T-Gshow]
出力ファイル名
タリー結果の三次元可視化用出力ファイル名
ベースとするファイル名は、EPSファイルや二次元ビットマップ画像ファイルと同じく、「file =」パラメータで設定したファイル名で、拡張子は「.vtk」である。
ParaView では、ファイル名に連番を付けたデータファイルは自動的に時間順序アニメーションファイルとして一括りにして扱ってくれる。従って、時間メッシュ(t-type)が設定されたタリーの場合、ファイル名に「_T」(Tは時間インデックス、インデックスの最大桁数に合わせて0埋め)を付加し、アニメーション可能となるようになっている。
物理タリーにおいて三次元可視化用出力をする場合に「gshow=1(以上)」とした場合は、同じメッシュ分割設定で幾何形状の三次元可視化用ファイル(スライス毎に領域境界を線で表示したもの)も出力する。そのときのファイル名は拡張子の前に「_g」をつけたものとなる(つまり、ファイル名末尾は「_g.vtk」となる)。また、T-Gshowタリーを使用することで、幾何形状の三次元可視化用ファイルを出力することができ、この場合は、メッシュ分割を自由に設定できる。
三次元可視化用出力ファイルの形式
三次元可視化用出力ファイルの形式は、VTKレガシー形式である。タリー値はエネルギーメッシュや粒子タイプごとに集計されている。タリーごとに分離しているパラメータの一覧を表 2-3に示す。タリー値に対応するデータ名は、二次元ビットマップ画像ファイルのファイル名と同じく、情報タイプとそのインデックスを使用する。物質番号、領域番号のデータ名はそれぞれ "material", "region" とする。物理量タリー値はセルデータとして、幾何形状はポリゴンデータとして出力されている。時間については、前述のように時間メッシュごとに別のファイルとしている。
表 2-3タリー出力結果の三次元可視化用セルデータとして分離するタリーパラメータ
下図に非常にシンプルなVTKレガシーファイル例を示す。
図 2-1 タリー出力結果の三次元可視化用ファイル例
下図にVTKレガシーPOLYDATAファイル例を示す。
図 2-2 幾何形状の三次元可視化用ファイル例
ParaViewのインストール
本章ではParaViewのバイナリファイルのインストール方法について述べる。ソースファイルからコンパイルインストールする方法については、Wiki を参照のこと。
インストールファイルのダウンロード
以下の手順で、ParaViewを使用するOSに対応したインストールファイルをダウンロードする。
ウェブブラウザでParaViewのサイトにURL「http://www.paraview.org」でアクセスする(図 3-1)。
「Download Latest Release」のリンク先「http://www.paraview.org/download/」に移動し、[Release] の項目から選択して [Download] ボタンをクリックし、インストールファイルをダウンロードする(図 3-2)。
以下の項目がある。項目1~3を選択すると、条件にあったダウンロード可能ファイルのリストが4で選択できるようになる。
図 3-1 ParaViewのウェブサイト
図 3-2 ParaViewのダウロードファイル選択
インストール
Linuxへのインストール
以下にUbuntu14.04 (64bit) を対象に、インストール方法について述べる。
ファイル「ParaView-5.0.1-Qt4-OpenGL2-MPI-Linux-64bit.tar.gz」をダウンロードし、保存したとする。図 3-3 のようにファイルを展開し、binディレクトリ内のparaview ファイルを実行すれば起動する。
インストールは、展開ディレクトリ「ParaView-5.0.1-Qt4-OpenGL2-MPI-Linux-64bit」を適当な保存先に名前を変えて変更し、binディレクトリにパスを通せばよい。
図 3-3 Linux用ダウンロードファイルの展開とParaViewの起動
Microsoft Windowsへのインストール
Windows7 (64bit) を対象に、インストール方法について述べる。
ファイル「ParaView-5.0.1-Qt4-OpenGL2-Windows-64bit.exe」をダウンロードし、保存したとする。保存したexeファイルをマウスでダブルクリックすると、 図 3-4 に示すようなウィザードダイアログが表示される。ライセンスに同意し(b)、インストール先を選択し(c)、[インストール] をクリックすると(e)、インストールが行われる。
実行は、スタートメニューから [プログラム]->[ParaView 5.0.1]-> [ParaView 5.0.1] と選択することにより行うことができる(図 3-5)。
インストールファイルのファイル形式がZIPの場合は、単に保存先に展開すればよい。スタートメニューに登録されないので、実行は直接paraview.exe を起動する必要がある。
MPI版の場合は、msmpi.dll (Microsoft MPI (MS-MPI)のDLLファイル) が必要である。Microsoft のサイトから MsMpiSetup.exe ファイルをダウンロード、実行してインストールすればよい。
図 3-4 Windows用ダウンロードファイルの実行とインストール
図 3-5 Windows用ParaViewの起動
MacOS Xへのインストール
ファイル「ParaView-5.0.1-Qt4-OpenGL2-MPI-OSX10.7-64bit.dmg」をダウンロードし、保存したとする。保存したdmgファイルをマウスでダブルクリックすると、ライセンス同意ダイアログが表示され(図 3-6)、同意するとdmgファイルが展開されてフォルダが開かれます(図 3-7)。フォルダ内のparaviewをダブルクリックすると、ParaViewが起動します。
インストールは、展開フォルダ「ParaView-5.0.1-Qt4-OpenGL2-MPI-OSX10.7-64bit」を適当な保存先に名前を変えて変更すればよい。
paraviewをダブルクリックしたときに(図 3-8)のような表示が出た場合、以下の方法で起動できます。
Controlキーを押しながらクリックするとコンテキストメニューが表示されるので、「開く」を選択して開く。
「開く」ボタンがあるエラーダイアログが表示されます(図 3-9)。「開く」ボタンをクリックすると、ParaViewが起動します。
あるいは、常時実行を許可するダイアログが開かれますので(図 3-10)、許可すればParaViewが起動します。
図 3-6 ParaView dmgファイルの展開時ダイアログ
図 3-7 dmgファイル展開後のParaViewフォルダ
図 3-8 「開発元が未確認のため開けません」エラーダイアログ
図 3-9 「開く」ボタン付き「開発元が未確認のため開けません」エラーダイアログ
図 3-10 常時実行の許可ダイアログ
三次元可視化の実行例
サンプル入力ファイル(sample.inp)
lecture\basic\lec03で使っているタマネギ体系を使って、三次元可視化の操作を行ってみる。入力ファイルを 図 4-1 に示す。
図 4-1 三次元可視化のサンプル入力ファイル (sample.inp)
PHITSコードの実行
通常通り、入力ファイルsample.inpを用いてPHITSを実行する。
ParaViewによる表示
タリー結果の表示
まずはタリー結果を三次元表示することから始めます。以下の手順で行います。
VTKファイルを読み込む。
図4-2 ParaViewファイルの読み込み
ParaViewを立ち上げ、表示されるParaViewのメニュー(図4-2)から [File]->[Open] で開いたダイアログで、PHITSの実行により出力されたVTKファイル "track.vtk" を開き、ParaViewの左上のパイプラインブラウザに "track.vtk" が表示されたら、左下のプロパティタブで「Apply」をクリックします(図 4-3)。
図4-3 Paraviewファイルの設定
最初はアウトライン表示されます(図 4-4)。
図4-4 VTKファイル読み込み時の最初の表示(アウトライン)
値を表示させる。
左下のプロパティタブを下にスクロールし、[Coloring]セクションの最初の項目のプルダウンメニュー(Solid Color, material, p1, p2, region)から選択することで、表示する値を変更できます。materialとregionはそれぞれ物質値と領域値で、p1とp2はタリーでpart=all protonとしているのに対応したそれぞれの物理量(p1がpart=allで、p2がpart=proton)を表すことになります。ここでは、例としてp1を選ぶこととします。また、[Coloring]セクションの一つ前にあるRepresentaionのプルダウンメニューを変更することで、値をどのように表示するのか指定できます。例えばSurfaceを選ぶことで、見ている範囲の表面での物質値がカラーマップで表示されます。現在の例の場合、タリー範囲の端(ボイド領域)の物理量を示しているため、全て範囲で値が0であり、単色の物体が表示されています(図4-5)。
図4-5 タリー結果の表示
右下の表示ウィンドウはマウスで操作ができます。例:左クリックを押しながらマウスを動かすことで回転し、真ん中ボタンをスクロールすることで拡大縮小ができます(図4-6)。
図4-6 マウスによる表示の回転・拡大縮小
一部を切り出す(クリップする)。
ウィンドウ上方のパネルの中からClipフィルターを選びます(図4-7)。
図4-7 Clipフィルターの選択
Origin(位置)やNormal(面の垂線)を変更することで、切り出す面の位置や向きを変更することができます。Applyをクリックすることで適用され、実際に切り出されます(図4-8)。
図4-8 Clipフィルターの適用
Show Planeのチェックを外すと枠の表示を消すことができます。また、マウスによって回転させることで、切り出した断面を見ることができます(図4-9)。
図4-9 Clipフィルターで切り出した面の確認
表示する領域に制限を掛ける。
ウィンドウ上方のパネルの中からThresholdフィルターを選びます(図4-10)
図4-10 Thresholdフィルターの選択
Scalarsのプルダウンメニューを選んで、どの量(material, region, p1, p2)に対する閾値を設定るするのか選びます。そして、最小値と最大値をその下で設定します。Applyをクリックすることで適用され、実際に指定範囲の値のみが表示されるようになります(図4-11)。
図4-11 Thresholdフィルターの適用
この例の場合、PHITS体系で領域101-105を表示するように設定しているため、アウターVoid(領域106)が表示されなくなります。
表示に対する制限をさらに加えることもできます。再度、ウィンドウ上方のパネルの中からThresholdフィルターを選ぶことで、表示に対する制限をさらに追加することもできます(図4-12)。
図4-12 二重のThresholdフィルターの適用
この例では、p1に対して最小値1e-10(10-10)と最大値1e10(1010)の閾値をさらに設定し、ゼロよりも大きい物理量が色つきで表示されます。
幾何形状をタリー結果に重ねて表示
幾何形状ファイル "geometry.vtk" を読み込む(図 4-13)。
図4-13 幾何形状ファイルの読み込み
Applyをクリックし、RepresantationのプルダウンメニューからWireframeを選択する(図 4-14)。
図4-14 幾何形状の同時表示
カラー軸の設定
初期設定では,赤から青に段階的に変更するカラー軸が設定されています。これをPHITSの2次元表示で使っていたレインボーカラーに変更するには,まず,フルエンスを表示しているThreshold2を選択した後,ColoringのChoose Presetボタンを押します。その後,出てくるウィンドウからPHITSの設定に近いBlue to Red Rainbowを選びApplyボタンを押すことにより,カラー軸が変更されます。
図4-15 カラー軸の設定を変更
カラー軸をLog表示にするには,Editボタンを押した後,Use log scale when mapping data to colorsのチェックボックスをクリックします。また,軸の最大値・最小値を指定するには,set rangeボタンを押して最大値・最小値を入力します。
図4-16 カラー軸のLog/Linear切り替えや最大値・最小値の設定
ParaViewの設定は,FileメニューにあるSave Stateで保存することができます。本書で解説した設定を保存したファイルがsample.pvsmとなります。
[TABLE]
Name | 値 | 説明
vtkout = | 0(省略時), 1 | タリー出力結果の三次元可視化用ファイルを出力する。 / ファイル名は出力ファイルの拡張子をvtkに変えたファイル名。 / mesh=xyz、axis=(xy, yz, xz のいずれか) のときのみ有効。
vtkfmt = | 0(省略時), 1 | タリー出力結果の三次元可視化用ファイルのフォーマット。 / テキスト形式(0)またはバイナリ形式(1)を選択する。
[TABLE]
タイプ名 | 内容 | 対応パラメータ | t-track | t-heat | t-deposit | t-yield | t-product | t-dpa | t-time | t-star
E | エネルギーメッシュ | e-type | [[[○]]] |  | [[[○]]] |  | [[[○]]] |  | [[[○]]] | [[[○]]]
A | 角度メッシュ | a-type |  |  |  |  | [[[○]]] |  |  |
P | 粒子タイプ | part | [[[○]]] |  | [[[○]]] |  | [[[○]]] | [[[○]]] | [[[○]]] | [[[○]]]
M | 物質乗数 | multiplier | [[[○]]] |  |  |  |  |  |  |
N | 核種生成 | nucleus |  |  |  | [[[○]]] |  |  |  |
O | 出力タイプ | output |  | [[[○]]] |  |  |  | [[[○]]] |  |
[TABLE]
# vtk DataFile Version 3.0 / vtk output / ASCII / DATASET RECTILINEAR_GRID / DIMENSIONS 3 4 3 / X_COORDINATES 3 float / 0 2 4 / Y_COORDINATES 4 float / 1 2 3 4 / Z_COORDINATES 3 float / 0 1 2 /  / CELL_DATA 12 / FIELD FieldData 3 / p1e1 1 12 float / 1.0 1.2 1.4 1.6 1.8 2.0 / 11.0 12.0 13.0 14.0 15.0 16.0 / material 1 12 int / 0 0 1 1 1 1 / 3 3 1 1 1 1 / region 1 12 int / 100 100 101 101 102 102 / 103 103 104 104 105 105 / POINT_DATA 36
[TABLE]
# vtk DataFile Version 2.0 / vtk output / ASCII / DATASET POLYDATA / POINTS 55 float /  -3.211092E+00 -3.832608E+00  0 /  -3.146341E+00 -3.885941E+00  0 /  -2.716515E+00 -4.197683E+00  0 /  -2.097561E+00 -4.538749E+00  0 /  -9.580654E-01 -4.907353E+00  0 /  -1.048780E+00 -4.888769E+00  0 /   1.801171E-01 -4.996755E+00  0 /   1.234568E-11 -5.000000E+00  0 /   1.107862E+00 -4.875720E+00  0 /   1.048780E+00 -4.888769E+00  0 /  / ...(略) /  /  -4.851415E+00 -1.209865E+00  0 /  -4.509026E+00 -2.160714E+00  0 /  -4.403248E+00 -2.368841E+00  0 /  -4.195122E+00 -2.720469E+00  0 /  -3.286830E+00 -3.767857E+00  0 / POLYGONS 1 56 / 55 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 /    20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 /    40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
[TABLE]
 | 項目 | 選択内容
1 | バージョン | バージョン1.0から最新版(v5.0, 2016年3月現在)までのリリース。
2 | ダウンロードファイルの種類 | v5.0 の場合: / 「ParaView Binary Installers」: ParaViewの実行ファイル本体 / 「ParaView Soure Files」: ParaViewのソースファイル / 「Data, Documentation, and Tutorials」: ユーザガイドやサンプルデータなど。 / 「Community Contributed Plugins」: コミュニティ提供プラグイン
3 | OS | v5.0の場合: / 「Windows 64-bit」 / 「Windows 32-bit」 / 「Linux 64-bit」 / 「Mac OS X」
4 | ダウンロードファイル | マイナーバージョン、MPI対応、インストールファイルの形式、などによってダウンロードファイルを選択できる。
[TABLE]
$ tar zxvf ParaView-5.0.1-Qt4-OpenGL2-MPI-Linux-64bit.tar.gz / $ cd ParaView-5.0.1-Qt4-OpenGL2-MPI-Linux-64bit / $ ./bin/paraview
[TABLE]
(a) | (b)
(c) | (d)
(e) | (f)
(g) |
[TABLE]
[ T i t l e ] / mille-feuille geometry /  / [ P a r a m e t e r s ] /  icntl    =          0     # (D=0) 3:ECH 5:NOR 6:SRC 7,8:GSH 11:DSH 12:DUMP /   maxcas  = 1000 /   maxbch  = 10 /  file(6)  = phits.out       # (D=phits.out) general output file name /  / [ S o u r c e ] /    s-type =   1             # mono-energetic axial source /      proj =  proton         # kind of incident particle /       dir =   1.0           # z-direction of beam [cosine] /        r0 =   1.0            # radius [cm] /        z0 =   0.            # minimum position of z-axis [cm] /        z1 =   0.            # maximum position of z-axis [cm] /        e0 =   150.          # energy of beam [MeV] /  / [ M a t e r i a l ] / mat[1]    1H 2  16O 1 / mat[2]    1H 2  16O 1 / mat[3]    1H 2  16O 1 / mat[4]    1H 2  16O 1 / mat[5]    1H 2  16O 1 / mat[6]    1H 2  16O 1 /  / [ S u r f a c e ] /   11  so       5. /   12  so      10. /   13  so      15. /   14  so      20. /   15  so      25. /  / [ C e l l ] /  101     1 -1.               -11 /  102     2 -1.          11   -12 /  103     3 -1.          12   -13 /  104     4 -1.          13   -14 /  105     5 -1.          14   -15 /  106    -1              15 /  / [ T - Gshow ] /      mesh =  xyz /    x-type =    2 /        nx =  100 /      xmin =  -30. /      xmax =   30. /    y-type =    2 /        ny =  100 /      ymin =  -30. /      ymax =   30. /   z-type =     2 /        nz =    5 /      zmin =  -22. /      zmax =   22. /      axis =   xy /      file = geometry.out /    output = 2 /    vtkout = 1 /  / [ T - T r a c k ] /      mesh =  xyz /    x-type =    2 /        nx =   30 /      xmin =  -30. /      xmax =   30. /    y-type =    2 /        ny =   30 /      ymin =  -30. /      ymax =   30. /    z-type =    2 /        nz =   30 /      zmin =  -30. /      zmax =   30. /      part =  all proton /    e-type =    1            # e-mesh is given by the below data /        ne =    1            # number of e-mesh points /             0.0   1000.0 /      unit =    1            # unit is [1/cm^2/source] /      axis =   xz            # axis of output /   2d-type = 3 /      file = track.out /     gshow =   0             # 0: no 1:bnd 2:bnd+mat 3:bnd+reg 4:bnd+lat /   vtkout =    1 /  / [ E n d ]
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: sample.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: geometry.vtk
