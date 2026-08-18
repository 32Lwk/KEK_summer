# Lecture: advanced/sourceA

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/sourceA
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: sourceA
LECTURE_PATH_INDEX: lecture/advanced/sourceA
PPTX_FILES: phits-lec-sourceA-en.pptx, phits-lec-sourceA-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: sourceA
SECTION_KEYWORDS: t-cross, t-track

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/sourceA
LECTURE_PATH_INDEX: lecture/advanced/sourceA
PPTX_FILES: phits-lec-sourceA-en.pptx, phits-lec-sourceA-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 1
SLIDE_COUNT: 68
EXERCISE_SLIDE_COUNT: 24
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- sourceA.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Setting of various sources A
- SLIDE 02: Goal of this lecture
- SLIDE 03: sourceA.inp
- SLIDE 04: Table of Contents
- SLIDE 05: Sources with energy distribution
- SLIDE 06: How to set 1
- SLIDE 07: How to set ２
- SLIDE 08: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/sourceA-2.inp
- SLIDE 09: Answer 1
- SLIDE 10: EXERCISE 2 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-3.inp
- SLIDE 11: [ S o u r c e ]
- SLIDE 12: EXERCISE 3 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-4.inp
- SLIDE 13: [ S o u r c e ]
- SLIDE 14: Table of Contents
- SLIDE 15: Source having discrete energy
- SLIDE 16: EXERCISE 4 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-5.inp
- SLIDE 17: cross_eng.eps
- SLIDE 18: Table of Contents
- SLIDE 19: Setup of multiple source
- SLIDE 20: How to set
- SLIDE 21: EXERCISE 5 | z=40cm
  ANSWER_FILE: input/sourceA-6.inp
- SLIDE 22: Multi-source
- SLIDE 23: Table of Contents
- SLIDE 24: α, β, γ-rays and neutron sources emitted from radioisotope can be defined by simply specifying the name of RI and its ac
- SLIDE 25: EXERCISE 6 | Set 60Co sources of 200 and 100Bq in the left- and right-sides, respectively, by using e-type=28.
  ANSWER_FILE: input/sourceA-7.inp
- SLIDE 26: [ S o u r c e ]
- SLIDE 27: RI source
- SLIDE 28: EXERCISE 7 | 28
  ANSWER_FILE: input/sourceA-8.inp
- SLIDE 29: RI source
- SLIDE 30: EXERCISE 8 | RI source
  ANSWER_FILE: input/sourceA-end.inp
- SLIDE 31: Answer8
- SLIDE 32: Spectrum Information
- SLIDE 33: Table of Contents
- SLIDE 34: Summary
- SLIDE 01: 多種多様な線源の設定方法A
- SLIDE 02: 本実習の目標
- SLIDE 03: sourceA.inpの確認
- SLIDE 04: Table of Contents
- SLIDE 05: エネルギー分布をもつ線源
- SLIDE 06: 入力方法１
- SLIDE 07: 入力方法２
- SLIDE 08: EXERCISE 1 | 課題1
  ANSWER_FILE: input/sourceA-2.inp
- SLIDE 09: EXERCISE 1 | 課題1の答え合わせ
  ANSWER_FILE: input/sourceA-2.inp
- SLIDE 10: EXERCISE 2 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-3.inp
- SLIDE 11: EXERCISE 2 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-3.inp
- SLIDE 12: EXERCISE 3 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-4.inp
- SLIDE 13: EXERCISE 3 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-4.inp
- SLIDE 14: Table of Contents
- SLIDE 15: 離散的なエネルギー分布をもつ線源
- SLIDE 16: EXERCISE 4 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-5.inp
- SLIDE 17: EXERCISE 4 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-5.inp
- SLIDE 18: Table of Contents
- SLIDE 19: 複数の線源の設定
- SLIDE 20: 入力方法
- SLIDE 21: EXERCISE 5 | 課題5
  ANSWER_FILE: input/sourceA-6.inp
- SLIDE 22: EXERCISE 5 | 課題5の答え合わせ
  ANSWER_FILE: input/sourceA-6.inp
- SLIDE 23: Table of Contents
- SLIDE 24: 60CoなどのRIから放出されるα, β, γ線、及び中性子は、そのRIを直接指定することで線源として設定できる。
- SLIDE 25: EXERCISE 6 | 課題6
  ANSWER_FILE: input/sourceA-7.inp
- SLIDE 26: EXERCISE 6 | [ S o u r c e ]
  ANSWER_FILE: input/sourceA-7.inp
- SLIDE 27: RI source
- SLIDE 28: EXERCISE 7 | RI source
  ANSWER_FILE: input/sourceA-8.inp
- SLIDE 29: EXERCISE 7 | 課題7の答え合わせ
  ANSWER_FILE: input/sourceA-8.inp
- SLIDE 30: EXERCISE 8 | RI source
  ANSWER_FILE: input/sourceA-end.inp
- SLIDE 31: EXERCISE 8 | 課題8の答え合わせ
  ANSWER_FILE: input/sourceA-end.inp
- SLIDE 32: スペクトル情報
- SLIDE 33: Table of Contents
- SLIDE 34: まとめ

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: sourceA.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Setting of various sources A
Title
Jun. 2024 revised
phits/lecture/advanced/sourceA
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Goal of this lecture
Purpose
Transport simulation with various kinds of sources
Simulation with two 60Co source
Source with energy distribution

--- SLIDE 03 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
sourceA.inp
Check Input File
Basic setup
Projectile:
Geometry:
Tally:
Geometry
150MeV proton (pencil beam with radius 1.0cm)
Water cylinder (10cm radius and 20cm thickness)
[t-track] fluence  distribution
[t-cross] proton energy spectrum coming into water
Water
150MeV
Proton
track_xz.eps
cross_eng.eps
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 04 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
Table of contents
Source with energy distribution
Continuous energy distribution
Discrete energy distribution
Setup of multiple sources
RI source
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 05 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Sources with energy distribution
Energy distribution
Source energy can be defined either as mono-energetic or distributed in PHITS
Proton beam
having energy distribution

--- SLIDE 06 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
How to set 1
Energy distribution
At [source] section, set e-type subsection
The unit of energy is MeV (per nucleon for ion) or angstrom (useful only for low-energy neutrons)
[ S o u r c e ]
 totfact =   1.0
  s-type =   1
   proj =  proton
$   e0 =   150.
   r0 =   1.0
   z0 =  -10.
   z1 =  -10.
   dir =   1.0
 e-type = 1
    ne =    2
       0.0   4
     50.0   1
    100.0
[ S o u r c e ]
 totfact =   1.0
  s-type =   1
   proj =  proton
   e0 =   150.
   r0 =   1.0
   z0 =  -10.
   z1 =  -10.
   dir =   1.0

--- SLIDE 07 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
How to set ２
Energy distribution
3 ways to specify energy distribution. （switched by e-type）
e-type=1*: Continuous distribution with integral value.
e-type=21*: Continuous distribution with differential value (particle/MeV).
e-type=8*: Discrete distribution.
e-type = 1
      ne = n
     e(1)   w(1)
     e(2)   w(2)
    ・ ・ ・ ・ ・ ・
     e(n)   w(n)
     e(n+1)
For  continuous distribution (e.g. e-type=1), specify the number of energy groups (ne), bin energy (e(i)), and intensity (w(i)).
Number of e(i) is n+1 in total.
Number of w(i) is n.
(When “ne” is negative, energy distribution in each bin is uniform in [/Lethergy].)
For discrete distribution (e.g. e-type=8), specify the number of energy peaks (ne), peak energy (e(i)), and intensity (w(i)).
e-type = 8
      ne = n
     e(1)   w(1)
     e(2)   w(2)
    ・ ・ ・ ・ ・ ・
     e(n)   w(n)
Numbers of e(i) and w(i) are n.
* To change weight or give energy with angstrom, use other e-type .
（See Sec. 5.3.19 of the manual）

--- SLIDE 08 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
Set proton beam with energy distribution
Bin : [0,50], [50,100], [100,150]  in MeV
Intensity : 1:3:2 in ratio. 	(See right figure)
[ S o u r c e ]
 totfact =   1.0
  s-type =   1
   proj =  proton
   e0 =   150.
   r0 =   1.0
   z0 =  -10.
   z1 =  -10.
   dir =   1.0
 e-type =
sourceA.inp
Energy distribution
e-type = 1
      ne = n
     e(1)   w(1)
     e(2)   w(2)
    ・ ・ ・ ・ ・ ・
     e(n)   w(n)
     e(n+1)
e-type=1 format
Add e-type subsection and set energy distribution.
Comment out the line “e0=150”
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-2.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Answer 1
[ S o u r c e ]
 totfact =   1.0
 s-type =   1
 proj =  proton
$   e0 =   150.
   r0 =   1.0
   z0 =  -10.
   z1 =  -10.
   dir =   1.0
 e-type = 1
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    150.0
sourceA.inp
Energy distribution
The ratio of intensity is 1:3:2.
(The ratio is given in integral value for e-type=1.)
Set proton beam with energy distribution
Bin : [0,50], [50,100], [100,150]  in MeV
Intensity : 1:3:2 in ratio.
cross_eng.eps
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
[ S o u r c e ]
・ ・ ・ ・ ・ ・
 e-type = 1
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    150.0
Exercise 2
Change the energy bin from [100:150] to [100:200].
sourceA.inp
Energy distribution
e-type=1 : Source intensity is given by integral value.
Change the energy range of the 3rd bin.
Check the energy distribution in the new energy bin setup.
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-3.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
[ S o u r c e ]
・ ・ ・ ・ ・ ・
 e-type = 1
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    200.0
Answer 2
sourceA.inp
Energy distribution
cross_eng.eps
The ratio of energy-integrated intensity in the three bins is 1:3:2.
(The ratio is 1:3:1 if it is given in per unit energy or differential value.)
Change the energy bin from [100:150] to [100:200].
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
[ S o u r c e ]
・ ・ ・ ・ ・ ・
 e-type = 1
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    200.0
Exercise 3
Give the intensity ratio 1:3:2 in differential value for the energy bins [0:50], [50:100], [100:200] .
Use e-type=21.
sourceA.inp
Energy distribution
e-type=21 : The ratio is given in differential value.
(Choose this option to use differential spectrum.)
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-4.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
[ S o u r c e ]
・ ・ ・ ・ ・ ・
 e-type = 21
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    200.0
Answer 3
sourceA.inp
Energy distribution
The ratio of the intensity is 1:3:2 in differential value.
(The ratio is 1:3:4 in integral value.)
cross_eng.eps
Give the intensity ratio 1:3:2 in differential value for the energy bins [0:50], [50:100], [100:200] .
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
Table of contents
Source with energy distribution
Continuous energy distribution
Discrete energy distribution
Setup of multiple sources
RI source
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 15 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Source having discrete energy
Energy distribution
Sources having more than one energy peaks such as 60Co and 134Cs can be defined in PHITS.
60Co source
60Co emits gamma-rays at two energies (1.173 and 1.333 MeV) after beta decay.

--- SLIDE 16 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
[ S o u r c e ]
 totfact =   1.0
  s-type =   1
 proj =  proton
$   e0 =   150.
   r0 =   1.0
・ ・ ・ ・ ・ ・
dir =   1.0
e-type = 21
        ne = 3
      0.0    1
     50.0    3
    100.0   2
    200.0
Exercise 4
Simulate 60Co source.
Change the source particle from proton to photon.
Define an isotropic point source. (Change the source radius (r0) and direction (dir).)
Use e-type=8 and set the photon energies (1.173MeV and 1.333MeV) with intensity ratio of 1:1.
Set [t-cross] to tally photon fluence from 0 to 2 MeV with 10keV resolution (200 groups) .
[change emax, ne, part]
sourceA.inp
Energy distribution
e-type = 8
      ne = n
     e(1)   w(1)
    ・ ・ ・ ・ ・ ・
     e(n)   w(n)
e-type=8 format
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-5.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
cross_eng.eps
track_xz.eps
[ S o u r c e ]
   totfact = 1.0
   s-type =   1
     proj = photon
$   e0 =   150.
     r0 =   0.0
     z0 =  -10.
     z1 =  -10.
    dir =   all
  e-type = 8
        ne = 2
     1.173   1
     1.333   1
Answer 4
sourceA.inp
Energy distribution
[ T - C r o s s ]
・ ・ ・ ・ ・ ・
emin =   0.0
emax =   2.0
ne =   200
unit =    1
axis =  eng
file = cross_eng.out
output = flux
part =  photon
epsout =    1
60Co source
Simulate 60Co source.
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
Table of contents
Source with energy distribution
Continuous energy distribution
Discrete energy distribution
Setup of multiple sources
RI source
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 19 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Setup of multiple source
Multi-source
Multiple source with different radiation types, positions, or energy distribution can be defined in PHITS.
60Co source
60Co source
60Co sources placed at right and left of target with the intensity ratio of 2:1.

--- SLIDE 20 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
How to set
In [source] section, set multi-source subsection starting with ”<source>=relative intensity”
Set totfact to normalize the total source intensity
Multi-source
[ S o u r c e ]
 totfact = 1.0
 <source> = 2.0
  s-type =   1
     proj = proton
・ ・ ・ ・ ・ ・

<source> = 1.0
  s-type =   1
     proj = neutron
・ ・ ・ ・ ・ ・

<source> = 3.0
  s-type =   2
     proj = photon
・ ・ ・ ・ ・ ・
Normalization factor.
If it is positive, particles are produced with the ratio of the defined intensity.
If it is negative, same number of particles are produced, and their weight is adjusted to realize the defined intensity ratio.
Triple sources
Relative intensity of each source.
(In this case, 2:1:3 from the top.)

--- SLIDE 21 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
z=40cm
z=-10cm
Exercise 5
60Co source
60Co source
Multi-source
z axis
Set 60Co sources at the left and right of the cylindrical water (z=-10, 40cm) with intensity ratio of 2:1.
Add <source> lines to define two sources
Put two point sources at the position z=-10 and 40cm (Change z0 and z1 to define point sources)
Define the relative intensity of the left (z=-10cm) and the right (z=40cm) source to be 2:1.
ANSWER_FILE: input/sourceA-6.inp

--- SLIDE 22 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Multi-source
sourceA.inp
track_xz.eps
[ S o u r c e ]
   totfact = 1.0
 <source> = 2.0
 s-type =   1
     proj = photon
$   e0 =   150.
     r0 =   0.0
     z0 =  -10.
     z1 =  -10.
・ ・ ・ ・ ・ ・
 <source> = 1.0
   s-type =   1
     proj = photon
     r0 =   0.0
     z0 =  40.
     z1 =  40.
    dir =   all
  e-type = 8
        ne = 2
     1.173   1
     1.333   1
Answer 5
Set 60Co sources at the left and right of the cylindrical water (z=-10, 40cm) with intensity ratio of 2:1.
Two 60Co sources.
(With intensity ratio of right:left = 2:1)
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 23 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
Table of contents
Source having energy distribution
Continuous energy distribution
Discrete energy distribution
Setup of multiple sources
RI source
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 24 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
α, β, γ-rays and neutron sources emitted from radioisotope can be defined by simply specifying the name of RI and its activity
RI (Radioactive Isotope) source
RI source
How to set.
Set e-type=28 or 29. (29 for changing weight of source.)
e-type = 28
      ni = n
     RI(1)   A(1)
     ・ ・ ・ ・ ・ ・
     RI(n)   A(n)
   norm = ***
e-type=28 format
Number of RIs.
Name of the RIs and their activity (Bq).
Option for normalization
    0: (/sec) (Default)
    1: (/source)

--- SLIDE 25 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Set 60Co sources of 200 and 100Bq in the left- and right-sides, respectively, by using e-type=28.
Change e-type.
Specify 60Co of 200 and 100 Bq at z=-10 and 40 cm, respectively. (Name format is Co-60 or 60Co.)
In case of e-type=28, 29, set <source> to be 1.0 and totfact to be the number of <source> subsections (totfact=2.0 in this case) because the absolute activity of RIs is directly defined in Bq.
Normalize tally results to the unit of (/sec) (not necessary to be explicitly specified).
RI source
Exercise 6
sourceA.inp
[ S o u r c e ]
 totfact = 1.0
 <source> = 2.0
 ・ ・ ・ ・ ・ ・
     z1 =  -10.
    dir =   all
  e-type = 8
        ne = 2
     1.173   1
     1.333   1
<source> = 1.0
 ・ ・ ・ ・ ・ ・
     z1 =  40.
    dir =   all
  e-type = 8
        ne = 2
     1.173   1
     1.333   1
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-7.inp

--- SLIDE 26 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
[ S o u r c e ]
   totfact = 2.0
<source> = 1.0
 ・ ・ ・ ・ ・ ・
     z1 =  -10.
    dir =   all
 e-type = 28
        ni = 1
        Co-60    200.0
  norm =   0
sourceA.inp
RI source
cross_eng.eps
(continued)
<source> = 1.0
 ・ ・ ・ ・ ・ ・
        z1 =  40.
       dir =   all
  e-type = 28
        ni = 1
     Co-60    100.0
  norm =   0
Set 60Co sources of 200 and 100Bq in the left- and right-sides, respectively, by using e-type=28.
Answer 6
Gamma spectrum of 60Co sources (1.173 & 1.333 MeV) is realized. Note that the unit of these data is [1/cm2/sec], though plot axis label is [1/cm2/source].
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 27 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
RI source
Decay time & Daughter nuclide
27
γ-rays are not emitted from 137Cs without considering its daughter nuclide
137Cs: 100 Bq
137mBa: 0 Bq
Cs-137    100.0
dtime = 0
Cs-137    100.0
dtime = 30.04*365.25*24*3600
137Cs: 50 Bq
137mBa: 50 Bq
For dtime > 0, activities at dtime (sec) later including daughter nuclides are considered
For dtime < 0, activity at half-life x dtime prior are calculated, and then, current activities including daughter nuclides are considered
Cs-137    100.0
dtime = -1.0
Now
30 years later
30 years ago
137Cs: 200 Bq
137mBa: 0 Bq
137Cs: 100 Bq
137mBa: 100 Bq
are considered as source RIs
Specify decay time parameter “dtime”
γ-rays of 0.6617 MeV are emitted from an isomer of Ba (137mBa) after the beta decay of 137Cs

--- SLIDE 28 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
28
Change 200Bq 60Co to 200Bq 137Cs, and consider the radioactive equilibrium.
RI source
sourceA.inp
Change Co-60 to Cs-137 in the first <source> subsection.
Add dtime=-10 to the subsection (optional because -10 is the default value).
Exercise 7
[ S o u r c e ]
   totfact = 2.0
<source> = 1.0
 ・ ・ ・ ・ ・ ・
     z1 =  -10.
    dir =   all
 e-type = 28
        ni = 1
        Co-60    200.0
  norm =   0
    dtime =
<source> = 1.0
 ・ ・ ・ ・ ・ ・
Most RIs reach equilibrium after 10 half-lives
10 x half-life is not enough to reach equilibrium for some RIs whose half-life is much shorter than that of its daughter nuclide; e.g. 105Ru（T1/2 = 4.44h）→ 105Rh（T1/2 = 35.36h）

Too large dtime (e.g. dtime = -1000.0)  may cause an error
dtime = -10 is convenient to reproduce
most RI sources in equilibrium.
Notes
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-8.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
RI source
sourceA.inp
cross_eng.eps
Answer 7
0.6617 MeV gamma-rays are emitted from 137mBa by defining 137Cs source.
Change 200Bq 60Co to 200Bq 137Cs, and consider the radioactive equilibrium.
[ S o u r c e ]
   totfact = 2.0
<source> = 1.0
 ・ ・ ・ ・ ・ ・
     z1 =  -10.
    dir =   all
 e-type = 28
        ni = 1
      Cs-137    200.0
  norm =   0
    dtime = -10
<source> = 1.0
 ・ ・ ・ ・ ・ ・
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
RI source
Exercise8
30
Let’s define 137Cs β-ray source
Change ‘proj’ in the <source> subsection for 137Cs from ‘photon’ to ‘all’

Set “part = photon electron” in [t-track] & [t-cross] to see the trajectories and energy spectra of electrons as well as photons
‘proj = all’ indicates all types of radiations emitted from RI are automatically considered as the sources in the PHITS simulation
ANSWER_FILE: input/sourceA-end.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Answer8
RI source
sourceA.inp
[ S o u r c e ]
   totfact = 2.0
<source> = 1.0
 proj =  all
 ・ ・ ・ ・ ・ ・
ni = 1
      Cs-137    200.0
  norm =   0
    dtime = -10
track_xz.eps
(2nd page)
cross_eng.eps
Continuum spectrum of β-rays
MENTIONED_INPUT_NAMES: sourceA.inp

--- SLIDE 32 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Spectrum Information
Nuclear decay data are taken from ICRP Pub.107
[ S o u r c e ]
  totfact =   3.0000        # (D=1.0) global factor
$ totfact =   1101.2        # revised global factor by e-type = 28 or 29

 <Source> =   1.0000        # weight of this sub-source
$<Source> =   444.06        # revised global factor by e-type=28 or 29
   s-type =   1             # cylindrical source
…
e-type =  28             # RI source
       ni =   1             # number of registered nuclide
                            #  data = ( nuclide(i), activity(i), i = 1, ni )
    Cs-137   2.00000E+02    # (Bq)
                            # ->  2.00000E+02 (Bq), half life:  30.16710002 (year)
$   X-rays (X)
$   Energy (MeV/u)             Activity (Bq) X Yield (abs.)
$      Lower        Upper
$   1.58399E-05  1.58399E-05   2.00000E+02*2.77693E-16
$   1.85999E-05  1.85999E-05   2.00000E+02*4.45808E-06
$   1.08844E-04  1.08844E-04   2.00000E+02*5.21835E-11
$   3.30500E-04  3.30500E-04   2.00000E+02*9.46744E-13
phits.out
Energy spectrum and intensity emitted from each RI and radiation type (X-ray, γ-ray, β-ray, auger etc.) are written in “Input Echo”

--- SLIDE 33 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
Table of contents
Source having energy distribution
Continuous energy distribution
Discrete energy distribution
Setup of multiple source
RI source
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 34 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Summary
Summary
Source energy distribution (continuous and discrete) can be defined by specifying e-type in the [source] section.
Multiple sources can be defined by setting <source> subsections.
α, β, γ decay sources and spontaneous fission neutron sources can be defined by directly specifying the name and activity of RIs.
Other lecture notes for source generation
advanced/sourceB: 2-step calculation with “dump source” data
advanced/cosmicray: Cosmic-ray source
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 01 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
多種多様な線源の設定方法A
Title
2024年6月改訂
phits/lecture/advanced/sourceA
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
本実習の目標
Purpose
様々な種類の線源を考慮した粒子輸送シミュレーションを実行できるようになる。
2箇所に60Co線源を配置したシミュレーション
連続的なエネルギー分布をもつ線源

--- SLIDE 03 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
sourceA.inpの確認
Check Input File
基本計算条件
入射粒子：
体系：
タリー：
計算体系
150MeV陽子（半径1.0cmのペンシルビーム）
円柱状（半径10cm, 厚さ20cm）の水と真空のみ
[t-track]によるフルエンス空間分布
[t-cross]による水領域へ入射する陽子のエネルギー分布
水
150MeV
陽子
track_xz.eps
cross_eng.eps

--- SLIDE 04 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
実習内容
エネルギー分布をもつ線源
連続的なエネルギー分布
離散的なエネルギー分布
マルチソースの設定
RI線源の設定
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 05 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
エネルギー分布をもつ線源
Energy distribution
単一エネルギーの線源だけでなく、エネルギー分布をもつ線源を設定することが可能。
陽子ビーム
エネルギー分布をもたせる

--- SLIDE 06 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
入力方法１
Energy distribution
[source]セクションにおいて、e-typeサブセクションを設定する。
エネルギーはMeV（イオンの場合は核子あたり）とÅ（低エネルギー中性子の場合に有用）の2種の単位で設定可能
[ S o u r c e ]
 totfact =   1.0
  s-type =   1
   proj =  proton
$   e0 =   150.
   r0 =   1.0
   z0 =  -10.
   z1 =  -10.
   dir =   1.0
 e-type = 1
    ne =    2
       0.0   4
     50.0   1
    100.0
[ S o u r c e ]
 totfact =   1.0
  s-type =   1
   proj =  proton
   e0 =   150.
   r0 =   1.0
   z0 =  -10.
   z1 =  -10.
   dir =   1.0

--- SLIDE 07 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
入力方法２
Energy distribution
エネルギー分布の与え方は3種類。（e-typeの値で使い分ける）
e-type=1*: 連続的なエネルギー分布を積分量で与える。
e-type=21*: 連続的なエネルギー分布を微分量（単位を[個/MeV]）で与える。
e-type=8*: 離散的なエネルギー分布を与える。
e-type = 1
      ne = n
     e(1)   w(1)
     e(2)   w(2)
    ・ ・ ・ ・ ・ ・
     e(n)   w(n)
     e(n+1)
連続的な分布（e-type=1など）の場合:
エネルギー群数ne, エネルギー分点e(i), 各エネルギービンの粒子の生成確率w(i)をデータで与える。
e(i)は合計n+1個、w(i)は合計n個与える。
（neが負の場合は
レサジー単位で均一に粒子が分布）
離散的な分布（e-type=8など）の場合:
エネルギー点数ne, エネルギー分点e(i), 各エネルギーにおける粒子の生成確率w(i)をデータで与える。
e-type = 8
      ne = n
     e(1)   w(1)
     e(2)   w(2)
    ・ ・ ・ ・ ・ ・
     e(n)   w(n)
e(i)とw(i)は共にn個与える。
* ウエイトを変えたりÅの単位で与える場合は別のe-typeを使う。（マニュアル5.3.19「エネルギー分布の定義」参照）

--- SLIDE 08 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1
0から50MeV, 50から100MeV, 100から150MeVのエネルギー領域におけるビーム強度が1:3:2となる陽子線源を設定してみましょう（右図参照）。
e-typeサブセクションを追加し、エネルギー分布を設定する。（e-type=1を使用する）
e0=150の行をコメントアウトする。
[ S o u r c e ]
 totfact =   1.0
  s-type =   1
   proj =  proton
   e0 =   150.
   r0 =   1.0
   z0 =  -10.
   z1 =  -10.
   dir =   1.0
 e-type =
sourceA.inp
Energy distribution
e-type = 1
      ne = n
     e(1)   w(1)
     e(2)   w(2)
    ・ ・ ・ ・ ・ ・
     e(n)   w(n)
     e(n+1)
e-type=1の入力形式
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-2.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1の答え合わせ
0から50MeV, 50から100MeV, 100から150MeVのエネルギー領域におけるビーム強度が1:3:2となる陽子線源を設定してみましょう。
[ S o u r c e ]
 totfact =   1.0
 s-type =   1
 proj =  proton
$   e0 =   150.
   r0 =   1.0
   z0 =  -10.
   z1 =  -10.
   dir =   1.0
 e-type = 1
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    150.0
sourceA.inp
Energy distribution
cross_eng.eps
強度の比率が1:3:2となっている。
（ただしe-type=1は各ビンの積分量を与える。）
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-2.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
[ S o u r c e ]
・ ・ ・ ・ ・ ・
 e-type = 1
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    150.0
課題2
100から150MeVのエネルギービンを100から200MeVに拡げてみましょう。
sourceA.inp
Energy distribution
e-type=1の場合は、エネルギーに関して積分した量で線源強度を設定する。
3番目のエネルギー範囲のみ変更する。
エネルギービンの幅が50MeV, 50MeV, 100MeVと、等間隔ではなくなった場合にどうなるかを確認する。
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-3.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
[ S o u r c e ]
・ ・ ・ ・ ・ ・
 e-type = 1
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    200.0
課題2の答え合わせ
100から150MeVのエネルギービンを100から200MeVに拡げてみましょう。
sourceA.inp
Energy distribution
cross_eng.eps
3つのビンをエネルギーで積分すると1:3:2となっている。
（単位エネルギーあたり（すなわち微分量）で見ると1:3:1。）
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-3.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
[ S o u r c e ]
・ ・ ・ ・ ・ ・
 e-type = 1
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    200.0
課題3
0から50MeV, 50から100MeV, 100から200MeVの各領域におけるビーム強度が微分量で1:3:2となる線源を設定してみましょう。
e-type=21を用いる。
sourceA.inp
Energy distribution
e-type=21の場合は、積分量ではなく微分量で比の値を設定する。
（微分スペクトルを設定する場合はこちらを使う。）
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-4.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
[ S o u r c e ]
・ ・ ・ ・ ・ ・
 e-type = 21
       ne = 3
       0.0    1
     50.0    3
    100.0   2
    200.0
課題3の答え合わせ
sourceA.inp
Energy distribution
強度の比率は微分量で1:3:2。
（積分量で見ると1:3:4。）
cross_eng.eps
0から50MeV, 50から100MeV, 100から200MeVの各領域におけるビーム強度が微分量で1:3:2となる線源を設定してみましょう。
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-4.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
実習内容
エネルギー分布をもつ線源
連続的なエネルギー分布
離散的なエネルギー分布
マルチソースの設定
RI線源の設定
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 15 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
離散的なエネルギー分布をもつ線源
Energy distribution
60Coや134Csのように、壊変に伴って複数のエネルギーのガンマ線を放出する放射線源を模擬することができる。
60Co線源
60Coは、ベータ崩壊の後、1.173MeVと1.333MeVの2本のガンマ線を出す。

--- SLIDE 16 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
[ S o u r c e ]
 totfact =   1.0
  s-type =   1
 proj =  proton
$   e0 =   150.
   r0 =   1.0
・ ・ ・ ・ ・ ・
dir =   1.0
e-type = 21
        ne = 3
      0.0    1
     50.0    3
    100.0   2
    200.0
課題4
60Co線源を模擬してみましょう。
線源を光子（photon)に変更する。
等方点線源とする（半径r0,方向dirのパラメータを変える）。
e-type=8として，1.173MeVと1.333MeVの光子が1：1の割合で放出されるようにする。
[t-cross]で0〜2MeV間の光子フルエンスを10keV分解能（200群）でタリーするように変更する（emax, ne, partを調整）。
sourceA.inp
Energy distribution
e-type = 8
      ne = n
     e(1)   w(1)
    ・ ・ ・ ・ ・ ・
     e(n)   w(n)
e-type=8の入力形式
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-5.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
[ S o u r c e ]
   totfact = 1.0
   s-type =   1
     proj = photon
$   e0 =   150.
     r0 =   0.0
     z0 =  -10.
     z1 =  -10.
    dir =   all
  e-type = 8
        ne = 2
     1.173   1
     1.333   1
課題4の答え合わせ
sourceA.inp
Energy distribution
cross_eng.eps
[ T - C r o s s ]
・ ・ ・ ・ ・ ・
emin =   0.0
emax =   2.0
ne =   200
unit =    1
axis =  eng
file = cross_eng.out
output = flux
part =  photon
epsout =    1
track_xz.eps
60Co線源
60Co線源を模擬してみましょう。
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-5.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
実習内容
エネルギー分布をもつ線源
連続的なエネルギー分布
離散的なエネルギー分布
マルチソースの設定
RI線源の設定
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 19 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
複数の線源の設定
Multi source
線種や位置、エネルギー分布などの条件を変えた複数の線源を設定することが可能。
60Co線源
60Co線源
60Co線源が、左右それぞれに2:1の量で配置された状況を模擬したい

--- SLIDE 20 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
入力方法
[source]セクションにおいて、”<source>=相対比”の指定で始まる複数のサブセクションを設定する
totfactを使って線源全体の規格化を行う
Multi source
[ S o u r c e ]
 totfact = 1.0
 <source> = 2.0
  s-type =   1
     proj = proton
・ ・ ・ ・ ・ ・

<source> = 1.0
  s-type =   1
     proj = neutron
・ ・ ・ ・ ・ ・

<source> = 3.0
  s-type =   2
     proj = photon
・ ・ ・ ・ ・ ・
規格化定数
正の数の場合は相対比にしたがって各粒子を生成
負の数の場合は同数の粒子を発生し、相対比にしたがってweightを変化
3種の線源を設定した場合
各線源の強度の相対比
（この場合は上から順に2:1:3）

--- SLIDE 21 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5
60Co線源を円柱状の水の左右（z=-10, 40cm）の位置に2:1の比で配置した状況を模擬してみましょう。
<source>=の行を加えて、2つのサブセクションをつくる
点線源の位置をそれぞれz=-10と40cmとする（z0とz1パラメーターを調整）
左(z=-10cm)と右(z=40cm)の線源から2:1の割合で光子が発生するようにする
Multi source
z=40cm
z=-10cm
60Co線源
60Co線源
z軸
ANSWER_FILE: input/sourceA-6.inp

--- SLIDE 22 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5の答え合わせ
60Co線源を円柱状の水の左右（z=-10, 40cm）の位置に2:1の比で配置した状況を模擬してみましょう。
Multi source
sourceA.inp
track_xz.eps
60Co線源
（強度比は左:右=2:1）
[ S o u r c e ]
   totfact = 1.0
 <source> = 2.0
 s-type =   1
     proj = photon
$   e0 =   150.
     r0 =   0.0
     z0 =  -10.
     z1 =  -10.
・ ・ ・ ・ ・ ・
 <source> = 1.0
   s-type =   1
     proj = photon
     r0 =   0.0
     z0 =  40.
     z1 =  40.
    dir =   all
  e-type = 8
        ne = 2
     1.173   1
     1.333   1
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-6.inp

--- SLIDE 23 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
実習内容
エネルギー分布をもつ線源
連続的なエネルギー分布
離散的なエネルギー分布
マルチソースの設定
RI線源の設定
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 24 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
60CoなどのRIから放出されるα, β, γ線、及び中性子は、そのRIを直接指定することで線源として設定できる。
RI（放射性同位体）線源
RI source
入力方法
e-type=28, 29を使う（29はウエイトを変える場合）。
e-type = 28
      ni = n
     RI(1)   A(1)
     ・ ・ ・ ・ ・ ・
     RI(n)   A(n)
   norm = ***
e-type=28の入力形式
指定するRIの数
RIと放射能（単位はBq）
規格化のオプション
 0: (/sec) （初期値）
 1: (/source)

--- SLIDE 25 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題6
e-type=28を使って、水円柱の左右にそれぞれ200と100Bqの60Co線源を設定してみましょう。
e-typeを変更する。
z=-10, 40cmのそれぞれに200, 100 Bqの60Coを指定する。（RIを指定する書式は、Co-60か60Co）
単位時間毎の結果を出力させる（norm=0）。
（注意）e-type=28,29かつnorm = 0の場合、<source>は常に1.0として，totfactはマルチソースの数（この場合は2）を設定する必要があります。これは，線源の絶対値を各RIの放射能で直接指定するためです。
RI source
sourceA.inp
[ S o u r c e ]
 totfact = 1.0
 <source> = 2.0
 ・ ・ ・ ・ ・ ・
     z1 =  -10.
    dir =   all
  e-type = 8
        ne = 2
     1.173   1
     1.333   1
<source> = 1.0
 ・ ・ ・ ・ ・ ・
     z1 =  40.
    dir =   all
  e-type = 8
        ne = 2
     1.173   1
     1.333   1
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-7.inp

--- SLIDE 26 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
[ S o u r c e ]
   totfact = 2.0
<source> = 1.0
 ・ ・ ・ ・ ・ ・
     z1 =  -10.
    dir =   all
 e-type = 28
        ni = 1
        Co-60    200.0
  norm =   0
課題6の答え合わせ
sourceA.inp
RI source
cross_eng.eps
60Coから出る2本のγ線（1.173&1.333MeV）が放出されている。グラフの単位は[1/cm2/source]だが，実際には[1/cm2/sec]で出力されている。
e-type=28を使って、水円柱の左右にそれぞれ200と100Bqの60Co線源を設定してみましょう。
（左の続き）
<source> = 1.0
 ・ ・ ・ ・ ・ ・
        z1 =  40.
       dir =   all
  e-type = 28
        ni = 1
     Co-60    100.0
  norm =   0
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-7.inp

--- SLIDE 27 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
RI source
崩壊時間・娘核の考慮
27
137Csは、ベータ崩壊の後、 Baの準安定同位体(137mBa)を経て0.6617MeVのガンマ線を出す。
娘核の崩壊を考慮しない限り137Csから0.6617MeVのγ線が出ない
137Csが100Bq
137mBaが0Bq
Cs-137    100.0
dtime = 0
Cs-137    100.0
dtime = 30.04*365.25*24*3600
137Csが50Bq
137mBaが50Bq
dtime>0の場合，単純にdtime秒，時間を進める
dtime<0の場合，半減期 ｘ dtime時間を遡って過去の放射能を計算し崩壊を考慮して現在まで戻す
Cs-137    100.0
dtime = -1.0
現在
30年後
30年前
137Csが200Bq
137mBaが0Bq
137Csが100Bq
137mBaが100Bq
が結果として出力される
崩壊時間パラメータ
dtimeを設定

--- SLIDE 28 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
RI source
課題7
28
RI線源の1つを137Csに変更し、放射平衡を考えましょう。
sourceA.inp
200Bqの60Coを200Bqの137Csに変更する。
137Csに変更した<source>サブセクションにdtime=-10を加える。（dtimeのデフォルト値）
[ S o u r c e ]
   totfact = 2.0
<source> = 1.0
 ・ ・ ・ ・ ・ ・
     z1 =  -10.
    dir =   all
 e-type = 28
        ni = 1
        Co-60    200.0
  norm =   0
    dtime =
<source> = 1.0
 ・ ・ ・ ・ ・ ・
10半減期まで遡ると，ほとんどの核種は平衡状態に達する
 → RI線源の現在の状態を再現するには，これが便利
娘核の半減期の方が圧倒的に長い場合は，10半減期では平衡状態に達しないので注意が必要
 例：105Ru（T1/2 = 4.44h）→ 105Rh（T1/2 = 35.36h）

あまりに長い崩壊時間（例：dtime = -1000.0）を設定するとエラーが出る
注意点
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-8.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
課題7の答え合わせ
RI source
sourceA.inp
[ S o u r c e ]
   totfact = 2.0
<source> = 1.0
 ・ ・ ・ ・ ・ ・
     z1 =  -10.
    dir =   all
 e-type = 28
        ni = 1
      Cs-137    200.0
  norm =   0
    dtime = -10
<source> = 1.0
 ・ ・ ・ ・ ・ ・
137Csが崩壊し、137mBaを経由して放出される0.6617MeVのガンマ線を線源に設定できる。
cross_eng.eps
RI線源の1つを137Csに変更し、放射平衡を考えましょう。
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-8.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
RI source
課題8
30
137Csから放出されるβ線も考慮してみよう
137Csに変更した<source>サブセクションのprojをallに変更する

[t-track]及び[t-cross]のpartをそれぞれphoton electronにして，電子及び光子の結果をそれぞれ出力させる
（RI線源の場合、proj = allとすると定義したRIから放出される全ての放射線が線源として自動的に設定されます）
ANSWER_FILE: input/sourceA-end.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
課題8の答え合わせ
RI source
sourceA.inp
track_xz.eps
2ページ目
cross_eng.eps
β線は連続エネルギー分布
[ S o u r c e ]
   totfact = 2.0
<source> = 1.0
 proj =  all
 ・ ・ ・ ・ ・ ・
ni = 1
      Cs-137    200.0
  norm =   0
    dtime = -10
MENTIONED_INPUT_NAMES: sourceA.inp
ANSWER_FILE: input/sourceA-end.inp

--- SLIDE 32 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
スペクトル情報
核崩壊データの出典はICRP Pub.107
[ S o u r c e ]
  totfact =   3.0000        # (D=1.0) global factor
$ totfact =   1101.2        # revised global factor by e-type = 28 or 29

 <Source> =   1.0000        # weight of this sub-source
$<Source> =   444.06        # revised global factor by e-type=28 or 29
   s-type =   1             # cylindrical source
…
e-type =  28             # RI source
       ni =   1             # number of registered nuclide
                            #  data = ( nuclide(i), activity(i), i = 1, ni )
    Cs-137   2.00000E+02    # (Bq)
                            # ->  2.00000E+02 (Bq), half life:  30.16710002 (year)
$   X-rays (X)
$   Energy (MeV/u)             Activity (Bq) X Yield (abs.)
$      Lower        Upper
$   1.58399E-05  1.58399E-05   2.00000E+02*2.77693E-16
$   1.85999E-05  1.85999E-05   2.00000E+02*4.45808E-06
$   1.08844E-04  1.08844E-04   2.00000E+02*5.21835E-11
$   3.30500E-04  3.30500E-04   2.00000E+02*9.46744E-13
phits.out
インプットエコーに、発生する粒子スペクトルが核種や
線種毎（X-ray, γ-ray, β-ray, augerなど）に出力されている

--- SLIDE 33 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
Table of Contents
実習内容
エネルギー分布をもつ線源
連続的なエネルギー分布
離散的なエネルギー分布
マルチソースの設定
RI線源の設定
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 34 ---
PPTX_FILE: phits-lec-sourceA-en.pptx
SLIDE_TEXT:
まとめ
Summary
[source]セクションにおいて、e-typeを指定することにより、連続的・離散的なエネルギー分布を線源として設定できる。
<source>サブセクションの設定により、複数の線源を用いたシミュレーションが可能となる。
RI（放射能同位体）を直接指定して、その崩壊により発生するα, β, γ線, 及び中性子を設定できる。
線源発生に関する他の講習会資料
advanced/sourceB: dump線源を用いた２段階計算方法
advanced/cosmicray: 宇宙線線源の使い方

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/sourceA-1.inp

[BONUS_TEXT_FILES]
NOTE: None
