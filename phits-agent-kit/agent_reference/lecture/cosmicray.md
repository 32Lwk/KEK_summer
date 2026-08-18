# Lecture: advanced/cosmicray

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/cosmicray
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: cosmicray
LECTURE_PATH_INDEX: lecture/advanced/cosmicray
PPTX_FILES: phits-lec-cosmicray-en.pptx, phits-lec-cosmicray-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: CosmicRay, muon, muon-source, source
SECTION_KEYWORDS: 1, 2, 3, 4, cm, mev, multiplier, t-cross, t-track

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/cosmicray
LECTURE_PATH_INDEX: lecture/advanced/cosmicray
PPTX_FILES: phits-lec-cosmicray-en.pptx, phits-lec-cosmicray-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 4
SLIDE_COUNT: 66
EXERCISE_SLIDE_COUNT: 24
BONUS_INPUT_COUNT: 23
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- CosmicRay.inp
- muon-source.inp
- muon.inp
- source.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Cosmic-ray simulation using PHITS
- SLIDE 02: Table of Contents
- SLIDE 03: Cosmic-ray Environment
- SLIDE 04: Cosmic-ray Source in PHITS
- SLIDE 05: cosmicray.inp
- SLIDE 06: Recommended parameter setting
- SLIDE 07: Source setting
- SLIDE 08: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 09: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 10: EXERCISE 3 | Exercise 3
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 11: EXERCISE 4 | Exercise 4
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 12: EXERCISE 5 | Exercise 5
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 13: cross.eps
- SLIDE 14: EXERCISE 6 | Exercise 6
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 15: Answer 6
- SLIDE 16: EXERCISE 7 | Exercise 7
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 17: Table of Contents
- SLIDE 18: Why is Cosmic-ray Dosimetry Necessary?
- SLIDE 19: EXERCISE 8 | Exercise 8
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 20: EXERCISE 9 | y: Dose equivalent [uSv/day]
  ANSWER_FILE: (missing)
- SLIDE 21: EXERCISE 10 | Exercise 10
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 22: Answer 10
- SLIDE 23: Table of Contents
- SLIDE 24: Introduction of Muon Radiography
- SLIDE 25: Disk source area
- SLIDE 26: Reflection Boundary
- SLIDE 27: EXERCISE 10 | Exercise 10
  ANSWER_FILE: input/exercise10/muon.inp
- SLIDE 28: Answer 10
- SLIDE 29: EXERCISE 11 | Exercise 11
  ANSWER_FILE: input/exercise10/muon.inp
- SLIDE 30: Answer 11
- SLIDE 31: Table of Contents
- SLIDE 32: Summary
- SLIDE 33: Appendix (Selection of sample input)
- SLIDE 01: PHITSを用いた宇宙線挙動解析
- SLIDE 02: 本実習の流れ
- SLIDE 03: 宇宙放射線環境
- SLIDE 04: PHITSの宇宙線線源モード
- SLIDE 05: cosmicray.inp
- SLIDE 06: 宇宙線挙動解析奨励設定
- SLIDE 07: 宇宙線線源設定
- SLIDE 08: EXERCISE 1 | 課題１
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 09: EXERCISE 2 | 課題２
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 10: EXERCISE 3 | 課題３
  ANSWER_FILE: input/allGCR/source.inp
- SLIDE 11: EXERCISE 4 | 課題４
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 12: EXERCISE 5 | 課題５
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 13: cross.eps
- SLIDE 14: EXERCISE 6 | 課題６
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 15: 解答６
- SLIDE 16: EXERCISE 7 | 課題７
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 17: 本実習の流れ
- SLIDE 18: 宇宙線被ばく線量評価の必要性
- SLIDE 19: EXERCISE 8 | 課題８
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 20: EXERCISE 9 | y: Dose equivalent [uSv/day]
  ANSWER_FILE: (missing)
- SLIDE 21: EXERCISE 10 | 課題１０
  ANSWER_FILE: input/exercise01/CosmicRay.inp
- SLIDE 22: 解答１０
- SLIDE 23: 本実習の流れ
- SLIDE 24: ミューオンラジオグラフィの概要
- SLIDE 25: muon.inp
- SLIDE 26: 反射境界
- SLIDE 27: EXERCISE 10 | 課題１０
  ANSWER_FILE: input/exercise10/muon.inp
- SLIDE 28: 解答１０
- SLIDE 29: EXERCISE 11 | 課題１１
  ANSWER_FILE: input/exercise10/muon.inp
- SLIDE 30: 解答１１
- SLIDE 31: 本実習の流れ
- SLIDE 32: まとめ
- SLIDE 33: 参考資料 (サンプル入力ファイルの選択方法）

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: CosmicRay.inp
FILE: muon-source.inp
FILE: muon.inp
FILE: source.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Cosmic-ray simulation using PHITS
Jan 2025 revised
phits/lecture/advanced/cosmicray

--- SLIDE 02 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Table of Contents
Cosmic-ray Source Mode in PHITS
Application to Cosmic-ray Dosimetry
Application to Muon Radiography
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 03 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Cosmic-ray Environment
https://phits.jaea.go.jp/expacs
Galactic Cosmic-Ray (GCR)
Existence: Everywhere (in space & atmosphere)
Temporal variation: gradually changed by solar activity cycle
Spectrum: Hard spectrum up to 1020 eV
Solar Energetic Particle (SEP)
Existence: In space, seldom in the atmosphere
Temporal variation: impulsively changed during solar particle event
Spectrum: Soft spectrum up to a few GeV
Trapped Particle (TP)
Existence: Only in the magnetosphere
Temporal variation: gradually changed by solar activity cycle
Spectrum: Soft spectrum up to several hundred MeV

--- SLIDE 04 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Cosmic-ray Source in PHITS
https://phits.jaea.go.jp/expacs
Galactic Cosmic-Ray (GCR)
In space & LEO: DLR model [1]
In atmosphere: PARMA/EXPACS [2]
Solar Energetic Particle (SEP)
In space: Tylka’s model [3]
In atmosphere & LEO: Not applicable
Trapped Particle (TP)
In LEO: AP8 (only for proton) [4]
In space & atmosphere: Not exist
Altitude, geographical, and angular dependences of GCR fluxes can be considered
[1] D. Matthia et al. Adv Space Res 51: 329-338 (2013)
[2] T. Sato PLOS ONE 11(8): e0160390 (2016)
[3] A.J. Tylka et al. 31th ICRC, Poland (2009)
[4] D. Sawyer & J. Vette, NSSDC Report 76-06 (1976)

--- SLIDE 05 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
cosmicray.inp
Basic setup
GCR protons in free space with radius of 200 cm
(source condition is specified in source.inp except for proj)
Co-centric spherical shells with radius of 100, 110, & 200 cm
[t-track] for visualizing particle trajectories (track_xz.out)
[t-track] for checking energy spectrum (track_reg.out)
[t-cross] for checking angular distribution at z = 0 cm (cross.out)
Source：

Geometry：
Tally：
track_xz.eps*
*Rotated by 90 degree (see FAQ 3.8 in manual)
Surface for
[t-cross]
track_reg.eps
cross.eps
← downward
upward →
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp

--- SLIDE 06 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Recommended parameter setting
[ P a r a m e t e r s ]
 icntl    =           0     # (D=0) 3:ECH 5:NOR 6:SRC 7,8:GSH 11:DSH 12:DUMP
 maxcas   =        1000     # (D=10) number of particles per one batch
 maxbch   =          10     # (D=10) number of batches
 e-mode   =           2     # (D=0) 0: Normal, 1: Event generator mode Ver.1, 2: Ver.2
 irqmd    =           1     # (D=0) 0: JQMD legacy version, 1: JQMD-2.0
 negs     =           2     # (D=-1) =-1:original, =0:No, =1:EGS
 mdbatima =        3000     # (D=500) max database size of ATIMA
 maxbnk   =      100000     # (D=10000) maximum bank memory length
 iMeVperU =           1     # (D=0) 0:[MeV] or 1:[MeV/u] is unit of tally output
 emin(12) =  1.00000000     # (D=1.e+9) cut-off energy of electron (MeV)
 emin(13) =  1.00000000     # (D=1.e+9) cut-off energy of positron (MeV)
irqmd=1: Use an accurate but time-consuming version of JQMD
negs=2: High energy EGS mode (dmax(12-14) are automatically set to 1.0e8)
mdbatima=3000: More memory is required to store the stopping power tables
iMeVperU=1: Cosmic-ray energy is generally expressed in MeV/n instead of MeV
emin(12-13): Increase them when low-energy electrons are not important

--- SLIDE 07 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Source setting
set:c1[200.0]
  totfact =  pi*c1**2
infl:{source.inp}
     proj =  proton
Various ions exit in space, but only one projectile can be specified in one multi-source.
cosmicray.inp
source.inp
<source> = 1.0
   s-type =   9           # spherical (shell) source
       r1 =   c1           # radius of sphere [cm]
       r2 =   c1           # radius of source circle [cm]
      dir =  iso          # inner direction with uniform dis. by analog
   e-type =  25           # Cosmic-ray source
    icenv =   0           # 0>: Terrestiral GCR, D=0: Free-space GCR, <0:Free-space SEP
 solarmod =   0.0000      # Solar activity W-index
    rigid =   0.0000        # Cut-off rigidity in GV
Each multi-source is recommended to be defined in an include file except for “proj” parameter
Absolute value of cosmic-ray fluxes inside the source sphere is normalized to (/cm2/sec)* by setting totfact = πr2 and <source> = 1.0
*(/cm2/event) in the case of SEP
isotropic source distribution inside sphere with radius c1
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
Add 4He and 56Fe ions to the source particles
set:c1[200.0]
  totfact =  pi*c1**2
infl:{source.inp}
     proj =  proton
cosmicray.inp
set:c1[200.0]
  totfact =  pi*c1**2
infl:{source.inp}
     proj =  proton
infl:{source.inp}
     proj =  4He
infl:{source.inp}
     proj =  56Fe
track_reg.eps
Poor statistics for Fe ion because of too low flux
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
Generate equal numbers of particles for proton, 4He, and 56Fe ions
cosmicray.inp
set:c1[200.0]
  totfact =  -pi*c1**2
infl:{source.inp}
     proj =  proton

infl:{source.inp}
     proj =  4He

infl:{source.inp}
     proj =  56Fe
Negative “totfact” indicates that equal numbers of sources are sampled from each multi-source, and their intensities are adjusted by weight*
track_reg.eps
*see phits/lecture/advanced/variance-reduction in more detail
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
Change solar activity to the solar maximum
source.inp
<source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  25
    icenv =   0
 solarmod =   0.0000
    rigid =   0.0000
Solar activity (W-index) can be directly specified by “solarmod”,
or determined from date specified by “icyear”, “icmonth”, “icday”
<source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  25
    icenv =   0
 solarmod =   150.00
    rigid =   0.0000
W-index ~ Sun spot number
Solar activity & GCR flux are anti-corelated!
Solar minimum ~ 0
Solar maximum ~ 150
track_reg.eps
Save source.inp & run cosmicray.inp
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
Consider rigidity cut off by magnetosphere up to 10 GV
source.inp
Low rigidity* cosmic-ray cannot penetrate the magnetosphere
Cut-off rigidity can be specified by “rigid” in GV
<source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  25
    icenv =   0
 solarmod =   150.00
    rigid =   0.0000
Vertical cut-off rigidity
<source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  25
    icenv =   0
 solarmod =   150.00
    rigid =   10.0000
*Effect of magnetic field on the motion of charged particle
track_reg.eps
Polar region ~ 0 GV
Equator region ~ 16 GV
Save source.inp & run cosmicray.inp
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Reproduce cosmic-ray environment at the altitude of 12 km above New York
source.inp
Change icenv from 0 (in free space) to 1 (in the atmosphere)
Comment out rigid and add glat and glong for specifying the geographical latitude and longitude, respectively, in degree*
Add alti for specifying the altitude in km
icenv =   1
 solarmod =   150.00
 $ rigid =   10.0000
 glat = 41
 glong = -74
 alti = 12.0
*Positive value indicates north and east, respectively
track_reg.eps
Geographical coordinate of NY
North 41 deg, West 74 deg
Save source.inp & run cosmicray.inp
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
cross.eps
Check angular distribution
Cosmic-ray environment in the atmosphere is not isotropic!
← downward
upward →
Strong downward directivities are observed

--- SLIDE 14 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6
Change source to more abundant cosmic-rays in the atmosphere
Ion fluxes are very small in the atmosphere except for very high altitude
Change proj in [source] and part in tallies to secondary cosmic-rays (neutron, muon+, muon-, electron, positron, photon)
cosmicray.inp
set:c1[200.0]
  totfact = -pi*c1**2
infl:{source.inp}
     proj =  proton
infl:{source.inp}
     proj =  4He
infl:{source.inp}
     proj =  56Fe
set:c1[200.0]
  totfact = -pi*c1**2
infl:{source.inp}
     proj =  neutron
infl:{source.inp}
     proj =  muon+
infl:{source.inp}
     proj =  muon-
infl:{source.inp}
     proj =  electron
infl:{source.inp}
     proj =  positron
infl:{source.inp}
     proj =  photon
[t-track]
…
file = track_reg.out
part =  proton alpha fe
...

[t-cross]
...
file = cross.out
part =  proton alpha fe
[t-track]
…
file = track_reg.out
$ part =  proton alpha fe
part = neutron muon+ muon- electron positron photon
...

[t-cross]
...
file = cross.out
$ part =  proton alpha fe
part = neutron muon+ muon- electron positron photon
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Answer 6
Change source to more abundant cosmic-rays in the atmosphere
track_reg.eps
cross.eps
Secondary cosmic-ray fluxes are much higher particularly for low energies
Strong downward directivities are still observed except for neutrons

--- SLIDE 16 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Exercise 7
Reproduce cosmic-ray environment at the ground level of New York*
source.inp
Change icenv from 1 (in the atmosphere) to 2 (at the ground level)
Change alti to 0 km
icenv =   1
 solarmod =   150.00
 $ rigid =   10.0000
 glat = 41
 glong = -74
 alti = 12.0
Low-energy neutron fluxes depending water density in soil (environ)
Horizontal (θ > ~45) muon fluxes by introducing correction factor
Ground influences…
track_reg.eps
Save source.inp & run cosmicray.inp
*Generally adopted as the reference cosmic-ray flux for estimating soft-error rates
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Table of Contents
Cosmic-ray Source Mode in PHITS
Application to Cosmic-ray Dosimetry
Application to Muon Radiography
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 18 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Why is Cosmic-ray Dosimetry Necessary?
Astronaut doses are generally limited by their life-time dose equivalent (~600 mSv)
Aircrew doses are generally limited by their annual effective dose (~5 mSv/year)
The worst-case scenario must be considered in the case of huge solar particle event
Effective dose (Sv) = ∫ Particle flux (/MeV/cm2) x Dose conversion coefficient (Sv.cm2) dE
This integration can be done in PHITS using [t-track] with multiplier subsection*
Multiplier ID= -211 (effective dose equivalent for male) and -203 (effective dose for ISO irradiation) are recommended for astronaut and aircrew dosimetry, respectively
How to calculate the effective dose (equivalent) using PHITS?
*See manual 5.24 [multiplier] or phits/lecture/advanced/options
Typical cosmic-ray dose ranges

--- SLIDE 19 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Exercise 8
Calculate astronaut dose in free space
Change proj to proton (other ions are ignored for simplicity)
Change icenv back to 0 (in free space) and comment out glat, glong & alti
Activate the last [t-track] with “file = track_dose.out”
cosmicray.inp
[t-track] off
…
multiplier = all
mat   mset1
all  (1.0e-6*3600*24  -211 )
y-txt = Dose equivalent [uSv/day]
Scaling factor
(convert pSv/sec to uSv/day)
track_dose.out
y: Dose equivalent [uSv/day]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n
#  num    reg     volume     all         r.err
    1       1   4.1888E+06   1.1447E+02  0.0062
    2       3   2.7935E+07   1.1442E+02  0.0013
Doses inside inner & outer spheres are the same
～114 uSv/day (Note: proton dose only)
muptilier ID
MENTIONED_INPUT_NAMES: cosmicray.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
y: Dose equivalent [uSv/day]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n   y(proton  ),d4r  n   y(neutron ),u5b  n
#  num    reg     volume                 all      r.err           proton      r.err         neutron     r.err
    1       1   4.1888E+06   2.2518E+02  0.0763   1.1499E+02  0.0658   6.9111E+01  0.1061
    2       3   2.7935E+07   1.3729E+02  0.0250   1.1167E+02  0.0147   1.5697E+01  0.0958
Exercise 9
Calculate astronaut dose inside spacecraft
Change material of cell 2 to Aluminum (mat[1]) with density of 2.7 g/cm3
Change maxcas from 100000 to 1000 for reducing computational time
track_dose.out
Total doses become higher particularly inside spacecraft due to neutron production
track_xy.eps
Many secondary particles are generated in the spacecraft wall
ANSWER_FILE: (missing)

--- SLIDE 21 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
Exercise 10
Change the source to SEP
Five historically large SPE can be selected
Change icenv in source.inp to -1 (SEP in free space)*
Increase maxcas to 100000 (Computational time per history is much lower)
Change the scaling factor in the multiplier subsection to 1.0e-12
Change y-txt to “Dose equivalent [Sv/event]”**
environ = 1: Feb 1956 (default, hardest event)
             = 2: Nov. 1960
             = 3: Aug. 1972
             = 4: Sum of Oct. 1989
             = 5: Jan. 2005
** Tally results are normalized to (/sec) in the GCR mode, while (/event) in the SEP mode
source.inp
icenv =   0
 ...
cosmicray.inp
[t-track]
…
multiplier = all
mat   mset1
all  (1.0e-6*3600*24  -211 )
y-txt = Dose equivalent [uSv/day]
*How to select solar particle event (SPE)
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 22 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Answer 10
track_dose.out
y: Dose equivalent [Sv/event]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n   y(proton  ),d4r  n   y(neutron ),u5b  n
#  num   reg     volume                all      r.err           proton      r.err        neutron      r.err
    1       1   4.1888E+06   1.1851E-01  0.0404   9.0267E-02  0.0470   2.6473E-02  0.0608
    2       3   2.7935E+07   6.2884E-01  0.0056   6.2361E-01  0.0056   4.9237E-03  0.0531
The dose inside spacecraft is approximately 1/6 of the outside dose
10 cm Aluminum is an effective shielding for solar particle events!
track_xy.eps

--- SLIDE 23 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Table of Contents
Cosmic-ray Source Mode in PHITS
Application to Cosmic-ray Dosimetry
Application to Muon Radiography
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 24 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Introduction of Muon Radiography
Applications
An imaging technique that uses cosmic-ray muons as the probe of radiography
What is it?
How to do it?
To reconstruct the 2D/3D image of an object based on the measured muon fluxes from different directions
Scanning ancient structures such as pyramids to detect hidden chambers
Monitoring volcano activity by identifying magma chambers
Detecting nuclear materials after nuclear accidents or for homeland security
and more…

--- SLIDE 25 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Disk source area
muon.inp
Basic setup
Muon at ground level (written in muon-source.inp except for proj)
A disk-shape source with 5 m radius (s-type = 1 & dir = cr)*
Cylindrical air and soil with thicknesses of 1 and 5 m, respectively
Reflection boundary is used to reproduce the infinite air and soil
[t-track] for visualizing particle trajectories (track_xz.out)
[t-cross] for visualizing the particle distributions at the ground surface and 5 m depth underground (detector position)
Source：

Geometry：

Tally：
track_xz.eps
cross_xy.eps
ground surface
(page 1)
5 m underground
(page 2)
reflection boundary
*The range of the source-generation angles can be restricted by ag1 and ag2 parameters
MENTIONED_INPUT_NAMES: muon-source.inp, muon.inp

--- SLIDE 26 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Reflection Boundary
When the surface number is defined with * (e.g., *1 cz 1.0), it becomes a reflection boundary, which acts like a perfect mirror of radiation
It is useful when the source area is much larger than the tally region(s)
without reflection surface
Tally
with reflection surface
Tally
soil
air
water
Source area should be large so that Radiations rarely hit the tally region
Source area can be restricted so that Radiations frequently hit the tally region
However, the geometry becomes repeated structures
To use refection boundary, the repeated objects inside the boundary (water in this case) should not influence the tally results very much
reflection boundary
Source area
Source area

--- SLIDE 27 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
Exercise 10
Make a spherical air chamber in the soil
Change material of cell 3 from soil (m1) to air (m2) with density of 1.21e-3 g/cm3
Run PHITS and check track_xz.eps and cross-xy.eps
[ Cell ]
  1  1  -2.7      -21 1 -2 11 $ soil
  2  2  -1.21e-3  -21 2 -3    $ air
  3  1  -2.7      -11         $ object
 99  -1 -99  #all
 ...
What happens in the muon distributions at the detectors if there is a hidden air chamber in the soil?
Detectors are here
muon.inp
MENTIONED_INPUT_NAMES: muon.inp
ANSWER_FILE: input/exercise10/muon.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Answer 10
track_xz.eps
cross_xy.eps
ground surface
(page 1)
5 m underground
(page 2)
More muons reach here
[ Cell ]
  1  1  -2.7      -21 1 -2 11 $ soil
  2  2  -1.21e-3  -21 2 -3    $ air
  3  2  -1.21e-3  -11         $ object
 99  -1 -99  #all
 ...
muon.inp
MENTIONED_INPUT_NAMES: muon.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
Exercise 11
Make a spherical gold in the soil
If you are extremely lucky that there is a huge spherical gold above the detector, what happens in the detector response?
Change the material of cell 3 to gold (m3) with the density of 19.32 g/cm3
[ Cell ]
  1  1  -2.7      -21 1 -2 11 $ soil
  2  2  -1.21e-3  -21 2 -3    $ air
  3  2  -1.21e-3  -11         $ object
 99  -1 -99  #all
 ...
Note: computational time becomes longer when transporting muons in heavy elements
muon.inp
MENTIONED_INPUT_NAMES: muon.inp
ANSWER_FILE: input/exercise10/muon.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Answer 11
track_xz.eps
cross_xy.eps
ground surface
(page 1)
5 m underground
(page 2)
Less muons reach here
[ Cell ]
  1  1  -2.7      -21 1 -2 11 $ soil
  2  2  -1.21e-3  -21 2 -3    $ air
  3  3  -19.32    -11         $ object
 99  -1 -99  #all
 ...
muon.inp
MENTIONED_INPUT_NAMES: muon.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Table of Contents
Cosmic-ray Source Mode in PHITS
Application to Cosmic-ray Dosimetry
Application to Muon Radiography
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 32 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Summary
PHITS can reproduce the cosmic-ray environments in free space for GCR and SEP, in low-earth orbits for GCR and TP, and in the atmosphere for GCR including their secondaries
Complicated altitude, geographical, and angular dependences of the GCR fluxes in the atmosphere can be considered using the PARMA model
The absolute values of the tally results are normalized to (/sec) for the GCR and TP modes, while (/event) for the SEP mode
Astronaut and aircrew doses can be directly calculated from [t-track] coupled with special dose conversion coefficients
Reflection boundary is useful to reproduce terrestrial cosmic-ray exposure scenarios (large source area with small tally region)
Please see phits/sample/source/Cosmicray for more samples

--- SLIDE 33 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
Appendix (Selection of sample input)
Does geometry include ground?
Does geometry include any big object preventing from the use of reflection boundary
(see page 26)?
Spherical source
GCR in the ideal atmosphere (GCR-atmosphere)
GCR at ground level (GCR-ground_level)
GCR in Low Earth Orbit (GCR-LEO)
GCR in free space (GCR-space)
SEP in free space (SEP-space)
Trapped proton in Low Earth Orbit (TR-LEO)
Plane source with reflection boundary
GCR from the top of the atmosphere (GCR-TOA)
GCR on lunar surface (GCR-moon)
GCR on ground (GCR-ground)
SEP on lunar surface (SEP-moon)
Hemispherical source + dump-source simulation
GCR on lunar surface (GCR-moon)
GCR on ground (GCR-ground)
SEP on lunar surface (SEP-moon)
No
No
Yes
Yes
See phits/sample/source/Cosmicray

--- SLIDE 01 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
PHITSを用いた宇宙線挙動解析
2025年1月改訂
phits/lecture/advanced/cosmicray

--- SLIDE 02 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
本実習の流れ
PHITSの宇宙線線源モード
宇宙線被ばく線量評価への応用
ミューオンラジオグラフィへの応用
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 03 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
宇宙放射線環境
https://phits.jaea.go.jp/expacs
銀河宇宙線(Galactic Cosmic-Ray: GCR)
存在場所: 全ての環境（宇宙空間、大気圏内）
時間変動: 約11年の太陽周期に従って緩やかに変動
スペクトル: 数GeV以上の高エネルギーが中心（最大1020 eV）
太陽高エネルギー粒子(Solar Energetic Particle: SEP)
存在場所: 宇宙空間。稀に地表面まで届く
時間変動: 巨大な太陽フレア時に突発的に飛来
スペクトル: 太陽フレアに依存。通常は最大でも数100MeVまでだが、稀にGeV級のイベントも発生する
捕捉粒子(Trapped Particle: TP)
存在場所: 地磁気圏内のみ
時間変動: 約11年の太陽周期に従って緩やかに変動
スペクトル: 最大で数100MeV

--- SLIDE 04 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
PHITSの宇宙線線源モード
https://phits.jaea.go.jp/expacs
宇宙空間＆地球低軌道（LEO）: DLR model [1]
大気圏内: PARMA/EXPACS [2]
宇宙空間: Tylka’s model [3]
大気圏内＆地球低軌道（LEO）: 未対応
地球低軌道（LEO）: AP8 (陽子のみ) [4]
宇宙空間及び大気圏内: 存在しない
高度・緯度・経度・角度依存性を精密に考慮可能
[1] D. Matthia et al. Adv Space Res 51: 329-338 (2013)
[2] T. Sato PLOS ONE 11(8): e0160390 (2016)
[3] A.J. Tylka et al. 31th ICRC, Poland (2009)
[4] D. Sawyer & J. Vette, NSSDC Report 76-06 (1976)
銀河宇宙線(Galactic Cosmic-Ray: GCR)
太陽高エネルギー粒子(Solar Energetic Particle: SEP)
捕捉粒子(Trapped Particle: TP)

--- SLIDE 05 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
cosmicray.inp
基本設定
宇宙空間における銀河宇宙線の陽子（半径 200 cmの等方照射）
線源条件はprojパラメータを除いて別ファイル（source.inp）に記載
同心円（半径100, 110, & 200 cm）
[t-track]（飛跡描画用、track_xz.out）
[t-track] （エネルギースペクトル評価用、track_reg.out）
[t-cross] （z=0cmにおける角度分布評価用、cross.out）
線源：

体系：
タリー：
*図を90°回転（方法はFAQ 3.8を参照）
track_xz.eps*
[t-cross]計算面
track_reg.eps
cross.eps
← 下方向
上方向 →
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp

--- SLIDE 06 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
宇宙線挙動解析奨励設定
[ P a r a m e t e r s ]
 icntl    =           0     # (D=0) 3:ECH 5:NOR 6:SRC 7,8:GSH 11:DSH 12:DUMP
 maxcas   =        1000     # (D=10) number of particles per one batch
 maxbch   =          10     # (D=10) number of batches
 e-mode   =           2     # (D=0) 0: Normal, 1: Event generator mode Ver.1, 2: Ver.2
 irqmd    =           1     # (D=0) 0: JQMD legacy version, 1: JQMD-2.0
 negs     =           2     # (D=-1) =-1:original, =0:No, =1:EGS
 mdbatima =        3000     # (D=500) max database size of ATIMA
 maxbnk   =      100000     # (D=10000) maximum bank memory length
 iMeVperU =           1     # (D=0) 0:[MeV] or 1:[MeV/u] is unit of tally output
 emin(12) =  1.00000000     # (D=1.e+9) cut-off energy of electron (MeV)
 emin(13) =  1.00000000     # (D=1.e+9) cut-off energy of positron (MeV)
 emin(14) =  1.00000000     # (D=1.0e-3) cut-off energy of photon (MeV)
irqmd=1:計算時間は掛かるがより精度のよい重イオン核反応モデルJQMD2.0を使用
negs=2: 高エネルギーEGSモード（dmax(12-14)が自動的に1.0e8に設定される）
mdbatima=3000: 阻止能テーブルを保存するためのメモリサイズ拡張
iMeVperU=1: 宇宙線エネルギーは通常MeV/nで表現されるため
emin(12-13): 低エネルギー電子輸送が重要でなければ高くして計算時間を削減

--- SLIDE 07 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
宇宙線線源設定
set:c1[200.0]
  totfact =  pi*c1**2
infl:{source.inp}
     proj =  proton
宇宙線には様々な粒子種が含まれるが、１つのマルチソースで再現できるのは１種類のみ
cosmicray.inp
source.inp
<source> = 1.0
   s-type =   9           # spherical (shell) source
       r1 =   c1           # radius of sphere [cm]
       r2 =   c1           # radius of source circle [cm]
      dir =  iso          # inner direction with uniform dis. by analog
   e-type =  25           # Cosmic-ray source
    icenv =   0           # 0>: Terrestiral GCR, D=0: Free-space GCR, <0:Free-space SEP
 solarmod =   0.0000      # Solar activity W-index
    rigid =   0.0000        # Cut-off rigidity in GV
粒子種（proj）を除く線源条件（範囲、太陽活動など）は別ファイルで設定し、それをinflコマンドで組込むと便利
宇宙線線源の場合、 totfact = πr2 かつ <source> = 1.0とすると、タリー結果の絶対値が(/cm2/sec)* となるように自動的に規格化される
*SEPの場合は(/cm2/event)に規格化される
半径c1の球内を等方照射
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１
4He及び56Feイオンを線源に加えよう
set:c1[200.0]
  totfact =  pi*c1**2
infl:{source.inp}
     proj =  proton
cosmicray.inp
set:c1[200.0]
  totfact =  pi*c1**2
infl:{source.inp}
     proj =  proton
infl:{source.inp}
     proj =  4He
infl:{source.inp}
     proj =  56Fe
track_reg.eps
Feイオンは数が少ないので統計が悪い
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題２
各イオン種に対して同等の数の線源を発生させよう
cosmicray.inp
set:c1[200.0]
  totfact =  -pi*c1**2
infl:{source.inp}
     proj =  proton

infl:{source.inp}
     proj =  4He

infl:{source.inp}
     proj =  56Fe
totfactを負値で設定すると、各マルチソースから均一に線源をサンプリングし、
ウェイト値を変化させてその強度の違いを表現するウェイト調整法*が採用される
track_reg.eps
*ウェイト調整法の詳細はphits/lecture/advanced/variance-reduction参照
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題３
太陽活動極大期の宇宙線環境を再現しよう
source.inp
<source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  25
    icenv =   0
 solarmod =   0.0000
宇宙線環境の時間変動は、太陽活動度（W-index）をsolarmodパラメータで直接指定するか、 再現したい日付をicyear、icmonth、icdayで指定する
<source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  25
    icenv =   0
 solarmod =   150.00
source.inpを保存してからcosmicray.inpを実行
W-index ~ 黒点数
太陽活動と銀河宇宙線フラックスは逆相関！
太陽活動極小期 ~ 0
太陽活動極大期 ~ 150
track_reg.eps
MENTIONED_INPUT_NAMES: source.inp
ANSWER_FILE: input/allGCR/source.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題４
地磁気によるカットオフ・リジディティ(rigidity cut-off)を考慮しよう
source.inp
低リジディティの宇宙線は、地磁気により曲げられLEOや大気圏に侵入できない
Cut-off rigidity（GV単位でrigidにより定義）を10GVに設定してPHITSを実行
<source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  25
    icenv =   0
 solarmod =   150.00
    rigid =   0.0000
Vertical cut-off rigidity
<source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  25
    icenv =   0
 solarmod =   150.00
    rigid =   10.0000
*磁場によって荷電粒子がどれくらい曲がりにくいかを表した指標
track_reg.eps
極域 ~ 0 GV（地磁気影響なし）
赤道付近 ~ 16 GV（地磁気影響大）
Save source.inp & run cosmicray.inp
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題５
大気圏内（ニューヨーク上空・高度12km）の宇宙線環境を再現しよう
source.inp
icenvを0（宇宙空間モード）から1（大気圏内モード）に変更
rigidをコメントアウトしてglatとglong を追加してそれぞれ緯度・経度を指定*
altiを追加して高度をkm単位で定義
icenv =   1
 solarmod =   150.00
 $ rigid =   10.0000
 glat = 41
 glong = -74
 alti = 12.0
*正値が北緯及び東経をそれぞれ表す
track_reg.eps
ニューヨークの緯度・経度は
北緯41度、西経74度
Save source.inp & run cosmicray.inp
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 13 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
cross.eps
天頂角分布も確認
大気圏内の宇宙線天頂角分布は等方的ではない！
← 下方向（地面）
上方向（上空） →
下方向（上空から地面）に進む宇宙線が支配的

--- SLIDE 14 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題６
大気圏内で支配的となる２次宇宙線を発生させよう
大気圏内では、大気と銀河宇宙線との反応で生成した2次宇宙線が支配的
[source]のprojとタリーのpartを2次宇宙線 (neutron, muon+, muon-, electron, positron, photon)に変更してPHITSを実行
cosmicray.inp
set:c1[200.0]
  totfact = -pi*c1**2
infl:{source.inp}
     proj =  proton
infl:{source.inp}
     proj =  4He
infl:{source.inp}
     proj =  56Fe
set:c1[200.0]
  totfact = -pi*c1**2
infl:{source.inp}
     proj =  neutron
infl:{source.inp}
     proj =  muon+
infl:{source.inp}
     proj =  muon-
infl:{source.inp}
     proj =  electron
infl:{source.inp}
     proj =  positron
infl:{source.inp}
     proj =  photon
[t-track]
…
file = track_reg.out
part =  proton alpha fe
...

[t-cross]
...
file = cross.out
part =  proton alpha fe
[t-track]
…
file = track_reg.out
$ part =  proton alpha fe
part = neutron muon+ muon- electron positron photon
...

[t-cross]
...
file = cross.out
$ part =  proton alpha fe
part = neutron muon+ muon- electron positron photon
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
解答６
track_reg.eps
cross.eps
大気圏内では中性子や光子など2次粒子が支配的
基本的には下方性であるが中性子は比較的等方な角度分布を持つ
大気圏内で支配的となる２次宇宙線を発生させよう

--- SLIDE 16 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
課題７
ニューヨーク地表面における宇宙線環境*を再現しよう
source.inp
icenvを1（理想大気中）から2（地表面モード）に変更
altiを0 kmに変更
icenv =   1
 solarmod =   150.00
 $ rigid =   10.0000
 glat = 41
 glong = -74
 alti = 12.0
低エネルギー中性子フラックスが地中水分濃度(environ)により変化する
水平方向（θ > 45度以上）のミューオンフラックスに補正係数が導入される
地表面モードの特徴…
track_reg.eps
Save source.inp & run cosmicray.inp
*半導体ソフトエラー発生率推定の際、基準宇宙線環境として採用されている
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
本実習の流れ
PHITSの宇宙線線源モード
宇宙線被ばく線量評価への応用
ミューオンラジオグラフィへの応用
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 18 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
宇宙線被ばく線量評価の必要性
宇宙飛行士の被ばく線量は、生涯実効線量当量で規制される場合が多い (~600 mSv)
航空機乗務員の被ばく線量は、年間被ばく線量で規制される場合が多い (~6 mSv/year)
巨大な太陽フレアが発生した場合に備え、最悪ケースに対して事前評価が重要となる
実効線量（当量） (Sv) = ∫ 粒子フラックス (/MeV/cm2) x 線量換算係数 (Sv.cm2) dE
上記積分は、 [t-track]のmultiplier機能*を使うことによりPHITSで直接実行可能
宇宙飛行士に対してはMultiplier ID= -211 (成人男性に対する実効線量当量）、航空機搭乗者に対してはID = -203 (等方照射に対する実効線量）を利用することを奨励
PHITSを用いた宇宙線被ばく線量の計算方法
*マニュアル5.24 [multiplier]もしくはphits/lecture/advanced/options参照
典型的な宇宙線被ばく線量

--- SLIDE 19 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
課題８
宇宙空間における宇宙飛行士の被ばく線量を評価しよう
projをprotonに変更（簡略化するため他のイオンは無視）
icenvを0（宇宙空間モード）に戻す
glat, glong & altiは削除かコメントアウト
最後の[t-track]（file = track_dose.out）を有効化してPHITSを実行
cosmicray.inp
[t-track] off
…
multiplier = all
mat   mset1
all  (1.0e-6*3600*24  -211 )
y-txt = Dose equivalent [uSv/day]
pSv/secからuSv/dayに変換する係数
track_dose.out
y: Dose equivalent [uSv/day]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n
#  num    reg     volume     all         r.err
    1       1   4.1888E+06   1.1447E+02  0.0062
    2       3   2.7935E+07   1.1442E+02  0.0013
球の内側と外側で線量は同じ
約114 uSv/day（陽子線量のみであることに注意）
muptilier ID
MENTIONED_INPUT_NAMES: cosmicray.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
y: Dose equivalent [uSv/day]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n   y(proton  ),d4r  n   y(neutron ),u5b  n
#  num    reg     volume                 all      r.err           proton      r.err         neutron     r.err
    1       1   4.1888E+06   2.2518E+02  0.0763   1.1499E+02  0.0658   6.9111E+01  0.1061
    2       3   2.7935E+07   1.3729E+02  0.0250   1.1167E+02  0.0147   1.5697E+01  0.0958
課題９
宇宙機内の宇宙飛行士被ばく線量を評価しよう
cell 2の物質をアルミ（mat[1]、密度2.7 g/cm3）に変更
計算時間短縮のため、maxcasを100000から1000に変更
track_dose.out
全被ばく線量は、中性子の影響により宇宙機内の方がむしろ高い
track_xy.eps
多くの2次粒子が船壁で生成される
ANSWER_FILE: (missing)

--- SLIDE 21 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
課題１０
太陽高エネルギー粒子（SEP）被ばくの場合は？
５つの歴史的巨大イベントを選択可能
source.inpに書かれたicenvを-1 (宇宙空間のSEPモード)*に変更
maxcasを100000にする（SEPはエネルギーが低いので計算時間が短い）
multiplierサブセクションに書かれた規格化定数を1.0e-12に変更
y-txtをDose equivalent [Sv/event]に変更**
**SEPモードの場合、タリー結果は(/event)に規格化されるので注意
（銀河宇宙線モードのときは(/sec)）
source.inp
icenv =   0
 ...
cosmicray.inp
[t-track]
…
multiplier = all
mat   mset1
all  (1.0e-6*3600*24  -211 )
y-txt = Dose equivalent [uSv/day]
*太陽フレアイベントの選択方法
environ = 1: Feb 1956 (default, hardest event)
             = 2: Nov. 1960
             = 3: Aug. 1972
             = 4: Sum of Oct. 1989
             = 5: Jan. 2005
MENTIONED_INPUT_NAMES: cosmicray.inp, source.inp
ANSWER_FILE: input/exercise01/CosmicRay.inp

--- SLIDE 22 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
解答１０
track_dose.out
y: Dose equivalent [Sv/event]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n   y(proton  ),d4r  n   y(neutron ),u5b  n
#  num   reg     volume                all      r.err           proton      r.err        neutron      r.err
    1       1   4.1888E+06   1.1851E-01  0.0404   9.0267E-02  0.0470   2.6473E-02  0.0608
    2       3   2.7935E+07   6.2884E-01  0.0056   6.2361E-01  0.0056   4.9237E-03  0.0531
宇宙空間の線量と比べて宇宙機内の線量は約1/6
たった10cmのアルミ壁でもSEPに対しては十分な遮へい効果を有する
track_xy.eps

--- SLIDE 23 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
本実習の流れ
PHITSの宇宙線線源モード
宇宙線被ばく線量評価への応用
ミューオンラジオグラフィへの応用
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 24 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
ミューオンラジオグラフィの概要
応用例
ラジオグラフィのプローブとして宇宙線ミューオンを使ったイメージング技術
ミューオンラジオグラフィとは？
原理
様々な方向から飛来するミューオンフラックスを測定し、その強度変化から2Dもしくは3Dの画像を再構築する
ピラミッドなどの遺跡をスキャンし、隠し部屋など中の構造を調査する
活火山をモニタし、マグマだまりの状態を確認する
核セキュリティや廃炉計画の目的で核物質の場所を検知する
  他多数…

--- SLIDE 25 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
muon.inp
基本設定
地表面ミューオン線源（icenv = 2、詳細はmuon-source.inp）
半径5mの円盤状線源（s-type = 1 & dir = cr）*
円柱状の空気（高さ1mまで）と土壌（深さ5mまで）
円柱側面は反射境界を使って無限に広がる空間を再現
[t-track]（飛跡描画用、track_xz.out）
[t-cross]（位置検出型検出器の応答を模擬した地表面及び地下5mにおけるミューオンフラックスの空間分布、cross_xy.eps）
線源：

体系：

タリー：
track_xz.eps
cross_xy.eps
ground surface
(page 1)
5 m underground
(page 2)
反射境界
線源発生円盤
*ag1, ag2で発生する線源の角度範囲を指定。今回は0（水平）～-90度（鉛直下方向）
MENTIONED_INPUT_NAMES: muon-source.inp, muon.inp

--- SLIDE 26 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
反射境界
面番号の前に*を付けた場合（例 *1 cz 1.0）、その面が反射境界となり全ての放射線を鏡のように反射するようになる
反射境界は、線源領域がタリー領域と比べて極めて大きい場合に有効となる
反射境界無し
タリー領域
反射境界あり
タリー領域
土壌
空気
水
線源領域を広く設定する必要があり、放射線がタリー領域に入るのは稀
線源領域を狭く設定することができるため、放射線が高頻度でタリー領域に入る
ただし、体系が繰り返し体系と同義になる
反射境界内にある物体（この場合は水）が繰り返されてもタリー結果に変動がほとんどないことが反射境界を使える条件
反射境界
線源領域
線源領域

--- SLIDE 27 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
課題１０
土壌の中に球状の空気部屋を作ろう
領域3の物質を土壌（m1）から空気（m2、密度1.21e-3 g/cm3）に変更
PHITSを実行し、track_xz.epsとcross-xy.epsを確認
muon.inp
[ Cell ]
  1  1  -2.7      -21 1 -2 11 $ soil
  2  2  -1.21e-3  -21 2 -3    $ air
  3  1  -2.7      -11         $ object
 99  -1 -99  #all
 ...
もし地下に巨大な空気の部屋があったら、地下のミューオン分布にどのような変化が起きるのだろうか？
検出器位置
MENTIONED_INPUT_NAMES: muon.inp
ANSWER_FILE: input/exercise10/muon.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
解答１０
track_xz.eps
cross_xy.eps
ground surface
(page 1)
5 m underground
(page 2)
空気の真下のミューオン強度が少し上がる
[ Cell ]
  1  1  -2.7      -21 1 -2 11 $ soil
  2  2  -1.21e-3  -21 2 -3    $ air
  3  2  -1.21e-3  -11         $ object
 99  -1 -99  #all
 ...
muon.inp
MENTIONED_INPUT_NAMES: muon.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
課題１１
もし土壌中に巨大な金塊があったら？
ミューオンを重い元素の中で走らせると計算時間が掛かるので注意
（ヒストリー数を減らしてもよい）
[ Cell ]
  1  1  -2.7      -21 1 -2 11 $ soil
  2  2  -1.21e-3  -21 2 -3    $ air
  3  2  -1.21e-3  -11         $ object
 99  -1 -99  #all
 ...
領域3の物質を空気（m2）から金（m3、密度19.32 g/cm3）に変更
PHITSを実行し、track_xz.epsとcross-xy.epsを確認
muon.inp
MENTIONED_INPUT_NAMES: muon.inp
ANSWER_FILE: input/exercise10/muon.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
解答１１
track_xz.eps
cross_xy.eps
ground surface
(page 1)
5 m underground
(page 2)
[ Cell ]
  1  1  -2.7      -21 1 -2 11 $ soil
  2  2  -1.21e-3  -21 2 -3    $ air
  3  3  -19.32    -11         $ object
 99  -1 -99  #all
 ...
金塊の真下のミューオン強度が下がる
muon.inp
MENTIONED_INPUT_NAMES: muon.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
本実習の流れ
PHITSの宇宙線線源モード
宇宙線被ばく線量評価への応用
ミューオンラジオグラフィへの応用
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 32 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
まとめ
PHITSは、宇宙空間におけるGCRとSEP、地球低軌道におけるGCRとTP、大気圏内におけるGCR及びその２次粒子環境を再現できる
大気圏内においては、宇宙線フラックスの複雑な高度・緯度・経度・角度分布をPARMAモデルを使うことにより考慮している
宇宙線線源モードを使えば、タリー結果の絶対値が自動的に(/sec)に規格化される（ただし、SEPモードの場合は（/event））
宇宙飛行士や航空機搭乗者の被ばく線量は、 [t-track]に専用の線量換算係数を組み合わせることにより直接評価することができる
反射境界を使えば、地上や地下における宇宙線挙動解析など、広い線源かつ小さなタリー領域の計算を効果的に行うことができる
様々な宇宙線環境に対するサンプル入力ファイルがphits/sample/source/Cosmicray に格納されている

--- SLIDE 33 ---
PPTX_FILE: phits-lec-cosmicray-en.pptx
SLIDE_TEXT:
参考資料 (サンプル入力ファイルの選択方法）
ジオメトリに地面（月面含む）は定義する必要があるか？
ジオメトリに反射境界の利用を妨げるような大きな物質は含まれているか（ｐ２６参照）？
球面（Sphere）線源
GCR in the ideal atmosphere (GCR-atmosphere)
GCR at ground level (GCR-ground_level)
GCR in Low Earth Orbit (GCR-LEO)
GCR in free space (GCR-space)
SEP in free space (SEP-space)
Trapped proton in Low Earth Orbit (TR-LEO)
平面（Plane）線源＋反射境界
GCR from the top of the atmosphere (GCR-TOA)
GCR on lunar surface (GCR-moon)
GCR on ground (GCR-ground)
SEP on lunar surface (SEP-moon)
半球面（Hemisphere）線源 + dump線源計算
GCR on lunar surface (GCR-moon)
GCR on ground (GCR-ground)
SEP on lunar surface (SEP-moon)
No
No
Yes
Yes
サンプル入力ファイルの格納フォルダ phits/sample/source/Cosmicray

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/allGCR/CosmicRay-allGCR.inp
FILE: input/exercise01/source.inp
FILE: input/exercise02/CosmicRay.inp
FILE: input/exercise02/source.inp
FILE: input/exercise03/CosmicRay.inp
FILE: input/exercise03/source.inp
FILE: input/exercise04/CosmicRay.inp
FILE: input/exercise04/source.inp
FILE: input/exercise05/CosmicRay.inp
FILE: input/exercise05/source.inp
FILE: input/exercise06/CosmicRay.inp
FILE: input/exercise06/source.inp
FILE: input/exercise07/CosmicRay.inp
FILE: input/exercise07/source.inp
FILE: input/exercise08/CosmicRay.inp
FILE: input/exercise08/source.inp
FILE: input/exercise09/CosmicRay.inp
FILE: input/exercise09/source.inp
FILE: input/exercise10/muon-source.inp
FILE: input/exercise11-end/muon-source.inp
FILE: input/exercise11-end/muon.inp
FILE: input/exercise11/muon-source.inp
FILE: input/exercise11/muon.inp

[BONUS_TEXT_FILES]
NOTE: None
