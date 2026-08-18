# Lecture: basic/lec02

SOURCE_FOLDER: D:/NEAgit/lecture/basic/lec02
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: lec02
LECTURE_PATH_INDEX: lecture/basic/lec02
PPTX_FILES: phits-lec02-en.pptx, phits-lec02-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: lec02, t-deposit
SECTION_KEYWORDS: 1, t-3dshow, t-4dtrack, t-cross, t-dchain, t-deposit, t-deposit2, t-dpa, t-gshow, t-interact, t-let, t-point, t-product, t-rshow, t-sed, t-track, t-yield

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/basic/lec02
LECTURE_PATH_INDEX: lecture/basic/lec02
PPTX_FILES: phits-lec02-en.pptx, phits-lec02-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 2
SLIDE_COUNT: 150
EXERCISE_SLIDE_COUNT: 39
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- lec02.inp
- t-deposit.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Basic Lecture II:
- SLIDE 02: Learn how to deduce various physics quantities from PHITS simulations
- SLIDE 03: What is Tally?
- SLIDE 04: In PHITS, the word of “Tally” used for functions to
- SLIDE 05: PHITS simulates the motion of each particle using the Monte Carlo method. You can estimate their average behavior by cal
- SLIDE 06: For example…
- SLIDE 07: What is Tally?
- SLIDE 08: Every time you construct a new geometry, it is better to check the geometry using [T-Track] with the gshow option (2D) o
- SLIDE 09: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/lec02-2.inp
- SLIDE 10: Answer 1
- SLIDE 11: What is Tally?
- SLIDE 12: How to define Tally
- SLIDE 13: [ T - T r a c k ]
- SLIDE 14: Visualize Particle Trajectory
- SLIDE 15: x-axis
- SLIDE 16: x-axis
- SLIDE 17: x-axis
- SLIDE 18: x-axis
- SLIDE 19: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/lec02-3.inp
- SLIDE 20: Answer 2
- SLIDE 21: Error file (*_err.eps)
- SLIDE 22: Red Screen
- SLIDE 23: How to define Tally
- SLIDE 24: xyz mesh:
- SLIDE 25: Geometrical Mesh
- SLIDE 26: 1: Define # of bins
- SLIDE 27: EXERCISE 3 | Exercise 3
  ANSWER_FILE: input/lec02-4.inp
- SLIDE 28: Spatial resolution of the tally results has been improved by increasing number of meshes
- SLIDE 29: EXERCISE 4 | Exercise 4
  ANSWER_FILE: input/lec02-5.inp
- SLIDE 30: Answer 4
- SLIDE 31: How to define Tally
- SLIDE 32: EXERCISE 5 | Exercise 5
  ANSWER_FILE: input/lec02-6.inp
- SLIDE 33: Answer 5
- SLIDE 34: How to define Tally
- SLIDE 35: EXERCISE 6 | Exercise 6
  ANSWER_FILE: input/lec02-7.inp
- SLIDE 36: Answer 6
- SLIDE 37: EXERCISE 7 | Exercise 7
  ANSWER_FILE: input/lec02-8.inp
- SLIDE 38: We can confirm the lower-energy fluences in detail.
- SLIDE 39: EXERCISE 8 | Exercise 8
  ANSWER_FILE: input/lec02-9.inp
- SLIDE 40: Answer 8
- SLIDE 41: EXERCISE 9 | Tally results for different particles (part) are plotted in the same page in the default
  ANSWER_FILE: input/lec02-10.inp
- SLIDE 42: EXERCISE 10 | Exercise 10
  ANSWER_FILE: input/lec02-11.inp
- SLIDE 43: Answer 10
- SLIDE 44: How to define Tally
- SLIDE 45: EXERCISE 11 | Exercise 11
  ANSWER_FILE: input/lec02-12.inp
- SLIDE 46: Answer 11
- SLIDE 47: EXERCISE 12 | Exercise 12
  ANSWER_FILE: input/lec02-13.inp
- SLIDE 48: A Bragg peak of the carbon beam is shown at z=12 cm.
- SLIDE 49: What is Tally?
- SLIDE 50: Graphic utility ANGEL
- SLIDE 51: Draw Tally Results Using PHIG-3D
- SLIDE 52: EXERCISE 13 | Exercise 13
  ANSWER_FILE: input/lec02-end.inp
- SLIDE 53: Answer 13
- SLIDE 54: EXERCISE 14 | Exercise 14
  ANSWER_FILE: input/lec02-6.inp
- SLIDE 55: A free software for 3D visualization.
- SLIDE 56: What is Tally?
- SLIDE 57: List of Tallies (Visualize geometry)
- SLIDE 58: [T-Gshow]
- SLIDE 59: [T-3Dshow]
- SLIDE 60: Parameters used in [T-3Dshow]
- SLIDE 61: List of Tallies (Deduce physical quantity)
- SLIDE 62: [T-Track]
- SLIDE 63: [T-Cross]
- SLIDE 64: [T-Point]
- SLIDE 65: Bragg peak calculated by [T-Deposit] tally
- SLIDE 66: Example of [T-Deposit2] tally
- SLIDE 67: Example of [T-Yield]
- SLIDE 68: Depth-DPA distribution calculated using [T-DPA]
- SLIDE 69: Example of [T-LET] tally
- SLIDE 70: Example of [T-Interact] tally
- SLIDE 71: Please see recommendation/dchain in detail
- SLIDE 72: What is Tally?
- SLIDE 73: A variety of information can be deduced from the PHITS simulation using functions called “Tally”.
- SLIDE 74: Depict the neutron and proton fluences, respectively, in your homework.
- SLIDE 75: Example Answer
- SLIDE 01: PHITS講習会 基礎実習（II）：
- SLIDE 02: 本実習の目標
- SLIDE 03: 実習内容
- SLIDE 04: 適当な日本語訳がないので…PHITS（の専門）用語として、
- SLIDE 05: PHITSは１つ１つの放射線挙動をコンピュータ内で全て再現するので、任意の場所、時間における放射線の数やエネルギー分布などを調べることが可能。
- SLIDE 06: 物理量として意味のある測定結果を得るためには、適切な条件（検出器の位置、検出粒子の種類やエネルギーなど）を設定する必要がある。
- SLIDE 07: 実習内容
- SLIDE 08: [Material], [Surface], [Cell]セクションで定義したジオメトリ  （仮想空間）を2次元的、或いは3次元的に表示させ確認する。
- SLIDE 09: EXERCISE 1 | 課題1
  ANSWER_FILE: input/lec02-2.inp
- SLIDE 10: EXERCISE 1 | 解答1
  ANSWER_FILE: input/lec02-2.inp
- SLIDE 11: 実習内容
- SLIDE 12: どの空間（面）における、どの粒子の、どういった物理量を、どういう形式で、見たいかを指定する。
- SLIDE 13: 例えば、ファイルlec02.inpの[T-Track]セクションでは、
- SLIDE 14: [T-Track]の計算方法は…
- SLIDE 15: x-axis
- SLIDE 16: x-axis
- SLIDE 17: x-axis
- SLIDE 18: x-axis
- SLIDE 19: EXERCISE 2 | 課題2
  ANSWER_FILE: input/lec02-3.inp
- SLIDE 20: EXERCISE 2 | 解答2
  ANSWER_FILE: input/lec02-3.inp
- SLIDE 21: *_err.epsファイルの活用
- SLIDE 22: Red Screen
- SLIDE 23: Tallyの使い方（物理量の導出）
- SLIDE 24: メッシュ型(mesh=)の種類
- SLIDE 25: [ T - T r a c k ]
- SLIDE 26: メッシュの定義
- SLIDE 27: EXERCISE 3 | 課題3
  ANSWER_FILE: input/lec02-4.inp
- SLIDE 28: EXERCISE 3 | 解答3
  ANSWER_FILE: input/lec02-4.inp
- SLIDE 29: EXERCISE 4 | [ T - T r a c k ]
  ANSWER_FILE: input/lec02-5.inp
- SLIDE 30: EXERCISE 4 | 解答4
  ANSWER_FILE: input/lec02-5.inp
- SLIDE 31: Tallyの使い方
- SLIDE 32: EXERCISE 5 | 課題5
  ANSWER_FILE: input/lec02-6.inp
- SLIDE 33: EXERCISE 5 | 解答5
  ANSWER_FILE: input/lec02-6.inp
- SLIDE 34: Tallyの使い方
- SLIDE 35: EXERCISE 6 | 課題6
  ANSWER_FILE: input/lec02-7.inp
- SLIDE 36: EXERCISE 6 | 解答6
  ANSWER_FILE: input/lec02-7.inp
- SLIDE 37: EXERCISE 7 | 課題7
  ANSWER_FILE: input/lec02-8.inp
- SLIDE 38: EXERCISE 7 | 解答7
  ANSWER_FILE: input/lec02-8.inp
- SLIDE 39: EXERCISE 8 | 課題8
  ANSWER_FILE: input/lec02-9.inp
- SLIDE 40: EXERCISE 8 | 解答8
  ANSWER_FILE: input/lec02-9.inp
- SLIDE 41: EXERCISE 9 | 課題9
  ANSWER_FILE: input/lec02-10.inp
- SLIDE 42: EXERCISE 10 | 課題10
  ANSWER_FILE: input/lec02-11.inp
- SLIDE 43: EXERCISE 10 | 解答10
  ANSWER_FILE: input/lec02-11.inp
- SLIDE 44: Tallyの使い方
- SLIDE 45: EXERCISE 11 | 課題11
  ANSWER_FILE: input/lec02-12.inp
- SLIDE 46: EXERCISE 11 | 解答11
  ANSWER_FILE: input/lec02-12.inp
- SLIDE 47: EXERCISE 12 | 課題12
  ANSWER_FILE: input/lec02-13.inp
- SLIDE 48: EXERCISE 12 | 解答12
  ANSWER_FILE: input/lec02-13.inp
- SLIDE 49: 実習内容
- SLIDE 50: グラフ作成ソフトANGEL
- SLIDE 51: PHIG-3Dを用いたタリー結果の描画
- SLIDE 52: EXERCISE 13 | 課題13
  ANSWER_FILE: input/lec02-end.inp
- SLIDE 53: 解答13
- SLIDE 54: EXERCISE 14 | 課題14
  ANSWER_FILE: input/lec02-end.inp
- SLIDE 55: 汎用の3次元可視化目的に使えるフリーソフト
- SLIDE 56: 実習内容
- SLIDE 57: Tallyの種類（ジオメトリの確認）
- SLIDE 58: 仮想空間に定義したジオメトリの境界線や領域番号、物質番号を表示する。[T-Rshow]では、領域毎に与える値(e.g.,密度)に依存した色付けが可能。
- SLIDE 59: [T-3Dshow]
- SLIDE 60: [T-3Dshow]
- SLIDE 61: Tallyの種類（物理量の導出）
- SLIDE 62: [T-Track]
- SLIDE 63: [T-Cross]
- SLIDE 64: Kinds of tallies in PHITS
- SLIDE 65: [T-Deposit]
- SLIDE 66: [T-Deposit2]で計算した、2つの検出器内でのエネルギー付与の相関
- SLIDE 67: フッ素
- SLIDE 68: [T-DPA]で計算したDPAの深さ分布の例
- SLIDE 69: [T-LET], [T-SED]
- SLIDE 70: [T-Interact]
- SLIDE 71: 詳細はrecommendation/dchain参照
- SLIDE 72: 実習内容
- SLIDE 73: まとめ
- SLIDE 74: 宿題
- SLIDE 75: 宿題（解答例）

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: lec02.inp
FILE: t-deposit.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Basic Lecture II:
Definition of Tally
Feb 2026 revised
phits/lecture/basic/lec02
SPEAKER_NOTES:
Let's start the basic lecture number two.
To access the working directory, please open the PHITS folder and go to the lecture folder, the basic folder and the lec02 folder.
They are many input files in the working directory.
We will mainly edit the lec02 dot inp through the exercises.

--- SLIDE 02 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Learn how to deduce various physics quantities from PHITS simulations
Purpose of This Lecture
You can obtain this kind of results at the end of this lecture.
Particle fluence (left) and depth-dose distribution (right) for the simulation condition for homework.
SPEAKER_NOTES:
In the lecture, you will learn how to deduce various physics quantities from PHITS simulations.
You can obtain this kind of results at the end of the lecture.
These figures show particle fluence and depth-dose distribution for the simulation condition for homework.

--- SLIDE 03 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
What is Tally?
How to use Tally?
Tally for checking geometry
Tally for calculating physical quantities
Software for drawing Tally results
Introduction of Each Tally
Summary
Table of Contents
SPEAKER_NOTES:
This slide shows the contents of lecture number two.
The first subject is "What is tally?".

--- SLIDE 04 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
In PHITS, the word of “Tally” used for functions to
 Deduce physical quantities such as particle fluence and deposition energy
                              or
 Depict the 2D or 3D geometry in certain area.
What is Tally?
Tally: a record of the number or amount of something, 	especially one that you can keep adding to;
[Oxford Advanced Learner’s Dictionary (7th edition), OXFORD.]
SPEAKER_NOTES:
According to the dictionary, tally means a record of the number or amount of something, especially one that you can keep adding to.
In PHITS, we use the word of tally for functions to deduce physical quantities such as flux and deposition energy, or depict the two-dimensional or three-dimensional geometry in certain area.

--- SLIDE 05 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
PHITS simulates the motion of each particle using the Monte Carlo method. You can estimate their average behavior by calculating various physical quantities, such as flux and deposition energy in a certain region, by using “Tally”.
Concept of Tally
Result of [T-Track] (Track-length tally)
How many particles were passed through this region?
 → Use “track-length” tally.
SPEAKER_NOTES:
PHITS simulates the motion of each particle using the Monte Carlo method.
You can estimate their average behavior by calculating various physical quantities by using tally.
Here is shown the result of [T-Track] for particle irradiation.
Blinking dots are particles.
Source particles enter the target, and some times they react with target material, and secondary particles are generated.
This is trajectories of each particle.
When you want to know how many particles were passed through this region, you will use [T-Track].

--- SLIDE 06 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
For example…
Calculating physical quantity
Particle fluence → [T-Track], [T-Cross]
Deposition energy (heat) → [T-Deposit], [T-Deposit2]
Secondary particles → [T-Yield], [T-Product]
LET or microdosimetric distribution → [T-LET], [T-SED]
Checking geometry
2-dimensional visualization → gshow option, [T-Gshow], [T-Rshow]
3-dimensional visualization → [T-3Dshow]
Tally Types
Various tally functions are implemented in PHITS.
Many physical quantities can be deduced from the PHITS simulation by selecting an appropriate tally.
SPEAKER_NOTES:
Various tally functions are implemented in PHITS, and many physical quantities can be deduced from the PHITS simulation by selecting an appropriate tally.
For example, particle fluence can be deduced by [T-Track] and [T-Cross].
Deposition energy can be deduced by [T-Deposit].
Secondary particles can be deduced by [T-Yield] and [T-Product].
You can also check your geometry by using these tallies or using gshow option.

--- SLIDE 07 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
What is Tally?
How to use Tally?
Tally for checking geometry
Tally for calculating physical quantities
Software for drawing Tally results
Introduction of Each Tally
Summary
Table of Contents
SPEAKER_NOTES:
Let's go on to the next subject.

--- SLIDE 08 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Every time you construct a new geometry, it is better to check the geometry using [T-Track] with the gshow option (2D) or PHIG-3D (3D).
Geometry Check
Otherwise you would obtain wrong results without noticing miss-definition of the geometry, especially when you make an overlapped region!
SPEAKER_NOTES:
Every time you construct a new geometry, it is better to check the geometry.
Otherwise you would obtain wrong results without noticing miss-definition of the geometry, especially when you make an overlapped region.
In this subject, you learn how to use tally for checking geometry.

--- SLIDE 09 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
[ M a t e r i a l ]
mat[1]    H 2  O 1

・ ・ ・ ・ ・ ・

[ S u r f a c e ]
  10  cz      10.
 101  pz       0.
 102  pz      50.
 999  so     500.

[ C e l l ]
  1     1 -1.0  -10  101  -102
 100    0      -999  #all
 101   -1       999
A water cylinder with a radius of 10 cm and a height of 50 cm.
lec02.inp
Set icntl = 8 in [Parameters] section and execute PHITS.
    (You must set icntl = 8 when you use the gshow option in tallies.)
Confirm the geometry of lec02.inp in a 2-dimensional view using gshow option in [T-Track] tally.
SPEAKER_NOTES:
Let's start exercise 1.
At first, we will confirm the geometry of lec02 dot inp in a 2-dimensional view using gshow option in [T-Track] section.
When you use G show option in tallies, you have to set icntl = 8.
So please set icntl = 8 in the Parameters section and execute PHITS.
In the lec02.inp, a water cylinder with a radius of 10 cm and a height of 50 cm is defined as cell 1.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-2.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 1
xz-plane
lec02.inp
track_xz.eps
[ P a r a m e t e r s ]
icntl = 8
・ ・ ・ ・ ・ ・

[ T - T r a c k ]
・ ・ ・ ・ ・ ・
axis = xz
file = track_xz.out
part = all
gshow = 3
epsout = 1
gshow option
0: No geometry drawing
1: Draw geometry with boundaries
2: Draw geometry with material name
3: Draw geometry with cell number
SPEAKER_NOTES:
Let's check the answer.
When you open the eps files, you can see the cross section views of the water cylinder in the yz plane.
Since the radius of the water cylinder is 10 cm and its height is 50 cm, the rectangle is 20 cm by 50 cm.
Note that G show option is set to 3 in [T-Track] section. This means that the geometry boundaries and region numbers are plotted on the figure.
You can change what is plotted on the figure by G show option.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
What is Tally?
How to use Tally?
Tally for checking geometry
Tally for calculating physical quantities
Software for drawing Tally results
Introduction of Each Tally
Summary
Table of Contents
SPEAKER_NOTES:
Let's go on to the next subject.

--- SLIDE 12 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
How to define Tally
what physical quantities
        Select types of tally: [T-Track], [T-Deposit] etc.
in where
        Select geometrical mesh: mesh = reg, xyz, r-z
of what particle
        Select particle type: part = neutron, proton etc.
in which unit e.g. (cm/source), (1/cm2/source) etc.
        Select unit: unit = 1, 2, 3 …
in what output form
        Select output axis: axis = eng, reg, xy, etc.
You have to determine …
SPEAKER_NOTES:
In this subject, you learn how to define Tally.
At first, you will select types of tally depending on what physical quantity do you want to know.
After that, you will set four components, that is, Where, What particle, Which unit, and What output form.
You will set these parameters depending on your purpose.

--- SLIDE 13 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[ T - T r a c k ]
 title = Track Detection in xyz mesh mesh =  xyz
   x-type =    2
       nx =   25
     xmin =  -25.
     xmax =   25.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =   50
     zmin =  -20.
     zmax =   80.
   e-type =    1
       ne =    1
            0.0  1.0e+9
   t-type =    1
       nt =    1
            0.0  1.0e+9
     unit =    1
     axis =   xz
     file = track_xz.out
     part =  all
    gshow =   3
   epsout =    1
Contents of [T-Track] tally
Geometrical mesh
Particle type
Unit of output quantity
Output form
Useful for visualizing mean particle trajectories by setting a fine mesh in the tally region.
[T-Track]: Tally for calculating track-lengths or fluences of particles in certain regions.
SPEAKER_NOTES:
Here is shown the example of [T-Track] section in lec02 dot inp.
[T-Track] is used for calculating track length or fluences of particles in certain regions.
[T-Track] can also be used for visualizing particle trajectories by setting a fine mesh in the tally region.
As described before, it has four components, i.e. Geometrical mesh, Unit of output, Output form, and Particle type.

--- SLIDE 14 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Visualize Particle Trajectory
x-axis
z-axis
SPEAKER_NOTES:
This slide shows you how to visualize particle trajectory.
In this case, the certain area is subdivided into small rectangle grids.
The orange sphere is a particle that you want to score.
The particle passes through the region, and grids are colored along particle trajectory.

--- SLIDE 15 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
x-axis
z-axis
Visualize Particle Trajectory
SPEAKER_NOTES:
Next particle passes through the region, and grids are colored along particle trajectory.

--- SLIDE 16 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
x-axis
z-axis
Visualize Particle Trajectory
SPEAKER_NOTES:
Next particle enters the region.
It is deflect, and grids are colored along particle trajectory.

--- SLIDE 17 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
x-axis
z-axis
Visualize Particle Trajectory
SPEAKER_NOTES:
Next particle enters the region.
It is deflected here and finally absorbed, and grids are colored along particle trajectory.

--- SLIDE 18 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
x-axis
z-axis
Visualize Particle Trajectory
SPEAKER_NOTES:
Trajectories of particles are shown here.
The color expresses the fluence of the particle.
Yellow means high fluence, green means middle fluence, and blue means low fluence.
When any particle does not enter, grids are not colored.

--- SLIDE 19 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
Confirm particle fluence by using [T-Track].
Set “icntl = 0” in [Parameters] section and execute PHITS.
What is the behavior of the particles?
[ P a r a m e t e r s ]
icntl = 8
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type = 1
  r0 = 2.5
  z0 = -10.
  z1 = -10.
  dir =  1.0
  e0 = 250.
proj = 12C
A carbon beam at 250 MeV/n with a radius of 2.5 cm
Check track-xz.eps.
lec02.inp
SPEAKER_NOTES:
Let's go on to exercise 2.
To confirm particle fluence, please set icntl = 0 in [Parameters] section and execute PHITS.
In this calculation, a carbon beam at two hundred fifty MeV/n with a radius of 2.5 cm is irradiated on the water cylinder.
After finish the calculation, please open track_xz.eps to see the particle fluence.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-3.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 2
file =:
Define output file name.
epsout = 1:
Generate eps file. The eps file name will be picked up from output file name.
（e.g. track_xz.out → track_xz.eps）
[ P a r a m e t e r s ]
icntl = 0
・ ・ ・ ・ ・ ・

[ T - T r a c k ]
・ ・ ・ ・ ・ ・
axis = xz
file = track_xz.out
part = all
gshow = 3
epsout = 1
lec02.inp
track_xz.eps
[ T-Track ]
    title = Track  Detection
     mesh =  xyz
   x-type =    2
     xmin =  -25.00000
     xmax =   25.00000
#    xdel =  0.5000000
       nx =    100
・ ・ ・ ・ ・ ・
track_xz.out
epsout = 1
SPEAKER_NOTES:
Let's check the answer.
You can see the particle fluence as shown here.
The warm color means the high fluence, and the cold color means low fluence.
The center of the cylinder has high fluence. It comes from the irradiated carbon beam.
Secondary particles are generated via nuclear reactions of carbon beam with target material.
Therefore middle fluence is observed around the carbon beam.
Note that the output file name is defined by the file parameter.
The epsout parameter is used to select whether generate eps file or not.
The eps file name will be picked up from the file parameter.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 21 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Error file (*_err.eps)
In 2D-plots such as tallies with “axis = xy, xz”, statistical errors are output in another file named ***_err.eps.

Warmer colors indicate larger relative standard errors (closer to 1), while colder colors mean smaller errors.
track_xz_err.eps
SPEAKER_NOTES:
Here is shown the error file.
In 2-D plots such as tallies with axis = xz or something, statistical errors are output in another file named foo_err.eps.
Warmer colors indicate larger relative standard errors (closer to 1), while colder colors mean smaller errors.
You can check whether relative standard errors are sufficiently small or not.

--- SLIDE 22 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Red Screen
If no particle is scored in a tally, all regions are painted in red
→ usually something is wrong with the input file!!
track_xz.eps with e0 = 0
SPEAKER_NOTES:
This slide shows you the Red screen obtained from PHITS simulation.
It is not fatal error like system error of windows PC, so please don't worry about it.
If no particle is scored in a tally, all regions are painted in red.
Here is shown the result of [T-Track] with dir = -1.0 in [Source] section.
All of the source particle goes to the opposite side of water cylinder, thus red screen appears.
Usually something is wrong with the input file.
If you get red screen, please check the setting of your input file.

--- SLIDE 23 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
How to define Tally
what physical quantities
        Select types of tally: [T-Track], [T-Deposit] etc.
in where
        Select geometrical mesh: mesh = reg, xyz, r-z
of what particle
        Select particle type: part = neutron, proton etc.
in which unit e.g. (cm/source), (1/cm2/source) etc.
        Select unit: unit = 1, 2, 3 …
in what output form
        Select output axis: axis = eng, reg, xy, etc.
You have to determine …
SPEAKER_NOTES:
Now, let's learn how to select geometrical mesh.

--- SLIDE 24 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
xyz mesh:
Divide the regions in
the XYZ coordinates.
Geometrical Mesh Types
There are 3 types of geometrical mesh in PHITS.
r-z mesh:
Divide the regions in
the Cylindrical coordinates.
reg mesh:
Divide the regions in
cells defined in the
PHITS virtual space.
SPEAKER_NOTES:
There are 3 types of geometrical mesh in PHITS.
That is, xyz mesh, r-z mesh, and reg mesh.
xyz mesh divide the regions in the XYZ coordinates.
r-z mesh divide the regions in the Cylindrical coordinates.
reg mesh divide the regions in cells defined in the PHITS virtual space.

--- SLIDE 25 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Geometrical Mesh
mesh = xyz :
Define tally region according to the xyz coordinate system.
  ⇒ x-type, y-type, z-type subsections
       are required to define each mesh.
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
   mesh =  xyz
   x-type =    2
       nx =   25
     xmin =  -25.
     xmax =   25.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =   50
     zmin =  -20.
     zmax =   80.
   e-type =    1
       ne =    1
            0.0  1.0e+9
   t-type =    1
       nt =    1
            0.0  1.0e+9
・ ・ ・ ・ ・ ・
lec02.inp
SPEAKER_NOTES:
In the [T-Track] section of lec02 dot inp, xyz mesh is adopted.
How to divide the region is defined by x-type, y-type, and z-type subsection.
These subsections should be defined just below the mesh parameter.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 26 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
1: Define # of bins
    and their boundaries.
2,3: Define # of bins, and the range (min & max values).
       Mesh is divided equally by linear scale (= 2) or log scale (= 3).
How to Define a Mesh
Mesh is a common concept used in many tallies.
x-type, y-type, z-type, r-type, e-type, t-type, a-type etc.
x-axis      y-axis      z-axis      radius     energy      time        angle
There are 5 types to define a mesh as follows. (types 4 & 5 are rarely used)
4,5: Define the range of the mesh (min & max values) and xdel for the mesh width.
       (= 5: xdel is given by log value of mesh interval)
x-type = 1
  nx = 10
  0  1  2  3  5  10
  15  20  30  50  100
x-type = 2
  nx = 100
  xmin =  0
  xmax =  1000
x-type = 3
  nx = 100
  xmin =  0.1
  xmax =  5000
Replace “x” to “y”, “z”, “r”, “e” , “t” , or “a” if you want to define other meshes.
(e.g. y-type, ny, ymin)
SPEAKER_NOTES:
This slide shows how to define a mesh.
Mesh is a common concept used in many tallies.
The type of subsection is x, y, z, r, e, t, and a. They are first letters for each physical quantity.
You can define each mesh using the following five types.
x-type = 1 and 2 are described before.
x-type = 3 is almost same as x-type = 2, but it subdivided mesh by logarithmic interval.
For x-type = 4 and 5, the minimum value, the maximum value and the width of a mesh are defined.
The red letter will be replaced if you want to define other meshes.

--- SLIDE 27 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
Let’s improve the spatial resolution of the tally results by changing mesh
Multiply nx and nz in the [T-Track] section by 4.
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
   mesh =  xyz
   x-type =    2
       nx =   25
     xmin =  -25.
     xmax =   25.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =   50
     zmin =  -20.
     zmax =   80.
・ ・ ・ ・ ・ ・
lec02.inp
track_xz.eps
Spatial resolution is rather poor with the current setting…
→ nx = 100 and nz = 200
SPEAKER_NOTES:
Let's go on to exercise 3.
To see a finer structure in a 2-D plot, increase the number of mesh in the [T-Track] section.
Please multiply nx and nz in the [T-Track] section with axis = xz by 4.
After that, please execute PHITS and check the result.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-4.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Spatial resolution of the tally results has been improved by increasing number of meshes
Answer 3
lec02.inp
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
   mesh =  xyz
   x-type =    2
       nx =   100
     xmin =  -25.
     xmax =   25.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =   200
     zmin =  -20.
     zmax =   80.
・ ・ ・ ・ ・ ・
track_xz.eps
SPEAKER_NOTES:
Let's check the answer.
We can see the tracks with a better resolution by increasing the number of meshes.
It should be noted that the file size become large when you increase the number of mesh.
So please set the appropriate number of meshes for your purpose.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
Let’s see the time dependence of particle trajectories
Edit t-type sub-section of [T-Track]

Set “t-type = 2” and set nt, tmin, tmax to be 5, 0.0, 5.0, respectively.
    (See “How to Define a Mesh” in p. 26.)

Delete or comment out the unnecessary line.
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
e-type = 1
  ne = 1
  0.0  1.0e+9
t-type = 1
  nt = 1
  0.0  1.0e+9
・ ・ ・ ・ ・ ・
lec02.inp
Unit of time in PHITS is nsec from the source generation
i.e., 1.0e+9 = 1 sec
SPEAKER_NOTES:
Next, let's subdivide the time mesh to see a change of fluence with a time.
In the current t-type sub-section of the [T-Track] section, nt is set to 1, with the time period defined from 0 to 10 to the 9th.
Since PHITS defines the source particles generation as time zero, and uses nanosecounds as the time unit, these settings correspond to a one-second interval.
Therefore, the tally results represent values integrated over 1 second following the source generation.
In this exercise, please edit t-type subsection so that the tally results are output by dividing the interval from 0 seconds to 5 nanoseconds into five equal parts.
Specifically, change the t-type from 1 to 2 and set nt, tmin, and tmax to appropriate values.
Here please do not forget to delete or comment out the unnecessary line for t-type = 2.
After that, please execute PHITS and check the result.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-5.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 4
1st page
（t = 0 ~ 1 nsec）
2nd page
（t = 1 ~ 2 nsec）
3rd page
（t = 2 ~ 3 nsec）
In SumatraPDF, the pages of *.eps can be switched by left and right keys.
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
e-type = 1
  ne = 1
  0.0  1.0e+9
t-type = 2
  nt = 5
$  0.0  1.0e+9
  tmin =  0.0
  tmax =  5.0
・ ・ ・ ・ ・ ・
lec02.inp
track_xz.eps
See phits/utility/animation for creating GIF animation from PHITS results
SPEAKER_NOTES:
Let's check the answer.
The time evolution of radiation fluence can be seen in each page of the eps file.
In SumatraPDF, you can switch the pages of eps file by left and right keys.
The gif animation can be made. An example is prepared in phits/utility/animation.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
How to define Tally
what physical quantities
        Select types of tally: [T-Track], [T-Deposit] etc.
in where
        Select geometrical mesh: mesh = reg, xyz, r-z
of what particle
        Select particle type: part = neutron, proton etc.
in which unit e.g. (cm/source), (1/cm2/source) etc.
        Select unit: unit = 1, 2, 3 …
in what output form
        Select output axis: axis = eng, reg, xy, etc.
You have to determine …
SPEAKER_NOTES:
Next, let's learn how to select observed particles.

--- SLIDE 32 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Replace “part = all” of [T-Track] by “part = 12C proton neutron”

Change nt in t-type back to 1 to reduce the number of pages
Let’s distinguish the fluences of each particle species
What are the typical behaviors of 12C, protons, and neutrons?
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
t-type = 2
  nt = 5
  tmin =     0.0
  tmax =    5.0
・ ・ ・ ・ ・ ・
axis = xz
file = track_xz.out
part = all
・ ・ ・ ・ ・ ・
lec02.inp
track_xz.eps
SPEAKER_NOTES:
Let's start exercise 5.
The aim of this exercise is to see the fluences of individual particle species.
Here, we will focus on carbon-12, protons, and neutrons.
Specifically, please change part = all to part = carbon twelve, proton, and neutron.
In addition, please change nt in t-type sub-section back to 1 to reduce the nuber of pages.
After that, please execute PHITS and check the result.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-6.inp

--- SLIDE 33 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 5
1st page
(part = 12C)
2nd page
(part = proton)
3rd page
(part = neutron)
track_xz.eps
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
t-type = 2
  nt = 1
  tmin =     0.0
  tmax =    5.0
・ ・ ・ ・ ・ ・

axis = xz
file = track_xz.out
part = 12C proton neutron
・ ・ ・ ・ ・ ・
lec02.inp
SPEAKER_NOTES:
Let's check the answer.
You may obtain this result.
They are individual behaviors of specified particles in each page of the eps file.
You can see that carbon ions are stopped in the water cylinder, and secondary protons and neutrons are emitted in several directions.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 34 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
How to define Tally
what physical quantities
        Select types of tally: [T-Track], [T-Deposit] etc.
in where
        Select geometrical mesh: mesh = reg, xyz, r-z
of what particle
        Select particle type: part = neutron, proton etc.
in which unit e.g. (cm/source), (1/cm2/source) etc.
        Select unit: unit = 1, 2, 3 …
in what output form
        Select output axis: axis = eng, reg, xy, etc.
You have to determine …
SPEAKER_NOTES:
Next, let's learn how to select output axis in tally.

--- SLIDE 35 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6
Let’s tally the energy distributions of each particle species
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
  x-type = 2
    nx = 100
・ ・ ・ ・ ・ ・
  z-type = 2
    nz = 200
・ ・ ・ ・ ・ ・
e-type = 1
  ne = 1
  0.0  1.0e+9
unit = 1
axis = xz
file = track_xz.out
・ ・ ・ ・ ・ ・
lec02.inp
Replace “axis = xz” by “axis = eng” in [T-Track]

Set “e-type = 2” to score the energy distribution from 0 to 300 MeV/n with 100 energy meshes
    (See “How to Define a Mesh” in p. 26.)

Set “nx = 1” and “nz = 1” to reduce the number of pages in the eps file.

Change the output file name to “track_eng.out”*
*Do not forget to change because track_xz.out will be used later in this lecture
SPEAKER_NOTES:
Let's start exercise 6.
The aim of this exercise is to see the particle fluence with its energy distribution.
The procedure is shown here.
First, replace axis = xz by axis = eng.
Second, set e-type = 2, ne = 100, emin = 0, and emax = 300.
Third, set nx = 1, and nz = 1 to reduce the number of pages in the output.
Last, change the output file name to track_eng.out.
After that, please execute PHITS and check the result.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-7.inp

--- SLIDE 36 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 6
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
  x-type = 2
    nx = 1
・ ・ ・ ・ ・ ・
  z-type = 2
    nz = 1
・ ・ ・ ・ ・ ・
e-type = 2
  ne = 100
$  0.0  1.0e+9
  emin = 0.0
  emax = 300.0
unit = 1
axis = eng
file = track_eng.out
・ ・ ・ ・ ・ ・
lec02.inp
track_eng.eps
The beam energy is 250 MeV/n
The basic energy unit for ions is MeV/n (kinetic energy per nucleon)*.
For particles other than ions, the energy unit is MeV, but it is written as (MeV/n) in the label (assuming n = 1).
By defining e-unit in tally, energy can be converted to wavelength (nm) or LET (keV/um).
*If you want to tally ions by total kinetic energy (MeV), set iMeVperN = 0 (the default in versions prior to 3.36)
SPEAKER_NOTES:
Let's check the answer.
As you can see here, this is the energy distribution for eac particle species.
The C-12 has a peak at 250 MeV/n, which corresponds to the beam energy.
Please note that the standard energy unit for ions is MeV/n, while for other particles, it is simply MeV.
In this specific label, however, MeV/n is used for all particles, including non-ions.
If you would like to tally ions by their total kinetic energy in MeV, please set iMeVperN = 0 in the [Parameters] section.
Additionaly, by defining e-unit in the tally section, you can convert energy into wavelength or LET.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 37 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Exercise 7
Let’s change the horizontal axis to a logarithmic scale.
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
  x-type = 2
    nx = 1
・ ・ ・ ・ ・ ・
  z-type = 2
    nz = 1
・ ・ ・ ・ ・ ・
e-type = 2
  ne = 100
$  0.0  1.0e+9
  emin = 0.0
  emax = 300.0
unit = 1
axis = eng
file = track_eng.out
・ ・ ・ ・ ・ ・
lec02.inp
track_eng.eps
This figure is shown in linear scale…
Set “e-type=3” and “emin=1.0”.
SPEAKER_NOTES:
Next, let's change the horizontal axis to a logarithmic scale.
Please set e-type = 3 and emin = 1.0.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-8.inp

--- SLIDE 38 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
We can confirm the lower-energy fluences in detail.
Answer 7
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
  x-type = 2
    nx = 1
・ ・ ・ ・ ・ ・
  z-type = 2
    nz = 1
・ ・ ・ ・ ・ ・
e-type = 3
  ne = 100
$  0.0  1.0e+9
  emin = 1.0
  emax = 300.0
unit = 1
axis = eng
file = track_eng.out
・ ・ ・ ・ ・ ・
lec02.inp
track_eng.eps
SPEAKER_NOTES:
You may obtain this result.
By plotting in a logarithmic scale, you can check the low-energy fluences in detail.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 39 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Exercise 8
[ T - T r a c k ]
mesh = xyz

  x-type = 2
    nx = 1
    xmin = -25.
    xmax =  25.
  y-type = 1
    ny = 1
    -5.0  5.0
  z-type = 2
    nz = 1
    zmin = -20.
    zmax =  80.
・ ・ ・ ・ ・ ・
lec02.inp
Delete
or
Comment out
Add “reg” parameter
Change the geometrical mesh from the xyz mesh to the reg mesh.
Add “reg” parameter and define cell numbers for regions inside and outside the cylinder (cell 1 and 100, respectively).
The format is “reg = 1  2” if tally regions are 1 and 2 (separated by blank).
Delete or comment out parameters for “mesh = xyz” sub-section.
Let’s tally the energy distributions inside and outside of the cylinder
SPEAKER_NOTES:
Let's go on to exercise 8.
Here, we will see the energy distributions inside and outside the cylinder.
The procedure is shown here.
First, please change the geometrical mesh from the xyz mesh to the reg mesh.
Second, please specify the two regions to tally by adding reg parameter.
The cell number of inside and outside of the cylinder are 1 and 100, respectively.
Last, please delete or comment out parameters for mesh = xyz.
After that, please execute PHITS and check the result.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-9.inp

--- SLIDE 40 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 8
1st page
(reg = 1: water)
2nd page
(reg = 100: void)
[ T - T r a c k ]
mesh = reg
  reg = 1 100
$  x-type = 2
$    nx = 1
$    xmin = -25.
$    xmax =  25.
$  y-type = 1
$    ny = 1
$    -5.0  5.0
$  z-type = 2
$    nz = 1
$    zmin = -20.
$    zmax =  80.
・ ・ ・ ・ ・ ・
lec02.inp
track_eng.eps
Flight path of primary 12C ion
before incident to water
SPEAKER_NOTES:
Here is shown the result.
You can see the energy distributions of each particles inside and outside the cylinder.
Looking at these results, the particle fluence of carbon ions in a vacuum is observed only at 250 MeV/n.
The values on the vertical axis correspond to the flight path of primary carbon ions before incident to water.
Furthermore, protons are rarely detected in a vacuum because they decelerate in water, while neutrons are detected frequently even in a vacuum.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 41 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
Tally results for different particles (part) are plotted in the same page in the default
You can change the parameter to be plotted in the same page by setting samepage parameter to reg, x, y, z, r, eng etc.
Output the tally results in different regions in the same page of EPS file
[ T - T r a c k ]
mesh = reg
  reg = 1 100
samepage = reg
・ ・ ・ ・ ・ ・
lec02.inp
1st page (part = 12C)
2nd page (part = proton)
3rd page (part = neutron)
Exercise 9
track_eng.eps
SPEAKER_NOTES:
Let's go on to exercise 9.
Here, we will see the tally results for different regions on the same page.
The tally results for each particle are output to the same page with the default setting.
By specifying samepage parameter in the tally section, tally results for different parameters can be displayed on the same page.
Here, please set samepage = reg in the [T-Track] section.
The figure below shows the result of setting the samepage = reg.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-10.inp

--- SLIDE 42 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
Exercise 10
[ T - D e p o s i t ]
title = Energy deposition in xyz mesh
mesh = xyz
・ ・ ・ ・ ・ ・
unit = 1
material = all
output = dose
axis = xz
file = deposit.out
part = all
gshow = 3
epsout = 1
t-deposit.inp
[T-Deposit]: Tally for calculating deposited energy in materials
Copy [T-Deposit] section from t-deposit.inp and paste it in lec02.inp.*

Execute PHITS with the input file of lec02.inp.
Let’s tally spatial distribution of deposited energies (i.e. dose) in water cylinder using [T-Deposit].
*You can paste the new tally anywhere except in the middle of other tallies or after [end] section
SPEAKER_NOTES:
Let's go on to exercise 10.
Here, we will confirm energy deposition using [T-Deposit].
Please open the t-deposit dot inp file and copy [T-Deposit] section and paste into the lec02 dot inp file.
You can paset [T-Deposit] section wherever you like, except the middle of each section and below the [End] section.
After that, please execute PHITS and open deposit.eps file.
MENTIONED_INPUT_NAMES: lec02.inp, t-deposit.inp
ANSWER_FILE: input/lec02-11.inp

--- SLIDE 43 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 10
deposit.eps
Energy deposition by the primary carbon beam.
Energy deposition by the secondary particles such as protons and neutrons.
SPEAKER_NOTES:
Here is shown the result.
You can see the spatial distribution of deposited energies.
The carbon beam deposited high energy in the left side of water cylinder.
And secondary particles deposited middle or low energies in a wide area.

--- SLIDE 44 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
How to define Tally
what physical quantities
        Select types of tally: [T-Track], [T-Deposit] etc.
in where
        Select geometrical mesh: mesh = reg, xyz, r-z
of what particle
        Select particle type: part = neutron, proton etc.
in which unit e.g. (cm/source), (1/cm2/source) etc.
        Select unit: unit = 1, 2, 3 …
in what output form
        Select output axis: axis = eng, reg, xy, etc.
You have to determine …
SPEAKER_NOTES:
Next, let's learn how to select the unit of physical quantity from exercise.

--- SLIDE 45 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
Exercise 11
Let’s change the unit of the output in the [t-deposit] tally from [MeV/cm3/source] to [Gy/source].
[ T - D e p o s i t ]
・ ・ ・ ・ ・ ・
unit = 1
material = all
output = dose
axis = xz
file = deposit.out
part = all
gshow = 3
epsout = 1
lec02.inp
The concept of the (/source) will be learned in the basic lecture III.
Replace “unit = 1” by “unit = 0”.
Calculating the deposit energy in units of Gy = J/kg.
SPEAKER_NOTES:
Let's start exercise 11.
The aim of this exercise is to change the unit of the output in the [T-Deposit] section from (MeV/cm3/source) to (Gy/source).
Please replace unit = 1 by unit = 0.
It should be noted that when a region includes more than two materials, the calculated dose in such a region does not equal to average value of the region.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-12.inp

--- SLIDE 46 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 11
deposit.eps
[ T - D e p o s i t ]
・ ・ ・ ・ ・ ・
unit = 0
material = all
output = dose
axis = xz
file = deposit.out
part = all
gshow = 3
epsout = 1
lec02.inp
The unit and its scale have changed.
SPEAKER_NOTES:
The answer is shown here.
The visual of the figure does not changed, but the unit and its scale have changed.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 47 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 12
SLIDE_TEXT:
Exercise 12
Let’s calculate the absorbed dose as a function of the depth in the water cylinder using an r-z mesh.
[ T - Deposit ]
・ ・ ・ ・ ・ ・
mesh = xyz
  x-type = 2
    nx = 100
    xmin = -25.
    xmax =  25.
  y-type = 1
    ny = 1
    -5.0  5.0
  z-type = 2
    nz = 200
    zmin = -20.
    zmax =  80.
・ ・ ・ ・ ・ ・
axis = xz
file = deposit.out
・ ・ ・ ・ ・ ・
lec02.inp
Delete
or
Comment out
Change to r-type
Change the geometrical mesh from the xyz mesh to the r-z mesh.

Delete or comment out the parameters for x-type sub-section.

Change y-type sub-section to r-type sub-section and set radial range from 0 to 10 cm within 1 bin.

Replace “axis=xz” by “axis=z”.
Plot the depth distribution of the energy deposition with an r-z mesh.
SPEAKER_NOTES:
Let's go on to the next exercise.
We will try to output the energy deposition along the z-axis in the water cylinder by using an r-z mesh.
Here is shown the procedure.
First, replace mesh = xyz by mesh = r-z and set r-type and z-type sub-sections.
Second, set radial range from zero to ten centimeter within one bin.
Last, replace axis = xz by axis = z.
After that, please execute PHITS and check the result.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-13.inp

--- SLIDE 48 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
A Bragg peak of the carbon beam is shown at z=12 cm.
[ T - Deposit ]
・ ・ ・ ・ ・ ・
mesh = r-z
$  x-type = 2
$    nx = 100
$    xmin = -25.
$    xmax =  25.
  r-type = 1
    nr = 1
    0.0  10.0
  z-type = 2
    nz = 200
    zmin = -20.
    zmax =  80.
・ ・ ・ ・ ・ ・
axis = z
file = deposit.out
・ ・ ・ ・ ・ ・
lec02.inp
deposit.eps
Answer 12
SPEAKER_NOTES:
The answer is shown here.
You can see a Bragg peak of the carbon beam at z = 12 cm.
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 49 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
What is Tally?
How to use Tally?
Tally for checking geometry
Tally for calculating physical quantities
Software for drawing Tally results
Introduction of Each Tally
Summary
Table of Contents
SPEAKER_NOTES:
Here, I will introduce graphic utilities.

--- SLIDE 50 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Graphic utility ANGEL
What is ANGEL?
A software to convert text data files (*.out) to image files (*.eps).
You can adjust regions of vertical axes by setting angel parameter in the tally sections. (See the ANGEL manual for details of angel parameters)
You can write angel parameters to the *.out files directly.
You can execute ANGEL only by ”right-click→send to→ANGEL” (Windows) or “drag&drop to the ANGEL ion”  (Mac).
(You don’t have to execute PHITS again only to re-draw the image files.)
For example, add
p: ymin(1e-11) ymax(1e-9)
to deposit.out, and then execute ANGEL.
The range of the vertical axis changes.
SPEAKER_NOTES:
First is ANGEL.
ANGEL is a software to convert text data files to image files.
You can adjust regions of vertical axes by setting ANGEL parameter in the tally section.
You can also write angel parameters to the output files directly.
You can execute ANGEL only by following method.
So you don't have to execute PHITS again only to re-draw the image files.
For example, add p: ymin(1e-11) ymax(1e-9) to deposit.out, and then execute ANGEL.
After that the range of the vertical axis changes.

--- SLIDE 51 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Draw Tally Results Using PHIG-3D
Text output (*.out) should be loaded instead of image file (*.eps)
Numerical values can be deduced from the image in PHIG-3D
Tally output with xyz-mesh
Particle trajectories generated by [t-4dtrack]
Animation of particle trajectories can be crated
Error could occur when the trajectories from large history number are loaded
Example of animation created by PHIG-3D with the results of [t-4dtrack]
SPEAKER_NOTES:
Next, I will explain how to draw tally results using PHIG-3D.
PHIG-3D supports the drawing of tally output with xyz mesh, as well as the drawing of 4-dimensional particle trajectories generated by [T-4d track].
To draw tally output with xyz mesh, load a text output.
Numerical values can be deduced from the image in PHIG-3D.
When drawing 4-dimensional particle trajectories, you can create animation like the one shown on the right.

--- SLIDE 52 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 13
SLIDE_TEXT:
Exercise 13
Let’s draw particle trajectories in 4D (x,y,z,t)
[ T - 4 D t r a c k ] off
     file = 4Dtrack.out
  HistoryMax = 20
lec02.inp
Activate [T-4Dtrack] section at the end of lec02.inp and run PHITS
Open PHIG-3D with lec02.inp
Press “draw” button and make the cylinder transparent (right-click -> opacity)
Press “Particle tracks” button in the left tab
Press “Open” button and select “4dtrack.out”
Change “tend (ns)” to 4
Increase “No. Frames” to 10 (or more)
Press “     “ button to watch the animation
Change these values
Maximum history number to draw the trajectories
(Too large number may result in slower your computer)
PHIG-3D
SPEAKER_NOTES:
Now, I will explain how to plot 4-dimensional particle trajectories using PHIG-3D through Exercise 13.
First, delete the off on the right side of the [T-4DTrack] section in lec02 dot inp, and run PHITS.
The History Max parameter in the [T-4D Track] section means the maximum history number to draw the trajectories.
Please be careful not to set this value too large, as it may cause the computer to slow down and run out of memory.
After PHITS calculation is finished, please open PHIG-3D with lec02 dot inp.
Once PHIG-3D has launched, please click the Draw button in the lower-left corner of the window to draw a cylinder.
And then, please right-click the cylinder on the screen where the system is displayed, and use the Opacity slider at the bottom of the context menu that appears to make the cylinder semi-transparent.
Next, click Particle tracks in the left tab list.
After the Particle tracks tab menu is expand, please click the Open button at the top of the tab menu.
When the file selection window appears, please select 4dtrack dot out and click Open to display the particle trajectories.
The correspondence between particle types and line colors on the screen is displayed in the Particle tracks tab menu.
After particle trajectories are displayed, please set t end to 4 at the bottom of the Particle tracks tab menu to increase the number of frames, which allows you to define the time intervals for drawing particle trajectories.
To view an animation of the particle trajectories, please click the Play button below the seek bar.
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-end.inp

--- SLIDE 53 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Answer 13
You can save the animation with this button
SPEAKER_NOTES:
This is an example for drawing particle trajectories.
You can also save the animation as a video file by clicking the red circle to the left of the play button.

--- SLIDE 54 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 14
SLIDE_TEXT:
Exercise 14
① Select “xyz-mesh Tally” → ② Press “Select” button and select ”track_xz.out”* →
③ Press “hemisphere” button → ④ Check ”y” checkbox → ⑤ Press “Draw” button →
⑥ Change “Tally name” to draw proton and neutron fluences
①
②
③
④
⑤
⑥
*If you cannot find track_xz.out or got an error, you must run PHITS with input/lec02-6.inp
Let’s draw the fluence distributions obtained from [t-track] using PHIG-3D
SPEAKER_NOTES:
Next, I will explain how to draw tally output with xyz mesh using PHIG-3D through Exercise 14.
First, if you are continuing from the previous exercise, please click the File tab on the left side of the top menu in the PHIG-3D window and click Reload.
If you have closed PHIG-3D, please open lec02 dot inp in PHIG-3D again.
Once PHIG-3D has launched, please click the Draw button in the lower-left corner of the window to draw a cylinder.
Next, please click xyz-mesh Tally from the tab list on the left side of the PHIG-3D window.
After the xyz-mesh Tally tab menu will expand, please click the Select button at the top of the tab menu.
When the file selection window appears, please select track_xz dot out and open the file.
Next, please click the Cross-Section button located at the bottom of the PHIG-3D window.
The Cross-Section button is the icon that looks like a sphere cut in half.
When you click the Cross-Section button, a dialog window will appear.
Please check the y checkbox within that window, and then please click the OK button at the bottom to close the dialog window.
A cross-section of the cylinder will appear on the screen where the system is displayed, along with the tally results.
What is displayed on the screen is the fluence of carbon ions, which is one of the tally results obtained from previous exercises.
You can change the tally results displayed on the screen by selecting a different tally name from the tally name drop-down menu in the xyz-mesh Tally tab on the left and clicking the Draw button in the lower-left corner again.
MENTIONED_INPUT_NAMES: lec02-6.inp
ANSWER_FILE: input/lec02-6.inp

--- SLIDE 55 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
A free software for 3D visualization.
Draw 3D view of tally results for mesh = xyz.
You can output tally results in ParaView format (*.vtk) by specifying “vtkout = 1” in each tally section.
ParaView + PHITS sample (lecture\advanced\ParaView)
http://www.paraview.org
Coupling with ParaView
SPEAKER_NOTES:
This slide introduces the third graphic utility, ParaView.
ParaView is a free soft ware for 3-dimensional visualization.
It draw 3-D view of tally results for mesh = xyz.
You can output tally results in ParaView format by specifying vtkout = 1 in each tally section.
The sample file is put in this directory.

--- SLIDE 56 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
What is Tally?
How to use Tally?
Tally for checking geometry
Tally for calculating physical quantities
Software for drawing Tally results
Introduction of Each Tally
Summary
Table of Contents
SPEAKER_NOTES:
So, now, let me go on to the next subject.

--- SLIDE 57 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
List of Tallies (Visualize geometry)
SPEAKER_NOTES:
This is a list of tallies to visualize geometry in PHITS.
I will introduce them briefly.

--- SLIDE 58 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Gshow]
Tally for visualizing the geometry in 2 dimensions cut by certain slices.
Show region boundary, cell number, material ID etc.
Other tallies can be used for this purpose by setting icntl=8 in the [Parameters] section (see Lecture I).
SPEAKER_NOTES:
[T-Gshow] is for visualizing the geometry in 2 dimensions cut by certain slices.
It shows region boundary, cell number, material ID and so on.
Other tallies with gshow parameter can be used for this purpose by setting icntl = 8 in the [Parameters] section.

--- SLIDE 59 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-3Dshow]
Tally for visualizing the geometry in 3 dimensions from a viewpoint of a certain location in PHITS virtual space.
Activated only when icntl = 11 in the [Parameters] section.
SPEAKER_NOTES:
Three D show tally is for visualizing the geometry in three dimensions from a viewpoint of a certain location in PHITS virtual space.
It is activated only when icntl = 11 in the [Parameters] section.

--- SLIDE 60 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Parameters used in [T-3Dshow]
SPEAKER_NOTES:
Here is shown the relation of parameters of Three D show tally.
The name of parameters are written in red.
These parameters define conditions of eye point, Light source, Origin, and Picture Flame.
It is difficult to make the figure what you expected at first try.
So please adjust parameters, execute PHITS, and check the result repeatedly until the expected figure is obtained.

--- SLIDE 61 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
List of Tallies (Deduce physical quantity)
Described in the following pages.
SPEAKER_NOTES:
This is a list of all tallies to deduce physical quantity.
I will introduce major tallies briefly.

--- SLIDE 62 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Track]
You can visualize the trajectory of particle using [T-Track] by setting small mesh for tallying regions.
Tally for calculating track-length (cm) of particles in certain regions.
Average fluence (/cm2) in the region can be also deduced from this tally, dividing the track length (cm) by the volume of the region (cm3).
SPEAKER_NOTES:
[T-Track] is for calculating track-length of particles in certain regions.
Average fluence in the region can be also deduced from this tally, dividing the track length by the volume of the region.
As you used so far, you can visualize the trajectory of particles by setting small mesh for tallying regions.

--- SLIDE 63 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Cross]
Tally for calculating fluence or current (/cm2) of particles across certain surfaces.
Current is simply added by 1 when a particle cross the surface, while flux is added by 1/cos(θ).
SPEAKER_NOTES:
[T-Cross] is for calculating fluence or current of particles across certain surfaces.
Current is simply added by 1 when a particle cross the surface, while flux is added by 1/cos(theta).

--- SLIDE 64 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Point]
[T-Track]
Neutron and photon fluences calculated by [T-Point] and [T-Track] for similar conditions.
[T-Point]
Tally for calculating fluence (/cm2) of neutron and/or photon at a certain point or ring.
There are some using limitations. (See phits/utility/tpoint)
SPEAKER_NOTES:
[T-Point] is for calculating fluence of neutron and/or photon at a certain point or ring.
[T-Point] provides fluence in a short computational time, but there are some using limitations.
The instruction and samples are placed in the folder of phits/utility/tpoint.
If you are interested in the point tally, please see them.

--- SLIDE 65 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Bragg peak calculated by [T-Deposit] tally
[T-Deposit]
Tally for calculating deposition energy (MeV) in certain regions.
Ionization energy losses by charged particles are scored.            → Event-by-event data can be also deduced!
Neutron and photon doses can be also calculated by the kerma approximation.
SPEAKER_NOTES:
[T-Deposit] is for calculating deposition energy in certain regions.
Ionization energy losses by charged particles are scored.
Event-by-event data can be also deduced.
Neutron and photon doses can be also calculated by the Kerma approximation.

--- SLIDE 66 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Example of [T-Deposit2] tally
[T-Deposit2]
Tally for calculating event-by-event deposition energies in two regions.
Output a 2D plot to show their correlation.
Useful for simulating experimental data obtained by using two detectors.
SPEAKER_NOTES:
[T-Deposit2] is for calculating event-by-event deposition energies in two regions.
Output a 2-D plot to show their correlation, as shown here.
It is useful for simulating experimental data obtained by using two detectors such as dE-E telescope.

--- SLIDE 67 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Example of [T-Yield]
[T-Yield], [T-Product]
Tally for calculating the number of secondary particles generated by nuclear reactions in certain regions.
Energy or time distribution of secondary particles can be obtained from [T-Product].
Yields of each nuclide can be depicted on nuclear chart with [T-Yield].
SPEAKER_NOTES:
[T-Yield] and [T-Product] are for calculating the number of secondary particles generated by nuclear reactions in certain regions.
There are little differences between two tallies.
Energy or time distribution of secondary particles can only be obtained from [T-Product].
Yields of each nuclide can only be depicted on nuclear chart with [T-Yield].

--- SLIDE 68 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Depth-DPA distribution calculated using [T-DPA]
[T-DPA]
Tally for calculating the radiation damage index DPA in certain regions.
DPA is the average number of displaced atoms per atom of a material, and is calculated by multiplying the fluence with the damage cross section.
SPEAKER_NOTES:
[T-DPA] is for calculating the radiation damage index DPA in certain regions.
DPA is the average number of displaced atoms per atom of a material, and is calculated by multiplying the fluence with the damage cross section.

--- SLIDE 69 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Example of [T-LET] tally
*SED represents
Specific Energy Distribution
[T-LET], [T-SED]
Tally for calculating the probability densities of deposition energy or fluence in terms of LET, lineal energy (y), or specific energy (z) in microscopic sites distributed in certain regions.
Useful for radiobiological calculations.
SPEAKER_NOTES:
[T-LET] and [T-SED] are for calculating the probability densities of deposition energy or fluence in terms of LET, lineal energy or specific energy in microscopic sites distributed in certain regions.
They are useful for radiobiological calculations.

--- SLIDE 70 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Example of [T-Interact] tally
[T-Interact]
Tally for calculating the number of interactions occurred in certain regions.
The mean number or probability density of interactions can be obtained.
SPEAKER_NOTES:
[T-Interact] is for calculating the number of interactions occurred in certain regions.
The mean number or probability density of interactions can be obtained.

--- SLIDE 71 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Please see recommendation/dchain in detail
Time-dependent radioactivities of a water phantom irradiated by 150-MeV protons for 6 min.
[T-DCHAIN]
Tally for generating input files for DCHAIN, which can calculate the time evolution of the radioactive nuclides during and after irradiation.
DCHAIN is also included in the PHITS package.
SPEAKER_NOTES:
[T-DCHAIN] is for generating input files for DCHAIN.
DCHAIN can calculate the time evolution of the radioactive nuclides during and after irradiation of radiations.
DCHAIN is also included in the PHITS package.

--- SLIDE 72 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
What is Tally?
How to use Tally?
Tally for checking geometry
Tally for calculating physical quantities
Software for drawing Tally results
Introduction of Each Tally
Summary
Table of Contents
SPEAKER_NOTES:
Let me summarize the basic lecture number two.

--- SLIDE 73 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
A variety of information can be deduced from the PHITS simulation using functions called “Tally”.
2 types of tallies are implemented in PHITS, one is for visualizing PHITS geometry, and the other is for calculating physical quantities.
You can find examples of each tally in the “phits/sample/tally” folder.
Summary
It is preferable to copy the sample tally, paste it to your input file, and adjust it to your own simulation condition
SPEAKER_NOTES:
A variety of information can be deduced from the PHITS simulation using functions called Tally.
Two types of tallies are implemented in PHITS, one is for visualizing PHITS geometry, and the other is for calculating physical quantities.
For defining tally, you have to determine following components.
You can find examples of each tally in this folder, so you can copy and paste tally section from them.

--- SLIDE 74 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Depict the neutron and proton fluences, respectively, in your homework.
Adjust [t-deposit] to see the Bragg peak of proton.
Investigate the difference of the depth-dose distributions between the inside and outside of the beam center (within the radius of 2.5 cm or not) by changing r-z mesh.
Output the depth-dose distributions between inside and outside the beam center in the same page (add samepage parameter in [t-deposit])
Homework #2
SPEAKER_NOTES:
Here is shown a homework number two.
This is continued from the homework number one.
The subjects are as follows.
At first, please depict the neutron and proton fluences, respectively, in your homework.
Second, please adjust [T-Deposit] to see the Bragg peak of proton.
And last, please investigate the difference of the depth-dose distributions between the inside and outside of the beam center within the radius of 2.5 cm or not by setting an r-z mesh.
After that, please change the minimum and maximum values of y axis in the graph for the depth-dose distribution for comparing them in the same scale.

--- SLIDE 75 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Example Answer
Proton (up) and neutron (down) fluences.
Depth-dose distribution inside (black)
and outside (red) the beam radius.
SPEAKER_NOTES:
This is an example of the answer.

--- SLIDE 01 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
PHITS講習会 基礎実習（II）：
Tally（タリー）の定義
2026年2月改訂
phits/lecture/basic/lec02
SPEAKER_NOTES:
それでは、PHITS講習会の基礎実習2番を始めます。
本実習で作業するフォルダを開くために、PHITSのインストールフォルダから、lectureフォルダ、basicフォルダ、lec02フォルダへと移動してください。
この作業フォルダの中には、いくつかファイルがありますが、本実習の課題では、主にlec02.inpファイルを編集・実行します。

--- SLIDE 02 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
本実習の目標
同じ粒子輸送シミュレーションから様々な物理量（粒子毎の飛跡空間分布，発熱量の深さ分布など）を導出できるようになる。
宿題体系内の陽子（上）・中性子（下）飛跡空間分布
宿題体系内の線量-深さ分布
SPEAKER_NOTES:
本実習では、同じ粒子輸送シミュレーションから、下の図に示すような、粒子ごとの飛跡空間分布や発熱量の深さ分布など、様々な物理量を導出できるようになることを目標とします。

--- SLIDE 03 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
実習内容
Tallyとは何か
Tallyの使い方
ジオメトリの確認
物理量の導出
Tally結果描画ソフトウェア
各Tallyの紹介
まとめ
SPEAKER_NOTES:
それでは、初めにタリーとは何かを説明します。

--- SLIDE 04 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
適当な日本語訳がないので…PHITS（の専門）用語として、
 Tally = （仮想的な）検出器
 Tallyする = （仮想的に）検出器を用意し物理量を測定する
といった使い方をしている。
Tally: a record of the number or amount of something, 	especially one that you can keep adding to;
[Oxford Advanced Learner’s Dictionary (7th edition), OXFORD.]
Tallyとは何か
SPEAKER_NOTES:
タリーという単語を英英辞典で調べると、このように説明されています。
適当な日本語訳がないので、PHITSの専門用語として、「仮想的な検出器」を「タリー」と呼んだり、「検出器を用意して物理量を測定すること」を「タリーする」と呼んだりします。

--- SLIDE 05 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
PHITSは１つ１つの放射線挙動をコンピュータ内で全て再現するので、任意の場所、時間における放射線の数やエネルギー分布などを調べることが可能。
Tallyとは何か
[T-Track](飛跡描画タリー)による結果
この領域を通過する
中性子は、線源１つ発生あたり何個か？
SPEAKER_NOTES:
PHITSは１つ１つの放射線挙動をコンピュータ内で全て再現するので、任意の場所や時間における放射線の数やエネルギー分布などを調べることができます。
下の動画は、ある標的への放射線照射のシミュレーションにおいて、 [T-Track]を使って放射線の挙動を二次元表示した結果です。
点滅しながら動いている点が粒子です。
線源から放出された粒子が標的に到達すると、そのまま標的を通過したり、あるいは標的の原子核との核反応によって二次粒子が生成されたりします。
このような放射線の挙動を時間積分すると、粒子が飛んだ跡、すなわち飛跡の空間分布が表示されます。
ここでは放射線の挙動を可視化した結果を示していますが、その他にも、例えば、図の右上の黄色い円柱で示す領域を通過する中性子の数やエネルギー分布を出力することも可能です。

--- SLIDE 06 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
物理量として意味のある測定結果を得るためには、適切な条件（検出器の位置、検出粒子の種類やエネルギーなど）を設定する必要がある。
Tallyとは何か
しかし、個人で用途に応じた条件を設定するのは大変！！
…なので、欲しい物理量に対応したTallyを用いる。
 ジオメトリの確認
作成した体系を見たい	→  gshowオプション, [T-3Dshow]
 物理量の導出
粒子束（フルエンス）	→  [T-Track], [T-Cross]
付与エネルギー（発熱）	→  [T-Deposit], [T-Deposit2]
核反応による生成粒子	→  [T-Yield], [T-Product]
SPEAKER_NOTES:
現実世界の実験では、物理量として意味のある測定結果を得るために、検出器の種類や位置などを適切に設定します。
PHITSによるシミュレーションも同様で、意味のある結果を得るためには、タリーの条件を適切に設定しなければなりません。
このとき、PHITSには、様々な種類のタリーが準備されているため、ユーザーは欲しい物理量に対応したタリーを選択し、入力パラメータをいくつか設定することで目的を達成できます。
具体例として、ジオメトリの確認にはgshowオプションを設定したタリー。
フルエンスの導出は[T-Track]、[T-Cross]。
付与エネルギー量の導出は[T-Deposit]。
核反応による生成粒子の導出は[T-Yield]、[T-Product]が、それぞれ対応します。

--- SLIDE 07 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
実習内容
Tallyとは何か
Tallyの使い方
ジオメトリの確認
物理量の導出
Tally結果描画ソフトウェア
各Tallyの紹介
まとめ
SPEAKER_NOTES:
それでは、タリーの使い方の一つとして、ジオメトリの確認方法を説明します。

--- SLIDE 08 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[Material], [Surface], [Cell]セクションで定義したジオメトリ  （仮想空間）を2次元的、或いは3次元的に表示させ確認する。
Tallyの使い方(ジオメトリの確認)
gshowオプションを用いた2次元的な表示（断面図）
[T-3Dshow]やPHIG-3Dを用いた3次元的な表示
新しいジオメトリを組むたびに、正しく定義されているかを確認することが重要！！
SPEAKER_NOTES:
タリーを用いることで、入力ファイルで定義したジオメトリを表示させて確認することができます。
具体的には、gshowオプションを用いたジオメトリの2次元断面図の表示や、[T-3Dshow]を用いたジオメトリの3次元的な表示が可能です。
なお、ジオメトリの確認には、タリーで図示する他にも、PHIG-3Dも役立ちます。
ここで強調しておきたいこととしては、新しいジオメトリを組むたびに、ジオメトリが想定通りに設定されているかを確認することが重要です。
もし確認しなかった場合、想定通りのジオメトリが設定できていないと、正しい計算結果が得られませんのでご注意ください。

--- SLIDE 09 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1
[T-Track]にあるgshowオプションを用いて、lec02.inpの体系を2次元的に確認してみよう
[Parameters]セクションで“icntl=8”としてPHITSを実行する。
    （gshowオプションを使うときはicntl=8）
[ M a t e r i a l ]
mat[1]    H 2  O 1

・ ・ ・ ・ ・ ・

[ S u r f a c e ]
  10  cz      10.
 101  pz       0.
 102  pz      50.
 999  so     500.

[ C e l l ]
  1     1 -1.0  -10  101  -102
 100    0      -999  #all
 101   -1       999
z軸を中心軸とする
半径10cm, 高さ50cmの水の円柱
lec02.inp
SPEAKER_NOTES:
それでは、課題1を始めます。
ここでは、lec02.inpで定義されているジオメトリを、[T-Track]セクションにあるgshowオプションを用いて確認します。
スライドの左側にはlec02.inpの一部を抜粋しています。
[Material]セクション、[Surface]セクション、[Cell]セクションを見ると、z軸を中心軸とする、半径10cm、高さ50cmの水の円柱が定義されていることがわかります。
ここで、[Parameters]セクションのicntlというパラメータの値を、0から8に変更してください。
icntlはPHITSの基本動作オプションで、0と設定されていると通常の粒子輸送計算が実行されます。
icntlを8と変更することで、gshowオプションでジオメトリを表示するモードに切り替わります。
icntlの値を変更したら、入力ファイルを上書き保存してからPHITSを実行し、出力されるファイルのうち、track_xy.epsを開いて、ジオメトリがどのように表示されるかを確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-2.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
解答1
track_xz.eps
xz座標平面
[ P a r a m e t e r s ]
icntl = 8
・ ・ ・ ・ ・ ・

[ T - T r a c k ]
・ ・ ・ ・ ・ ・
axis = xz
file = track_xz.out
part = all
gshow = 3
epsout = 1
gshowオプション
lec02.inp
0: 描画しない
1: 境界線のみ描画
2: 境界線と物質名を描画
3: 境界線と領域番号を描画
SPEAKER_NOTES:
課題1の解答です。
epsファイルを開くと、右に示すように、円柱をxz平面で切断した断面である長方形が表示されます。
定義されている水の円柱の半径は10cm、高さは50cmですので、表示されている長方形の大きさは、縦20cm、横50cmとなっています。
なお、この図を出力した[T-Track]セクションの、gshowオプションの値は3に設定されています。これは、ジオメトリの境界線と領域番号を図に描画することを意味します。
gshowオプションの値を変えることで、図に描画される内容を変更することができます。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-2.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
実習内容
Tallyとは何か
Tallyの使い方
ジオメトリの確認
物理量の導出
Tally結果描画ソフトウェア
各Tallyの紹介
まとめ
SPEAKER_NOTES:
それでは、次のスライドから、タリーを使って物理量を導出する方法を学んでいきます。

--- SLIDE 12 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
どの空間（面）における、どの粒子の、どういった物理量を、どういう形式で、見たいかを指定する。
Tallyの使い方（物理量の導出）
空間（面）：メッシュ(mesh =)を用いて定義する。
粒子：粒子名(part =)を指定する。
物理量：単位(unit =)を選ぶ。
形式：出力データの横軸(axis =)を決める。
  （空間のX,Y,Z 座標(x,y,z)、エネルギー(eng)、時間(t)に
   応じたメッシュ定義文が必要）
求める物理量に応じてこれらのパラメーターを変える！！
SPEAKER_NOTES:
最初のほうでも述べましたが、物理量を導出するためには、タリーの条件を適切に設定する必要があります。
設定する手順としては、はじめに、導出したい物理量に適したタリーを選択します。
そして、「どの空間における、どの粒子の、どういった物理量を、どういう形式で見たいか」、という、4つの条件を指定するため、それぞれパラメータを設定します。
具体的なパラメータ名としては、mesh、part、unit、axisが、それぞれの条件と対応します。
これらのパラメータは、求める物理量に応じて適切に設定する必要があります。

--- SLIDE 13 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
例えば、ファイルlec02.inpの[T-Track]セクションでは、
[ T - T r a c k ]
 title = Track Detection in xyz mesh mesh =  xyz
   x-type =    2
       nx =   25
     xmin =  -25.
     xmax =   25.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =   50
     zmin =  -20.
     zmax =   80.
   e-type =    1
       ne =    1
            0.0  1.0e+9
   t-type =    1
       nt =    1
            0.0  1.0e+9
     unit =    1
     axis =   xz
     file = track_xz.out
     part =  all
    gshow =   3
   epsout =    1
空間（面）：
mesh = xyzの場合は、xyz座標系で分割
粒子：
part = allの場合は、全ての粒子を対象とする。
物理量：
unit = 1の場合は、[1/cm2/source]を単位とする量（[t-track]の場合）
形式:
axis = xzの場合は、xz平面に平行な断面図で出力する。
[T-Track]は、放射線（個数）を数えるタリー。
いわゆる粒子束（フルエンス）を求めることができる
→ 平均飛跡を描画する目的で利用可能
SPEAKER_NOTES:
例として、lec02.inpに書かれている[T-Track]セクションを示します。
[T-Track]は、放射線の個数を数えるタリーで、粒子フルエンスを求めるときに利用される他にも、平均飛跡を描画する目的でも利用できます。。
先ほどのスライドで示したパラメータの設定値をそれぞれ見ていくと、meshパラメータはxyzと設定されています。これは、空間をxyz座標系で分割することを意味します。
その下の行からは、xyz座標をどのように分割するかを設定しています。
unitパラメータは1と設定されています。この値は、[T-Track]の場合は単位を(1/cm2/source)とすることを意味します。
axisパラメータはxyと設定されています。これは、xy平面に平行な断面図で出力することを意味します。
partパラメータはallと設定されています。これは、すべての粒子をタリーの対象とすることを意味します。

--- SLIDE 14 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Track]の計算方法は…
x-axis
z-axis
SPEAKER_NOTES:
ここで、[T-Track]の計算方法を図と共に説明します。
この例では、ある空間が、xz座標系について四角の領域に細かく分けられています。
左にあるオレンジ色の丸は、タリーの対象となる粒子です。
粒子が空間を通過するとき、粒子が通った四角にだけ色を付けます。

--- SLIDE 15 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
x-axis
z-axis
[T-Track]の計算方法は…
SPEAKER_NOTES:
次の粒子が下から飛んできたとき、先ほどと同様に、粒子が通った四角にだけ色を付けます。
既に色がついている四角は、色を青から緑に変更します。

--- SLIDE 16 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
x-axis
z-axis
[T-Track]の計算方法は…
SPEAKER_NOTES:
また粒子が飛んできて、今度は途中で移動する方向が変わりましたが、このときも、粒子が通った四角にだけ色を付けます。
緑色の四角を通過した場合は、色を緑から黄色に変更します。

--- SLIDE 17 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
x-axis
z-axis
[T-Track]の計算方法は…
SPEAKER_NOTES:
更に粒子が飛んできて、途中で移動する方向が変わり、更に途中で停まりました。
このときも、先ほどと同じルールで四角に色を付けます。

--- SLIDE 18 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
x-axis
z-axis
[T-Track]の計算方法は…
SPEAKER_NOTES:
矢印の線は先ほどの4つの粒子の飛行経路を示しており、四角の色は粒子のフルエンスを示しています。
フルエンスが高い領域は黄色、フルエンスが中程度の領域は緑色、フルエンスが低い領域は水色となります。
また、色のついていない四角は、粒子が通過していないことを意味します。

--- SLIDE 19 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2
[T-Track]を用いて、放射線フルエンスの空間分布を確認しましょう。
[Parameters]セクションで“icntl = 0”としてPHITSを実行する。
放射線の振る舞いはどうなるか？
[ P a r a m e t e r s ]
icntl = 8
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type = 1
  r0 = 2.5
  z0 = -10.
  z1 = -10.
  dir =  1.0
  e0 = 250.
proj = 12C
半径2.5cm,
250 MeV/nの
炭素ビーム
track-xz.epsを確認
lec02.inp
SPEAKER_NOTES:
それでは、課題2に進みます。
ここでは、[T-Track]を用いて、放射線フルエンスの空間分布を確認します。
これまでの課題と同様に、スライドの左側にlec02.inpの一部を抜粋しており、この課題において編集すべきパラメータを赤線で示しています。
[Source]セクションを確認すると、250 MeV/n の炭素ビームが、水標的の左側から入射するように設定されています。
課題1でジオメトリを確認するために[Parameters]セクションのicntlの値を8に変更しましたが、この課題では、粒子輸送計算を行うために、icntlの値を0と設定してください。
編集が終わったら、入力ファイルを上書き保存してPHITSを実行してください。
そして計算が終わったら、出力されるファイルのうち、track_xz.epsを開いて、計算結果を確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-3.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
解答2
file = :
出力ファイル名を指定する。
epsout = 1:
file =で指定したファイル名のepsファイルを作成する。
（***.out → ***.eps）
[ P a r a m e t e r s ]
icntl = 0
・ ・ ・ ・ ・ ・

[ T - T r a c k ]
・ ・ ・ ・ ・ ・
axis = xz
file = track_xz.out
part = all
gshow = 3
epsout = 1
lec02.inp
track_xz.eps
[ T-Track ]
    title = Track  Detection
     mesh =  xyz
   x-type =    2
     xmin =  -25.00000
     xmax =   25.00000
#    xdel =  0.5000000
       nx =    100
・ ・ ・ ・ ・ ・
track_xz.out
epsout = 1
SPEAKER_NOTES:
課題2の解答です。
track_yz.epsを開くと、右下に示すようにとxz座標平面に関するフルエンスが表示されます。
表示されている色について、暖色系はフルエンスが高いことを意味し、寒色系はフルエンスが低いことを意味します。
フルエンスの空間分布をみると、円柱の中央は炭素ビームが照射されているため高いフルエンスを示しています。
また、炭素ビームと標的との核反応によって二次粒子が生成されるため、中程度のフルエンスが炭素ビームの周辺に現れます。
なお、タリー結果が出力されるファイルの名前は、[T-Track]セクションのfileパラメータで指定することができます。
出力ファイルであるtrack_xz.outをエディタで開くと、左下に示すように、タリーセクションで設定された情報と、タリー結果が文字で閲覧できます。
先ほど開いたtrack_xz.epsは、outファイルの内容が図示されたもので、入力ファイルの[T-Track]セクションでepsoutを1と設定すると自動で出力されます。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-3.inp

--- SLIDE 21 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
*_err.epsファイルの活用
２次元プロットを出力するタリー（“axis=xy, rz”など）は、その統計誤差を*_err.out及び*_err.epsファイルとして出力する。
暖色系は相対誤差が大きい（１に近い）領域を表し、寒色系は相対誤差が小さい領域を表す。
track_xz_err.eps
SPEAKER_NOTES:
次に、track_yz_err.epsを開くと、下に示す図が表示されます。
これはフルエンスの統計誤差を示しており、暖色系は相対誤差が大きく、寒色系は相対誤差が小さいことを意味します。
2次元プロットで物理量を出力した場合、このように統計誤差の空間分布を表示できますので、例えば着目している領域の計算精度が十分かどうか判断する目安などにご利用ください。

--- SLIDE 22 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Red Screen
2次元プロットで1つも粒子がタリーされなかった場合、全ての領域が赤色になる。 → インプットファイルに何か問題がある場合が多い！
track_xz.eps with e0 = 0
SPEAKER_NOTES:
ここで、PHITS計算で生じるRed Screenについて紹介したいと思います。
Windowsのシステムエラーを思い起こさせる名前ですが、深刻なエラーではないのでご安心ください。
これは、2次元プロットで1つも粒子がタリーされなかった場合に、すべての領域が赤色になることを指します。
例として、[Source]セクションでdir=-1.0と設定し、炭素ビームを円柱に入射させなかった時の計算結果を中央に示します。
Red Screenが生じた場合、線源粒子の情報やジオメトリ、あるいはタリー条件など、入力ファイルの設定に何らかの問題があることが多いため、入力ファイルを見直すことをお勧めします。

--- SLIDE 23 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Tallyの使い方（物理量の導出）
どの空間（面）における、どの粒子の、どういった物理量を、どういう形式で、見たいかを指定する。
空間（面）：メッシュ(mesh =)を用いて定義する。
粒子：粒子名(part =)を指定する。
物理量：単位(unit =)を選ぶ。
形式：出力データの横軸(axis =)を決める。
  （空間のX,Y,Z 座標(x,y,z)、エネルギー(eng)、時間(t)に
   応じたメッシュ定義文が必要）
SPEAKER_NOTES:
ここからは、タリーセクションのパラメータの設定方法について学びます。
はじめに、タリー対象とする空間を指定する方法を学びます。

--- SLIDE 24 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
メッシュ型(mesh=)の種類
メッシュ型には、xyz, r-z, regの3種類がある。
SPEAKER_NOTES:
形状メッシュには、xyz、r-z、regの3つがあります。
xyzメッシュは、空間をxyz座標系で分割します。
r-zメッシュは、空間を円柱座標系で分割します。
regメッシュは、領域番号やセル番号で指定します。

--- SLIDE 25 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
   mesh =  xyz
   x-type =    2
       nx =   25
     xmin =  -25.
     xmax =   25.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =   50
     zmin =  -20.
     zmax =   80.
   e-type =    1
       ne =    1
            0.0  1.0e+9
   t-type =    1
       nt =    1
            0.0  1.0e+9
・ ・ ・ ・ ・ ・
mesh = xyz:
xyz座標系に沿った空間の指定
⇒ x-type, y-type, z-typeサブセクションが必要になる。
メッシュ型
lec02.inp
SPEAKER_NOTES:
lec02.inpの[T-Track]セクションでは、xyzメッシュを選択しています。
このとき、空間をどのように分割するかを設定するために、x-type、y-type、z-typeサブセクションをmeshパラメータのすぐ下に書く必要があります。
MENTIONED_INPUT_NAMES: lec02.inp

--- SLIDE 26 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
メッシュの定義
1: 群数、分点をデータで与える。
  （与えるデータはnx+1個）
2,3: 群数と最小値、最大値を与え、等分する。
       （2は線形、3は対数で等分する）
4,5: 最小値、最大値、メッシュ幅xdel（5はメッシュ幅の対数値）を与え、等分する。
メッシュを定義することで各座標軸（サブセクション）を分割する
サブセクションの種類はx-type, y-type, z-type, r-type, e-type, t-type, a-type

メッシュの定義方法は以下の5種類 （ただし4,5はあまり使わない）
x軸       y軸        z軸       半径    エネルギー  時間  角度
x-type = 1
  nx = 10
  0  1  2  3  5  10
  15  20  30  50  100
x-type = 2
  nx = 100
  xmin =  0
  xmax =  1000
x-type = 3
  nx = 100
  xmin =  0.1
  xmax =  5000
サブセクションで定義する変数の “x” は、サブセクションの種類に従って“y”, “z”, “r”, “e” , “t” , “a” などに変更する。（例: y-type, ny, ymin )
SPEAKER_NOTES:
このスライドでは、メッシュの定義方法について説明します。
メッシュを定義することで、各座標軸を分割します。
サブセクションの種類は、x軸、y軸、z軸、半径、エネルギー、時間、角度の7種類です。
メッシュの定義方法は5種類あります。ただし、4番と5番はあまり利用しません。
まず1番の定義方法は、メッシュの群数を与え、次の行でそれぞれの分点を数値データで与えます。
2番と3番の定義方法は、メッシュの群数と、範囲の最小値と最大値を与えて等分します。
2番は線形、3番は対数で、それぞれ等分します。
4番と5番の定義方法は、メッシュの範囲の最小値と最大値、そしてメッシュの幅を与えて等分します。
4番はメッシュ幅の数値を、5番はメッシュ幅の対数値を、それぞれ設定します。
なお、サブセクションで定義する変数の赤字の部分は、サブセクションの種類に従って変更します。
例えば、y軸のサブセクションを設定する場合は、赤文字をyに置き換えます。

--- SLIDE 27 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題3
[T-Track]の空間メッシュ分割数を増やして、解像度を上げましょう。
メッシュの分割数が少ないと、図示した場合の飛跡が粗くなる。
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
   mesh =  xyz
   x-type =    2
       nx =   25
     xmin =  -25.
     xmax =   25.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =   50
     zmin =  -20.
     zmax =   80.
・ ・ ・ ・ ・ ・
lec02.inp
track_xz.eps
メッシュの分割数を与えるパラメータ nx, nz を4倍にして解像度Up!

ただし、断面の数（ny）は変更しない。
SPEAKER_NOTES:
それでは、課題3に進みます。
この課題では、[T-Track]セクションの形状メッシュの群数を増やして、図の解像度を上げることを目標とします。
lec02.inpに設定されている[T-Track]セクションを見ると、nxが25, nzが50に、それぞれ設定されています。
ここでは、形状メッシュの群数をそれぞれ4倍にして解像度を上げてください。
注意点として、断面の数は変更したくないので、nyの値は変更しないでください。
編集が終わったら、入力ファイルを保存してPHITSを実行してください。
そして、計算が終わったら、track_xz.epsを開いて、図がどのように変わったかを確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-4.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
解答3
lec02.inp
メッシュを細かく取ることにより、画像の空間分解能が改善された
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
   mesh =  xyz
   x-type =    2
       nx =   100
     xmin =  -25.
     xmax =   25.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =   200
     zmin =  -20.
     zmax =   80.
・ ・ ・ ・ ・ ・
track_xz.eps
SPEAKER_NOTES:
課題3の解答です。
上段の図は、形状メッシュの群数を増やす前のフルエンスの空間分布で、ご覧の通り、解像度が粗いです。
下段の図は、形状メッシュの群数を4倍に増やした後の結果です。
メッシュを細かくとることによってフルエンスの空間分布の図の空間分解能が改善され、粒子の飛跡をよりはっきりと確認できるようになりました。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-4.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
e-type = 1
  ne = 1
  0.0  1.0e+9
t-type = 1
  nt = 1
  0.0  1.0e+9
・ ・ ・ ・ ・ ・
課題4
[T-Track]のt-typeサブセクションを変更する。

 “t-type=2”とし、0～5 nsecまでを5等分するように各種パラメータを定義する。
  （nt, tmin, tmaxをそれぞれ定義、
  26ページの「メッシュの定義」を参考）
lec02.inp
[T-Track]の時間メッシュを分割して、粒子フルエンスの時間変化を確認しましょう。
時間の単位はnsec （1.0e+9は線源発生から1秒後）
SPEAKER_NOTES:
それでは、課題4に進みます。
ここでは、[T-Track]セクションの時間メッシュを分割して、粒子フルエンスの時間変化を観察することを目的とします。
現在の設定を見ると、t-typeサブセクションは設定されていますが、群数は1となっており、指定した時刻の間のタリー結果が時間積分されたものが出力されるようになっています。
時間の分点には0と10の9乗が設定されていますが、PHITSは線源粒子が発生した時刻を0秒とし、入力ファイルの時間の単位はナノ秒であるため、線源発生から1秒後の結果がタリーされることになります。
この課題では、0秒から5ナノ秒までを5等分してタリー結果を出力するように、t-typeサブセクションを編集してください。
具体的には、t-typeを1から2に変更し、nt, tmin, tmaxを適切な値に設定してください。
その際、t-typeが2のときに不必要なパラメータは、削除するかコメントアウトしてください。
編集が終わったら、入力ファイルを保存してPHITSを実行してください。
そして、計算が終わったら、track_xz.epsを開いて結果を確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-5.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
解答4
1ページ目
（t = 0 ~ 1 nsec）
2ページ目
（t = 1 ~ 2 nsec）
3ページ目
（t = 2 ~ 3 nsec）
SumatraPDFでは，左右キーで図のページを切り替えられます
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
e-type = 1
  ne = 1
  0.0  1.0e+9
t-type = 2
  nt = 5
$  0.0  1.0e+9
  tmin =  0.0
  tmax =  5.0
・ ・ ・ ・ ・ ・
lec02.inp
PHITS結果からGIF動画の作り方はphits/utility/animationを参照
track_xz.eps
SPEAKER_NOTES:
課題4の解答です。
入力ファイルの変更箇所としては、まずt-typeを1から2に変更します。
次に、時間メッシュの群数を設定するパラメータである、ntの値を、1から5に変更します。
また、t-typeが1のときに必要だった、分点の数値データを設定する行をコメントアウトします。
そして、t-typeが2のときに必要となるパラメータ、tminとtmaxを新たに追加し、それぞれの値を0と5に設定します。
以上の設定により、track_xz.epsファイルには、右に示す図のように、線源粒子が発生してから5ナノ秒までの放射線の挙動が1ナノ秒刻みで出力されるようになりました。
なお、epsファイルを閲覧する際にSumatraPDFを使っている場合には、左右の矢印キーで図のページを切り替えることができます。
フルエンスの空間分布の時間変化をタリーすることで、放射線が円柱の左側から入射し、さまざまな方向に向かっていく様子が確認できます。
このように、各時刻の計算結果を出力することで、5ページで示したようなgif動画を作成することが可能です。
PHITSのタリー結果からgif動画を作成する方法は、phits/utility/animationに例題がありますので、興味のある方はそちらをご覧ください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-5.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Tallyの使い方
どの空間（面）における、どの粒子の、どういった物理量を、どういう形式で、見たいかを指定する。
空間（面）：メッシュ(mesh =)を用いて定義する。
粒子：粒子名(part =)を指定する。
物理量：単位(unit =)を選ぶ。
形式：出力データの横軸(axis =)を決める。
  （空間のX,Y,Z 座標(x,y,z)、エネルギー(eng)、時間(t)に
   応じたメッシュ定義文が必要）
SPEAKER_NOTES:
それでは、続いて、タリー対象とする粒子の指定方法について学びます。

--- SLIDE 32 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5
粒子フルエンスの分布を粒子毎に分けてタリーしてみましょう。
[T-Track]のpartパラメータを書き換える。
粒子はproton, neutronなど粒子の名前で、重イオンは12Cのように「質量数＋元素記号」で表現（allは全粒子）
複数の粒子を指定するときはスペース区切り（例： part = 12C proton neutron）
出力ファイル数を減らすため時間メッシュ数（nt）は1に戻す
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
t-type = 2
  nt = 5
  tmin =     0.0
  tmax =    5.0
・ ・ ・ ・ ・ ・
axis = xz
file = track_xz.out
part = all
・ ・ ・ ・ ・ ・
lec02.inp
track_xz.eps
12C、陽子、中性子の振る舞いはそれぞれどうなっているだろうか。
SPEAKER_NOTES:
早速、課題5に進みます。
この課題では、粒子フルエンスの空間分布を、粒子ごとに分けてタリーすることを目的とします。
ここでは、炭素イオン、陽子、中性子をタリーの対象とします。
タリー対象とする粒子はpartパラメータで設定するのですが、このとき、陽子や中性子はprotonやneutronのように粒子の名前で、重イオンの場合は12Cのように質量数と元素記号で表現します。
また、partパラメータに複数の粒子を指定するときは、それぞれをスペースで区切る必要があります。
なお、この課題では出力される図の枚数を減らすために、先ほど変更したt-typeサブセクションのうち、ntの値を1に戻してください。
編集が終わったら、入力ファイルを保存してPHITSを実行してください。
そして、計算が終わったら、track_xz.epsを開いて結果を確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-6.inp

--- SLIDE 33 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
解答5
track_xz.eps
1ページ目
(part = 12C)
2ページ目
(part = proton)
3ページ目
(part = neutron)
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
t-type = 2
  nt = 1
  tmin =     0.0
  tmax =    5.0
・ ・ ・ ・ ・ ・

axis = xz
file = track_xz.out
part = 12C proton neutron
・ ・ ・ ・ ・ ・
lec02.inp
SPEAKER_NOTES:
課題5の解答です。
入力ファイルの変更箇所としては、まずt-typeサブセクションのntの値を5から1に戻します。
次に、partをallから12C proton neutron と変更します。
以上の変更により、track_xz.epsには、右に示す図のように、炭素イオン、陽子、中性子のフルエンスの空間分布がそれぞれ出力されます。
粒子ごとにタリー結果を出力することで、線源位置から放出された炭素イオンが水の円柱標的で減速し、途中で止まっていることが確認できます。
また、標的中で起きた核反応によって生成された陽子や中性子が、様々な方向に飛んでいることも確認できます。
このように、興味のある粒子をpartで指定して別個にタリーすることで、計算結果の考察の助けとなります。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-6.inp

--- SLIDE 34 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Tallyの使い方
どの空間（面）における、どの粒子の、どういった物理量を、どういう形式で、見たいかを指定する。
空間（面）：メッシュ(mesh =)を用いて定義する。
粒子：粒子名(part =)を指定する。
物理量：単位(unit =)を選ぶ。
形式：出力データの横軸(axis =)を決める。
  （空間のX,Y,Z 座標(x,y,z)、エネルギー(eng)、時間(t)に
   応じたメッシュ定義文が必要）
SPEAKER_NOTES:
それでは、続いて、タリーで出力するデータの横軸を指定する方法を学びます。

--- SLIDE 35 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題6
各放射線のエネルギー分布をタリーしよう
[T-Track]セクションのaxisをxzからengに変更する

出力結果のページ数を減らすために、nxとnzは1に変更する

“e-type = 2”とし、0～300MeV/nまでを100等分するようにパラメータを定義する
  （ne, emin, emaxをそれぞれ定義、
  26ページの「メッシュの定義」を参考）

出力ファイル名を“track_eng.out”に変更する*
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
  x-type = 2
    nx = 100
・ ・ ・ ・ ・ ・
  z-type = 2
    nz = 200
・ ・ ・ ・ ・ ・
e-type = 1
  ne = 1
  0.0  1.0e+9
unit = 1
axis = xz
file = track_xz.out
・ ・ ・ ・ ・ ・
lec02.inp
*track_xz.outは後の演習で利用するので忘れずにファイル名を変更
SPEAKER_NOTES:
それでは、課題6に進みます。
これまでは、粒子フルエンスの空間分布を出力していましたが、ここでは、粒子フルエンスをエネルギーの関数としてタリーします。
まず、[T-Track]セクションのaxisパラメータを、xzからengに変更してください。
また、これまで空間分布を出力するために、x-typeサブセクションとz-typeサブセクションの群数を、それぞれ100と200と設定していましたが、axisを変更しますので、このままだと、100かける200=2万ページの結果が出力されてしまいます。
これを回避するために、nxとnzの値は1に変更してください。
続いて、e-typeを1から2に変更し、0MeVから300MeV/nまでの範囲を100等分するように、各種パラメータを設定してください。
e-typeが2のときに必要となるパラメータは、エヌイー、emin、emaxです。
また、e-typeが2のときに不必要なパラメータは、削除するかコメントアウトしてください。
そして、出力ファイル名が現状の設定ではtrack_xz.outとなっていますので、track_eng.outに変更してください。
編集が終わったら、入力ファイルを保存してPHITSを実行してください。
そして、計算が終わったら、track_eng.epsを開いて結果を確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-7.inp

--- SLIDE 36 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
解答6
炭素線源のエネルギーは250 MeV/n
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
  x-type = 2
    nx = 1
・ ・ ・ ・ ・ ・
  z-type = 2
    nz = 1
・ ・ ・ ・ ・ ・
e-type = 2
  ne = 100
$  0.0  1.0e+9
  emin = 0.0
  emax = 300.0
unit = 1
axis = eng
file = track_eng.out
・ ・ ・ ・ ・ ・
lec02.inp
track_eng.eps
イオンに対するエネルギーの基本単位はMeV/n（核子あたりの運動エネルギー）*
イオン以外に対するエネルギーの単位はMeVだが、表記上は(MeV/n)となる（n=1と仮定）
e-unitパラメータを定義することにより、波長(nm)やLET(keV/μm)でスコアすることも可能
*イオンを全運動エネルギー（MeV）でタリーしたい場合はiMeVperN=0とする（version.336以前のデフォルト）
SPEAKER_NOTES:
課題6の解答です。
入力ファイルの変更箇所としては、nxとnzの値を1とします。
これにより、x軸方向とz軸方向の空間メッシュの群数が1となり、出力ファイルが1ページとなります。
次に、e-typeを1から2に変更し、エネルギーメッシュの群数を設定するパラメータであるエヌイーの値を1から100に変更します。
また、e-typeが1のときに必要だった、分点の数値データを設定する行をコメントアウトし、e-typeが2のときに必要となるパラメータ、eminとemaxを新たに追加し、それぞれの値を0と300と設定します。
そして、axisをxzからengに変更し、fileをtrack_xz.outからtrack_eng.outに変更します。
以上の変更により、track_eng.epsには、右に示す図のように、横軸を核子当たりの運動エネルギーとした、炭素イオン、陽子、中性子の粒子フルエンス分布が出力されます。
タリー結果を見ると、炭素イオンのフルエンスは250MeV/nにピークが現れることが分かります。
これは、[Source]セクションのe0パラメータで設定した炭素イオンの入射エネルギーが250MeV/nで、線源位置から円柱に入射するまでは真空中であることに由来します。
なお、タリー結果のエネルギーの単位について、いくつか補足情報があります。
まず、イオンに対するエネルギーの基本単位はMeV/nとなります。
もしイオンの全運動エネルギーでタリーしたい場合は、[Parameters]セクションでiMeVperNを0と設定してください。
次に、陽子や中性子、光子など、イオン以外の粒子の対するエネルギーの基本単位はMeVなのですが、表記上はMeV/nとなってしまうためご注意ください。
また、e-unitパラメータを定義することで、波長やLETでスコアすることも可能ですので、目的に応じて適宜ご利用ください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-7.inp

--- SLIDE 37 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
課題7
エネルギー軸（横軸）を対数(log)スケールに変えてみましょう。
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
  x-type = 2
    nx = 1
・ ・ ・ ・ ・ ・
  z-type = 2
    nz = 1
・ ・ ・ ・ ・ ・
e-type = 2
  ne = 100
$  0.0  1.0e+9
  emin = 0.0
  emax = 300.0
unit = 1
axis = eng
file = track_eng.out
・ ・ ・ ・ ・ ・
lec02.inp
“e-type = 3”とし、eminの値を0MeV以外の値に変更する。
track_eng.eps
対数スケールで見るとどうなるだろうか？
SPEAKER_NOTES:
それでは、課題7に進みます。
ここでは、先ほどの粒子フルエンスのエネルギー分布の横軸を、ログスケールに変更します。
具体的には、e-typeを2から3に変更してください。
続いて、ログスケールで出力する場合、タリーするエネルギー範囲として0は使えないため、eminの値を0MeV以外の値に変更してください。
編集が終わったら、入力ファイルを保存してPHITSを実行してください。
そして、計算が終わったら、track_eng.epsを開いて結果を確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-8.inp

--- SLIDE 38 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
解答7
低エネルギーまではっきりと確認できるようになった
[ T - T r a c k ]
・ ・ ・ ・ ・ ・
  x-type = 2
    nx = 1
・ ・ ・ ・ ・ ・
  z-type = 2
    nz = 1
・ ・ ・ ・ ・ ・
e-type = 3
  ne = 100
$  0.0  1.0e+9
  emin = 1.0
  emax = 300.0
unit = 1
axis = eng
file = track_eng.out
・ ・ ・ ・ ・ ・
lec02.inp
track_eng.eps
SPEAKER_NOTES:
課題7の答え合わせです。
入力ファイルの変更箇所としては、e-typeを2から3に変更します。
また、eminをゼロ以外の値、ここでは1MeVに変更します。
e-typeを3としたことにより、track_eng.epsの図は、右に示すように横軸がログスケールに変わりました。
ログスケールでプロットすることで、粒子フルエンスを低エネルギーまではっきりと確認できるようになりました。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-8.inp

--- SLIDE 39 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
課題8
領域別（円柱の内側と外側）のエネルギー分布をタリーしましょう。
メッシュ型をxyzメッシュからregメッシュに変更する（mesh = reg）。
regパラメータを追加し、領域番号を与えることでタリー領域を指定する（reg = 領域番号をスペース区切りで列挙）
領域番号は、円柱の内側が1,円柱の外側が100。
mesh = xyzのサブセクションを削除もしくはコメントアウトする。
[ T - T r a c k ]
mesh = xyz

  x-type = 2
    nx = 1
    xmin = -25.
    xmax =  25.
  y-type = 1
    ny = 1
    -5.0  5.0
  z-type = 2
    nz = 1
    zmin = -20.
    zmax =  80.
・ ・ ・ ・ ・ ・
lec02.inp
削除
or
コメント
アウト
パラメータ追加
SPEAKER_NOTES:
それでは、課題8に進みます。
先ほどまでは、形状メッシュをxyzとして、1つの立方体の内側をタリーの対象としていましたが、ここでは、領域別、すなわち円柱の内側と外側についいて、粒子フルエンスのエネルギー分布をタリーします。
具体的には、まず形状メッシュをxyzメッシュからregメッシュに変更します。
次に、regメッシュで必要となるregパラメータを追加します。
regに領域番号を与えることで、タリー領域を指定することができます。
このとき、複数の領域番号を指定するときは、それぞれの番号の間をスペースで区切ります。
今回の体系では、領域番号は、円柱の内側が1、円柱の外側が100です。
さらに、形状メッシュの変更に伴い、x-type, y-type, z-typeサブセクションは必要なくなりますので、削除またはコメントアウトします。
編集が終わったら、入力ファイルを保存してPHITSを実行してください。
そして、計算が終わったら、track_eng.epsを開いて結果を確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-9.inp

--- SLIDE 40 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
解答8
1st page
(reg = 1: 水)
2nd page
(reg = 100: 真空)
[ T - T r a c k ]
mesh = reg
  reg = 1 100
$  x-type = 2
$    nx = 1
$    xmin = -25.
$    xmax =  25.
$  y-type = 1
$    ny = 1
$    -5.0  5.0
$  z-type = 2
$    nz = 1
$    zmin = -20.
$    zmax =  80.
・ ・ ・ ・ ・ ・
lec02.inp
track_eng.eps
12Cイオンが水中に入る
前に飛んだ距離に相当
SPEAKER_NOTES:
課題8の解答です。
入力ファイルの変更箇所としては、meshをxyzからregに変更します。
形状メッシュをregとしたので、regパラメータを追加する必要があります。
その値は、円柱の内側である1と、円柱の外側である100を設定します。
一方、形状メッシュがxyzのときに必要となったサブセクションは、全てコメントアウトします。
以上の変更により、track_eng.epsには、右に示す図のように、円柱の内側、すなわち水中と、円柱の外側、すなわち真空における、炭素イオン、陽子、中性子の粒子フルエンスのエネルギー分布が出力されます。
この結果を見ると、真空中の炭素イオンの粒子フルエンスは250MeV/nにだけ現れています。
このときの縦軸の値は、炭素イオンが水中に入る前に飛んだ距離に相当します。
これは、線源から水標的に到達するまでのものが検出されたものです。
また、陽子は水中で減速するため真空中ではあまり検出されていない一方、中性子は真空中でも多く検出されていることがわかります。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-9.inp

--- SLIDE 41 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
課題9
初期設定では、各粒子（part）に対する結果が同じページに出力されます
別のパラメータ（reg, x, y, z, r, engなど）のデータを同じページに表示したい場合はsamepageパラメータを指定します
異なる領域のデータを同じページに表示しよう
[ T - T r a c k ]
mesh = reg
  reg = 1 100
samepage = reg
・ ・ ・ ・ ・ ・
lec02.inp
track_eng.eps
1ページ目 (part = 12C)
2ページ目 (part = proton)
3ページ目 (part = neutron)
SPEAKER_NOTES:
それでは、課題9に進みます。
この課題では、異なる領域のタリー結果を同じページに表示することを目標とします。
デフォルトの設定では、それぞれの粒子に対するタリー結果が同じページに出力されます。
別のパラメータのタリー結果を同じページに表示したい場合は、タリーセクションにsamepageパラメータを用いて指定します。
ここでは、[T-Track]セクションにsamepageパラメータを追加して、そこにregを指定してください。
下に示す図は、samepageパラメータをregに設定した結果です。
1ページ目が炭素イオン、2ページ目が陽子、3ページ目が中性子の粒子フルエンスで、円柱の内側と外側に関するタリー結果が同じ図に表示されるようになりました。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-10.inp

--- SLIDE 42 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
課題10
ファイル”t-deposit.inp”の[T-Deposit]セクションをコピー*、lec02.inpに貼り付ける*

lec02.inpをインプットファイルとして、PHITSを実行する。
[ T - D e p o s i t ]
title = Energy deposition in xyz mesh
mesh = xyz
・ ・ ・ ・ ・ ・
unit = 1
material = all
output = dose
axis = xz
file = deposit.out
part = all
gshow = 3
epsout = 1
t-deposit.inp
[T-Deposit]は、指定した空間（物質）に対して付与されたエネルギーを計算するタリー。
[T-Deposit]を用いて、円柱の水に対する付与エネルギー量（吸収線量）の空間分布を確認しましょう。
*コピーする場所はどこでも良いが、セクションの途中や[end]の後にはコピー不可
SPEAKER_NOTES:
続いて、課題10に進みます。
ここでは、[T-Deposit]を用いて、円柱の水に対する付与エネルギー量の空間分布を観察することを目標とします。
具体的には、まず、lec02フォルダにあるt-deposit.inpファイルを開いてください。
この入力ファイルの中に、[T-Deposit]セクションがあるかと思います。
これをコピーして、lec02.inpに貼り付けてください。
貼り付ける場所は、各セクションの途中や[End]セクションの後でなければどこでも大丈夫です。
ここでは、分かりやすくするために、[End]セクションの直前に貼り付けてください。
編集が終わったら、入力ファイルを保存してPHITSを実行してください。
そして、計算が終わったら、deposit.epsを開いて結果を確認してください。
MENTIONED_INPUT_NAMES: t-deposit.inp
ANSWER_FILE: input/lec02-11.inp

--- SLIDE 43 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
解答10
deposit.eps
炭素ビームよるエネルギー付与
核反応により発生した陽子や中性子などの2次粒子によるエネルギー付与
SPEAKER_NOTES:
課題10の解答です。
deposit.epsを開くと、スライドに示す図が表示されます。
水の円柱の左側の中央部には、線源から入射する炭素イオンによるエネルギー付与の高い領域が確認されます。
また、そのほかの領域にも、核反応によって発生した陽子や中性子などの二次粒子によるエネルギー付与が確認できます。
ANSWER_FILE: input/lec02-11.inp

--- SLIDE 44 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Tallyの使い方
どの空間（面）における、どの粒子の、どういった物理量を、どういう形式で、見たいかを指定する。
空間（面）：メッシュ(mesh =)を用いて定義する。
粒子：粒子名(part =)を指定する。
物理量：単位(unit =)を選ぶ。
形式：出力データの横軸(axis =)を決める。
  （空間のX,Y,Z 座標(x,y,z)、エネルギー(eng)、時間(t)に
   応じたメッシュ定義文が必要）
SPEAKER_NOTES:
それでは、続いて、タリーで出力するデータの物理量を指定する方法を学びます。

--- SLIDE 45 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
課題11
エネルギーが付与される物質の密度からGy=J/kgを計算して出力する。
単位中の /source の概念は基礎実習IIIで詳しく学習します。
[T-Deposit]で出力される量の単位を[MeV/cm3/source]から[Gy/source]に変更しましょう。
[ T - D e p o s i t ]
・ ・ ・ ・ ・ ・
unit = 1
material = all
output = dose
axis = xz
file = deposit.out
part = all
gshow = 3
epsout = 1
lec02.inp
[T-Deposit]セクションにある“unit”を1から0に変える。
SPEAKER_NOTES:
それでは、課題11に進みます。
ここでは、[T-Deposit]で出力される量の単位を、(MeV/cm3/source)から、(Gy/source)に変更します。
具体的には、unitを1から0に変更してください。
そうすると、エネルギーが付与される物質の密度から、Gy、すなわち(J/kg)が自動で計算されて出力されるようになります。
なお、ここで挙げた単位中の、(/source)の概念は、基礎実習の3番で詳しく学習します。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-12.inp

--- SLIDE 46 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
解答11
deposit.eps
[ T - D e p o s i t ]
・ ・ ・ ・ ・ ・
unit = 0
material = all
output = dose
axis = xz
file = deposit.out
part = all
gshow = 3
epsout = 1
lec02.inp
単位と数値のスケールが変わっている。
SPEAKER_NOTES:
課題11の解答です。
unitを1から0に変更してPHITSを実行してdeposit.epsを確認すると、表示される図は、unitの値を変更する前と全く同じように見えます。
ここで、図の右に示されているカラーバーをよく見ると、単位が(Gy/source)となっており、また数値のスケールも変わっていることが確認できます。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-12.inp

--- SLIDE 47 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 12
SLIDE_TEXT:
課題12
[T-Deposit]のメッシュ型をxyzメッシュからr-zメッシュに変更して、水部分における付与エネルギーの深さ分布を出力しましょう。
[ T - Deposit ]
・ ・ ・ ・ ・ ・
mesh = xyz
  x-type = 2
    nx = 100
    xmin = -25.
    xmax =  25.
  y-type = 1
    ny = 1
    -5.0  5.0
  z-type = 2
    nz = 200
    zmin = -20.
    zmax =  80.
・ ・ ・ ・ ・ ・
axis = xz
file = deposit.out
・ ・ ・ ・ ・ ・
lec02.inp
削除
or
コメント
アウト
r-typeに
変更
メッシュ型をxyzメッシュからr-zメッシュに変更する。（mesh = r-z）

x-typeサブセクションを削除もしくはコメントアウトする。

y-typeサブセクションをr-typeサブセクションに変更し、0~10cmまでを1群とするようにパラメータを定義する。

axisをxzからzに変更する。
r-zメッシュで深さ方向(z方向）の分布を調べる。
SPEAKER_NOTES:
それでは、課題12に進みます。
ここでは、[T-Deposit]セクションの形状メッシュをxyzメッシュからr-zメッシュに変更して、水部分における付与エネルギーの深さ分布を出力します。
具体的には、まず形状メッシュをxyzメッシュからr-zメッシュに変更します。
次に、r-zメッシュでは必要ないx-typeサブセクションを削除またはコメントアウトします。
y-typeサブセクションも必要ないのですが、ここでは、yの文字をrに変更して、再利用します。
そして、r方向について、0cmから10cmまでをタリー範囲とし、群数は1となるように、各種パラメータを設定してください。
最後に、axisをxzからzに変更してください。
編集が終わったら、入力ファイルを保存してPHITSを実行してください。
そして、計算が終わったら、deposit.epsを開いて結果を確認してください。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-13.inp

--- SLIDE 48 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 12
SLIDE_TEXT:
解答12
炭素ビームのブラッグピークがz = 12 cmの辺りで見える。
[ T - Deposit ]
・ ・ ・ ・ ・ ・
mesh = r-z
$  x-type = 2
$    nx = 100
$    xmin = -25.
$    xmax =  25.
  r-type = 1
    nr = 1
    0.0  10.0
  z-type = 2
    nz = 200
    zmin = -20.
    zmax =  80.
・ ・ ・ ・ ・ ・
axis = z
file = deposit.out
・ ・ ・ ・ ・ ・
lec02.inp
deposit.eps
SPEAKER_NOTES:
課題12の解答です。
入力ファイルの変更箇所としては、meshをxyzからr-zに変更します。
形状メッシュをr-zとしたので、xyzメッシュの時に必要だったx-typeサブセクションはコメントアウトします。
次に、y-typeサブセクションの各種パラメータのyという文字をrに置き換えて、r-typeサブセクションとします。
r方向のメッシュの群数は既に1ですので変更する必要はなく、0cmから10cmをタリー範囲とするために、分点の数値を0.0と10.0と設定します。
最後に、axisをxzからzに変更します。
以上の変更により、deposit.epsには、右に示す図のように、深さ方向に関するエネルギー付与量の分布が出力されます。
この結果を見ると、炭素ビームのブラッグピークが、z=12cmの辺りで確認できます。
また、12cmよりも深い領域では、二次粒子によるエネルギー付与が確認できます。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-13.inp

--- SLIDE 49 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
実習内容
Tallyとは何か
Tallyの使い方
ジオメトリの確認
物理量の導出
Tally結果描画ソフトウェア
各Tallyの紹介
まとめ
SPEAKER_NOTES:
それでは、ここで、タリー結果を描画するソフトウェアをいくつか紹介します。

--- SLIDE 50 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
グラフ作成ソフトANGEL
ANGELとは？
PHITSのタリー出力をテキスト形式（*.out）から画像形式（*.eps）に変換するプログラム
タリー中にepsout=1と指定することにより，PHITS計算と連動して実行する。
タリー中にangelパラメータを書き込むことにより，軸の調整などができる。          （angelパラメータについてはANGELのマニュアルを参照）
angelパラメータは、テキスト形式のタリー出力ファイルに直接書き込むことも可能
書き変えたタリー出力ファイルを「右クリック→送る→ANGEL」（Windows）もしくは    「ANGELアイコンにドラッグ＆ドロップ」（Mac）することにより，ANGEL単体で動かすことができる。（グラフの再描画のためにPHITSそのものを再実行する必要はない。）
例えば、deposit.outに
p: ymin(1e-11) ymax(1e-9)
を加えANGELを実行
縦軸の範囲を変更
SPEAKER_NOTES:
はじめに、グラフ作成ソフトのANGELについて紹介します。
ANGELとは、PHITSのタリー出力をテキスト形式から画像形式に変換するプログラムです。
入力ファイルのタリーセクションの中で、epsoutというパラメータの値を1に設定することで、PHITS計算と連動して実行され、自動的にepsファイルが出力されます。
また、タリーセクションの中にangelパラメータを書き込むことで、軸の調整などができます。
angelパラメータの詳細については、ANGELのマニュアルをご参照ください。
angelパラメータは、テキスト形式のタリー出力ファイルを編集して直接書き込むことも可能です。
タリー出力ファイルを書き換えてepsファイルに出力される図を変更する場合、Windows環境であれば、タリー出力ファイルを右クリックで選択し、項目の中から送るを選び、そこからANGELを選択してください。
Mac環境であれば、ドックにあるANGELアイコンに、タリー出力ファイルをドラッグアンドドロップしてください。
これによって、ANGELが単体で起動し、図が再描画されます。
すなわち、グラフの再描画のためにPHITSそのものを再実行する必要はありません。
スライドの下側に、例を示します。
先ほど得られたdeposit.outに、こちらに示す1行を加えて、ANGELを実行すると、右側に示す図のように縦軸の範囲が変更され、ブラッグ曲線だけが図示されるようになりました。
このように、着目する事象に応じて、図の描画範囲を変更すると便利です。

--- SLIDE 51 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
PHIG-3Dを用いたタリー結果の描画
読み込むファイルは画像ファイル(*.eps)ではなくテキストファイル(*.out)
画像上の数値データを読み取ることが可能
xyzメッシュ形式のタリー結果
[t-4dtrack]で出力した4次元(x,y,z,t）飛跡情報
動画を作成することが可能
大量のヒストリに対するデータを読み込むとメモリ不足のエラーが起きるので注意
[t-4dtrack]の結果をPHIG-3Dで描画した例
SPEAKER_NOTES:
次に、PHIG-3Dを用いたタリー結果の描画について紹介します。
PHIG-3Dでは、xyzメッシュ形式のタリー結果の描画と、[T-4DTrack]で出力した4次元の飛跡情報の描画が可能です。
xyzメッシュ形式のタリー結果の描画の場合は、テキストファイルを読み込みます。
また、PHIG-3D上で描画したタリー結果の数値データを読み取ることも可能です。
4次元の飛跡情報の描画では、右に示すような動画を作成することが可能です。
ただし、大量のヒストリーに対するデータを読み込むと、メモリ不足のエラーが起きるためご注意ください。

--- SLIDE 52 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 13
SLIDE_TEXT:
課題13
PHIG-3Dを用いて飛跡を４次元(x,y,z,t)で描画しよう
[ T - 4 D t r a c k ] off
     file = 4Dtrack.out
  HistoryMax = 20
lec02.inp
削除
lec02.inpの最後にある[T-4Dtrack]を有効にしてPHITSで実行
lec02.inpをPHIG-3Dで開く
描画ボタンを押して体系を描画し、円柱を右クリックして「不透明度」を下げる
左のタブにあるParticle tracksをクリック
「開く」ボタンを押して4dtrack.outを選択
tend (ns)を4に変更
フレーム数を10もしくはそれ以上に増やして再生ボタン「 」を押す
これらのパラメータを変更
飛跡を出力する最大ヒストリー数
（大きすぎるとメモリ不足になるので注意）
PHIG-3D
SPEAKER_NOTES:
それでは、PHIG-3Dを用いた4次元の飛跡情報の描画方法について、課題13を通して説明します。
はじめに、lec02.inpの[T-4DTrack]セクションの右側にあるoffの文字を削除し、PHITSを実行してください。
[T-4DTrack]セクションのHistoryMaxパラメータで、飛跡を出力する最大ヒストリー数を設定できるのですが、この値が大きすぎるとメモリ不足になるためご注意ください。
PHITSの計算が終了したら、次はlec02.inpをPHIG-3Dで開いてください。
PHIG-3Dが立ち上がりましたら、まずはウィンドウ左下にある描画ボタンを押して円柱を描画してください。
次に、体系が描画されている画面で円柱を右クリックし、出てきたコンテキストメニューの下にある不透明度のスライダーを動かし、円柱を半透明にしてください。
続いて、PHIG-3Dのウィンドウ左のタブリストのうち、Particle tracksをクリックしてください。
Particle tracksタブのメニューが展開されるので、メニュー上部にある、開くボタンを押してください。
ファイルの選択ウィンドウが表示されたら、そこで4dtrack.outを選択し、開くことで、粒子の飛跡が描画されます。
粒子の種類と画面上の線の色の対応はParticle tracksタブのメニューに表示されます。
Particle tracksタブのメニュー下部にある、t endを4に設定し、フレーム数を増やすことで、飛跡を描画する粒子の時刻を区切ることができます。
その下の再生ボタンを押すことで、飛跡の時間変化をアニメーション表示することができます。
MENTIONED_INPUT_NAMES: lec02.inp
ANSWER_FILE: input/lec02-end.inp

--- SLIDE 53 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
解答13
動画保存ボタン
SPEAKER_NOTES:
こちらは4次元の飛跡情報を描画した一例です。
なお、再生ボタンの左側にある赤い丸を押すことで、アニメーションを動画形式で保存することも可能です。

--- SLIDE 54 ---
PPTX_FILE: phits-lec02-en.pptx
EXERCISE_NO: 14
SLIDE_TEXT:
課題14
PHIG-3Dを用いてxyzメッシュタリー結果を描画しよう
①“xyz-mesh Tally”タブを選択 → ②“選択”ボタンを押して”track_xz.out”を選択 →
③断面ボタンを押す → ④”y”のチェックボックスをON →
⑤“描画”ボタンを押す → ⑥タリー名を変更して陽子や中性子の空間分布を描画
①
②
③
④
⑤
⑥
*track_xz.outがなかったり読み込みに失敗する場合はinput/lec02-6.inpをPHITSで実行
SPEAKER_NOTES:
続いて、PHIG-3Dを用いたxyzメッシュ形式のタリー結果の描画方法について、課題14を通して説明します。
はじめに、先ほどの課題から続けて取り組まれている方は、PHIG-3Dのウィンドウの上部メニューの左にあるファイルタブを選択し、そこから再読込をクリックしてください。
もしPHIG-3Dを閉じている場合は、もう一度lec02.inpをPHIG-3Dで開いてください。
PHIG-3Dが立ち上がりましたら、ウィンドウ左下にある描画ボタンを押して円柱を描画してください。
PHIG-3Dのウィンドウ左のタブリストのうち、xyz-mesh Tallyをクリックしてください。
xyz-mesh Tallyタブのメニューが展開されるので、メニュー上部にある、選択ボタンを押してください。
ファイルの選択ウィンドウが表示されたら、そこでtrack_xz.outを選択してファイルを開いてください。
次に、PHIG-3Dのウィンドウ下にあるボタンのうち、断面ボタンを押してください。
球を半分に切断したようなアイコンで、アイコン上にマウスカーソルをホバーした際に、表示中のセルをカット、と表示されるものが断面ボタンです。
断面ボタンを押すと、ダイアログウィンドウが現れますので、その中のうち、yのチェックボックスにチェックを入れてください。
そして、下にあるOKボタンを押してダイアログウィンドウを閉じると、体系が描画されている画面に円柱の断面が、タリー結果と共に現れます。
画面に表示されているのは、これまでの課題で得られたタリー結果のうち、炭素イオンの粒子フルエンスです。
左のxyz-mesh Tallyタブのタリー名のプルダウンメニューから、別のタリー名を選択して左下の描画ボタンを押すことで、画面に表示されるタリー結果を変更することができます。
ANSWER_FILE: input/lec02-end.inp

--- SLIDE 55 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
汎用の3次元可視化目的に使えるフリーソフト
mesh = xyzのタリー結果を３次元的に可視化できる
各タリーセクション内にvtkout = 1と書くことによりParaView用のフォーマットでタリー結果を出力可能
3次元可視化ソフトParaView
ParaView + PHITS sample (lecture\advanced\ParaView)
http://www.paraview.org
SPEAKER_NOTES:
こちらのスライドでは、3次元可視化ソフトウェアの、ParaViewを紹介します。
ParaViewは、汎用の3次元可視化目的に使えるフリーソフトウェアです。
PHITSでは、mesh=xyzのタリー結果を3次元的に可視化するために利用できます。
PHITSの入力ファイルのタリーセクションにて、vtkoutというパラメータの値を1に設定することで、ParaView用のフォーマットでタリー結果が自動的に出力されます。
具体的な利用方法に関しては、講習会資料のうち、advancedフォルダの中のParaViewというフォルダに資料がありますので、興味のある方はこちらをご参照ください。

--- SLIDE 56 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
実習内容
Tallyとは何か
Tallyの使い方
ジオメトリの確認
物理量の導出
Tally結果描画ソフトウェア
各Tallyの紹介
まとめ
SPEAKER_NOTES:
それでは、次のスライドから、PHITSに搭載されているタリーを紹介します。

--- SLIDE 57 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Tallyの種類（ジオメトリの確認）
SPEAKER_NOTES:
PHITSには、ジオメトリを確認するためのタリーが3種類準備されています。
[T-Gshow]と[T-Rshow]は、ジオメトリを2次元で表示するタリーで、[T-3Dshow]は3次元で表示するタリーです。

--- SLIDE 58 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
仮想空間に定義したジオメトリの境界線や領域番号、物質番号を表示する。[T-Rshow]では、領域毎に与える値(e.g.,密度)に依存した色付けが可能。
[Parameters]セクションでicntl = 7,9を指定すると、それぞれ輸送計算を行わずに[T-Gshow], [T-Rshow]の出力が可能。
他のタリーにおいてオプション指定も可能。
[T-Gshow], [T-Rshow]
SPEAKER_NOTES:
[T-Gshow]と[T-Rshow]は、仮想空間に定義したジオメトリの境界線や領域番号、物質番号を表示します。
[T-Rshow]では、領域ごとに与える値、例えば密度などに依存した色付けが可能です。
[Parameters]セクションでicntlを7または9と指定すると、それぞれ輸送計算を行わずにジオメトリの出力だけを実行できます。
また、これまでの課題でも利用してきましたが、gshowオプションを設定したmeshがxyzのタリーでも、ジオメトリの表示が可能です。

--- SLIDE 59 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-3Dshow]
仮想空間に定義したジオメトリの3次元パース図を出力する。[Parameters]セクションでicntl = 11を指定した場合のみ利用可能。
PHIG-3Dで代用可能だが、光源と視点がそれぞれ設定できるため陰影がきれいに表示できる
→ プレゼンテーション用のジオメトリ描画などに最適！
SPEAKER_NOTES:
[T-3Dshow]は、仮想空間に定義したジオメトリの3次元パース図を出力します。
[Parameters]セクションでicntlを11と指定した場合だけ実行されます。
またこの時は、粒子輸送計算が行われません。
[T-3Dshow]で出力される図は、光源と視点を設定できるため、陰影がきれいに表示されます。
そのため、プレゼンテーション用のジオメトリ描画などに適しています。

--- SLIDE 60 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-3Dshow]
SPEAKER_NOTES:
こちらのスライドは、[T-3Dshow]における、光源、視点と原点、そしてそのあいだに配置される画面フレームの関係を図示しています。
それぞれの設定パラメータを赤字で示しており、これらのパラメータを適切に設定することで、3次元のジオメトリの図が得られます。
ただし、どのパラメータをどの程度の値にすればよいかを把握するのは難しいため、PHITSを実行して図を確認しながら、パラメータを調整してください。

--- SLIDE 61 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Tallyの種類（物理量の導出）
次ページ
以降で紹介
SPEAKER_NOTES:
続いて、物理量を導出するためのタリーを紹介します。
こちらの表は、PHITSに搭載されている18個のタリーです。
次のスライドからは、主なタリーをいくつか紹介します。

--- SLIDE 62 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Track]
※ 使い方次第（空間を細かく区切ること）で、放射線の飛跡を観測できる。
指定した任意の空間における粒子のフルエンスを求める。
指定した空間中での飛跡長(track length)をカウントしており、その和を空間の体積で割ることによって、単位面積当たりの粒子の流量(1/cm2)を得る。
SPEAKER_NOTES:
はじめに、実習でも利用してきた[T-Track]です。
このタリーは、指定した任意の空間における粒子のフルエンスを求めるときに利用します。
具体的には、指定した空間中での飛跡長をカウントしており、その和を空間の体積で除することで、単位面積当たりの粒子の流量を得ます。
また、空間を細かく区切ることで、放射線の飛跡を観測できます。

--- SLIDE 63 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Cross]
指定した任意の面における粒子のカレントまたはフラックス（正確にはフルエンス）を求める。
粒子が面を通過する度にそのままカウントするものがカレントで、面に対する入射角度に応じた重みを付けて求めたものがフラックス。共に、単位面積あたりの粒子の流量を評価する。
SPEAKER_NOTES:
[T-Cross]は、指定した任意の面における粒子のカレントまたはフラックスを求めるときに利用します。
粒子が面を通過する度に、そのままカウントするものがカレントで、面に対する入射角度に応じた重みをつけて求めるものがフラックスです。
どちらも、単位面積当たりの粒子の流量を評価します。

--- SLIDE 64 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
Kinds of tallies in PHITS
[T-Point]
[T-Track]
同じ条件に対して[T-Point]と[T-Track]で計算した中性子及び光子フルエンス
（utility/tpoint参照）
[T-Point]
指定した点や線分上における中性子及び光子フラックス（正確にはフルエンス）を求める。
[T-Track]がある領域を対象とするのに対し、[T-Point]は点や線など体積を持たない領域に対して計算できる。ただし、核データの利用が必須など、その使用にはいくつかの制限がある。
SPEAKER_NOTES:
[T-Point]は、指定した点や線分上における、中性子及び光子フラックスを求める際に利用します。
[T-Track]が、ある領域を対象とするのに対し、[T-Point]は点や線など、体積を持たない領域に対して計算できます。
ただし、核データの利用が必須など、その使用にはいくつかの制限がありますのでご注意ください。

--- SLIDE 65 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Deposit]
指定した任意の空間における付与エネルギー（熱量）を求める。
基本的には荷電粒子（陽子や電子など）による付与エネルギーを評価する。中性子や光子による付与エネルギーをKerma近似を使って計算することも可能。
[T-Deposit]で計算したBragg曲線
SPEAKER_NOTES:
[T-Deposit]は、指定した任意の空間における付与エネルギーを求めるときに利用します。
基本的には、陽子や電子などの荷電粒子による付与エネルギーを評価しますが、中性子や光子など、電気的に中性な粒子についても、Kerma近似を使って付与エネルギーを計算できます。

--- SLIDE 66 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Deposit2]で計算した、2つの検出器内でのエネルギー付与の相関
[T-Deposit2]
[T-Deposit]を2つの領域において同時に実行し、得られたエネルギー付与の相関を出力する。
dE-E カウンターなどの模擬が可能。
SPEAKER_NOTES:
[T-Deposit2]は、[T-Deposit]を2つの領域において同時に実行し、得られたエネルギー付与の相関を出力します。
dE-E検出器などを模擬することが可能です。

--- SLIDE 67 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
フッ素
酸素
窒素
炭素
ホウ素
ベリリウム
リチウム
ヘリウム
水素
[T-yield], [T-Product]
指定した任意の空間において、原子核反応や原子相互作用を通じて生成される核種を求める。
[T-Yield]では、核図表(nuclear chart)の形式で出力が可能。[T-Product]では、エネルギーや時間に関する分布を評価できる。
[T-Yield]で計算した、原子核反応からの生成各種のチャート図
SPEAKER_NOTES:
[T-Yield]と[T-Product]は、指定した任意の空間において、原子核反応や原子相互作用を通じて生成される粒子を求める際に利用します。
[T-Yield]では、横軸が中性子数、縦軸が原子番号の、核図表の形式で生成核種量を出力することができます。
一方、[T-Product]では、エネルギーや時間に関する分布を評価できます。

--- SLIDE 68 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-DPA]で計算したDPAの深さ分布の例
[T-DPA]
指定した任意の空間における原子あたりのはじき出し数（DPA; Displacement Per Atom）を求める。
DPAは照射領域に存在する全原子数に対するはじき出された原子数の比で、粒子フルエンスとはじき出し断面積の積で計算する。
SPEAKER_NOTES:
[T-DPA]は、指定した任意の空間における原子当たりのはじき出し数、DPAを求める際に利用します。
DPAは、照射領域に存在する全原子数に対する、はじき出された原子数の比で、具体的には、粒子フルエンスとはじき出し断面積の積で計算します。

--- SLIDE 69 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-LET], [T-SED]
指定した任意の空間における飛跡長や線量(dose)をLET(dE/dx)やlineal energy(y), specific energy(z)の関数として出力する。
[T-LET]で計算した、LETに対するDose量の分布
SPEAKER_NOTES:
[T-LET]および[T-SED]は、指定した任意の空間における飛跡長や線量を、LET、lineal energy、specific energyの関数として出力する際に利用します。

--- SLIDE 70 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
[T-Interact]
指定した任意の空間において、原子核反応や原子相互作用が生じた回数を求める。反応数の平均値や、ヒストリー毎の頻度分布を出力することが可能。
[T-Interact]で計算した反応数の頻度分布
SPEAKER_NOTES:
[T-Interact]は、指定した任意の空間において、原子核反応や原子相互作用が生じた回数を求める際に利用します。
反応数の平均値や、ヒストリー毎の頻度分布を出力することが可能です。

--- SLIDE 71 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
詳細はrecommendation/dchain参照
[T-DCHAIN]
DCHAIN用の入力ファイルを作成する。
DCHAINは、核反応により生成された残留核（[T-Yield]で計算）と20MeV以下の中性子のフルエンス（[T-Track]で計算）を用いて、照射中や照射後の残留放射能の時間変化を計算するプログラム。
150MeV陽子を水ファントムに6分間で5Gy照射したときの残留放射能の時間変化
SPEAKER_NOTES:
[T-DCHAIN]は、DCHAIN用の入力ファイルを作成する際に利用します。
DCHAINとは、核反応により生成された残留核と、20MeV以下の中性子フルエンスを用いて、放射線照射中や照射後の残留放射能の時間変化を計算するプログラムです。

--- SLIDE 72 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
実習内容
Tallyとは何か
Tallyの使い方
ジオメトリの確認
物理量の導出
Tally結果描画ソフトウェア
各Tallyの紹介
まとめ
SPEAKER_NOTES:
それでは、本実習のまとめです。

--- SLIDE 73 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
まとめ
PHITSでは、粒子や放射線の振る舞いを調べるために仮想的な“検出器（タリー）”を使用する。
PHITSには利用できる数多くのタリーが用意されており、大きく分けるとジオメトリの確認と物理量の導出に関するものがある。
各タリーでは，どの空間（面）の、どの粒子に関する、どうような物理量を、どういった形式で、見たいかを指定する必要がある。
各タリーのサンプルはsample/tallyフォルダにあるので，それをコピー&ペーストして各自の計算したい条件に調整する。
SPEAKER_NOTES:
本実習では、粒子輸送シミュレーションから、様々な物理量を導出できるようになることを目標としました。
PHITSでは、粒子や放射線の振る舞いを調べるために、仮想的な検出器、タリーを使用します。
そして、PHITSには数多くのタリーが用意されており、大きく分けると、ジオメトリの確認と、物理量の導出に関するものがあります。
各タリーでは、どの空間の、どの粒子に関する、どのような物理量を、どういった形式で見たいかを指定する必要があります。
なお、各タリーのサンプルはsampleフォルダのタリーフォルダにあるので、そこからタリーセクションをコピーして、各自の入力ファイルに貼り付けたのち、各種パラメータを、目的に応じて調整してください。

--- SLIDE 74 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
宿題
宿題体系の粒子フルエンスを，陽子，中性子ごとに表示するようにする。
[T-Deposit]を調整し，陽子のブラッグピークが見えるようにする。
円柱中心部分（半径2.5cm以内）とその外側で吸収線量-深さ分布の違いを調べる。（r-zメッシュを変更する）
内側と外側の吸収線量を同じページに表示するようにする（samepageパラメータを加える）
SPEAKER_NOTES:
こちらは、基礎実習2の宿題で、基礎実習1の宿題からの続きとなります。
はじめに、宿題体系の粒子フルエンスを、陽子、中性子ごとに表示するようにしてください。
次に、[T-Deposit]を調整して、陽子のブラッグピークが見えるようにしてください。
最後に、円柱中心部とその外側で、吸収線量の深さ分布の違いを確認してください。
その際、円柱の内側と外側の吸収線量を同じページに表示するように、samepageパラメータを設定してください。

--- SLIDE 75 ---
PPTX_FILE: phits-lec02-en.pptx
SLIDE_TEXT:
宿題（解答例）
陽子（上）・中性子（下）フルエンス
円柱中心（黒線）と端側（赤線）における吸収線量の深さ分布
xz_track.eps
deposit.eps
SPEAKER_NOTES:
宿題の回答例を示します。

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/lec02-1.inp

[BONUS_TEXT_FILES]
NOTE: None
