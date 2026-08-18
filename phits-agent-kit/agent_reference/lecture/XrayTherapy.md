# Lecture: therapy/XrayTherapy

SOURCE_FOLDER: D:/NEAgit/lecture/therapy/XrayTherapy
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: XrayTherapy
LECTURE_PATH_INDEX: lecture/therapy/XrayTherapy
PPTX_FILES: phits-lec-XrayTherapy-en.pptx, phits-lec-XrayTherapy-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: XrayTherapy, XrayTherapy-final
SECTION_KEYWORDS: counter, t-cross, t-track, transform

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/therapy/XrayTherapy
LECTURE_PATH_INDEX: lecture/therapy/XrayTherapy
PPTX_FILES: phits-lec-XrayTherapy-en.pptx, phits-lec-XrayTherapy-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 2
SLIDE_COUNT: 70
EXERCISE_SLIDE_COUNT: 31
BONUS_INPUT_COUNT: 11
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- XrayTherapy-final.inp
- XrayTherapy.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Dosimetry Simulation for X-ray therapy
- SLIDE 02: Purpose of this lecture
- SLIDE 03: Target design
- SLIDE 04: Geometry
- SLIDE 05: Simulation Results
- SLIDE 06: EXERCISE 1 | Exercise 1: Check geometry
  ANSWER_FILE: (missing)
- SLIDE 07: Answer 1
- SLIDE 08: Geometry around Target
- SLIDE 09: EXERCISE 2 | Exercise 2
  ANSWER_FILE: (missing)
- SLIDE 10: Answer 2
- SLIDE 11: Target design
- SLIDE 12: EXERCISE 3 | Exercise 3
  ANSWER_FILE: (missing)
- SLIDE 13: Answer 3
- SLIDE 14: EXERCISE 4 | Exercise 4
  ANSWER_FILE: (missing)
- SLIDE 15: Answer 4
- SLIDE 16: EXERCISE 5 | Exercise 5
  ANSWER_FILE: (missing)
- SLIDE 17: Answer 5
- SLIDE 18: Target design
- SLIDE 19: EXERCISE 6 | Exercise 6: Add JAW collimators
  ANSWER_FILE: (missing)
- SLIDE 20: Answer 6
- SLIDE 21: EXERCISE 7 | 5cm
  ANSWER_FILE: (missing)
- SLIDE 22: How to set up [transform]
- SLIDE 23: Answer 7
- SLIDE 24: EXERCISE 8 | Exercise 8
  ANSWER_FILE: (missing)
- SLIDE 25: Answer 8
- SLIDE 26: Target design
- SLIDE 27: EXERCISE 9 | Exercise 9
  ANSWER_FILE: (missing)
- SLIDE 28: Answer 9
- SLIDE 29: EXERCISE 10 | Exercise 10
  ANSWER_FILE: (missing)
- SLIDE 30: Answer 10
- SLIDE 31: Target design
- SLIDE 32: Summary
- SLIDE 33: Homework
- SLIDE 34: Sample Answer（XrayTherapy-final.inp）
- SLIDE 35: track_xz.eps
- SLIDE 01: X線治療の線量評価シミュレーション
- SLIDE 02: 本実習の目標
- SLIDE 03: ターゲットの設計
- SLIDE 04: 計算体系
- SLIDE 05: 実行確認
- SLIDE 06: EXERCISE 1 | 課題1：ターゲット周辺の体系確認
  ANSWER_FILE: (missing)
- SLIDE 07: EXERCISE 1 | 課題1の解答
  ANSWER_FILE: (missing)
- SLIDE 08: ターゲット周辺の体系確認
- SLIDE 09: EXERCISE 2 | 課題2：コリメータホールを変更
  ANSWER_FILE: (missing)
- SLIDE 10: EXERCISE 2 | 課題2の解答
  ANSWER_FILE: (missing)
- SLIDE 11: ターゲットの設計
- SLIDE 12: EXERCISE 3 | 課題3：Dump線源作成の準備
  ANSWER_FILE: (missing)
- SLIDE 13: EXERCISE 3 | 課題3の解答
  ANSWER_FILE: (missing)
- SLIDE 14: EXERCISE 4 | 課題4：Dump線源の作成
  ANSWER_FILE: (missing)
- SLIDE 15: EXERCISE 4 | 課題4の解答
  ANSWER_FILE: (missing)
- SLIDE 16: EXERCISE 5 | 課題5：Dump線源の利用
  ANSWER_FILE: (missing)
- SLIDE 17: EXERCISE 5 | 課題5の解答
  ANSWER_FILE: (missing)
- SLIDE 18: ターゲットの設計
- SLIDE 19: EXERCISE 6 | 課題6：閉口状態のコリメータを設置
  ANSWER_FILE: (missing)
- SLIDE 20: EXERCISE 6 | 課題6の解答
  ANSWER_FILE: (missing)
- SLIDE 21: EXERCISE 7 | 5cm
  ANSWER_FILE: (missing)
- SLIDE 22: 角度単位オプション
- SLIDE 23: EXERCISE 7 | 課題7の解答
  ANSWER_FILE: (missing)
- SLIDE 24: EXERCISE 8 | 課題8：粒子輸送計算を実行
  ANSWER_FILE: (missing)
- SLIDE 25: EXERCISE 8 | 課題8の解答
  ANSWER_FILE: (missing)
- SLIDE 26: ターゲットの設計
- SLIDE 27: EXERCISE 9 | 課題9：照射条件の変更
  ANSWER_FILE: (missing)
- SLIDE 28: EXERCISE 9 | 課題9の解答
  ANSWER_FILE: (missing)
- SLIDE 29: EXERCISE 10 | 課題10：散乱線の影響を評価
  ANSWER_FILE: (missing)
- SLIDE 30: EXERCISE 10 | 課題10の解答
  ANSWER_FILE: (missing)
- SLIDE 31: ターゲットの設計
- SLIDE 32: まとめ
- SLIDE 33: EXERCISE 10 | 宿題
  ANSWER_FILE: (missing)
- SLIDE 34: 宿題の解答例（詳細はXrayTherapy-final.inp）
- SLIDE 35: 宿題の解答例（詳細はXrayTherapy-final.inp）

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: XrayTherapy-final.inp
FILE: XrayTherapy.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Dosimetry Simulation for X-ray therapy
Last revised: Sep. 2025
phits/lecture/therapy/XrayTherapy

--- SLIDE 02 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Purpose of this lecture
To learn how to apply PHITS to dosimetry of X-ray therapy
Results of PHITS simulation at the end of this lecture
Reproduce geometry around the target
Reduce computational time by introducing 2-step calculation
Reproduce JAW collimator
Analyze the influence of scattered radiations using [counter]

--- SLIDE 03 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Target design
2-step calculation
Design of JAW collimator
Changing the irradiation conditions
Summary & homework
Table of Contents

--- SLIDE 04 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Geometry
Electron
10 MeV
Target
XrayTherapy.inp
Water phantom
c1 x c1 x c1 cm3
W(0.1×2cmΦ)
+ Cu(0.9×2cmΦ)
Collimator
Air hole: 6 x 2cmΦ
Tungsten alloy: 6 x 20cmΦ
Photon
c2 = 70 cm
(c1 = 30 cm)
Flattening filter
Cone-shape Cu:
(1.5cm x 16cmΦ）
track_xz.eps
drawn with icntl = 8
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 05 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Simulation Results
track_xz.eps
track_xy.eps
PDD.eps
OCR.eps
PDD
OCR
All tally results are normalized to per electron source generation
Page 1
Page 1

--- SLIDE 06 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1: Check geometry
Set to icntl = 8  (geometry check mode)
Enlarge the target area by changing zmax of [t-track] with file=track_xz.out to 15 cm
Enlarge this area
Size of water phantom is defined by c1（30cm）
Distance from the target to the surface of water phantom is defined by c2 （70cm）
Area for drawing this figure is defined as -5.0 < z < c1 + c2 + 5.0
c2
c1
c1
ANSWER_FILE: (missing)

--- SLIDE 07 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 1
XrayTherapy.inp
track_xz.eps
[ P a r a m e t e r s ]
 icntl    =           8
…
[ T - T r a c k ]
    title = Track in xyz
z-type =    2
     zmin =  -5.0
     zmax =   15.0
$     zmax =   c1+c2+5.0
       nz =  110
…
axis =   xz
     file = track_xz.out
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Geometry around Target
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012   3 -4 -11    $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
…
XrayTherapy.inp
track_xz.eps
Definition of collimator
Center of the bottom circle (vx  vy  vz)
Vector from the bottom to top circle
(hx  hy  hz)
Top radius r2
Flattening filter is defined by a trc surface
 (truncated right-angle cone)
Bottom radius r1
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
31 trc  0.0 0.0 8.0   0.0 0.0 -1.5   8.0 0.1
Definition of trc: surfaceID  trc  vx vy vz  hx hy hz  r1 r2
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
Define new trc surface in [surface]
Adjust its parameter as shown below
Replace cylindrical air hole to newly defined trc
Let’s : Change the shape of Collimator hole to truncated right-angle cone (trc)
r1 = 2 cm
r2 = 0.5 cm
6 cm
Center of the bottom circle (vx  vy  vz)
Vector from the bottom to top circle
(hx  hy  hz)
(0    0    6)
(0    0    -6)
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012   3 -4 -11    $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
…
XrayTherapy.inp
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
31 trc  0.0 0.0 8.0   0.0 0.0 -1.5   8.0 0.1
32 trc  **   **  **   **  **    **   **   **
Definition of trc: surfaceID  trc  vx vy vz  hx hy hz  r1 r2
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 10 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 2
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012  -32    $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
…
XrayTherapy.inp
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
31 trc  0.0 0.0 8.0   0.0 0.0 -1.5   8.0 0.1
32 trc  0.0 0.0 6.0   0.0 0.0 -6.0   2.0  0.5
track_xz.eps
Definition of trc: surfaceID  trc  vx vy vz  hx hy hz  r1 r2
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Target design
2-step calculation
Design of JAW collimator
Changing the irradiation conditions
Summary & homework
Table of contents
Table of Contents

--- SLIDE 12 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
Define a new surface where the dump source file is generated as “ 5 pz 10.0”
Comment out cell 21 (water phantom) and define a new “outer void” cell for area with z over 10 cm (positive side of surface 5)
Execute PHITS and check the geometry
Geometry around the target is generally not changed.
It is beneficial to employ the 2-step calculation* by generating the dump source behind the target area
For that purpose, it is necessary to define “outer void” behind the target area
*Please see /phits/lecture/advanced/sourceB in detail
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012   -32        $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
$ 21   1 -1.0    -21          $ Water phantom
 21  **  **
XrayTherapy.inp
[ S u r f a c e ]
 1   pz  -1.0
 2   pz  -0.9
 3   pz   0.0
 4   pz   6.0
 5   pz   10.0
・ ・ ・ ・ ・ ・
Procedures of this exercise
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 13 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 3
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012   -32        $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
$ 21   1 -1.0    -21          $ Water phantom
 21  -1 5
…
XrayTherapy.inp
[ S u r f a c e ]
 1   pz  -1.0
 2   pz  -0.9
 3   pz   0.0
 4   pz   6.0
 5   pz   10.0
・ ・ ・ ・ ・ ・
track_xz.eps
Outer void
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
Set icntl = 0
Increase maxbch to 50*
Remove “off” for the last [t-cross] to store the particle information
Execute PHITS
Check the existence of “cross.out” & “cross_dmp.out”
Let’s generate the dump source file with sufficient source particles by executing the 1st-step PHITS simulation
*It is OK to terminate the PHITS simulation if the computational time is too long
[ T - C r o s s ] off
    title = Energy distribution in region mesh
     mesh =  reg
      reg =    1
      r-from  r-to  area
          98    21   1.0
   e-type =    2
     emin =   0.0
     emax =   1000.0
       ne =    1
     unit =    1
    axis =  eng
     file = cross.out
   output = flux
     part =  all
     dump =  -11
 1 2 3 4 5 6 7 8 9 18 19
XrayTherapy.inp
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 15 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 4
track_xz.eps
Photon fluence (page 1)
track_xz.eps
Electron fluence (page 2)
Dump source generation surface

--- SLIDE 16 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Add “off” behind the 1st [source] and remove “off” behind 2nd [source]
Change the definition of cell 21 (outer void) to the original one (water phantom)
Change zmax of [t-track] with “file = track_xz.eps”  back to c1+c2+5.0
Add “off” behind the last [t-cross] (not to generate the dump source again)
Execute PHITS and check PDD.eps & OCR.eps
Let’s perform 2nd-step simulation for calculating PDD* & OCR**
*Percentage Depth Dose,   **Off-Center Ratio
[ C e l l ]
…
$ 21   1 -1.0    -21
   21  -1  5
…
XrayTherapy.inp
[ S o u r c e ]
   s-type =   1
...

[ S o u r c e ] off
   s-type =  17
     file =  cross_dmp.out
     dump =  0
[ T - T r a c k ]
    title = Track in xyz
z-type =    2
     zmin =  -5.0
     zmax =   15.0
$     zmax =   c1+c2+5.0
       nz =  110
…
axis =   xz
     file = track_xz.out
[ T - C r o s s ]
…
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 17 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 5
track_xz.eps
track_xy.eps
PDD
OCR
Page 2
OCR.eps
1ページ目
PDD.eps
Slightly build-up and decrease
Almost flat distribution
All tally results are normalized to per electron source generation

--- SLIDE 18 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Target design
2-step calculation
Design of JAW collimator
Changing the irradiation conditions
Summary & homework
Table of contents
Table of Contents

--- SLIDE 19 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6: Add JAW collimators
In X-ray therapy, the irradiation field size is determined by JAW collimators, which can be rotated at a certain point around the target
Let’s reproduce the JAW collimators at the close position
track_xz.eps
Change icntl = 8 for checking geometry
Add 2 rpp surfaces in [surface] with sizes of (0 < x < 20 cm or -20 < x < 0 cm） & (-10 cm < y < 10 cm) & （30 < z < 40 cm）
Add 2 cells using the above rpp surfaces filled with Tungsten alloy (material 5) with density of 17g/cm3
Remove the newly defined cells from cell 98 (air region)
Newly defined cells
ANSWER_FILE: (missing)

--- SLIDE 20 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 6
track_xz.eps
[ C e l l ]
…
 22   5 -17.0   -22          $ JAW1
 23   5 -17.0   -23          $ JAW2
 98   2 -0.0012  #1 #2 #3 #4 #5 #21 #22 #23  -999  $ Air
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
21  rpp  -c1/2 c1/2  -c1/2 c1/2    c2 c2+c1
22  rpp    0.0 20.0  -10.0 10.0  30.0 40.0
23  rpp  -20.0  0.0  -10.0 10.0  30.0 40.0
XrayTherapy.inp
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 21 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
5cm
Exercise 7
Let’s rotate the JAW collimators around the origin (target location)
Rotational angle can be determined from the field size and the distance between the target and water phantom
In this lecture, let’s set the field size to 10 cm → θ = atan(5.0/c2)
track_xz.eps
Change tr1 & tr2 in [transform] for rotating with angle of atan(5.0/c2) and -atan(5.0/c2), respectively, around the Y axis
Apply tr1 & tr2 to JAW cells → Add trcl=1 & trcl=2 in their cell definitions
Run PHITS and check the geometry
θ
c2 cm
tan(θ) = 5.0/c2      atan(5.0/c2) = θ
10cm
ANSWER_FILE: (missing)

--- SLIDE 22 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
How to set up [transform]
[ Transform ]
*Trn      X0  Y0  Z0        XC  YC  ZC     A1  θ1     A2  θ2     A3  θ3      M
Order of translation & rotation
M=3：rotation → translation
M=-3：translation → rotation
Translation component
*Axis (Ai) & angle (θi) for ith rotation
ID number
Example 1: *tr1    0.0 0.0 5.0      0.0 10.0 0.0     2 45.0     3 -60.0      0 0.0      3

Example 2：  tr1    0.0 0.0 -5.0      0.0 0.0 0.0     1  pi/4       0 0.0       0 0.0      -3
Angle unit option
with *: degree
without *: radian
To define a transformation, an ID and 13 parameters are needed.
1, Define a [transform] section
2, Use this [transform] by setting trcl=n in [cell], [source], etc.
Center of rotation
Rotating at the center of (0 10 0) around Y-axis by 45 deg and Z-axis by -60 deg, and then translating along +Z-axis by 5 cm.
Translating along +Z-axis by 5cm, and then rotating at the center of (0 0 0) around X-axis by 45 deg. (Note that when M=-3, direction of translation is opposite to that in M=3)
*Ai=1,2, & 3 indicate the rotation around X, Y, & Z axes, respectively

--- SLIDE 23 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 7
track_xz.eps
[ C e l l ]
…
 22   5 -17.0   -22 trcl=1   $ JAW1
 23   5 -17.0   -23 trcl=2   $ JAW2
 98   2 -0.0012  #1 #2 #3 #4 #5 #21 #22 #23  -999  $ Air
[ Transform ]
tr1    0  0  0    0  0  0    2  atan(5.0/c2)  0  0  0  0    3
tr2    0  0  0    0  0  0    2 -atan(5.0/c2)  0  0  0  0    3
XrayTherapy.inp
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 24 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Exercise 8
Let’s run PHITS by setting icntl = 0 to check PDD & OCR
track_xz.eps
track_xy.eps
Page 2
Page 4
Page 8
ANSWER_FILE: (missing)

--- SLIDE 25 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 8
PDD.eps
Page 1 (0 ~ 6cm)
Page 3 (12 ~ 18 cm)
Page 5 (24 ~ 30 cm)
OCR.eps
10 cm
Doses are decreased very much due to the introduction of JAW collimators*
Field edges become vague with increase of the depth
*Because the tally region was set to wider than the field size

--- SLIDE 26 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Target design
2-step calculation
Design of JAW collimator
Changing the irradiation conditions
Summary & homework
Table of contents
Table of Contents

--- SLIDE 27 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
Exercise 9
Let’s change the phantom location and field size
Change the distance from the target to phantom surface to 100 cm
Double the field size to (-10cm < x < 10cm)
Run PHITS and check track_xz.eps & OCR.eps
[ S u r f a c e ]
set:c1[30.0] $ size of cubic water phantom
set:c2[70.0] $ distance from the target to water phantom
…
[ Transform ]
tr1    0  0  0    0  0  0    2  atan(5.0/c2)  0  0  0  0    3
tr2    0  0  0    0  0  0    2 -atan(5.0/c2)  0  0  0  0    3
XrayTherapy.inp
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 28 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 9
[ Transform ]
tr1    0  0  0    0  0  0    2  atan(10.0/c2)  0  0  0  0    3
tr2    0  0  0    0  0  0    2 -atan(10.0/c2)  0  0  0  0    3
XrayTherapy.inp
track_xz.eps
[ S u r f a c e ]
set:c1[30.0]
set:c2[100.0]
…
OCR.eps
20 cm
Field size is rather stable at the deeper locations in comparison to the previous case
Page 1 (0 ~ 6cm)
Page 3 (12 ~ 18 cm)
Page 5 (24 ~ 30 cm)
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
Exercise 10
Let’s check the influence of the JAW collimators using [counter]*
Remove “off” behind [counter]
Change [counter] to add +1 to counter#1 when a collision (coll) occurs in the JAW collimators (reg = 22 & 23)
Add ctmin(1)=1 to [t-track] with file=track_xz.out in order to tally only radiations scattered in the JAW collimators (i.e. radiation having counter#1 more than 0).
[ Counter ] off
  counter = 1
     part =  photon
     reg        in
      21         1
XrayTherapy.inp
In the original setting, add +1 to counter#1 when radiation goes into cell 21
You have to use () when you would like to combine two cells in one definition
  e.g.: (22 23)
*Please see phits/lecture/advanced/options in detail
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 30 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Answer 10
[ Counter ]
  counter = 1
     part =  photon
     reg       coll
 (22 23)         1
XrayTherapy.inp
[ t-track ]
…
 file = track_xz.out    # file name of output for the above axis
     part =  photon electron
    gshow =    3            # 0: no 1:bnd, 2:bnd+mat, 3:bnd+reg 4:bnd+lat
   epsout =    1            # (D=0) generate eps file by ANGEL
 ctmin(1) =    1
track_xz.eps
Scattered photons hardly reach the water phantom
(Almost no influence on PDD and OCR)
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Target design
2-step calculation
Design of JAW collimator
Changing the irradiation conditions
Summary & homework
Table of contents
Table of Contents

--- SLIDE 32 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Summary
It is beneficial to introduce the 2-step calculation when you need to run PHITS simulations by changing the irradiation conditions several times
JAW collimator can be easily reproduced using [transform]
Influence of scattered radiations can be estimated using [counter]
Phase space file is better to be used when it is available for your X-ray generator
Please see phits/utility/PSFC4PHITS in more detail

--- SLIDE 33 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Homework
The field size only in X-direction is collimated in this lecture
Let’s add JAW collimators to adjust the field size in Y-direction to 20 cm
Delete “ctmin(1) = 1” in [t-track]
Make a new [t-track] with file = track_yz.out by referring that with file = track_xy.out

Define two rpp surfaces in [surface] with the sizes of (-10 cm < x < 10 cm) & (0 < y < 20 cm or -20 < y < 0 cm) & (45 < z < 55 cm)
Add tr3 and tr4 in [transform] for rotating along the X-axis

Define two cells using newly defined surfaces and transforms
Check the geometry by setting icntl = 8
Run PHITS simulation by setting icntl = 0
→ You have to change axis, nx, xmin, xmax, ny, ymin, ymax, & file
→ Be careful with the rotational direction!
If you cannot finish the previous exercises, please use input/XrayTherapy-homework.inp
MENTIONED_INPUT_NAMES: XrayTherapy-homework.inp

--- SLIDE 34 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
Sample Answer（XrayTherapy-final.inp）
track_yz.eps with icntl = 8
Geometry drawn by PHIG-3D
MENTIONED_INPUT_NAMES: XrayTherapy-final.inp

--- SLIDE 35 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
track_xz.eps
track_yz.eps
track_xy.eps
20 cm < z < 33 cm
33 cm < z < 46 cm
46 cm < z < 59 cm
97 cm < z < 110 cm
Sample Answer（XrayTherapy-final.inp）
MENTIONED_INPUT_NAMES: XrayTherapy-final.inp

--- SLIDE 01 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
X線治療の線量評価シミュレーション
phits/lecture/therapy/XrayTherapy
2025年9月改訂

--- SLIDE 02 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
本実習の目標
X線治療を模擬するための様々なテクニックを習得する
本実習の最後で実施する10MVのX線治療装置を模擬したシミュレーション結果
ターゲット周辺の体系作成
２段階計算による計算時間短縮
JAWコリメータの設置
[counter]を活用した散乱線の影響評価

--- SLIDE 03 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
ターゲットの設計
２段階計算（Dump線源の作成と利用）
JAWコリメータの設置
照射条件の変更と高度な解析
まとめと宿題
実習内容

--- SLIDE 04 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
計算体系
電子線
10 MeV
標的
XrayTherapy.inp
水ファントム
c1 x c1 x c1 cm3
W(0.1×2cmΦ)
+ Cu(0.9×2cmΦ)
コリメータ
空気穴：6×2cmΦ
タングステン合金：6×20cmΦ
光子
c2 = 70 cm
(c1 = 30 cm)
Flattening filter
円錐状のCu：
(1.5cm x 16cmΦ）
track_xz.eps
drawn with icntl = 8
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 05 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
実行確認
track_xz.eps
track_xy.eps
PDD.eps
OCR.eps
PDD
OCR
全てのタリー結果は、相対値ではなく１電子発生辺りに規格化
1ページ目
1ページ目

--- SLIDE 06 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1：ターゲット周辺の体系確認
icntl = 8としてジオメトリ確認モードにする
[t-track]のfile=track_xz.outに対するzmaxを小さくして(15cm）、ターゲット付近を拡大
この部分を拡大
水ファントムの大きさはc1（30cm）、
ターゲットから水ファントムまでの距離はc2（70cm）
描画の範囲は-5.0 < z < c1 + c2 + 5.0で定義
c2
c1
c1
ANSWER_FILE: (missing)

--- SLIDE 07 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1の解答
XrayTherapy.inp
track_xz.eps
[ P a r a m e t e r s ]
 icntl    =           8
…
[ T - T r a c k ]
    title = Track in xyz
z-type =    2
     zmin =  -5.0
     zmax =   15.0
$     zmax =   c1+c2+5.0
       nz =  110
…
axis =   xz
     file = track_xz.out
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 08 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
ターゲット周辺の体系確認
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012   3 -4 -11    $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
…
XrayTherapy.inp
track_xz.eps
コリメータは太い円柱（cell 3）から細い円柱（cell 4）をくり抜いている
底面の中心の座標(vx  vy  vz)
底面中心から上面中心へのベクトル
(hx  hy  hz)
半径r2
フラットニングフィルタはカットされた円錐（trc）で表現
半径r1
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
31 trc  0.0 0.0 8.0   0.0 0.0 -1.5   8.0 0.1
trcの定義は「面番号 trc  vx  vy  vz  hx  hy  hz  r1 r2 」
MENTIONED_INPUT_NAMES: XrayTherapy.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2：コリメータホールを変更
[surface]で新たなtrc（カットされた円錐）を定義
下の図のような形状になるようパラメータを調整
円柱のコリメータホールを上記trcに置き換える
実際のコリメータホールは、徐々に口径が拡がっていくカットされた円錐
r1 = 2 cm
r2 = 0.5 cm
6 cm
底面の中心の座標(vx  vy  vz)
底面中心から上面中心へのベクトル(hx  hy  hz)
(0    0    6)
(0    0    -6)
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012   3 -4 -11    $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
…
XrayTherapy.inp
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
31 trc  0.0 0.0 8.0   0.0 0.0 -1.5   8.0 0.1
32 trc  **   **  **   **  **    **   **   **
trcの定義は「面番号 trc  vx  vy  vz  hx  hy  hz  r1 r2 」
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 10 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2の解答
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012  -32    $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
…
XrayTherapy.inp
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
31 trc  0.0 0.0 8.0   0.0 0.0 -1.5   8.0 0.1
32 trc  0.0 0.0 6.0   0.0 0.0 -6.0   2.0  0.5
track_xz.eps
trcの定義は「面番号 trc  vx  vy  vz  hx  hy  hz  r1 r2 」
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 11 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
ターゲットの設計
２段階計算（Dump線源の作成と利用）
JAWコリメータの設置
照射条件の変更と高度な解析
まとめと宿題
Table of contents
実習内容

--- SLIDE 12 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題3：Dump線源作成の準備
粒子情報を保存したい面（pz 10.0）を面番号５として定義する
水ファントム（セル番号２１）をコメントアウトし、面番号５の＋側全ての領域を外部ボイドとして再定義する
PHITSを実行して2重定義や未定義領域がないか確認する
ターゲット周辺の計算は時間が掛かるため、様々な条件（照射野サイズ、ファントム位置）に対して計算するためには、ターゲット後方における粒子情報（Dump線源）を保存して２段階計算にすると便利
2段階計算の詳細は/phits/lecture/advanced/sourceBを参照
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012   -32        $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
$ 21   1 -1.0    -21          $ Water phantom
 21  **  **
XrayTherapy.inp
[ S u r f a c e ]
 1   pz  -1.0
 2   pz  -0.9
 3   pz   0.0
 4   pz   6.0
 5   pz   10.0
・ ・ ・ ・ ・ ・
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 13 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題3の解答
[ C e l l ]
 1    3 -19.25    1 -2 -11    $ W for X-ray generator
 2    4 -8.94     2 -3 -11    $ Cu for X-ray generator
 3    5 -17.0     3 -4 -12 #4 $ Collimator with hole
 4    2 -0.0012   -32        $ Hole in the collimator
 5    4 -8.94   -31          $ Flattening filter
$ 21   1 -1.0    -21          $ Water phantom
 21  -1 5
…
XrayTherapy.inp
[ S u r f a c e ]
 1   pz  -1.0
 2   pz  -0.9
 3   pz   0.0
 4   pz   6.0
 5   pz   10.0
・ ・ ・ ・ ・ ・
track_xz.eps
外部ボイド
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 14 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題4：Dump線源の作成
icntl = 0に戻す
maxbchを50に増やす*
最後の[t-cross]のoffを外して領域21に入る粒子情報を保存
PHITSを実行
「cross.out」と「cross_dmp.out」が出力されていることを確認
ターゲット周辺の放射線挙動解析を実施して、ターゲット後方の粒子情報をできるだけ多く貯め込もう
*計算時間が掛かる場合は途中で止めても問題ありません
[ T - C r o s s ] off
    title = Energy distribution in region mesh
     mesh =  reg
      reg =    1
      r-from  r-to  area
          98    21   1.0
   e-type =    2
     emin =   0.0
     emax =   1000.0
       ne =    1
     unit =    1
    axis =  eng
     file = cross.out
   output = flux
     part =  all
     dump =  -11
 1 2 3 4 5 6 7 8 9 18 19
XrayTherapy.inp
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 15 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題4の解答
track_xz.eps
1ページ目（光子フラックス）
track_xz.eps
２ページ目（電子フラックス）
粒子情報出力面
ANSWER_FILE: (missing)

--- SLIDE 16 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5：Dump線源の利用
１つ目の[source]をoffにして、2つ目の[source]のoffを削除する
セル21（外部ボイド）の定義を水ファントムに戻す
track_xz.epsで描画するｚの範囲を元に戻す(zmax = c1 + c2 +5.0)
最後の[t-cross]をoffにする
PHITSを実行してPDD.epsやOCR.epsを確認する
Dumpした粒子情報を使って水ファントム内のPDD*やOCR**を計算
*Percentage Depth Dose (線量-深さ分布）, **Off-Center Ratio（線量の横方向拡がり）
[ C e l l ]
…
$ 21   1 -1.0    -21
   21  -1  5
…
XrayTherapy.inp
[ S o u r c e ]
   s-type =   1
...

[ S o u r c e ] off
   s-type =  17
     file =  cross_dmp.out
     dump =  0
[ T - T r a c k ]
    title = Track in xyz
z-type =    2
     zmin =  -5.0
     zmax =   15.0
$     zmax =   c1+c2+5.0
       nz =  110
…
axis =   xz
     file = track_xz.out
[ T - C r o s s ]
…
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 17 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5の解答
track_xz.eps
track_xy.eps
PDD
OCR
全てのタリー結果は、1段階目計算の１電子発生辺りに規格化
2ページ目
OCR.eps
1ページ目
PDD.eps
少しビルドアップして減衰
ほぼ平坦な分布を達成
ANSWER_FILE: (missing)

--- SLIDE 18 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
ターゲットの設計
２段階計算（Dump線源の作成と利用）
JAWコリメータの設置
照射条件の変更と高度な解析
まとめと宿題
Table of contents
実習内容

--- SLIDE 19 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題6：閉口状態のコリメータを設置
X線治療では、JAWコリメータと呼ばれる可動式コリメータにより照射野のおおよその大きさを決定します。
本実習では、まずは閉じた状態のJAWコリメータを再現します
目指すべきtrack_xz.eps
icntl = 8として体系確認モードにする
[surface]で直方体(rpp)を２つ定義する。大きさは（0 < x < 20 cm もしくは -20 < x < 0 cm）・（-10 cm < y < 10 cm）・（30 < z < 40 cm）
[cell]で上記直方体を物質番号５（タングステン合金、密度17g/cm3）で満たした領域を定義する
新しく定義したセルを空気セル（セル番号98）から取り除く
新しく定義
ANSWER_FILE: (missing)

--- SLIDE 20 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題6の解答
track_xz.eps
[ C e l l ]
…
 22   5 -17.0   -22          $ JAW1
 23   5 -17.0   -23          $ JAW2
 98   2 -0.0012  #1 #2 #3 #4 #5 #21 #22 #23  -999  $ Air
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
21  rpp  -c1/2 c1/2  -c1/2 c1/2    c2 c2+c1
22  rpp    0.0 20.0  -10.0 10.0  30.0 40.0
23  rpp  -20.0  0.0  -10.0 10.0  30.0 40.0
XrayTherapy.inp
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 21 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
5cm
課題7：コリメータの開口
原点（ターゲット）を中心にJAWを回転させて開口させます
回転角は、水ファントムまでの距離と照射野の大きさで決まります
今回は、照射野の大きさを10cmとします→回転角度はatan(5.0/c2)
目指すべきtrack_xz.eps
[transform]でｙ軸回りにatan(5.0/c2)及び-atan(5.0/c2)回転する行列（tr1とtr2）を作成する
それぞれのtransformをJAWを定義したセルに適用する

PHITSを実行して下図のようにJAWが回転したことを確認する
θ
c2 cm
tan(θ) = 5.0/c2      atan(5.0/c2) = θ
10cm
→適用方法はセルの定義にtrcl=1もしくはtrcl=2を加える
ANSWER_FILE: (missing)

--- SLIDE 22 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
角度単位オプション
*有:degree
*無:radian
[ Transform ]
*Trn      X0  Y0  Z0        XC  YC  ZC     A1  θ1     A2  θ2     A3  θ3      M
変換方法
M=3：回転後に平行移動
M=-3：平行移動後に回転
[Transform]セクションで座標変換番号nを定義し、[cell], [source]セクション等においてtrcl=nとする。
平行移動の各成分
*i回目の
回転軸Aiと
回転角度θi
座標変換番号
例1： *tr1    0.0 0.0 5.0      0.0 10.0 0.0     2 45.0     3 -60.0      0 0.0      3
(0.0 10.0 0.0)を中心にY軸周りに45度、Z軸周りに-60度回転後、zの+方向に5cm平行移動

例2：  tr1    0.0 0.0 -5.0      0.0 0.0 0.0     1  pi/4       0 0.0       0 0.0      -3
zの+方向に5cm平行移動後、原点を中心にX軸周りに45度回転
（M=-3の場合、平行移動の方向が逆転することに注意！）
[transform]において、座標変換番号と13のパラメーターを指定する。
*A=1,2,3は、それぞれX,Y,Z軸周りの回転を表す。A=0の場合は回転させない。
回転の中心座標
参考：[transform]の定義方法

--- SLIDE 23 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
課題7の解答
track_xz.eps
[ C e l l ]
…
 22   5 -17.0   -22 trcl=1   $ JAW1
 23   5 -17.0   -23 trcl=2   $ JAW2
 98   2 -0.0012  #1 #2 #3 #4 #5 #21 #22 #23  -999  $ Air
[ Transform ]
tr1    0  0  0    0  0  0    2  atan(5.0/c2)  0  0  0  0    3
tr2    0  0  0    0  0  0    2 -atan(5.0/c2)  0  0  0  0    3
XrayTherapy.inp
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 24 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
課題8：粒子輸送計算を実行
icntl = 0として粒子輸送計算を実行し、PDDやOCRを確認してみよう
track_xz.eps
track_xy.eps
2ページ目
4ページ目
8ページ目
ANSWER_FILE: (missing)

--- SLIDE 25 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
課題8の解答
PDD.eps
1ページ目（0～6cm）
3ページ目（12～18cm）
5ページ目（24～30cm）
OCR.eps
10 cm
コリメータ設置前と比べて大幅に下がっている*
徐々に形が崩れていく
*統計を上げるためにタリー幅を広く設定しているため
ANSWER_FILE: (missing)

--- SLIDE 26 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
ターゲットの設計
２段階計算（Dump線源の作成と利用）
JAWコリメータの設置
照射条件の変更と高度な解析
まとめと宿題
Table of contents
実習内容

--- SLIDE 27 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
課題9：照射条件の変更
ファントムの位置や照射野サイズを変更してみよう
ファントム表面がターゲットから100cm離れるように移動
照射野サイズを２倍（-10cm < x < 10cm）にする
PHITSを実行してtrack_xz.epsやOCR.epsを確認する
[ S u r f a c e ]
set:c1[30.0] $ size of cubic water phantom
set:c2[70.0] $ distance from the target to water phantom
…
[ Transform ]
tr1    0  0  0    0  0  0    2  atan(5.0/c2)  0  0  0  0    3
tr2    0  0  0    0  0  0    2 -atan(5.0/c2)  0  0  0  0    3
XrayTherapy.inp
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 28 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
課題9の解答
[ Transform ]
tr1    0  0  0    0  0  0    2  atan(10.0/c2)  0  0  0  0    3
tr2    0  0  0    0  0  0    2 -atan(10.0/c2)  0  0  0  0    3
XrayTherapy.inp
track_xz.eps
1ページ目（0～6cm）
3ページ目（12～18cm）
5ページ目（24～30cm）
[ S u r f a c e ]
set:c1[30.0]
set:c2[100.0]
…
OCR.eps
20 cm
課題８と比べて照射野サイズが深部まで維持される
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 29 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
課題10：散乱線の影響を評価
[counter]を使ってJAWコリメータで散乱した光子の影響のみタリーしよう
[counter]セクションのoffを削除して有効にする
JAWコリメータ（reg = 22 & 23）で反応（coll）したらカウンタ１を+1するように[counter]を変更
カウンタ１の最小値が１以上の場合のみにスコアするように[t-track]のfile=track_xz.outを変更する（「ctmin(1)=1」を追記）
[ Counter ] off
  counter = 1
     part =  photon
     reg        in
      21         1
XrayTherapy.inp
現在の設定は光子が水ファントム（reg = 21）に入ったら（in）カウンタ1を+1する
２つ以上の領域を定義する場合は()でまとめる
  例: (22 23)
[counter]の詳細はphits/lecture/advanced/options参照
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 30 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
課題10の解答
[ Counter ]
  counter = 1
     part =  photon
     reg       coll
 (22 23)         1
XrayTherapy.inp
[ t-track ]
…
 file = track_xz.out    # file name of output for the above axis
     part =  photon electron
    gshow =    3            # 0: no 1:bnd, 2:bnd+mat, 3:bnd+reg 4:bnd+lat
   epsout =    1            # (D=0) generate eps file by ANGEL
 ctmin(1) =    1
track_xz.eps
散乱線は水ファントムにほとんど到達していない（PDD及びOCRへの影響はほとんどない）
MENTIONED_INPUT_NAMES: XrayTherapy.inp
ANSWER_FILE: (missing)

--- SLIDE 31 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
ターゲットの設計
２段階計算（Dump線源の作成と利用）
JAWコリメータの設置
照射条件の変更と高度な解析
まとめと宿題
Table of contents
実習内容

--- SLIDE 32 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
まとめ
X線治療を模擬したシミュレーションは、上流側と下流側で２段階計算すると効率的
JAWコリメータは[transform]を使えば簡単に再現可能
[counter]を使えば、2次散乱線の影響を個別に評価可能
実務上は、加速器メーカーなどが提供するPhase Space Fileを使って下流側のみシミュレーションするのが一般的
Phase Space Fileの使い方は、phits/utility/PSFC4PHITSをご参照下さい

--- SLIDE 33 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
宿題
今回作成したインプットは、X方向のみコリメートされている
Y方向も同様に照射野が20cmとなるJAWコリメータを設置しよう
課題10でタリーに追加した「ctmin(1) = 1」を削除する
[t-track]のfile=track_xz.outをベースにyz方向に対する[t-track]を新たに作成する

[surface]で直方体(rpp)を２つ定義する。大きさは（-10 cm < x < 10 cm）・（0 < y < 20 cm もしくは -20 < y < 0 cm）・（45 < z < 55 cm）
[transform]でX軸回りに回転させる行列を２つ定義する

新たに定義した[surface]と[transform]を使って[cell]を定義する
icntl=8で体系を確認した後、icntl=0に戻して粒子輸送計算を実行
→ axis, nx, xmin, xmax, ny, ymin, ymax, fileなどを変更
→ 回転方向に注意！（yz平面で見て反時計回りに回転）
ここまでの課題が出来ていない場合はinput/XrayTherapy-homework.inpを使用する
ANSWER_FILE: (missing)

--- SLIDE 34 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
宿題の解答例（詳細はXrayTherapy-final.inp）
track_yz.eps with icntl = 8
PHIG-3Dによる体系描画
MENTIONED_INPUT_NAMES: XrayTherapy-final.inp

--- SLIDE 35 ---
PPTX_FILE: phits-lec-XrayTherapy-en.pptx
SLIDE_TEXT:
宿題の解答例（詳細はXrayTherapy-final.inp）
track_xz.eps
track_yz.eps
track_xy.eps
20 cm < z < 33 cm
33 cm < z < 46 cm
46 cm < z < 59 cm
97 cm < z < 110 cm
MENTIONED_INPUT_NAMES: XrayTherapy-final.inp

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/XrayTherapy01.inp
FILE: input/XrayTherapy02.inp
FILE: input/XrayTherapy03.inp
FILE: input/XrayTherapy04.inp
FILE: input/XrayTherapy05.inp
FILE: input/XrayTherapy06.inp
FILE: input/XrayTherapy07.inp
FILE: input/XrayTherapy08.inp
FILE: input/XrayTherapy09.inp
FILE: input/XrayTherapy10.inp
FILE: input/XrayTherapy-homework.inp

[BONUS_TEXT_FILES]
NOTE: None
