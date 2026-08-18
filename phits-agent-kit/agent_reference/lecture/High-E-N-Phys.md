# Lecture: advanced/High-E-N-Phys

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/High-E-N-Phys
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: High-E-N-Phys
LECTURE_PATH_INDEX: lecture/advanced/High-E-N-Phys
PPTX_FILES: phits-lec-HENP-en.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: homework, NuclearReaction
SECTION_KEYWORDS: 1, 3, 27, 30, 50, 5000, delta-ray, fragdata, t-dpa, t-product, t-track, t-yield

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/High-E-N-Phys
LECTURE_PATH_INDEX: lecture/advanced/High-E-N-Phys
PPTX_FILES: phits-lec-HENP-en.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 2
SLIDE_COUNT: 62
EXERCISE_SLIDE_COUNT: 20
BONUS_INPUT_COUNT: 19
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- homework.inp
- NuclearReaction.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: EXERCISE 18 | High energy nuclear physics in PHITS
  ANSWER_FILE: input/NuclearReaction-19.inp
- SLIDE 02: Particle categories
- SLIDE 03: Reaction physics parameters
- SLIDE 04: Reaction physics parameters
- SLIDE 05: Goal of this lecture
- SLIDE 06: NuclearReaction.inp
- SLIDE 07: Outline
- SLIDE 08: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 09: Answer 1
- SLIDE 10: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 11: Answer 2
- SLIDE 12: Total cross section model
- SLIDE 13: EXERCISE 3 | Exercise 3
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 14: Answer 3
- SLIDE 15: EXERCISE 4 | Exercise 4
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 16: Answer 4
- SLIDE 17: Answer 4’
- SLIDE 18: EXERCISE 5 | Exercise 5
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 19: Answer 5
- SLIDE 20: EXERCISE 6 | Exercise 6
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 21: Answer 6
- SLIDE 22: Does JENDL-5 cover all elements?
- SLIDE 23: JENDL-5 is advantageous
- SLIDE 24: Outline
- SLIDE 25: EXERCISE 7 | Exercise 7
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 26: Answer 7
- SLIDE 27: Deuteron total reaction cross sections
- SLIDE 28: EXERCISE 8 | Exercise 8
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 29: Answer 8
- SLIDE 30: EXERCISE 9 | Exercise 9
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 31: X-section with e-mode for any particles but low-E neutrons
- SLIDE 32: EXERCISE 10 | Exercise 10
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 33: Answer 10
- SLIDE 34: Answer 10’
- SLIDE 35: Outline
- SLIDE 36: EXERCISE 11 | Exercise 11
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 37: Answer 11
- SLIDE 38: EXERCISE 12 | Exercise 12
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 39: Answer 12
- SLIDE 40: Calculation procedure of JQMD
- SLIDE 41: EXERCISE 13 | Exercise 13
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 42: Answer 13
- SLIDE 43: Answer 13
- SLIDE 44: Algorithm of SMM
- SLIDE 45: EXERCISE 14 | Exercise 14
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 46: Answer 14
- SLIDE 47: EXERCISE 15 | Exercise 15
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 48: Answer 15
- SLIDE 49: EXERCISE 16 | Exercise 16
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 50: Answer 16
- SLIDE 51: Outline
- SLIDE 52: EXERCISE 17 | Exercise 17
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 53: Answer 17
- SLIDE 54: Answer 17
- SLIDE 55: EXERCISE 18 | Exercise 18
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 56: Answer 18
- SLIDE 57: EXERCISE 19 | Exercise 19
  ANSWER_FILE: input/NuclearReaction.inp
- SLIDE 58: Answer 19
- SLIDE 59: Summary
- SLIDE 60: Outline
- SLIDE 61: Homework
- SLIDE 62: Answer sample

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: homework.inp
FILE: NuclearReaction.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 18
SLIDE_TEXT:
High energy nuclear physics in PHITS
title
Aug. 2024 revised
phits/lecture/advanced/High-E-N-Phys
SPEAKER_NOTES:
To be included in future

Low E mu- absorption
Photonuclear by JENDL (inserted as Exercise 18)
Neutrino reactions
Fission
Use cross section data and Dchain by ndata = 3
	(calculate activity using JENDL)
ANSWER_FILE: input/NuclearReaction-19.inp

--- SLIDE 02 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Particle categories
Proton, Neutron,
Pion0,∓
K±, 0-short,0-long
Λ0, Σ ±, Σ0, Ξ0, Ξ-, Ω-,,,
d(H-2), t(H-3), He-3, α (He-4)
Ions heavier than A > 4
emin(1-2)
emin(3-5)
emin(8-10)
emin(11)
Transport threshold
emin(15-18)
emin(19)

--- SLIDE 03 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Reaction physics parameters
Relevant parameters (& sections)
dmax
ngem
igamma
ismm
ndedx
mdbatima
icxsni
icxspi
[fragdata]
[Delta-ray]
[ Repeated Collisions ]
inclg
icrdm
icrhi
iMeVperU
irqmd
eqmdmin
Numerous parameters are inherited from upper-class particles
To study ion physics parameters, begin with hadron physics!

--- SLIDE 04 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Reaction physics parameters
Relevant parameters (& sections)
dmax
ngem
igamma
ismm
ndedx
mdbatima
icxsni
icxspi
[fragdata]
[Delta-ray]
[ Repeated Collisions ]
inclg
icrdm
icrhi
iMeVperU
irqmd
eqmdmin
Numerous parameters are inherited from upper-class particles
To study ion physics parameters, begin with hadron physics!
Usually,
default is the most accurate and safe
option.

--- SLIDE 05 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Goal of this lecture
Design a neutron source with a Li target
Calculate neutron, DPA, and radioactivity

--- SLIDE 06 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
NuclearReaction.inp
Initial setup
100 MeV Proton pencil beam
1-cm-thick Li pellet target
[t-track] for visualizing particle trajectories (track_xz.out)
[t-product] for produced particle energy spectra (prod_reg.out)
[t-yield] for produced nuclide (yield.out)
[forced collisions] for proton-induced reactions
Source：
Geometry：
Tally：

Bias:
track_xz.eps
prod_reg.eps
yield_reg.eps
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Outline
Hadronic physics
Light cluster physics
Heavy ion physics
Non-hadron reactions
Homework

--- SLIDE 08 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
NuclearReaction.inp
[ P a r a m e t e r s ]
......
$ ielas    =           0
Proton elastic
scattering by Li
Poor statistics for the other reaction events
ielas : flag to consider p/n elastic scattering
Turn off elastic collsions of protons
prod_reg.eps
Continue up to
exercise #6
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 1
Turn off elastic collisions of protons
NuclearReaction.inp
[ P a r a m e t e r s ]
......
ielas    =           0
More inelastic reaction event statistics
Proton elastic scattering is not seen
This options is reserved for debug because reaction physics is distorted.
prod_reg.eps
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
Change total reaction cross section
[ P a r a m e t e r s ]
......
$ ielas    =           0
icxsni   =           1
Total reaction cross section for nucleons is controlled by icxsni.
PHITS offers 3 options.
NuclearReaction.inp
prod_reg.eps
Before excercise 1
~32
・Switch total reaction cross section from default to Kurotama
・Reverting ielas to default (=2) is encouraged for accuracy
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 2
Change total reaction cross section
[ P a r a m e t e r s ]
......
$ ielas    =           0
icxsni   =           1
NuclearReaction.inp
Total reaction cross section for nucleons is controlled by icxsni.
PHITS offers 3 options.
~26
prod_reg.eps
・Default is encouraged because Kurotama is not necessarily verified.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Total cross section model
Reaction simulation has 3 phases
Proj.
Free path sampling
Total cross section
Phase
Model
Non-equilibrium
Cascade model
Equilibrium
Evaporation model
Total cross
section(mb)
●Measurement
－Kurotama formula
- -NASA’s formula
All reaction observable are scaled by total cross section.

--- SLIDE 13 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
Change cascade model and find out which model is used.
[ P a r a m e t e r s ]
......
icxsni   =           1
inclg    =           0
NuclearReaction.inp
prod_reg.eps
Before excercise 3
~Energetic
      clusters
・How does prod_reg.eps change?
・Default is INCL model. Where can you find the model in place of INCL?
PHITS offers several models for proton/neutron-induced nuclear reactions.
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 3
Change cascade model and find out which model is used.
[ P a r a m e t e r s ]
......
icxsni   =           1
inclg    =           0
NuclearReaction.inp
prod_reg.eps
Clusters are below 30MeV
JAM model is used!
phits.out
inclg = 1 (default) is encouraged. JAM is a model for E > 3 GeV.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
Change evaporation model setting.
[ P a r a m e t e r s ]
maxcas   =        1000
inclg      =           1
igamma =           0
NuclearReaction.inp
・How does prod_reg.eps change?
Revert inclg and change target from Li to Al.
Change igamma from 2 (default) to 0 to stop prompt gamma.
Then, try igamma = 3. What tally output changes?
[ M a t e r i a l ]
set: c1[2.7]
set: c2[27]
m1     Al  1.0
Prompt gamma rays
(To get decay gamma-rays,
use DCHAIN)
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 16 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 4
Change evaporation model setting.
[ P a r a m e t e r s ]
maxcas   =        1000
inclg      =           1
igamma =           0
NuclearReaction.inp
Prompt gamma rays are considered by igamma = 2 (default)
.
[ M a t e r i a l ]
set: c1[2.7]
set: c2[27]
m1     Al  1.0
igamma = 2 (default) is encouraged. 0 is a debug option.
prod_reg.eps
Al
igamma = 0
inclg = 1
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 17 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 4’
Change evaporation model setting.
[ P a r a m e t e r s ]
maxcas   =        1000
inclg      =           1
igamma =           3
NuclearReaction.inp
igamma = 3 gives 2nd page of t-yield tally
[ M a t e r i a l ]
set: c1[2.7]
set: c2[27]
m1     Al  1.0
Isomer : Nucleus reaching meta-stable states during gamma-decay.
Yield_reg.eps
Isomers appear for igamma =2 are from nuclear data
Underestimated.
To calculate total yield, igamma = 3 is needed.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 18 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Change evaporation model setting.
[ P a r a m e t e r s ]
.......
ngem      =           2
NuclearReaction.inp
yield_reg.eps
・How does yield_reg.eps change?
Change ngem from 0 to 2 to upgraded GEM evaporation model.
Compare yield_reg.eps for ngem = 0 and 2.
[ T – Y i e l d ]
……
axis = mass
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 5
Change evaporation model setting.
[ P a r a m e t e r s ]
.......
ngem      =           2
NuclearReaction.inp
yield_reg.eps
Change ngem from 0 to 2 to upgraded GEM evaporation model.
Compare yield_reg.eps for ngem = 0 and 2.
[ T – Y i e l d ]
……
axis = mass
ngem = 2 invokes GEM Ver.2 featured by
Competition of gamma emission and nucleon emission
Nucleon shell energy taken from KTUY formula…
ngem = 1 is encouraged. GEM Ver.2 is beta-version subject to change.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6
Use JENDL5 cross section data in place of default algorithm
and make sure that cross section is used
[ P a r a m e t e r s ]
......
dmax(1)  =    200.
NuclearReaction.inp
prod_reg.eps
Before excercise 6
Reaction algorithms of the previous pages are overwritten by nuclear data
Think how to be sure that X-section was used
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 21 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 6
Change total reaction cross section
Proton transport and secondary particle production are
Calculated by JENDL-5, available up to 200 MeV.
prod_reg.eps
[ P a r a m e t e r s ]
......
dmax(1)  =    200.
NuclearReaction.inp
phits.out
h-data : # of proton cross section calls
Which is better, cross section or model? -> See the page after next.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 22 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Does JENDL-5 cover all elements?
No. Please see \phits\XS\jendl5\proton
X-section of 31 nuclei are installed by default.
To add 208 nuclei, photo-nuclear, alpha, S(α,β) table, … use jendl5_setup_win.exe or jendl5_setup_mac_lin.sh
Automated installer to set up extra cross sections

(Attention! Cross section data are heavy!)

--- SLIDE 23 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
JENDL-5 is advantageous
Transport of particles matters (e.g. shielding).
Kerma factor is applicable
Calculation is faster
Residual nuclide production matters (e.g. Use Dchain)
Cross section data pros & cons
☺
The same applies to other (d, t, α) cross sections.

--- SLIDE 24 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Outline
Hadronic physics
Light cluster physics
Heavy ion physics
Non-hadron reactions
Homework

--- SLIDE 25 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Exercise 7
Change total reaction cross section
In the same way as icxsni = 1
$ Light cluster physics
$ icrdm    =           1
$ icrhi    =           1
$ dmax(15) =  100.00
$ dmax(18) =  15.000
NuclearReaction.inp
prod_reg.eps
Continue up to
exercise #10
[ Parameters ]
....
 maxcas   =         200
Reduce CPU time
[ Source ]
….
proj =  deuteron
Source is H-2 beam
Which parameter can change the total cross section?
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 26 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 7
Change total reaction cross section
In the same way as icxsni = 1
$ Light cluster phycis
icrdm    =           1
$ icrhi    =           1
$ dmax(15) =  100.00
$ dmax(18) =  15.000
NuclearReaction.inp
prod_reg.eps
Graph looks the same
but the spectral height is different (see prod.out).
Forced collision changes particle weight (reaction probability depends on fcl parameter)
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 27 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Deuteron total reaction cross sections
Thin lines:
  Default NASA’s formula
Thick lines:
  MWO formula (icrdm = 1)
Difference : Factor of about 2
K. Minomo, K. Washiyama and K. Ogata, J. Nucl. Sci. Technol. 54, 127 (2017).
NASA’s formula (icrdm = 0) is the default for backward compatibility
but use of MWO formula is encouranged at low energy and heavy targets

--- SLIDE 28 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Exercise 8
Use JENDL-5 deuteron cross section for Li, C, B targets
$ Light cluster phycis
icrdm    =           1
$ icrhi    =           1
dmax(15) =  100.00
$ dmax(18) =  15.000
NuclearReaction.inp
Li : Density 0.53, Atomic mass 6.941
C : Density 2.00, Atomic mass 12.01
B : Density 2.34, Atomic mass 10.81
[ M a t e r i a l ]
set: c1[2.7]
set: c2[27]
m1     Al  1.0
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 29 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 8
Use JENDL-5 deuteron cross section for Li, C, and B targets
$ Light cluster phycis
icrdm    =           1
$ icrhi    =           1
dmax(15) =  100.00
$ dmax(18) =  15.000
NuclearReaction.inp
Li : OK
C : OK
B : NG. Reaction model (INCL) is used instead.
[ M a t e r i a l ]
set: c1[2.0]
set: c2[12.01]
m1     C  1.0
Li
B
C
See \phits\XS\jendl5\deuteron for data availability
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 30 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
Exercise 9
What happens if e-mode = 2 is present.
[ P a r a m e t e r s ]
 dmax(15) =  100.00
…
  e-mode = 2
NuclearReaction.inp
[ M a t e r i a l ]
set: c1[2.0]
set: c2[12.01]
m1     C  1.0
Target is C to use JENDL5.
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 31 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
X-section with e-mode for any particles but low-E neutrons
→ Use X-section for total cross section and use reaction models (INCL).
This combination is better than pure model calculation (i.e. without dmax(15))
Answer 9
What happens if e-mode = 2 is present
NuclearReaction.inp
h-data =           459.  : p, d, a data library
…
 INCL =              11.  : INCL model
h-data=              0.  : p, d, a data library…
…
 INCL =           8029.  : INCL model
[ P a r a m e t e r s ]
 dmax(15) =  100.00
…
  e-mode = 2
[ M a t e r i a l ]
set: c1[2.0]
set: c2[12.01]
m1     C  1.0
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 32 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 10
SLIDE_TEXT:
Exercise 10
Use alpha particle as source and use JENDL-5 cross section
$ Light cluster phycis
$ icrhi    =           1
 imevperu =           1
 dmax(15) =  100.00
$ e-mode = 2
$ dmax(18) =  3.75
NuclearReaction.inp
Change projectile species and energy to use cross section for alpha
Change target material if needed. (Comment out e-mode = 2)
[ S o u r c e ]
set: c4[3.75]
  totfact =   1.000
   s-type =   1
     proj =  deuteron
       e0 =   c4
[ M a t e r i a l ]
Exercise below require JENDL5 installation
(alpha and photo-nuclear)
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 33 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 10
Use alpha particle as source and JENDL-5 cross section for α
$ Light cluster phycis
$ icrhi    =           1
 dmax(18) =  3.750
NuclearReaction.inp
Change projectile species and energy until cross section is used for alpha
Change target material if needed.
[ S o u r c e ]
set: c4[3.75]
  totfact =   1.000
   s-type =   1
     proj =  alpha
       e0 =   c4
[ M a t e r i a l ]
set: c1[2.34]
set: c2[10.81]
m1     B  1.0
Secondary particles
Scattered primary alphas
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 34 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 10’
Use alpha particle as source and JENDL-5 cross section for α
$ Light cluster phycis
 icrhi    =           2
 dmax(18) =  3.750
NuclearReaction.inp
Change projectile species and energy until cross section is used for alpha
Change target material if needed.
[ S o u r c e ]
set: c4[3.75]
  totfact =   1.000
   s-type =   1
     proj =  alpha
       e0 =   c4
[ M a t e r i a l ]
set: c1[2.34]
set: c2[10.81]
m1     B  1.0
Don’t worry. They are messages on p and d.
Alpha cross sections are 5010.20a and 5011.20a
See phits.out h-data to be sure
Total cross section is changed (like icrdm = 1) but impact is small
icrhi = 2 is meaningful around 100 MeV/n
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 35 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Outline
Hadronic physics
Light cluster physics
Heavy ion physics
Non-hadron reactions
Homework

--- SLIDE 36 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 11
SLIDE_TEXT:
Exercise 11
Change projectile to carbon ion and use ion reaction model
$ Heavy ion phycis
$ irqmd    =       1
$ eqmdmin  =  1.0
NuclearReaction.inp
Change projectile species and include 12C to [forced collisions] is not enough.
Change [parameters] relevant to QMD model to let nuclear reactions happen.
[ S o u r c e ]
set: c4[3.75]
  totfact =   1.000
   s-type =   1
     proj =  12C
       e0 =   c4
No reactions
12C is just stopped by stopping power
[ Forced collisions ]
 part = proton deuteron alpha 12C
  reg     fcl
  1        -1
Continue up to
exercise #16
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 37 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 11
Change projectile to carbon ion and use ion reaction model
$ Heavy ion phycis
$ irqmd    =       1
eqmdmin  =  1.0
NuclearReaction.inp
Change projectile species and [forced collisions] is not enough.
JQMD works only above 10 MeV/n by default (eqmdmin = 10).
[ S o u r c e ]
set: c4[3.75]
  totfact =   1.000
   s-type =   1
     proj =  12C
       e0 =   c4
* Lower eqmdmin is mandatory for low E ions, nontheless JQMD might be inaccurate below 10 MeV/n.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 38 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 12
SLIDE_TEXT:
Exercise 12
What if target is heavy?
[ P a r a m e t e r s ]
 maxcas   =         10     $ Heavy ion phycis
irqmd    =       1
NuclearReaction.inp
Change target to lead (density : 11.34 g/cm^3, atomic mass : 207.2 u)
Raise projectile energy to 50 MeV/n to surpass Coulomb barrier.
[ M a t e r i a l ]
set: c1[11.34]
set: c2[207.2]
m1     Pb  1.0
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 39 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 12
What if target is heavy?
Slow
(~10 s/projectile)
[ P a r a m e t e r s ]
 maxcas   =         10     $ Heavy ion phycis
irqmd    =       1
NuclearReaction.inp
[ M a t e r i a l ]
set: c1[11.34]
set: c2[207.2]
m1     Pb  1.0
track_xz.eps
prod_reg.eps (2nd page)
[ S o u r c e ]
 set: c4[50]
proj =  12C
  e0 =   c4
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 40 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Calculation procedure of JQMD
CPU time ≈ Projectile nucleon x Target nucleon
=
The slowest process
	 ↓
Dominate CPU time

--- SLIDE 41 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 13
SLIDE_TEXT:
Exercise 13
Make fragment production more accurate
[ P a r a m e t e r s ]
 maxcas   =         10
$ Hadron physics
 ismm     =           1     $ Heavy ion phycis
 irqmd    =       1
NuclearReaction.inp
Turn on “irqmd = 1” and “ismm = 1”
E = 50 MeV/n
w/o ismm, irqmd
yield_reg.eps
Peripheral abrasion
[ T - Y i e l d ]
 …
 axis = chart
Intermediate-mass
fragments
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 42 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 13
Make fragment production more accurate
[ P a r a m e t e r s ]
 maxcas   =         10
$ Hadron physics
 ismm     =           1     $ Heavy ion phycis
 irqmd    =       1
NuclearReaction.inp
Turn on “irqmd = 1” and “ismm = 1”
irqmd = 1 is accurate for peripheral collisions
yield_reg.eps
More intermediate-mass fragments
[ T - Y i e l d ]
 …
 axis = chart
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 43 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 13
Make fragment production more accurate
[ P a r a m e t e r s ]
 maxcas   =         10
$ Hadron physics
 ismm     =           1     $ Heavy ion phycis
 irqmd    =       1
NuclearReaction.inp
Turn on “irqmd = 1” and “ismm = 1”
ismm and irqmd are slow
→Not activated by default
irqmd = 0/1
ismm = 0/1
See
irqmd https://doi.org/10.1103/PhysRevC.92.024614
ismm https://doi.org/10.1016/j.nima.2013.04.078
for more details.
[ T - Y i e l d ]
 …
 axis = chart
irqmd and ismm usually improve accuracy but they are slow. For ismm see next page.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 44 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Algorithm of SMM
SMM is effective for
*compound mass (projetile+Target) > 100 and
*Excitation energy > 2 MeV/nucleon
e.g. 〇50 MeV/n C + NatPb
   ×100 MeV/n p + NatAg
SMM is theoretically applicable to p, d, t, α but effectively not impactful.

--- SLIDE 45 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 14
SLIDE_TEXT:
Exercise 14
Calculate DPA (Displacement Per Atom : damage index)
[ P a r a m e t e r s ]
 maxcas   =         10
$ Hadron physics
$ ismm     =      1     $ Heavy ion phycis
$ irqmd    =       1
NuclearReaction.inp
Introduce [T-DPA] tally with mesh = r-z from \phits\sample\tally\t-dpa\t-dpa_r-z.inp to score DPA in cell 100.
Tune [T-DPA] z coordinate to cover cell 100
Turn off ismm and irqmd to save CPU time
[ T - D P A ]
   mesh =  r-z
   r-type =    1
       nr =    1
            0.0 10.0
   z-type =    2
     zmin =    0.00000
     zmax =         c3
        nz =   10
      axis =   z
MENTIONED_INPUT_NAMES: NuclearReaction.inp, t-dpa_r-z.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 46 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 14
Calculate DPA (Displacement Per Atom : damage index)
[ P a r a m e t e r s ]
 maxcas   =         10
$ Hadron physics
$ ismm     =      1     $ Heavy ion phycis
$ irqmd    =       1
NuclearReaction.inp
Pb crystal lattice is damaged by C ion and its secondary particles.
[ T - D P A ]
   mesh =  r-z
   r-type =    1
       nr =    1
            0.0 10.0
   z-type =    2
     zmin =    0.00000
     zmax =         c3
        nz =   10
      axis =   z
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 47 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 15
SLIDE_TEXT:
Exercise 15
Calculate DPA for low energy ions
[ S o u r c e ]
set: c4[3]
 e0 =   c4
NuclearReaction.inp
Lower projectile energy to 3 MeV/n.
Nuclear reactions are unlikely but …
[ S u r f a c e ]
set: c3[0.003]
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 48 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 15
Calculate DPA for low energy ions
[ S o u r c e ]
set: c4[3]
 e0 =   c4
NuclearReaction.inp
dpa_reg.eps
track_xz.eps
Even below nuclear reaction threshold, DPA is induced by Ruthorford scattering
[ S u r f a c e ]
set: c3[0.003]
Lower projectile energy to 3 MeV/n.
Nuclear reactions are unlikely but …
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 49 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 16
SLIDE_TEXT:
Exercise 16
Change stopping power model
[ P a r a m e t e r s ]
...
 ndedx    =           0
NuclearReaction.inp
Calculate dE/dx by SPAR model in place of ATIMA
dpa_reg.eps
track_xz.eps
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 50 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 16
Change stopping power model
[ P a r a m e t e r s ]
...
 ndedx    =           0
NuclearReaction.inp
Calculate dE/dx by SPAR model in place of ATIMA
dpa_reg.eps
track_xz.eps
Energy loss in matter depends on dE/dx model.
ATIMA (Default, ndedx = 3) is encouraged for accuracy.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 51 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Outline
Hadronic physics
Light cluster physics
Heavy ion physics
Non-hadron reactions
Homework

--- SLIDE 52 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 17
SLIDE_TEXT:
Exercise 17
Simulate photo-nuclear reactions
[ P a r a m e t e r s ]
…..
 maxcas   =  50
 negs     =     1
 ipnint    =     1
 pnimul  =     100
NuclearReaction.inp
[ S o u r c e ]
 set: c4[30]
proj =  photon
  e0 =   c4
[ Forced collisions ]
 part = photon
[T-Track]
 part =  all neutron proton deuteron alpha photon
Continue up to
exercise #19
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 53 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 17
Simulate photo-nuclear reactions
[ P a r a m e t e r s ]
…..
 maxcas   =  50
 negs     =     1
 ipnint    =     1
 pnimul  =     100
NuclearReaction.inp
[ S o u r c e ]
 set: c4[30]
proj =  photon
  e0 =   c4
[ Forced collisions ]
 part = photon
[T-Track]
 part =  all neutron proton deuteron alpha photon
track_xz.eps
prod_reg.eps (2nd page)
pnimul = 100 and forced collisions are encouraged for photo-nuclear reactions.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 54 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 17
Photo-nuclear reaction cross sections *
[ P a r a m e t e r s ]
…..
 maxcas   =  50
 negs     =     1
 ipnint    =     1
 pnimul  =     100
NuclearReaction.inp
* See  S. Noda, et al, JNST 52(1), 57–62. (2014). https://doi.org/10.1080/00223131.2014.923349
Atomic reactions
Energy
X-sec
Photonuclear reaction cross section is multiplied by pnimul and weight of product is 1/pnimul
Otherwise, only atomic reactions are biased by [forced collisions]
Photo-nuclear reactions
X-sec is 100 times smaller
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 55 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 18
SLIDE_TEXT:
Exercise 18
Simulate photo-nuclear reactions by electron beam
[ P a r a m e t e r s ]
…..
 negs     =     1
 ipnint    =     1
 pnimul  =     100
NuclearReaction.inp
[ S o u r c e ]
set: c4[30]
…
   proj =  electron
[ S u r f a c e ]
set: c3[1]
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 56 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 18
Simulate photo-nuclear reactions by electron beam
[ P a r a m e t e r s ]
…..
 negs     =     1
 ipnint    =     1
 pnimul  =     100
NuclearReaction.inp
[ S o u r c e ]
set: c4[30]
…
   proj =  electron
[ S u r f a c e ]
set: c3[1]
track_xz.eps
prod_reg.eps
Electron
Photon
Secondary hadrons
Bremsstrahlung
by negs = 1
Photo-nuclear
by ipnint = 1
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 57 ---
PPTX_FILE: phits-lec-HENP-en.pptx
EXERCISE_NO: 19
SLIDE_TEXT:
Exercise 19
Simulate GeV-class electron beam
[ P a r a m e t e r s ]
...
 negs     =        2
 igmuppd =      1
 gmumul =    100000
NuclearReaction.inp
[ S o u r c e ]
set: c4[5000]
GeV-TeV electron, positron, photon transport mode
μ-μ pair production model and bias factor
MENTIONED_INPUT_NAMES: NuclearReaction.inp
ANSWER_FILE: input/NuclearReaction.inp

--- SLIDE 58 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer 19
Simulate GeV-class electron beam
[ P a r a m e t e r s ]
...
 negs     =        2
 igmuppd =      1
 gmumul =    100000
NuclearReaction.inp
[ S o u r c e ]
set: c4[5000]
part. = muon+
part. = muon-
Muon pair production is seen
gmumul ~ 100000 is encouraged for photo-muon production.
MENTIONED_INPUT_NAMES: NuclearReaction.inp

--- SLIDE 59 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Summary
Summary
Various options for hadron transport control reactions physics are available.
Most of them are optimized by default. But some time-consuming options are not used by default
Parameters for reaction models and total cross sections
Use of evaluated cross section data library is an option alternative to reaction models + total cross sections.
But cross section data library covers limited number of nuclei
Use [T-DPA] to calculate DPA. Both elastic (Rutherford) and inelastic (nuclear) reactions are considered

--- SLIDE 60 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Outline
Hadronic physics
Light cluster physics
Heavy ion physics
Non-hadron reactions
Homework

--- SLIDE 61 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Homework
Build Li(d,n) neutron source
Calculate DPA and heat in Li
Maximise neutron yield
Optimize models to get accurate neutron spectrum
Calculate isomers in Al pipe (e.g. 26mAl)
Example geometry

--- SLIDE 62 ---
PPTX_FILE: phits-lec-HENP-en.pptx
SLIDE_TEXT:
Answer sample
Neutron in beam pipe
DPA in Li target
Energy deposition
Nuclide yield
26mAl

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/Homework-example.inp
FILE: input/NuclearReaction-2.inp
FILE: input/NuclearReaction-3.inp
FILE: input/NuclearReaction-4.inp
FILE: input/NuclearReaction-5.inp
FILE: input/NuclearReaction-6.inp
FILE: input/NuclearReaction-7.inp
FILE: input/NuclearReaction-8.inp
FILE: input/NuclearReaction-9.inp
FILE: input/NuclearReaction-10.inp
FILE: input/NuclearReaction-11.inp
FILE: input/NuclearReaction-12.inp
FILE: input/NuclearReaction-13.inp
FILE: input/NuclearReaction-14.inp
FILE: input/NuclearReaction-15.inp
FILE: input/NuclearReaction-16.inp
FILE: input/NuclearReaction-17.inp
FILE: input/NuclearReaction-18.inp
FILE: input/NuclearReaction-20.inp

[BONUS_TEXT_FILES]
NOTE: None
