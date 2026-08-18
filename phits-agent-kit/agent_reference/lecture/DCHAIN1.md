# Lecture: advanced/DCHAIN1

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/DCHAIN1
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: DCHAIN1
LECTURE_PATH_INDEX: lecture/advanced/DCHAIN1
PPTX_FILES: phits-lec-dchain01-en.pptx, phits-lec-dchain01-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: dchain, exercise
SECTION_KEYWORDS: 3, 4, 5, 8, 10, bq, gev, h, m, ma, mw, s, t-dchain, t-track, t-yield, volume

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/DCHAIN1
LECTURE_PATH_INDEX: lecture/advanced/DCHAIN1
PPTX_FILES: phits-lec-dchain01-en.pptx, phits-lec-dchain01-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 2
SLIDE_COUNT: 110
EXERCISE_SLIDE_COUNT: 9
BONUS_INPUT_COUNT: 2
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- dchain.inp
- exercise.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Evaluation of Induced Radioactivity:
- SLIDE 02: PHITS is particle transport code.
- SLIDE 03: Abstract
- SLIDE 04: Flowchart of Connection Calculation
- SLIDE 05: Let’s try running them!
- SLIDE 06: Output files from [t-dchain]
- SLIDE 07: Output files from DCHAIN
- SLIDE 08: Most parameters used in DCHAIN can be also specified in the [t-dchain] section
- SLIDE 09: Abstract
- SLIDE 10: Geometry in our example
- SLIDE 11: Check Calculation Result
- SLIDE 12: Settings for using [T-Dchain]
- SLIDE 13: Use of JENDL-5
- SLIDE 14: Parameters in [T-Dchain]
- SLIDE 15: timeevo：Number of irradiation and cooling time steps. After this line, time and relative amplitude must be specified
- SLIDE 16: outtime：Number of output times
- SLIDE 17: Check the time-dependence of Induced Activities
- SLIDE 18: [ T-DCHAIN ]
- SLIDE 19: Let’s change irradiation time steps
- SLIDE 20: Answer
- SLIDE 21: tdchain.out
- SLIDE 22: Answer
- SLIDE 23: EXERCISE 2 | Exercise 2: Answer
  ANSWER_FILE: input/exercise-3.inp
- SLIDE 24: Abstract
- SLIDE 25: tdchain.act: Induced activity, decay heat*, and dose rates
- SLIDE 26: Graphic Output File (*.eps)
- SLIDE 27: tdchain.dcs: Shows how each nuclide is produced / destroyed
- SLIDE 28: Abstract
- SLIDE 29: Objective (exercise.inp)
- SLIDE 30: [T-DCHAIN]
- SLIDE 31: H*(10) distribution
- SLIDE 32: Fe_target.eps (page 1)
- SLIDE 33: *.pht output with [Source]
- SLIDE 34: EXERCISE 1 | $ Photon source from DCHAIN output
  ANSWER_FILE: input/exercise-2.inp
- SLIDE 35: $ Photon source from DCHAIN output
- SLIDE 36: EXERCISE 2 | $ Photon source from DCHAIN output
  ANSWER_FILE: input/exercise-3.inp
- SLIDE 37: $ Photon source from DCHAIN output
- SLIDE 38: EXERCISE 3 | $ Photon source …
  ANSWER_FILE: input/exercise-3.inp
- SLIDE 39: $ Photon source …
- SLIDE 40: EXERCISE 4 | htitle = [t-dchain]  in xyz mesh
  ANSWER_FILE: (missing)
- SLIDE 41: ! --- calculation parameters ---
- SLIDE 42: Abstract
- SLIDE 43: DCHAIN can calculate the time variation of induced activities, decay heats, γ-ray spectra, and dose rates during irradia
- SLIDE 44: Supplemental Information
- SLIDE 45: Change materials in DCHAIN
- SLIDE 46: DCHAIN reaction types
- SLIDE 47: [source] output option
- SLIDE 48: [t-dchain] with xyz or reg mesh?
- SLIDE 49: Additional Information on Output Files from DCHAIN
- SLIDE 50: ACMIN – controls threshold inventory/activity necessary for printing nuclides. (D = total activity x 10-10)
- SLIDE 51: IANGBPWR – toggles display of beam power schedule 	overlay (the red/pink bars)
- SLIDE 52: CHRLVTH – controls threshold change in inventory/activity 	necessary for chains to be printed (similar to ACMIN, 	good f
- SLIDE 01: PHITSとDCHAINを組み合わせた
- SLIDE 02: 放射線挙動解析コードPHITS
- SLIDE 03: PHITS-DCHAIN接続計算の概要
- SLIDE 04: PHITS-DCHAIN接続計算の流れ
- SLIDE 05: PHITS-DCHAIN接続計算を実行
- SLIDE 06: [t-dchain]からの出力ファイル
- SLIDE 07: DCHAINからの出力ファイル
- SLIDE 08: DCHAINで指定するパラメータは、基本的に [t-dchain]内にて直接指定することができる
- SLIDE 09: 実習内容
- SLIDE 10: dchain.inpの計算体系
- SLIDE 11: 計算結果の確認
- SLIDE 12: [T-Dchain]を使う際の奨励設定
- SLIDE 13: JENDL-5の利用
- SLIDE 14: [T-Dchain]のパラメータ①
- SLIDE 15: timeevo：照射及び冷却時間のステップ数。この行の後に時間と相対ビーム強度（1.0がampに相当）を入力
- SLIDE 16: outtime：結果を出力する時間の数
- SLIDE 17: 誘導放射能の時間変化を確認
- SLIDE 18: [ T-DCHAIN ]
- SLIDE 19: 照射時間・強度を変更してみよう
- SLIDE 20: tdchain.out
- SLIDE 21: 出力時間を変更してみよう
- SLIDE 22: tdchain.out
- SLIDE 23: 解答2（つづき）
- SLIDE 24: 実習内容
- SLIDE 25: tdchain.act: 誘導放射能、崩壊熱*、線量率が確認できる
- SLIDE 26: 画像出力(*.eps)
- SLIDE 27: tdchain.dcs: 各核種の壊変連鎖スキーム（Decay Chain Scheme）
- SLIDE 28: 実習内容
- SLIDE 29: 演習の目的 (exercise.inp)
- SLIDE 30: [T-DCHAIN]
- SLIDE 31: H*(10)の空間分布
- SLIDE 32: DCHAINを実行して結果を確認
- SLIDE 33: DCHAINより出力された[source] (*.pht)
- SLIDE 34: EXERCISE 1 | $ Photon source from DCHAIN output
  ANSWER_FILE: input/exercise-2.inp
- SLIDE 35: $ Photon source from DCHAIN output
- SLIDE 36: EXERCISE 2 | $ Photon source from DCHAIN output
  ANSWER_FILE: input/exercise-3.inp
- SLIDE 37: $ Photon source from DCHAIN output
- SLIDE 38: EXERCISE 3 | $ Photon source …
  ANSWER_FILE: input/exercise-3.inp
- SLIDE 39: $ Photon source …
- SLIDE 40: EXERCISE 4 | htitle = [t-dchain]  in xyz mesh
  ANSWER_FILE: (missing)
- SLIDE 41: ! --- calculation parameters ---
- SLIDE 42: 実習内容
- SLIDE 43: DCHAINは、誘導放射能、崩壊熱、γ線スペクトルとそれに伴う線量率の時間変化を任意の照射・冷却スケジュールに対して計算することができる
- SLIDE 44: 実習内容
- SLIDE 45: 用語の解説
- SLIDE 46: 放射性壊変
- SLIDE 47: 放射性壊変による放射能の減衰
- SLIDE 48: 放射性壊変による核種Bの生成（純増）
- SLIDE 49: 生成・崩壊方程式の一般解は、
- SLIDE 50: 放射能は、放射性核種の崩壊定数λ（または、半減期 T1/2）により、時間とともに指数関数的に増減する。
- SLIDE 51: 長期間稼働予定の施設の誘導放射能の評価には、長半減期核種を生成しやすいCoやEuなどの不純物を含めた評価が必須です
- SLIDE 52: DCHAINの反応カテゴリー
- SLIDE 53: DCHAINによる[source]出力オプション
- SLIDE 54: mesh=xyzとregの使い分け
- SLIDE 55: 出力ファイルに関する追加情報
- SLIDE 56: ACMIN – *.actファイルに出力する放射能の下限値。デフォルトは全放射能×10-10
- SLIDE 57: IANGBPWR – ビーム出力の変化をピンク色のバーで出力するオプション
- SLIDE 58: CHRLVTH – *.dcsファイルに出力する放射能の下限値（*.actのACMINに相当）

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: dchain.inp
FILE: exercise.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Evaluation of Induced Radioactivity:
Connection between PHITS & DCHAIN
phits/lecture/advanced/DCHAIN1
Sep. 2025 revised

--- SLIDE 02 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
PHITS is particle transport code.
Operates on the time scales of nuclear reactions
Can calculate the induced radioactivity immediately after a pulse irradiation but not the variation of activity with time
DCHAIN is decay, burnup, and activation code.
Designed to track production and destruction of nuclide inventories as a function of time over any time scale
Can also calculate decay heat and gamma-ray spectra
In this lecture, you will learn how to connect PHITS and DCHAIN and calculate the time variation of the induced radioactivity based on the connection.
Purpose

--- SLIDE 03 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Abstract
Parameter settings in [t-dchain]
Output files from DCHAIN
Exercises
Summary
Table of Contents

--- SLIDE 04 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Flowchart of Connection Calculation
PHITS
Particle Transport Simulation
Basic input file for DCHAIN (specified by “file=”)
Nuclear yield calculated by   [t-yield] （*.dyld）
Neutron fluxes below 20 MeV calculated by [t-track] （*.dtrk)
Information on the path of data library used in DCHAIN (dch_link.dat)
Output files from [t-dchain]
DCHAIN
Decay chain calculation
Data libraries for DCHAIN
Activation cross sections for neutrons
Decay data (daughters, branching ratios, γ-ray emissions, decay energies, etc.)
Fission yields (spontaneous & induced)
Calculation Results
Induced activity（Bq)
Decay heat （W）
Emitted γ-ray spectrum
Extra decay γ calc.
during and after irradiation

--- SLIDE 05 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Let’s try running them!
Execute PHITS with “dchain.inp” (send to -> PHITS)
(tdchain.out, .dtrk, .dyld, and dch_link.dat are generated)
（tdchain.lst, .act, .pht, .ang, .gsd, .gso, .alr, .eps, .dcs are generated）
Execute DCHAIN with “tdchain.out” (send to -> DCHAIN)
Time variation of induced activity in each cell
tdchain.eps
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 06 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Output files from [t-dchain]
tdchain.out: Basic input file for DCHAIN
          （File name is specified by “file=” in [t-dchain])
tdchain.dyld: Nuclear yields calculated by [t-yield]
tdchain.dtrk: Neutron fluxes below 20 MeV calculated by [t-track]*
dch_link.dat: Folder name containing the libraries for DCHAIN
         (specified by “file(21)=” in [parameters]）
*In principle, time variation of induced activity can be calculated only from the nuclear yields calculated by [t-yield]. However, the calculation accuracy can be improved when nuclear yields from neutrons below 20 MeV are separately calculated in DCHAIN using specially developed activation cross sections.
SPEAKER_NOTES:
Note that the [t-yield] tally is essentially the “everything else” category of reaction products outside of the <20 MeV neutron reactions.

--- SLIDE 07 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Output files from DCHAIN
tdchain.act: Main output (Induced radioactivity, decay heat,
tdchain.ｌｓｔ: Diagnostic output file (similar to “phits.out” in PHITS)
tdchain.dcs: Decay chain schemes and reaction information
tdchain.ang: Induced radioactivity, decay heat, dose rates
tdchain.eps: Graphs generated by ANGEL using above file
tdchain.mat: Activated compositions in PHITS [Material] format
tdchain.alr: Induced activity & decay heat summed over all regions
dose rate, emitted γ-ray spectrum)
written in ANGEL input format
Information on run-time errors is written in this file

--- SLIDE 08 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Most parameters used in DCHAIN can be also specified in the [t-dchain] section
In general, their default values are adequately set, and do not need to be changed. If you would like to change them, please refer to the DCHAIN manual for their explanations.

*/phits/dchain-sp/manual/DCHAIN_input_manual_en.pdf

(The DCHAIN manual also includes general guidance, troubleshooting help, example calculations, and more)
Important Notice

--- SLIDE 09 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Abstract
Parameter settings in [t-dchain]
Output files from DCHAIN
Exercises
Summary
Table of Contents
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 10 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Geometry in our example
Accelerate 250 MeV protons into:

W / H2O / Fe target
(8 cm x 8 cm x 3/10/5 cm)

encased in Be
(4 cm thick on sides,
 5 cm thick on back,
 none on front face)
yz-track.eps (if icntl = 8)

--- SLIDE 11 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Check Calculation Result
yz-track.eps
Proton flux
(first page)
Neutron flux
(second page)

--- SLIDE 12 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Settings for using [T-Dchain]
dchain.inp
[Parameters]
...
$  required options for DCHAIN
jmout	=         1 # (D=0) Density echo, 0:input, 1:number density
e-mode	=         0 # (D=0) Event generator mode is not recommended
$ recommended option for isomer production
igamma	=         3  $ (D=2) 0:No, 1:Old, 2:EBITEM,3:EBITEM+Isomer
…

[Volume]   $ required section for DCHAIN
    reg   vol
     1   c1*(2*c5)**2  $ Tungsten (W)
…
jmout should be 1 because the information on the atomic densities in each material are required in DCHAIN
Event Generator Mode should not be used （e-mode = 0) since nuclear yields from low-energy neutron interactions are separately calculated in DCHAIN
igamma should be 3 to consider the isomer production
The volume of the regions where the activity is calculated should be defined in [volume]
set:c1[3]   	$ thickness of W set:c2[10]	$ thickness of H2O set:c3[5]   	$ thickness of Fe
set:c4[5]   	$ thickness of Be  	   back end
set:c5[4]   	$ half side length   	   of inner block
set:c6[8]   	$ half side length 	   of outer block
SPEAKER_NOTES:
From v3.33, jmout defaults to 1 if a [t-dchain] tally is present, otherwise it retains its default value of 0.
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Use of JENDL-5
dchain.inp
[Parameters]
...
$  recommended use for activation calculation, installation of JENDL-5 is required
 dmax(1)  =  200.000000     # (D=emin(1)) data max. energy of proton (MeV)
 dmax(2)  =  200.000000     # (D=20.0) data max. energy of neutron (MeV)
$ dmax(15) =  100.000000     # (D=emin(15)) data max. energy of deuteron (MeV/n)
$ dmax(18) =  50.000000     # (D=emin(18)) data max. energy of alpha (MeV/n)
$ dpnmax   =  200.000000     # (D=emin(14)) data max. energy for photo-nuclear lib. (MeV)
…
For activation calculations involving neutrons above 20 MeV, protons, deuterons, alpha particles, and photons, JENDL-5 is recommended for use because their activation cross sections are utilized in [t-yield].
Installation of JENDL-5 is required using its installer in XS folder*
*Results shown in this lecture note were obtained without installing JENDL-5
SPEAKER_NOTES:
From v3.33, jmout defaults to 1 if a [t-dchain] tally is present, otherwise it retains its default value of 0.
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Parameters in [T-Dchain]
dchain.inp
Basic parameters
・ mesh (must be “reg”, “xyz”, or “tet”）

・ file: Input file name for DCHAIN

・ amp: Maximum source intensity per sec
[ T-DCHAIN ]
  title = 250 MeV protons on core
  mesh =  reg
  reg =  1 2 3
  file = tdchain.out
  timeevo =    1
     2.0 h  1.0
  outtime =    7
     1 h
     2 h
     3 h  $ or -1 h
     4 h  $ or -2 h
     5 h  $ or -3 h
     6 h  $ or -4 h
     7 h  $ or -5 h
set:c11[100.0]  $ beam current (nA)
set:c12[c11*1.0e-9/1.602177e-19]
amp = c12 $ Source Intensity (#/sec)
If totfact is specified in the [source] section, please adjust amp so that amp x totfact = actual source intensity (source/sec).
mesh = r-z is not supported. Combined cell, e.g. (1 2), cannot be used for reg mesh
File names (***.dtrk, ***.dyld, ***_err.dyld, ***.dout, ***.lst, ***.yld, ***.gsd, ***.gso, ***.alr, ***.act, ***.ang, ***.pht, ***.dcs, ***.mat, dch_link.dat, yield.out) are not allowed because PHITS/DCHAIN automatically generate them
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
timeevo：Number of irradiation and cooling time steps. After this line, time and relative amplitude must be specified
These are INTERVALS of time, Δt
Example:
2.0 h 1.0 → irradiate 2 hours at full amplitude
After beam, infinite cooling (beam off) is assumed
s (second), m (minute), h (hour), d (day), y (year)
You must insert a space before and after them
[ T-DCHAIN ]
  title = 250 MeV protons on core
  mesh =  reg
  reg =  1 2 3
  file = tdchain.out
  timeevo =    1
     2.0 h  1.0
  outtime =    7
     1 h
     2 h
     3 h  $ or -1 h
     4 h  $ or -2 h
     5 h  $ or -3 h
     6 h  $ or -4 h
     7 h  $ or -5 h
set:c11[100.0]  $ beam current (nA)
set:c12[c11*1.0e-9/1.602177e-19]
amp = c12 $ Source Intensity (#/sec)
dchain.inp
Parameters in [T-Dchain]
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 16 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
outtime：Number of output times
After this line, output timing must be specified in the same manner as timeevo
These are POINTS in time, t
Positive value: Count from the beginning of the first time step
Negative value: Count from the end of the last irradiation step
Parameters in [T-Dchain]
[ T-DCHAIN ]
  title = 250 MeV protons on core
  mesh =  reg
  reg =  1 2 3
  file = tdchain.out
  timeevo =    1
     2.0 h  1.0
  outtime =    7
     1 h
     2 h
     3 h  $ or -1 h
     4 h  $ or -2 h
     5 h  $ or -3 h
     6 h  $ or -4 h
     7 h  $ or -5 h
set:c11[100.0]  $ beam current (nA)
set:c12[c11*1.0e-9/1.602177e-19]
amp = c12 $ Source Intensity (#/sec)
dchain.inp
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Check the time-dependence of Induced Activities
dchain.inp
tdchain.eps
[ T-DCHAIN ]
…
timeevo =    1
   2.0 h  1.0

outtime =   7
   1 h
   2 h
   3 h  $ or -1 h
   4 h  $ or -2 h
   5 h  $ or -3 h
   6 h  $ or -4 h
   7 h  $ or -5 h
…
SPEAKER_NOTES:
Make note that the tungsten region is the most activated here.  This is the motivation for only looking at the tungsten region later in the example.
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[ T-DCHAIN ]
  title = 250 MeV protons on core
  mesh =  reg
  reg =  1 2 3
  file = tdchain.out
  timeevo =    1
     2.0 h  1.0
  outtime =    7
     1 h
     2 h
     3 h  $ or -1 h
     4 h  $ or -2 h
     5 h  $ or -3 h
     6 h  $ or -4 h
     7 h  $ or -5 h
set:c11[100.0]  $ beam current (nA)
set:c12[c11*1.0e-9/1.602177e-19]
amp = c12 $ Source Intensity (#/sec)
DCHAIN input file automatically written; [T-Dchain] values are passed along.
Note: if desiring to change parameters, it is often faster to modify the DCHAIN input only and rerun it.
Only need to rerun PHITS if changing the amp*, source, materials, geometry, parameters, or regions being tallied
Produced DCHAIN input file
dchain.inp
tdchain.out
…
amp =  1.0000E-04  ! (mA)
…
! --- irradiation time ---
itstep =       1
 2.0000E+00 h  1.0000E+00

! --- output time ---
itout =       7
      1.0000E+00 h
      2.0000E+00 h
      3.0000E+00 h
      4.0000E+00 h
      5.0000E+00 h
      6.0000E+00 h
      7.0000E+00 h
…
*amp automatically is converted from source/sec to mA and should not be changed in DCHAIN input
SPEAKER_NOTES:
As a warning, if you increase AMP in PHITS [T-Dchain], in the DCHAIN input it will increase both the AMP parameter (used for scaling nuclides produced from the [T-Yield] tally) and FLUXS in each region (total neutron flux tallied by [T-Track] scaled by source intensity, used for nuclides produced/consumed by neutron reactions).  If you want to scale the total intensity of the beam without rerunning PHITS, this is most easily accomplished by just changing the beam intensity in the irradiation schedule section (istep) rather than adjusting AMP and the FLUXS value(s).
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Let’s change irradiation time steps
tdchain.out
…
! --- irradiation time ---
itstep =       1
   2.0000E+00 h  1.0000E+00

! --- output time ---
itout =       7
      1.0000E+00 h
      2.0000E+00 h
      3.0000E+00 h
      4.0000E+00 h
      5.0000E+00 h
      6.0000E+00 h
      7.0000E+00 h
…
Open tdchain.out and find itstep
Change the irradiation schedule to:
2.0 hours beam at full power
1.0 hour of cooling (beam off)
1.0 hour of beam at half power
1.3 hours of beam at full power
1.7 hours of cooling (beam off)
Run tdchain.out with DCHAIN again
Remember that:
- time units use a single character
    s (second), m (minute), h (hour), d (day), y (year)
- a space is required between each item on a line

--- SLIDE 20 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Answer
tdchain.out
…
! --- irradiation time ---
itstep =       5
   2.0 h  1.0
   1.0 h  0.0
   1.0 h  0.5
   1.3 h  1.0

! --- output time ---
itout =       7
      1.0000E+00 h
      2.0000E+00 h
      3.0000E+00 h
      4.0000E+00 h
      5.0000E+00 h
      6.0000E+00 h
      7.0000E+00 h
…
tdchain.eps
The activities and the beam power display show the impact of changing the irradiation schedule.

--- SLIDE 21 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
tdchain.out
…
! --- irradiation time ---
itstep =       5
   2.0 h  1.0
   1.0 h  0.0
   1.0 h  0.5
   1.3 h  1.0

! --- output time ---
itout =       7
      1.0000E+00 h
      2.0000E+00 h
      3.0000E+00 h
      4.0000E+00 h
      5.0000E+00 h
      6.0000E+00 h
      7.0000E+00 h
…
In tdchain.out, modify itout :
Change the output times to:
1.3 hours after the start of irradiation
2.0 hours after the start of irradiation
2.5 hours after the start of irradiation
3.0 hours after the start of irradiation
4.0 hours after the start of irradiation
4.7 hours after the start of irradiation
5.3 hours after the start of irradiation
5.8 hours after the start of irradiation
7.0 hours after the start of irradiation
Bonus: specify these final two values with negative values (as time since the end of the final irradiation) instead.
Run tdchain.out with DCHAIN again
Let’s change output time

--- SLIDE 22 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Answer
tdchain.out
…
! --- irradiation time ---
  itstep =       5
   2.0 h  1.0
   1.0 h  0.0
   1.0 h  0.5
   1.3 h  1.0

! --- output time ---
  itout =       9
   1.3 h
   2.0 h
   2.5 h
   3.0 h
   4.0 h
   4.7 h
   5.3 h
   -0.5 h   ! or 5.8 h
   -1.7 h   ! or 7.0 h
…
tdchain.eps

--- SLIDE 23 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2: Answer
…
! --- irradiation time ---
  itstep =       5
   2.0 h  1.0
   1.0 h  0.0
   1.0 h  0.5
   1.3 h  1.0

! --- output time ---
  itout =       9
   1.3 h
   2.0 h
   2.5 h
   3.0 h
   4.0 h
   4.7 h
   5.3 h
   -0.5 h   ! or 5.8 h
   -1.7 h   ! or 7.0 h
…
Cannot specify
output
times
End of the last irradiation step
End of the last specified timeevo interval
tdchain.out
ANSWER_FILE: input/exercise-3.inp

--- SLIDE 24 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Abstract
Parameter settings in [t-dchain]
Output files from DCHAIN
Exercises
Summary
Table of Contents
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 25 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
tdchain.act: Induced activity, decay heat*, and dose rates
Main Output File (*.act)
Many output files are generated from DCHAIN (see its manual for more details)
<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>
 <>-<>   no.     1  regionwise calculation data     <>-<>
 <>-<>   region label : DUMMY001                    <>-<>
 <>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>
beam current ......  1.0000E-04 [mA]
beam energy .......  3.0000E+00 [GeV]
beam power ........  3.0000E-04 [MW]
neutron flux ......  1.7699E+10 [n/cm**2/s]
region volume .....  1.9200E+02 [cm**3]
irradiation time ..  4.3000E+00 [h]
region number .....           1  (in nmtc yield file)

 --- output time --- 1.3000E+00 [h]   ( 4.6800000E+03 [s])
  nuclide         atoms       radioactivity         relative    rate                decay heat [W/cc]                half-life   dose-rate
             [atoms/cc]      [Bq/cc]         [Bq]    error       [%]        beta      gamma      alpha      total          [s]  [uSv*m^2/h]
   H   3     1.9626E+11   3.4990E+02   6.7180E+04  9.2808E-02          3.190E-13  0.000E+00  0.000E+00  3.190E-13    3.888E+08   0.000E+00
   He  6     1.5133E+06   1.3003E+06   2.4966E+08  4.9990E-01   0.33   3.266E-07  0.000E+00  0.000E+00  3.266E-07    8.067E-01   0.000E+00
   He  8     1.1171E+05   6.5016E+05   1.2483E+08  7.0710E-01   0.16   4.583E-07  8.573E-08  6.563E-10  5.447E-07    1.191E-01   1.667E+02
   Li  8     1.8435E+06   1.5214E+06   2.9210E+08  6.2389E-01   0.38   1.523E-06  0.000E+00  3.262E-09  1.526E-06    8.399E-01   3.451E+01
   Dy157     1.4402E+09   3.4070E+04   6.5414E+06  1.0000E+00          5.388E-11  1.894E-09  0.000E+00  1.948E-09    2.930E+04   3.665E+00
   Ho158     3.1532E+08   3.2236E+05   6.1893E+07  1.0000E+00   0.08   8.005E-09  1.224E-07  0.000E+00  1.304E-07    6.780E+02   2.126E+02...
Induced Activity (Bq/cm3 & Bq)
Inventory
Decay Heat (W/cm3)
Dose Rate (µSv*m2/hr)
Output timing
Cell/region
*Local energy deposition is assumed in the estimate of decay heat
SPEAKER_NOTES:
The *.act file is organized first by region and then by time step in each region.  With imode = 2 (the default value), each of these sections is subdivided into three subsections: (1) inventory/activity/decay heat/etc of all nuclides outputted, (2) gamma spectrum, (3) Summary and top 10 lists for most significant nuclides regarding activity, decay heat, and dose rate.

--- SLIDE 26 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Graphic Output File (*.eps)
Time variation for each cell (points+line) & total (thick line)
tdchain.eps
γ decay heat*
Dose rate**
α decay heat*
β decay heat*
Decay heat
Induced activity

--- SLIDE 27 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
tdchain.dcs: Shows how each nuclide is produced / destroyed
Can be used to determine what reactions are responsible for all transmutations in a simulation (and their inventory contributions)
Enabled with IWRTCHN = 1 (default)
Described in greater detail in the DCHAIN manual
Decay Chain Scheme (*.dcs)
--- during irradiation time (end of final substep,    50 of    50 ---
--- output time ---         10 [h]   ( 3.6000000E+04 [s])
Product  Chain number  N_i-1 [atm/cc] dN [atm/cc]  N_i [atm/cc] A_i [Bq/cc]  A_i [Bq]        Decay chain
Ar 39    (  1 of 100)  3.88664E+11    8.03157E+09  3.96696E+11  3.23874E+01  1.69580E+04     P  39  --(B-)->
A_i [Bq]        Decay chain
1.69580E+04     P  39  --(B-)->  S  39  --(B-)->  Cl 39  --(B-)->  Ar 39
      dN_Beam:                   1.87215E+05      5.20911E+07      7.29774E+09
  dN_Decay/nx:                   8.61687E+03      6.81577E+08     -2.28468E+04
     dN_Total:                   1.95831E+05      7.33669E+08      7.29771E+09
With IWRCHDT = 1 (0 by default) contributions from each reaction in each chain are listed too.
End nuclide
Change in inventory from this chain
Internal chain ID
Atoms of S and Cl (per cm3) transmuted to Ar-39 in this chain and calculation time step.
SPEAKER_NOTES:
This is one of the most advanced but powerful output files.
IWRCHDT shows how many atoms (per cm^3) of each nuclide in each chain were transmuted to the end nuclide through the reaction mechanisms shown.

Note that the numbers on this slide are an example taken from the DCHAIN manual and not from the actual simulations of this exercise.

--- SLIDE 28 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Abstract
Parameter settings in [t-dchain]
Output files from DCHAIN
Exercises
Summary
Table of Contents
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 29 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Objective (exercise.inp)
h10.eps (icntl = 8)
Calculate gamma-ray doses inside a small room after 100 nA & 10 minutes irradiation of 100 MeV proton beam on Fe target (10 x 10 x 10 cm)
100 MeV proton
Source:
100 MeV proton with 100 nA
Geometry:
Fe target (10 x 10 x 10 cm)
Vacuum room (40 x 40 x 40 cm)
Fe wall (5 cm thickness)
Tally:
[t-dchain] at the target (only 1 xyz-mesh) (Fe_target.out)
[t-track] for calculating H*(10) inside the room (H10.out)
3 step calculation (PHITS with [t-dchain] → DCHAIN → PHITS with [source] generated by DCHAIN) is required
Fe target
Fe wall
SPEAKER_NOTES:
Note that we will do the mesh = reg part first
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[T-DCHAIN]
mesh = xyz
…
file = Fe_target.out     timeevo =    1
   10.0 m 1.0

outtime =    3
    1.0 m
   10.0 m
   -30.0 m
idivs = 50
amp = 1.0
ipltmode = 1
iphtout = -20
iaonucl = 4
aonucl = Fe-53 ...
…
 idivs = 50
…
amp =  1.6022E-16 ! (mA)
…
! --- irradiation time ---
itstep =       1
1.0000E+01 m 1.0000E+00

! --- output time ---
itout =       3
      1.0000E+00 m
      1.0000E+01 m
     -3.0000E+01 m
…
ipltmode =       1
…
phitsout =  -20
…
angelout_nuclides   =  4
Fe-53 Co-54  Cr-55 Mn-51
idivs is the number of sub-step within a single time step: A smaller value results in shorter computational time but occasionally less accurate
The unit of amp in DCHAIN input file is mA instead of source/sec*
ipltmode = 1 enables DCHAIN 2D xy activity plot
phitsout is a control parameter for [source] generation option (see p.47)
iaonucl and aonucl specify the RIs to be shown in the EPS file of the time evolution of activities (see p.51)
Run PHITS & check output
exercise.inp
Fe_target.out
*In this PHITS input file, the beam current is normalized to 100 nA in [source], so amp =1
SPEAKER_NOTES:
Note the different irradiation schedule and output times from the other [T-Dchain] tally from earlier.
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
H*(10) distribution
H10.eps
Proton (page 1)
Neutron (page 2)
Photon (page 3)
[T-Track]
  title = H*(10) distribution
…
 multiplier = all     $ number of regions using multiplier
     mat    mset1
     all  ( 3600/1.0E+09 -200 ) $ convert pSv/sec to mSv/h
  z-txt = Ambient dose equivalent rate H*(10) [mSv/hr]
exercise.inp
Please see phits/advanced/options/ for how to set multiplier subsection
~104 mSv/h outside the wall due to secondary neutrons
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 32 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Fe_target.eps (page 1)
Run DCHAIN & check output
Activities of each RI are drawn in the figure due to specification of angelout_nuclides
53Fe is the dominant RI at the peak
The contributions from longer half-life RI such as 51Mn become important after certain cooling time
…
 idivs = 50
…
amp =  1.6022E-16 ! (mA)
…
! --- irradiation time ---
itstep =       1
1.0000E+01 m 1.0000E+00

! --- output time ---
itout =       3
      1.0000E+00 m
      1.0000E+01 m
     -3.0000E+01 m
…
ipltmode =       1
…
phitsout =  -20
…
angelout_nuclides   =  4
Fe-53 Co-54  Cr-55 Mn-51
Fe_target.out

--- SLIDE 33 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
*.pht output with [Source]
$||=======================================================||
$|| output time index :      2                            ||
$|| output time :         10 [m]   ( 6.0000000E+02 [s])   ||
$||=======================================================||

[ S o u r c e ]
  totfact =  56

 <source> =   1
   s-type =   22
     mesh =  xyz
…
   y-type =   2
     ymin =   -5.0
     ymax =    5.0
       ny =   1
   z-type =   2
     zmin =   -5.0
     zmax =    5.0
       nz =   1
  1.0000E+00     # nx=1-1, ny=1, nz=1
     proj = photon
   e-type =   28
       ni =   1
  P-30    2.0788E-01
     norm =   0
    dtime =     0.0
   iannih = 0
      dir = all
Fe_target_t*.pht (* indicates output time ID)
← Number of generated RIs*
← Information on output time
Same xyz mesh in [t-dchain]
(when mesh=reg, user must specify its rough area)
RI source (e-type = 28) with proj = photon for iphtout = -20
*Loading time becomes longer when numbers of produced RI and mesh are large
← s-type = 22 is xyz mesh distribution source*
Spatial distribution of each RI (only 1 mesh in this case)

--- SLIDE 34 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
$ Photon source from DCHAIN output
$ infl:{Fe_target_RIsrc_t2.pht}
$ You must "off" the [source] and [t-dchain] sections when you activate this command

[Source]
$ Beam settings to be used in [T-Dchain] tallies
…
[T-DCHAIN]
  mesh = xyz
…
exercise.inp
Activate “infl” command to include [source] generated by DCHAIN at the 2nd output time (t2)
Set “off” to the original [source] and [t-dchain] sections*
Run PHITS with exercise.inp and check H10.eps
Let’s calculate γ-ray doses just after the irradiation
Exercise 1
*You can keep the [t-dchain] section, but its output file is overwritten
MENTIONED_INPUT_NAMES: exercise.inp
ANSWER_FILE: input/exercise-2.inp

--- SLIDE 35 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
$ Photon source from DCHAIN output
infl:{Fe_target_RIsrc_t2.pht}
…

[Source] off
$ Beam settings to be used …
…
[T-DCHAIN] off
  mesh = xyz
…
exercise.inp
Answer 1
H10.eps (page 3)
H*(10) outside of the wall are approximately 0.1 mSv/h
γ-rays are uniformly generated in the Fe target because only 1 xyz-mesh is defined in [t-dchain]
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 36 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
$ Photon source from DCHAIN output
infl:{Fe_target_RIsrc_t2.pht}
$ You must "off" the [source] and [t-dchain] sections when you activate this command
…
exercise.inp
Change the include file name to the 3rd output time (t3)
Run PHITS with exercise.inp and check H10.eps
Let’s calculate γ-ray doses 30 minutes after the irradiation
Exercise 2
MENTIONED_INPUT_NAMES: exercise.inp
ANSWER_FILE: input/exercise-3.inp

--- SLIDE 37 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
$ Photon source from DCHAIN output
infl:{Fe_target_RIsrc_t3.pht}
…
exercise.inp
Answer 2
H10.eps (page 3)
H*(10) outside of the wall decrease approximately one-order of magnitude (~0.01 mSv/h) due to the decay of RIs
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 38 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
$ Photon source …
infl:{Fe_target_RIsrc_t3.pht}

[Source] off
$ Beam settings …
…
[T-DCHAIN] off
  mesh = xyz
 x-type = 2
      nx = 1
    xmin = -c1
    xmax =  c1
  y-type = 2
      ny = 1
    ymin = -c1
    ymax =  c1
  z-type = 2
      nz = 1
    zmin = -c1
    zmax =  c1
exercise.inp
Comment out “infl” command to include DCHAIN [source]
Activate the original [source] and [t-dchain]
Increase the number of xyz mesh (nx = ny = nz = 3) in [t-dchain]

Run PHITS with revised exercise.inp
Run DCHAIN with Fe_target.out (takes long time)
Check Fe_target_pxy.eps for activity distributions*

Activate “infl” command again to include the updated Fe_target_RIsrc_t3.pht into exercise.inp
Deactivate the original [source] and [t-dchain]
Run PHITS with revised exercise.inp
Let’s consider spatial distribution of γ-ray generation
Exercise 3
*Generated only when ipltmode = 1
MENTIONED_INPUT_NAMES: exercise.inp
ANSWER_FILE: input/exercise-3.inp

--- SLIDE 39 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
$ Photon source …
infl:{Fe_target_RIsrc_t3.pht}

[Source] off
$ Beam settings …
…
[T-DCHAIN] off
  mesh = xyz
 x-type = 2
      nx = 3
    xmin = -c1
    xmax =  c1
  y-type = 2
      ny = 3
    ymin = -c1
    ymax =  c1
  z-type = 2
      nz = 3
    zmin = -c1
    zmax =  c1
exercise.inp
Answer 3
Fe_target_pxy.eps (page 1)
H10.eps (page 3)
Activities are concentrated at the center near the irradiation surface
After the 2nd PHITS simulation
γ-ray doses at the left (irradiation) side are higher due to heterogeneity of the activities in the Fe target
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 40 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
htitle = [t-dchain]  in xyz mesh

! --- control parameters ---
     imode =       2
     jmode =       2

! --- calculation parameters ---
     idivs =      50
…
Fe_target.out
Change idivs in Fe_target.out to 5, run DCHAIN, and check Fe_target.eps
Run PHITS with exercise.inp including updated Fe_target_RIsrc_t3.pht and check H10.eps
Reduce computational time of DCHAIN
Exercise 4
idivs is the number of sub-step within a single time step.
A smaller idivs results in shorter computational time but occasionally less accurate
In general, it can be decreased unless production/depletion rates of important nuclides change within any single irradiation time step
MENTIONED_INPUT_NAMES: exercise.inp
ANSWER_FILE: (missing)

--- SLIDE 41 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
! --- calculation parameters ---
     idivs =      5
…
Fe_target.out
Answer 4
Fe_target.eps (page 1)
H10.eps (page 3)
Almost unchanged, but the computational time of DCHAIN should be reduced to roughly 1/5

--- SLIDE 42 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Abstract
Parameter settings in [t-dchain]
Output files from DCHAIN
Exercises
Summary
Table of Contents
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 43 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
DCHAIN can calculate the time variation of induced activities, decay heats, γ-ray spectra, and dose rates during irradiation and cooling time
PHITS automatically generates an input file for DCHAIN by using the [t-dchain] tally
And can be used for easily modeling transport of the decay radiation calculated by DCHAIN
Combination of PHITS & DCHAIN enables estimation of the long-term variation of induced activity in complex environments, important for the design of nuclear and accelerator facilities
Summary

--- SLIDE 44 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Supplemental Information

--- SLIDE 45 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Change materials in DCHAIN
For the evaluation of induced radioactivity in facilities planned for long-term operation, it is essential to include an assessment of impurities such as Co and Eu, which tend to produce long-lived radionuclides
Since their abundances are generally trivial, evaluating their effects for various concentrations without recalculating PHITS is possible*.
To change material compositions in DCHAIN, change the number of elements (itgnucls) and add elements."
!1)HRGCMM 2)IREGS 3)ITGNCLS 4)FLUXS 5)HNFLUXS 6)VOLUMES
   DUMMY003        3    4  9.3610E+08   tdchain.dtrk  3.2000E+02
  Fe-54      4.9642E-03
  Fe-56      7.7928E-02
  Fe-57      1.7997E-03
  Fe-58      2.3951E-04
tdchain.out
!1)HRGCMM 2)IREGS 3)ITGNCLS 4)FLUXS 5)HNFLUXS 6)VOLUMES
   DUMMY003        3    5  9.3610E+08   tdchain.dtrk  3.2000E+02
  Fe-54      4.9642E-03
  Fe-56      7.7928E-02
  Fe-57      1.7997E-03
  Fe-58      2.3951E-04
  Co-59      1.0e-7
tdchain.out
*Recalculation of PHITS is required when neutrons above 20 MeV or ions predominantly produce the long-live radionuclides

--- SLIDE 46 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
DCHAIN reaction types
DCHAIN has 3 basic categories of reactions:
Decay reactions
using DCHAIN’s decay library
Neutron-induced reactions below 20 MeV
using the [t-track] neutron flux with DCHAIN’s activation cross section library
Everything else
using the [t-yield] nuclide yields
The JMODE parameter controls which of these three are considered (default JMODE = 2 considers all three)
Note: Fission is included in categories 1 (spontaneous fission) and 2 (neutron induced fission) and additionally uses DCHAIN’s fission yield data libraries.
SPEAKER_NOTES:
The JMODE input parameter considers which of these 3 are used in a DCHAIN calculation

DCHAIN considers 3 categories of reaction mechanisms:
1) Decay (using DCHAIN’s decay library)
2) Neutron reactions under 20 MeV (using DCHAIN’s activation cross section library and the [t-track] neutron flux)
3) Everything else (using the [t-yield] nuclide yields)
*Note that fission is included in categories 1 (spontaneous fission) and 2 (neutron induced fission) and also utilizes additional fission yield libraries inside of DCHAIN.

--- SLIDE 47 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[source] output option
iphtout in PHITS / phitsout in DCHAIN
When the last digit of iphtout/phitsout is 1, [source] based on DCHAIN’s gamma-ray database* written in e-type = 4 is also output (e.g. both RI source with proj = all and DCHAIN database sources are generated when iphtout = 11
When iphtout/phitsout is specified in a negative value, [source] sections for each output timing are separately generated in different files (*_t1.pht, *_t2.pht…)
0 or 1: No output for [source] section based on RI source
10 or 11: RI source with proj = all
20 or 21: RI source with proj = photon
30 or 31: RI source with proj = electron
40 or 41: RI source with proj = positron
50 or 51: RI source with proj = alpha
Notes
*Energy resolution is poorer in comparison to RI source function in PHITS

--- SLIDE 48 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[t-dchain] with xyz or reg mesh?
Advantages of xyz-mesh source
Spatial distribution inside the source region can be considered and output in an eps file*
User does not have to provide the approximate coordinates of the source region in *.pht file
Disadvantages of xyz-mesh source
Rather long computational time particularly when the number of meshes is large
Complicated source shape that cannot be represented by rectangles cannot be considered

--- SLIDE 49 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
Additional Information on Output Files from DCHAIN

--- SLIDE 50 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
ACMIN – controls threshold inventory/activity necessary for printing nuclides. (D = total activity x 10-10)
ISTABL – toggle whether stable nuclides are printed (D = 0: not printed)
IDOSECF, IDOSUNIT – control γ–ray dose rate coefficients used and units reported. The default is Effective dose based on ICRP Pub. 116 for AP irradiation in the unit of uSv.m2/hr.
INXSLIB, IDCYLIB, INFYLIB, ISFYLIB – control source of evaluated nuclear data for activation cross sections, decay data, and fission yields used by DCHAIN
Parameters relevant to *.act

--- SLIDE 51 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
IANGBPWR – toggles display of beam power schedule 	overlay (the red/pink bars)
ANGELOUT_REGION † – specify which regions (some, all, 	and/or sum of all regions) are displayed
ANGELOUT_NUCLIDES † – select specific nuclides to plot 	(summed over all regions)
Parameters relevant to *.eps
†These parameters can be changed in the [T-Dchain] section as below:
  aoreg = 1  5   7
  iaonucl = 3
  aonucl = Mn-56  Fe-53  Fe-53m
Note that ANGELOUT_REGION is changed to aoreg, while ANGELOUT_NUCLIDE is changed to iaonucl in [T-Dchain]

--- SLIDE 52 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
CHRLVTH – controls threshold change in inventory/activity 	necessary for chains to be printed (similar to ACMIN, 	good for filtering out many “useless” chains)
IWRCHDT – toggles display of contribution to inventory 	changes from each reaction in each chain
IWRCHSS – display all calculation steps, including  the 	IDIVS substeps in each irradiation period (usually hidden)
IWRCHNUC – Only include chains ending in the 	production/destruction of select specified nuclides
Parameters relevant to *.dcs
SPEAKER_NOTES:
This file can be quite long, and these parameters control what gets printed, greatly impacting the length of the file depending on your desired level of detail.

--- SLIDE 01 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
PHITSとDCHAINを組み合わせた
誘導放射能計算
2025年9月改訂
phits/lecture/advanced/DCHAIN1

--- SLIDE 02 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
放射線挙動解析コードPHITS
ナノ秒オーダーの放射線挙動を解析
照射直後に生成される誘導放射能は計算できるが、その崩壊による時間変化を推定することはできない
誘導放射能計算コードDCHAIN
照射中・照射後の誘導放射能の時間変化を任意の時間スケールで解析
崩壊による発熱やガンマ線スペクトルの評価も可能
本実習では、PHITSとDCHAINの接続計算による誘導放射能評価方法を学習します
本実習の目的

--- SLIDE 03 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
PHITS-DCHAIN接続計算の概要
[t-dchain]とDCHAINの使い方
DCHAIN出力ファイルの解説
演習
まとめ
参考資料（計算原理と注意事項）
実習内容

--- SLIDE 04 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
PHITS-DCHAIN接続計算の流れ
PHITS
放射線挙動解析
DCHAIN入力ファイル (“file=”で指定したファイル名)
[t-yield]で計算した誘導放射能 （ただし20MeV以下の中性子による寄与は除く）（*.dyld）
[t-track]で計算した20MeV以下の中性子フラックス（*.dtrk)
DCHAINのデータフォルダ名 (dch_link.dat)
[t-dchain]からの出力
DCHAIN
核壊変連鎖の計算
DCHAIN用データライブラリ
20MeV以下の中性子放射化断面積
核壊変データ (娘核、分岐比、γ線エネルギースペクトル、崩壊熱など）
核分裂生成核種収率
計算結果
誘導放射能（Bq)
崩壊熱 （W）
放出γ線スペクトル
γ線遮へい計算
任意のビーム出力・時間における

--- SLIDE 05 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
PHITS-DCHAIN接続計算を実行
dchain.inpをPHITSで実行 (送る -> PHITS)
(tdchain.out, .dtrk, .dyld, and dch_link.datなどが出力される)
（tdchain.lst, .act, .pht, .ang, .gsd, .gso, .alr, .eps, .dcsなどが出力される）
tdchain.outをDCHAINで実行する（送る -> DCHAIN）
Time variation of induced activity in each cell
tdchain.eps

--- SLIDE 06 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[t-dchain]からの出力ファイル
tdchain.out: DCHAIN入力ファイル
          （ファイル名は[t-dchain]の“file=”で指定した名前)
tdchain.dyld: [t-yield]で計算した核種生成率（ただし、20MeV以下の中性子による寄与は除く）
tdchain.dtrk: [t-track]で計算した20MeV以下の中性子フルエンス*
dch_link.dat: DCHAIN用のデータベースを格納したフォルダ名         (“file(21)=”で指定した値もしくはfile(1)/dchain-sp/data）
*原理的には[t-yield]で計算した核種生成率のみから誘導放射能の時間変化は計算可能だが、低エネルギー中性子の複雑な共鳴反応などを正確に考慮するためには、DCHAINに含まれる専用の中性子放射化断面積ライブラリを用いる必要がある
SPEAKER_NOTES:
Note that the [t-yield] tally is essentially the “everything else” category of reaction products outside of the <20 MeV neutron reactions.

--- SLIDE 07 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
DCHAINからの出力ファイル
tdchain.act: メイン出力（誘導放射能、崩壊熱、線量率、
tdchain.ｌｓｔ: 標準出力 (PHITSにおけるphits.outのような役割)
tdchain.dcs: 核壊変連鎖や反応に関する情報
tdchain.ang: ANGEL形式での誘導放射能、崩壊熱、線量率情報
tdchain.eps: 上記ファイルをANGELで処理して出力した画像ファイル
tdchain.mat: PHITSの[Material]形式で出力された放射化物質情報
tdchain.alr:全領域を合計した誘導放射能及び崩壊熱の情報
放出γ線スペクトル情報）
実行時エラーの詳細情報が出力される場合もある

--- SLIDE 08 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
DCHAINで指定するパラメータは、基本的に [t-dchain]内にて直接指定することができる
本実習で説明するamp, idivs, phitsoutなどいくつかのパラメータを除き、基本的には、DCHAINのパラメータをユーザーが変更する必要はありません。もし変更する場合は、DCHAINマニュアルを参照して適切な値に設定してください

*/phits/dchain-sp/manual/DCHAIN_input_manual_jp.pdf
インプットパラメータの変更方法

--- SLIDE 09 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
実習内容
PHITS-DCHAIN接続計算の概要
[t-dchain]とDCHAINの使い方
DCHAIN出力ファイルの解説
演習
まとめ
参考資料（計算原理と注意事項）

--- SLIDE 10 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
dchain.inpの計算体系
250MeV陽子をW / H2O / Fe ターゲットに入射
(8 cm x 8 cm x 3/10/5 cm)

ターゲットはBeケースに格納

それ以外は真空
yz-track.eps (if icntl = 8)

--- SLIDE 11 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
計算結果の確認
yz-track.eps
陽子フラックス
（１ページ目）
中性子フラックス
（2ページ目）

--- SLIDE 12 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[T-Dchain]を使う際の奨励設定
dchain.inp
[Parameters]
...
$  required options for DCHAIN
jmout	=         1  # (D=0) Density echo, 0:input, 1:number density
e-mode	=         0  # (D=0) Event generator mode is not recommended
$ recommended option for isomer production
igamma	=         3  $ (D=2) 0:No, 1:Old, 2:EBITEM,3:EBITEM+Isomer
…

[Volume]   $ required section for DCHAIN
    reg   vol
     1   c1*(2*c5)**2  $ Tungsten (W)
     2   c2*(2*c5)**2  $ Water (H2O)
     3   c3*(2*c5)**2  $ Iron (Fe)
     4   ((c1+c2+c3+c4)*(2*c6)**2)-((c1+c2+c3)*(2*c5)**2)  $ Be
物質の原子数密度情報がDCHAINで必要なため jmout = 1とする
イベントジェネレータモードは使用しない （e-mode = 0)
核異性体（meta stable）の生成を考慮する（igamma = 3）
[t-dchain]でmesh=regとする場合は、その領域の体積を[volume] セクションで定義
set:c1[3]   	$ thickness of W set:c2[10]	$ thickness of H2O set:c3[5]   	$ thickness of Fe
set:c4[5]   	$ thickness of Be  	   back end
set:c5[4]   	$ half side length   	   of inner block
set:c6[8]   	$ half side length 	   of outer block
SPEAKER_NOTES:
From v3.33, jmout defaults to 1 if a [t-dchain] tally is present, otherwise it retains its default value of 0.
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
JENDL-5の利用
dchain.inp
[Parameters]
...
$  recommended use for activation calculation, installation of JENDL-5 is required
 dmax(1)  =  200.000000     # (D=emin(1)) data max. energy of proton (MeV)
 dmax(2)  =  200.000000     # (D=20.0) data max. energy of neutron (MeV)
$ dmax(15) =  100.000000     # (D=emin(15)) data max. energy of deuteron (MeV/n)
$ dmax(18) =  50.000000     # (D=emin(18)) data max. energy of alpha (MeV/n)
$ dpnmax   =  200.000000     # (D=emin(14)) data max. energy for photo-nuclear lib. (MeV)
…
高エネルギー中性子、陽子、重陽子、α粒子、光子による放射化を計算したい場合は、それらに対するJENDL-5の利用を奨励（核データを使うことにより[t-yield]で放射化断面積が利用されるため）
DCHAINを使う前に、XSフォルダにあるJENDL-5のインストーラを使ってJENDL-5をインストールすることを奨励*
*この資料では、JENDL-5をインストールしていないPHITSで得られた結果を示す
SPEAKER_NOTES:
From v3.33, jmout defaults to 1 if a [t-dchain] tally is present, otherwise it retains its default value of 0.
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[T-Dchain]のパラメータ①
dchain.inp
基本パラメータ
・ mesh (“reg”, “xyz”もしくは“tet”）

・ file: DCHAINのインプットファイル名

・ amp: 最大ビーム電流(source/sec）
[ T-DCHAIN ]
  title = 250 MeV protons on core
  mesh =  reg
  reg =  1 2 3
  file = tdchain.out
  timeevo =    1
     2.0 h  1.0
  outtime =    7
     1 h
     2 h
     3 h  $ or -1 h
     4 h  $ or -2 h
     5 h  $ or -3 h
     6 h  $ or -4 h
     7 h  $ or -5 h
set:c11[100.0]  $ beam current (nA)
set:c12[c11*1.0e-9/1.602177e-19]
amp = c12 $ Source Intensity (#/sec)
DCHAINの出力ファイル名（***.dtrk, ***.dyld, ***_err.dyld, ***.dout, ***.lst, ***.yld, ***.gsd, ***.gso, ***.alr, ***.act, ***.ang, ***.pht, ***.dcs, ***.mat, dch_link.dat, yield.out)は使用不可
mesh = r-zには未対応
totfactが指定されている場合は、totfact x ampが最大出力となるようにampを調整
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
timeevo：照射及び冷却時間のステップ数。この行の後に時間と相対ビーム強度（1.0がampに相当）を入力
時間は各ステップの時間幅, Δt
例:
2.0 h 1.0 → 2時間フルパワー（amp強度)で照射
そのあとは冷却 (ビームオフ)
単位はs (秒), m (分), h (時), d (日), y (年)
スペース区切りで入力
[ T-DCHAIN ]
  title = 250 MeV protons on core
  mesh =  reg
  reg =  1 2 3
  file = tdchain.out
  timeevo =    1
     2.0 h  1.0
  outtime =    7
     1 h
     2 h
     3 h  $ or -1 h
     4 h  $ or -2 h
     5 h  $ or -3 h
     6 h  $ or -4 h
     7 h  $ or -5 h
set:c11[100.0]  $ beam current (nA)
set:c12[c11*1.0e-9/1.602177e-19]
amp = c12 $ Source Intensity (#/sec)
dchain.inp
[T-Dchain]のパラメータ②
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 16 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
outtime：結果を出力する時間の数
この行の後に、timeevoと同じく出力する時間を入力する
正値で指定した場合は、最初のタイムステップ（timeevo = 0）からの時間タイミング
負値で指定した場合は、直前の照射終了時からの時間タイミング
[ T-DCHAIN ]
  title = 250 MeV protons on core
  mesh =  reg
  reg =  1 2 3
  file = tdchain.out
  timeevo =    1
     2.0 h  1.0
  outtime =    7
     1 h
     2 h
     3 h  $ or -1 h
     4 h  $ or -2 h
     5 h  $ or -3 h
     6 h  $ or -4 h
     7 h  $ or -5 h
set:c11[100.0]  $ beam current (nA)
set:c12[c11*1.0e-9/1.602177e-19]
amp = c12 $ Source Intensity (#/sec)
dchain.inp
[T-Dchain]のパラメータ③
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
誘導放射能の時間変化を確認
dchain.inp
tdchain.eps
[ T-DCHAIN ]
…
timeevo =    1
   2.0 h  1.0

outtime =   7
   1 h
   2 h
   3 h  $ or -1 h
   4 h  $ or -2 h
   5 h  $ or -3 h
   6 h  $ or -4 h
   7 h  $ or -5 h
…
SPEAKER_NOTES:
Make note that the tungsten region is the most activated here.  This is the motivation for only looking at the tungsten region later in the example.
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[ T-DCHAIN ]
  title = 250 MeV protons on core
  mesh =  reg
  reg =  1 2 3
  file = tdchain.out
  timeevo =    1
     2.0 h  1.0
  outtime =    7
     1 h
     2 h
     3 h  $ or -1 h
     4 h  $ or -2 h
     5 h  $ or -3 h
     6 h  $ or -4 h
     7 h  $ or -5 h
set:c11[100.0]  $ beam current (nA)
set:c12[c11*1.0e-9/1.602177e-19]
amp = c12 $ Source Intensity (#/sec)
[t-dchain]で定義したパラメータがそのままDCHAIN入力ファイルに書き出される（ただしパラメータ名が異なる場合がある）
timeevo, outtimeなどPHITSの結果に直接関係ないパラメータ*を変更したい場合は、DCHAINの入力ファイルを直接編集してDCHAINのみ再実行すればよい
DCHAIN入力ファイル
dchain.inp
tdchain.out
…
amp =  1.0000E-04  ! (mA)
…
! --- irradiation time ---
itstep =       1
 2.0000E+00 h  1.0000E+00

! --- output time ---
itout =       7
      1.0000E+00 h
      2.0000E+00 h
      3.0000E+00 h
      4.0000E+00 h
      5.0000E+00 h
      6.0000E+00 h
      7.0000E+00 h
…
*ampは[t-yield]の結果に影響する。また、単位がsource/secからmA単位に自動で変換されるので注意
SPEAKER_NOTES:
As a warning, if you increase AMP in PHITS [T-Dchain], in the DCHAIN input it will increase both the AMP parameter (used for scaling nuclides produced from the [T-Yield] tally) and FLUXS in each region (total neutron flux tallied by [T-Track] scaled by source intensity, used for nuclides produced/consumed by neutron reactions).  If you want to scale the total intensity of the beam without rerunning PHITS, this is most easily accomplished by just changing the beam intensity in the irradiation schedule section (istep) rather than adjusting AMP and the FLUXS value(s).
MENTIONED_INPUT_NAMES: dchain.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
照射時間・強度を変更してみよう
tdchain.out
…
! --- irradiation time ---
itstep =       1
   2.0000E+00 h  1.0000E+00

! --- output time ---
itout =       7
      1.0000E+00 h
      2.0000E+00 h
      3.0000E+00 h
      4.0000E+00 h
      5.0000E+00 h
      6.0000E+00 h
      7.0000E+00 h
…
tdchain.outをエディタで開いてitstepを探す
照射スケジュールを以下に変更:
2.0 hours beam at full power
1.0 hour of cooling (beam off)
1.0 hour of beam at half power
1.3 hours of beam at full power
1.7 hours of cooling (beam off)
tdchain.outをDCHAINで実行

--- SLIDE 20 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
tdchain.out
…
! --- irradiation time ---
itstep =       5
   2.0 h  1.0
   1.0 h  0.0
   1.0 h  0.5
   1.3 h  1.0

! --- output time ---
itout =       7
      1.0000E+00 h
      2.0000E+00 h
      3.0000E+00 h
      4.0000E+00 h
      5.0000E+00 h
      6.0000E+00 h
      7.0000E+00 h
…
tdchain.eps
変更した照射スケジュールにしたがってビーム出力や誘導放射能が変化した
照射時間・強度を変更してみよう

--- SLIDE 21 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
出力時間を変更してみよう
tdchain.out
…
! --- irradiation time ---
itstep =       5
   2.0 h  1.0
   1.0 h  0.0
   1.0 h  0.5
   1.3 h  1.0

! --- output time ---
itout =       7
      1.0000E+00 h
      2.0000E+00 h
      3.0000E+00 h
      4.0000E+00 h
      5.0000E+00 h
      6.0000E+00 h
      7.0000E+00 h
…
tdchain.outでitoutを探す
出力時間を以下に変更:
1.3 hours after the start of irradiation
2.0 hours after the start of irradiation
2.5 hours after the start of irradiation
3.0 hours after the start of irradiation
4.0 hours after the start of irradiation
4.7 hours after the start of irradiation
5.3 hours after the start of irradiation
5.8 hours after the start of irradiation
7.0 hours after the start of irradiation
tdchain.outをDCHAINで実行
最後の２ステップを負値（照射終了時からの時間）に変更してDCHAINを再実行

--- SLIDE 22 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
tdchain.out
…
! --- irradiation time ---
  itstep =       5
   2.0 h  1.0
   1.0 h  0.0
   1.0 h  0.5
   1.3 h  1.0

! --- output time ---
  itout =       9
   1.3 h
   2.0 h
   2.5 h
   3.0 h
   4.0 h
   4.7 h
   5.3 h
   -0.5 h   ! or 5.8 h
   -1.7 h   ! or 7.0 h
…
tdchain.eps
出力時間を変更してみよう

--- SLIDE 23 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
解答2（つづき）
…
! --- irradiation time ---
  itstep =       5
   2.0 h  1.0
   1.0 h  0.0
   1.0 h  0.5
   1.3 h  1.0

! --- output time ---
  itout =       9
   1.3 h
   2.0 h
   2.5 h
   3.0 h
   4.0 h
   4.7 h
   5.3 h
   -0.5 h   ! or 5.8 h
   -1.7 h   ! or 7.0 h
…
ここはitoutで定義できない
最後の照射終了時間
timeevoで定義した最後の時間ステップ終了時間
tdchain.out

--- SLIDE 24 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
実習内容
PHITS-DCHAIN接続計算の概要
[t-dchain]とDCHAINの使い方
DCHAIN出力ファイルの解説
演習
まとめ
参考資料（計算原理と注意事項）

--- SLIDE 25 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
tdchain.act: 誘導放射能、崩壊熱*、線量率が確認できる
メイン出力ファイル(*.act)
<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>
 <>-<>   no.     1  regionwise calculation data     <>-<>
 <>-<>   region label : DUMMY001                    <>-<>
 <>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>
beam current ......  1.0000E-04 [mA]
beam energy .......  3.0000E+00 [GeV]
beam power ........  3.0000E-04 [MW]
neutron flux ......  1.7699E+10 [n/cm**2/s]
region volume .....  1.9200E+02 [cm**3]
irradiation time ..  4.3000E+00 [h]
region number .....           1  (in nmtc yield file)

 --- output time --- 1.3000E+00 [h]   ( 4.6800000E+03 [s])
  nuclide         atoms       radioactivity         relative    rate                decay heat [W/cc]                half-life   dose-rate
             [atoms/cc]      [Bq/cc]         [Bq]    error       [%]        beta      gamma      alpha      total          [s]  [uSv*m^2/h]
   H   3     1.9626E+11   3.4990E+02   6.7180E+04  9.2808E-02          3.190E-13  0.000E+00  0.000E+00  3.190E-13    3.888E+08   0.000E+00
   He  6     1.5133E+06   1.3003E+06   2.4966E+08  4.9990E-01   0.33   3.266E-07  0.000E+00  0.000E+00  3.266E-07    8.067E-01   0.000E+00
   He  8     1.1171E+05   6.5016E+05   1.2483E+08  7.0710E-01   0.16   4.583E-07  8.573E-08  6.563E-10  5.447E-07    1.191E-01   1.667E+02
   Li  8     1.8435E+06   1.5214E+06   2.9210E+08  6.2389E-01   0.38   1.523E-06  0.000E+00  3.262E-09  1.526E-06    8.399E-01   3.451E+01
   Dy157     1.4402E+09   3.4070E+04   6.5414E+06  1.0000E+00          5.388E-11  1.894E-09  0.000E+00  1.948E-09    2.930E+04   3.665E+00
   Ho158     3.1532E+08   3.2236E+05   6.1893E+07  1.0000E+00   0.08   8.005E-09  1.224E-07  0.000E+00  1.304E-07    6.780E+02   2.126E+02...
誘導放射能 (Bq/cm3 & Bq)
生成核種
崩壊熱
 (W/cm3)
線量率 (µSv*m2/hr)
出力時間タイミング
セル番号
*崩壊熱は、ローカル近似（その場所に全てのエネルギーが付与される）で推定
SPEAKER_NOTES:
The *.act file is organized first by region and then by time step in each region.  With imode = 2 (the default value), each of these sections is subdivided into three subsections: (1) inventory/activity/decay heat/etc of all nuclides outputted, (2) gamma spectrum, (3) Summary and top 10 lists for most significant nuclides regarding activity, decay heat, and dose rate.

--- SLIDE 26 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
画像出力(*.eps)
*.actに出力された各領域（マーク＋細線）とその合計値（太線）が時間の関数としてグラフ表示される
tdchain.eps
γ decay heat*
Dose rate**
α decay heat*
β decay heat*
Decay heat
Induced activity

--- SLIDE 27 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
tdchain.dcs: 各核種の壊変連鎖スキーム（Decay Chain Scheme）
各核種がどのような壊変経路で生成されたか、その寄与も含めて調査できる
IWRTCHN = 1 (default)の場合のみ出力される
詳細はDCHAINマニュアル参照
核壊変連鎖出力ファイル (*.dcs)
--- during irradiation time (end of final substep,    50 of    50 ---
--- output time ---         10 [h]   ( 3.6000000E+04 [s])
Product  Chain number  N_i-1 [atm/cc] dN [atm/cc]  N_i [atm/cc] A_i [Bq/cc]  A_i [Bq]        Decay chain
Ar 39    (  1 of 100)  3.88664E+11    8.03157E+09  3.96696E+11  3.23874E+01  1.69580E+04     P  39  --(B-)->
A_i [Bq]        Decay chain
1.69580E+04     P  39  --(B-)->  S  39  --(B-)->  Cl 39  --(B-)->  Ar 39
      dN_Beam:                   1.87215E+05      5.20911E+07      7.29774E+09
  dN_Decay/nx:                   8.61687E+03      6.81577E+08     -2.28468E+04
     dN_Total:                   1.95831E+05      7.33669E+08      7.29771E+09
IWRCHDT = 1 (デフォルト値は0）の場合は、 各壊変連鎖の各反応ごとの寄与が出力される
最終核種
この壊変経路による生成量
壊変連鎖ID
S-39とCl-39が壊変してAr-39 になった原子数(per cm3)
SPEAKER_NOTES:
This is one of the most advanced but powerful output files.
IWRCHDT shows how many atoms (per cm^3) of each nuclide in each chain were transmuted to the end nuclide through the reaction mechanisms shown.

Note that the numbers on this slide are an example taken from the DCHAIN manual and not from the actual simulations of this exercise.

--- SLIDE 28 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
実習内容
PHITS-DCHAIN接続計算の概要
[t-dchain]とDCHAINの使い方
DCHAIN出力ファイルの解説
演習
まとめ
参考資料（計算原理と注意事項）

--- SLIDE 29 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
演習の目的 (exercise.inp)
h10.eps (icntl = 8)
100 MeV 陽子ビームを Fe ターゲット（10×10×10 cm）に 100 nA・10 分間照射した後の鉄箱内外におけるγ線線量を計算しよう
100 MeV 陽子
線源:
100 MeV陽子（100 nAに規格化）
体系:
鉄ターゲット (10 x 10 x 10 cm)
真空 (40 x 40 x 40 cm)
鉄箱 (5 cm thickness)
Tally:
[t-dchain]（ターゲット領域を1つのxyzメッシュで定義) (file=Fe_target.out)
[t-track] （鉄箱内のH*(10)を計算） (file=H10.out)
PHITS with [t-dchain] → DCHAIN → PHITS with [source] generated by DCHAINの３段階計算が必要
鉄ターゲット
鉄箱
SPEAKER_NOTES:
Note that we will do the mesh = reg part first
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
[T-DCHAIN]
mesh = xyz
…
file = Fe_target.out     timeevo =    1
   10.0 m 1.0

outtime =    3
    1.0 m
   10.0 m
   -30.0 m
idivs = 50
amp = 1.0
ipltmode = 1
iphtout = -20
iaonucl = 4
aonucl = Fe-53 ...
…
 idivs = 50
…
amp =  1.6022E-16 ! (mA)
…
! --- irradiation time ---
itstep =       1
1.0000E+01 m 1.0000E+00

! --- output time ---
itout =       3
      1.0000E+00 m
      1.0000E+01 m
     -3.0000E+01 m
…
ipltmode =       1
…
phitsout =  -20
…
angelout_nuclides   =  4
Fe-53 Co-54  Cr-55 Mn-51
idivsは１つのタイムステップをDCHAIN内部計算で分割する数。小さくすると計算時間が短くなるが場合によっては精度が下がる
DCHAIN入力ファイルでのamp単位はmAであることに注意*
ipltmode = 1とするとDCHAINで計算した放射能空間分布がepsファイル形式で出力される
phitsoutはDCHAINにより出力するPHITS[source]セクションの形式を指定(詳細は53ページ参照)
iaonuclとaonuclはDCHAINで出力する放射能時間変化画像ファイルにRI別の寄与を加えるオプション（詳細は57ページ参照)
PHITSを実行して結果を確認
exercise.inp
Fe_target.out
*この入力ファイルではtotfactを使って規格化しているため[t-dchain]ではamp = 1と設定
SPEAKER_NOTES:
Note the different irradiation schedule and output times from the other [T-Dchain] tally from earlier.
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
H*(10)の空間分布
H10.eps
Proton (page 1)
Neutron (page 2)
Photon (page 3)
[T-Track]
  title = H*(10) distribution
…
 multiplier = all     $ number of regions using multiplier
     mat    mset1
     all  ( 3600/1.0E+09 -200 ) $ convert pSv/sec to mSv/h
  z-txt = Ambient dose equivalent rate H*(10) [mSv/hr]
exercise.inp
multiplierサブセクションの定義方法はphits/advanced/options/を参照
鉄箱の外側では104 mSv/h程度（２次中性子による寄与が支配的）
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 32 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
DCHAINを実行して結果を確認
核種毎の放射能が出力される（angelout_nuclidesが定義されているため）
照射直後は53Feなど短半減期核種が支配的
ある程度冷却時間が経つと51Mnなど長半減期核種が重要となる
…
 idivs = 50
…
amp =  1.6022E-16 ! (mA)
…
! --- irradiation time ---
itstep =       1
1.0000E+01 m 1.0000E+00

! --- output time ---
itout =       3
      1.0000E+00 m
      1.0000E+01 m
     -3.0000E+01 m
…
ipltmode =       1
…
phitsout =  -20
…
angelout_nuclides   =  4
Fe-53 Co-54  Cr-55 Mn-51
Fe_target.out
Fe_target.eps (page 1)

--- SLIDE 33 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
DCHAINより出力された[source] (*.pht)
$||=======================================================||
$|| output time index :      2                            ||
$|| output time :         10 [m]   ( 6.0000000E+02 [s])   ||
$||=======================================================||

[ S o u r c e ]
  totfact =  56

 <source> =   1
   s-type =   22
     mesh =  xyz
…
   y-type =   2
     ymin =   -5.0
     ymax =    5.0
       ny =   1
   z-type =   2
     zmin =   -5.0
     zmax =    5.0
       nz =   1
  1.0000E+00     # nx=1-1, ny=1, nz=1
     proj = photon
   e-type =   28
       ni =   1
  P-30    2.0788E-01
     norm =   0
    dtime =     0.0
   iannih = 0
      dir = all
Fe_target_RIsrc_t*.pht (*は出力時間ID）
← 生成されたRI核種の数*
← Information on output time
[t-dchain]のxyzメッシュと一致するように自動調整*（mesh = regの場合はユーザーが指定する必要有）
iphtout = -20の場合は、RI線源形式(e-type = 28) で光子のみ（proj = photon）考慮する
*RI数やメッシュ数が多くなるとPHITSでの読込時間が長くなる
← xyz空間分布を持つ線源形状
DCHAINで計算した各RIの空間分布 (今回は1メッシュのため1つの値のみ）

--- SLIDE 34 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
$ Photon source from DCHAIN output
$ infl:{Fe_target_RIsrc_t2.pht}
$ You must "off" the [source] and [t-dchain] sections when you activate this command

[Source]
$ Beam settings to be used in [T-Dchain] tallies
…
[T-DCHAIN]
  mesh = xyz
…
exercise.inp
DCHAINより出力された2番目の出力時間(t2)に対する線源ファイルを“infl”コマンドでPHITS入力ファイルに組み込む
従来の[source]と[t-dchain]セクションを無効化(off)する*
exercise.inpを入力ファイルとしてPHITSを実行し、H10.epsを確認
照射直後のγ線線量を計算しよう
課題１
*[t-dchain]が有効のままでも動作はするが結果が上書きされるので注意
MENTIONED_INPUT_NAMES: exercise.inp
ANSWER_FILE: input/exercise-2.inp

--- SLIDE 35 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
$ Photon source from DCHAIN output
infl:{Fe_target_RIsrc_t2.pht}
…

[Source] off
$ Beam settings to be used …
…
[T-DCHAIN] off
  mesh = xyz
…
exercise.inp
解答１
H10.eps (page 3)
鉄箱外側のH*(10)は約0.1 mSv/h
[t-dchain]で１つの空間メッシュとしているため、γ線はターゲット内で均一に発生
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 36 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
$ Photon source from DCHAIN output
infl:{Fe_target_RIsrc_t2.pht}
$ You must "off" the [source] and [t-dchain] sections when you activate this command
…
exercise.inp
組み込む線源ファイルを3番目の出力時間(t3)に変更
PHITSを再実行し、H10.epsを確認
冷却時間３０分後のγ線線量を計算しよう
課題２
MENTIONED_INPUT_NAMES: exercise.inp
ANSWER_FILE: input/exercise-3.inp

--- SLIDE 37 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
$ Photon source from DCHAIN output
infl:{Fe_target_RIsrc_t3.pht}
…
exercise.inp
解答２
H10.eps (page 3)
鉄箱外側のH*(10)は照射直後と比べて約１桁小さくなった（～0.01 mSv/h）
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 38 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
$ Photon source …
infl:{Fe_target_RIsrc_t3.pht}

[Source] off
$ Beam settings …
…
[T-DCHAIN] off
  mesh = xyz
 x-type = 2
      nx = 1
    xmin = -c1
    xmax =  c1
  y-type = 2
      ny = 1
    ymin = -c1
    ymax =  c1
  z-type = 2
      nz = 1
    zmin = -c1
    zmax =  c1
exercise.inp
DCHAIN出力線源を組み込むinflコマンドを無効化
従来の[source]と[t-dchain]を有効化
[t-dchain]の空間メッシュ数（nx, ny, nz）を３に増やす（ターゲットを27分割する）
修正したexercise.inpでPHITSを実行

新しく生成されたFe_target.outでDCHAINを実行 (計算時間が長くなるので注意)
放射能の空間分布をFe_target_pxy.epsで確認*

DCHAIN出力線源を組み込むinflコマンドを再有効化
従来の[source]と[t-dchain]を無効化
修正したexercise.inpでPHITSを再実行
ターゲット内でのγ線発生空間分布を考慮しよう
課題３
*ipltmode = 1の場合のみ出力される
MENTIONED_INPUT_NAMES: exercise.inp
ANSWER_FILE: input/exercise-3.inp

--- SLIDE 39 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
$ Photon source …
infl:{Fe_target_RIsrc_t3.pht}

[Source] off
$ Beam settings …
…
[T-DCHAIN] off
  mesh = xyz
 x-type = 2
      nx = 3
    xmin = -c1
    xmax =  c1
  y-type = 2
      ny = 3
    ymin = -c1
    ymax =  c1
  z-type = 2
      nz = 3
    zmin = -c1
    zmax =  c1
exercise.inp
解答３
Fe_target_pxy.eps (page 1)
H10.eps (page 3)
放射能は表面中央に集中
（2回目のPHITS実行後）
γ線の空間線量は照射側（左側）で高くなる
→ターゲット内での放射能空間分布が不均一なため
MENTIONED_INPUT_NAMES: exercise.inp

--- SLIDE 40 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
htitle = [t-dchain]  in xyz mesh

! --- control parameters ---
     imode =       2
     jmode =       2

! --- calculation parameters ---
     idivs =      50
…
Fe_target.out
Fe_target.outに書かれたidivsを5に変更してからDCHAINを再実行し、Fe_target.epsで放射能の時間変化を確認
exercise.inpを用いてPHITSを再実行し、H10.epsを確認
DCHAINの計算時間を短縮しよう
課題４
idivsは１つのタイムステップをDCHAIN内部計算で分割する数。
小さくすると計算時間が短くなるが場合によっては精度が下がる.
１つのタイムステップ内で重要核種の放射能が劇的に変化しないならば、ある程度小さくしても問題ない場合が多い
ANSWER_FILE: (missing)

--- SLIDE 41 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
! --- calculation parameters ---
     idivs =      5
…
Fe_target.out
解答４
Fe_target.eps (page 1)
H10.eps (page 3)
idivs=50の場合と比べて結果はほとんど変わらないが、DCHAINの計算時間は約1/5になった

--- SLIDE 42 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
実習内容
PHITS-DCHAIN接続計算の概要
[t-dchain]とDCHAINの使い方
DCHAIN出力ファイルの解説
演習
まとめ
参考資料（計算原理と注意事項）

--- SLIDE 43 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
DCHAINは、誘導放射能、崩壊熱、γ線スペクトルとそれに伴う線量率の時間変化を任意の照射・冷却スケジュールに対して計算することができる
[t-dchain]を使うことにより、PHITSは自動でDCHAINの入力ファイルを生成することができる
DCHAINの結果を[source]形式で出力することにより、誘導放射能により放出されるγ線の挙動解析をPHITSで行うことができる
PHITSとDCHAINを組み合わせることにより、加速器や原子力施設の長期的な安全設計を簡単に実施できるようになる
まとめ

--- SLIDE 44 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
実習内容
PHITS-DCHAIN接続計算の概要
[t-dchain]とDCHAINの使い方
DCHAIN出力ファイルの解説
演習
まとめ
参考資料（計算原理と注意事項）

--- SLIDE 45 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
用語の解説
放射能：
 ・ 放射性物質が壊変して放射線を放出する性質
 ・ 放射能の強さ （単位：Bq ＝ 崩壊/秒）
     ※ベクレルは、ウランの塩類から放射線が出ていることを発見（1896）
放射性物質（放射性核種、放射性同位元素とも言われる）：
 ・ 放射能を持つ物質（核種、同位元素）
放射線：
 ・ エネルギーを持って媒質中を伝搬している粒子
  （PHITSで挙動解析が可能な陽子・中性子・光子など）

  ⇒ 放射線・放射性物質ともに規制の対象になる。

--- SLIDE 46 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
放射性壊変
放射性核種Aが核種Bに放射性壊変する場合、

 このとき、
 放射性核種Aを親核種、核種Bを娘核種と言う。
 これを、それぞれの核種について見てみると、
  放射性核種A：放射性核種Aの個数は、崩壊定数λ
          により時間とともに減少（放射能の減衰）
  核種B：核種Bの個数は、時間とともに増加（生成）
	   ※ ここでは、壊変の分岐比は100% とする。
放射性核種A → 核種B
λ
：崩壊定数

--- SLIDE 47 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
放射性壊変による放射能の減衰
放射性壊変による放射能（放射性核種A）の減衰
N = N 0 exp(-λt ) = N 0 (1/2)
0        2T1/2      4T1/2     6T1/2      8T1/2     10T1/2
t/T1/2
0       2T1/2     4T1/2     6T1/2     8T1/2    10T1/2
放射性壊変による放射能の減衰曲線（左：線形、右：片対数）
減衰曲線
半減期 T1/2
減衰曲線
崩壊定数 λ
放射性核種A
放射性核種A
※崩壊定数λ、半減期 T1/2

--- SLIDE 48 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
放射性壊変による核種Bの生成（純増）
放射性壊変による核種の生成
N = N 0 (1 - exp(-λt )) = N 0 (1 - (1/2)      )
0        2T1/2      4T1/2     6T1/2      8T1/2     10T1/2
t/T1/2
放射性壊変による核種の生成曲線（線形）
生成曲線
半減期 T1/2
※崩壊定数λ、半減期 T1/2
核種B
分岐比は100%

--- SLIDE 49 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
生成・崩壊方程式の一般解は、
生成曲線と飽和係数
N x(t ) = C x /λx (1 - exp(-λxt ))
0        2Tx          4Tx         6Tx        8Tx       10Tx
生成曲線
 （= 飽和曲線）
半減期 T x
放射性核種X
← C x/λx ： 生成量の上限値
      （最大想定：飽和放射能）
C xTx
飽和係数
※崩壊定数λx、半減期 Tx
197Au (n,γ)198Au のとき、
    C x = φσxN Au-197

  ここで、
   φ (cm-2 s-1)：中性子束
   σx (cm2)：反応断面積
中性子照射による生成曲線（線形）

--- SLIDE 50 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
放射能は、放射性核種の崩壊定数λ（または、半減期 T1/2）により、時間とともに指数関数的に増減する。
 ⇒ 計算結果出力時間の設定の際は注意してください。
  出力時間の間隔を粗くとって直線で結んでしまうと
  間違った解釈をしてしまう可能性があります。
指数関数的な放射能の時間進展
粗くとった結果
細かくとった結果

--- SLIDE 51 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
長期間稼働予定の施設の誘導放射能の評価には、長半減期核種を生成しやすいCoやEuなどの不純物を含めた評価が必須です
微量元素の取り扱い
微量のため、PHITSを再計算することなく様々な濃度に対して評価が可能です*
DCHAINで物質を変更するには、 元素数（itgnucls）を変更し元素を加えます
!1)HRGCMM 2)IREGS 3)ITGNCLS 4)FLUXS 5)HNFLUXS 6)VOLUMES
   DUMMY003        3    4  9.3610E+08   tdchain.dtrk  3.2000E+02
  Fe-54      4.9642E-03
  Fe-56      7.7928E-02
  Fe-57      1.7997E-03
  Fe-58      2.3951E-04
tdchain.out
!1)HRGCMM 2)IREGS 3)ITGNCLS 4)FLUXS 5)HNFLUXS 6)VOLUMES
   DUMMY003        3    5  9.3610E+08   tdchain.dtrk  3.2000E+02
  Fe-54      4.9642E-03
  Fe-56      7.7928E-02
  Fe-57      1.7997E-03
  Fe-58      2.3951E-04
  Co-59      1.0e-7
tdchain.out
*高エネルギー中性子による寄与が支配的な場合はPHITSの再計算が必要

--- SLIDE 52 ---
PPTX_FILE: phits-lec-dchain01-en.pptx
SLIDE_TEXT:
DCHAINの反応カテゴリー
DCHAINは反応を３つのカテゴリーに分類してそれぞれ計算
核壊変
DCHAINの核壊変データライブラリを用いて計算
20MeV以下の中性子による核反応
[t-track]で計算した20MeV以下の中性子フラックスとDCHAINの放射化断面積ライブラリを組み合わせて計算
それ以外の核反応
[t-yield]で計算
JMODEパラメータによりどの反応を考慮するか変更することができる。デフォルト（JMODE = 2）は全ての反応を考慮するモード
注意：自発核分裂はカテゴリー１（核壊変）、中性子入射による核分裂はカテゴリー2に分類され、DCHAINの核分裂収率データに従って各核分裂生成核種の収率が計算される
SPEAKER_NOTES:
The JMODE input parameter considers which of these 3 are used in a DCHAIN calculation

DCHAIN considers 3 categories of reaction mechanisms:
1) Decay (using DCHAIN’s decay library)
2) Neutron reactions under 20 MeV (using DCHAIN’s activation cross section library and the [t-track] neutron flux)
3) Everything else (using the [t-yield] nuclide yields)
*Note that fission is included in categories 1 (spontaneous fission) and 2 (neutron induced fission) and also utilizes additional fission yield libraries inside of DCHAIN.

--- SLIDE 53 ---
PPTX_FILE: phits-lec-dchain01-jp.pptx
SLIDE_TEXT:
DCHAINによる[source]出力オプション
iphtout in PHITS / phitsout in DCHAIN
下一桁を1にすると、従来形式（DCHAINのデータベースに基づくγ線エネルギースペクトル*）も出力される。例えば、iphtout = 11とした場合、proj = allで定義するRI線源と従来形式のγ線スペクトルが両方出力される。
iphtout/phitsoutを負値で定義した場合、各出力時間タイミングの線源情報が個別ファイル (*_t1.pht, *_t2.pht…)に出力されため、inflコマンドで直接PHITS入力ファイルに取り込むことが可能。（t1, t2などは出力時間タイミングの番号）
0 or 1: RI線源形式での[source]を出力しない
10 or 11: proj = allで定義するRI線源
20 or 21: proj = photonで定義するRI線源
30 or 31: proj = electronで定義するRI線源
40 or 41: proj = positronで定義するRI線源
50 or 51: proj = alphaで定義するRI線源
*エネルギー分解能はRI線源形式よりも粗い

--- SLIDE 54 ---
PPTX_FILE: phits-lec-dchain01-jp.pptx
SLIDE_TEXT:
mesh=xyzとregの使い分け
xyzメッシュ線源を使うメリット
誘導放射能の空間分布を考慮できる。また、その空間分布を可視化できる*
ユーザーが線源領域の範囲を自分で設定する必要がない（*.phtファイルを編集する必要がない）
メッシュ数が増えた場合に計算時間が長くなる
直方体で表現できない複雑な線源形状を再現できない
xyzメッシュ線源を使うデメリット
SPEAKER_NOTES:
Note that decay photons are much faster to simulate than 250 MeV protons, so we are increasing the number of histories for better statistics for the photon dose calculation

--- SLIDE 55 ---
PPTX_FILE: phits-lec-dchain01-jp.pptx
SLIDE_TEXT:
出力ファイルに関する追加情報

--- SLIDE 56 ---
PPTX_FILE: phits-lec-dchain01-jp.pptx
SLIDE_TEXT:
ACMIN – *.actファイルに出力する放射能の下限値。デフォルトは全放射能×10-10
ISTABL – 安定核を出力するオプション。デフォルトは出力しない
IDOSECF, IDOSUNIT – 線量率を計算するための換算係数に関するオプション。デフォルトはICRP Pub. 116に基づく前方（AP）照射に対する実効線量をuSv.m2/hr単位で出力
INXSLIB, IDCYLIB, INFYLIB, ISFYLIB – DCHAINで利用する放射化断面積、核壊変データ、核分裂収率などに関するライブラリ選択オプション
標準出力（*.act）関連パラメータ

--- SLIDE 57 ---
PPTX_FILE: phits-lec-dchain01-jp.pptx
SLIDE_TEXT:
IANGBPWR – ビーム出力の変化をピンク色のバーで出力するオプション
ANGELOUT_REGION † – 出力する領域を指定
ANGELOUT_NUCLIDES † – 核種ごとの誘導放射能をグラフ表示する際、その核種を指定する（全領域の合計値のみ出力可能）
画像出力（*.eps）関連パラメータ
†[t-dchain]から指定する場合は下記のように定義する
  aoreg = 1  5   7
  iaonucl = 3
  aonucl = Mn-56  Fe-53  Fe-53m
[t-dchain]ではパラメータ名がANGELOUT_REGIONはaoreg、ANGELOUT_NUCLIDESはiaonuclと変化することに注意
SPEAKER_NOTES:
This file can be quite long, and these parameters control what gets printed, greatly impacting the length of the file depending on your desired level of detail.

--- SLIDE 58 ---
PPTX_FILE: phits-lec-dchain01-jp.pptx
SLIDE_TEXT:
CHRLVTH – *.dcsファイルに出力する放射能の下限値（*.actのACMINに相当）
IWRCHDT – 各壊変連鎖の各反応ごとの寄与を出力するオプション。デフォルトは出力しない
*.dcs関連パラメータ
SPEAKER_NOTES:
This file can be quite long, and these parameters control what gets printed, greatly impacting the length of the file depending on your desired level of detail.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/exercise-1.inp
FILE: input/exercise-final.inp

[BONUS_TEXT_FILES]
NOTE: None
