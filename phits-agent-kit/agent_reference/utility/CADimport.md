# Utility: CADimport

SOURCE_FOLDER: D:/NEAgit/utility/CADimport
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: CADimport
UTILITY_PATH_INDEX: utility/CADimport
UTILITY_FOLDER_NAME: CADimport

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/CADimport
BASIC_FILE_COUNT: 0
BASIC_FILE: (none)
BASIC_FILE_TYPE: none
PPTX_COUNT: 2
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 2

[BASIC_FILES]
FILE: (not found)
NOTE: No readme* file and no .docx file found.

[PPTX_CONTENTS]
FILE: phits-lec-CADimport-en.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-lec-CADimport-en.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
PHITS Tutorial
How to import CAD geom. into PHITS
Title
1
Mar. 2023 revised

--- SLIDE 02 ---
2
Conventional Geometry
Spherical surface
Box surface
Cylindrical surface
Combination of simple surfaces
=> Difficult to construct complex geometries
Geometry construction using GUI software (e.g. CAD) is desire
Conventional geometry construction
Import of CAD geometry into PHITS through tetrahedral-mesh geometry
PHITS
CAD: computer-aided design
Various purpose (Engineering design + analysis)
More flexible (higher degree of freedom)
Suited to create complex geometries

--- SLIDE 03 ---
Polygon or CAD
TM geom.
TetGen HP (http://wias-berlin.de/software/tetgen/)
Component = Tetrahedron
(shape and size can be different)
Connecting the triangular surfaces
simple but complex geometries can be formed
Two tetrahedron geom.
Convert
Mesh generation
Tetrahedral-mesh geometry (TM geom.)
PHITS can import TM geom. (phits/utility/TetraGEOM)
3
Conventional Geometry

SPEAKER_NOTES:
45 (3:15)

--- SLIDE 04 ---
CAD (STEP file)
TM geom.
Conversion to TM geom. by Gmsh
4
Conversion by Gmsh
Gmsh (https://gmsh.info/)
Gmsh (version 4. 11. 0 Windows) is used in this lecture
Gmsh
Mesh generation
Windows, Mac, Linux
An open source 3D finite element mesh generator with a build-in CAD engine and post-processor
Other CAD software may be also used if it can export into NASTRAN BDF file (explained later)

SPEAKER_NOTES:
45 (3:15)

--- SLIDE 05 ---
CAD file import
Physical volume tag setting
Tetrahedral-mesh generation
Export in NASTRAN bulk data file
Import to PHITS
Contents
Table of Contents
5

--- SLIDE 06 ---
CAD file import (Gmsh)
6
CAD file import
Run Gmsh
Mac&Linux: Open terminal and type gmsh & Enter
Windows: Double-click executable
Confirmation of overwrite if you still have a file with same name
In desired folder
(phits/utility/CADimport)
open a file with the extension .geo (test.geo)
Choose OpenCASCADE kernel
SAVE

--- SLIDE 07 ---
7
Select a CAD file in STEP format
(snowman.step)
CAD file import
A perfect geometry (water-proof, non-intersection, no overlap) is required
CAD file import (Gmsh)

--- SLIDE 08 ---
8
Option => All geometry options
Show surface and volume points
Y軸垂直描画
Volume point
Surface
Geometry can be rotated by mouse with clicking the left button
CAD file import
Update of Gmsh may be required if volume point dose not appear
CAD file import (Gmsh)

--- SLIDE 09 ---
CAD file import
Physical volume tag setting
Tetrahedral-mesh generation
Export in NASTRAN bulk data file
Import to PHITS
Contents
Table of Contents
9

--- SLIDE 10 ---
Physical volume tag setting (Gmsh)
10
Physical volume tag
Press "e" to set the volume property
The "Name" is not going to implemented in PHITS unfortunately but help sorting
Press "q" to abort
Volume point becomes red when the object is selected by click
The "Tag" will be the universe number of the object in PHITS
Uncheck the box to choose the free "Tag" number
(Hat, 5002)
(Eyes, 5003)
(Nose, 5004)
(Buttons, 5005)
(Body, 5001)

--- SLIDE 11 ---
CAD file import
Physical volume tag setting
Tetrahedral-mesh generation
Export in NASTRAN bulk data file
Import to PHITS
Contents
Table of Contents
11

--- SLIDE 12 ---
四面体メッシュ化 (Gmsh)
12
Tetrahedral-mesh generation
Default 3D meshing will create "tetrahedral mesh"

--- SLIDE 13 ---
CAD file import
Physical volume tag setting
Tetrahedral-mesh generation
Export in NASTRAN bulk data file
Import to PHITS
Contents
Table of Contents
13

--- SLIDE 14 ---
Export in NASTRAN bulk data file (Gmsh)
14
Export NASTRAN bulk data file
Click "File" => "Export"
Select Nastran Bulk Data File (*.bdf)
Specify a file with the extension .bdf
Select "Physical entity" to set physical volume tag
SAVE

--- SLIDE 15 ---
$ Created by Gmsh
GRID    1       0       0.400000-9.8E-171.450000
GRID    2       0       0.400000-9.8E-171.400000
GRID    3       0       0.270000-6.6E-171.450000
GRID    4       0       0.264575-6.5E-171.400000
GRID    5       0       0.270000-6.6E-171.8500000
...
CTETRA  1       5002    162     65      163     177
CTETRA  2       5002    67      160     164     176
CTETRA  3       5002    163     92      77      78
CTETRA  4       5002    159     68      164     173
...
CTETRA  951     5001    75      330     74      148
CTETRA  952     5001    75      74      330     308
CTETRA  953     5001    153     142     139     154
CTETRA  954     5001    153     139     142     322
...
Export in NASTRAN bulk data file (Gmsh)
15
You can check the created BDF file by opening with some text editor
Grid information
Tetra information
x
y
z
Physical volume tag = PHITS universe ID
Grid IDs to form the tetra
Export NASTRAN bulk data file

--- SLIDE 16 ---
CAD file import
Physical volume tag setting
Tetrahedral-mesh generation
Export in NASTRAN bulk data file
Import to PHITS
Contents
Table of Contents
16

--- SLIDE 17 ---
[ Parameters ]
...
itetauto = 0
itgchk  = 1

[ Material ]
MAT[1]   N  78.1  O  20.9  Ar  0.93   $ Air
MAT[2]   H  2       O  1                       $ Water
MAT[3]   Al 1                                     $ Aluminium
...
[ Surface ]
  10  rpp   -80.0  80.0  -80.0  80.0  -20.0  200.0
  20  rpp   -80.1  80.1  -80.1  80.1  -20.1  200.1
  90  so     500.0

[ Cell ]
 101   1 -0.001205   -20  U=1     LAT=3   nfile=snowman
   1   0           -10  FILL=1
   2  -1            10
   2   -1.0      -90  U=5001
5002   3   -7.874  -90  U=5002
...
Import to PHITS
17
itetauto=1 can not be used because the solid and material properties are missing in the created BDF file ( phits/utilitiy/FLUENT)
universe ID
Nastran BDF file name without extension
Filling this material in the region except for tetrahedrons
Option to use TM geom.
TM geom. container (RPP) needs to be sufficiently large to contain all grids of TM
NOTE: Unit of TM geom. by BDF is considered as "meter"
test.inp
More details on the function to import TM geom. => phits/utility/TetraGEOM
By using scaling factor TSFAC=0.01, the geometry can be scaled in "cm"
No need to specify (Default = 0)
Import to PHITS
Tetra-mesh geometry check option 1:on 0: off
=> Will be explained in the next page

--- SLIDE 18 ---
[ Parameters ]
itgchk   = 1
18
Import to PHITS
test.inp
Tetra-mesh geometry check 1:on 0: off
TETRAHEDRAL-MESH GEOM. check has been started  by itgchk= 1
*** TETRA INTERSECTION ERROR: intersection found in itet= 1 between
ielem =      309 jelem =      898
TETRAHEDRAL-MESH GEOM. check has been started  by itgchk= 1
 No error found in TETRAHEDRAL-MESH GEOM. !!
 itgchk=0 to skip TETRAHEDRAL-MESH GEOM check
Found errors
No errors
[ Parameters ]
itgchk   = 0
Geometry drawing or transport calculation after tetra-mesh geometry check
test.inp
=>The intersection will be outputted into tet_geoerr.inp
Check of zero-volume tetrahedrons
Check of irregular intersections
Intersection between tetrahedron 309 and tetrahedron 898 is found
Check by PHIG3D
Import to PHITS
Intersections among tetrahedrons are detected
Zero-volume tetrahedrons are detected
*** TETRA VOLUME ERROR: zero volume tetra found in itet= 1
ielem =  3418602
Zero-volume tetrahedron 3418602 is found
=>The zero-volume tetrahedron is outputted into tet_geoerr.inp
itgchk=1: OpenMP parallelization is  possible

--- SLIDE 19 ---
Import to PHITS
19
Import to PHITS
icntl=11
icntl=8
3D.eps
deposit-xz.eps

--- SLIDE 20 ---
Summary
20
Summary
CAD geom. can be imported to PHITS through TM geom.
PHITS supports NASTRAN bulk data file (explained in this lecture) & TetGen files (.node and .ele).
Gmsh can import CAD data and generate TM geom.
Other CAD software may be also used if it can export into NASTRAN bulk data file (TM geom. + small/long field).
	f.g. Ansys Fluent (phits/utility/FLUENT), MSC Apex

Import of TetGen Files (.node and .ele) is also possible (phits/utility/TetraGEOM)
Note: Mesh needs to be perfect tetrahedral mesh (non-intersecting & water proof).
          Mesh containing other than CTETRA is NOT supported.

--- SLIDE 21 ---
Additional document
Geometry construction by Gmsh
21
Additional document

--- SLIDE 22 ---
A compatible CAD software
22
What is Gmsh
Gmsh (https://gmsh.info/)
An open source 3D finite element mesh generator with a build-in CAD engine and post-processor
Windows
Mac
Linux
Creation of complex 3D geometries using Boolean operations is possible with Gmsh.  Many examples of how to create geometries using Gmsh can be found in the internet

--- SLIDE 23 ---
Geometry construction (Gmsh)
23
Geometry construction
Various shapes of surfaces are prepared
Sub-windows to set parameters will be opened with click

--- SLIDE 24 ---
Geometry construction (Gmsh)
24
Geometry construction
Origin
Size
Create object by clicking button

--- SLIDE 25 ---
Geometry construction (Gmsh)
25
Geometry construction
Press "e" to add the object
You can also navigate the origin of the box by mouse pointer
Press "q" to abort

--- SLIDE 26 ---
Geometry construction (Gmsh)
26
Geometry construction
You can remove the last created geometry by clicking

--- SLIDE 27 ---
Geometry construction (Gmsh)
27
Geometry construction
Let's create two boxes along z axis
Press "q" to abort
View perpendicular to x axis

--- SLIDE 28 ---
Set physical volume tag (Gmsh)
28
Physical volume tag
Press "e" to set the volume property
The "Name" is not going to implemented in PHITS unfortunately but help sorting
Press "q" to abort
Volume point becomes red when the object is selected by click
The "Tag" will be the universe number of the object in PHITS
Uncheck the box to choose the free "Tag" number

--- SLIDE 29 ---
Tetrahedral-mesh generation (Gmsh)
29
Physical volume tag
Default 3D meshing will create "tetrahedral mesh"
END_PPTX_TEXT

FILE: phits-lec-CADimport-jp.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-lec-CADimport-jp.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
PHITS講習会
PHITSへのCAD体系の取り込み方
Title
1
2023年3月改訂

--- SLIDE 02 ---
2
Conventional Geometry
球面
直方体面
円柱面
単純な面形状の組み合わせで体系を表現
=> 複雑な形状を記述するのが大変!
GUIの体系作成ソフトウェア(CAD等)が使えれば便利
従来の体系の記述
四面体メッシュ体系を通して、CADの体系をPHITSに取り込み可能
PHITS
CAD: computer-aided design
様々な目的 (工学的な体系作成 + 分析)
自由度の高い記述が可能
複雑体系の作成に適している

--- SLIDE 03 ---
ポリゴン or CAD
四面体メッシュ体系
TetGen HP (http://wias-berlin.de/software/tetgen/)
構成要素 = 四面体
(各四面体のサイズ・形は異なる)
各三角形の面を隣り合わせた四面体と共有し、複雑な三次元体系を構成可能
Two tetrahedron geom.
変換
メッシュ作成
四面体メッシュ体系
PHITS:四面体メッシュ体系を取り込み可(phits/utility/TetraGEOM)
3
Tetrahedral-mesh Geometry

SPEAKER_NOTES:
45 (3:15)

--- SLIDE 04 ---
CAD (STEPファイル)
四面体メッシュ体系
Gmshによる四面体メッシュへの変換
4
Conversion by Gmsh
Gmsh (https://gmsh.info/)
オープンソース三次元有限要素メッシュ作成ソフト三次元CADエンジンと後処理プログラムが付属
この講義ではGmsh (version 4. 11. 0 Windows)を使用
後述するが、他のソフトでもNASTRAN bulk data fileに出力できれば使用可能
Gmsh
メッシュ作成
Windows, Mac, Linuxに対応

SPEAKER_NOTES:
45 (3:15)

--- SLIDE 05 ---
CADファイルのインポート
体積情報タグの設定
四面体メッシュ化
NASTRAN bulk data fileへの出力
PHITSへの取り込み
講習の流れ
Table of Contents
5

--- SLIDE 06 ---
CADファイルのインポート(Gmsh)
6
CAD file import
Gmshを起動
Mac&Linux: 端末でgmshとタイプしてEnter
Windows: exeをダブルクリック
既に同名のファイルが存在する場合は上書きの確認
適当なフォルダ
(phits/utility/CADimport)で.geo拡張子のファイルを新規作成 (test.geo)
OpenCASCADEカーネルを選択

--- SLIDE 07 ---
CADファイルのインポート(Gmsh)
7
STEP形式のCADファイルを選択
(snowman.step)
CAD file import
完全な体系(水密、非交差、不重複)である必要あり

--- SLIDE 08 ---
CADファイルのインポート(Gmsh)
8
Option => All geometry options
面・体積点を表示
Y軸垂直描画
体積点
面
左クリックを押しながらのマウス移動で体系を回転
CAD file import
体積点が現れない場合はGmshを新しいバージョンに更新が必要

--- SLIDE 09 ---
CADファイルのインポート
体積情報タグの設定
四面体メッシュ化
NASTRAN bulk data fileへの出力
PHITSへの取り込み
講習の流れ
Table of Contents
9

--- SLIDE 10 ---
体積情報タグの設定 (Gmsh)
10
Physical volume tag
eボタンで体積情報の付加
名称はPHITSに引き継げないが整理する上で付けることを推奨
qボタンで終了
体積代表点をクリック
赤色に変わる=選択状態
タグ番号はPHITS内の物質のuniverse 番号となる
自由にタグ番号を指定するためにチェックを外す
(Hat, 5002)
(Eyes, 5003)
(Nose, 5004)
(Buttons, 5005)
(Body, 5001)
*体積情報を付加しようとすると体系が消えてしまう場合は再度MergeによりSTEPファイルをインポートし直す

--- SLIDE 11 ---
CADファイルのインポート
体積情報タグの設定
四面体メッシュ化
NASTRAN bulk data fileへの出力
PHITSへの取り込み
講習の流れ
Table of Contents
11

--- SLIDE 12 ---
四面体メッシュ化 (Gmsh)
12
Tetrahedral-mesh generation
デフォルトの三次元メッシュ化オプションで四面体メッシュ体系が作成可能

--- SLIDE 13 ---
CADファイルのインポート
体積情報タグの設定
四面体メッシュ化
NASTRAN bulk data fileへの出力
PHITSへの取り込み
講習の流れ
Table of Contents
13

--- SLIDE 14 ---
NASTRAN bulk data fileへの出力 (Gmsh)
14
Export NASTRAN bulk data file
File => Exportと順にクリック
Nastran Bulk Data File (*.bdf)を選択
拡張子に.bdfを付けたファイル名を指定
体積情報をタグにしようするためPhysical entityを選択

--- SLIDE 15 ---
NASTRAN bulk data fileへの出力 (Gmsh)
15
Export NASTRAN bulk data file
テキストエディタで出来たBDFファイルの中身を確認
$ Created by Gmsh
GRID    1       0       0.400000-9.8E-171.450000
GRID    2       0       0.400000-9.8E-171.400000
GRID    3       0       0.270000-6.6E-171.450000
GRID    4       0       0.264575-6.5E-171.400000
GRID    5       0       0.270000-6.6E-171.8500000
...
CTETRA  1       5002    162     65      163     177
CTETRA  2       5002    67      160     164     176
CTETRA  3       5002    163     92      77      78
CTETRA  4       5002    159     68      164     173
...
CTETRA  951     5001    75      330     74      148
CTETRA  952     5001    75      74      330     308
CTETRA  953     5001    153     142     139     154
CTETRA  954     5001    153     139     142     322
...
グリッド点情報
四面体情報
x
y
z
体積情報タグ = PHITSのuniverse番号
四面体を構成するグリッド点番号

--- SLIDE 16 ---
CADファイルのインポート
体積情報タグの設定
四面体メッシュ化
NASTRAN bulk data fileへの出力
PHITSへの取り込み
講習の流れ
Table of Contents
16

--- SLIDE 17 ---
[ Parameters ]
...
itetauto = 0  # (D=0) =1 Automatic mode for tetrahedrons
itgchk   = 1  # (D=0) Tetra-mesh geometry check 0: off 1: on

[ Material ]
MAT[1]   N  78.1  O  20.9  Ar  0.93   $ Air
MAT[2]    H  2      O  1                       $ Water
MAT[3]    Al 1                                    $ Alminium
...
[ Surface ]
  10  rpp   -80.0  80.0  -80.0  80.0  -20.0  200.0
  20  rpp   -80.1  80.1  -80.1  80.1  -20.1  200.1
  90  so     500.0

[ Cell ]
 101   1 -0.001205   -20  U=1     LAT=3   nfile=snowman
   1   0           -10  FILL=1
   2  -1            10
   2   -1.0      -90  U=5001
5002   3   -2.7      -90  U=5002
...
PHITSへの取り込み
17
Import to PHITS
itetauto=1は作成されたBDFファイル内に物体情報が無いため使用不可 ( phits/utilitiy/FLUENT)
Universe番号
拡張子無しでNastran BDF file名を指定
領域内の四面体メッシュ体系以外をこの物質で満たす
四面体メッシュ体系の使用
四面体メッシュ体系全体を内包する十分な大きさの直方体 (RPP)が必要
注意: PHITSではBDFの単位をメートルとして解釈
test.inp
四面体メッシュ体系の取り込みに関する詳細=> phits/utility/TetraGEOM
BDFの読み込みでスケールTSFAC=0.01を指定すれば,センチメートルに変換可
デフォルト=0なので指定の必要無し
四面体メッシュ体系のチェック 1:on 0: off
    => 次のページ

--- SLIDE 18 ---
[ Parameters ]
itgchk   = 1
PHITSへの取り込み
18
Import to PHITS
test.inp
四面体メッシュ体系のチェック 1:on 0: off
*** TETRA INTERSECTION ERROR: intersection found in itet= 1 between
ielem =      309 jelem =      898
TETRAHEDRAL-MESH GEOM. check has been started  by itgchk= 1
 No error found in TETRAHEDRAL-MESH GEOM. !!
 itgchk=0 to skip TETRAHEDRAL-MESH GEOM check
体系にエラーがある場合
体系にエラーがない場合
[ Parameters ]
itgchk   = 0
体系チェックを終え、体系描画や輸送計算を実行
test.inp
=>四面体同士の交差の体系をtet_geoerr.inpに出力
・四面体メッシュ体系内の各四面体の体積がゼロ(異常)でないかチェック
・四面体メッシュ体系内に四面体同士の交差(異常)があるかどうかチェック
四面体309と四面体898に交差あり(異常検知)
PHIG3Dで状況確認できる
・交差のある四面体同士を検知して出力
・体積ゼロの四面体を検知して出力
*** TETRA VOLUME ERROR: zero volume tetra found in itet= 1
ielem =  3418602
体積がゼロの四面体3418602を発見(異常検知)
=>体積ゼロの四面体をtet_geoerr.inpに出力
itgchk=1: OpenMP並列可

--- SLIDE 19 ---
19
Import to PHITS
icntl=11
icntl=8
3D.eps
deposit-xz.eps
PHITSへの取り込み

--- SLIDE 20 ---
まとめ
20
Summary
四面体メッシュ体系を通してPHITSではCAD体系の取り込みが可能
PHITSではNASTRAN bulk data file (この講習) と TetGen files (.node and .ele)に対応
GmshではSTEP形式のCADデータを読み込み、四面体メッシュ化することが可能
NASTRAN bulk data file (四面体メッシュ体系 + small/long field)への出力に対応しているソフトであれば他のCADソフトも使用可
      例:ANSYS FLUENT(phits/utility/FLUENT), MSC Apex

TetGen file (.node and .ele)についてはphits/utility/TetraGEOMを参照
但し、完全な四面体メッシュ体系である必要があり、メッシュにCTETRA以外のものが含まれている体系や交差等の不備がある体系には未対応

--- SLIDE 21 ---
追加資料
Gmshを使った体系作成
Additional document
21

--- SLIDE 22 ---
対応CAD ソフトウェア
22
What is Gmsh
Gmsh (https://gmsh.info/)
オープンソース三次元有限要素メッシュ作成ソフト
三次元CADエンジンと後処理プログラムが付属
Windows
Mac
Linuxに対応
Gmshではブーリアン演算等を含めた複雑な三次元体系の作成が可能。様々な使用例がネット上で公開されている

--- SLIDE 23 ---
体系作成 (Gmsh)
23
Geometry construction by Gmsh
様々な形状が用意されている
クリックするとパラメータを設定するためのサブウィンドウが表示される

--- SLIDE 24 ---
体系作成 (Gmsh)
24
原点位置
サイズ
クリックで体系を作成
Geometry construction by Gmsh

--- SLIDE 25 ---
体系作成 (Gmsh)
25
キーボードのeで体系作成
マウスポインタ―を画面上に移動されて原点位置を設定することも可能
qボタンで終了
Geometry construction by Gmsh

--- SLIDE 26 ---
体系作成 (Gmsh)
26
ここをクリックすることで、最後の操作で作成したオブジェクトを消すことができる
Geometry construction by Gmsh

--- SLIDE 27 ---
体系作成 (Gmsh)
27
ここでは、Z軸に並んだ二つの直方体を作成する
qボタンを押して終了
ここをクリックすることで視点をX軸に垂直な面に変更
Geometry construction by Gmsh

--- SLIDE 28 ---
体積情報タグの設定 (Gmsh)
28
eボタンで体積情報の付加
名称はPHITSに引き継げないが整理する上で付けることを推奨
qボタンで終了
体積代表点をクリック
赤色に変わる=選択状態
タグ番号はPHITS内の物質のuniverse 番号となる
自由にタグ番号を指定するためにチェックを外す
Geometry construction by Gmsh

--- SLIDE 29 ---
四面体メッシュ化 (Gmsh)
29
デフォルトの三次元メッシュ化オプションで四面体メッシュ体系が作成可能
Geometry construction by Gmsh
END_PPTX_TEXT

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: test.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: snowman.bdf
FILE: snowman.step
