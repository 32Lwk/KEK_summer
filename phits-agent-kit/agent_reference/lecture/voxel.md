# Lecture: advanced/voxel

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/voxel
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: voxel
LECTURE_PATH_INDEX: lecture/advanced/voxel
PPTX_FILES: phits-lec-voxel-en.pptx, phits-lec-voxel-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: lattice, robot, universe
SECTION_KEYWORDS: 5, 6, t-deposit, t-volume

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/voxel
LECTURE_PATH_INDEX: lecture/advanced/voxel
PPTX_FILES: phits-lec-voxel-en.pptx, phits-lec-voxel-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 3
SLIDE_COUNT: 58
EXERCISE_SLIDE_COUNT: 20
BONUS_INPUT_COUNT: 5
BONUS_TEXT_COUNT: 1

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- lattice.inp
- robot.inp
- universe.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Making Voxel Phantom
- SLIDE 02: What is Voxel Phantom?
- SLIDE 03: Table of Contents
- SLIDE 04: What is Universe?
- SLIDE 05: Example of Universe
- SLIDE 06: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/lattice-1.inp
- SLIDE 07: Table of Contents
- SLIDE 08: What is Lattice?
- SLIDE 09: How to define lattice?
- SLIDE 10: lattice.inp
- SLIDE 11: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/lattice-2.inp
- SLIDE 12: EXERCISE 3 | Exercise 3
  ANSWER_FILE: input/lattice-3.inp
- SLIDE 13: EXERCISE 4 | Exercise 4
  ANSWER_FILE: input/robot-5.inp
- SLIDE 14: Table of Contents
- SLIDE 15: How to define voxel phantom?
- SLIDE 16: robot.inp
- SLIDE 17: Definition of cells
- SLIDE 18: EXERCISE 5 | Exercise 5
  ANSWER_FILE: input/robot-6.inp
- SLIDE 19: EXERCISE 6 | Exercise 6
  ANSWER_FILE: input/robot-7.inp
- SLIDE 20: EXERCISE 7 | [ surface ]
  ANSWER_FILE: input/robot-8.inp
- SLIDE 21: EXERCISE 8 | Exercise 8
  ANSWER_FILE: input/robot-9.inp
- SLIDE 22: EXERCISE 9 | Exercise 9
  ANSWER_FILE: input/robot-10.inp
- SLIDE 23: Answer 9
- SLIDE 24: EXERCISE 10 | Exercise 10
  ANSWER_FILE: input/robot-10.inp
- SLIDE 25: Answer 10
- SLIDE 26: Table of Contents
- SLIDE 27: Summary
- SLIDE 28: Tips 1: Reduce the loading time of phantom with a large number of voxels
- SLIDE 29: Tips 2: Change the order of lattice
- SLIDE 01: Voxelファントムの作り方
- SLIDE 02: Voxelファントムとは？
- SLIDE 03: Table of Contents
- SLIDE 04: Universeとは？
- SLIDE 05: Universeの例
- SLIDE 06: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/lattice-1.inp
- SLIDE 07: Table of Contents
- SLIDE 08: Latticeとは？
- SLIDE 09: 格子の定義方法
- SLIDE 10: lattice.inp
- SLIDE 11: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/lattice-2.inp
- SLIDE 12: EXERCISE 3 | Exercise 3
  ANSWER_FILE: input/lattice-3.inp
- SLIDE 13: EXERCISE 4 | Exercise 4
  ANSWER_FILE: input/robot-5.inp
- SLIDE 14: Table of Contents
- SLIDE 15: 簡易Voxelファントムの作り方
- SLIDE 16: robot.inp
- SLIDE 17: Cellの定義
- SLIDE 18: EXERCISE 5 | Exercise 5
  ANSWER_FILE: input/robot-6.inp
- SLIDE 19: EXERCISE 6 | Exercise 6
  ANSWER_FILE: input/robot-7.inp
- SLIDE 20: EXERCISE 7 | [ surface ]
  ANSWER_FILE: input/robot-8.inp
- SLIDE 21: EXERCISE 8 | Exercise 8
  ANSWER_FILE: input/robot-9.inp
- SLIDE 22: EXERCISE 9 | Exercise 9
  ANSWER_FILE: input/robot-10.inp
- SLIDE 23: Answer 9
- SLIDE 24: EXERCISE 10 | Exercise 10
  ANSWER_FILE: input/robot-10.inp
- SLIDE 25: Answer 10
- SLIDE 26: Table of Contents
- SLIDE 27: まとめ
- SLIDE 28: PHITSでは一度インプットファイルを全てバイナリー化してから再読込
- SLIDE 29: lattice.inp

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: lattice.inp
FILE: robot.inp
FILE: universe.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Making Voxel Phantom
title
Jun 2021, revised
phits/lecture/advanced/voxel

--- SLIDE 02 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
What is Voxel Phantom?
Reproduce human body based on repeated rectangles filled with a certain material
(See Manual 5.6.5)
Low resolution
High resolution
You can automatically make voxel phantom from DICOM-CT image data using RT-PHITS*
This lecture focuses on how to make voxel phantom manually using universe and lattice functions
*See /phits/utility/RTphits

--- SLIDE 03 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Table of Contents
Table of Contents
Universe
Lattice
Simple voxel phantom
Summary

--- SLIDE 04 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
What is Universe?
Universe
You can define many universes in PHITS virtual space
But only 1 universe (main space) is the stage of particle transport simulation
Other universes are used for replacing some parts of the main space using “fill” command
Some parts of the main space (inside the boxes) are filled with universe 1
Universe1
Main space
→ Virtual space in PHITS

--- SLIDE 05 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Example of Universe
Universe
universe.inp
[ C e l l ]
$ Main space
 1  0  -11  -1 FILL=1
 2  0  -11   1 FILL=2
99 -1   11
$ Universe 1
 101 1 -1.00 -10 U=1
 102 0        10 U=1
$ Universe 2
 201 2 -7.86 -10 U=2
 202 1 -1.00  10 U=2

 [ S u r f a c e ]
  1 pz  0.0
 10 cy  5.0
 11 rpp -6. 6. -6. 6. -6. 6.
Step 1:
Declare universe 1
Step 2:
Filled with universe 1
Universe-2D.out (main space)
Universe 1
Universe 2
All surfaces can be used in any universe
It is not necessary to define outer void in each universe
The material of a cell to be filled with another universe should be void
MENTIONED_INPUT_NAMES: universe.inp

--- SLIDE 06 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
Universe
Change the cells to be filled from x = -3 to +9 cm
universe.inp
[ C e l l ]
$ Main space
 1  0  -11  -1 FILL=1
 2  0  -11   1 FILL=2
99 -1   11
$ Universe 1
 101 1 -1.00 -10 U=1
 102 0        10 U=1
$ Universe 2
 201 2 -7.86 -10 U=2
 202 1 -1.00  10 U=2

 [ S u r f a c e ]
  1 pz  0.0
 10 cy  5.0
 11 rpp -6. 6. -6. 6. -6. 6.
Universe-2D.out
[ C e l l ]
$ Main space
 1  0  -11  -1 FILL=1
 2  0  -11   1 FILL=2
99 -1   11
$ Universe 1
 101 1 -1.00 -10 U=1
 102 0        10 U=1
$ Universe 2
 201 2 -7.86 -10 U=2
 202 1 -1.00  10 U=2

 [ S u r f a c e ]
  1 pz  0.0
 10 cy  5.0
 11 rpp -3. 9. -6. 6. -6. 6.
Universes inside the filled regions do not change
MENTIONED_INPUT_NAMES: universe.inp
ANSWER_FILE: input/lattice-1.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Table of Contents
Table of Contents
Universe
Lattice
Simple voxel phantom
Summary

--- SLIDE 08 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
What is Lattice?
Lattice
→ Repeated structure used
     in PHITS virtual space
It is troublesome to define all surfaces and cells used in repeated structure
Define only surfaces and cells used in fundamental structure
Examples of Lattice in PHITS
Express the repeated structure using “lat” command

--- SLIDE 09 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
How to define lattice?
Only repeated structure can be defined in lattice universe
You have to fill lattice with other universe
It is better to define lattice not
in main space but in a universe
You cannot directly define the contents inside lattice
Define repeated structure using more than 2 universes
Universe1
(Lattice structure)
Universe2
(fundamental structure)
fill
Main space
fill
Lattice

--- SLIDE 10 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
lattice.inp
[ S u r f a c e ]
 1  rpp  -5 5 -5 5 -1 1
 2  rpp  -6 6 -6 6 -2 1
 99  so  100
101  rpp  -1 1 -1 1 -1 1
201  so   1
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
Declare lattice type 1 (Rectangle)
Define the region of basic lattice
Define the number of repeated structure
Universe number to be filled with（5×5×1 matrix）
Location should be adjusted to that of
the basic lattice
Basic lattice（0,0,0）
-5                X                 5
（2,2,0）
-5                Y                5
（-2,-2,0）
Sample input
Lattice
Adjust the lattice-container
surface to be the same as whole lattice region
MENTIONED_INPUT_NAMES: lattice.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
lattice.inp
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
$ Add a new cell with u = 3
lattice-2D.eps
Lattice
Change the center box from golden ball to void
Make a new void cell inside surface 99
Assign the cell to universe 3 (add u=3)
Change the universe ID of the center
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      2 2 2 2 2
      2 2 2 2 2
      2 2 3 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
$ Add a new cell with u = 3
 301  0  -99  u=3
MENTIONED_INPUT_NAMES: lattice.inp
ANSWER_FILE: input/lattice-2.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
lattice.inp
lattice-2D.eps
Lattice
Change the left-bottom box from golden ball to void
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      2 2 2 2 2
      2 2 2 2 2
      2 2 3 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
$ Add a new cell with u = 3
 301  0  -99  u=3
Universe number should be written in the order of
(x-2,y-2,z0)→ (x-1,y-2,z0)→ (x0,y-2,z0) → (x1,y-2,z0)→ (x2,y-2,z0)→
(x-2,y-1,z0)→ (x-1,y-1,z0)→ (x0,y-1,z0) → (x1,y-1,z0)→ (x2,y-1,z0)→…
Hint
((( universe(ix,iy,iz), ix = xmin, xmax), iy = ymin, ymax), iz = zmin, zmax)
Here!
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      3 2 2 2 2
      2 2 2 2 2
      2 2 3 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
$ Add a new cell with u = 3
 301  0  -99  u=3
In programming …
MENTIONED_INPUT_NAMES: lattice.inp
ANSWER_FILE: input/lattice-3.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
lattice.inp
Lattice
Rotate lattice by 45 degree around z axis
Rotate the surface of lattice container cell by adding transform ID “500” between surface number and symbol
Rotate lattice cell by adding “trcl=500” to cell 101
Rotate other cells in main space if necessary. In this case, you have to rotate Cu box (cell 2)
[ S u r f a c e ]
  1  500 rpp  -5 5 -5 5 -1 1
…
[ C e l l ]
$ Main space
 1  0   -1  fill=1
  2  3  -8.96  #1 -2 trcl=500
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1 trcl=500
      fill=-2:2 -2:2  0:0
...
[ transform ]
$ rotate 45 degree around z axis
*tr500 0 0 0 0 0 0 3 45 0 0 0 0 3
lattice-2D.eps
MENTIONED_INPUT_NAMES: lattice.inp
ANSWER_FILE: input/robot-5.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Table of Contents
Table of Contents
Universe
Lattice
Simple voxel phantom
Summary

--- SLIDE 15 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
How to define voxel phantom?
Universe1
(void)
Simple Voxel Phantom
① Make universes filled with an unique material such as bone and soft tissue
Universe2
(water)
Universe3
(Aluminum)
② Make voxel phantom by repeating those universes
Universe10
(Voxel Phantom)
Main Space
③ Fill some part of the main space with the voxel phantom

--- SLIDE 16 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
robot.inp
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[5]  $ number of z pixel
set: c84[2.0] $ unit voxel x
set: c85[2.0] $ unit voxel y
set: c86[2.0] $ unit voxel z
set: c87[-c81*c84/2] $ smallest x
set: c88[-c82*c85/2] $ smallest y
set: c89[-c83*c86/2] $ smallest z
set: c90[   0.00001] $ small quota
Basic lattice surface
Definition of surfaces
Simple Voxel Phantom
c88 = -c82*c85/2
c88 + c85
0
c88+c82*c85
X
Y
101 rpp  c87 c87+c84 c88 c88+c85 c89 c89+c86
Lattice container cell
201 500 rpp c87 c87+c81*c84 c88 c88+c82*c85 c89 c89+c83*c86
transform ID
c87
c87+c84
c87+c81*c84
0
Correlate basic lattice and lattice-container cells using user-defined parameters
MENTIONED_INPUT_NAMES: robot.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Definition of cells
Simple Voxel Phantom
robot.inp
[ C e l l ]
$ Material universe
 1   0           -99  u=1
 2   1  -1.00  -99  u=2
 3   2  -2.70  -99  u=3
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:4
      1 1 1 1 1
      1 2 1 2 1
      1 2 1 2 1
      1 1 1 1 1
      1 1 1 1 1
… repeat 4 times
$ Main space
 201  0  -201  fill=10
 202  0  -202 #201  trcl=500
 203  3  -8.96 202 -203 trcl=500
 204  0  -99   #201 #202 #203
 205 -1   99
Basic lattice surface with transform
Any large region is OK
Need to specify the number of lattice directly because user-defined parameter cannot be used
Lattice container surface (already transformed)
MENTIONED_INPUT_NAMES: robot.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Simple Voxel Phantom
Change the material of shoes to Cu
robot.inp
[ C e l l ]
$ Material universe
 1   0           -99  u=1
 2   1  -1.00  -99  u=2
 3   2  -2.70  -99  u=3
 add new universe filled with Cu here
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:4
      1 1 1 1 1
      1 2 1 2 1
      1 2 1 2 1
      1 1 1 1 1
      1 1 1 1 1
Make a new universe filled with Cu (material 3 with density of 8.96 g/cm3)
Change the universe ID at the shoes location
robot-3D.eps
(or you can check with PHIG-3D)
[ C e l l ]
$ Material universe
 1   0           -99  u=1
 2   1  -1.00  -99  u=2
 3   2  -2.70  -99  u=3
 4   3  -8.96  -99  u=4
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:4
      1 1 1 1 1
      1 4 1 4 1
      1 4 1 4 1
      1 1 1 1 1
      1 1 1 1 1
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-6.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6
Simple Voxel Phantom
Add Cu hat on the head
robot.inp
Increase the number of lattice for z direction defined in cell 101
Copy & paste the last (i.e. top) z layer and change the center lattice to universe 4
Increase the number of z pixel (c83)
robot-3D.eps
[ C e l l ]
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:4
… (the last one)
      1 1 1 1 1
      1 1 1 1 1
      1 1 2 1 1
      1 1 1 1 1
      1 1 1 1 1
…
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[5]  $ number of z pixel
[ C e l l ]
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:5
… (the last one)
      1 1 1 1 1
      1 1 1 1 1
      1 1 2 1 1
      1 1 1 1 1
      1 1 1 1 1

      1 1 1 1 1
      1 1 1 1 1
      1 1 4 1 1
      1 1 1 1 1
      1 1 1 1 1
…
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[6]  $ number of z pixel
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-7.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[6]  $ number of z pixel
set: c84[2.0] $ unit voxel x
set: c85[2.0] $ unit voxel y
set: c86[2.0] $ unit voxel z
Exercise 7
Simple Voxel Phantom
Shorten the phantom by 3/4
robot.inp
Change the unit voxel z (c86) to 1.5
robot-3D.eps
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[6]  $ number of z pixel
set: c84[2.0] $ unit voxel x
set: c85[2.0] $ unit voxel y
set: c86[1.5] $ unit voxel z
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-8.inp

--- SLIDE 21 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Exercise 8
Simple Voxel Phantom
Irradiate the phantom by setting icntl = 0
robot-deposit-xz.eps
150 MeV proton
robot-deposit-reg.out
x: Serial Num. of Region
y: Dose [Gy/source]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n
#  num    reg     volume     all         r.err
    1       2   5.4000E+01   3.4551E-11  0.0143
    2       3   3.6000E+01   1.1548E-10  0.0114
You can calculate the mean absorbed doses in certain organs
[ T-Deposit ]
     mesh = reg
      reg = 2 3
   volume
   reg   vol     # reg definition
     2  c84*c85*c86*9
     3  c84*c85*c86*6
Need to specify manually
(or use [t-volume])
ANSWER_FILE: input/robot-9.inp

--- SLIDE 22 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
Exercise 9
Let’ｓ calculate deposition energy in each voxel filled with water
(Cell ID: 2)
robot.inp
[ T-Deposit ]
     mesh = reg
      reg = 2 3 add region specification here
    Hint：Cell ID of lattice container is 101 and its ranges are [0:4 0:4 0:5]
Format for specify the cell ID of each voxel
( Cell ID for Tally region < Cell ID for Lattice container[coordinated of lattice] )
(3 < 101[0 0 0])  Tally in cell 3 in the lattice-container cell 101 at the lattice coordinate [0 0 0] (i.e., fundamental lattice)
(2 < 101[1:2 2:3 0:4]) Tally in cell 2 in the lattice-container cell 101 at the lattice coordinate of x = 1~2, y = 2~3, and z= 0~4 (2 x 2 x 5 = 20 results are given from this tally)
Example
See manual “6.1 Geometrical mesh” in more detail
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-10.inp

--- SLIDE 23 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Answer 9
robot-deposit-reg.out
[ T-Deposit ]
    title = [t-deposit] in region mesh
     mesh =  reg            # mesh type is region-wise
      reg = 2 3 ( 2 < 101[ 0:4 0:4 0:5 ] )
   volume                   # combined, lattice or level structure
   non     reg      vol     # reg definition
    1        2   5.4000E+01 # 2
    2        3   3.6000E+01 # 3
    3  1000001   1.0000E+00 # ( 2 < 101[ 0 0 0 ] )
    4  1000002   1.0000E+00 # ( 2 < 101[ 1 0 0 ] )
    5  1000003   1.0000E+00 # ( 2 < 101[ 2 0 0 ] )
...
#  num    reg     volume       all       r.err
    1       2   5.4000E+01   3.4586E-11  0.0143
    2       3   3.6000E+01   1.1545E-10  0.0114
    3 1000001   1.0000E+00   0.0000E+00  0.0000
    4 1000002   1.0000E+00   0.0000E+00  0.0000
    5 1000003   1.0000E+00   0.0000E+00  0.0000
...
   39 1000037   1.0000E+00   3.7871E-13  0.3671
   40 1000038   1.0000E+00   0.0000E+00  0.0000
   41 1000039   1.0000E+00   3.2709E-12  0.8039
[ T-Deposit ]
     mesh = reg
      reg = 2 3 (2 < 101[0:4 0:4 0:5])
New cell IDs are automatically assigned from 1000001
Volume is automatically set to 1.0
(You can specify it using newly assigned cell ID)
Lattice coordinate
If cell 2 is not included in the lattice, it should be 0
Deposition energy in cell 2 at the lattice coordinate of [1 2 1]

--- SLIDE 24 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
Exercise 10
Simple Voxel Phantom
Rotate the phantom by +45 degree around y-axis
Change 7th (rotation axis) and 8th (rotation angle) columns of transform in the case of type M=3
Lattice-container surface should be slightly smaller than the lattice universe to avoid the lost particles due to the loss-of-digits problem
robot.inp
set: c90[   0.00001] $ small quota

$ fundamental voxel
101 rpp  c87 c87+c84 c88 c88+c85 c89 c89+c86
99 so 100
$ Main space
201 500 rpp c87+c90 c87+c81*c84-c90 c88+c90 c88+c82*c85-c90 c89+c90 c89+c83*c86-c90
202 rcc  0 0 c89   0 0 4 8
203 rcc  0 0 c89-1 0 0 5 9
[ transform ]
*tr500  0 0 0  0 0 0  2 45 0 0 0 0 3
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-10.inp

--- SLIDE 25 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Answer 10
robot-deposit-xz.eps

--- SLIDE 26 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Table of Contents
Table of Contents
Universe
Lattice
Simple voxel phantom
Summary

--- SLIDE 27 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Summary
*see phits/utility/RTphits
Several universes can be defined in PHITS geometry, but only main space is used in the particle transport simulation
The lattice concept helps you to easily construct a geometry with repeated structure
Voxel phantom can be constructed using the concepts of both universe and lattice
For conversion from CT image to voxel phantom, please use CT2PHITS module in RT-PHITS*

--- SLIDE 28 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Tips 1: Reduce the loading time of phantom with a large number of voxels
It converts its input file to binary, and re-reads the binary file
Make binary file of voxel phantom prior to the PHITS execution
Purpose
Procedure
① Insert the following 2 lines in the [Parameters] section
ivoxel = 2                 # Convert the “fill” part of lattice to binary and output to file(18)
file(18) = voxel.bin   # Output file name for binary voxel phantom
② Execute PHITS → Binary file was successfully generated!!
③ Change “ivoxel = 1”
ivoxel = 1 # Read the “fill” part of lattice from file(18)
Speed up!
Tips
It is better to…
Every time PHITS runs…

--- SLIDE 29 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Tips 2: Change the order of lattice
[ S u r f a c e ] (pick up partially)
101  px  -1
102  px   1
103  py  -1
104  py   1
105  pz  -1
106  pz   1
[ C e l l ] (pick up partially)
$ Universe 1
 101 0 -102 101 -104 103 -106 105
     lat=1 u=1
     fill=-2:2 -2:2 0:0
     3 2 2 2 2
     2 2 2 2 2
     2 2 2 2 2
     2 2 2 2 2
     2 2 2 2 2
-102 101 103 -104 -106 105
X: +, Y: –, Z:+
Tips
RPP is divided
into each surface
Order is
important!
-102 101 -104 103 -106 105
X:+, Y:+, Z:+
101 -102 -104 103 -106 105
X: –, Y:+, Z: +
101 -102 103 -104 -106 105
X: –, Y: –, Z: +
Prior surface faces to
the forward direction
Same as
RPP, BOX

--- SLIDE 01 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Voxelファントムの作り方
title
2021年6月改訂
phits/lecture/advanced/voxel
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Voxelファントムとは？
直方体を積み重ねて生物など複雑な体系を再現したもの
（マニュアル5.6.5.3）
低分解能
高分解能
PHITSのUniverseとLattice構造を使って構築
（マニュアル5.6.3＆5.6.4）
*RT-PHITSを使えばCTデータから簡単に作成可能
*See /phits/utility/RTphits
本講習では、universe と lattice 機能を使ってボクセルファントムを自作する方法を学習します

--- SLIDE 03 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Table of Contents
講習の流れ
Universe
Lattice
簡易Voxelファントム
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 04 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Universeとは？
Universe
PHITSでは，いくつもの仮想空間（universe）を定義できる
実際に粒子輸送の舞台となるのはメイン空間のみ
メイン空間の一部を別のuniverseで満たすことにより入れ子構造を再現する
メイン空間にある箱の中を，球が並んでいる別の宇宙(universe1)に置換
Universe1
メイン空間
→ PHITSの中の仮想空間

--- SLIDE 05 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Universeの例
Universe
universe.inp
[ C e l l ]
$ Main space
 1  0  -11  -1 FILL=1
 2  0  -11   1 FILL=2
99 -1   11
$ Universe 1
 101 1 -1.00 -10 U=1
 102 0        10 U=1
$ Universe 2
 201 2 -7.86 -10 U=2
 202 1 -1.00  10 U=2

 [ S u r f a c e ]
  1 pz  0.0
 10 cy  5.0
 11 rpp -6. 6. -6. 6. -6. 6.
ステップ 1:
universeを宣言
ステップ 2:
ある領域をuniverseで満たす
Universe-2D.out (main space)
Universe 1
Universe 2
universeは各セルに定義可能（surfaceは全てのuniverseで共通）
各universeでは、無限に続く領域を定義可能（outer voidの定義は不要）
他のuniverseで満たす領域の物質番号は常に0
MENTIONED_INPUT_NAMES: universe.inp

--- SLIDE 06 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
Universe
universe 1と2で満たす領域の範囲をx = -3 ～ +9 cmに移動
universe.inp
[ C e l l ]
$ Main space
 1  0  -11  -1 FILL=1
 2  0  -11   1 FILL=2
99 -1   11
$ Universe 1
 101 1 -1.00 -10 U=1
 102 0        10 U=1
$ Universe 2
 201 2 -7.86 -10 U=2
 202 1 -1.00  10 U=2

 [ S u r f a c e ]
  1 pz  0.0
 10 cy  5.0
 11 rpp -6. 6. -6. 6. -6. 6.
Universe-2D.out
[ C e l l ]
$ Main space
 1  0  -11  -1 FILL=1
 2  0  -11   1 FILL=2
99 -1   11
$ Universe 1
 101 1 -1.00 -10 U=1
 102 0        10 U=1
$ Universe 2
 201 2 -7.86 -10 U=2
 202 1 -1.00  10 U=2

 [ S u r f a c e ]
  1 pz  0.0
 10 cy  5.0
 11 rpp -3. 9. -6. 6. -6. 6.
各universeの中身は変化せず、そのuniverseを覗く窓が移動するイメージ
MENTIONED_INPUT_NAMES: universe.inp
ANSWER_FILE: input/lattice-1.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Table of Contents
講習の流れ
Universe
Lattice
簡易Voxelファントム
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 08 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Latticeとは？
Lattice
→ PHITSの中で使う
格子(lattice，繰り返し）構造
同じ形状のものが繰り返し並んでいるときに，個々の形状を全て定義するのは大変！
基本構造のみ定義して，あとはその繰り返しで表現する
格子には直方体と六角柱があるが，ボクセルファントムで使うのは直方体のみ
Latticeの例

--- SLIDE 09 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
格子の定義方法
格子空間には他の構造物は定義できない
別のuniverseで満たす(fillする）必要がある
メイン空間ではなく，universeの１つとして定義するのが便利
格子の中身は直接定義できない
Universeを２つ以上使った２重入れ子構造にする
Universe1
（Lattice構造）
Universe2
（基本構造）
fill
Main space
（粒子輸送の舞台）
fill
Lattice

--- SLIDE 10 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
lattice.inp
[ S u r f a c e ]
 1  rpp  -5 5 -5 5 -1 1
 2  rpp  -6 6 -6 6 -2 1
 99  so  100
101  rpp  -1 1 -1 1 -1 1
201  so   1
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
直方体タイプのLatticeを宣言
基本格子の領域を定義
格子に物質を満たす領域を指定（0は基本格子）
各格子に満たすuniverse番号（5×5×1の行列）
基本格子と座標を合わせる必要有
基本格子 （0,0,0）
-5                X軸                5
（2,2,0）
-5                Y軸              5
（-2,-2,0）
サンプルインプット
Lattice
Lattice格納面の大きさは
Lattice全体の領域に一致させる必要がある
MENTIONED_INPUT_NAMES: lattice.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
lattice.inp
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
$ Add a new cell with u = 3
lattice-2D.eps
Lattice
中心の玉を取り除く（真空に変える）
surface 99の内側を全て真空にした新しいcellを作成する
作成したcellをuniverse 3 (u=3)に割り当てる
Lattice中心のuniverse番号を3に変更
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      2 2 2 2 2
      2 2 2 2 2
      2 2 3 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
$ Add a new cell with u = 3
 301  0  -99  u=3
MENTIONED_INPUT_NAMES: lattice.inp
ANSWER_FILE: input/lattice-2.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
lattice.inp
lattice-2D.eps
Lattice
左下の玉を取り除く（真空に変える）
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      2 2 2 2 2
      2 2 2 2 2
      2 2 3 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
$ Add a new cell with u = 3
 301  0  -99  u=3
Universe番号は、下記の順番で書かれている
(x-2,y-2,z0)→ (x-1,y-2,z0)→ (x0,y-2,z0) → (x1,y-2,z0)→ (x2,y-2,z0)→
(x-2,y-1,z0)→ (x-1,y-1,z0)→ (x0,y-1,z0) → (x1,y-1,z0)→ (x2,y-1,z0)→…
ヒント
((( universe(ix,iy,iz), ix = xmin, xmax), iy = ymin, ymax), iz = zmin, zmax)
ここ!
[ C e l l ]
$ Main space
  1  0   -1  fill=1
  2  3  -8.96  #1 -2
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1
      fill=-2:2 -2:2  0:0
      3 2 2 2 2
      2 2 2 2 2
      2 2 3 2 2
      2 2 2 2 2
      2 2 2 2 2
$ Universe 2
 201  1  -19.32  -201  u=2
 202  0   201          u=2
$ Add a new cell with u = 3
 301  0  -99  u=3
プログラムで書くなら…
MENTIONED_INPUT_NAMES: lattice.inp
ANSWER_FILE: input/lattice-3.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
lattice.inp
Lattice
全体をZ軸に対して+45度回転させる
Lattice格納面を回転させる（面番号1とrppの間にtransform ID番号500を挿入）
Latticeを定義するcell（セル番号101）を回転させる（セルの定義に“trcl=500”を追加）
Main spaceの他のセルも必要に応じて同じtransformで回転。今回の場合は銅箱（セル番号2）
[ S u r f a c e ]
  1  500 rpp  -5 5 -5 5 -1 1
…
[ C e l l ]
$ Main space
 1  0   -1  fill=1
  2  3  -8.96  #1 -2 trcl=500
 98  0  -99    #1 #2
 99 -1   99
$ Universe 1
 101  0  -101  lat=1 u=1 trcl=500
      fill=-2:2 -2:2  0:0
...
[ transform ]
$ rotate 45 degree around z axis
*tr500 0 0 0 0 0 0 3 45 0 0 0 0 3
lattice-2D.eps
MENTIONED_INPUT_NAMES: lattice.inp
ANSWER_FILE: input/robot-5.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Table of Contents
講習の流れ
Universe
Lattice
簡易Voxelファントム
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 15 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
簡易Voxelファントムの作り方
Universe1
(void)
Simple Voxel Phantom
① 単一の物質（骨・軟組織など）で満たされたuniverseを作る
Universe2
(water)
Universe3
(Aluminum)
② ①で作ったuniverseをLatticeを使って組み合わせ，ボクセルファントムが入ったuniverseを作る
Universe10
(Voxel Phantom)
③ ②で作ったuniverseを
メイン空間の一部にFillする
メイン空間

--- SLIDE 16 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
robot.inp
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[5]  $ number of z pixel
set: c84[2.0] $ unit voxel x
set: c85[2.0] $ unit voxel y
set: c86[2.0] $ unit voxel z
set: c87[-c81*c84/2] $ smallest x
set: c88[-c82*c85/2] $ smallest y
set: c89[-c83*c86/2] $ smallest z
set: c90[   0.00001] $ small quota
基本Lattice面
面の定義
Simple Voxel Phantom
c88 = -c82*c85/2
c88 + c85
0
c88+c82*c85
X
Y
101 rpp  c87 c87+c84 c88 c88+c85 c89 c89+c86
Lattice格納面
201 500 rpp c87 c87+c81*c84 c88 c88+c82*c85 c89 c89+c83*c86
transform ID
c87
c87+c84
c87+c81*c84
0
基本LatticeとLattice格納面の定義をユーザー定義定数により相関させる
MENTIONED_INPUT_NAMES: robot.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Cellの定義
Simple Voxel Phantom
robot.inp
[ C e l l ]
$ Material universe
 1   0           -99  u=1
 2   1  -1.00  -99  u=2
 3   2  -2.70  -99  u=3
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:4
      1 1 1 1 1
      1 2 1 2 1
      1 2 1 2 1
      1 1 1 1 1
      1 1 1 1 1
… repeat 4 times
$ Main space
 201  0  -201  fill=10
 202  0  -202 #201  trcl=500
 203  3  -8.96 202 -203 trcl=500
 204  0  -99   #201 #202 #203
 205 -1   99
基本Lattice面
（transformしない場合もtrclを定義しておくと便利）
とにかく大きい領域であれば何でもよい
（outer voidとの境界面を使うのが便利）
Latticeのメッシュ数を直接定義する必要有
（ここではユーザー定義定数が使えないため）
Lattice格納面（面の定義で既にtransform済）
MENTIONED_INPUT_NAMES: robot.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Simple Voxel Phantom
ロボットの「靴」を銅に変更
robot.inp
[ C e l l ]
$ Material universe
 1   0           -99  u=1
 2   1  -1.00  -99  u=2
 3   2  -2.70  -99  u=3
 add new universe filled with Cu here
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:4
      1 1 1 1 1
      1 2 1 2 1
      1 2 1 2 1
      1 1 1 1 1
      1 1 1 1 1
全てが銅（物質番号３、密度8.96g/cm3）で満たされた新しいuniverse (u=4)を作る
靴の場所に対応するLatticeのuniverse番号を4に変更
robot-3D.eps
(もしくはPHIG-3Dで確認）
[ C e l l ]
$ Material universe
 1   0           -99  u=1
 2   1  -1.00  -99  u=2
 3   2  -2.70  -99  u=3
 4   3  -8.96  -99  u=4
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:4
      1 1 1 1 1
      1 4 1 4 1
      1 4 1 4 1
      1 1 1 1 1
      1 1 1 1 1
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-6.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6
Simple Voxel Phantom
ロボットの頭の上に銅の帽子を乗せる
robot.inp
Z方向に対するLatticeの数を１つ増やす（繰り返し数はcell 101のfillで定義）
最後の階層のuniverse定義をコピー＆ペーストして、新しく作成した階層の中心Lattice番号を銅（universe 4）に変更する
z pixel数 (c83)を１つ増やす
robot-3D.eps
[ C e l l ]
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:4
… (the last one)
      1 1 1 1 1
      1 1 1 1 1
      1 1 2 1 1
      1 1 1 1 1
      1 1 1 1 1
…
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[5]  $ number of z pixel
[ C e l l ]
$ Voxel universe
 101  0  -101 trcl=500
      lat=1 u=10
      fill=0:4 0:4 0:5
… (the last one)
      1 1 1 1 1
      1 1 1 1 1
      1 1 2 1 1
      1 1 1 1 1
      1 1 1 1 1

      1 1 1 1 1
      1 1 1 1 1
      1 1 4 1 1
      1 1 1 1 1
      1 1 1 1 1
…
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[6]  $ number of z pixel
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-7.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[6]  $ number of z pixel
set: c84[2.0] $ unit voxel x
set: c85[2.0] $ unit voxel y
set: c86[2.0] $ unit voxel z
Exercise 7
Simple Voxel Phantom
ロボットの身長を3/4に縮める
robot.inp
z方向に対する基本Latticeの長さ (c86)を2.0から1.5に変更する
robot-3D.eps
[ surface ]
set: c81[5]  $ number of x pixel
set: c82[5]  $ number of y pixel
set: c83[6]  $ number of z pixel
set: c84[2.0] $ unit voxel x
set: c85[2.0] $ unit voxel y
set: c86[1.5] $ unit voxel z
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-8.inp

--- SLIDE 21 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Exercise 8
*[t-volume]を使って計算してもよい
icntl = 0にして粒子輸送計算を実行する
robot-deposit-xz.eps
150 MeV 陽子ビーム
robot-deposit-reg.out
x: Serial Num. of Region
y: Dose [Gy/source]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n
#  num    reg     volume     all         r.err
    1       2   5.4000E+01   3.4551E-11  0.0143
    2       3   3.6000E+01   1.1548E-10  0.0114
臓器毎にuniverseを設定すれば、その平均吸収線量（Gy）を直接計算可能
[ T-Deposit ]
     mesh = reg
      reg = 2 3
   volume
   reg   vol     # reg definition
     2  c84*c85*c86*9
     3  c84*c85*c86*6
体積は各universeに対応するLattice数を数えて手入力*
ANSWER_FILE: input/robot-9.inp

--- SLIDE 22 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
Exercise 9
個々のボクセル中の領域番号２（水）への付与エネルギーをタリーしよう
robot.inp
[ T-Deposit ]
     mesh = reg
      reg = 2 3 ここに下記フォーマットに従って新たな領域番号を加える
          ヒント：Lattice領域番号は101でその全範囲は[0:4 0:4 0:5]
個々のボクセルを指定するフォーマットは
( Tally領域番号 < Lattice領域番号[Lattice座標] )
(3 < 101[0 0 0])  Lattice領域番号101の基本Lattice中にある領域３に限定してTally
(2 < 101[1:2 2:3 0:4]) Lattice領域番号101の基本LatticeからX方向1～2、Y方向2～3、Z方向0～4のLattice中にある領域2を個別にTally (2 x 2 x 5 = 20個の結果が出力される）
例
詳細はマニュアル 6.1 形状メッシュを参照
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-10.inp

--- SLIDE 23 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Answer 9
robot-deposit-reg.out
[ T-Deposit ]
    title = [t-deposit] in region mesh
     mesh =  reg            # mesh type is region-wise
      reg = 2 3 ( 2 < 101[ 0:4 0:4 0:5 ] )
   volume                   # combined, lattice or level structure
   non     reg      vol     # reg definition
    1        2   5.4000E+01 # 2
    2        3   3.6000E+01 # 3
    3  1000001   1.0000E+00 # ( 2 < 101[ 0 0 0 ] )
    4  1000002   1.0000E+00 # ( 2 < 101[ 1 0 0 ] )
    5  1000003   1.0000E+00 # ( 2 < 101[ 2 0 0 ] )
...
#  num    reg     volume       all       r.err
    1       2   5.4000E+01   3.4586E-11  0.0143
    2       3   3.6000E+01   1.1545E-10  0.0114
    3 1000001   1.0000E+00   0.0000E+00  0.0000
    4 1000002   1.0000E+00   0.0000E+00  0.0000
    5 1000003   1.0000E+00   0.0000E+00  0.0000
...
   39 1000037   1.0000E+00   3.7871E-13  0.3671
   40 1000038   1.0000E+00   0.0000E+00  0.0000
   41 1000039   1.0000E+00   3.2709E-12  0.8039
[ T-Deposit ]
     mesh = reg
      reg = 2 3 (2 < 101[0:4 0:4 0:5])
自動で新たなreg番号が付与される
Volumeは1.0 cm3となる
（指定する場合は自動付与番号を使う）
どのlatticeかが書かれている
領域番号が2でないLatticeに対しては付与エネルギーが常に０となる
領域番号が2の領域における付与エネルギー
 → 1000037は[1 2 1]に相当

--- SLIDE 24 ---
PPTX_FILE: phits-lec-voxel-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
Exercise 10
全体をY軸に対して+45度回転させる
回転軸は７カラム目（Y軸は２）、回転角度は８カラム目で定義（M=3の場合）
Lattice構造を回転させる場合、Lattice格納面（surface 201）は、実際のLatticeよりも少しだけ小さくしておく必要がある → 完全に同じ大きさの場合、桁落ちの問題によりLost particleが発生してしまう可能性があるため
robot.inp
set: c90[   0.00001] $ small quota

$ fundamental voxel
101 rpp  c87 c87+c84 c88 c88+c85 c89 c89+c86
99 so 100
$ Main space
201 500 rpp c87+c90 c87+c81*c84-c90 c88+c90 c88+c82*c85-c90 c89+c90 c89+c83*c86-c90
202 rcc  0 0 c89   0 0 4 8
203 rcc  0 0 c89-1 0 0 5 9
[ transform ]
*tr500  0 0 0  0 0 0  2 45 0 0 0 0 3
MENTIONED_INPUT_NAMES: robot.inp
ANSWER_FILE: input/robot-10.inp

--- SLIDE 25 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Answer 10
robot-deposit-xz.eps

--- SLIDE 26 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
Table of Contents
講習の流れ
Universe
Lattice
簡易Voxelファントム
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 27 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
まとめ
PHITSジオメトリでは複数のuniverseを定義できるが、粒子輸送の舞台となるのはMain spaceのみ
Lattice構造を使えば、同じ形状が複数回繰り返されるジオメトリを簡単に定義することができる
ボクセルファントムは、universeとlatticeコンセプトを組み合わせることにより定義可能
CTデータからボクセルファントムを自作するのは難しいが、RT-PHITS*に含まれるCT2PHITSモジュールを使えば簡単に変換可能
*see phits/utility/RTphits

--- SLIDE 28 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
PHITSでは一度インプットファイルを全てバイナリー化してから再読込
巨大なボクセルデータをあらかじめバイナリー化して読込時間短縮！
目的
手順
① [Parameters]セクションのivoxelを有効にする（cを消す）
ivoxel = 2                 # LatticeのFill部分をバイナリー化としてfile(18)に出力させるオプション
file(18) = voxel.bin   # 出力するバイナリーファイルのファイル名
② PHITSを実行する → Binary file was successfully generated!!
③ ivoxel = 1に変更する
ivoxel = 1 # LatticeのFill部分をfile(18)から読み込むオプション
高速化！
Appendix
補足資料①
巨大なボクセルファントムの読込を高速化する

--- SLIDE 29 ---
PPTX_FILE: phits-lec-voxel-en.pptx
SLIDE_TEXT:
lattice.inp
[ S u r f a c e ] （一部抜粋）
101  px  -1
102  px   1
103  py  -1
104  py   1
105  pz  -1
106  pz   1
[ C e l l ] （一部抜粋）
$ Universe 1
 101 0 -102 101 -104 103 -106 105
     lat=1 u=1
     fill=-2:2 -2:2 0:0
     3 2 2 2 2
     2 2 2 2 2
     2 2 2 2 2
     2 2 2 2 2
     2 2 2 2 2
-102 101 103 -104 -106 105
X正方向，Y負方向，Z正方向
Appendix
RPPを各面
に分解
順番が
重要！
-102 101 -104 103 -106 105
X正方向，Y正方向，Z正方向
101 -102 -104 103 -106 105
X負方向，Y正方向，Z正方向
101 -102 103 -104 -106 105
X負方向，Y負方向，Z正方向
先に書く面
が正方向
RPP, BOX
と同じ
補足資料②
基本Latticeを６つの面で定義し、その順番を変更すれば、より直感的にUniverse番号が定義可能となる
MENTIONED_INPUT_NAMES: lattice.inp

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/lattice-4.inp
FILE: input/lattice-final.inp
FILE: input/robot-final.inp
FILE: input/universe-1.inp
FILE: input/universe-final.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: readme.txt
