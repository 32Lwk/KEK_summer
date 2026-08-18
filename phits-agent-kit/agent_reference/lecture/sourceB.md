# Lecture: advanced/sourceB

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/sourceB
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: sourceB
LECTURE_PATH_INDEX: lecture/advanced/sourceB
PPTX_FILES: phits-lec-sourceB-en.pptx, phits-lec-sourceB-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: sourceB
SECTION_KEYWORDS: 1, 2, 3, t-cross, t-deposit, t-dpa, t-interact, t-point, t-product, t-time, t-track

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/sourceB
LECTURE_PATH_INDEX: lecture/advanced/sourceB
PPTX_FILES: phits-lec-sourceB-en.pptx, phits-lec-sourceB-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 1
SLIDE_COUNT: 64
EXERCISE_SLIDE_COUNT: 26
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- sourceB.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Setting of various source
- SLIDE 02: Goal of this lecture
- SLIDE 03: sourceB.inp
- SLIDE 04: Table of Contents
- SLIDE 05: Source with dump data
- SLIDE 06: In the [t-track], [t-cross], [t-point], [t-deposit], [t-product], [t-dpa], [t-time] or [t-interact] tally, set dump para
- SLIDE 07: Dump data
- SLIDE 08: Two modes to use dump data
- SLIDE 09: EXERCISE 1 | To record information on particles passing through the water as dump data, set outer void behind the water (positive sid
  ANSWER_FILE: input/sourceB-2.inp
- SLIDE 10: Dump data
- SLIDE 11: EXERCISE 2 | Record photons from the 60Co source which passed through the water as dump data.
  ANSWER_FILE: input/sourceB-3.inp
- SLIDE 12: SourceB.inp
- SLIDE 13: EXERCISE 3 | Make large dump data can be used as source.
  ANSWER_FILE: input/sourceB-4.inp
- SLIDE 14: The result becomes continuum spectrum. This can be used as source.
- SLIDE 15: Table of Contents
- SLIDE 16: EXERCISE 4 | Perform the transport simulation using dump data.
  ANSWER_FILE: input/sourceB-5.inp
- SLIDE 17: Dump data
- SLIDE 18: EXERCISE 5 | Put a lead block behind the water.
  ANSWER_FILE: input/sourceB-6.inp
- SLIDE 19: Dump data
- SLIDE 20: Dump data
- SLIDE 21: Table of Contents
- SLIDE 22: Summary
- SLIDE 23: Parallel computing
- SLIDE 24: MCPL converters for PHITS
- SLIDE 25: Bonus slides
- SLIDE 26: EXERCISE 6 | Overwriting dumped source
  ANSWER_FILE: input/sourceB-7.inp
- SLIDE 27: Dump data
- SLIDE 28: Dump data
- SLIDE 29: EXERCISE 7 | Then how can we apply filter to source particles?
  ANSWER_FILE: input/sourceB-8.inp
- SLIDE 30: Dump data
- SLIDE 31: EXERCISE 8 | Then how can we apply time filter to source particles?
  ANSWER_FILE: input/sourceB-end.inp
- SLIDE 32: Dump data
- SLIDE 01: Title
- SLIDE 02: 本実習の目標
- SLIDE 03: SourceB.inpの確認
- SLIDE 04: Table of Contents
- SLIDE 05: Dump dataを用いた線源
- SLIDE 06: Dump dataの使用方法
- SLIDE 07: Dump定義文
- SLIDE 08: 二種類のdumpデータ使用モード
- SLIDE 09: EXERCISE 1 | 課題1
  ANSWER_FILE: input/sourceB-2.inp
- SLIDE 10: EXERCISE 1 | 課題1の答え合わせ
  ANSWER_FILE: input/sourceB-2.inp
- SLIDE 11: EXERCISE 2 | 課題2
  ANSWER_FILE: input/sourceB-3.inp
- SLIDE 12: EXERCISE 2 | 課題2の答え合わせ
  ANSWER_FILE: input/sourceB-3.inp
- SLIDE 13: EXERCISE 3 | 課題3
  ANSWER_FILE: input/sourceB-4.inp
- SLIDE 14: EXERCISE 3 | 課題3の答え合わせ
  ANSWER_FILE: input/sourceB-4.inp
- SLIDE 15: Table of Contents
- SLIDE 16: EXERCISE 4 | 課題4
  ANSWER_FILE: input/sourceB-5.inp
- SLIDE 17: EXERCISE 4 | 課題4の答え合わせ
  ANSWER_FILE: input/sourceB-5.inp
- SLIDE 18: EXERCISE 5 | 課題5
  ANSWER_FILE: input/sourceB-6.inp
- SLIDE 19: EXERCISE 5 | 課題5の答え合わせ1
  ANSWER_FILE: input/sourceB-6.inp
- SLIDE 20: EXERCISE 5 | 課題5の答え合わせ2
  ANSWER_FILE: input/sourceB-6.inp
- SLIDE 21: Table of Contents
- SLIDE 22: まとめ
- SLIDE 23: 並列計算時の注意点
- SLIDE 24: MCPL converters for PHITS
- SLIDE 25: 追加資料
- SLIDE 26: EXERCISE 6 | ダンプ線源を上書きしよう
  ANSWER_FILE: input/sourceB-7.inp
- SLIDE 27: EXERCISE 6 | Dump data
  ANSWER_FILE: input/sourceB-7.inp
- SLIDE 28: EXERCISE 6 | Dump data
  ANSWER_FILE: input/sourceB-7.inp
- SLIDE 29: EXERCISE 7 | ではフィルタを適用するにはどうしたら？
  ANSWER_FILE: input/sourceB-8.inp
- SLIDE 30: EXERCISE 7 | Dump data
  ANSWER_FILE: input/sourceB-8.inp
- SLIDE 31: EXERCISE 8 | 時間のフィルタを課すにはどうしたらよいか
  ANSWER_FILE: input/sourceB-end.inp
- SLIDE 32: EXERCISE 8 | Dump data
  ANSWER_FILE: input/sourceB-end.inp

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: sourceB.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Setting of various source
Part II
Title
Mar. 2021 revised
phits/lecture/advanced/sourceB
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Goal of this lecture
Purpose
Transport simulation using dump data as sources
Simulation of radiation shielding using dump data, which were information on particles from a 60Co source and were recorded at z=20cm.

--- SLIDE 03 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
sourceB.inp
Check Input File
Basic setup
Projectile:
Geometry:
Tally:
Geometry
1.173 and 1.333MeV photons (from 60Co)
Water cylinder (10cm radius and 20cm thickness)
[t-track] fluence  distribution
[t-cross] photon energy spectrum coming into water
track_xz.eps
Water
60Co
cross_photon.eps
MENTIONED_INPUT_NAMES: sourceB.inp

--- SLIDE 04 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Table of Contents
Table of contents
Source with dump data
Making dump data file
Transport simulation using dump data
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 05 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Source with dump data
PHITS can perform two-step calculation using information on particles coming into specified regions.
Dump data
For example,
to study shielding effect changing thickness of lead block.
60Co
Lead
Water
In the 1st step, only one time calculation is performed, and
information on photons coming into the lead is recorded.
Sources in the 2nd step.
You can perform calculations of the 2nd step many times changing the thickness of the lead block.

--- SLIDE 06 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
In the [t-track], [t-cross], [t-point], [t-deposit], [t-product], [t-dpa], [t-time] or [t-interact] tally, set dump parameters.
Execute PHITS calculation of the 1st step.
A data file named as ******_dmp.out is made (****** is specified by “file=“). This file contains information on the tallied particles.
In the [source] section, set s-type=17 with dump parameters.
The old [source] section and old tally, which were used in the 1st step, should be invalid by “off”.
Execute PHITS calculation of the 2nd step.
Dump data
[ T - C r o s s ]
・ ・ ・ ・ ・ ・
 file = ******.out
 dump = -12
1 2 3 4 5 6 7 8 9 10 18 19
dump parameters (1st step)
[source] section with dump parameters (2nd step)
[ S o u r c e ]
s-type =   17
     file = ******_dmp.out
    dump = 0
The number of the data item.
(If positive, the data file is made as binary. If negative, the file is made as ASCII data.)
How to use
0 means to read all
(Explicit specification is also accepted to read partially)

--- SLIDE 07 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
dump = -12
   1 2 3 4 5 6 7 8 9 10 18 19
Using dump parameters, you can set the data item and their order to output in the dump data file.
You can change this order
ID number of dump data
Read manual 6.7.21 for other data

--- SLIDE 08 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Two modes to use dump data
(1st step) set the dump region as void in order to avoid a double-count of particles passing through the region.
(1st step) tally the energy spectrum of the dump data and check whether the data are statistically sufficient to be used as source.
(2nd step) The result of the 1st step is not included in the 2nd step. If you want total, you have to use “sum tally” to add 1st & 2nd step results.
(2nd step) When the dump ID 18 and 19 are included, “maxcas” and “maxbch” of the 1st step. (“maxcas” and “maxbch” in the 2nd step are ignored.)
Dump data
idmpmode=1: Consider correlations between particles in 1st step (New*)
idmpmode=0: Assume independence of initial particle in 2nd step (Old)
Recommended  To obtain correct statistical calculation,  nocas & nobch info are required (default if they exist).
Automatically selected if nocas or nobch does not exist
Should be use only when many particles are produced and particle correlation can be ignored in 1st step (e.g. x-ray generation by bombarding electrons on target)
Other cautions to use dump data

--- SLIDE 09 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
To record information on particles passing through the water as dump data, set outer void behind the water (positive side of z-axis).
Dump region
(defined as outer void)
Set a cylindrical region (cell number is 102) with 10cm radius and 5cm thickness as outer void behind the water (positive side of z-axis).
In the [cell] section, outer void is defined by setting its material number = -1 (density is not needed).
Check the geometry by setting icntl=8.
Dump data
Exercise 1
ANSWER_FILE: input/sourceB-2.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
SourceB.inp
[ Parameters ]
  icntl = 8
・・・ ・・・ ・・・ ・・・

[ S u r f a c e ]
  10  so     500.
  11  cz      10.
  12  pz       0.
  13  pz      20.
  14  pz      25.

[ C e l l ]
 100    -1      10
 101     1 -1.  -11  12  -13
 102    -1      -11  13  -14
 110     0      -10  #101 #102
track_xz.eps
The white region denotes the outer void.
Answer 1
To record information on particles passing through the water as dump data, set outer void behind the water (positive side of z-axis).
MENTIONED_INPUT_NAMES: SourceB.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Record photons from the 60Co source which passed through the water as dump data.
Dump region
(cell 102)
Add dump parameters (from 1 to 10, 18, and 19) to [t-cross].
In [t-cross], change cell ID numbers so that this tally counts the number of photons moving from cell 101 to 102.
Execute PHITS with icntl=0 in [parameters].
Dump data
Water
(cell 101)
Record photons moving from 101 to 102.
Exercise 2
ANSWER_FILE: input/sourceB-3.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
SourceB.inp
The data are not enough to be used as sources, because this result should be continuum spectrum.
[ T - C r o s s ]
・ ・ ・ ・ ・ ・
 1     101     102     314.15
・ ・ ・ ・ ・ ・
ne =    200
unit =    1
axis =  eng
file = cross_photon.out
output = flux
part =  photon
 epsout =    1
dump =   -12
1  2  3  4  5  6  7  8  9 10 18 19
cross_photon.eps
Dump data
Answer 2
Record information on photons from the 60Co source, passing through the water as dump data.
[ Parameters ]
  icntl = 0
・・・ ・・・ ・・・ ・・・
MENTIONED_INPUT_NAMES: SourceB.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Make large dump data can be used as source.
Increase “maxcas” to obtain large data.
cross_photon.eps
Result with maxcas=1000
not enough
Dump data
Exercise 3
Result with maxcas=10000
ANSWER_FILE: input/sourceB-4.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
The result becomes continuum spectrum. This can be used as source.
(Note that the relative errors are 10 -20%)
Dump data
Make large dump data can be used as source.
Answer 3
Result with maxcas=100000
cross_photon.eps

--- SLIDE 15 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Table of Contents
Table of contents
Source with dump data
Making dump data file
Transport simulation using dump data
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 16 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Perform the transport simulation using dump data.
Create the new [source] section with s-type=17. (Set the old [source] section to be invalid by “off”.)
Set cell 102 to be void (its material number is 0)
Set the [t-cross] section with dump parameters to be invalid by “off”.
[ S o u r c e ]
s-type =   17
     file = cross_photon_dmp.out
    dump = 0
Both two files,
cross_photon_dmp.out and
cross_photon.out, are needed.*
When dump ≠ 0, dump ID must be explicitly specified in the next line
*When the dump ID 18 and 19 are included in the dump data, “maxcas” and “maxbch” of the 1st step written in “cross_photon.out” are used. (“maxcas” and “maxbch” in the input file of the 2nd step are ignored.)
Exercise 4
[source] section with dump parameters (2nd step)
ANSWER_FILE: input/sourceB-5.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
[ S o u r c e ] off
   totfact = 2.0
・ ・ ・ ・ ・ ・
・ ・ ・ ・ ・ ・
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   0
SourceB.inp
[ C e l l ]
 100    -1      10
 101     1 -1.  -11  12  -13
 102     0      -11  13  -14
 110     0      -10  #101 #102
[ T - C r o s s ] off
・ ・ ・ ・ ・ ・
dump =   -12
1  2  3  4  5  6  7  8  9 10 18 19
track_xz.eps
Particles included in dump data are generated behind the water.
Perform the transport simulation using dump data.
Answer 4
MENTIONED_INPUT_NAMES: SourceB.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Put a lead block behind the water.
Dump data
cell 102 (lead)
cell 101 (water)
cell 103 (void)
1cm
Exercise 5
Restore [t-cross]. Change output file name to 	     Add cell IDs to tally photons from cell 102 to 103 (its area is p102 cm2). Make sure to turn off dump
Change the material of cell 102 to lead (Element symbol : Pb) and the density of 11.34 g/cm3. (Change parameters in [material] and [cell].)
In order to study an effect of the shielding, define a new cell 103 (a cylindrical region with 10cm radius and 1cm thickness).
Warning! If file is overwritten, go back to exercise 3
cross_photon2.out.
ANSWER_FILE: input/sourceB-6.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
SourceB.inp
track_xz.eps
The particle fluence is reduced in the lead region.
Put a lead block behind the water.
Answer 5
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
  13  pz      20.
  14  pz      25.
  15  pz      26.

[ C e l l ]
 100    -1      10
 101     1 -1.  -11  12  -13
 102     2 -11.34  -11  13  -14
 103     0      -11  14  -15
 110     0      -10  #101 #102 #103
[ M a t e r i a l ]
mat[1]    H 2  O 1
mat[2]    Pb  1.0
[ T - C r o s s ]
・ ・ ・ ・ ・ ・
reg =    1
non     r-from  r-to      area
    1     102     103      314.15
・ ・ ・ ・ ・ ・
 file = cross_photon2.out
・ ・ ・ ・ ・ ・
$    dump =   -12
$    1 2 3 4 5 6 7 8 9 10 18 19
MENTIONED_INPUT_NAMES: SourceB.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
The lead block reduces the strength of 1.173 and 1.333MeV photons to 1/10.
(Investigate the thickness of the lead so that the strength becomes 1/100.)
cross_photon2.eps
cross_photon2.eps
Energy spectrum of photons entering the lead region
Put a lead block behind the water.
Answer 5

--- SLIDE 21 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Table of Contents
Table of contents
Source with dump data
Making dump data file
Transport simulation using dump data
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 22 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Summary
We can perform two step simulation using dump data.
A correct statistical process using “idmpmode=1” can be applied by recording dump ID 18 and 19. (From PHITS2.80)
Notes about idmpmode=1
“totfact” is compulsory reflected the setting of “totfact” in the 1st step (at the time of making dump data) in the calculation of the 2nd step using dump data.
The option “idmpmode=1” is incompatible with multi-source. (Use sumtally option)
In the 2nd step, “istdev<0” (restart calculation) or “dumpall=1” in [parameters] cannot be used.
maxcas and maxbch in the input file of the 2nd step are ignored.
If you use the old statistical process of PHITS, set “idmpmode=0”.
With idmpmode=1, the option “dmpmulti” controls the number of re-use of the dump file. (dmpmulti=2.0 is 2 times)
Acknowledgement
The option “idmpmode=1” and re-used calculation using the option “dmpmulti” were introduced by referring to the presentation “Estimation of uncertainty in multi-step Monte Carlo calculation”(N50) by Prof. Y. Namito et al. at the 2015 annual meeting of AESJ (Hitachi, Japan).
Summary
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 23 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Parallel computing
OpenMP (shared-memory parallel computing mode) can be used both processes (the 1st step and the 2nd step).
MPI (distributed-memory parallel computing) can be used, if the number of processor elements in the 1st and 2nd steps is the same.
For parallel computing

--- SLIDE 24 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
MCPL converters for PHITS
MCPL converters for PHITS
Dump data converters developed by Dr. Douglas Di Julio (European Spallation Source)
Dump data (particle information file) in the PHITS, MCNP, or Geant4 format can be converted to those in the other code format
This converter can be used as command line in terminal on Linux, Mac, Cygwin(Windows) systems
https://mctools.github.io/mcpl/hooks_phits/
Dump data in PHITS format
Dump data in MCNP or Geant4 format
Conversion among several codes

--- SLIDE 25 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Bonus slides
How to overwrite and filter dumped sources

--- SLIDE 26 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Overwriting dumped source
Dump data
Exercise 6
Particle data of dumped sources are overwritten by the specification given by users in [source] section
[ S o u r c e ] off
   totfact = 2.0
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
   1 2 3 4 5 6 7 8 9 10 18 19
  x0 = -5
  x1 = 5
SourceB.inp
track_xz.eps
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-7.inp

--- SLIDE 27 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
Answer 6
Overwriting dumped source
[ S o u r c e ] off
   totfact = 2.0
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
  1 2 3 4 5 6 7 8 9 10 18 19
  x0 = -5
  x1 = 5
SourceB.inp
track_xz.eps
Source x coordinate was
uniformly sampled from -5 to +5.
MENTIONED_INPUT_NAMES: SourceB.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
Answer 6
Attention : This is not filter but overwrite!
[ S o u r c e ] off
   totfact = 2.0
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
  1 2 3 4 5 6 7 8 9 10 18 19
  x0 = 20
  x1 = 20
 dir = -0.8
SourceB.inp
track_xz.eps
Sources were not at x = 20
But their coordinates were overwritten

Angle, time, weight, etc. are overwritable.
MENTIONED_INPUT_NAMES: SourceB.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Then how can we apply filter to source particles?
Dump data
Exercise 7
Let’s use outer-void (= ideal black body)
Define a cylinder (Thickness : 0.001 cm, radius : 8cm) and assign outer void to this region, where you cut-off sources
[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
  1 2 3 4 5 6 7 8 9 10 18 19
$  x0 = -5
$  x1 = 5
SourceB.inp
[ S u r f a c e ]
…
  20  cz      8.
  21  pz      20.001
[ S u r f a c e ]
…
 102   2 -11.34  -11  13  -14 #104
 104    -1      -20  13  -21
 110   0        -10 #101 #102 #103 #104
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-8.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
Answer 7
Filter out source particles inside 8-cm circle
SourceB.inp
track_xz.eps
[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
  1 2 3 4 5 6 7 8 9 10 18 19
$  x0 = -5
$  x1 = 5
[ S u r f a c e ]
…
  20  cz      8.
  21  pz      20.001
[ S u r f a c e ]
…
 102   2 -11.34  -11  13  -14 #104
 104    -1      -20  13  -21
 110   0        -10 #101 #102 #103 #104
MENTIONED_INPUT_NAMES: SourceB.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Then how can we apply time filter to source particles?
Dump data
Exercise 8
Let’s combine outer-void (= ideal black body) and [mat time change]
Fill Cell 102 with void for simplicity
SourceB.inp
[mat time change ]
  mat time change
    3    1.05     -1
[ C e l l ]
…
 102     0      -11  13  -14 #104
 104     3   1e-10   -20  14  -21
[M a t e r i a l ]
…
mat[3]    H  1.0  $ dummy
[ T - C r o s s ]
…
   ne =    1
$       ne =  200
   t-type =    2
     tmin =   0.0
     tmax =  3.0
         nt =  100
$     axis =  eng
     axis =  t
cross_photon2.eps  without [mat time change]
Abundant
late photons
Replace material 3 (dummy vacuum) with -1 (black body) at 1.05 ns
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-end.inp

--- SLIDE 32 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump data
Answer 8
Filter out source particles after 1.1 ns
cross_photon2.eps  with [mat time change]
SourceB.inp
[mat time change ]
  mat time change
    3    1.05     -1
[ C e l l ]
…
 102     0      -11  13  -14 #104
 104     3   1e-10   -20  14  -21
[M a t e r i a l ]
…
mat[3]    H  1.0  $ dummy
[ T - C r o s s ]
…
   ne =    1
$       ne =  200
   t-type =    2
     tmin =   0.0
     tmax =  3.0
         nt =  100
$     axis =  eng
     axis =  t
Let’s combine outer-void (= ideal black body) and [mat time change]
Fill Cell 102 with void for simplicity
Late photons
were cut-off
Cell 104 works as a black hole to cut-off source particles
MENTIONED_INPUT_NAMES: SourceB.inp

--- SLIDE 01 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Title
1
多種多様な線源の設定方法B
2021年3月改訂
phits/lecture/advanced/sourceB
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
本実習の目標
Purpose
Dump dataを線源とした粒子輸送シミュレーションを実行できるようになる。
60Co線源より放出された光子をz=20cmの位置でdump dataとして蓄積し、それらを線源として鉛の遮へい体に照射したシミュレーション

--- SLIDE 03 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
SourceB.inpの確認
Check Input File
基本計算条件
入射粒子：
体系：
タリー：
計算体系
e-type=28の60Co線源（1.173と1.333MeVの光子）
円柱状の水（半径10cm, 厚さ20cm）と真空のみ
[t-track]によるフルエンス空間分布
[t-cross]による水領域へ入射する光子のエネルギー分布
Water
track_xz.eps
cross_photon.eps
60Co線源

--- SLIDE 04 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Table of Contents
実習内容
Dump dataを用いた線源
Dump dataの作成
Dump dataを利用した輸送計算
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 05 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump dataを用いた線源
Dump data
指定した領域に入射した放射線の情報を蓄え、それを線源とした2段階計算をすることができる
60Co線源
水の部分を通過した位置に遮へい体を置き、その厚さを変えながら遮へい効果を調べたい
鉛
水
1段階目の計算では1度だけPHITSを実行し、
鉛に入射する光子の情報を記録する
2段階目の計算の線源
鉛の厚さを変えて、
2段階目の計算を何度も行うことが可能

--- SLIDE 06 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump dataの使用方法
[t-track], [t-cross], [t-point], [t-deposit], [t-product], [t-dpa], [t-time], [t-interact]タリーにおいて、dumpパラメーターを加える
PHITSを実行し、1段階目の計算を行う
タリーで指定したファイル名に_dmpが付いたファイルが作成される。これに線源データが書き出されるので、そのデータを線源とする[source]セクションを作成する（s-type=17を使う）
1段階目で使った古い[source]セクションとdumpパラメーターを加えたタリーのセクションはoffで無効にする
PHITSを実行し、2段階目の計算を行う
Dump data
[ T - C r o s s ]
・ ・ ・ ・ ・ ・
 file = ******.out
 dump = -12
1 2 3 4 5 6 7 8 9 10 18 19
タリー中のdumpパラメーターの入力形式（1段階目）
dumpデータを用いた[source]セクションの入力形式（2段階目）
[ S o u r c e ]
s-type =   17
     file = ******_dmp.out
    dump = 0
データの個数を指定
（正ならバイナリで、負ならアスキー形式で出力）
0にすると、自動的に全部を読む
(一部を読む場合は、明示指定も可能)

--- SLIDE 07 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Dump定義文
Dump data
dump = -12
  1 2 3 4 5 6 7 8 9 10 18 19
Dump定義文によって、dump dataとして出力するデータの種類と順番を指定します
順番を変えることもできる
他のデータは
マニュアル
6.7.21参照

--- SLIDE 08 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
二種類のdumpデータ使用モード
（1段階目）指定した領域を粒子が複数回通過することによるダブルカウントを避けるために、dump dataを蓄える領域は外部ボイドとする
（1段階目）エネルギー分布等を同時にタリーし、dump dataとして蓄えた結果が線源として十分な量であるかを確認する
（2段階目）Dump dataを線源とする計算には、1段階目の結果は含まれないことに注意（合計が必要な場合はsum tallyを使って足し併せる）
（2段階目）イベント番号とバッチ番号がdumpデータに含まれる場合、１段階目のmaxcasとmaxbchを読み込む（2段階目のmaxcasとmaxbchは無視される）
Dump data
idmpmode=1：１段階目の粒子間の相関を考慮する（新手法*）
                     正しい統計誤差計算のために、nocasとnobchの
               ダンプ情報が必要（ある場合はデフォルト）
idmpmode=0：１段階目の粒子間の相関を考慮しない（従来の手法）
          nocasとnobchが無い場合は自動的に選択
こちらを選ぶのが無難
１段階目が大量に粒子が発生する等で粒子相関が無視できる場合に使用可能
（例：電子線を標的に当ててX線を生成）
その他のdumpデータ使用の注意点

--- SLIDE 09 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1
水の部分を通過した粒子の情報をdump dataとして蓄えるために、水の後ろ部分（z軸の正の側）を外部ボイドとして設定しましょう
Dump領域
（外部ボイドとして定義）
水の後ろ側（z軸の正の側）に半径10cm, 厚さ5cmの円柱状の領域を外部ボイドとして定義する（セル番号は102とする）
[cell]セクションにおいて外部ボイドとして設定する場合は、物質番号の箇所を-1とする（密度の項目は必要ない）
icntl=8として体系を確認する
Dump data
ANSWER_FILE: input/sourceB-2.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1の答え合わせ
水の部分を通過した粒子の情報をdump dataとして蓄えるために、水の後ろ部分（z軸の正の側）を外部ボイドとして設定しましょう
Dump data
SourceB.inp
[ Parameters ]
  icntl = 8
・・・ ・・・ ・・・ ・・・

[ S u r f a c e ]
  10  so     500.
  11  cz      10.
  12  pz       0.
  13  pz      20.
  14  pz      25.

[ C e l l ]
 100    -1      10
 101     1 -1.  -11  12  -13
 102    -1      -11  13  -14
 110     0      -10  #101 #102
track_xz.eps
外部ボイドの領域は白で表示される
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-2.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2
60Coを起源とするガンマ線が水の部分を通過した場合の状態を、dump dataとして蓄えてみましょう
Dump領域
（セル番号102）
[t-cross]にdumpパラメーターを加える（蓄積するデータは番号1から10までの10種類とイベント番号[番号18]とバッチ番号[番号19]の合計12種類）
[t-cross]において、セル番号101から102に移動する光子をタリーするように変更する。
icntl=0としてPHITSを実行
Dump data
水の領域
（セル番号101）
101から102に移動する光子をdumpする
ANSWER_FILE: input/sourceB-3.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2の答え合わせ
60Coを起源とするガンマ線が水の部分を通過した場合の状態を、dump dataとして蓄えてみましょう
SourceB.inp
連続スペクトルとなるべき部分がまばらで、線源として十分ではない
[ T - C r o s s ]
・ ・ ・ ・ ・ ・
 1     101     102     314.15
・ ・ ・ ・ ・ ・
ne =    200
unit =    1
axis =  eng
file = cross_photon.out
output = flux
part =  photon
 epsout =    1
dump =   -12
1  2  3  4  5  6  7  8  9 10 18 19
cross_photon.eps
Dump data
[ Parameters ]
  icntl = 0
・・・ ・・・ ・・・ ・・・
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-3.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題3
線源として十分な量のdump dataを求めましょう
maxcasを増やしてdump data量を大きくする
cross_photon.eps
maxcas=1000の結果
maxcas=10000の結果
まだ隙間がある
Dump data
ANSWER_FILE: input/sourceB-4.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題3の答え合わせ
線源として十分な量のdump dataを求めましょう
cross_photon.eps
maxcas=100000の結果
隙間もなくなっており、線源として使用可能
（ただし、相対誤差は10～20%）
Dump data
ANSWER_FILE: input/sourceB-4.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Table of Contents
実習内容
Dump dataを用いた線源
Dump dataの作成
Dump dataを利用した輸送計算
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 16 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題4
Dump dataを線源とした輸送計算を実行させましょう
s-type=17を用いる新しい[source]セクションを作成する（60Coを線源とする方はoffにする）
セル番号102の領域をvoidにする（物質番号の箇所は0）
Dumpパラメーターを含んだ[t-cross]はoffにする
dumpデータを用いた[source]セクションの入力形式
[ S o u r c e ]
s-type =   17
     file = cross_photon_dmp.out
    dump = 0
cross_photon_dmp.outと
cross_photon.outが必要*
dump ≠ 0の場合、dumpデータIDを次の行に直接指定する必要がある
*イベント番号とバッチ番号がdumpデータに含まれる場合、”_dmp”が付いてない方のファイルから、自動で１段階目のmaxcasとmaxbchを読み込む（2段階目のmaxcasとmaxbchは無視される）
ANSWER_FILE: input/sourceB-5.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題4の答え合わせ
Dump dataを線源とした輸送計算を実行させましょう
Dump data
[ S o u r c e ] off
   totfact = 2.0
・ ・ ・ ・ ・ ・
・ ・ ・ ・ ・ ・
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   0
SourceB.inp
[ C e l l ]
 100    -1      10
 101     1 -1.  -11  12  -13
 102     0      -11  13  -14
 110     0      -10  #101 #102
[ T - C r o s s ] off
・ ・ ・ ・ ・ ・
dump =   -12
1  2  3  4  5  6  7  8  9 10 18 19
track_xz.eps
水の後ろ側からdump dataにある粒子が放出されている
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-5.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5
水の後ろ側に鉛の遮へい体を置きましょう
Dump data
セル番号102
（鉛）
セル番号101
（水）
セル番号103
（真空）
1cm
ANSWER_FILE: input/sourceB-6.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5の答え合わせ1
Dump data
SourceB.inp
[ S u r f a c e ]
・ ・ ・ ・ ・ ・
  13  pz      20.
  14  pz      25.
  15  pz      26.

[ C e l l ]
 100    -1      10
 101     1 -1.  -11  12  -13
 102     2 -11.34  -11  13  -14
 103     0      -11  14  -15
 110     0      -10  #101 #102 #103
[ M a t e r i a l ]
mat[1]    H 2  O 1
mat[2]    Pb  1.0
[ T - C r o s s ]
・ ・ ・ ・ ・ ・
reg =    1
non     r-from  r-to      area
    1     102     103      314.15
・ ・ ・ ・ ・ ・
 file = cross_photon2.out
・ ・ ・ ・ ・ ・
$    dump =   -12
$    1 2 3 4 5 6 7 8 9 10 18 19
track_xz.eps
鉛の領域で粒子フルエンスが減少
水の後ろ側に鉛の遮へい体を置きましょう
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-6.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5の答え合わせ2
Dump data
鉛の前後（左右の結果）で1.173MeVと1.333MeVのスペクトルの強度がおよそ1/10になっている
（1/100になる鉛の厚さはどの位か調べてみましょう）
水の後ろ側に鉛の遮へい体を置きましょう
cross_photon2.eps
cross_photon.eps
鉛領域に入射する
光子のスペクトル
ANSWER_FILE: input/sourceB-6.inp

--- SLIDE 21 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
Table of Contents
実習内容
Dump dataを用いた線源
Dump dataの作成
Dump dataを利用した輸送計算
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 22 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
まとめ
Summary
Dump機能を用いることで、dump dataとして蓄えた2次粒子を線源とするシミュレーションが効率よく行えるようになった
粒子情報と共にイベント番号とバッチ番号を同時にdumpしておくことで、１段階目も含めた統計誤差計算idmpmode=1が行える
idmpmode=1の注意点
dumpデータを作るとき（1段階目） のtotfactが引き継がれるため， dumpデータをソースに使用する計算（2段階目）で設定したtotfactは無視される
   ⇒ 1段階目で適切にtotfactを設定する
マルチソースと共に使用することはできない（代わりにSumtallyを使用する）
（2段階目の計算時）[Parameters]セクションで指定する再開始計算（istdev<0）や全ての情報をダンプさせるオプション（dumpall=1）は使用不可
（2段階目の計算時）dumpデータから読み取るので、インプットのmaxcasとmaxbchは無視される
従来の統計処理を行いたい場合はidmpmode=0を明示的に指定する
idmpmode=1ではdmpmultiの値を設定することで、dumpデータの使い回しが行える（dmpmulti=2.0⇒2回）
Acknowledgement
idmpmode=1およびdmpmultiによる使い回し計算は、日本原子力学会「2015年春の年会」での波戸氏(KEK)らの発表“モンテカルロつなぎ計算における不確かさ評価”（演題番号N50）を参考に改良を行ったものです。
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 23 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
並列計算時の注意点
Parallel computing
OpenMPは、1段階目の計算および2段階目の両方で使用できます。
MPIは、1段階目と2段階目の並列数を変えずに使用してください。

--- SLIDE 24 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
MCPL converters for PHITS
MCPL converters for PHITS
Douglas Di Julio氏(European Spallation Source)により開発されたフリーソフト
Dump data（粒子情報ファイル）をPHITSとMCNPやGeant4等の別のコードとの間で相互に変換できる
Linux, Mac, Cygwin(Windows)等の環境において、ターミナルで使用可能
https://mctools.github.io/mcpl/hooks_phits/
PHITS形式のdump data
MCNPやGeant4形式のdump data
相互に
変換可能

--- SLIDE 25 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
SLIDE_TEXT:
追加資料
ダンプファイルの上書きとフィルター

--- SLIDE 26 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
ダンプ線源を上書きしよう
Dump data
課題 6
ダンプ線源の情報は、 [source] セクションに情報が書かれると上書きされます
[ S o u r c e ] off
   totfact = 2.0
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
   1 2 3 4 5 6 7 8 9 10 18 19
  x0 = -5
  x1 = 5
SourceB.inp
track_xz.eps
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-7.inp

--- SLIDE 27 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Dump data
課題6の答え合わせ
ダンプ線源を上書きしよう
[ S o u r c e ] off
   totfact = 2.0
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
  1 2 3 4 5 6 7 8 9 10 18 19
  x0 = -5
  x1 = 5
SourceB.inp
track_xz.eps
線源のx座標は
-5 ～ +5 の範囲で均一サンプリング
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-7.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Dump data
課題6
注意 : 上書きであって、フィルターではない
[ S o u r c e ] off
   totfact = 2.0
・ ・ ・ ・ ・ ・

[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
  1 2 3 4 5 6 7 8 9 10 18 19
  x0 = 20
  x1 = 20
 dir = -0.8
SourceB.inp
track_xz.eps
宣言は x = 20 にはなかった
しかし、上書きされてx=20へ移動

角度・時間・ウェイトなども上書き可能
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-7.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
ではフィルタを適用するにはどうしたら？
Dump data
課題7
外部ボイド(= 理想的な黒体)を使ってみよう
円筒 (厚み : 0.001 cm, 半径 : 8cm) を定義し、 黒体(mat -1)を割り当てる
[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
  1 2 3 4 5 6 7 8 9 10 18 19
$  x0 = -5
$  x1 = 5
SourceB.inp
[ S u r f a c e ]
…
  20  cz      8.
  21  pz      20.001
[ S u r f a c e ]
…
 102   2 -11.34  -11  13  -14 #104
 104    -1      -20  13  -21
 110   0        -10 #101 #102 #103 #104
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-8.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Dump data
課題7の答え合わせ
8-cm の円の内側から出る粒子をカットオフ
SourceB.inp
track_xz.eps
[ S o u r c e ]
s-type =  17
file =  cross_photon_dmp.out
dump =   -12
  1 2 3 4 5 6 7 8 9 10 18 19
$  x0 = -5
$  x1 = 5
[ S u r f a c e ]
…
  20  cz      8.
  21  pz      20.001
[ S u r f a c e ]
…
 102   2 -11.34  -11  13  -14 #104
 104    -1      -20  13  -21
 110   0        -10 #101 #102 #103 #104
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-8.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
時間のフィルタを課すにはどうしたらよいか
Dump data
課題8
外部ボイド (= 理想的黒体) と [mat time change] を組み合わせる
簡単のためCell 102 は真空にしておく
SourceB.inp
[mat time change ]
  mat time change
    3    1.05     -1
[ C e l l ]
…
 102     0      -11  13  -14 #104
 104     3   1e-10   -20  14  -21
[M a t e r i a l ]
…
mat[3]    H  1.0  $ dummy
[ T - C r o s s ]
…
   ne =    1
$       ne =  200
   t-type =    2
     tmin =   0.0
     tmax =  3.0
         nt =  100
$     axis =  eng
     axis =  t
cross_photon2.eps.eps [mat time change] なし
遅い光子
   が沢山
Mat[3] (ダミー真空) を -1 (黒体) に1.05 ns ですり替える
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-end.inp

--- SLIDE 32 ---
PPTX_FILE: phits-lec-sourceB-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Dump data
課題8の答え合わせ
cross_photon2.eps.eps [mat time change] あり
SourceB.inp
[mat time change ]
  mat time change
    3    1.05     -1
[ C e l l ]
…
 102     0      -11  13  -14 #104
 104     3   1e-10   -20  14  -21
[M a t e r i a l ]
…
mat[3]    H  1.0  $ dummy
[ T - C r o s s ]
…
   ne =    1
$       ne =  200
   t-type =    2
     tmin =   0.0
     tmax =  3.0
         nt =  100
$     axis =  eng
     axis =  t
遅い光子は
 カットオフ
Cell 104 が黒体として線源粒子を吸い取る
時間のフィルタを課すにはどうしたらよいか
外部ボイド (= 理想的黒体) と [mat time change] を組み合わせる
簡単のためCell 102 は真空にしておく
MENTIONED_INPUT_NAMES: SourceB.inp
ANSWER_FILE: input/sourceB-end.inp

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/sourceB-1.inp

[BONUS_TEXT_FILES]
NOTE: None
