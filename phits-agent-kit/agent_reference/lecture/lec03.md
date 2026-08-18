# Lecture: basic/lec03

SOURCE_FOLDER: D:/NEAgit/lecture/basic/lec03
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: lec03
LECTURE_PATH_INDEX: lecture/basic/lec03
PPTX_FILES: phits-lec03-en.pptx, phits-lec03-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: lec03, onion
SECTION_KEYWORDS: 1, 1-31, 2, 3, 3d-show, 5, 6, 20, 25, character, cm, cm2, cm3, n1-n2, neutron, photon, proton, section, t-3dshow, t-cross, t-deposit, t-track, t-volume, volume, x

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/basic/lec03
LECTURE_PATH_INDEX: lecture/basic/lec03
PPTX_FILES: phits-lec03-en.pptx, phits-lec03-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 2
SLIDE_COUNT: 134
EXERCISE_SLIDE_COUNT: 37
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- lec03.inp
- onion.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Basic Lecture III:
- SLIDE 02: Purpose of This Lecture
- SLIDE 03: Goal of This Lecture
- SLIDE 04: Contents of Lecture III
- SLIDE 05: The mode can be changed by icntl in [parameters] section.
- SLIDE 06: [ T i t l e ]
- SLIDE 07: [ T i t l e ]
- SLIDE 08: [ T i t l e ]
- SLIDE 09: track_xz.eps
- SLIDE 10: Contents of Lecture III
- SLIDE 11: [ T i t l e ]
- SLIDE 12: [ T i t l e ]
- SLIDE 13: Intrinsic functions
- SLIDE 14: lec03.inp
- SLIDE 15: onion.inp
- SLIDE 16: EXERCISE 1 | set: c1[5]
  ANSWER_FILE: input/lec03-2.inp
- SLIDE 17: set: c1[25]
- SLIDE 18: Contents of Lecture III
- SLIDE 19: Volume and Area Calculation
- SLIDE 20: Monte Carlo Integration
- SLIDE 21: Volume calculation by PHITS
- SLIDE 22: EXERCISE 2 | Let’s calculate the volumes of each cell in the onion structure
  ANSWER_FILE: input/lec03-3.inp
- SLIDE 23: EXERCISE 2 | Volumes can be calculated by Monte Carlo integration.
  ANSWER_FILE: input/lec03-3.inp
- SLIDE 24: Contents of Lecture III
- SLIDE 25: maxcas×maxbch ＝total number of histories
- SLIDE 26: History and batch
- SLIDE 27: EXERCISE 3 | lec03.inp
  ANSWER_FILE: input/lec03-4.inp
- SLIDE 28: EXERCISE 3 | [ V o l u m e ]
  ANSWER_FILE: input/lec03-4.inp
- SLIDE 29: [ P a r a m e t e r s ]
- SLIDE 30: Random number used in PHITS is a pseudo-random number* with the period of 264-1(~ 1019)
- SLIDE 31: 440 <--- Number of remaining batches
- SLIDE 32: EXERCISE 4 | lec03.inp
  ANSWER_FILE: input/lec03-5.inp
- SLIDE 33: EXERCISE 5 | [ P a r a m e t e r s ]
  ANSWER_FILE: input/lec03-6.inp
- SLIDE 34: Both shared-memory (OpenMP) and distributed-memory (MPI) parallelization are available in PHITS.
- SLIDE 35: $OMP = 4
- SLIDE 36: Contents of Lecture III
- SLIDE 37: set: c1[25]
- SLIDE 38: Estimate the absolute value of dose in Gy
- SLIDE 39: EXERCISE 6 | Exercise 6
  ANSWER_FILE: input/onion.inp
- SLIDE 40: EXERCISE 6 | Answer 6
  ANSWER_FILE: input/lec03-7.inp
- SLIDE 41: EXERCISE 7 | Exercise 7
  ANSWER_FILE: input/lec03-8.inp
- SLIDE 42: EXERCISE 7 | Answer 7
  ANSWER_FILE: input/lec03-8.inp
- SLIDE 43: Contents of Lecture III
- SLIDE 44: Why cross section data libraries?
- SLIDE 45: Related Parameters
- SLIDE 46: emin(i) & dmax(i)
- SLIDE 47: “file” Parameters
- SLIDE 48: EXERCISE 8 | lec03.inp
  ANSWER_FILE: input/lec03-9.inp
- SLIDE 49: Activate electron and positron transport using EGS5
- SLIDE 50: EXERCISE 9 | lec03.inp
  ANSWER_FILE: input/lec03-10.inp
- SLIDE 51: lec03.inp
- SLIDE 52: Contents of Lecture III
- SLIDE 53: Option for beam transport analysis
- SLIDE 54: Switching Energy
- SLIDE 55: Neutron     Nuclear data         INCL (inclg=1)             JAM
- SLIDE 56: Conventional Mode
- SLIDE 57: Event generator mode is recommended
- SLIDE 58: How to Use EG-Mode
- SLIDE 59: EXERCISE 10 | lec03.inp
  ANSWER_FILE: input/lec03-11.inp
- SLIDE 60: lec03.inp
- SLIDE 61: EXERCISE 11 | [ P a r a m e t e r s ]
  ANSWER_FILE: input/lec03-end.inp
- SLIDE 62: Answer 11
- SLIDE 63: Contents of Lecture III
- SLIDE 64: [Parameters] section is used for controlling PHITS simulation procedure.
- SLIDE 65: EXERCISE 5 | AI Phi-chan (https://x.gd/WAynQ)
  ANSWER_FILE: input/lec03-6.inp
- SLIDE 66: Transport electrons and positrons using  EGS5
- SLIDE 67: Depth-dose distribution inside (up) and outside (down) beam radius
- SLIDE 01: PHITS 講習会 基礎実習（III）:
- SLIDE 02: はじめに
- SLIDE 03: 本実習の目標
- SLIDE 04: 実習内容
- SLIDE 05: 計算モードの選択
- SLIDE 06: [ T i t l e ]
- SLIDE 07: [ T i t l e ]
- SLIDE 08: [ T i t l e ]
- SLIDE 09: 線源の飛跡確認
- SLIDE 10: 実習内容
- SLIDE 11: [ T i t l e ]
- SLIDE 12: [ T i t l e ]
- SLIDE 13: 利用できる関数一覧
- SLIDE 14: lec03.inp
- SLIDE 15: onion.inp
- SLIDE 16: EXERCISE 1 | set: c1[5]
  ANSWER_FILE: input/lec03-2.inp
- SLIDE 17: EXERCISE 1 | set: c1[25]
  ANSWER_FILE: input/lec03-2.inp
- SLIDE 18: 実習内容
- SLIDE 19: 体積、面積計算の必要性
- SLIDE 20: モンテカルロ積分
- SLIDE 21: PHITSによる体積計算の原理
- SLIDE 22: EXERCISE 2 | 課題2
  ANSWER_FILE: input/lec03-3.inp
- SLIDE 23: 体積計算の結果
- SLIDE 24: 実習内容
- SLIDE 25: 試行回数（ヒストリ数）の設定
- SLIDE 26: ヒストリーとバッチの関係
- SLIDE 27: EXERCISE 3 | [ V o l u m e ]
  ANSWER_FILE: input/lec03-4.inp
- SLIDE 28: EXERCISE 3 | [ V o l u m e ]
  ANSWER_FILE: input/lec03-4.inp
- SLIDE 29: lec03.inp
- SLIDE 30: 乱数について
- SLIDE 31: バッチ計算の活用
- SLIDE 32: EXERCISE 4 | [ T i t l e ]
  ANSWER_FILE: input/lec03-5.inp
- SLIDE 33: EXERCISE 5 | [ P a r a m e t e r s ]
  ANSWER_FILE: input/lec03-6.inp
- SLIDE 34: PHITSの並列計算は，メモリ共有型（OpenMP）とメモリ分散型（MPI）があります
- SLIDE 35: EXERCISE 1 | $OMP = 4
  ANSWER_FILE: input/lec03-2.inp
- SLIDE 36: 実習内容
- SLIDE 37: set: c1[25]
- SLIDE 38: 吸収線量を絶対値で評価
- SLIDE 39: EXERCISE 6 | 課題6
  ANSWER_FILE: input/onion.inp
- SLIDE 40: EXERCISE 6 | 課題6の答え合わせ
  ANSWER_FILE: input/lec03-7.inp
- SLIDE 41: EXERCISE 7 | 課題7
  ANSWER_FILE: input/lec03-8.inp
- SLIDE 42: EXERCISE 7 | 課題7の答え合わせ
  ANSWER_FILE: input/lec03-8.inp
- SLIDE 43: 実習内容
- SLIDE 44: 断面積データライブラリとは？
- SLIDE 45: 関連するパラメータ
- SLIDE 46: emin(i)とdmax(i)
- SLIDE 47: 入出力ファイルの設定
- SLIDE 48: EXERCISE 8 | lec03.inp
  ANSWER_FILE: input/lec03-9.inp
- SLIDE 49: EXERCISE 8 | lec03.inp
  ANSWER_FILE: input/lec03-9.inp
- SLIDE 50: EXERCISE 9 | lec03.inp
  ANSWER_FILE: input/lec03-10.inp
- SLIDE 51: EXERCISE 9 | lec03.inp
  ANSWER_FILE: input/lec03-10.inp
- SLIDE 52: 実習内容
- SLIDE 53: 荷電粒子のビームライン設計オプション
- SLIDE 54: 核反応モデルの変更
- SLIDE 55: Neutron     Nuclear data         INCL (inclg=1)             JAM
- SLIDE 56: (n,2n)
- SLIDE 57: EGモードON/OFFの判断材料
- SLIDE 58: EGモードの設定
- SLIDE 59: EXERCISE 10 | lec03.inp
  ANSWER_FILE: input/lec03-11.inp
- SLIDE 60: EXERCISE 10 | lec03.inp
  ANSWER_FILE: input/lec03-11.inp
- SLIDE 61: EXERCISE 11 | [ P a r a m e t e r s ]
  ANSWER_FILE: input/lec03-end.inp
- SLIDE 62: EXERCISE 11 | 課題11の答え合わせ
  ANSWER_FILE: input/lec03-end.inp
- SLIDE 63: 実習内容
- SLIDE 64: まとめ
- SLIDE 65: EXERCISE 5 | AI Phi-chan (https://x.gd/WAynQ)
  ANSWER_FILE: input/lec03-6.inp
- SLIDE 66: 宿題
- SLIDE 67: 宿題（解答例）

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: lec03.inp
FILE: onion.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Basic Lecture III:
Parameter Setting
Jul 2026 revised
phits/lecture/basic/lec03
SPEAKER_NOTES:
Let’s get started, everyone. This is the basic lecture part 3 on parameter settings.

--- SLIDE 02 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Purpose of This Lecture
PHITS simulation is controlled by various parameters defined in [Parameters] section.
Every parameter has its default value, and you do not have to change most of them.
But you have to change some parameters to obtain appropriate results depending on the condition of the particle transport.
You will learn how to setup those parameters in this lecture!
SPEAKER_NOTES:
As explained in the basic lecture 1, geometry, source and tally are the essential elements of PHITS inputs. They were already explained in the basic lecture 1 and 2, which means that you already have learned the basis of PHITS inputs. Then, why do we need lecture 3? Because parameters section is also vital for PHITS input files.
PHITS simulation is controlled by the parameters of the parameters section, which have default values. The default values are good in most of conditions but depending on the calculation conditions, it is advisable to optimize the parameters to get reasonable output.

--- SLIDE 03 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Goal of This Lecture
Proton (up) and neutron (down) fluences calculated by default settings in the homework
You can obtain such results at the end of this lecture
Proton (up) and neutron (down) fluences calculated by appropriate settings in the homework
SPEAKER_NOTES:
For instance, by optimizing the parameters, calculation is improved in this way. Both right and left show the fluence distribution around a water cylinder exposed to a proton beam. The parameters are optimized in the right while they are default in the left. The statistical accuracy of the left, which shows sparse trajectories, is out of question. What we need is result with good accuracy like the plot on the right.

--- SLIDE 04 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Contents of Lecture III
Selection of Calculation Mode
Convenient functions for input
Setting for statistics
Monte Carlo integration
History Number and statistical error
Scaling of tally results
Setting for physics
Nuclear Data Library
Physics Models
Summary
SPEAKER_NOTES:
In this lecture, let’s study how to select the calculation mode, what are convenient functions to write inputs, how to improve statistical accuracy and how to configure physical processes.
Let’s go on to the first content about the calculation mode.

--- SLIDE 05 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
The mode can be changed by icntl in [parameters] section.
Let’s check the geometry using icntl=11 [3D-show] and icntl=8 (gshow option)
Selection of Calculation Mode
SPEAKER_NOTES:
To tell the truth, you have already learned some calculation modes which is specified by the parameter icntl. For example, 0 means normal radiation transport and 8 means 2 dimensional visualization by tallies with gshow option.
In the following slides, let’s try 5, 11 and 14.

--- SLIDE 06 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 11
  maxcas = 100
  maxbch = 10
  file(6) = phits.out

set: c1[20]

[ S o u r c e ]
・ ・ ・ ・ ・ ・

infl: {onion.inp}[1-31]
lec03.inp
[ T - 3 D s h o w ]
  output = 3
material = -1
          6
      x0 =   0
      y0 =   0
      z0 =   0
   e-the =  70  $ eye
   e-phi =  20
   e-dst =  80
   l-the =  20  $ light
   l-phi =   0
   l-dst = 100
   w-wdt =  50  $ window
   w-hgt =  50
   w-dst =  25
  heaven = z
       line = 1
  shadow = 2
    file = 3dshow.out
   title = Check onion structure using [T-3dshow] tally
  epsout = 1
・ ・ ・ ・ ・ ・
3dshow.eps
Activate
[t-3dshow]
[3D-Show] (icntl=11)
Geometry Visualization Mode
Onion structure
PHIG-3D is superior to this function
SPEAKER_NOTES:
Please open the input L E C 03 dot I N P. The first thing to try is icntl 11. Running with icntl 11, PHITS finds T three D show in the input file and generates 3 dimensional plot. As PHIG 3D can create 3D geometry plot, one can create 3D geometry view using this tally instead. Please try running this input with inctl 11 and open its output file named 3d show dot eps.
Fig three D is encouraged if it is available in your computer because Fig three D is superior version of this old function icntl 11.
MENTIONED_INPUT_NAMES: lec03.inp, onion.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 11
  maxcas = 100
  maxbch = 10
  file(6) = phits.out

set: c1[20]

[ S o u r c e ]
・ ・ ・ ・ ・ ・

infl: {onion.inp}[1-31]
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 8
  maxcas = 100
  maxbch = 10
  file(6) = phits.out

set: c1[20]

[ S o u r c e ]
・ ・ ・ ・ ・ ・

infl: {onion.inp}[1-31]
[ T - T r a c k ]
     mesh =  xyz
   x-type =    2
       nx =  100
     xmin =  -50.
     xmax =   50.
   y-type =    1
       ny =    1
           -5.0  5.0
   z-type =    2
       nz =  100
     zmin =  -50.
     zmax =   50.
     part =  proton
   e-type =    1
       ne =    1
            0.  200.
     unit =    1
     axis =   xz
     file = track_xz.out
    title = Check source
    gshow =    3
   epsout =    1
lec03.inp
[T-Track] with gshow = 3 (icntl=8)
Activate gshow option in [t-track]
Check cell ID and filled materials
Track_xz.eps
SPEAKER_NOTES:
When icntl is 8, PHITS finds gshow options in the input file to plot the 2 dimensional view of the geometry cross sections. In this case, by running PHITS with icntl 8, PHITS detects the g show option in t track tally and creates 2 dimensional geometry plot like track X Z dot e p s.
MENTIONED_INPUT_NAMES: lec03.inp, onion.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 5
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
lec03.inp
Change and Execute
[ T - T r a c k ]
    mesh = xyz
  x-type = 2
      nx = 100
    xmin = -50.
    xmax =  50.
  y-type = 1
      ny = 1
          -5.0  5.0
  z-type = 2
      nz = 100
    zmin = -50.
    zmax =  50.
 e-type = 1
      ne = 1
          0.  200.
    unit = 1
    axis = xz
    file = track_xz.out
   title = Check source direction using [T-track] tally
  epsout = 1
Check Sources ([t-track])
SPEAKER_NOTES:
Let’s try icntl 5. What happens ?
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
track_xz.eps
No reaction and no ionization because all regions are assumed void.
（You can confirm positions and directions of sources.）
Check Trajectory of Sources
SPEAKER_NOTES:
Do you see track x z dot e p s file with horizontal stripes in the middle? icntl 5 replaces all the materials with vacuum so all the particles from the source fly straight ahead. This function is useful to check the source setup. Suppose if you get a result showing 0, and you don’t know what is to blame, source, geometry or tally. In that case, please change icntl to 5 to see where source starts and where the source is directed.

--- SLIDE 10 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Contents of Lecture III
Selection of Calculation Mode
Convenient functions for input
Setting for statistics
Monte Carlo integration
History Number and statistical error
Scaling of tally results
Setting for physics
Nuclear Data Library
Physics Models
Summary
SPEAKER_NOTES:
Let’s go on to the functions convenient to write inputs.

--- SLIDE 11 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 5
  maxcas = 100
  maxbch = 10
  file(6) = phits.out

set: c1[5]

[ S o u r c e ]
・ ・ ・ ・ ・ ・

infl: {onion.inp}[1-31]
lec03.inp
[ M a t e r i a l ]
・ ・ ・ ・ ・ ・
[ M a t  N a m e  C o l o r ]
・ ・ ・ ・ ・ ・
[ S u r f a c e ]
  10  so     500.
  11  so       5.
  12  so      10.
  13  so      15.
  14  so      20.
  15  so      25.

[ C e l l ]
 100    -1      10
 101     1 -19.32            -11
 102     2 -1.          11   -12
 103     3 -8.93        12   -13
 104     4 -1.          13   -14
 105     5 -0.9         14   -15
 106     6 -1.20e-3     15   -10
Replace this line by lines 1 to 40 in “onion.inp”
onion.inp
Include File
You can include other files into PHITS input file using “infl” command
Specify file name by {}, and line numbers by [n1-n2]
infl is disregarded if the section including infl is disactivated by “off”
Write a line  file=(input file name) in the first line of input if you run executable directly instead of phits.bat or phits.sh (e.g. MPI cluster)
SPEAKER_NOTES:
For a quick glance, you might think that this l e c 0 3 input file does not have geometry definition. Scrolling the file down from the top, title section, parameters section, and source section are seen. The sections below source are tallies, which means that the sections required to define geometry such as material, surface and cell sections are missing.
But a command infl is found below the source section. This command, include file, tells PHITS to import an external file. The first argument of infl command in the bracket is a file name. The subsequent argument in the square bracket is a line number specification. In this case, a file named onion dot i n p from its top to 33rd line is inserted to this input file. Eventually, material, surface and cell sections in onion dot i n p file are read.
Please note 2 things. First, if the section including infl command is turned off by off command, infl command is also disregarded. Second, when you launch not the shell or batch file but the executable file directly, please don’t forget to write a line to specify the file name at the top of the input. The format is file equal input file name.
MENTIONED_INPUT_NAMES: lec03.inp, onion.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
・ ・ ・ ・ ・ ・

set: c1[5]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 = -30.0
 z1 = -30.0
 dir =  1.0
lec03.inp
You can define your own variables in PHITS input file.
Format: set: ci[x]
i: integer (1~999)
x: variable
“set: ci[x]” is valid starting from the command line till the end of the input, but is ignored in “[section] off"
How to Use Variables
You can use mathematic equations in PHITS input files
Format: FORTRAN syntax
    e.g. exp(-2.0), cos(pi/2), pi*c1**2
(pi is a predefined constant as 3.141592…)
[Intrinsic functions are shown in the next slide.]
That way the source area is linked with tally area etc.
You can automatically execute many PHITS simulations by changing certain parameters using infl & set (see phits/utility/script)
SPEAKER_NOTES:
There are three more functions to learn, they are user-defined variables, mathematical expressions and user-defined characters.
In the source section, another strange thing can be seen. Can you see a line, x zero equal c one? Here, c one is what we call a user-defined variable. The line, set colon c one bracket 5, means that a user-defined variable c one is treated as 5 hereafter. So all c ones in the source section are replaced by 5.
In this way, you can define your own variables to use them later. Users can define 99 user-defined variables from c 1 to c 99 and use them wherever below the definition. If you define c one at one place as 10 and redefine it somewhere below as 20, c one is 10 at first and c one becomes 20 below the redefinition. By reusing the variables in this way, you can effectively use more than 99 variables.
If the section is turned off, the variable definitions in the sections are also skipped, in the same way as infl commands.

The other thing to explain in this slide is use of mathematical expressions. In PHITS input files, users can use mathematical formulae written in FORTRAN format. For example, P I in inputs is pie by default. In fortran double asterisk means power. In addition, most of mathematical functions can be used. By combining these, one can define cosine pie over 2, for instance.
Moreover, by combining infl commands and user defined variables, you can launch shell scripts which sweep the input parameters such as energy or shielding thickness continuously and get results as a function of the input parameter.
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Intrinsic functions
SPEAKER_NOTES:
This is a list of functions which you can use in PHITS inputs. Functions such as trigonometric functions, their inverse, hyperbolic functions, exponential, logarithmic, square root can be used.

--- SLIDE 14 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
lec03.inp
Character variable can be set as
  set:%Variable_Name%[character]
LARGE and small characters are distinguished (Case Sensitive!)
User-defined character
Character variable is available from version 3.31
Rewrite (rwt) file
Input data after converting the character variables are generated in a rewrite-file named *_rwt.inp
By adding “$RWT=0” before the 1st section, generation of *_rwt.inp file is stopped. This speeds up PHITS initialization if your input file is large, at the price of user-defined character feature.
You can generate *_rwt.inp without performing particle transport simulation by adding “$RWT=3”
[ Source ]
set:%projectile%[proton]
  totfact =   1.0
   s-type =   2
      proj =  %projectile%
…

[ T-Track ]
…
part =  %projectile%
…
Correlate proj in [source] and part in [t-track] using a character variable %projectile%
SPEAKER_NOTES:
From version 3.31, character variables can be used in input files in a way similar to the user-defined variables. In this input file, a user-defined character is used for representing the name of the incident particle, i.e., the projectile. By defining it as set percent projectile percent proton, the type of incident particle and the type of particle tallied in [t-track] can always be kept consistent.
When user-defined characters are defined, PHITS internally converts them to the actual strings and dumps this temporary input file to an external file named original file name underscore R W T dot I N P. By adding a line dollar R W T equals zero before the first section, PHITS initialization time is shortened by skipping this file generation. However, this configuration, dollar R W T equals zero means that you cannot use user-defined characters.
If you would like to use the same input containing user defined characters without initialization time overhead, define dollar R W T equals three. PHITS stops immediately after generating a converted file. You can use this file whose user defined characters are already converted.
MENTIONED_INPUT_NAMES: _rwt.inp, lec03.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
onion.inp
Defining @material_name@ in [material] automatically sets its mass density
In subsequent lines, %material_name% can be used as the material number

Since the density of predefined materials is defined as mass density, you can always set the density to 0 in [cell]
List of predefined materials is available in data/predefined_material.dat
Each material has many registered names (aliases), selectable via auto completion
Predefined materials
available from version 3.37
[ Material ]
mat[1]  @GOLD@
mat[2]  @WATER@
mat[3]  @COPPER@
mat[5]  @POLYETHYLENE(0.94)@
mat[6]  @AIR_DRY@
…
 [ Cell ]
 100  -1       10
 101  %GOLD% 0   -11
 102  %WATER% 0   11   -12
 103  %COPPER% 0  12   -13
 104  %WATER%  0  13   -14
 105  %POLYETHYLENE(0.94)% 0 14 -15
 106  %AIR_DRY% 0 15   -10
Looking up the composition and density of materials is troublesome…
Hard to tell which material is assigned to each region in [cell]…
Hard to remember material numbers when defining cells…
e.g.: mat[1] @GOLD@
mat[1] au -19.32
set:%GOLD%[1]
Replace
Thermal scattering law and stopping-power data are also assigned for some materials
SPEAKER_NOTES:
As an application of this user-defined character variable feature, predefined materials have become available from Version 3.37, in response to user requests such as: looking up the composition and density of materials is troublesome; it is hard to tell which material is assigned to each region in the cell section; and it is hard to remember the material numbers when defining cells
With this feature, just by defining at material name at in the material section, the mass density of the material is automatically defined, and the character variable percent material name percent can be used as a material number in the subsequent lines. For example, if you define mat[1] at gold at, it is replaced as shown here. Since the density of predefined materials is defined as mass density, you can always set the density to 0 in the cell section. List of predefined materials is available in data/predefined_material.dat file, where various material names (aliases) are registered for each material, and they can be selected via the auto completion function of editors such as PHITS Pad or Notepad++.
MENTIONED_INPUT_NAMES: onion.inp

--- SLIDE 16 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
set: c1[5]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 =  -30.0
 z1 =  -30.0
 dir =  1.0
Increase the beam width so that the beam covers the whole onion structure.
Increase the beam size so that the beam covers the entire sphere with a radius of 25 cm.
Increase the variable c1
lec03.inp
rectangular
(s-type=2)
track_xz.eps
Source particles travelling along the z-axis are generated from a 10 x 10 cm2 square on the xy-plane
Exercise 1
SPEAKER_NOTES:
Let’s go on to an exercise. The exercise number one is about the setting of user-defined variables. As we learned, the input file of lec 0 3 includes an onion-like geometry definitions of a five-layered sphere whose radius is 25 centimeters. The beam is square shaped source defined by s type 2 which covers only 5 cm in plus and minus directions. So, the goal of this exercise is to cover the entire onion of 25-centimeter radius with the beam by changing the user defined variable c1.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-2.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
set: c1[25]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 =  -30.0
 z1 =  -30.0
 dir =  1.0
lec03.inp
track_xz.eps
The beam generated from a 50 x 50 cm2 square can cover the whole onion structure.
Answer 1
Extend the beam width so that the beam hits the whole of the onion structure.
rectangular
(s-type=2)
SPEAKER_NOTES:
This is the answer of exercise one. Above the source section, in the line where c one is set, please change 5 to 25. As c one is overwritten by 25 hereafter, the beam covers X and Y both from minus 25 to plus 25. Eventually, the beam having 50 cm of vertical and horizontal width covers the whole onion.
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Contents of Lecture III
Selection of Calculation Mode
Convenient functions for input
Setting for statistics
Monte Carlo integration
History Number and statistical error
Scaling of tally results
Setting for physics
Nuclear Data Library
Physics Models
Summary
SPEAKER_NOTES:
Let’s go on to the next subject, how to improve the statistical accuracy.

--- SLIDE 19 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Volume and Area Calculation
When you set mesh=reg in tallies, you have to calculate volumes and surface areas of cells in advance*.
＊You can set the volumes in [volume] section and the surface areas in ”area” column of [t-cross] section.
How much is the deposit energy per unit volume in the specified cell?
How much is the particle fluence per unit area in the specified cell?
When a cell is a simple object such as spheres and cylinders, you can analytically calculate its volume and surface area.
	However, for complex objects?
	→ Monte Carlo integration by PHITS!
SPEAKER_NOTES:
To discuss statistical accuracy, let’s take volume and surface calculation as an example.
In case of X Y Z mesh, mesh unit is cubic therefore one can easily calculate its volume and surface. These values are necessary to calculate energy deposition per volume or particle fluence per area. However, when it comes to region mesh, which might be a combination of spheres and cubes, their volumes are not always obvious.
PHITS has a function to calculate the volumes of geometry elements in an automated way based on Monte-Carlo integration.

--- SLIDE 20 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Monte Carlo Integration
a cm
a cm
Set a target of a 1 x 1 cm2 square, and then mark points on it randomly.  If the point is inside the colored region, add +1 to the score.

Increasing the trial number, the total score divided by the trial number approaches to the ratio of the colored region to the total area (1/2 for the left case).
By multiplying its result by a area of the target (a2) you can obtain the area of the colored region approximately.
You can apply this method to any shape.
Furthermore, you can apply the same idea to 3D to estimate the volume of a specified region.
Monte Carlo Integration is a numerical method to obtain an approximate solution of definite integrals using random numbers. This method estimates the solution approximately by counting the number of points inside a cell after marking random points on a target. Its statistical error depends on the history number.
Please watch the PHITS promotional video: https://youtu.be/9_bs6g0n3Hg
SPEAKER_NOTES:
Have you ever heard of a method called Monte-Carlo integration? It is a numerical method to calculate definite integrals such as surface areas and volumes using random numbers. Suppose there is a target plane and the area of interest is inside the target plane. Hitting the target plane at random and judging if the hit position is inside the area of interest or not, one can calculate the integral with statistical fluctuation.
Suppose there is a square target whose side is A cm long and half of it is painted. Think of hitting lots of points inside square at random and count up when painted part is hit.
Looking at the picture in this slide, number of points in the painted region and total number of points are 8 and 14, respectively. Then multiplying the area of square, A to the power of 2, and the ratio, 8 over 14, you can calculate the area of painted area as 8 times A square over 14. This value is close to the right answer, which is A square over 2.
This case is very much straight forward because the target is square and the region of interest is triangle. But this method can be applied to arbitrary geometry, no matter how it is complicated. On top of that, this method can be extended to 3 dimension to calculate volumes.

--- SLIDE 21 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Volume calculation by PHITS
PHITS can estimate an approximate value of the volume of each cell by using [t-volume] tally
Target
Source area
Set a condition that an area of the target is equal to that of the source region.
Volume of a cell [cm3]
Total track length [cm]
Density of lines [/cm2]
Total track length [cm]
History number / source area [cm2]
＝
＝
SPEAKER_NOTES:
PHITS has a built-in function called T volume tally which calculates volumes of cells in the geometry. The procedure to hit points and count them up is automated and done internally. To be more precise, the whole target is uniformly exposed to virtual radiation which penetrates everything without being scattered or slowed down. Then the radiation travels inside the region of interest, the length of trajectory is tallied by an internal function equivalent to T track tally.

--- SLIDE 22 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Let’s calculate the volumes of each cell in the onion structure
Set icntl = 14 (volume calculation mode)
Execute PHITS
Open “volume.out” by a text editor
Check the calculated volumes of each cell
lec03.inp
What are the volumes of these cells?
Exercise 2
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
…

[ T - V o l u m e ]
     mesh =  reg
     reg = 101 102 103 104 105
     file = volume.out
     s-type =    2
     x0 = -c1
     x1 =  c1
     y0 = -c1
     y1 =  c1
     z0 = -c1
     z1 =  c1
Monte Carlo
integration range
→ Rectangular
     source area
SPEAKER_NOTES:
Let’s try T volume tally. The aim of this exercise is to calculate the volumes of onion layers. Please run PHITS after changing icntl to 14. Then PHITS runs in 14th mode, in which only t volume tally is activated. T volume tally projects virtual radiation from the cubic surface ranging from minus c1 centimeters to plus c1 centimeters. After running this input, please open volume dot out file, which is the output of t volume tally, to see what the volumes of these cells are.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-3.inp

--- SLIDE 23 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Volumes can be calculated by Monte Carlo integration.
volume.out
Volume of each cell is…
4π(5)3/3=524 cm3
4π(10)3/3 - 524=3665 cm3
4π(15)3/3 - 4189=9948 cm3
4π(20)3/3 - 14137=19373 cm3
4π(25)3/3 - 33510=31940 cm3
Differences become larger for inner spheres
→ Statistics are not enough!!
→ How to improve the statistics?
Results of Calculation
[ V o l u m e ]
  non      reg      vol      non
    1      101   5.6046E+02  0.1791
    2      102   4.0305E+03  0.0836
    3      103   9.6478E+03  0.0540
    4      104   1.9110E+04  0.0360
    5      105   3.0618E+04  0.0224
SPEAKER_NOTES:
Here you see the answer of exercise 2. In the volume dot out file, you can see a section starting from bracket volume as well as the calculated volumes.
Please think what the correct answer is. In this case, the volumes are analytically calculated because they are spheres and spherical shells. The analytically-calculated volumes do not agree with the results of Monte-Carlo calculation. Taking the most inner sphere as an example, the volume must be 560 cubic centimeters but Monte-Carlo calculation says that it is 415 cubic centimeters. Depending on the PHITS version, this number may vary. This discrepancy comes from poor Monte-Carlo statistics. So let’s think how we can improve the statistical accuracy.
ANSWER_FILE: input/lec03-3.inp

--- SLIDE 24 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Contents of Lecture III
Selection of Calculation Mode
Convenient functions for input
Setting for statistics
Monte Carlo integration
History number and statistical error
Scaling of tally results
Setting for physics
Nuclear Data Library
Physics Models
Summary
SPEAKER_NOTES:
Next subject is how statistical uncertainty is reduced by increasing the number of trials.

--- SLIDE 25 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
maxcas×maxbch ＝total number of histories
Change History Number
The accuracy of Monte Carlo simulation depends on the number of histories in a simulation
You can obtain results with better statistics by increasing the number of histories
SPEAKER_NOTES:
The number of trials, also called history number, affects the statistical accuracy of Monte-Carlo calculation. To get reliable calculation results, history number must be large enough. It is given by 2 parameters, max cas and max b c h also called max batch. Max cas is a number of histories per one batch, while max batch is the number of batch repetition. Max batch multiplied by max cas makes total number of histories.

--- SLIDE 26 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
History and batch
Q. What is number of histories?
   Number of source particles generated in the [source] section
Q. What is number of batches?
Q. What does PHITS do at the end of each batch?
Q. Why is the concept of batch introduced in PHITS?
You must adjust maxcas and maxbch case by case
Total number of histories is divided into a certain number of sets (i.e. batches). Number of histories per batch is “maxcas”; number of batches is “maxbch”
PHITS summarizes the tally results, and outputs them in text files
If PHITS does not output the intermediate results at all, you may waste a long computational time before noticing something wrong in your input file
If PHITS outputs the intermediate results very frequently, you may waste a large part of computational time just for summarizing the tally results
→ Total number of histories = maxcas x maxbch
SPEAKER_NOTES:
You could come up with a question ‘why there are two parameters to define one history number’. Please remember that history number is the number of particles starting from the source, which is defined in source section. Batch is a unit of histories, as it is called. Here histories are split into batches not to run all the histories at once. This is the reason why the idea of batch exists.
Then why do we need to split histories? To tell the truth, PHITS internally runs calculation to dump the mean and statistical uncertainty at the end of each batch. PHITS writes such midway results not to waste time. Suppose you run a calculation that takes a week without batch splitting, you will never know if your calculation makes sense until next week.  However, dumping intermediate results after every single history is not efficient because tally output takes some time.
Afterall, max cas and max batch should be optimized to make one batch reasonably long not to spend too much time for tally output. In this type of test calculations, one batch should end in some minutes. When you run bigger calculations for your business, research or study, some hours or a day per batch is appropriate.

--- SLIDE 27 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
lec03.inp
volume.out
statistical errors
(relative errors)
Increase the history number to obtain results with better statistics.
Increase maxcas to 1,000 or 10,000
Confirm that the statistical errors are decreased
How much do the statistical errors decrease when the history number increases by 10 times?
Exercise 3
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
[ V o l u m e ]
  non      reg      vol      non
    1      101   5.6046E+02  0.1791
    2      102   4.0305E+03  0.0836
    3      103   9.6478E+03  0.0540
    4      104   1.9110E+04  0.0360
    5      105   3.0618E+04  0.0224
SPEAKER_NOTES:
Let’s see how the statistical accuracy changes by the number of histories. Max cas is 100 at first so why don’t we increase it to 1000? Then let’s open volume dot out to check the results. What the statistical uncertainty, the value on the right of the volumes, will be like? Does the uncertainty go down even more if you increase max cas to 10000?
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-4.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
[ V o l u m e ]
  non      reg      vol      non
    1      101   4.1549E+02  0.2106
    2      102   3.3346E+03  0.0922
    3      103   9.9239E+03  0.0541
    4      104   1.8974E+04  0.0361
    5      105   3.0770E+04  0.0222
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
lec03.inp
volume.out
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 1000
  maxbch = 10
  file(6) = phits.out
[ V o l u m e ]
  non      reg      vol      non
    1      101   5.4065E+02  0.0578
    2      102   3.7146E+03  0.0275
    3      103   9.8763E+03  0.0170
    4      104   1.9252E+04  0.0112
    5      105   3.1481E+04  0.0068
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 10000
  maxbch = 10
  file(6) = phits.out
[ V o l u m e ]
  non      reg      vol      non
    1      101   5.3264E+02  0.0185
    2      102   3.6575E+03  0.0088
    3      103   9.9620E+03  0.0054
    4      104   1.9343E+04  0.0035
    5      105   3.1887E+04  0.0021
4π(5)3/3=524 cm3
4π(10)3/3 - 524=3665 cm3
4π(15)3/3 - 4189=9948 cm3
4π(20)3/3 - 14137=19373 cm3
4π(25)3/3 - 33510=31940 cm3
The true value does not always lie within the statistical error!
Increase the history number to obtain results with better statistics.
exact solutions
（analytic solutions）
Answer 3
SPEAKER_NOTES:
This is the answer of exercise 3. By increasing max cas, the statistical uncertainty goes down. Eventually, the volume of innermost sphere gets much closer to the analytical answer of 524 cubic centimeters.
Theoretically, history number and statistical uncertainty are related in following manner. First, the answer converges by increasing the history number. Second, the statistical error decreases approximately by square root of 10 when you increase the history number by 10. Third, as PHITS shows one sigma statical error, the convergence value lies within the range of error at 68% of probability. This means that the convergence value does not necessarily fall within the statistical error in the output file.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-4.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 10000
  maxbch = 10
  file(6) = phits.out
  istdev = -2
lec03.inp
You can obtain the result with better statistics by restart calculation adding a new result to the previous result.
Add istdev=-2 and then execute PHITS in restart calculation mode.
Restart Calculation mode
Information on each batch is also outputted.
In the restart calculation mode, a message is shown in the console screen.
SPEAKER_NOTES:
Please note another useful function, that is restart calculation function.
Given that you had run one-week long calculation but you found the statistical uncertainty was not satisfactory low. You would like to improve the statistics even more but at the same time you don’t want to waste the result of last 1 week. In that case, let’s set a parameter named i s t d e v to be minus one and run. Then PHITS reads the existing results and run as a continued calculation. In this way, you can run a two-week long calculation by running another week.
When you run a restart calculation, a message saying ≪?this is restart calculation?≫ pops up in the console screen. In the next slide, let me explain why this message is followed by another message saying about initial random number seed. The information on each batch in the restart calculation follows.
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Random number used in PHITS is a pseudo-random number* with the period of 264-1(~ 1019)
Default random seed (rseed) is fixed for sustaining the reproducibility of simulation results
264-1
Start
Restart simulation
Random Number
*Based on xorshift64 algorithm
SPEAKER_NOTES:
So far, we haven’t explained anything about the random number even though PHITS uses random numbers. Some of you might have wondered why your calculation result is always identical no matter how many times you run it. This is because PHITS uses pseudo-random numbers. Pseudo-random number is a sequence of completely uncorrelated numbers which are created by certain algorithms. The algorithm built in PHITS doesn’t change as long as you use PHITS, so the random numbers and the results are the same.
The random number used in PHITS has a cycle of 2 to the power of 64, which is about 10 to 19. For the sake of reproducibility of the calculation, the initial random number is always the same being 6.647299061401 times ten to 12.
This initial random number can be specified by a parameter called r seed. If r seed is 10, the random number starts from 10.
Getting back to the story about restart calculation, you start a calculation with a certain initial random number seed and use certain length of random number sequence. If you launch a restart calculation, it inherits the final random number of the previous run as an initial random number and use another set of random number sequence. If you launch another restart calculation, subsequent random numbers are used. As a result, the statistical accuracy of this calculation become identical to that of 3 times as long. Not overlapping each other, all the random numbers are valid. After all, the core message of this slide is that you don’t have to care about random number overlap.

--- SLIDE 31 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
440 <--- Number of remaining batches

-------------------------------------------------------------------------------
bat[     560] ncas =            560. : rijk    = 151264979546685.
       low neutron =              0. : ncall/s =  4.000000000E+00
          cpu time =   0.288 s.

 date = 2018-05-02
 time = 15h 08m 25
The value at the first line is the remaining batch number. You can reduce it by changing the value and saving batch.out. For example, changing the value to “0” will terminate the PHITS execution when the simulation of current batch is finished
batch.out
Terminate PHITS simulation by batch.out
“Batch” is a set of source particles to be simulated in a single program run
When the simulation of one batch is finished
PHITS updates the tally outputs, and the code is still running for the next batch. Plots (*.eps) are also updated if you set “itall=1” in [parameters]
You can terminate the job manually by editing “batch.out” file
SPEAKER_NOTES:
The next thing to learn is use of the batch file.
As explained earlier, PHITS calculation is split into multiple batches corresponding to sets of source particles. Users can terminate the calculation at the end of a batch by manually editing batch dot out. Of course, you can stop it with control key plus c in the console screen but by soft stop using batch file gives you all the results including PHITS dot out.
The first value of batch dot out means the number of remaining batches. So if you overwrite it with 0, the calculation stops after the current batch.

--- SLIDE 32 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
lec03.inp
Comment out the line of istdev by marking $. (Do not use restart calculation mode)
Increase maxbch to 106 to execute a long calculation.
Check the intermediate result.
Terminate the job by “batch.out”.
Exercise 4
Terminate the job by “batch.out”
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 10000
  maxbch = 1000000

  file(6) = phits.out
 $ istdev = -2
This job was terminated by batch.out
SPEAKER_NOTES:
Let’s try terminating calculation by batch dot out file. Please be careful that timing is very important in this exercise. First, please comment out i s t d e v not to make the calculation complicated. As we want to stop the calculation on the halfway, please increase max batch to 1000 or 1,000,000 to make the calculation long. Then let’s launch the calculation.
Opening volume dot out, you can see that the results are updated. Then please open batch dot out and overwrite the first number to be zero. As soon as the current batch is finished, PHITS stops, with showing a message in the console window which says the calculation is stopped by batch dot out.
If you failed to stop the calculation, try again afresh. Please start the calculation, open batch dot out and change the first number to be zero.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-5.inp

--- SLIDE 33 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
[ P a r a m e t e r s ]
   icntl = 14
maxcas = 10000
  maxbch = 1000
…
[ T - V o l u m e ]
     mesh =  reg
     reg = 101 102 103 104 105
     file = volume.out
     s-type =    2
     x0 = -c1
     x1 =  c1
     y0 = -c1
     y1 =  c1
     z0 = -c1
     z1 =  c1
    stdcut = 0.01
lec03.inp
Standard Deviation Cut-off
Terminate the job when the statistical errors of all tally results reach the stdcut
You can specify “stdcut” in each tally
    (The job is terminated only when all stdcut conditions are satisfied)
Exercise 5
Terminate the job by “stdcut”
What does “stdcut” means?
This job is terminated by stdcut
SPEAKER_NOTES:
The other tool to terminate calculation in halfway is stdcut, which stops calculation when the statistical uncertainty satisfies the specified criteria. When the statistical uncertainty of all bins in the tally decreased below stdcut of the tally, PHITS stops. In other words, stdcut terminates calculation when the statistical uncertainty is good enough. Stdcut can be specified in more than 1 tally. In this case, calculation is stopped when all the conditions are satisfied. So please be careful to set stdcut in a tally whose convergence is slow, calculation may take very long time.
Let’s try exercise 5, insert a line stdcut equal 0.01 in t volume section. After running this calculation, please confirm that the statistical uncertainty of t volume tally output is equal or lower than 0.01.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-6.inp

--- SLIDE 34 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Both shared-memory (OpenMP) and distributed-memory (MPI) parallelization are available in PHITS.
Installation of MPI protocol is necessary for using MPI version*, while no additional software installation is required for using the OpenMP version.
You can use the parallelization by adding “$MPI=XX” or “$OMP = XX”
(XX: number of CPU core) in your input file before the 1st section.**
MPI is faster than OpenMP when you use the same number of CPU cores.
If you set “$OMP=0”, all CPU cores are used in the PHITS simulation. This option may slow down other applications in your computer.
Parallel Mode
Important notice
For Linux, libiomp5.so library may be required for PHITS with OpenMP.    Install & setup the library following the instruction in 2.3.3 in the PHITS manual.
**Only when phits.bat or phits.sh is used for running PHITS. “$MPI” option is not available in Mac
*See phits/document/Install-IntelFortran-OneAPI-en.pdf for the installation of MPI protocol on Windows
SPEAKER_NOTES:
So far, we learned how to terminate calculation in halfway. Then the next question is how we can run calculation faster. The answer is parallelization. PHITS has 2 options to parallelize calculation, one is shared-memory parallelization, the other is distributed-memory parallelization. Distributed-memory parallelization by M P I is not easy because it requires installation of M P I protocol. On the other hand, open M P is much easier because it does not need any computer configuration in most environments. The downside of open M P is low parallelization efficiency. To use the same number of cores, calculation by M P I is faster than that by open M P.
To use open M P, please insert a line starting with dollar symbol, o, m, p, equal, number, at the top of the input. This number means the number of cores assigned to this calculation. If this number is zero, PHITS uses all the cores in your computer slowing down all the other programs such as text editor, mailer, etc.
Open M P is not available in 32-bit windows and some Linux machines which does not have a library file named lib i o m p 5 dot s o. In such Linux environment, please configure the setup of your machine following the PHITS manual.

--- SLIDE 35 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
$OMP = 4
[T i t l e ]
・ ・ ・ ・ ・ ・
lec03.inp
Optional Exercise
Let’s set “$OMP” at the 1st line of input file, and run PHITS
Message for the use of OpenMP
SPEAKER_NOTES:
Once you launch your calculation with an input whose first line is dollar o m p equal 4, the calculation is parallelized in this way. In the console window, you see lines saying that open m p parallel process from 1 to 4 were started. At the end, you see messages saying that open m p parallel processes were terminated. CPU time does not change very much in case of this short calculation but when it comes to long calculation, the difference is noticeable.
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 36 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Contents of Lecture III
Selection of Calculation Mode
Convenient functions for input
Setting for statistics
Monte Carlo integration
History Number and statistical error
Scaling of tally results
Setting for physics
Nuclear Data Library
Physics Models
Summary
SPEAKER_NOTES:
Next subject is normalization of calculation.

--- SLIDE 37 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
set: c1[25]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 =  -30.0
 z1 =  -30.0
 dir =  1.0
lec03.inp
Normalization of Tally Results
Tally outputs are normalized to per “single” source generation*, NOT proportional to the total number of source generation (maxcas x maxbch).
To compare the results with measured values, the calculation results have to be scaled to the source intensity (e.g. Bq and /cm2/s), or multiplied by a conversion factor.
Using the parameter “totfact”, you can obtain the results directly in units you want, such as /cm2/s and mGy/h.
* per “weight” in a stricter sense
SPEAKER_NOTES:
In the calculation so far, tally outputs were normalized to be per single source particle. In other words, no matter how many particles are shot from the source, the results do not increase because they were divided by the product of max cas and max batch. They instead converge to certain value.
However, to compare calculated data with experimental data, the magnitude taking into account for the source intensity or beam intensity is crucial.
To compare the results with measurement data with units such as gray per hour, please define a parameter called t o t fact to normalize the results of PHITS by source intensity.
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 38 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Estimate the absolute value of dose in Gy
Assuming that the onion structure is uniformly irradiated by 150-MeV protons. The flux is 106 particle/cm2/sec, and irradiation time is 1 hour. What are the absorbed doses (Gy) deposited in each cell?
150-MeV protons are incident to the onion with the flux of 106 (/cm2/s) for 1 hour
SPEAKER_NOTES:
Let’s take this onion structure as an example of absolute dose calculation.
Suppose that the onion structure is exposed to uniform 150 MeV proton beam whose flux is 10 to 6 particle per square centimeter per second for one hour. The question is that are the absorbed doses in each cell.

--- SLIDE 39 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6
Let’s calculate the absorbed dose per 1 proton source first!
lec03.inp
Set icntl = 0 for normal PHITS simulation
Set maxcas = 2000 and maxbch = 5 to reduce the computational time
Activate infl:{volume.out} command to read the [volume] section generated by
[t-volume], otherwise PHITS does not know the volume of each cell
Activate [t-deposit] section
Execute PHITS and check deposit.out
[ P a r a m e t e r s ]
   icntl = 0
  maxcas = 2000
  maxbch = 5
…

[ S o u r c e ]
…
infl: {onion.inp}[1-31]
$ infl: {volume.out}
…

[ T - Deposit ]
  title = Deposition energy in reg mesh
  mesh =  reg
  reg = 101 102 103 104 105
  unit =    0    # unit is [Gy/source]
SPEAKER_NOTES:
Let’s try this calculation in exercise 6 and 7. Exercise 6 is for calculation of dose per single incident proton. When exercise 6 is done, please proceed to exercise 7 to change the beam fluence.
First, please change icntl from 14 to 0 to run normal transport calculation. To save CPU time, please decrease max cas and max batch to 2000 and 5, respectively. To calculate absorbed dose, PHITS must know the masses of cells. So please activate i n f l command which imports volume dot out by deleting comment symbol.
Finally, activate t deposit section by deleting off.
MENTIONED_INPUT_NAMES: lec03.inp, onion.inp
ANSWER_FILE: input/onion.inp

--- SLIDE 40 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Answer 6
(around line 29)
#  num    reg     volume       all       r.err
    1     101   5.2465E+02   3.7110E-16  0.2021
    2     102   3.6454E+03   1.8475E-15  0.1577
    3     103   9.9378E+03   2.5310E-14  0.0194
    4     104   1.9364E+04   2.8606E-13  0.0116
    5     105   3.1919E+04   3.2218E-13  0.0086
deposit.out
track_xz.eps
Tally results are basically normalized to per source particle (/source)
Only 3.2E-13(Gy) = 0.32 pGy is deposited at the outermost shell per incidence of one 150-MeV proton
Absorbed doses in inner shells are much lower because primary protons cannot reach the cells
SPEAKER_NOTES:
The result of exercise 6 is like this.
Being normalized to one source particle, the dose is about 0.32 pico gray even in the outermost shell. In the core sphere, the dose is 3 orders of magnitude smaller.
ANSWER_FILE: input/lec03-7.inp

--- SLIDE 41 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Exercise 7
How about the case of 1-hour irradiation with flux of 106(/cm2/s)?
If the flux is 106 protons cm-2 s-1, how many protons in total should be generated over the whole source area in 1 second?
   (source area is (2*c1)2cm2 = 2500 cm2)
How about the case of 1-hour irradiation, instead of 1-second irradiation?
Set “totfact” in [source] section for the total number of protons generated in the source area
→ all tally results are multiplied by that number
lec03.inp
set: c1[25]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 =  -30.0
 z1 =  -30.0
 dir =  1.0
SPEAKER_NOTES:
Let’s proceed to exercise number 7 to calculate the dose deposited to the onion considering the irradiation time of 1 hour and fluence of 10 to 6 per square centimeter per second.
The number of protons popping out from the source surface is the product of the source intensity and the source area of 2500 square centimeters. Please don’t forget to consider the irradiation time of 1 hour.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-8.inp

--- SLIDE 42 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Answer 7
(Around line 29)
#  num    reg     volume       all       r.err
    1     101   5.2465E+02   3.3399E-03  0.2021
    2     102   3.6454E+03   1.6628E-02  0.1577
    3     103   9.9378E+03   2.2779E-01  0.0194
    4     104   1.9364E+04   2.5745E+00  0.0116
    5     105   3.1919E+04   2.8996E+00  0.0086
deposit.out
track_xz.eps
All tally results are multiplied by totfact, i.e. data are scaled to 9x1012 proton incidence
Absorbed dose in the outmost shell is 2.9 Gy
Absorbed dose in the inner sphere is 4.3 mGy, but this value is not statistically significant due to the large statistical error
lec03.inp
set: c1[25]

[ S o u r c e ]
 totfact = 1.0e6*(2*c1)**2*3600
…
Multiplied by totfact
(Label is not changed)
You can check the numerical value of totfact in phits.out
SPEAKER_NOTES:
This is the answer of exercise 7. As the number of protons from the sources is 10 to 6 per square centimeter per second, this is multiplied by the source area 2500 square centimeters which is square of c1 times 2. Furthermore, the total number of protons is this value multiplied by 3600 seconds.
This calculation shows that the dose of the outermost shell is about 2.9 Grays. Meanwhile, the dose in the inner most core has large uncertainty but it is 3 orders of magnitude lower
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-8.inp

--- SLIDE 43 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Contents of Lecture III
Selection of Calculation Mode
Convenient functions for input
Setting for statistics
Monte Carlo integration
History Number and statistical error
Scaling of tally results
Setting for physics
Nuclear Data Library
Physics Models
Summary
SPEAKER_NOTES:
To obtain physically meaningful results, appropriate settings for physics models and data libraries are required.

In PHITS, appropriate physics models and data libraries are already assigned for each particle type and energy range, and therefore change of parameters are not necessary for most of the cases.

However, there are still some cases, for instance, to reduce the computational time, change of parameters are required.

In this lecture, we will explain the default settings and how one can change the parameters.

--- SLIDE 44 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Why cross section data libraries?
Because reaction cross sections of photons, electrons, positrons, and low-energy neutrons (E < 20 MeV) have complex structures, reaction models cannot well-describe their behaviors. → Cross section data libraries are required.
If you want to extend the library use in PHITS such as particle types and energy ranges, you have to change some parameters in [parameters]
Neutron reaction cross sections on 113Cd target（JENDL-4.0）
*Only limited libraries of JENDL-5 are included in the PHITS package and their full package can be automatically download and setup using jendl5_setup files in XS folder
Recently, high-energy neutrons (E< 200 MeV), charged particles (p, d, α), and photo-nuclear data libraries are prepared as JENDL-5*
SPEAKER_NOTES:
Firstly the setting for data libraries.

Because reaction cross sections of photons, electrons, positrons, and low-energy neutrons have complex structures, reaction models cannot well-describe their behaviors.

For instance, this figure shows the neutron reaction cross-section for cadmium. In the range from several ten MeV to several hundred MeV, fluctuation due to nuclear resonances is seen. This structure varies for each isotope and thus it is impossible to reproduce precisely by physics models even with the updated nuclear theory.

Nuclear cross-section data libraries for each nucleus are included in PHITS and transport calculations are performed by directly adopting the data. Actually these cross-section data libraries occupies large portion of the PHITS package.

The setting for the data libraries is controlled by the parameters in the parameter section of the PHITS input file.

--- SLIDE 45 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Related Parameters
negs
Option for electromagnetic transport simulation
-1: Transport only photons based on the PHITS original database (default)
0: Do not transport photons, electrons, and positrons
1: Transport photons, electrons, and positrons based on EGS5 database
emin(i), i: particle ID
Cut off energy of each particle ID. Particles below this energy dump the rest of their kinetic energies locally, and are no longer transported in the simulation.
dmax(i), i: particle ID
Maximum energy of each particle ID to use cross section data library
Must be specified when you want to use charged-particle and high-energy neutron libraries such as JENDL-5
*Recommended for most calculation!
*negs = 2 is recommended when photons & electrons with energies over 1 GeV are transported
SPEAKER_NOTES:
The parameters controlling the data libraries are as follows.

NEGS is a parameter to select the option for transport photons, electrons, and positrons. When it is -1, only photons are transported by the PHITS original library. When it is 0, no photon, electron, and positron transport are considered. When it is 1, photons, electrons, and positrons are transported by the EGS5 data library. The default value is -1, namely only photons are transported, and electrons and positrons are not transported. This is to prevent too long computational time due to the production of tremendous number of electrons during the transport of protons and ions. Electron transport may not be necessary for users who are interested in ion transport. On the other hand, consideration of electron transport is necessary for microscopic scale calculations and NEGS=1 is required.

EMIN is a parameter to set the cut-off energy of each particle. The number in the bracket corresponds the particle ID. For instance, 1 is proton, 2 is neutron and so on. The reasonable cut-off energies were already assigned as default values.

DMAX is a parameter to set the upper limit energy for the data libraries. Above this energy, the transport calculation is performed by a physics model. Default values for DMAX are also prepared and so you do not need to change unless you have a strong reason.

--- SLIDE 46 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
emin(i) & dmax(i)
calculate the deposition energy in a fine mesh (less than 1 mm) → emin(12, 13) = 0.001*
reduce the computating time if the simulation objects are too large → emin(12, 13) = 1.0
transport very high energy photons, electrons, and positrons → dmax(12-14) = 1.0e5**
use JENDL-5 for charged particle and high energy neutrons → dmax(1, 2) = 200.0 etc.
You have to change these parameters when you want to…
*The numbers in red are automatically set only when negs = 1
(In the case of negs=-1, the values for electrons and positrons are not set.)
*dmax(12-14) should be also set to small depending on particle energies
** dmax(12-14) is automatically adjusted to 1.0e7 when negs = 2
SPEAKER_NOTES:
The default values of EMAX and DMAX are as follows.

The data library is used to transport particles within the energy range between the cut-off energy EMIN and the upper limit DMAX.
For neutrons, nuclear data library is used from thermal energy to 20 MeV.
For electrons and positrons, the default cut-off energy is 100 keV.
For photons, the cut-off energy is 1 keV.
Because the default values are given in this way, usually you do not need to specify EMIN and DMAX. However, there are some cases the specifications are required as explained below.

For instance, if you are interested in the simulation finer than 1 mm scale, the cut-off energy of electrons, 100 keV, is too high and need to lower to 1 keV. If the geometry is huge and no interest for fine distributions, it may be better to increase the cut-off energy till 1 MeV to reduce the computational time.

In addition, if you would like to transport high energy photons, electrons, and positrons, or you would like to use high energy nuclear data libraries, increase of the upper limit DMAX is required.

--- SLIDE 47 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
“file” Parameters
SPEAKER_NOTES:
In some case, setting of data path may be required to use data libraries.
The followings are the data path related to data libraries.

File(1) is the path for the PHITS folder. The absolute path for the PHITS folder needs to be assigned. The default setting of other data paths are specified relative to the PHITS folder path and thus you do not need to specify unless you change the folder structure inside the PHITS folder.

The specification of the data path for File(1) is also not necessary if you have used the PHITS installer to install PHITS. The PHITS installer automatically register the PHITS path into environmental path. The data path specification is only required when you install PHITS without using the PHITS installer.

--- SLIDE 48 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
lec03.inp
Activate electron and positron transport using EGS5
Set maxcas=1000 and maxbch = 1 to reduce the computational time
Set source particles to 10-MeV photons
(change %projectile% and “e0” in [source] section)
Add electron  positron in “part” of [t-track]
Exercise 8
[ P a r a m e t e r s ]
   icntl = 0
  maxcas = 2000
  maxbch = 5

file(6) = phits.out
$ istdev = -2
 negs =
[ T - T r a c k ]
mesh =  xyz
・ ・ ・ ・ ・ ・
part =  %projectile%
・ ・ ・ ・ ・ ・
file = track_xz.out
[ S o u r c e ]
set:%projectile%[proton]
・ ・ ・ ・ ・ ・
 e0 =   150.0
Set negs = 1 in [parameters] section
Execute PHITS and check electron, positron, and photon fluxes (see 2nd to 4th pages of track_xz.eps)
Execute PHITS again and check the trajectories of electrons and positrons
SPEAKER_NOTES:
Let’s try using data library.

Firstly please decrease the number of histories as MAXCAS=1000 and MAXBCH=1 in order to reduce the computational time. Then please change the source to 10 MeV photon.

Please add electron, positron, and photon in the PART parameter in the T-TRACK tally. This will allow you to see the tracks of electrons, positrons, and photons additionally to proton tracks.

Firstly let’s execute PHITS with this input. No NEGS specification is given in this input and therefore only photons will be transported.

When you obtain the result, please check the track_xz.eps file. The page 2 shows the electron tracks, the page 3 shows the positrons tracks, and the page 4 shows the photon tracks. You can confirm that no track in page 2 and 3 while there are tracks in page 4.

Secondly please add NEGS=1 in the parameter section and re-execute PHITS.
Electrons and positrons will be also transported and you should be able to see tracks in page 2 and 3.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-9.inp

--- SLIDE 49 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Activate electron and positron transport using EGS5
Answer 8
lec03.inp
[ P a r a m e t e r s ]
   icntl = 0
  maxcas = 1000
  maxbch = 1

  file(6) = phits.out
$ istdev = -2
 negs = 1
[ T - T r a c k ]
mesh =  xyz
・ ・ ・ ・ ・ ・
part =  %projectile% electron positron
・ ・ ・ ・ ・ ・
file = track_xz.out
[ S o u r c e ]
set:%projectile%[photon]
・ ・ ・ ・ ・ ・
 e0 =   10.0
track_xz.eps (2nd page)
track_xz.eps (1st page)
Electron Flux
Photon Flux
Electrons and positrons generated by photo-atomic interactions are transported using EGS5
SPEAKER_NOTES:
With NEGS=1 in the parameter section, electrons and positrons are also transported so that you can see tracks in page 2 and 3. The photon track do not show significant difference compared to the previous result without NEGS=1. If you are interested in only the dynamics of low energy photons, specification of NEGS may not be necessary.
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 50 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
lec03.inp
Let’s feel the extension of computational time by setting a lower cut-off energy (1 keV) for electrons and positrons
Add emin(12) = 0.001 and emin(13) = 0.001 in [parameters] section
Exercise 9
[ P a r a m e t e r s ]
   icntl = 0
maxcas = 1000
  maxbch = 1

 file(6) = phits.out
$ istdev = -2
 negs = 1
 emin(12) =
 emin(13) =
Note: default value of emin(12) & emin(13) is 100 keV
SPEAKER_NOTES:
In the next, let’s change the cut-off energies.

The default values of electrons and positrons are 100 keV. Please set EMIN(12) and EMIN(13) to 1 keV in order to lower the cut-off energy to 1 keV and check how the computation becomes longer in time.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-10.inp

--- SLIDE 51 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
lec03.inp
Let’s feel the extension of computational time by setting a lower cut-off energy (1 keV) for electrons and positrons
Answer 9
[ P a r a m e t e r s ]
   icntl = 0
  maxcas = 1000
  maxbch = 1

 file(6) = phits.out
$ istdev = -2
 negs = 1
 emin(12) = 0.001
 emin(13) = 0.001
track_xz.eps (2nd page)
track_xz.eps (1st page)
Electron Flux
Photon Flux
Results are almost independent of the cut-off energy in this spatial resolution (5 mm), instead of the longer computational time
Note: range of 100 keV electron in water is approximately 0.14 mm
SPEAKER_NOTES:
You can realize the computational time becomes much longer compared to the 100 keV cut-off energy calculation.

However, if you see the track distribution in track_xz.eps, no significant difference is noticed. This is because the range of 100 keV electron in water is about 0.14 mm and thus you can not see much difference in this scale. Consideration of the scale of physics is required to set appropriate cut-off energies. In contrast, you can reduce the computational time by setting the higher cut-off energies for large scale geometries.
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 52 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Contents of Lecture III
Selection of Calculation Mode
Convenient functions for input
Setting for statistics
Monte Carlo integration
History Number and statistical error
Scaling of tally results
Setting for physics
Nuclear Data Library
Physics Models
Summary
SPEAKER_NOTES:
Let’s move on to the topic of the physics models.

--- SLIDE 53 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Option for beam transport analysis
nspred and nedisp: Consider angular and energy straggling of charged particle, respectively (Important for beam transport analysis). Entries of [Parameters] section.
Recommended settings are nspred = 2 & nedisp = 1.
(Default settings are nspred=0 & nedisp=0)
Depth-dose distribution of 200MeV/u 12C beams into water.
(close-up view around Bragg peak)
SPEAKER_NOTES:
Firstly the options for charged particle beam transport.

Charged particle beams are broadened by the multiple Coulomb scattering with the elements in matter. PHITS adopted angular and energy struggling models to reproduce the beam broadening. The angular struggling is activated by NSPRED parameter and the energy struggling is activated by NEDISP parameter in the parameter section. The recommended settings are NSPRED=2 and NEDISP=1.

This figure shows the Bragg peak of the carbon beam in water. Without angle and energy struggling, carbon beam produce a very sharp Bragg peak. In reality, however, the peak is broadened due to fluctuation of the peak position of each carbon ion due to the struggling.

--- SLIDE 54 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Switching Energy
* note: easy to check what models are used from “phits.out”
SPEAKER_NOTES:
Parameters to change nuclear reaction models are as follows.

PHITS includes many physics models inside and appropriate models are already assigned for each  particle type and energy range. It is possible to change the physics models to study influence of the different physics models. The parameters listed in this table are for this purpose.

--- SLIDE 55 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Neutron     Nuclear data         INCL (inclg=1)             JAM
(10-11 MeV)
emin(2)
(20 MeV)
dmax(i)
(3 GeV)
einclmax
(10-3 MeV)
emin(1)
Nucleus                                 JQMD                         JAMQMD
d, t, 3He, α                             INCL (inclg=1)           JAMQMD
(3 GeV)
einclmax
Map of Nuclear Reaction Models
Proton                                   INCL (inclg=1)               JAM
(1 MeV)
einclmin
(10-3 MeV/n)
emin(i)
(3 GeV/n)
einclmax
(1 MeV/n)
einclmin
(10-3 MeV/n)
emin(i)
(3 GeV/n)
ejamqmd
(10 MeV/n)
eqmdmin
SPEAKER_NOTES:
This table shows the list of physics models and their energy threshold parameters.

--- SLIDE 56 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Conventional Mode
Event Generator (EG) Mode
A nuclear reaction model for low-energy neutron interaction using nuclear data library combined with a mathematical model*
Determine all ejectiles emitted from low-energy neutron interaction, considering the energy and momentum conservation
* T. Ogawa et al., Nucl. Instru. Method. A 763 (2014) 575
(n,2n)
20 MeV
15 MeV
10 MeV
(n,2n)
20 MeV
(n,np)
8 MeV
20 MeV
15 MeV
4 MeV
1 MeV
20 MeV
(n,np)
8 MeV
11 MeV
1 MeV
neutron
proton
recoil
nucleus
(presume Q = 0)
Event Generator Mode
Only neutrons and gammas are considered as secondary particles
Energy and momentum is NOT conserved in each event
Cross sections in nuclear data library are perfectly reproduced
All particles are considered as secondary particles
Energy and momentum is conserved in each event
Cross sections in nuclear data library are slightly distorted
SPEAKER_NOTES:
Explanation of event generator mode.
This function is a unique feature of PHITS, which does not exist in other Monte Carlo codes.

Transport of low-energy neutrons are computed by the nuclear data library. The reactions and transport of neutrons are calculated with a good accuracy, but production of secondary particles and transport of recoil particles are not considered. This is because only part of the reaction channels within countless number of channels are included in the data libraries and reproduction of the whole reaction system including secondary particles as an event is not possible.

In PHITS, therefore, the event generator model is prepared, which combines statistical decay models with the nuclear data library to reproduce an event of the whole reaction system of low-energy neutron reaction. The event generator mode produce an event includes secondary particles satisfying the momentum and energy conservation as a whole reaction system.

In the normal mode without the event generator, only neutrons and gamma rays are treated as secondary particles. Energy and momentum are not conserved for each individual reaction event, although the averaged distributions perfectly reproduce those given by the nuclear data libraries.

In contrast, the event generator mode considers all secondary particles, including residual nuclei, and conserves energy and momentum in each reaction event. The averaged results still reproduce the nuclear data distributions with good accuracy.

--- SLIDE 57 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Event generator mode is recommended
to know spectra of proton or alpha particles from reactions of low-energy neutrons.
to obtain information on residual nuclei (e.g. recoil energies).
to perform event-by-event analysis (e.g. response function calculation).
Event generator mode is NOT recommended
to calculate neutron/photon transmission.
to use neutron nuclear data library up to 200 MeV
to calculate dose by neutrons below 200 MeV using kerma approximation* (e.g. dosimetry for BNCT)
When do we use EG-Mode ?
*Approximation for estimating the average heat generation from neutron fluence
SPEAKER_NOTES:
Next, we explain situations in which the event generator mode should or should not be used.

The event generator mode is recommended when detailed information on secondary particles produced by low-energy neutron reactions is required. Typical examples include studies focusing on the spectra of emitted charged particles such as protons or alpha particles, investigations of residual nuclei, and simulations requiring event-by-event information, such as detector response calculations. The use of the event generator mode is also recommended for heat deposition calculations involving high-energy neutrons, where the kerma approximation is no longer valid. Medical physics simulations, such as proton therapy and heavy-ion therapy calculations, are representative applications of this category.

On the other hand, the event generator mode is not necessary for calculations in which neutron and photon information alone is sufficient, such as shielding analyses, or for simulations that require highly accurate tracking of low-energy neutron behavior based strictly on nuclear data libraries. Furthermore, because the treatment of nuclear data libraries differs above 20 MeV in the event generator mode, this mode should be disabled when accurate secondary particle production based directly on evaluated neutron nuclear data libraries up to 200 MeV is required.

When the event generator mode is not used, the neutron dose contribution is calculated based on the kerma approximation, allowing statistical accuracy to be improved more efficiently within shorter computation times.

--- SLIDE 58 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
How to Use EG-Mode
Set “e-mode = 2” in the [Parameters] section
SPEAKER_NOTES:
The activation of the event generator mode is controlled by the E-MODE parameter.
E-MODE=0 is specified as default value so that the event generator mode is not activated.
Please set E-MODE=2 to activate the event generator mode.

--- SLIDE 59 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
lec03.inp
Exercise 10
Remove (or comment out) emin(12) & emin(13) to reduce the computational time

Set source particles to 10-MeV neutrons
(change %projectile% in [source] section)
Change “part = all” to “part = neutron proton”
[ T - Deposit ]
・ ・ ・ ・ ・ ・
file = deposit.out
part = all
[ S o u r c e ]
set:%projectile%[photon]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
・ ・ ・ ・ ・ ・
 emin(12) = 0.001
 emin(13) = 0.001
Execute PHITS and check neutron and proton doses (see deposit.out)
First, perform the transport calculation with 10-MeV neutron sources without using an event generator mode.
SPEAKER_NOTES:
Let’s try to use the event generator mode.

Firstly let’s calculate without the event generator mode.

To reduce the computational time, please remove the cut-off setting of electrons and positrons.
Then please set the source to be 10 MeV neutrons.

Please replace all to neutron and proton in the PART parameter for the T-DEPOSIT tally.

Then let’s check the text file DEPOSIT.OUT after executing PHITS.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-11.inp

--- SLIDE 60 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
lec03.inp
Answer 10
[ P a r a m e t e r s ]
・ ・ ・ ・ ・ ・
$ emin(12) = 0.001
$ emin(13) = 0.001
(around line 29)
#  num    reg     volume       neutron   r.err      proton    r.err
    1     101   5.2465E+02   4.4415E-05  0.2975   0.0000E+00  0.0000
    2     102   3.6454E+03   6.4578E-02  0.1427   0.0000E+00  0.0000
    3     103   9.9378E+03   1.5546E-03  0.0875   0.0000E+00  0.0000
    4     104   1.9364E+04   1.0111E-01  0.0491   0.0000E+00  0.0000
    5     105   3.1919E+04   1.5905E-01  0.0264   0.0000E+00  0.0000
deposit.out
[ T - Deposit ]
・ ・ ・ ・ ・ ・
file = deposit.out
part = neutron proton
[ S o u r c e ]
set:%projectile%[neutron]
・ ・ ・ ・ ・ ・
 e0 =   10.0
No dose contribution from protons → Charged particles are not produced in neutron transport simulation below 20 MeV without using event generator mode
First, perform the transport calculation with 10-MeV neutron sources without using an event generator mode.
SPEAKER_NOTES:
Around the line 29 of the DEPOSIT.OUT, you should see the result as follows. You may see statistically different results due to the different version of PHITS, but you can confirm that the values exist in the neutron column but zero in the proton column. This is because protons which should be produced from neutron reactions are not transported without the event generator mode and thus the dose by protons is zero. Without the event generator mode, the neutron dose is computed by using the Kerma approximation.
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 61 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
[ P a r a m e t e r s ]
・ ・ ・ ・ ・ ・
e-mode = 2
Set “e-mode = 2” in [parameters] section and execute PHITS
Exercise 11
A warning is shown when “neutron” is specified in “part” of [t-deposit]
because Kerma approximation is recommended to use for calculating “neutron dose”
lec03.inp
Check neutron and proton doses (see deposit.out)
Use an event generator mode.
SPEAKER_NOTES:
Secondly, let’s set E-MODE=2 in the parameter section to activate the event generator mode.

With the event generator mode, the neutron dose is not computed but instead doses from the secondary particles are computed. To avoid the double counting, the neutron dose becomes zero even if it is calculated.

The warning message shown in the pop-up window is indicating this fact that PART=neutron is specified in the T-DEPOSIT tally even though the event generator mode is activated.

After  executing PHITS, please check the dose contributions of neutrons and protons in the DEPOSIT.OUT file.
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-end.inp

--- SLIDE 62 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Answer 11
Neutron and proton doses are almost exchanged
Statistical uncertainties are larger for e-mode = 2 because neutron can deposit energies only when it causes nuclear reaction
(around line 29)
#  num    reg     volume       neutron   r.err      proton    r.err
    1     101   5.2465E+02   0.0000E+00  0.0000   0.0000E+00  0.0000
    2     102   3.6454E+03   0.0000E+00  0.0000   5.1766E-02  0.2056
    3     103   9.9378E+03   0.0000E+00  0.0000   8.3706E-04  0.2664
    4     104   1.9364E+04   0.0000E+00  0.0000   8.0923E-02  0.0712
    5     105   3.1919E+04   0.0000E+00  0.0000   1.4615E-01  0.0402
deposit.out
(around line 29)
#  num    reg     volume       neutron   r.err      proton    r.err
    1     101   5.2465E+02   4.4415E-05  0.2975   0.0000E+00  0.0000
    2     102   3.6454E+03   6.4578E-02  0.1427   0.0000E+00  0.0000
    3     103   9.9378E+03   1.5546E-03  0.0875   0.0000E+00  0.0000
    4     104   1.9364E+04   1.0111E-01  0.0491   0.0000E+00  0.0000
    5     105   3.1919E+04   1.5905E-01  0.0264   0.0000E+00  0.0000
deposit.out
（e-mode = 0）
（e-mode = 2）
SPEAKER_NOTES:
With the event generator mode by E-MODE=2, the neutron dose becomes zero while the proton dose has values. Compare to the case with E-MODE=0, the roles of neutrons and protons are exchanged. The values become almost equivalent when you increase the number of events. When we see the statistics, it is worse with E-MODE=2. This is because the neutron dose is computed by the Kerma approximation for E-MODE=0 so that it can be computed as long as  there is neutron flux. On the other hand, the proton dose is only computed when secondary protons are produced by the rare neutron reactions.

--- SLIDE 63 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Contents of Lecture III
Selection of Calculation Mode
Convenient functions for input
Setting for statistics
Monte Carlo integration
History Number and statistical error
Scaling of tally results
Setting for physics
Nuclear Data Library
Physics Models
Summary

--- SLIDE 64 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[Parameters] section is used for controlling PHITS simulation procedure.
You can select the calculation modes such as particle transport simulation, geometry and source check using “icntl” parameter.
Statistical uncertainties of PHITS simulation depend on the  history number (“maxcas” & “maxbch”)
Low-energy neutrons, as well as photons, electrons and positron must be transported using nuclear, atomic data libraries, and EGS5.
You must carefully select the physics models used in your simulation, as well as the event generator mode
Summary
If you feel difficulties for selecting these parameters, ask PHITS tutor powered by AI to find appropriate recommendation settings for your simulation
SPEAKER_NOTES:
In summary.

Selection of calculation mode and physics models are controlled in the parameter section.
The ICNTL parameter controls the calculation mode of PHITS.
Statistics and the number of events are closely related. Increase of the number of events is required to achieve better statistical results.
By using data libraries, precise calculation of the low-energy neutrons, photons, electrons, and positrons is possible.
Depending on the purpose, the setting for the physics models should be chosen such as the event generator mode.

If the appropriate setting is not known, please  try using PHITS tutor powered by AI. It will give you appropriate recommendation settings for your simulation. A sample chat is given in the next slide.

--- SLIDE 65 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
AI Phi-chan (https://x.gd/WAynQ)
Examples of prompts
Please tell me the recommended settings for using PHITS in accelerator shielding calculations
I would like to use the cosmic-ray source mode, so please tell me where the lecture materials and sample files are located
I do not fully understand the content of Exercise 5 in lec01, so please explain it in detail
Please modify the geometry in lec02 to a dice shape
How to create it for your own? (optional)
Access your NotebookLM page (or equivalent service in other AIs)
Create a new notebook
Upload text files in workbench/AI/knowledge_base folder
Upload PDF manuals of ANGEL & DCHAIN if you use these software
Edit crucial_notice_forAI.txt in workbench/AI/knowledge_base if necessary
You need to have a Google account to use NotebookLM
SPEAKER_NOTES:
This slide show examples of prompts to be provided with the AI-powered PHITS tutor. If you cannot access NoteboolLM, please try to create the AI-powered PHITS tutor for your own by following these procedures.
ANSWER_FILE: input/lec03-6.inp

--- SLIDE 66 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Transport electrons and positrons using  EGS5
Activate an event generator mode
Obtain depth-dose distribution with the relative standard deviations less than 0.5% around the Bragg peak region, by changing maxcas, istdev, batch.out etc.
Normalize the dose distribution in (Gy/s) for the case of 1-nA irradiation
Homework #3
Continued with the HW #2

--- SLIDE 67 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Depth-dose distribution inside (up) and outside (down) beam radius
Example Answer
Proton (up) and neutron (down) fluences

--- SLIDE 01 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
PHITS 講習会 基礎実習（III）:
計算条件の設定
2026年7月改訂
phits/lecture/basic/lec03
SPEAKER_NOTES:
それでは、基礎実習３を始めます。ここでは計算条件の設定についてみていきます。

--- SLIDE 02 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
はじめに
PHITSの計算は，[Parameters]セクションで定義される様々なパラメータ（物理モデルの選択など）によりコントロールされています。
全てのパラメータには初期設定値があり，基本的には変更する必要はありません。
ただし，最適な計算結果を得るためには，着目している輸送粒子の条件に応じて、いくつかのパラメータを変更する必要があります。
本実習では，パラメータの設定方法について学習します
SPEAKER_NOTES:
基礎実習１でお話しした通り、PHITSの計算には、幾何形状、線源、タリーの3つが必要です。それら３つはこれまでの基礎実習１と２でお話しました。つまり、皆さんはもうPHITSを使うための基礎は習得済みということです。基礎実習３で習得するのは、パラメータセクションの設定方法です。PHITSの計算はパラメータセクションの様々なパラメータでコントロールされていて、すべてのパラメータには初期設定値があります。
多くのパラメータは初期設定から変更する必要はありませんが、輸送粒子の条件によっては最適な計算結果を得るために、それらを最適化することが重要となります。

--- SLIDE 03 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
本実習の目標
PHITSの便利な機能を活用し，統計量や物理モデルを変化させ，最適な計算結果が得られるようになる
宿題体系における初期設定での
陽子（上）・中性子（下）フルエンス
ヒストリー数や物理モデルを適切に設定した陽子（上）・中性子（下）フルエンス
SPEAKER_NOTES:
本実習でPHITSのパラメータセクションを使えば、このように計算が変わります。どちらも陽子を水の円柱に照射した際の粒子フルエンスですが、左はパラメータセクションを初期設定のままにしたものです。不規則な分布が見えるだけで、統計制度がよくありません。右はパラメータセクションでヒストリー数や物理モデルを適切に設定することで、計算精度を改善したものです。この実習ではPHITSの便利な機能を活用し，統計量や物理モデルを変化させることで，こうした結果を得られるようになります。

--- SLIDE 04 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
実習内容
計算モードの選択
便利な入力補助機能
統計的に信頼できる結果を得るための設定
モンテカルロ積分を使った体積・面積計算
試行回数と統計誤差
計算結果の規格化
物理的に信頼できる結果を得るための設定
断面積データライブラリの利用
物理モデルの選択
まとめ
SPEAKER_NOTES:
この実習では大まかに４つ、計算モード、インプットを書く際の入力補助機能、統計的な信頼性のための設定、物理的な信頼性のための設定、についてお話していきます。

--- SLIDE 05 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
計算モードの選択
[parameters]セクションのicntlでPHITSの計算モードを変更する。
基本設定
体系確認
体積計算
まずは、基礎実習(II)で行ったジオメトリを確認するタリーを用いて、サンプルインプットの体系を確認してみましょう。
反応なし
SPEAKER_NOTES:
まずパラメータセクションのicntlという計算モードを変えるパラメータで、これは皆さんがこれまで触ったことのあるパラメータです。
これまで0で通常の輸送計算をし、8で2次元の幾何形状を確認しました。これに加えて、3次元の幾何形状を確認する11と、すべてを真空に置き換える5、体積計算を行う14についてご説明します。

--- SLIDE 06 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 11
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
lec03.inp
体系の確認([t-3dshow])
[ T - 3 D s h o w ]
  output = 3
material = -1
          6
      x0 =   0
      y0 =   0
      z0 =   0
   e-the =  70  $ eye
   e-phi =  20
   e-dst =  80
   l-the =  20  $ light
   l-phi =   0
   l-dst = 100
   w-wdt =  50  $ window
   w-hgt =  50
   w-dst =  25
  heaven = z
       line = 1
  shadow = 2
    file = 3dshow.out
   title = Check onion structure using [T-3dshow] tally
  epsout = 1
・ ・ ・ ・ ・ ・
3dshow.eps
[t-3dshow]を実行
1層5cm幅の玉ねぎ構造
現在はPHIG-3Dが代替する
SPEAKER_NOTES:
インプットを開いてみましょう。icntlパラメータが11だと、PHITSはインプット中のティースリーディーショウを探し出し、3次元体系のプロットを行います。フィグスリーディーでも3次元体系はプロットできますが、icntlパラメータが11の状態でPHITSを実行すると、スリーディーショウドットイーピーエスのように、この方法でも3次元体系をプロットできます。
ただしこれは古いオプションで、フィグスリーディーが使えるなら、そちらのほうが便利です。
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 11
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 8
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
[ T - T r a c k ]
 mesh =  xyz
 x-type =    2
 nx =  100
 xmin =  -50.
 xmax =   50.
 y-type =    1
 ny =    1
         -5.0  5.0
 z-type =    2
 nz =  100
 zmin =  -50.
 zmax =   50.
・ ・ ・ ・ ・ ・
axis =   xz
 file = track_xz.out
 title = Check source direction using [T-track] tally
gshow =    3
epsout =    1
lec03.inp
体系の確認(gshowオプション)
修正して実行
track_xz.eps
各領域のセル番号と満たされている物質名をチェック！
SPEAKER_NOTES:
icntlパラメータが8だと、PHITSはインプット中のジーショウオプションを探し出し、2次元体系のプロットを行います。実際、icntlパラメータが8の状態でPHITSを実行すると、ティートラックタリーのジーショウオプションを検知して、トラックエックスゼッドドットイーピーエスのように2次元体系がプロットされます。
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 5
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
lec03.inp
線源の確認([t-track])
修正して実行（反応なしモード）
[ T - T r a c k ]
    mesh = xyz
  x-type = 2
      nx = 100
    xmin = -50.
    xmax =  50.
  y-type = 1
      ny = 1
          -5.0  5.0
  z-type = 2
      nz = 100
    zmin = -50.
    zmax =  50.
 e-type = 1
      ne = 1
          0.  200.
    unit = 1
    axis = xz
    file = track_xz.out
   title = Check source direction using [T-track] tally
  epsout = 1
SPEAKER_NOTES:
ではここで、icntlを5、反応なしモードにして実行してみましょう。どうなるでしょうか。
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
線源の飛跡確認
track_xz.eps
全ての物質がvoidとなるため，まっすぐに飛んでいく
（線源の発生位置・方向が確認できる）
SPEAKER_NOTES:
このトラックエックスゼッドイーピーエスのような結果が得られました。すべての物質が真空で置き換えられ、線源から発生した粒子はまっすぐ飛んでいきます。この機能は線源の設定を確認するのに便利です。計算を走らせたのに結果がゼロだった場合、線源が悪いのか、幾何形状が悪いのか、タリーが悪いのか調べる必要があります。そんな時はicntlを5にすると、線源で発生した粒子がどこから発生して、どの方向に向いているか確認できます。

--- SLIDE 10 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
実習内容
計算モードの選択
便利な入力補助機能
統計的に信頼できる結果を得るための設定
モンテカルロ積分を使った体積・面積計算
試行回数と統計誤差
計算結果の規格化
物理的に信頼できる結果を得るための設定
断面積データライブラリの利用
物理モデルの選択
まとめ
SPEAKER_NOTES:
次にインプットを書く際に便利な補助機能についてです。

--- SLIDE 11 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 5
  maxcas = 100
  maxbch = 10
  file(6) = phits.out

set: c1[5]

[ S o u r c e ]
・ ・ ・ ・ ・ ・

infl: {onion.inp}[1-31]
lec03.inp
外部ファイルの挿入
[ M a t e r i a l ]
・ ・ ・ ・ ・ ・
[ M a t  N a m e  C o l o r ]
・ ・ ・ ・ ・ ・
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
[ C e l l ]
・ ・ ・ ・ ・ ・
インプットファイルとは別のファイルを取り込む場合は”infl:”コマンドを使う
  {}でファイル名，[n1-n2]で取り込む行の範囲を指定する
“off”したセクションの下にある場合、無視されるので注意
onion.inp
（inflコマンドを使う際の注意事項）バッチファイル（phits.bat）やシェルスクリプト（phits.sh）を使わずにPHITSを実行する場合は，インプットファイルの1行目にfile=ファイル名と書く必要があります
SPEAKER_NOTES:
実はこのLec03ですが、幾何形状の設定に関するセクションがないように見えます。インプットは上から見ていくと、タイトル、パラメータ、ソースと続き、ティースリーディーショウ以下はすべてタリーです。幾何形状に必要なマテリアル, サーフェス, セルセクションはありません。
しかし、ソースの下、アイエヌエフエルというコマンドがあります。このコマンドはインクルードファイルを意味し、外部ファイルから内容を持ってくることができます。コマンドの後の名前はファイル名、角カッコの中は読み込む行番号の指定で、ここではオニオンドットアイエヌピーというファイルの1から33行目を読み込みます。外部ファイルオニオンドットアイエヌピーの中は、マテリアル, サーフェス, セルセクションであり、幾何形状の設定です。これにより、PHITSは幾何形状の設定を読み込むことができます。
ここで注意すべきことが２つ、まずアイエヌエフエルコマンドを書いたセクションをオフによって無効にした場合、アイエヌエフエルコマンドも無効になってしまいます。また、PHITSのエグゼファイルを直接実行する場合、インプットファイルの一行目にファイル イコール、でこのインプットファイル名、ここではレックゼロサンを書く必要があります。
MENTIONED_INPUT_NAMES: lec03.inp, onion.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
・ ・ ・ ・ ・ ・

set: c1[5]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 = -30.0
 z1 = -30.0
 dir =  1.0
lec03.inp
PHITSでは定数を定義して、インプットファイル内でその定数を参照することが可能。
“set: ci[x]”
名前はc1からc999まで使用可能
書いた箇所より下の部分で有効となる。また、何度も同じ名前を定義できる
“off”で飛ばしたセクションの下にある場合、無視されるので注意
 （Warningが出力されます）
ユーザー定義定数と数式の利用
ユーザー定義定数の利用：
同じ値を使う場合は，予め定義しておくと便利！
数式の利用：
PHITS入力ファイルでは，FORTRAN形式の数式が利用可能
円周率（pi）は定義しなくても使える
べき乗は「**」なので注意（例えば、p(c1)2はpi*c1**2）
cosやexpなどの関数も使える（例えばcos(pi/2)。次頁に関数一覧）
inflとsetを組み合わせれば，様々な条件に対して連続して自動実行するスクリプトを作成可能*
*phits/utility/script参照
SPEAKER_NOTES:
もう３つ便利な機能を説明します。それはユーザー定義変数、数式とユーザー定義文字列です。
このインプットにはもう一つ変なところがあり、それはソースセクションのエックスゼロイコールシー1という表記です。これはユーザー定義変数というものです。その前のセットコロンシー１カッコ５という文で、シー１というユーザー定義変数が今後5として扱われることを示しています。これを受けて、ソースセクションの中のシー１が5という数値として解釈されます。このように、同じ値を使う場合、あらかじめユーザー定義定数として定義しておくことで使いまわせます。
このユーザー定義変数は、シー１からシー99まで99個定義することができ、書いた場所から下ならどこでも使えます。一度定義した場所から下で、同じ変数を別の値に定義すると、その下では新しいほうの値で解釈されます。こうして使いまわせば実質的に99個以上の変数を使うことができます。
また、アイエヌエフエルコマンドと同様、セクションをオフにすると変数を定義したことも無視されてしまうので注意してください。
もう一つの便利な機能は数式です。PHITSの入力ファイルではフォートラン形式の数式表現を使うことができます。
例えば円周率パイは、ピーアイと書くことで定義なしに使うことができます。フォートラン形式では、べき乗はアスタリスク二つで表記します。また、初等数学関数のほとんど、コサインや指数関数のエクスポネンシャルを使うこともできます。これらを組み合わせれば、コサイン2分のパイなどを表記することができます。
さらに、アイエヌエフエルコマンドとユーザー定義変数セットを組み合わせると、エネルギーや幾何形状の長さなどインプットパラメータを連続的に変化させたインプットをスクリプトで連続自動実行させる、といった応用もできます。
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
利用できる関数一覧
SPEAKER_NOTES:
インプットファイル中で使える関数のリストです。三角関数、その逆関数、双曲線関数、指数対数、平方根など、実に多様な関数が使えます。

--- SLIDE 14 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
lec03.inp
文字列変数は
  set:%Variable_Name%[character]
  で定義
変数名は大文字・小文字を区別する
それ以外の仕様はユーザー定義変数と同じ
ユーザー定義文字列の利用
Version 3.31から文字列変数も利用可能
Rewrite (rwt) ファイル
文字列パラメータを置換した入力データがリライトファイル（*_rwt.inp）に出力される
最初のセクションの前に$RWT=0と書くと、リライトファイルを出力しなくなり初期設定時間が多少速くなる（ただし、文字列変数は使用不可）
$RWT=3と書くとリライトファイルを出力して計算終了
[ Source ]
set:%projectile%[proton]
  totfact =   1.0
   s-type =   2
      proj =  %projectile%
…

[ T-Track ]
…
part =  %projectile%
…
入射粒子の種類 と[t-track]でタリーする粒子の種類を連動させる
SPEAKER_NOTES:
バージョン3.31から、ユーザー定義文字列をユーザー定義変数と似た方法で使うことができます。
ユーザー定義文字列はこのインプットでは、入射粒子、すなわちプロジェクタイルの名前に使われ、このようにセット、パーセント、プロジェクタイル、パーセント、プロトンと定義しておけば、入射粒子の種類とティートラックでタリーする粒子の種類を常に統一することができます。
ユーザー定義文字列が定義されたとき、PHITS内部ではそれらを中身の文字列と置き換え、元のファイル名にアンダーバー アール ダブリュー ティー ドット アイエヌピーを加えた一時ファイルに書き出します。アール ダブリュー ティー イコール ゼロを最初のセクションの前に書くと、この一時ファイルの生成をやめることで、計算の初期化時間を短縮できますが、ユーザー定義文字列は使えなくなります。
同じインプットファイルを何度も使う場合に計算時間を節約するには、アール ダブリュー ティー を ３としてください。PHITSはユーザー定義文字列を変換した後のファイルを作って止まります。この変換後のファイルを使えば、変換に時間を使うことなく、計算を実行できます。
MENTIONED_INPUT_NAMES: _rwt.inp, lec03.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
onion.inp
[material]で@物質名@と定義するだけで、その物質の重量密度が自動で定義される
それ以降の行で文字列変数%物質名%が物質番号として使える

既定物質の密度は重量密度で定義されているため、[cell]では常に密度0とすればよい
既定物質はdata/predefined_material.datに定義されている
１つの物質に様々な物質名(alias）が登録され、エディタの補完機能から選択可能
既定物質の利用
Version 3.37から既定物質が利用可能
物質の組成や密度を調べるのが手間…
[cell]セクションだけを見ても、どの領域が何の物質か分からない…
[material]で定義した物質番号を覚えるのが大変…
例: mat[1] @GOLD@
mat[1] au -19.32
set:%GOLD%[1]
置換
熱中性子散乱測や阻止能データベースも使われるため、計算精度が高くなる場合もある
[ Material ]
mat[1]  @GOLD@
mat[2]  @WATER@
mat[3]  @COPPER@
mat[5]  @POLYETHYLENE(0.94)@
mat[6]  @AIR_DRY@
…
 [ Cell ]
 100  -1       10
 101  %GOLD% 0   -11
 102  %WATER% 0   11   -12
 103  %COPPER% 0  12   -13
 104  %WATER%  0  13   -14
 105  %POLYETHYLENE(0.94)% 0 14 -15
 106  %AIR_DRY% 0 15   -10
SPEAKER_NOTES:
また、このユーザー定義文字列機能を応用して、物質の組成や密度を調べるのが手間、セルセクションだけ見てもどの領域が何の物質が分からない、マテリアルセクションで定義した物質番号を覚えるのが大変、という声に応えるため、Version 3.37から既定物質の利用が可能となりました。
この機能を使えば、マテリアルセクションでアット物質名アットと定義するだけで、その物質の重量密度が自動で定義され、それ以降の行で文字列変数パーセント 物質名 パーセントが物質番号として使えるようになります。例えば、マット括弧１ アット ゴールド アットと定義すると、それがこのように置換されます。既定物質の密度は重量密度で定義されているため、セルセクションでは常に密度０とすればよいです。また、既定物質は、データフォルダのプレデファインド マテリアル ドットダットファイルに定義されており、１つの物質に様々な物質名、通称エイリアスが登録され、フィッツパッドやノートパッドプラスプラスなどエディタの補完機能から選択可能です。
MENTIONED_INPUT_NAMES: onion.inp

--- SLIDE 16 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
set: c1[5]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 =  -30.0
 z1 =  -30.0
 dir =  1.0
課題1
玉ねぎ体系全体を覆うように、ビームの幅を拡げてみましょう。
半径25cmの球を覆うことができるように、ビームの幅を拡げてみよう
ユーザー定義定数c1の値を大きくする
lec03.inp
角柱形状の線源
(s-type=2)
track_xz.eps
x軸とy軸に関して1辺10cmの正方形を発生領域とし、+z軸をビームの方向とする線源
SPEAKER_NOTES:
では実習で使い慣れてみましょう。
課題１は、ユーザー定義変数の設定についてです。基礎実習3のインプットファイルは、インクルードファイルにより半径25センチの、玉ねぎのような5層の球の体系を取り込んでいます。ただ、ビームはエスタイプ2の角柱状線源で、その幅はユーザー定義変数の通り上下5センチしかありません。そこで、ユーザー定義変数c1を大きくすることでビームの幅を広げて、玉ねぎ体系を覆ってみましょう。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-2.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
set: c1[25]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 =  -30.0
 z1 =  -30.0
 dir =  1.0
課題1の答え合わせ
玉ねぎ体系全体を覆うように、ビームの幅を拡げてみましょう。
lec03.inp
角柱形状の線源
(s-type=2)
track_xz.eps
発生領域となる正方形の1辺の長さを50cmをとすることで玉ねぎ体系を覆うことが可能となった
SPEAKER_NOTES:
課題１の答え合わせです。ソースセクションの上、セットと書かれている行で、5だったところを25に書き直します。すると、シー1は25として解釈され、ビームは玉ねぎの端であるマイナス25センチからプラス25センチに広がり、幅が上下左右とも50センチになります。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-2.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
実習内容
計算モードの選択
便利な入力補助機能
統計的に信頼できる結果を得るための設定
モンテカルロ積分を使った体積・面積計算
試行回数と統計誤差
計算結果の規格化
物理的に信頼できる結果を得るための設定
断面積データライブラリの利用
物理モデルの選択
まとめ
SPEAKER_NOTES:
では次に統計精度の上げ方についてお話をしていきます。

--- SLIDE 19 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
体積、面積計算の必要性
mesh=regとして各領域毎の物理量を計算するタリーの場合、その領域の体積や表面積を計算しておく必要があります*。
＊各領域の体積は[volume]セクションで、表面積は[t-cross]の”area”で与えることができます。
指定した領域の
単位体積あたりの熱量は？
指定した表面の
単位面積あたりの粒子フルエンスは？
指定した領域が球や円柱などであれば解析的に計算可能。
しかし、複雑な形状の場合はどうすれば良いだろうか？
→ PHITSを用いてモンテカルロ積分を行う
SPEAKER_NOTES:
統計精度について考えるために、ここでは体積や面積の計算を例にとって説明していきます。
エックスワイゼッドメッシュの場合、メッシュは碁盤の目になりますので、体積や面積の計算は簡単です。しかし、領域メッシュの場合、球や直方体を組み合わせた複雑な図形は、体積がわからないことが多いです。一方で、領域の単位体積当たりの熱量や、面積当たりのフルエンスを計算するには、PHITSに体積や面積を教えてあげる必要があります。
その体積をPHITSを使ってモンテカルロ積分により計算することができます。

--- SLIDE 20 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
モンテカルロ積分
乱数を用いて定積分の近似解を求める方法。積分範囲の内か外かを判定することにより、積分値を確率的に概算する。計算精度は試行回数に依存する。
a cm
a cm
1辺a cmの正方形の的を用意し、その的の内部にランダムに点を打って、色の付いた部分に当たれば+1点とする。

試行回数を増やすと、総得点を試行回数で割った値は、的の中で色の付いた部分の割合に近づいていく（左の例の場合は1/2）。これに的の面積（a2）を掛けると、色の付いた部分の面積（a2/2）を概算することができる。
この手法で任意の形状の面積を概算することができます。
また、この考え方は3次元にも拡張でき、体積も概算できます。
https://youtu.be/9_bs6g0n3Hg
参考動画「Dr.サトーと学ぶ放射線科学シリーズ①モンテカルロ法をサイコロで科学する」
SPEAKER_NOTES:
モンテカルロ積分、という方法を聞いたことがあるでしょうか。
乱数を使って定積分、つまり面積や体積ですが、その近似解を求める方法です。ランダムに点を打って、積分範囲の中か外かを判定することで、積分値を確率的に計算します。ランダムに点を打つ以上、その試行回数が少ないと不正確になります。
例えば一辺がエイセンチメートルの正方形の的を用意し、その的の内側にランダムに点を打つことを考えます。もし色のついたところに当たれば一点としてカウントします。
試行回数を増やしていくと、点を打った全回数のうち、色のついたところに当たった点数は、この場合8割る14で、正解の二分の一に近い値です。これに的の面積エイ二乗を掛けると、面積が概算できます。
この例題の場合はただの四角で簡単ですが、もっと複雑な形でも使えますし、3次元に拡大して体積を計算することもできます。

--- SLIDE 21 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
PHITSによる体積計算の原理
PHITSでは[t-volume]を使うことにより，自動的にモンテカルロ積分法を用いて各領域の体積を概算する機能がある
的
線源領域
線源と的の間に全ての領域が含まれるように線源を設定する
全ての相互作用（核反応・電離）は自動的に起きないようになる
求める体積 [cm3]
線の長さの合計（総得点）[cm]
線の密度[/cm2]
線の長さの合計（総得点）[cm]
試行回数 / 線源領域[cm2]
＝
＝
SPEAKER_NOTES:
実際、PHITSで体積を計算する場合、ランダムに点を打ったり集計したりするモンテカルロ積分の操作は、ティーボリュームタリーで自動化して行えます。目標の物体全体をカバーするように、物体による散乱を受けない仮想的な放射線を出し、物体の中を通っているときの線の長さは、ティートラックタリーに相当する機能を使って計算します。

--- SLIDE 22 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2
玉ねぎ体系の各層の体積を計算してみよう。
icntl = 14（体積計算モード）としてPHITSを実行
volume.outをテキストエディタで開いて確認
lec03.inp
各層の体積はどの位になるだろう？
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
…

[ T - V o l u m e ]
     mesh =  reg
     reg = 101 102 103 104 105
     file = volume.out
     s-type =    2
     x0 = -c1
     x1 =  c1
     y0 = -c1
     y1 =  c1
     z0 = -c1
     z1 =  c1
修正して実行
体積積分をする範囲
→直方体線源
SPEAKER_NOTES:
ではこのティーボリュームタリーを実際に使ってみましょう。
今使っているインプットの玉ねぎ体系で、各層の体積を計算するというのがこの課題です。
Icntlを14に変えて、実行してみましょう。このとき、PHITSは14番、体積計算モードとして走り、ティーボリュームタリーだけが実行されます。仮想的な放射線を出す線源は直方体で、マイナスシー1からプラスシー1までの範囲をカバーします。
実行後、ティーボリュームタリーの出力であるボリュームドットアウトファイルを開いてみましょう。各層の体積はどれくらいになるでしょうか。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-3.inp

--- SLIDE 23 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
体積計算の結果
モンテカルロ積分の要領で体系の体積を求めることが可能
[ V o l u m e ]
 non      reg      vol      non
    1      101   5.6046E+02  0.1791
    2      102   4.0305E+03  0.0836
    3      103   9.6478E+03  0.0540
    4      104   1.9110E+04  0.0360
    5      105   3.0618E+04  0.0224
volume.out
各層の体積は？
4π(5)3/3=524 cm3
4π(10)3/3 - 524=3665 cm3
4π(15)3/3 - 4189=9948 cm3
4π(20)3/3 - 14137=19373 cm3
4π(25)3/3 - 33510=31940 cm3
内側の結果ほど一致していない
→ 統計量が十分ではない
→ 統計量を増やすには？
SPEAKER_NOTES:
課題二の答えです。ボリュームドットアウトファイルを下に進むと、カッコボリュームで始まる部分があり、モンテカルロ積分で計算された体積が表示されています。
ここで考えるべきは本当の答えです。球や球殻の場合、その体積は解析的に求めることができます。そうやって計算した右側の体積は、モンテカルロ積分で求めた値と合いません。一番内側を例にとると、524立方センチになるべきところ、計算値は560立方センチ、PHITSのバージョンによってはもっと違う値になっているかもしれません。この乖離の原因はモンテカルロ計算の統計が足りないせいです。そこで、統計をどうやったら改善できるか考えてみましょう。

--- SLIDE 24 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
実習内容
計算モードの選択
便利な入力補助機能
統計的に信頼できる結果を得るための設定
モンテカルロ積分を使った体積・面積計算
試行回数と統計誤差
計算結果の規格化
物理的に信頼できる結果を得るための設定
断面積データライブラリの利用
物理モデルの選択
まとめ
SPEAKER_NOTES:
試行回数によって統計誤差をどうやって下げられるか、説明していきます。

--- SLIDE 25 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
試行回数（ヒストリ数）の設定
モンテカルロ計算の統計精度は、シミュレーションの試行回数に依存しています。したがって、信頼できる計算結果を得るためには、十分な数の試行回数を設定する必要があります。
maxcas ×maxbch ＝全試行回数
SPEAKER_NOTES:
試行回数はヒストリー数とも呼ばれ、モンテカルロ計算の統計精度を決めています。信頼できる計算結果を得るためには、十分なヒストリー数が必要で、PHITSでは二つのパラメータ、マックスキャスとマックスバッチの二つの入力パラメータで決めます。マックスキャスは一バッチ当たりのヒストリー数で、マックスバッチはバッチを繰り返す回数です。この二つの掛け算がヒストリー数になります。

--- SLIDE 26 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
ヒストリーとバッチの関係
Q. ヒストリー数とは？
   [source]セクションで指定した線源を発生させる回数

Q. バッチ数とは？
  ある一定のヒストリー数（maxcas）を束（バッチ）にして，その束を実行する回数（maxbch）
Q. 各バッチの終了時には何をするの？
   タリーの結果を取りまとめて平均値や統計誤差を導出し，途中経過を出力する*
Q. なぜ束（バッチ）に分けるの？
  → 一気に全てのヒストリー数を実行すると，何か間違っていたときに再計算が大変！
   → 各ヒストリー終了時に統計処理をすると，計算時間が掛かりすぎてしまう
統計処理の時間が気にならない程度に，maxcasとmaxbchを調整する
例）1バッチ当たりの計算時間を2～3分にする
*画像ファイルも出力するにはitall = 1と設定する
SPEAKER_NOTES:
ここで疑問が生じます、なんでヒストリー数、という一つのパラメータでなく、二つもパラメータがあるのでしょうか。
まずヒストリー数とは、ソースセクションで指定した線源から粒子を発生させる回数です。
そして、先ほど説明したバッチとは、ヒストリーを一定数まとめたものです。ヒストリーを一個にまとめずに、分けて実行するためにバッチというものがあるのですね。
ではなぜ分けて実行するのでしょうか。実は、各バッチの終了時には、タリーの結果を取りまとめて平均値や統計誤差を導出し、途中経過を出力します。
この途中経過の出力をする理由は、時間を無駄にしないためです。もし例えば一週間かかる計算を一気にすべて実行すると、間違っていた場合に気づくのは一週間後です。とはいえ、ヒストリー一つごとに途中経過を出力したら、途中経過の計算をするせいで遅くなります。
そのため、途中経過を出す統計処理の時間が気にならない程度に、マックスキャスとマックスバッチを調整してください。こうしたテスト計算なら一バッチ当たり数分がいいですし、業務で使う本格的な計算は一バッチ当たり数時間くらいにするのがよいと思います。

--- SLIDE 27 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
[ V o l u m e ]
 non      reg      vol      non
    1      101   5.6046E+02  0.1791
    2      102   4.0305E+03  0.0836
    3      103   9.6478E+03  0.0540
    4      104   1.9110E+04  0.0360
    5      105   3.0618E+04  0.0224
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
lec03.inp
volume.out
統計誤差
（相対誤差）
課題3
統計精度を高めるために、試行回数を増やしてみましょう。
maxcasを1,000や10,000に増やす
統計誤差が小さくなっていることを確認する
試行回数を10倍にすると誤差の値はどの程度小さくなるか？
SPEAKER_NOTES:
では統計精度がどのように改善するのか、試行回数を増やして調べてみましょう。マックスキャスは最初100ですが、これを千に増やしてみましょう。そして、ボリュームドットアウトを開いて結果を見直します。体積の右側に書き出される統計誤差はどのように変化するでしょうか。
さらに、マックスキャスを一万に増やした場合、統計誤差はどれくらい下がるでしょうか。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-4.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
[ V o l u m e ]
  non      reg      vol      non
    1      101   4.1549E+02  0.2106
    2      102   3.3346E+03  0.0922
    3      103   9.9239E+03  0.0541
    4      104   1.8974E+04  0.0361
    5      105   3.0770E+04  0.0222
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 100
  maxbch = 10
  file(6) = phits.out
lec03.inp
volume.out
課題3の答え合わせ
統計精度を高めるために、試行回数を増やしてみましょう。
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 1000
  maxbch = 10
 file(1)  = c:/phits
 file(6) = phits.out
[ V o l u m e ]
  non      reg      vol      non
    1      101   5.4065E+02  0.0578
    2      102   3.7146E+03  0.0275
    3      103   9.8763E+03  0.0170
    4      104   1.9252E+04  0.0112
    5      105   3.1481E+04  0.0068
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 10000
  maxbch = 10
  file(6) = phits.out
[ V o l u m e ]
 non      reg      vol      non
    1      101   5.3264E+02  0.0185
    2      102   3.6575E+03  0.0088
    3      103   9.9620E+03  0.0054
    4      104   1.9343E+04  0.0035
    5      105   3.1887E+04  0.0021
試行回数と統計誤差の関係
試行回数を増やすと正解に近づく
試行回数を10倍する毎に、誤差はおよそ1/√10になる
PHITSで出力する誤差は全て1σ （約68%の確率でその範囲内に計算結果が入る）
4π(5)3/3=524 cm3
4π(10)3/3 - 524=3665 cm3
4π(15)3/3 - 4189=9948 cm3
4π(20)3/3 - 14137=19373 cm3
4π(25)3/3 - 33510=31940 cm3
正解
（解析解）
必ずその範囲内に真値があるわけではないことに注意！
SPEAKER_NOTES:
課題三番の答えです。マックスキャスを増やすと、統計誤差が減っていったのがわかると思います。一番内側の球の体積も524立方センチにずいぶん近い値になり、結果が本当に正確になったこともわかります。
試行回数や統計誤差は、理論上次のような性質があります。まず、上でみたように試行回数を増やすと正解に収束していきます。その速さは、試行回数を10倍するたびに、誤差がルート10ぶんの１になります。また、PHITSの誤差は1シグマですので、約68パーセントの確率でその範囲内に正解が収まるということです。つまり、誤差の範囲内に必ず正解があるわけではないことに注意してください。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-4.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
lec03.inp
再開始計算
統計量が足りない場合に、過去のタリー結果を読み込んで、続き計算を行うことが可能です。
再開始計算が実行された場合、コンソール画面にメッセージが表示されます。
計算が終了した各バッチの情報も出力されます。
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 10000
  maxbch = 10

 file(6) = phits.out
 istdev = -2
istdev=-2を加えて、再開始計算を実行してみましょう！
SPEAKER_NOTES:
再開始計算という便利な機能についてもお話しておきます。
例えば一週間の計算を行ったのに、その結果の誤差が大きくて、もっと計算を続けたいとします。そこまでの一週間を無駄にするのは勿体ないですね。こんな時、インプットのパラメータセクションでアイエスティーディーエーブイというパラメータをマイナス１にします。すると、PHITSはそれまでのタリー結果を読み込んで、その続きとして計算を行います。もしもう一週間計算をすると、二週間分の計算ができるということです。
再開始計算を行った場合、コンソール画面に、これは再開始計算です、という旨のメッセージが出て、各バッチの情報が続きます。この後ろに、最初の乱数が、というメッセージが続きますが、この意味は次で説明します。
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
乱数について
PHITSの乱数は，疑似乱数*でその周期は264-1(~ 1019)
初期設定（デフォルト）では，結果に再現性を持たせるため常に同じ乱数を発生
 （再開始計算を行わない限り，何度計算しても同じ結果を出力）
264-1
スタート
再開始計算
SPEAKER_NOTES:
そもそもPHITSで使っている乱数の説明をしていませんでしたね。皆さんの中には、「PHITSは乱数を使ったモンテカルロ計算なのに、なんで私の計算結果は毎回同じなのだろう」と思った方もいるかもしれません。
それは、PHITSが疑似乱数、という乱数を使っているからです。疑似乱数とは、数とその次の数の間はバラバラですが、そのバラバラな数をアルゴリズムで人為的に作っているからです。皆さんのコンピュータで、常に同じアルゴリズムを使っていますので、乱数もその計算結果も同じなのです。
PHITSで使っているアルゴリズムは、2の64乗、つまり約10の19乗のサイクルで続く乱数を使っています。そして、計算結果の再現性を確保するため、デフォルトの設定では同じ数から乱数を始めています。
最初の乱数はアールシードというパラメータで指定でき、デフォルトが6.647299061401かける10の12乗という数です。もしアールシードを適当な数、例えば10にすると、10という数が最初の乱数になります。
ここで再開始計算の話に戻ると、再開始計算の場合何らかの初期乱数から計算をはじめて、一回分の計算をするとその分だけ乱数を使用します。そこで再開始計算をすると、前回の計算の最後の乱数を初期乱数として計算を続けます。そのあとさらに再開始計算をすると、前回の乱数を引き継ぐので、さらにその先を計算します。結果的に、最初から3倍の長さの計算をしたのと完全に同じ計算になりますし、乱数には重複がなく、すべて有効な計算です。つまり再開始計算は、乱数の重複を気にせずやっていい、ということです。

--- SLIDE 31 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
バッチ計算の活用
PHITSでは、タリーの結果を各バッチが終了する度に出力させることができ、それを見ながらモンテカルロ計算を中断することができます。
440 <--- Number of remaining batches

-------------------------------------------------------------------------------
bat[     560] ncas =            560. : rijk    = 151264979546685.
       low neutron =              0. : ncall/s =  4.000000000E+00
          cpu time =   0.288 s.

 date = 2012-05-02
 time = 15h 08m 25
最初の数字は残りバッチ数。この数字を書き換えることにより、残りのバッチ数を減らすことができる。例えば、0に書き換え保存すると、その時のバッチを最後に計算をやめる。
batch.out
SPEAKER_NOTES:
次にバッチファイルの使い方を覚えておきましょう。
先ほどご説明したように、PHITSは計算を複数のバッチに分けて行い、そのバッチ終了時に出力されるタリーの結果を見て、計算を終了することもできます。もちろん、コンソール画面でコントロールとシーを押すなど、PHITSの計算を強制終了することもできますが、ここで説明する方法ならPHITSドットアウトファイルなど、計算結果をすべて完全に得ることができます。
その中断の方法というのがバッチドットアウトファイルの最初の数字を書き換えるというものです。この数字は、まだ残っているバッチの数を意味していて、これを0にすれば、今走っているバッチが終わったときに、計算を終了します。

--- SLIDE 32 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 14
   maxcas = 10000
  maxbch = 1000000

  file(6) = phits.out
 $ istdev = -2
lec03.inp
istdevの行は$マークでコメントアウト（再開始計算は行わない）
maxbchを106に増やして長時間の計算を実行
volume.outを開いて結果が更新されていることを確認
batch.outを開いて1行目を0として計算を中断
課題4
batch.outを使って、計算を中断させてみましょう
注意：いくつかのエディタ（SakuraエディタやCotEditorなど）は，ファイルを占有したり自動更新してしまうため，batch.outをうまく修正できない可能性があります。その場合は，標準エディタ（ノートパッド for Windows、テキストエディット* for Mac）を使って編集して下さい。
batch.outを用いて計算を終了させた場合
Macの場合、batch.outのアイコンをコントロールキーを押しながらクリックして，「このアプリケーションで開く」から「テキストエディット」を選択
SPEAKER_NOTES:
課題４では、バッチドットアウトを使って計算を中断してみましょう。この実習はタイミングが複雑なので、この解説と同時にやってみましょう。まず、アイエスティーディーエーブイは計算を複雑にするのでコメントアウトします。また、計算の途中で操作をしたいので、マックスバッチを1000や100万など大きな数にして、計算時間を長くします。この二つが終わったら計算を開始します。
ボリュームドットアウトを開いて、計算結果が次々更新されていることを確認します。そうしたら、バッチドットアウトを開いて、一行目の初めの数字を０に書き換えます。すると、その時走っているバッチが終わってすぐ、PHITSは計算終了します。計算を止めることができたら、コンソール画面に計算がバッチドットアウトによって終了したことが表示されます。
もし中断する前に計算が終わってしまったなら、もう一度試しましょう。インプットファイルを使ってPHITSを実行し、バッチドットアウトを開き、最初の数字を０にします。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-5.inp

--- SLIDE 33 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
[ P a r a m e t e r s ]
   icntl = 14
  maxcas = 10000
  maxbch = 1000
…
[ T - V o l u m e ]
     mesh =  reg
     reg = 101 102 103 104 105
     file = volume.out
     s-type =    2
     x0 = -c1
     x1 =  c1
     y0 = -c1
     y1 =  c1
     z0 = -c1
     z1 =  c1
    stdcut = 0.01
lec03.inp
タリーの結果の統計誤差が全て指定値以下になった場合に計算を自動で終了
各タリーに対してそれぞれ指定可能（全てのタリーに対して条件を満たした場合のみ終了）
課題5
stdcutを使って、統計誤差が十分小さくなったら自動で計算を中断させてみよう
stdcutパラメータとは？
stdcutで計算が終了した場合
SPEAKER_NOTES:
計算を途中で止めるには、もう一つ方法があって、統計誤差がある値になったときに自動停止させる機能があります。それがエスティーディーカットです。
エスティーディーカットというパラメータは、タリーに入れることができ、タリーの統計誤差がエスティーディーカットで指定した値より小さくなった場合、そこで計算を止めます。つまり、計算精度が十分よくなった、とみなせる場合に計算を止めるということです。エスティーディーカットは複数のタリーに入れることもでき、その場合全部のエスティーディーカットの条件が満たされた場合に計算は停止します。つまり、収束の遅いタリーにエスティーディーカットを使うと、そのタリーのため計算がなかなか終わらないということがあり得ます、注意してください。
では、ティーボリュームセクションに、エスティーディーカットを0.01として入れてみましょう。この状態で実行して、ティーボリュームのアウトプットを見たとき、統計誤差が0.01以下になっていることを確認してください。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-6.inp

--- SLIDE 34 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
PHITSの並列計算は，メモリ共有型（OpenMP）とメモリ分散型（MPI）があります
MPIは別途MPIプロトコルをインストール*する必要がありますが，OpenMPは別ソフトをインストールの必要はありません。ただし，同じ並列数であればMPI版の方が計算時間が短くなります。
インプットファイルの最初のセクションの前に「$OMP=並列数」もしくは「$MPI=並列数」と書けば並列計算版が動作します**
$OMP=0とすると，全てのCPUコアを使って並列計算します。ただし，PCの動作が重くなる場合があるのでご注意ください
並列計算
並列計算の注意点
Linuxの場合には、libiomp5.soのライブラリが必要とされる場合があります。PHITSマニュアルの2.3.3に従ってインストール&設定を行って下さい。
*WindowsでのMPIプロトコルインストールはphits/document/Install-IntelFortran-OneAPI-en.pdfを参照
**PHITSの実行ファイルを直接実行する場合を除く。Mac版は「$OMP」のみ有効
SPEAKER_NOTES:
ここまで、長い計算でも途中で終わらせる方法があることを説明してきました。では長い計算を速くすることはできないのでしょうか。そのために、並列計算という技術があります。PHITSでは、オープンエムピーというメモリ共有型と、エムピーアイというメモリ分散型の二つの並列計算方法が使えます。メモリ分散型の並列、エムピーアイは、プロトコルをインストールする必要があるため、少し難易度が高いです。一方オープンエムピーは、ごく一部の例外を除いて、追加のインストールが必要なく今すぐ使えるため簡単です。オープンエムピーの弱点は、エムピーアイに比べると並列化の効率が低く、同じコア数ならエムピーアイのほうが計算が早いです。
オープンエムピーは、インプットの一番初めにドル オーエムピー イコール数字と記入することにより使うことができます。この数字は使いたいコア数で、この数字を０にすると、コンピュータのコアすべてを使いますが、ほかのプログラム、テキストエディタやメールなども遅くなりますので、気を付けてください。
オープンエムピーが使えないごく一部の例外というのは、32ビット版ウインドウズと、一部のリナックスマシンです。リナックスは環境によってリブアイオーエムピー５ドットエスオーというライブラリファイルが足りず、オープンエムピーが実行できない場合がありますので、PHITSのマニュアルに沿って設定してください。

--- SLIDE 35 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
$OMP = 4
[ T i t l e ]
・ ・ ・ ・ ・ ・
lec03.inp
追加課題
1行目に$OMPを設定して並列計算を実行しよう
最初と最後にOpenMPに関するメッセージが出力される
SPEAKER_NOTES:
インプットの1行目にドルオーエムピー イコール 4と書いて実行してみると、こんな風に計算が並列化します。コンソールの初めのほうにオープンエムピーパラレルプロセスが１から４まで実行されていることが表示され、計算の最後にオープンエムピーパラレルプロセスをすべて一個ずつ終了したことが表示されます。このような短い計算では並列化の効率を感じられませんが、もっと長い計算になるとこの計算加速は大変役に立ちます。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-2.inp

--- SLIDE 36 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
実習内容
計算モードの選択
便利な入力補助機能
統計的に信頼できる結果を得るための設定
モンテカルロ積分を使った体積・面積計算
試行回数と統計誤差
計算結果の規格化
物理的に信頼できる結果を得るための設定
断面積データライブラリの利用
物理モデルの選択
まとめ
SPEAKER_NOTES:
基礎実習３前半の最後に、計算結果の規格化についてご説明します。

--- SLIDE 37 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
set: c1[25]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 =  -30.0
 z1 =  -30.0
 dir =  1.0
lec03.inp
規格化について
PHITSのタリー結果は，発生する線源１個あたり*)で出力される（maxcasやmaxbchに比例して大きくなるわけではない）
測定値などと比較するには，Bqや/cm2/sで表される線源の発生頻度で規格化する必要がある
タリー結果を定数倍（totfactで定義）することにより，直接， /cm2/sやmGy/hなどの単位に換算した値を出力できるようになる
*)厳密には１ウェイトあたり
SPEAKER_NOTES:
これまで行ってきた計算は、入射してきた粒子一個あたりに規格化した結果を出していました。つまり、マックスキャスやマックスバッチで線源から出てくる粒子を増やしても、計算結果はマックスキャスとマックスバッチで割るので、値が大きくなっていくわけではありません。むしろある一定の収束値に向かっていきます。
しかし、実験値などを比較する場合は、線源が何ベクレルであるか、もしくはビームなら何粒子パー平方センチメートル パー秒の強度であるか、などを考慮した、結果の絶対的な大きさが重要ですね。そういう場合、線源から出てくる粒子の数を表すトトファクトというソースセクションのパラメータを設定することで、結果をそれによってグレイパーアワーなどの実測値と比べられる値に規格化できます。
MENTIONED_INPUT_NAMES: lec03.inp

--- SLIDE 38 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
吸収線量を絶対値で評価
玉ねぎ球に150MeVの陽子ビームを一様に照射します。ビームフラックス（流束）を1cm2・1秒あたり106個とし，そのビームを1時間照射した場合の各層の吸収線量を計算しましょう。
150MeVの陽子が1cm2・1秒あたり106個の割合で1時間照射される
吸収線量は何Gy？
SPEAKER_NOTES:
ここでは、玉ねぎ体系に陽子を照射し、その吸収線量を絶対値で計算してみましょう。
玉ねぎに150メガエレクトロンボルトの陽子ビームを、一平方センチメートル当たり、かつ一秒あたり10の6乗個のフラックスで一様に照射して、一時間当て続けるとします。その場合の吸収線量は何グレイになるでしょうか。

--- SLIDE 39 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題6
まずは，陽子を1個照射あたりの平均吸収線量を計算しよう
[ P a r a m e t e r s ]
   icntl = 0
  maxcas = 2000
  maxbch = 5
…

[ S o u r c e ]
…
infl: {onion.inp}[1-31]
$ infl: {volume.out}
…

[ T - Deposit ]
  title = Deposition energy in reg mesh
  mesh =  reg
  reg = 101 102 103 104 105
  unit =    0    # unit is [Gy/source]
lec03.inp
icntl = 0 として通常モードとする（[source]セクションは変更の必要なし）
maxcasとmaxbchを2000と5に減らす（計算時間を短縮するため）
$infl:{volume.out}の$を削除し，icntl=14で計算した[volume]セクションを読み込む（これがないと各領域の重さが分からない）
[t-deposit]のoffを削除する
PHITSを実行しdeposit.outを確認する
SPEAKER_NOTES:
課題６と７で、実際にやってみましょう。課題６ではまず、陽子一個の照射に対する吸収線量を計算します。課題６が終わったら、陽子のフラックスを考慮して規格化する課題７に進んでください。
まずアイシーエヌティーエルを0にして、通常の輸送計算にします。
計算時間を節約するため、マックスキャスとマックスバッチはそれぞれ2000と5にしましょう。
吸収線量は、エネルギー付与量を標的の質量で割る必要があるので、PHITSに標的の大きさを教えてあげる必要があります。そのため、コメントアウトを外して、ボリュームドットアウトを読み込むアイエヌエフエルコマンドを有効にします。
最後にティーデポジットのオフを外して、吸収線量を計算できるようにしましょう。この状態で、PHITSを実行してください。
MENTIONED_INPUT_NAMES: lec03.inp, onion.inp
ANSWER_FILE: input/onion.inp

--- SLIDE 40 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題6の答え合わせ
（29行目あたり）
#  num    reg     volume       all       r.err
    1     101   5.2465E+02   3.7110E-16  0.2021
    2     102   3.6454E+03   1.8475E-15  0.1577
    3     103   9.9378E+03   2.5310E-14  0.0194
    4     104   1.9364E+04   2.8606E-13  0.0116
    5     105   3.1919E+04   3.2218E-13  0.0086
deposit.out
track_xz.eps
PHITSの計算結果は，基本的には線源１個発生当たりに規格化される
陽子1個照射あたり，一番外側の層でも3.2E-13(Gy) = 0.32 pGyしか吸収線量がない
内側の層は1次陽子が届かないため，さらに3桁ほど吸収線量が低い
SPEAKER_NOTES:
課題６の結果はこのようになります。
この計算結果は、線源の粒子一個あたりに規格化されていて、陽子一個当たり一番外の層で約0.32ピコグレイしか線量がありません。内側の層になると、さらに3桁程度少ない線量になります。
ANSWER_FILE: input/lec03-7.inp

--- SLIDE 41 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
課題7
フラックス106(/cm2/s)で1時間照射したときの吸収線量は？
フラックスが1cm2・1秒あたり106個の場合，線源面を1秒当たりに通過する陽子の数は？
  （線源面積は(2*c1)2cm2 = 2500 cm2）
そのフラックスで1時間照射した場合の合計発生陽子数は？
その陽子数を[source]セクションのtotfactパラメータで指定し，タリー結果を全てtotfact倍に規格化する
lec03.inp
set: c1[25]

[ S o u r c e ]
 totfact =   1.0
 s-type =   2
 proj =  proton
 e0 =   150.0
 x0 =  -c1
 x1 =   c1
 y0 =  -c1
 y1 =   c1
 z0 =  -30.0
 z1 =  -30.0
 dir =  1.0
SPEAKER_NOTES:
では課題7番に進みましょう。一平方センチメートル当たり、一秒あたり10の6乗のフラックスだった場合、一時間の照射で玉ねぎはどんな線量を受けるか、というのが問題です。
線源の面を一秒間あたりに通る陽子の数は、線源の面積が2500平方センチメートルであることから計算できます。さらに、一時間照射した場合に通る陽子の数は、時間が3600秒であることから計算できます。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-8.inp

--- SLIDE 42 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
課題7の答え合わせ
（29行目あたり）
#  num    reg     volume       all       r.err
    1     101   5.2465E+02   3.3399E-03  0.2021
    2     102   3.6454E+03   1.6628E-02  0.1577
    3     103   9.9378E+03   2.2779E-01  0.0194
    4     104   1.9364E+04   2.5745E+00  0.0116
    5     105   3.1919E+04   2.8996E+00  0.0086
deposit.out
track_xz.eps
totfactは，単純に全てのタリー結果を定数倍数する
一番外側の層は2.9Gy程度照射された
一番内側の層は4.3mGyしか照射されていないが，統計誤差が大きいため信頼できる結果ではない
lec03.inp
set: c1[25]

[ S o u r c e ]
 totfact = 1.0e6*(2*c1)**2*3600
…
totfact倍されている
（ただし，ラベルは変更されない）
計算したtotfactはphits.outで確認可能
SPEAKER_NOTES:
課題7番の結果がこちらです。一平方センチ、一秒あたり10の6乗の陽子が出ますから、線源の面積を考慮するには、2500センチメートル、つまりシー１の２倍の２乗を掛けます。さらに、一時間の照射なので、3600秒を掛けると、トータルの陽子の数を計算できます。
この条件で計算すると、一番外側の層は2.9グレイ程度の線量になります。一方、内側の層はPHITSのバージョンによって多少変わるものの、3桁程度少ない線量になります。ただこの値は統計誤差が大きく、あまり信頼できない結果です。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-8.inp

--- SLIDE 43 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
実習内容
計算モードの選択
便利な入力補助機能
統計的に信頼できる結果を得るための設定
モンテカルロ積分を使った体積・面積計算
試行回数と統計誤差
計算結果の規格化
物理的に信頼できる結果を得るための設定
断面積データライブラリの利用
物理モデルの選択
まとめ
SPEAKER_NOTES:
物理的に意味のあるシミュレーションを実行するためには、そのシミュレーションに適した物理モデルやデータライブラリを選択する必要があります。

ただ、PHITSでは、標準設定で既に、輸送粒子の種類やエネルギーに合わせて物理モデルやデータライブラリを適切に参照するような設定になっているため、ほとんどの場合においては、ユーザーが特に意識する必要はありません。

しかし、一部の目的や計算時間を出来るだけ短くしたい場合など、設定を変更したほうが良い場合も存在します。本講義では、標準設定がどうなっているのかということと、設定を変更する方法について説明します。

--- SLIDE 44 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
断面積データライブラリとは？
光子・電子・陽電子並びに低エネルギー中性子（20MeV以下）の断面積は，ターゲットやエネルギーに複雑に依存するため，画一的なモデルでは表現できない → 断面積データライブラリが必要
近年は、高エネルギー中性子（200MeV以下）、荷電粒子（陽子、重陽子、α粒子）、光核反応に対するライブラリ(JENDL-5）も整備されている
計算条件によって断面積データライブラリを使う粒子の種類やエネルギー範囲を [parameters]セクションで変更する必要があります
113Cdの中性子反応断面積（JENDL-4.0より）
*JENDL-5は、一部の粒子や元素に対してしかPHITSパッケージには含まれていません。全てのデータを利用するには、XSフォルダにあるjendl5_setupファイルを使ってダウンロード・設定する必要があります
SPEAKER_NOTES:
まず、断面積データライブラリについてです。

光子・電子・陽電子および低エネルギー中性子の反応は、ターゲットやエネルギーに複雑に依存するため、画一的モデルで表現することが困難です。例えば、右下の図はカドミウムに対する中性子の反応断面積を示したものですが、数十eVから数100eVの領域で、原子核の共鳴による反応断面積の激しい増減が見られます。この構造は同位体毎に異なりことが知られており、この様な構造を物理モデルで正確に再現することは、最新の原子核理論を持ってしても不可能です。

このため、PHITSでは原子核毎の断面積データをライブラリとして内包し、複雑なデータを直接使用して輸送計算を実行しています。PHITSのパッケージの容量の大部分を占めているのは、実はこの断面積データライブラリです。断面積データライブラリの使用に関する設定は、PHITSの入力ファイルのパラメータセクションで行います。

--- SLIDE 45 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
関連するパラメータ
negs
光子・電子・陽電子の輸送に関するオプション
-1: 光子のみ輸送する（PHITSオリジナルライブラリを用いる，デフォルト）
0: 光子・電子・陽電子の輸送を行わない
1: 光子・電子・陽電子を輸送する（EGS5ライブラリを用いる）
emin(i), i:粒子ID番号
各粒子のカットオフエネルギー。指定したエネルギー以下の輸送は行わない。計算時間を短縮したい場合や，高い空間分解能を必要とする計算で変更が必要となる。
dmax(i), i:粒子ID番号
断面積ライブラリを用いて輸送する粒子エネルギーの上限
JENDL-5など荷電粒子や高エネルギー中性子ライブラリを使う場合に設定
詳細な計算にはnegs=1が奨励！！*
*1GeV以上の高エネルギー光子・電子・陽電子を輸送したい場合はnegs = 2に設定
SPEAKER_NOTES:
各データライブラリを制御するパラメータとして以下のものがあります。

NEGSは光子・電子・陽電子の輸送およびデータライブラリの選択に関するパラメータです。-1の時には、光子のみをPHITSオリジナルライブラリで輸送し、0の時には、光子・電子・陽電子の輸送を行わず、1の時には光子・電子・陽電子をEGS5ライブラリを用いて輸送します。デフォルト値は-1、つまり電子が輸送されないように設定されています。これは、陽子や重イオン等の輸送の際に、大量に電子が発生し、計算時間が非常に長くなることを防ぐためです。ユーザーの興味が陽子や重イオンによる線量付与そのものにあるようであれば、電子の輸送を行わない近似で計算精度が十分であることがほとんどです。これに対し、電子の輸送も考慮したミクロな計算をするためには、電子の輸送設定が必須となるので、必ずNEGS=1を追加設定する必要があります。
EMINのパラメータは各粒子のカットオフエネルギーを設定するパラメータです。括弧に入る数字は粒子のID番号で、例えば1であれば陽子、２であれば中性子といった設定になっています。どの粒子が何のID番号になっているかは、PHITSのマニュアルを参照ください。カットオフエネルギーには、デフォルトで通常に用いられるべき設定が既に準備されています。
DMAXのパラメータはデータライブラリを用いて輸送を行う粒子エネルギーの上限値を設定するパラメータです。これ以上のエネルギーの粒子は、データライブラリではなく、物理モデルによって輸送計算が行われることになります。DMAXに関してもデフォルトで通常に用いられるべき設定が既に準備されています。

--- SLIDE 46 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
emin(i)とdmax(i)
*ただし、赤字の値はnegs=1とした場合
（negs = -1の場合は電子・陽電子については設定しません）
1mm以下の分解能で吸収線量を計算したい → emin(12, 13) = 0.001*
体系が大きいのでなんとか計算時間を短縮したい → emin(12, 13) = 1.0
高エネルギーの光子・電子・陽電子を輸送したい → dmax(12-14) = 1.0e5**
荷電粒子や高エネルギー中性子に対してJENDL-5を利用したい → dmax(1,2) etc.
変更が必要な計算例
*dmax(12-14)も粒子のエネルギーにあわせて小さくしてください
** negs = 2とすれば自動でdmax(12-14)を1.0e7に設定します
SPEAKER_NOTES:
EMAXとDMAXのデフォルトでの設定値です。カットオフエネルギーEMINからライブラリの上限値DMAXの間がデータライブラリによる輸送計算が行われるエネルギー範囲になります。
中性子に関しては低速中性子から20MeVまで、核データによる輸送計算が実行されるように設定されています。
電子・陽電子のカットオフエネルギーはデフォルトで100keVに設定されています。光子のカットオフエネルギーはデフォルトで1keVに設定されています。

このようにデフォルトで値が設定されているために、通常の計算では、EMIN、DMAXを明示的に設定する必要はありません。ただし、これから述べる例のように明示的に設定し、デフォルト値から変更したほうが良い計算例もあります。

例えば、1mm以下の分解能で吸収線量を計算したい場合には、電子の100keVのカットオフエネルギー値は高すぎるので、1keV程度の低いカットオフエネルギーに変更する必要があります。
体系が大きく、細かな分布等に興味がない場合は、逆にカットオフエネルギーを1MeVのように高く設定することで、計算時間を短くすることができます。
また、高エネルギーの光子・電子・陽電子を輸送したい場合や高エネルギー核データライブラリを使用したい場合には、データライブラリ使用の上限値DMAXを変更する必要があります。

--- SLIDE 47 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
入出力ファイルの設定
*インストーラを実行した際、環境変数PHITSPATHにインストールしたフォルダ名が設定されます。
インストーラを使用していない場合は、デフォルトがc:/phitsとなります。
SPEAKER_NOTES:
さらに、データライブラリを使用するにあたり、データパスの設定が必要になる場合があります。

データライブラリに関係するパスの設定には以下のようなものがあります。
File(1)にはPHITSをインストールしたフォルダを絶対パスで設定してください。
他のパスに関しては、File(1)に対する相対的なパスがデフォルトで設定されているので、PHITSの内部構造をユーザーが変更しない限り、特に設定する必要はありません。File(1)に関しても、インストーラーを使用してPHITSのインストールを行った場合は、環境変数に自動的にFile(1)の内容が登録されるため、File(1)の設定も必要ありません。インストーラーを使用せずにPHITSのインストールを行った場合にのみ、File(1)をパラメータセクションで指定する必要があります。

--- SLIDE 48 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
lec03.inp
課題8
EGS5を利用して、電子と陽電子を考慮した輸送計算を実行しましょう
[parameters]において、maxcas = 1000，maxbch = 1として計算時間を短縮する

線源を10MeVの光子とする
  （[source]において%projectile%と”e0”を変更）

[t-track]のpartに”electron  positron”を加える
[ P a r a m e t e r s ]
   icntl = 0
  itall = 1
  maxcas = 2000
  maxbch = 5
  file(6) = phits.out
$ istdev = -2
 negs =
[ T - T r a c k ]
mesh =  xyz
・ ・ ・ ・ ・ ・
part =  %projectile%
・ ・ ・ ・ ・ ・
file = track_xz.out
[ S o u r c e ]
set:%projectile%[proton]
・ ・ ・ ・ ・ ・
  e0 =   150.0
[parameters]においてnegs = 1を追加
PHITSを実行して電子・陽電子・光子のフラックスを確認（track_xz.epsの2ページ目以降）
PHITSを再実行して，電子・陽電子が輸送されていることを確認
SPEAKER_NOTES:
実際にデータライブラリのオン・オフを試してみましょう。

まず、現在の入力ファイルでは、計算時間がかかりすぎるので、試行回数を減らします。MAXCAS=1000とMAXBCH=1としてください。次に線源を変更します。sourceセクションを変更して、10MeVの光子として下さい。T-trackセクションのpartのパラメータにelectron, positron, photonを追加してください。
今まで表示されていた陽子の飛跡に加えて電子、陽電子、光子の飛跡のページが追加されます。

まず、この入力ファイルの状態でPHITSを実行させてみて下さい。Parameterセクションにnegsのパラメータの指定がないので、デフォルトの設定となり、光子のみが輸送される計算になります。実行が終わりましたら、track_xz.epsファイルの2ページ目が電子で、3ページ目が陽電子、4ページ目が光子の飛跡にになるので、確認して下さい。2ページ目、3ページ目には飛跡が見られず、電子、陽電子が輸送されていないことが確認できます。4ページ目では飛跡が確認でき、光子の輸送はちゃんと行われていることが確認できます。

次に、parameterセクションにnegs=1を追加してから再度PHITSを実行して下さい。電子、陽電子もEGSデータライブラリによって輸送されるようになるため、2ページ目、3ページ目にも飛跡が見られるようになります。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-9.inp

--- SLIDE 49 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
lec03.inp
課題8の答え合わせ
EGS5を利用して、電子と陽電子を考慮した輸送計算を実行しましょう
[ P a r a m e t e r s ]
   icntl = 0
  maxcas = 1000
  maxbch = 1
  file(6) = phits.out
$ istdev = -2
  negs = 1
track_xz.eps（2ページ目）
track_xz.eps（1ページ目）
光子から生成された電子・陽電子が輸送されている
電子フラックス
光子フラックス
[ T - T r a c k ]
mesh =  xyz
・ ・ ・ ・ ・ ・
part =  %projectile% electron positron
・ ・ ・ ・ ・ ・
file = track_xz.out
[ S o u r c e ]
set:%projectile%[photon]
・ ・ ・ ・ ・ ・
  e0 =   10.0
SPEAKER_NOTES:
NEGS=1のパラメータを追加することで、電子、陽電子も輸送されるようになり、2ページ目、3ページ目に電子、陽電子の飛跡が現れることが確認できます。光子の飛跡に関しては、NEGSのパラメータを追加する前の結果と統計的な違いを除いてほぼ同様な結果が得られていることも確認できます。低エネルギーの光子の輸送で光子のみの挙動に興味がある場合には、NEGSのパラメータ無しのデフォルトの計算で十分です。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-9.inp

--- SLIDE 50 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
lec03.inp
課題9
電子・陽電子を1keVまで輸送して，計算時間が長くなるのを体感しよう
[parameters]において、emin(12)とemin(13)を1 keV （= 0.001 MeV） と指定する
[ P a r a m e t e r s ]
   icntl = 0
  maxcas = 1000
  maxbch = 1

file(6) = phits.out
$ istdev = -2
 negs = 1
 emin(12) =
 emin(13) =
（emin(12)とemin(13)のデフォルトは100keV）
SPEAKER_NOTES:
次に、カットオフエネルギーを変更してみましょう。

デフォルトの設定では、電子、陽電子ともにカットオフエネルギーは100keVに設定されています。EMIN(12)とEMIN(13)を1keVと設定して、カットオフエネルギーを1keVに下げて計算を実行し、計算時間が長くなることを実感してみましょう。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-10.inp

--- SLIDE 51 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
lec03.inp
課題9の答え合わせ
[ P a r a m e t e r s ]
   icntl = 0
  maxcas = 1000
  maxbch = 1

  file(6) = phits.out
$ istdev = -2
 negs = 1
 emin(12) = 0.001
 emin(13) = 0.001
この分解能で見ると結果はほとんど変わらないが，計算時間だけ長くなる
（カラープロットの範囲が変わるので色は変わったように見える）
電子・陽電子を1keVまで輸送して，計算時間が長くなるのを体感しよう
参考：水中での100keV電子の飛程 ≒ 0.14 mm
track_xz.eps（2ページ目）
track_xz.eps（1ページ目）
電子フラックス
光子フラックス
SPEAKER_NOTES:
だいぶ計算時間が延びることが実感できたと思います。

ただ、飛跡の分布を見てみると、カットオフエネルギーが100keVだった場合と、あまり違いがないことがわかります。これは、水中の100keV電子の飛程が0.14mm程度であり、今回見ているスケールでは違いが見られないことを示しています。カットオフエネルギーを下げるとより低エネルギーの粒子輸送まで計算を追うことになるので、興味がある物理のスケールを考えて設定しないと余計な計算時間を生じてしまいます。逆に、興味のある物理スケールが大きい場合には、カットオフエネルギーを上げることで、計算時間を短くすることができます。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-10.inp

--- SLIDE 52 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
実習内容
計算モードの選択
便利な入力補助機能
統計的に信頼できる結果を得るための設定
モンテカルロ積分を使った体積・面積計算
試行回数と統計誤差
計算結果の規格化
物理的に信頼できる結果を得るための設定
断面積データライブラリの利用
物理モデルの選択
まとめ
SPEAKER_NOTES:
次に物理モデルの選択について説明します。

--- SLIDE 53 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
荷電粒子のビームライン設計オプション
nspred & nedisp: 荷電粒子の物質中での角度・エネルギー分散を考慮するためのオプション。加速器ビームのビームライン設計の際，不可欠となる。[Parameters]セクションに入力
ビームライン設計時の奨励値は nspred = 2 & nedisp = 1
（初期設定では共に0）
200MeV/u炭素線を水に照射した際の吸収線量の深さ分布（ブラックピーク付近を拡大）
SPEAKER_NOTES:
まず、荷電粒子のビームライン設計等のためのオプションについて説明します。

荷電粒子のビームは、物質中の元素との間の多重クーロン散乱等の影響で空間的にもエネルギー的にも拡がります。PHITSでは、モデルを用いて、これらの角度分散およびエネルギー分散を考慮します。これらの物理を考慮する場合は、parameterセクションに角度分散オプションNSPREDとエネルギー分散オプションNEDISPを設定して下さい。奨励値はNSPRED=2とNEDISP=1です。

この図では、炭素線ビームが水中で作るブラッグピークの様子を示しています。角度分散およびエネルギー分散が無いと画一のエネルギーの炭素線は非常に鋭いブラッグピークを作ることになります。しかし、実際には角度分散およびエネルギー分散があるため、ピーク位置に揺らぎが生じ、ある程度ならされたピークになります。

--- SLIDE 54 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
核反応モデルの変更
PHITSには、Bertini, JAM, JQMD, INCL, INC-ELFという核反応モデルがあり、状況に応じてユーザーが使い分けることができます。
SPEAKER_NOTES:
次に核反応モデルの変更に関するパラメータです。

PHITSには複数の物理モデルが内包されています。これらの物理モデルは、輸送粒子の種類やエネルギーによって、自動で切り替えられるようにデフォルトで設定されています。ただ、物理モデルの違いの影響を確認したい等の要望に応えるため、状況に応じて物理モデルの切り替えをユーザーが変更できるようになっています。ここで示されるパラメータが物理モデルの変更に関するパラメータです。

--- SLIDE 55 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
Neutron     Nuclear data         INCL (inclg=1)             JAM
(10-11 MeV)
emin(2)
(20 MeV)
dmax(i)
(3 GeV)
einclmax
(10-3 MeV)
emin(1)
Nucleus                                 JQMD                         JAMQMD
d, t, 3He, α                             INCL (inclg=1)           JAMQMD
(3 GeV)
einclmax
Proton                                   INCL (inclg=1)               JAM
(1 MeV)
einclmin
(10-3 MeV/n)
emin(i)
(3 GeV/n)
einclmax
(1 MeV/n)
einclmin
(10-3 MeV/n)
emin(i)
(3 GeV/n)
ejamqmd
(10 MeV/n)
eqmdmin
核反応モデルの切替エネルギー
SPEAKER_NOTES:
それぞれの物理モデルの切り替えエネルギーはこの図の通りになっています。

--- SLIDE 56 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
(n,2n)
イベントジェネレーター（EG）モード
核データ＋統計崩壊モデルの利用により、残留核からの放出粒子まで考慮し、かつエネルギーと運動量の保存則を満たした核反応イベントを生成するモード。
通常モード
20 MeV
15 MeV
10 MeV
(n,2n)
20 MeV
(n,np)
8 MeV
20 MeV
15 MeV
4 MeV
1 MeV
20 MeV
(n,np)
8 MeV
11 MeV
1 MeV
2次粒子は中性子とγ線のみ考慮
エネルギーや運動量は各反応毎に保存しない
平均値は核データを完璧に再現
イベントジェネレータモード
全ての2次粒子を考慮
エネルギーや運動量は各反応毎に保存する
平均値は核データをほぼ再現する
詳細はT. Ogawa et al., NIM A, 763, 575-590 (2014)
neutron
proton
recoil
nucleus
（Q = 0と仮定）
SPEAKER_NOTES:
イベントジェネレーターモードについて説明します。この機能は他のモンテカルロコードにはない、PHITS独自の機能です。

20MeV以下の低エネルギー中性子はデータライブラリを使用した計算が実行されます。この場合、中性子の反応と輸送はデータライブラリに従い、精度の高い計算が実行されるのですが、二次粒子の生成や反跳粒子の輸送は行われません。これは、無数にある反応チャンネルのデータの一部しかデータライブラリに含まれていないためで、この情報だけでは、二次粒子まで含めた反応系全体（イベント）を再現することができません。

そこで、PHITSではデータライブラリに加えて、統計崩壊モデルを組み合わせることで、低エネルギー中性子のイベントを再現する機能、イベントジェネレーターモードを用意しています。イベントジェネレータモードでは、二次粒子や反跳粒子を含み、系全体としてエネルギーと運動量の保存則を満たしたイベントが生成されます。

イベントジェネレーターを使用しない通常モードでは、二次粒子として中性子とガンマ線のみを考慮します。エネルギーや運動量は各反応毎に保存しません。平均値として、核データによる分布を完璧に再現します。

一方、イベントジェネレーターモードでは、残留核を含めた全ての二次粒子を考慮し、エネルギーや運動量は各反応毎に保存されます。平均値として、核データによる分布をほぼ再現します。

--- SLIDE 57 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
EGモードON/OFFの判断材料
イベントジェネレータモードを使った方がよい場合
低エネルギー中性子が放出する陽子やα粒子スペクトルが見たい
残留核の情報（反跳エネルギーなど）が知りたい
イベント毎の情報が知りたい（検出器応答関数の計算など）
イベントジェネレータモードを使わない方がよい場合
中性子と光子の情報だけ知りたい（遮へい計算など）
中性子核データライブラリを200MeVまで使いたい
カーマ近似*を用いて200MeV以下の中性子による発熱を計算したい  （BNCTに対する医学物理計算など）
*中性子フルエンスから平均発熱量を直接計算する近似計算方法
SPEAKER_NOTES:
次に、このイベントジェネレーターモードを使った方が良い場合と使わない方が良い場合について説明します。

イベントジェネレーターモードを使った方がよい場合は、低エネルギー中性子の反応によって生成する二次粒子に興味がある場合で、放出される陽子やアルファ粒子のスペクトルに興味がある場合や、残留核の情報が知りたい場合、そして検出器応答などイベント情報が必要な場合です。また、カーマ近似が成立しない高エネルギー中性子に対する発熱計算においてもイベントジェネレーターモードの使用が推奨されます。陽子線治療や重粒子線治療に対する医学物理計算などがこれに当たります。

イベントジェネレーターモードを使わない方がよい場合は、遮蔽計算等、中性子と光子の情報だけで十分な計算や、低エネルギー中性子の正確な挙動を追う計算等の場合です。また、20MeV以上でイベントジェネレーターモードでの核データライブラリの取り扱いが変わるため、200MeVまで高精度に中性子核データライブラリに従った二次粒子生成を行いたい場合も、イベントジェネレーターモードをオフにしたほうがベターです。イベントジェネレーターモードを使わない場合は、中性子による線量寄与はカーマ近似に基づき計算されるため、比較的短時間で統計精度を上げることができます。

--- SLIDE 58 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
EGモードの設定
使用する方法は、 [parameters]セクションにおいて“e-mode=2”とするだけです(指定しない場合は“e-mode=0”となります)
SPEAKER_NOTES:
イベントジェネレーターモードの設定はparameterセクションのE-MODEパラメータで行います。デフォルトでは、E-MODE=0と設定されており、イベントジェネレーターモードが使用されません。イベントジェネレーターモードを使用したい場合はE-MODE=2と設定してください。

--- SLIDE 59 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
lec03.inp
課題10
まず、イベントジェネレータモードを使用せずに、10MeV中性子を線源とする計算を実行してみよう
emin(12)とemin(13)を削除する
  （計算時間短縮のため）

線源を10MeVの中性子とする
  （[source]において%projectile%を変更）

[t-deposit]のpart = allを
  part = neutron protonに変更する
[ T - Deposit ]
・ ・ ・ ・ ・ ・
file = deposit.out
part = all
[ S o u r c e ]
set:%projectile%[photon]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
・ ・ ・ ・ ・ ・
 emin(12) = 0.001
 emin(13) = 0.001
PHITSを実行して，中性子と陽子
それぞれの線量寄与を計算
（deposit.outを確認）
SPEAKER_NOTES:
イベントジェネレートモードを試してみましょう。

まず、イベントジェネレーターモードを使わずに計算を行います。計算時間の節約のため、電子・陽電子のカットオフエネルギーの設定を削除し、線源を10MeVの中性子としてください。T-depositのPART=allをneutronスペースprotonに変更して、PHITSを実行し、出力結果のテキストファイルdeposit.outを確認して下さい。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-11.inp

--- SLIDE 60 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
lec03.inp
課題10の答え合わせ
まず、イベントジェネレータモードを使用せずに、10MeV中性子を線源とする計算を実行してみよう
[ P a r a m e t e r s ]
・ ・ ・ ・ ・ ・
$ emin(12) = 0.001
$ emin(13) = 0.001
（29行目あたり）
#  num    reg     volume       neutron   r.err      proton    r.err
    1     101   5.2465E+02   4.4415E-05  0.2975   0.0000E+00  0.0000
    2     102   3.6454E+03   6.4578E-02  0.1427   0.0000E+00  0.0000
    3     103   9.9378E+03   1.5546E-03  0.0875   0.0000E+00  0.0000
    4     104   1.9364E+04   1.0111E-01  0.0491   0.0000E+00  0.0000
    5     105   3.1919E+04   1.5905E-01  0.0264   0.0000E+00  0.0000
deposit.out
[ T - Deposit ]
・ ・ ・ ・ ・ ・
file = deposit.out
part = neutron proton
[ S o u r c e ]
set:%projectile%[neutron]
...
 e0 =   10.0
陽子からの線量寄与がない → 中性子が核反応で生成する荷電粒子を考慮せず，カーマ近似により吸収線量を計算するため
SPEAKER_NOTES:
Deposit.outの29行目あたりに次の様な結果が得られたはずです。細かな数値に関しては、PHITSのバージョンにより違いがあると思いますが、中性子の欄には値があるのに対し、陽子の欄ではゼロになっているのが確認できます。

これは、デフォルトでイベントジェネレーターを使用していないため、低エネルギー中性子の反応で生まれる陽子を輸送していないためで、陽子による線量寄与がゼロになります。このように、イベントジェネレーターモードを使用しない場合は、中性子の線量寄与はカーマ近似を基に中性子線量として計算されます。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-11.inp

--- SLIDE 61 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
[ P a r a m e t e r s ]
・ ・ ・ ・ ・ ・
e-mode = 2
[parameters]セクションでe-mode = 2としてPHITSを実行する
課題11
イベントジェネレータモードを使用してみよう
[t-deposit]でpart = neutronと指定してるにも関わらずイベントジェネレータモードを使用している，というwarningが表示される
lec03.inp
（通常，[t-deposit]でpart = neutronと指定する場合はカーマ近似を使うため）
deposit.outを見て中性子と陽子の線量寄与を確認
SPEAKER_NOTES:
次にE-MODE=2をparameterセクションに追加し、イベントジェネレーターモードを使用した計算を実行してみましょう。

イベントジェネレーターモードを使用する場合は、中性子による線量寄与は計算されず、代わりに生成する二次荷電粒子による線量寄与が計算されます。ダブルカウントを防ぐために、この場合は中性子による線量寄与はゼロとされます。

ポップアップウィンドウに表示されるワーニングは、t-depositタリーの中でPART=neutronと設定し、中性子による線量寄与を出力するように指定しているものの、イベントジェネレーターモードを使用していることに対するワーニングメッセージです。

出力されるdeposit.outの中性子と陽子の線量寄与を確認して下さい。
MENTIONED_INPUT_NAMES: lec03.inp
ANSWER_FILE: input/lec03-end.inp

--- SLIDE 62 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
課題11の答え合わせ
中性子と陽子の寄与がほぼ逆になっている
e-mode = 2の方が統計が悪い（カーマ近似を使わないので，中性子が核反応を起こして荷電粒子を生成しない限りエネルギーを付与しないため）
（29行目あたり）
#  num    reg     volume       neutron   r.err      proton    r.err
    1     101   5.2465E+02   0.0000E+00  0.0000   0.0000E+00  0.0000
    2     102   3.6454E+03   0.0000E+00  0.0000   5.1766E-02  0.2056
    3     103   9.9378E+03   0.0000E+00  0.0000   8.3706E-04  0.2664
    4     104   1.9364E+04   0.0000E+00  0.0000   8.0923E-02  0.0712
    5     105   3.1919E+04   0.0000E+00  0.0000   1.4615E-01  0.0402
deposit.out
（29行目あたり）
#  num    reg     volume       neutron   r.err      proton    r.err
    1     101   5.2465E+02   4.4415E-05  0.2975   0.0000E+00  0.0000
    2     102   3.6454E+03   6.4578E-02  0.1427   0.0000E+00  0.0000
    3     103   9.9378E+03   1.5546E-03  0.0875   0.0000E+00  0.0000
    4     104   1.9364E+04   1.0111E-01  0.0491   0.0000E+00  0.0000
    5     105   3.1919E+04   1.5905E-01  0.0264   0.0000E+00  0.0000
deposit.out
（e-mode = 0）
（e-mode = 2）
SPEAKER_NOTES:
E-MODE=2でイベントジェネレーターモードを使用した場合は、中性子による線量寄与がゼロになる一方で、陽子による線量寄与が観測できます。E-MODE=0の場合に比べると中性子と陽子の寄与がほぼ逆になっています。試行回数を増やすとこれらの結果はほぼ一致します。統計精度に着目するとE-MODE=2のほうが統計精度が悪くなっています。これは、E-MODE=0ではカーマ近似によって中性子線量が計算されるため、中性子のフラックスがあれば計算されるのに対し、E-MODE=2の場合は中性子が反応して二次粒子が生成されたイベントのみで計算されるためです。
ANSWER_FILE: input/lec03-end.inp

--- SLIDE 63 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
実習内容
計算モードの選択
便利な入力補助機能
統計的に信頼できる結果を得るための設定
モンテカルロ積分を使った体積・面積計算
試行回数と統計誤差
計算結果の規格化
物理的に信頼できる結果を得るための設定
断面積データライブラリの利用
物理モデルの選択
まとめ

--- SLIDE 64 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
まとめ
PHITSでは、[Parameters]セクションの設定を変更することで、様々な計算モードや物理モデルの選択を行うことができる。
各計算モード（icntl）を使い分けることにより、ジオメトリの確認，ソースのチェック、粒子の輸送計算を行う。
統計精度と試行回数(maxcas, maxbch)は密接に関連しており、適切な数を設定する必要がある。
低エネルギーの中性子や光子，電子，陽電子等は断面積データライブラリやEGS5を利用することで精度の高い計算結果を得ることができる。
状況に応じてイベントジェネレーターモード(e-mode)など物理モデルの設定を変更する必要がある。
様々な目的に対応する最適な設定がphits/recommendationフォルダに格納されています。どの奨励設定がよいか、ＡＩに利用目的を伝えて聞いてください
SPEAKER_NOTES:
まとめです。

Parameterセクションでは、計算モードや物理モデルの選択を行います。ICNTLパラメータで計算モードの選択を行います。統計精度と試行回数は密接に関連しており、求める統計精度に応じて試行回数を増やす必要があります。低エネルギー中性子や光子、電子、陽電子等データライブラリを使用することで、精度の高い計算を行うことができます。状況に応じてイベントジェネレーターモードなどの物理モデルの設定を変更する必要があります。

最適な設定が分からない場合は、PHITSパッケージに含まれる奨励設定ファイル、recommendationを参照してください。次のスライドで紹介するように、AIを利用して最適な設定を選択することも可能です。

--- SLIDE 65 ---
PPTX_FILE: phits-lec03-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
AI Phi-chan (https://x.gd/WAynQ)
加速器の遮へい計算にPHITSを使いたいので最適な奨励設定を教えてください
宇宙線線源を使いたいので、講習会資料やサンプルがどこにあるか教えてください
lec01の課題5の内容がよく理解できないので詳しく教えてください
lec02の体系をサイコロ形状に変更してください
質問例
NotebookLMにアクセス
ノートブックを新規作成
workbench/AI/knowledge_baseフォルダにあるテキストファイルを教材としてアップロード
DCHAINやANGELも使いたい場合は、それらのPDFマニュアルを教材としてアップロード
学習を強化したい場合は、 knowledge_baseにあるcrucial_notice_forAI.txtに指示を追記
自分専用のページを作りたい場合
NotebookLMを使っているため、接続にはGoogleアカウントが必要となります
SPEAKER_NOTES:
AIへの質問例です。例えば、加速器の遮へい計算にPHITSを使いたいので最適な奨励設定を教えてください、宇宙線線源を使いたいので、講習会資料やサンプルがどこにあるか教えてください、lec01の課題5の内容がよく理解できないので詳しく教えてください、などのように具体的に質問すると丁寧に回答してくれます。また、lec02の体系をサイコロ形状に変更してください、のように伝えると、インプットを直接出力してくれます。また、自分専用のページを作ることも可能で、その場合は、下記インストラクションに従って作成して下さい。

下方のリンクにアクセスしていただき、お試しいただければと思います。
ANSWER_FILE: input/lec03-6.inp

--- SLIDE 66 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
宿題
EGS5を利用して電子・陽電子も輸送する（線源粒子は陽子から変更しない）
イベントジェネレータモードを使う
線量-深さ分布のブラッグピーク付近における統計誤差0.5％以内を目指す    （maxcas, istdev, batch.outなどを活用する）
1nA照射に対する吸収線量率(Gy/s)に規格化する
SPEAKER_NOTES:
宿題（3次元体系）

--- SLIDE 67 ---
PPTX_FILE: phits-lec03-en.pptx
SLIDE_TEXT:
宿題（解答例）
陽子（上）・中性子（下）フルエンス
円柱中心（上）と端側（下）における
吸収線量(Gy/s)の深さ分布

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/lec03-1.inp

[BONUS_TEXT_FILES]
NOTE: None
