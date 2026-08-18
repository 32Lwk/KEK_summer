# Lecture: advanced/shielding

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/shielding
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: shielding
LECTURE_PATH_INDEX: lecture/advanced/shielding
PPTX_FILES: PHITS-shielding-en.pptx, PHITS-shielding-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: accelerator, activation, maze
SECTION_KEYWORDS: bq, gev, h, m, ma, multiplier, mw, s, t-cross, t-dchain, t-deposit, t-point, t-track, t-wwg

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/shielding
LECTURE_PATH_INDEX: lecture/advanced/shielding
PPTX_FILES: PHITS-shielding-en.pptx, PHITS-shielding-jp.pptx
INPUT_DIR_COUNT: 2
MAIN_INPUT_COUNT: 3
SLIDE_COUNT: 96
EXERCISE_SLIDE_COUNT: 30
BONUS_INPUT_COUNT: 3
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- accelerator/input
- maze/input

[MAIN_INPUT_FILES]
- accelerator/accelerator.inp
- activation/activation.inp
- maze/maze.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Radiation shielding design
- SLIDE 02: Final goal of this exercise
- SLIDE 03: Table of contents
- SLIDE 04: Purpose
- SLIDE 05: Calculation of dose rates using the simplified formula
- SLIDE 06: Results of dose rate calculations using the simplified formula
- SLIDE 07: EXERCISE 1 | Flow of this lecture
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 08: Importance notices for applying PHITS to shielding design
- SLIDE 09: Check geometry
- SLIDE 10: EXERCISE 1 | Exercise 1: Check source
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 11: Answer 1
- SLIDE 12: Conversion to effective dose rate
- SLIDE 13: EXERCISE 2 | Exercise 2: Calculation of effective dose rate with [t-track]
  ANSWER_FILE: accelerator/input/accelerator-3.inp
- SLIDE 14: [t-point]
- SLIDE 15: EXERCISE 3 | Exercise 3: Calculation of effective dose rate with [t-point]
  ANSWER_FILE: accelerator/input/accelerator-4.inp
- SLIDE 16: Summary of calculation
- SLIDE 17: Summary for calculation
- SLIDE 18: Table of contents
- SLIDE 19: Purpose
- SLIDE 20: Neutron dose rate calculation using Tesch's  formula
- SLIDE 21: Neutron dose rate calculation using Tesch's  formula
- SLIDE 22: EXERCISE 1 | Flow of this lecture
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 23: Check geometry
- SLIDE 24: High energy nuclear data library JENDL-4.0/HE
- SLIDE 25: EXERCISE 1 | Exercise 1: Normal particle transport calculation
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 26: Source with dump data
- SLIDE 27: ID number of dump data
- SLIDE 28: EXERCISE 2 | Exercise 2: Setting outer void for dump source
  ANSWER_FILE: accelerator/input/accelerator-3.inp
- SLIDE 29: Answer 2
- SLIDE 30: EXERCISE 3 | Exercise 3: Create dump source data
  ANSWER_FILE: accelerator/input/accelerator-4.inp
- SLIDE 31: Answer 3
- SLIDE 32: EXERCISE 4 | Exercise 4: Reduce the statistical uncertainty of Dump data
  ANSWER_FILE: accelerator/input/accelerator-5.inp
- SLIDE 33: EXERCISE 5 | Exercise 5: Transport simulation using dump data as the source
  ANSWER_FILE: accelerator/input/accelerator-6.inp
- SLIDE 34: Answer 5
- SLIDE 35: EXERCISE 6 | Exercise 6: Transport calculation using variance reduction technique
  ANSWER_FILE: accelerator/input/accelerator-end.inp
- SLIDE 36: EXERCISE 6 | Exercise 6: Transport simulation using variance reduction technique
  ANSWER_FILE: accelerator/input/accelerator-end.inp
- SLIDE 37: Answer 6
- SLIDE 38: Summary of calculation
- SLIDE 39: Summary of calculation
- SLIDE 40: Air activation estimation
- SLIDE 41: EXERCISE 7 | Exercise7: Air activation
  ANSWER_FILE: accelerator/input/accelerator-end.inp
- SLIDE 42: Main output file (*.act)
- SLIDE 43: Drawing output file (*.eps)
- SLIDE 44: Radioactivity time variation of major nuclides
- SLIDE 45: Radioactivity time variation of major nuclides
- SLIDE 46: Radioactivity time variation of major nuclides
- SLIDE 47: Table of contents
- SLIDE 48: Summary
- SLIDE 01: 放射線遮蔽計算
- SLIDE 02: 本実習の目標
- SLIDE 03: 内容
- SLIDE 04: 目的
- SLIDE 05: 簡易式による線量率の計算
- SLIDE 06: 簡易式による線量率の計算結果
- SLIDE 07: EXERCISE 1 | 本実習の流れ
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 08: PHITSを遮蔽計算に適用する際の注意点
- SLIDE 09: 計算体系の確認
- SLIDE 10: EXERCISE 1 | 課題１: 線源の確認
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 11: EXERCISE 1 | 課題１の解答
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 12: 実効線量率への換算
- SLIDE 13: EXERCISE 2 | 課題２: [t-track]による実効線量率の計算
  ANSWER_FILE: accelerator/input/accelerator-3.inp
- SLIDE 14: [t-point]
- SLIDE 15: EXERCISE 3 | 課題３: [t-point]による実効線量率の計算
  ANSWER_FILE: accelerator/input/accelerator-4.inp
- SLIDE 16: 計算値のまとめ
- SLIDE 17: 計算値のまとめ
- SLIDE 18: 内容
- SLIDE 19: 目的
- SLIDE 20: Tesch の点状線源の式による中性子線量率計算
- SLIDE 21: Tesch の点状線源の式による中性子線量率計算
- SLIDE 22: EXERCISE 1 | 本実習の流れ
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 23: 計算体系の確認
- SLIDE 24: 高エネルギー核データライブラリJENDL-4.0/HE
- SLIDE 25: EXERCISE 1 | 課題１: 通常の粒子輸送計算を実行
  ANSWER_FILE: accelerator/input/accelerator-2.inp
- SLIDE 26: Dump dataを用いた線源
- SLIDE 27: Dump定義文
- SLIDE 28: EXERCISE 2 | 課題２: Dump data作成のための外部ボイドの設定
  ANSWER_FILE: accelerator/input/accelerator-3.inp
- SLIDE 29: EXERCISE 2 | 課題２の解答
  ANSWER_FILE: accelerator/input/accelerator-3.inp
- SLIDE 30: EXERCISE 3 | 課題３: Dump data作成
  ANSWER_FILE: accelerator/input/accelerator-4.inp
- SLIDE 31: EXERCISE 3 | yz-track.eps
  ANSWER_FILE: accelerator/input/accelerator-4.inp
- SLIDE 32: EXERCISE 4 | 課題4: Dump dataの統計誤差を小さくする
  ANSWER_FILE: accelerator/input/accelerator-5.inp
- SLIDE 33: EXERCISE 5 | 課題5: Dump dataを線源とした遮蔽計算
  ANSWER_FILE: accelerator/input/accelerator-6.inp
- SLIDE 34: EXERCISE 5 | 課題5の解答
  ANSWER_FILE: accelerator/input/accelerator-6.inp
- SLIDE 35: Step6: 分散低減法を用いた輸送計算
- SLIDE 36: EXERCISE 6 | 課題6: 分散低減法を用いた輸送計算
  ANSWER_FILE: accelerator/input/accelerator-end.inp
- SLIDE 37: EXERCISE 6 | 課題6の解答
  ANSWER_FILE: accelerator/input/accelerator-end.inp
- SLIDE 38: 計算値のまとめ
- SLIDE 39: 計算結果
- SLIDE 40: 空気の放射化計算
- SLIDE 41: EXERCISE 7 | 課題7: 空気の放射化計算
  ANSWER_FILE: accelerator/input/accelerator-end.inp
- SLIDE 42: 主な出力ファイル(*.act)
- SLIDE 43: 描画出力ファイル(*.eps)
- SLIDE 44: 主要核種の放射能時間変化
- SLIDE 45: 主要核種の放射能時間変化
- SLIDE 46: 主要核種の放射能時間変化
- SLIDE 47: 内容
- SLIDE 48: まとめ

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: accelerator/accelerator.inp
FILE: activation/activation.inp
FILE: maze/maze.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Radiation shielding design
Last revised: March 2023
phits/lecture/advanced/shielding
SPEAKER_NOTES:
I would like to start with radiation shielding design with PHITS.

--- SLIDE 02 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Final goal of this exercise
Learn how to design radiation shielding for RI and accelerator facilities using various useful functions of PHITS
Calculation of γ-ray streaming in concrete maze structures
Calculation of neutron shielding and air activation around the beam dump of a proton accelerator facility
Dose limitation given in this lecture note is based on Japanese regulation
SPEAKER_NOTES:
Final goal of this exercise is to learn how to design radiation shielding for RI and accelerator facilities using various useful functions of PHITS.
For RI source, we will calculate γ-ray streaming in concrete maze structures.
For accelerator facilities, we will calculate neutron shielding and air activation around the beam dump of a proton accelerator facility.
Please note that Dose limitation given in this lecture note is based on Japanese regulation.

--- SLIDE 03 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Table of contents
1. Calculation of γ-ray streaming in concrete maze structures

2. Calculation of neutron shielding and air activation around the beam dump of a proton accelerator facility

3. Summary
SPEAKER_NOTES:
This is a table of contents.
First is   Calculation of γ-ray streaming in concrete maze structures.
Second is Calculation of neutron shielding and air activation around the beam dump of a proton accelerator facility.
Third is summary.

--- SLIDE 04 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Purpose
A simplified formula for calculating dose rates is generally used in shielding design for RI facilities

Let’s check the accuracy of the simplified formula using PHITS
SPEAKER_NOTES:
This is the purpose of the first recture.
 A simplified formula for calculating dose rates is generally used in shielding design for RI facilities.
Let’s check the accuracy of the simplified formula using PHITS.

--- SLIDE 05 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Calculation of dose rates using the simplified formula
The German Industrial Standard  (DIN) formula gives the dose rate at the exit of a two-bend duct with a 90-degree bend angle. Let’s calculate dose rates for P0 to P3 (D0 to D3).
Auslegung von Zweifach Gekickten Gasgefullten in Abschirm Wanden aus Beton gegen Gammastrahlung. DEUTSCHE NORMMEN, DIN 25-427 Teil 1,2 (1977).
Effective dose rate constant in μSvh-1MBq-1m2. For 192Ir: 0.117*
Source Intensity in MBq:
in m
Correction factor of effect of radiation penetrating the edge of the bend: 1.5**
Effective scattering coefficient at the bend: 0.08**
Concrete maze structure
Enter geometric shape conditions in the light blue cells of the DIN sheet in AnalyticalMethod.xlsx
*Isotope Handbook in Japanese
*Handbook of radiation shielding Japanese
SPEAKER_NOTES:
The German Industrial Standard  (DIN) formula gives the dose rate at the exit of a two-bend duct with a 90-degree bend angle.
This is an iridium source. Let’s calculate dose rates for P0 to P3 (D0 to D3).
To calculate dose rates, please open the exel file.
Please enter geometric shape conditions in the light blue cells of the DIN sheet in AnalyticalMethod.xlsx

--- SLIDE 06 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Results of dose rate calculations using the simplified formula
Assuming that P3 is the boundary of the controlled area, the evaluated dose at this point should be below the 3-month effective dose limit of 1.3 mSv.
The maximum time that this Ir source can be used within three months is 1.3 mSv/1.03 (μSv/h) = 1262 hours.
Assuming 3 months = 13 weeks (2184 hourse), the Ir source should be stored in a storage box outside the facility for 922 hours to keep the total dose below the limitation.
Let’s check the accuracy of this estimation using PHITS
SPEAKER_NOTES:
These are results of dose rate calculations using the simplified formula.

Assuming that P3 is the boundary of the controlled area, the evaluated dose at this point should be below the 3-month effective dose limit of 1.3 mSv.
The maximum time that this Ir source can be used within three months is 1.3 mSv/1.03 (μSv/h) = 1262 hours.
Assuming 3 months = 13 weeks (2184 hourse), the Ir source should be stored in a storage box outside the facility for 922 hours to keep the total dose below the limitation.
This is a results by the simplified formula.
Let’s check this estimation using PHITS.

--- SLIDE 07 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Flow of this lecture
Exercise 1: Check source
Exercise 2: Calculation of effective dose rate with [t-track]
Exercise 3: Calculation of effective dose rate with [t-point]
SPEAKER_NOTES:
Here is flow of this lecture.
Check source, Calculation of effective dose rate with [t-track], and with [t-point].
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 08 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Importance notices for applying PHITS to shielding design
“Dose” evaluated in shielding design is not “absorbed dose” calculated by [t-deposit] but “ambient dose” or “effective dose” calculated by [t-track] or [t-point] with the multiplier function
The reduction of the computational time is the key issue in shielding design, and event generator and EGS modes are not necessary to be used
PHITS and simple formulae are needed to be supplementally used because it is impractical to evaluate the doses everywhere in the radiation facilities using PHITS

--- SLIDE 09 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Check geometry
P1
P2
P3
1m
1.5m
3m
1.5m
Height
2m
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 8
Check geometry
200GBq
192Ir source
Concrete
1st leg
2nd leg
3rd leg
0.8m
[Material]
$   Concrete   2.302 g/cm^3, taken from ANL-5800 Type 02-a
m1     H     -0.023
         C     -0.0023
         O     -1.22
         Na    -0.0368
         Mg    -0.005
         Al    -0.078
         Si    -0.775
         K     -0.0299
         Ca    -0.1
         Fe    -0.032

$   Air at ground level  1.21e-3 g/cm^3
m2      N   4.0586E-05
          O   1.0800E-05
         Ar   2.4255E-07
Air
xz-track.eps
maze/maze.inp
SPEAKER_NOTES:
Lets go to maze folder.
The maze is composed of concrete blocks and air.
Lets check geometry in your PC and open the eps file.
MENTIONED_INPUT_NAMES: maze.inp

--- SLIDE 10 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1: Check source
Nuclide：Iridium  192 (192Ir)
Activity：200 GBq
Check the energy spectrum and direction of the source.
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 5
Change and execute（No reaction mode）
maze.inp
[ S o u r c e ]
   s-type =   1
     proj =  photon
......

   e-type =  28
       ni =   1
Ir-192    200e9
norm =   0
Number of RI to specify
RI and activity(unit is Bq）
Option for normalization
 0: (/sec) （Initial value）
 1: (/source)
Usage of RI source function
SPEAKER_NOTES:
This is Exetcise 1 for checking source.
In the source section, iridium 192 with 200 GBq is defined as a source.
E-type=28 means Usage of RI source function.
Ni is the number of RI to specify.
This is RI and acutuvity unit is Bq.
Nnorm is option for normalization.
Zero is per seoncd and 1 is per source. In this lecture, we use zero, per second.
To check the energy spectrum and direction of the source,
Lets change icntle parameter and execute PHITS. Five means no reaction mode.
MENTIONED_INPUT_NAMES: maze.inp
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 11 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Answer 1
Check the energy spectrum and direction of the source.
Since all matter is void, the gamma rays fly in a straight line.
Multiple gamma rays are emitted from 192Ir.
track_xz.eps
p1-ene.eps
The unit of the graph is [1/cm2/source], but the actual output is [1/cm2/sec].
P1
SPEAKER_NOTES:
This is the answer.
Since all matter is void, the gamma rays fly in a straight line.
Multiple gamma rays are emitted from 192Ir.
Please note that the unit of the graph is [1/cm2/source], but the actual output is [1/cm2/sec].

--- SLIDE 12 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Conversion to effective dose rate
[ T - T r a c k ]
…
 multiplier = all
…
      mat              mset1
   all    ( 3600*1e-6 -202 )
The fluence calculated with [t-track] and [t-point] can be multiplied with multiple functions stored in PHITS, or defined in the [multiplier] section.
(C k): C normalization factor
         k ID number
When the fluence is normalized by the source intensity, the dose is derived in (pSv).
An excerpt from the database of DCC stored in the folder phits/data/multiplier/.
To derive the effective dose rate (μSv/h),
substitute a value for the normalization factor C.
flux(1/cm2/sec) x DCC (pSv・cm2) x 3600(sec/h) x 1e-6(μ/pico)
= effective dose rate（μSv/h)
Dose Conversion Coefficient (DCC)*
*Current Japanese laws and regulations are based on ICRP60, but in this case, values based on ICRP103 definitions were used.
SPEAKER_NOTES:
This is Conversion to effective dose rate.
The fluence calculated with [t-track] and [t-point] can be multiplied with multiple functions stored in PHITS, or defined in the [multiplier] section.
This is an example.
Normalization factor and ID number, which is DCC, are set in the [t-track] section.
An excerpt from the database of DCC stored in the folder phits/data/multiplier/.
We prepared Ambient dose equivalent, Effective dose.  Unit of DCC is pSv cm2.

When the fluence is normalized by the source intensity, the dose is derived in (pSv).
To derive the effective dose rate (μSv/h), substitute a value for the normalization factor C.

Current Japanese laws and regulations are based on ICRP60, but in this case, values based on ICRP103 definitions were used.

--- SLIDE 13 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2: Calculation of effective dose rate with [t-track]
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 0
 maxcas   =        100000
 maxbch   =          10
[T-Track]
  title =  dose rate at p1, p2, p3
    mesh = reg
    reg = 11 12 13
  e-type = 2
    emin = 0
    emax =  100
      ne = 1
  axis = reg
  file = dose-track.out
  part = photon
  unit = 1
  z-txt = Effective dose rate
multiplier =all
emax = 1000
mat mset1
all ( 3600*1e-6 -202 )
Detector:
sphere with 15 cm radius
xz-track.eps
P1
P2
P3
dose-track.out
Normal calculation mode
P1
P2
P3
Too large statistical uncertainty!
Let’s calculate dose rate efficiently with [t-point].
Change to 10
Let’s calculate dose rate for detectors (P1-P3).
h:   x      n     n          y(photon  ),l3   n
#  num    reg     volume     photon      r.err
    1      11   1.4137E+04   6.0184E+03  0.0394
    2      12   1.4137E+04   5.3274E+01  0.2712
    3      13   1.4137E+04   5.0319E+00  0.7095
SPEAKER_NOTES:
Lets move on exercise 2, Calculation of effective dose rate with [t-track].

In t-track section, sphere with 15 cm radius are set in the three positions.
Let’s calculate dose rate for detectors with changing to 10.

If the number of histories is small, the statistical uncertainty will be too large.
Therefore, increasing the number of maxcas and maxbch can provide good statistical uncertainty.

Here, we introduce another method of increasing statistical uncertainty using [t-point] .
ANSWER_FILE: accelerator/input/accelerator-3.inp

--- SLIDE 14 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
[t-point]
It is impractical to calculate particle fluence at a certain point (point detector) or line (ring detector), using [t-track].
Normally, radiation that probabilistically enters a set region is tallied, and when tally region is small, it takes an extremely long calculation time to obtain sufficient statistical accuracy.
Unlike [t-track], [t-point] can be evaluated by calculating the directional and transmission probabilities to the tally position at the source location or at the point where the particle is generated by scattering. Therefore, [t-point] works well for measurements in regions where the probability of particle presence is small.
However, [t-point] can only be evaluated if the angular and energy distributions of the produced particles at the scattering point are known in advance.
Since it is difficult to evaluate the transmission probability if there is energy loss of charged particles in the material, the particles are limited to neutrons and photons for which a cross section library exists.
The following conditions must be satisfied.
(1) Particle energy should not exceed the maximum energy of the data library used, i.e., dmax.
(2) Only the fluence of neutrons and photons can be calculated.
(3) Neither event generator mode nor EGS5 should be used.
(4) Reflection or white boundary surface should not be used.
Detailed information is available in PHITS manual and /phits/utility/tpoint

--- SLIDE 15 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3: Calculation of effective dose rate with [t-point]
[ T-point ] off
point = 3
non  x         y    z               r0
1     200      0    -200         1.0
2     200-c7  0    -200         1.0
  200-c7  0   -200-150   1.0

・ ・ ・ ・ ・ ・
dose-point.out
The statistical error of [t-point] is smaller than that of [t-track].
Coordinates of the point detector
Radius of the fictitious sphere (cm)
(for more information on the fictitious sphere, see the read-me file in “/phits/utility/tpoint” )
Number of Point detectors. Upper limit is 20.
#  e-lower      e-upper          photon          r.err
 0.0000E+00   1.0000E+02   6.1766E+03  0.0029
・ ・ ・ ・ ・ ・
 0.0000E+00   1.0000E+02   6.0139E+01  0.0165
・ ・ ・ ・ ・ ・
 0.0000E+00   1.0000E+02   2.8960E+00  0.0906
・ ・ ・ ・ ・ ・
Activate [t-point] and execute PHITS again
SPEAKER_NOTES:
Exercise 3 is Calculation of effective dose rate with [t-point].

This is the [t-point] tally.
Point= is the number of point detector. Upper limit is 20.
X, y, z are coordinates of the point detector.
R0 is radius of the fictitious sphere. For more information on the fictitious sphere, see the read-me file in “/phits/utility/tpoint”

Lets Activate [t-point] and execute PHITS again .
ANSWER_FILE: accelerator/input/accelerator-4.inp

--- SLIDE 16 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Summary of calculation
Let’s complete the following table. Add error to PHITS dose rate.
Number of trials for Monte Carlo simulations
maxcas   =        100000
maxbch   =          10
Maximum usable time of source for 3-month
Tmax  = 1300 / D3
The value at D3 should be less than the 3-month effective dose limit of 1.3 mSv.
Comparison of dose rate (μSv/h)

--- SLIDE 17 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Summary for calculation
Let’s complete the following table. Add error to PHITS dose rate.
Number of trials for Monte Carlo simulations
maxcas   =        100000
maxbch   =          10
Maximum usable time of source for 3-month
Tmax  = 1300 / D3
The value at D3 should be less than the 3-month effective dose limit of 1.3 mSv.
Comparison of dose rate (μSv/h)
Results of the simplified formula agree with PHITS calculations within a factor of 3.
SPEAKER_NOTES:
Here is summary for calculation.
We don’t have enough time, I show you results.
We can see that in a Monte Carlo simulations with the same number of trials,
statistic uncertainty in t-point is much better than that in t-track.

According to Japanese law, The value at D3 should be less than the 3-month effective dose limit of 1.3 mSv.
Maximum usable time of source for 3-month is 1262 hours for DIN and 448 hours for PHITS.
We also see that results of the simplified formula agree with PHITS calculations within a factor of 3.

--- SLIDE 18 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Table of contents
1. Calculation of γ-ray streaming in concrete maze structures

2. Calculation of neutron shielding and air activation around the beam dump of a proton accelerator facility

3. Summary

--- SLIDE 19 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Purpose
In the shielding design of proton accelerator facilities, a simplified formula is used to calculate the neutron dose rate behind the shielding.

Let's compare the results of dose rates from the simplified equation and PHITS.

Let’s also calculate air activation around a beam dump.

--- SLIDE 20 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Neutron dose rate calculation using Tesch's  formula
Thickness of shielding material （g/cm2）
（density(g/cm3) x thickness of shield(cm)）
Used for point sources with proton energy less than 1 GeV
Beam loss rate（proton/sec）
Neutron dose equivalent at a distance of 1 m from the target (Sv m2/proton)
Dose equivalent attenuation lengths for concrete, 90-degree to proton beam（g/cm2）
Distance from source to evaluation point （m）
400 MeV, 250 kW proton beam is completely stopped by copper.
The value of Hcasc for 400 MeV is 2.00 x 10-15 (Sv m2/proton).
The value of λ for 400 MeV is 90 (g/cm2).
Thickness and density of concrete shield are 50 cm and 2.2 g/cm3
（Sv/sec）
400MeV, 250kW proton
Copper target
Air
Concrete, density 2.2 g/cm3
Let’s calculate the neutron dose rate (Sv/sec) on the concrete shield at 90 degree to the target center (r = 150cm) using the “Tesch” sheet in AnalyticalMethod.xlsx
K. Tesch, “A Simple Estimation of the Lateral Shielding for Proton Accelerators in the Energy Range
50 to 1000 MeV”, Radiation Protection Dosimetry, Vol.11 No.3, pp.165-172 (1985)
Calculation condition
SPEAKER_NOTES:
This slide shows Neutron dose rate calculation using Tesch's  formula used for point sources with proton energy less than 1 GeV.

--- SLIDE 21 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Neutron dose rate calculation using Tesch's  formula
（Sv/sec）
Let’s check the accuracy of this estimation using PHITS
SPEAKER_NOTES:
This is ansewer. I think you obtained the same dose rate.
Lets check it using PHITS.

--- SLIDE 22 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Flow of this lecture
Exercise 1: Check geometry
Exercise 2: Normal particle transport calculation
Exercise 3: Setting outer void for dump data
Exercise 4: Dump data production
Exercise 5: Shielding calculation using dump data as a source
Exercise 6: Shielding calculation using variance reduction method
Exercise 7: Air activation calculation
SPEAKER_NOTES:
This is flow of this lecture.
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 23 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Check geometry
yz-track.eps
[ T i t l e ]
・ ・ ・ ・ ・ ・
[Parameters]
icntl    =           8
maxcas   =        1000
maxbch   =          10
[Material]
$   Concrete   2.302 g/cm^3, taken from ANL-5800 Type 02-a
m1     H     -0.023
         C     -0.0023
         O     -1.22
         Na    -0.0368
         Mg    -0.005
         Al    -0.078
         Si    -0.775
         K     -0.0299
         Ca    -0.1
         Fe    -0.032

$   Air at ground level  1.21e-3 g/cm^3
m2      N   4.0586E-05
          O   1.0800E-05
         Ar   2.4255E-07
accelerator/accelerator.inp
SPEAKER_NOTES:
First step is to check geometry.
Lets move on accelerator folder. This input is composed of concrete, void, air, and copper target.
Lets execute PHITS to obtain this eps file. I think warning message will be appeard during execution of PHITS.
I will explain it next slide.
MENTIONED_INPUT_NAMES: accelerator.inp

--- SLIDE 24 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
High energy nuclear data library JENDL-4.0/HE
We recommend to use JENDL-4.0/HE to obtain more reliable shielding calculation results

PHITS package contains JENDL-4.0/HE only for H, C, N, O, Al, S, Fe, Cu, Pb

You may see the warnings in the left figure, but you can ignore them
JENDL-4.0/HE cannot be used for activation calculation because the activation cross section data are available only up to 20 MeV
https://rpg.jaea.go.jp/main/en/ACE-J40HE/index.html
Y. Iwamoto et al., J. Nucl. Sci. Technol. (2021) DOI: 10.1080/00223131.2021.1993372
→ See Iwamoto et al. 2021 in more detail
→ Data for other nuclides can be downloaded from the link below
[Parameters]
…
 dmax(1)  =  200.0  # (D=emin(1)) data max. energy of proton (MeV)
 dmax(2)  =  200.0  # (D=20.0) data max. energy of neutron (MeV)
Upper limit of JENDL-4.0/HE is 200 MeV
SPEAKER_NOTES:
Here I shows High energy nuclear data library JENDL-4.0/HE.
Now, dmax(1) and dmax(2) is 200 MeV. This means uppler limit of JENDL-4.0/HE is 200 MeV.

We recommend to use JENDL-4.0/HE to obtain more reliable shielding calculation results compared to the Physics model in PHITS.
If you are interested in using JENDL4.0/HE files, please see this paper in more detail after lecture.

Please note that PHITS package contains JENDL-4.0/HE only for these elements due to the huge size of data file..
So for more reliable simulation, Data for other nuclides can be downloaded from the link below.
You may see the warnings in the left figure, but you can ignore them.

And please note that JENDL-4.0/HE cannot be used for activation calculation because the activation cross section data are available only up to 20 MeV.
Later , we will learn the example of dchain calculations.

--- SLIDE 25 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1: Normal particle transport calculation
[Parameters]
icntl     =           0
maxcas   =        1000
maxbch   =          10

[ S o u r c e ]
 totfact = 250e3/400e6/1.602e-19
Basic calculation condition
Incident particle：
Geometry：
Tallies：
400 MeV proton pencil beam (s-type = 1)
Cylindrical copper with 10 cm thickness, concrete, air, and void
[t-track] for dose rate partial distribution, dose rate and energy spectrum at detector
[t-cross] for neutron energy distribution incident on upper concrete region and dump file production
[t-wwg] for automatic production of weight window for upper concrete area
#  num    reg     volume     neutron     r.err
 1      11   1.4137E+04   1.0838E+00  0.4665
yz-track.eps
dose-detector.out
Accelerator.inp
Output unit conversion (1/source)       (1/sec)
Let’s reduce the statistical uncertainty using various techniques
SPEAKER_NOTES:
This is Exercise 1: Normal particle transport calculation.
Here is basic calculation condition.

Incident particle is 400 MeV proton pencil beam.
Geometry is composed of Cylindrical copper with 10 cm thickness, concrete, air, and void.
These are tally information.
[t-track] for dose rate partial distribution, dose rate and energy spectrum at detector.
[t-cross] for neutron energy distribution incident on upper concrete region and dump file production.
[t-wwg] for automatic production of weight window for upper concrete area.

This is the normalization factor for output unit conversion from 1/source to 1/sec.
Lets execute phits.

We see that statistic uncertainty is large with this the history number.
Let’s reduce the statistical uncertainty using various techniques.
MENTIONED_INPUT_NAMES: Accelerator.inp
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 26 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Source with dump data
Concrete
Air
Proton beam
Details are in the manual and the folder,/phits/lecture/advanced/sourceB
PHITS can perform two-step calculation using information on particles coming into specified regions.
For example,
to study shielding effect changing thickness of concrete block.
Sources in the 2nd step.
You can perform calculations of the 2nd step many times changing the thickness of the concrete block.
In the 1st step, only one time calculation is performed, and
information on photons coming into the concrete is recorded.
SPEAKER_NOTES:
This slide shows Source with dump data.
PHITS can perform two-step calculation using information on particles coming into specified regions.

For example,
to study shielding effect changing thickness of concrete block.
In the 1st step, only one time calculation is performed, and information on neutrons coming into the lead is recorded as sources in the 2nd step.
You can perform calculations of the 2nd step many times changing the thickness of the lead block.

--- SLIDE 27 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
ID number of dump data
dump = -11
      1 2 3 4 5 6 7 8 9 18 19
Using dump parameters, you can set the data item and their order to output in the dump data file.
You can change this order

--- SLIDE 28 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2: Setting outer void for dump source
Set upper concrete region (cell 4) as outer void behind the air (positive side of y-axis).
In the [cell] section, outer void is defined by setting its material number = -1 (density is not needed).
Check the geometry by setting icntl=8.
To record information on particles passing through the air as dump data, set outer void behind the air (positive side of y-axis).
Dump region
(defined as outer void)
SPEAKER_NOTES:
Next is exercise 2, Setting outer void for dump source.

To record information on particles passing through the air as dump data, please set outer void behind the air (positive side of y-axis).
Set upper concrete region (cell 4) as outer void behind the air (positive side of y-axis).
In the [cell] section, outer void is defined by setting its material number = -1 (density is not needed).
Check the geometry by setting icntl=8.
ANSWER_FILE: accelerator/input/accelerator-3.inp

--- SLIDE 29 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Answer 2
[ T i t l e ]
・ ・ ・ ・ ・ ・
[Parameters]
icntl     =           8
maxcas   =        1000
maxbch   =          10
yz-track.eps
The white region denotes the outer void.
[Cell]
3 -8.90          -1
2    0          -2 4  -3
3    2 -1.21e-3 -5 #1 #2
$  4    1 -2.302   -6
 4   -1     -6
 5    1 -2.302   -7
11    2 -1.21e-3 -11

--- SLIDE 30 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3: Create dump source data
Enable the two [t-cross] sections. (The first one is for dump data, the second one is to check the spectrum of the stored data).
Run PHITS with icntl=0.
[ T - C r o s s ]
mesh =  reg
reg =    1            # number of crossing regions
      non     r-from  r-to       area
        1      3        4      400*400
......
       ne =   100            # number of e-mesh points
     unit =    1            # unit is [1/cm^2/source]
     axis =  eng            # axis of output
     file = cross_neutron.out
   output = flux            # surface crossing flux
     part =  neutron
   epsout =    0
   dump =   -11
1  2  3  4  5  6  7  8  9 18 19
Neutrons moving from cell 3 (air) to cell 4 (upper concrete) are dumped.
Contact area between cell 3 & 4
（Not necessary for creating dump file)
11 data are stored in ASCII format:
Particle information (1-9) and history information (18, 19)
Output the information on neutrons incident to the concrete shielding into dump source data file
SPEAKER_NOTES:
Exercise 3 is to create dump source data.
Output the information on neutrons incident to the concrete shielding into dump source data file.

At first, please Enable the two [t-cross] sections. The first one is for dump data, the second one is to check the spectrum of the stored data.
This is the first one.
Neutrons moving from cell 3 (air) to cell 4 (upper concrete) are dumped.
And this is Contact area between cell 3 & 4.
11 data are stored in ASCII format with Particle information (1-9) and history information (18, 19).
Lets Run PHITS with icntl=0.
ANSWER_FILE: accelerator/input/accelerator-4.inp

--- SLIDE 31 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Answer 3
yz-track.eps
cross_eng.out
Neutrons are scored and terminated at the surface between cells 3 & 4
（used for checking the statistical uncertainty of the stored data)
cross_neutron_dmp.out
cross_neutron.out
（used for 2nd step simulation)
SPEAKER_NOTES:
This is output from the first t-cross tally and output from the second one.
We can see that Neutrons are scored and terminated at the surface between cells 3 & 4.

We can see A normal tally file without "dmp" will be generated along with a dump file with "dmp" in the file name.

--- SLIDE 32 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4: Reduce the statistical uncertainty of Dump data
Obtain dump source data file with sufficient numbers of particle information
Increase “maxcas” and run PHITS again
maxcas   =        1000
maxbch   =          10
maxcas   =        5000
maxbch   =          10
Due to the time limitation of this lecture, maxcas=5000 (or less) depending on the speed of your computer
cross_eng.eps
SPEAKER_NOTES:
Exercise 4 is to reduce the statistical uncertainty of Dump data.

Lets Obtain dump source data file with sufficient numbers of particle information.
Increase “maxcas” and run PHITS again.
Due to the time limitation of this lecture, maxcas=5000 (or less) depending on the speed of your computer.
質問
How much statistics should I accumulate in the first step of the calculation?
The exact value is not known, as it depends on the conditions of the calculation. It is better to accumulate as many statistics as possible in the first stage of the calculation.
ANSWER_FILE: accelerator/input/accelerator-5.inp

--- SLIDE 33 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5: Transport simulation using dump data as the source
[ S o u r c e ]
s-type =   17
 idmpmode = 1
 file = cross_neutron_dmp.out
 dump = 0
Let’s perform the transport simulation using dump source data.
Create the new [source] section with s-type=17. (Set the old [source] section to be invalid by “off”.)
Set cell 4 to be concrete (material 1, density = 2.302 g/cm3) again
Set the [t-cross] section with dump parameters to be invalid by “off”.
[source] section with dump parameters (2nd step)
cross_neutron_dmp.out and
cross_neutron.out, are needed
In the case of idmpmode = 1, maxcas and maxbch written in the input file are ignored because they are taken from dump data (cross_neutron_dmp.out)
ANSWER_FILE: accelerator/input/accelerator-6.inp

--- SLIDE 34 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Answer 5
yz-track.eps
#  num    reg     volume     neutron     r.err
    1      11   1.4137E+04   7.3578E-01  0.2487
dose-detector.out
Reuse the same dumped source data for various shield thicknesses.
Proton beam interaction is skipped when sweeping shielding thickness in the 2nd step.
maxcas and maxbch are fixed in the 2nd step. If statistics is poor, increase in maxcas or maxbch in the 1st step. Istdev < 0 in the 1st step also works.

--- SLIDE 35 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6: Transport calculation using variance reduction technique
Example：track length tally
Weight： Importance of the particles in Monte Carlo simulation
	is always 1 in normal calculation*
Artificially increase the probability of rare event occurrences with changing weight of particle.
Frequency distribution per a history cannot be calculated,
   e.g. [t-deposit] with output = deposit
Li: track length of i-th particle
Wi: weight of i-th particle
n0: total history number
Concept of weight in Monte Carlo calculation
Details are in the manual and the folder,/phits/lecture/advanced/weightA, weightB
SPEAKER_NOTES:
Weight of particle is used in Monte Carlo calculation.
Weight is changed to improve efficiency of calculation  by variance reduction techniques.
ANSWER_FILE: accelerator/input/accelerator-end.inp

--- SLIDE 36 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6: Transport simulation using variance reduction technique
Let’s reduce the statistical uncertainty using [weight window]
Activate [T-WWG] and run PHITS for the 1st simulation
After creating WWG.out, activate infl: {WWG.out} and run PHITS for 2nd simulation
Weights are generated by dividing the area covering the upper concrete and a detector into 10 sections in the x, y, and z directions (100 sections in total).
[ T - WWG ]  off
   mesh = xyz
  y-type = 2
    ymin =  100
    ymax =  100+c2+2*c3
      ny = 10
  z-type = 2
    zmin = -200
    zmax =  200
      nz = 10
  x-type = 2
    xmin = -200
    xmax =  200
      nx =   10
   part = neutron
   e-type = 1
       ne = 2
     0    0.01   1e5
   axis   =  wwg
    file  =  WWG.out
Tally to automatically generate the optimal weight window range for each region.
Details are in the manual and the folder /phits/lecture/advanced/weightB
Output the value of the weight window for each region.
In the second calculation, use the value of the weight window obtained in the first calculation.
→delete
ANSWER_FILE: accelerator/input/accelerator-end.inp

--- SLIDE 37 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Answer 6
yz-track.eps (2nd simulation)
#  num    reg     volume     neutron     r.err
 1      11   1.4137E+04   7.0707E-01  0.2604
dose-detector.out
[Parameters]
 icntl    =           0
..........
$ infl: {WWG.out}
Delete→
In the 2nd simulation, use [weight window] obtained in the 1st simulation
Efficient calculations are possible using the variance reduction method.
However, the number of MC trials (maxcas x maxbch) cannot be increased when using Dump sources.
To increase the number of dump sources, the number of trials in the first step of the two-step calculation should be increased.
In this exercise, it is not increased due to time limitation.

--- SLIDE 38 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Summary of calculation
If the detector is located at the boundary of the controlled area, the evaluated value at this point should be less than 1.3 mSv, which is the effective dose limit for three months. Assuming 3 months as 500 hours, the effective dose rate must be less than 2.6 μSv/h.
Let’s complete the following table. Add error to PHITS dose rate.
Comparison of dose rate (Sv/sec)

--- SLIDE 39 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Summary of calculation
Let’s complete the following table. Add error to PHITS dose rate.
Comparison of dose rate (Sv/sec)
50 cm of concrete is totally inadequate
 (dose rate is about 109 times higher)
In actual shielding design, calculations must be repeated using simplified formulas and parallel calculations to determine the optimum shielding thickness
FYI: According to Tesch‘s formula, 1.1 μSv/h at dump-ceiling distance 1 m, and 800 cm concrete thickness
0.707 Sv/sec = 2.55 kSv/h is much higher than 2.6 μSv/h!!

--- SLIDE 40 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Air activation estimation
Activation due to neutrons produced by nuclear reactions in targets, etc.
Radionuclides originating from atoms in the air are produced by spallation reactions of N, O, and Ar, thermal neutron capture reactions, and so on.
H-3 (Half life 12.3year)
Be-7（ Half life 53day), C-11（ Half life 20min.)
N-13（ Half life 10min.), O-15（ Half life 2min.)
Ar-41（ Half life 1.8hour, Thermal neutron capture 40Ar(n,γ)）, and so on.
Generate an input file for DCHAIN and calculate neutron energy spectra and nuclide production from nuclear reactions using [t-dchain] in PHITS.
Calculate the radioactivity of nuclides during and after irradiation using DCHAIN.
Let’s calculate the radioactivity of these nuclides during and after irradiation.
Two Step Calculation Procedure
Nuclide production in DCHAIN
Activation cross section
Details are in the manual (/phits/dchain-sp/manual) and the folders (/phits/lecture/advanced/DCHAIN1, DCHAIN2), and (/phits/recommendation/DCHAIN).

--- SLIDE 41 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Exercise7: Air activation
Let's examine the air activation in region 3 when a 400 MeV, 250 kW proton beam is completely stopped at the copper target, irradiated for one day, and cooled for one day after irradiation.
[ T - D C H A I N ]
.........
    reg =  3
     file = air.out
  timeevo =    2
    1.0 d  1.0
    1.0 d 0.0
  outtime =    10
  1.0 h
    2.0 h
    6.0 h
   12.0 h
   1.0 d
   25 h
   26 h
   31 h
   1.5 d
   2.0 d
  amp=1
Beam output
1
0
Irradiation
Cooling
24h
48h
Output time
Volume of region 3 is 400 x 400 x 200 cm3.
Relationship between irradiation history (timevo) and output time (outtime)
Input file for DCHAIN
(1) Run PHITS with “activation/activation.inp" as input.
(2) Run DCHAIN with created "air.out" as input.
Region 3
air
[ S o u r c e ]
totfact = 250e3/400e6/1.602e-19
PHITS output unit conversion (1/source)→(1/sec)
In this case, amp=1 because it is defined in [source].
MENTIONED_INPUT_NAMES: activation.inp
ANSWER_FILE: accelerator/input/accelerator-end.inp

--- SLIDE 42 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Main output file (*.act)
Open the main output file (*.act) to check the radioactivity, decay heat, and dose rate of the produced nuclides!
<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>
 <>-<>   no.     1  regionwise calculation data     <>-<>
 <>-<>   region label : DUMMY001                    <>-<>
 <>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>
beam current ......  1.6022E-16 [mA]
beam energy .......  3.0000E+00 [GeV]
beam power ........  4.8066E-16 [MW]
neutron flux ...... 5.1994E+10 [n/cm**2/s]
region volume .....  3.1969E+07 [cm**3]
irradiation time ..          24 [h]
region number .....           3  (in nmtc yield file)

 --- output time ---         60 [m]   ( 3.6000000E+03 [s])
  nuclide         atoms     radioactivity                    relative        rate                decay heat [W/cc]                                      half-life   dose-rate
             [atoms/cc]      [Bq/cc]         [Bq]            error            [%]            beta       gamma          alpha          total                [s]  [uSv*m^2/h]
 H   3     1.4693E+08   2.6194E-01   8.3739E+06  6.2688E-01          2.388E-16  0.000E+00  0.000E+00  2.388E-16    3.888E+08   0.000E+00
 He  6     1.2360E-08   1.0620E-08   3.3950E-01  8.3851E-01          2.667E-21  0.000E+00  0.000E+00  2.667E-21    8.067E-01   0.000E+00
 Li  5     2.7133E-30   6.1288E-09   1.9593E-01  1.0004E+00          0.000E+00  0.000E+00  1.930E-21  1.930E-21    3.069E-22   0.000E+00
..............
・Information on the generated nuclides is output at each output time. Extract the information you want and use it.
・Information on the top 10 major nuclides is also available.
Produced activity
(Bq/cm3 & Bq)
Produced nuclide
Decay heat
(W/cm3)
Dose rate
(µSv*m2/hr)
air.act

--- SLIDE 43 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Drawing output file (*.eps)
Open the drawing output file (*.eps) to check the radioactivity, decay heat, and dose rate of the produced nuclides!
Time variation for radioactivity, decay heat (decay by beta, gamma, and alpha decay), and dose rate (effective dose or ambient dose equivalent H*(10))
Numerical data available in air.ang file.
IDOSECF=1, Effective dose according to ICRP103 (Source: ICRP116, default)
        =7, Ambient dose equivalent (Source: ICRP74)
The dose rate (μSv m2/hr) is given as the product of the photon emission rate of the nuclide and the dose conversion factor.
Dose conversion coefficients can be selected from ICRP103-compliant AP effective dose and ambient dose equivalent using IDOSECF parameter
air.eps

--- SLIDE 44 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Radioactivity time variation of major nuclides
! --- output option for ANGEL ---
  phitsout =   1
......
angelout_nuclides   = 4
O-15, Ar-41, Be-7, H-3
air.out
air.act
(1) Check the Top 10 major nuclides produced from air.act
(2) Add representative nuclides to the last line of air.out and run dchain
This time, we draw time variation of radioactivity of O-15, Ar-41, Be-7, and H-3.
dominant nuclides (top 10)
--- -------- Activity ------------------------------
no. nuclide     [Bq/cc]       [Bq]          rel. err.       [%]
    1   O  15   2.5913E+04 8.2841E+11 5.9010E-01  28.50
    2   N  13   2.2529E+04 7.2023E+11 5.7259E-01  24.78
    3   O  14   1.3238E+04 4.2321E+11 4.0690E-01  14.56
    4   C  11   1.2916E+04 4.1291E+11 2.5650E-01  14.21
    5   B   8   1.2203E+04 3.9011E+11 1.0000E+00  13.42
    6   C  10   2.6257E+03 8.3941E+10 2.9140E-01   2.89
    7   Ar 41   6.4660E+02 2.0671E+10 2.7185E-02   0.71
    8   N  16   5.6968E+02 1.8212E+10 2.6076E-02   0.63
    9   Be 11   1.3945E+02 4.4581E+09 2.7590E-01   0.15
   10   Be  7   8.7756E+01 2.8055E+09 2.5250E-01   0.10
dominant nuclides (top 10)
--- -------- Activity ------------------------------
no. nuclide     [Bq/cc]       [Bq]         rel. err.        [%]
1   C  11   1.6791E+03 5.3681E+10 2.5650E-01  65.49
2   Ar 41   4.4244E+02 1.4144E+10 2.7185E-02  17.26
3   N  13   3.4691E+02 1.1090E+10 5.7259E-01  13.53
4   Be  7   8.7709E+01 2.8040E+09 2.5250E-01   3.42
5   H   3   6.2860E+00 2.0096E+08 6.2688E-01   0.25
Immediately after irradiation (output time: 24 hours), lines648
After 1hour after irradiation (output time: 25 hours), lines754

--- SLIDE 45 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Radioactivity time variation of major nuclides
air.eps
The minimum value on the vertical axis is 105 [Bq].
Open air.ang and add ymin(1e5) at line 18
                  p: xlin ylog ymin(1e5)
Run drawing program angel with air.ang as input
Open the rendering output file (*.eps) to check the radioactivity of major nuclides.
Change the range of the vertical axis to make the figure easier to understand.

--- SLIDE 46 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Radioactivity time variation of major nuclides
air.eps
Open the drawing output file (*.eps) and check the time variation of radioactivity of major nuclides!
Ar-41,O-15, etc. cannot be trapped by filters .
Operation by confining (circulating) the air in the accelerator room.
Operation by constantly replacing the air when the concentration in the air during operation does not exceed 1/10 of the legal value.
Example: 1/10 of concentration limit (Bq/cm3): 2e-2(O-15), 1e-2(Ar-41)
This time, air confinement operation is mandatory based on the results on page 44: 2.59e4(O-15), 6.47e2(Ar-41).
Be-7 exists as a radioactive aerosol and is filtered out when released.
H-3 exists in the chemical form of HTO and HT and is released into the atmosphere.

--- SLIDE 47 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Table of contents
1. Calculation of γ-ray streaming in concrete maze structures

2. Calculation of neutron shielding and air activation around the beam dump of a proton accelerator facility

3. Summary

--- SLIDE 48 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Summary
“Dose” evaluated in shielding design is either “ambient dose” or “effective dose” calculated by [t-track] or [t-point] with the multiplier function
2-step calculation using dump source file, and variance reduction methods are beneficial for reducing the computational time
Activation calculation is feasible by combining PHITS and DCHAIN.
The actual licensing application may consider facility-specific safety likelihood (factor of about 2) due to the systematic uncertainties of the PHITS simulation results.
This lecture note is based on the Japanese regulation,
and you have to check the regulation of your own country

--- SLIDE 01 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
放射線遮蔽計算
2023年3月更新
phits/lecture/advanced/shielding
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
本実習の目標
PHITSの計算機能を活用して、様々な施設の放射線遮蔽設計を行えるようになる。
コンクリートの迷路構造におけるγ線ストリーミング計算
陽子加速器施設のビームダンプ周辺における中性子遮蔽と空気の放射化計算

--- SLIDE 03 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
内容
1. コンクリートの迷路構造におけるγ線ストリーミング計算

2. 陽子加速器施設のビームダンプ周辺における中性子遮蔽と空気の放射化計算

3. まとめ

--- SLIDE 04 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
目的
放射線同位元素使用施設における遮蔽設計において、線量率を求める簡易式が利用されている。

遮蔽計算で有用となるPHITSの計算機能を使って、PHITSと簡易式による線量率の結果を比較しよう。

--- SLIDE 05 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
簡易式による線量率の計算
ドイツ工業規格(DIN)の屈曲角度90度の2回屈曲ダクト出口におけるγ線ストリーミングの線量率計算式を用いて、P0～P3の線量（D0～D3）を求めよう。
Auslegung von Zweifach Gekickten Gasgefullten in Abschirm Wanden aus Beton gegen Gammastrahlung. DEUTSCHE NORMMEN, DIN 25-427 Teil 1,2 (1977).
実効線量率定数(μSvh-1MBq-1m2)
192Irの場合、0.117*
線源強度                    (MBq)
実効的なダクト幅
(m)
補正係数 1.5**（屈曲部のエッジを透過する放射線の効果）
屈曲部での実効的な散乱係数
0.08**
*出典：アイソトープ手帳
**出典：放射線遮へいハンドブック
AnalyticalMethod.xlsxのDINシートの水色セルに幾何学形状の条件を入力

--- SLIDE 06 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
簡易式による線量率の計算結果
P3を管理区域境界とすると、この地点における評価値が、3月間の実効線量限度値1.3mSvを下回る必要がある
3月間の線源利用可能な最大時間は、1.3mSv/1.03(μSv/h)=1262時間となる
3月間の使用時間が上記時間を超えないよう、本線源を使用施設外の貯蔵箱に保管する必要がある
例：3月間を13週間（2184時間）と想定して合計922時間、貯蔵箱に保管する
PHITSによる結果と比較してみよう

--- SLIDE 07 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
本実習の流れ
課題１: 線源の確認
課題２: [t-track]による実効線量率の計算
課題３: [t-point]による実効線量率の計算
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 08 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
PHITSを遮蔽計算に適用する際の注意点
遮蔽計算で計算する線量は、[t-deposit]で計算する吸収線量ではなく、[t-track]（もしくは[t-point]）にmultiplier機能を使って計算する周辺線量当量や実効線量
計算時間短縮が重要となるため、イベントジェネレータモードや電子輸送は不要
施設内全ての場所に対してPHITSで遮蔽計算をするのは現実的でなく、簡易式とPHITSを組み合わせて実施することが重要

--- SLIDE 09 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
計算体系の確認
P1
P2
P3
1m
1.5m
3m
1.5m
高さ2m
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 8
計算体系の確認
200GBqの192Ir線源
コンクリート壁
第1脚
第2脚
第3脚
0.8m
[Material]
$   Concrete   2.302 g/cm^3, taken from ANL-5800 Type 02-a
m1     H     -0.023
         C     -0.0023
         O     -1.22
         Na    -0.0368
         Mg    -0.005
         Al    -0.078
         Si    -0.775
         K     -0.0299
         Ca    -0.1
         Fe    -0.032

$   Air at ground level  1.21e-3 g/cm^3
m2      N   4.0586E-05
          O   1.0800E-05
         Ar   2.4255E-07
空気
xz-track.eps
maze/maze.inp
MENTIONED_INPUT_NAMES: maze.inp

--- SLIDE 10 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１: 線源の確認
核種：イリジウム 192 (192Ir)
放射能：200 GBq
icntl = 5として線源のエネルギースペクトルと方向を確認しよう
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 5
修正して実行（反応なしモード）
maze.inp
[ S o u r c e ]
   s-type =   1
     proj =  photon
......

   e-type =  28
       ni =   1
Ir-192    200e9
norm =   0
指定するRIの数
RIと放射能（単位はBq）
規格化のオプション
 0: (/sec) （初期値）
 1: (/source)
RI線源機能の利用
MENTIONED_INPUT_NAMES: maze.inp
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 11 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１の解答
全ての物質がvoidとなるため，まっすぐに飛んでいく
192Irから複数のγ線が放出されている。
track_xz.eps
p1-ene.eps
グラフの単位は[1/cm2/source]だが，実際には[1/cm2/sec]で出力されている。
P1
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 12 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
実効線量率への換算
[ T - T r a c k ]
…
 multiplier = all
…
      mat              mset1
   all    ( 3600*1e-6 -202 )
[t-track]や[t-point]で計算したフルエンスは、格納もしくは[multiplier]セクションで定義した複数の関数と掛け合わせることができる
(C k): C 規格化定数, k ID番号
フルエンスを線源強度で規格化したとき、(pSv)単位で線量を導出
/phits/data/multiplier/フォルダに
格納されている線量換算係数データ一覧の抜粋
実効線量率（μSv/h)にするため、規格化定数Cに値を代入。
フルエンス率(1/cm2/sec) x 線量換算係数(pSv・cm2) x 3600(sec/h) x 1e-6(μ/pico)
=実効線量率（μSv/h)
線源強度
線量換算係数*
*現行の日本の法令はICRP60準拠だが、今回はICRP103定義に基づく値を利用

--- SLIDE 13 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題２: [t-track]による実効線量率の計算
[ T i t l e ]
・ ・ ・ ・ ・ ・
[ P a r a m e t e r s ]
   icntl = 0
 maxcas   =        100000
 maxbch   =          10
[T-Track]
  title =  dose rate at p1, p2, p3
    mesh = reg
    reg = 11 12 13
  e-type = 2
    emin = 0
    emax =  100
      ne = 1
  axis = reg
  file = dose-track.out
  part = photon
  unit = 1
  z-txt = Effective dose rate
multiplier =all
emax = 1000
mat mset1
all ( 3600*1e-6 -202 )
半径15cmの球
xz-track.eps
P1
P2
P3
dose-track.out
修正して実行（通常モード）
P1
P2
P3
迷路の深い地点で統計誤差が極めて大きい
[t-point]を用いて効率的に線量率を求めよう
10に変更
検出器P1-P3における線量率を求めよう
h:   x      n     n          y(photon  ),l3   n
#  num    reg     volume     photon      r.err
    1      11   1.4137E+04   6.0184E+03  0.0394
    2      12   1.4137E+04   5.3274E+01  0.2712
    3      13   1.4137E+04   5.0319E+00  0.7095
ANSWER_FILE: accelerator/input/accelerator-3.inp

--- SLIDE 14 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
[t-point]
ある点(point detector) やリング状の線分(ring detector) におけるフルエンスを計算
通常、設定した領域に確率的に入ってくる放射線をタリーするため、タリー領域が小さくなると、十分な統計精度を得るためには極めて長い計算時間を要する。
[t-point] タリーは、[t-track] タリーの手法とは異なり、線源位置、もしくは、散乱によって粒子が発生した地点で、タリー位置への方向確率と透過確率を計算して評価することができるため、粒子の存在確率が小さい領域での測定に有効に機能。
ただし、散乱点での生成粒子の角度分布、エネルギー分布があらかじめ分かっていないと評価できない。
物質中での荷電粒子のエネルギー損失があると透過確率の評価が難しいので、対象粒子は、断面積ライブラリの存在する中性子と光子に限られる。
利用条件
(1) 輸送計算の上限エネルギーは、ライブラリを使う上限エネルギー(dmax) とする
(2) 検出可能な粒子は中性子・光子のみとする
(3) Event Generator mode 及びEGS5 mode を使用しない
(4) 面定義で全反射や白色反射の面を利用しない
詳細は、マニュアル、及び\phits\utility\tpoint フォルダを参照

--- SLIDE 15 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題３: [t-point]による実効線量率の計算
[ T-point ] off
point = 3
non  x         y    z               r0
1     200      0    -200         1.0
2     200-c7  0    -200         1.0
  200-c7  0   -200-150   1.0

・ ・ ・ ・ ・ ・
dose-point.out
[t-track]の結果に比べて、統計誤差が良くなる。
ポイントを指定する座標
架空の球の半径(cm)
詳細は\phits\utility\tpoint\readme-jp.docxを参照
Point detectorの数。上限数は20
#  e-lower      e-upper          photon          r.err
 0.0000E+00   1.0000E+02   6.1787E+03  0.0029
・ ・ ・ ・ ・ ・
 0.0000E+00   1.0000E+02   6.0227E+01  0.0165
・ ・ ・ ・ ・ ・
 0.0000E+00   1.0000E+02   2.9032E+00  0.0906
・ ・ ・ ・ ・ ・
[t-point]を有効化してPHITS計算を再実行
ANSWER_FILE: accelerator/input/accelerator-4.inp

--- SLIDE 16 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
計算値のまとめ
以下の表を完成させよう。PHITSの線量率（μSv/h)は、誤差も記載。
PHITSのモンテカルロ試行回数は、以下の通り。
maxcas   =        100000
maxbch   =          10
3月間の線源利用可能な最大時間Tmax  = 1300 / D3
D3の評価値が、3月間の実効線量限度値1.3mSvを下回る必要がある

--- SLIDE 17 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
計算値のまとめ
PHITSのモンテカルロ試行回数は、以下の通り。
 maxcas   =        100000
 maxbch   =          10
3月間の線源利用可能な最大時間Tmax  = 1300 / D3
以下の表を完成させよう。PHITSの線量率（μSv/h)は、誤差も記載。
簡易式の結果はPHITSの計算値とファクター3以内で一致。
D3の評価値が、3月間の実効線量限度値1.3mSvを下回る必要がある

--- SLIDE 18 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
内容
1. コンクリートの迷路構造におけるγ線ストリーミング計算

2. 陽子加速器施設のビームダンプ周辺における中性子遮蔽と空気の放射化計算

3. まとめ

--- SLIDE 19 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
目的
陽子加速器施設における遮蔽設計において、天井の遮蔽体透過後の中性子線量率を求める簡易式が利用されている。

簡易式とPHITSによる線量率の結果を比較しよう。

ビームダンプ周辺の空気の放射化を計算しよう。

--- SLIDE 20 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Tesch の点状線源の式による中性子線量率計算
遮へい体の厚さ（g/cm2）
（密度(g/cm3)×遮へい体厚さ(cm)）
陽子エネルギーが1GeV未満の点状線源に対して使用するTeschの式
ビーム損失率（proton/sec）
ターゲットから1 m の位置での入射陽子１個当たりの中性子線量当量(Sv m2/proton)
90 度方向減弱距離（g/cm2）
線源から計算点までの距離（m）
（Sv/sec）
AnalyticalMethod.xlsxのTeschシートの水色セルに条件を入力して中性子線量率を求めよう
K. Tesch, “A Simple Estimation of the Lateral Shielding for Proton Accelerators in the Energy Range
50 to 1000 MeV”, Radiation Protection Dosimetry, Vol.11 No.3, pp.165-172 (1985)
400MeV, 250kWの陽子ビームが銅で完全に止まる状況を想定
400MeV に相当するHcasc の値は2.00×10-15 (Sv m2/proton)
400MeV に相当するλの値は90 (g/cm2)
コンクリートは厚さ50cm、密度2.2 (g/cm3)と仮定し、評価点はコンクリートの直後（線源から1.5mの地点）とする

--- SLIDE 21 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Tesch の点状線源の式による中性子線量率計算
（Sv/sec）
PHITSによる結果と比較してみよう。

--- SLIDE 22 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
本実習の流れ
課題 1:通常の粒子輸送計算を実行
課題 2: Dump data作成のための外部ボイドの設定
課題 3: Dump data作成
課題 4: Dump dataの統計誤差を小さくする
課題 5: Dump dataを線源とした遮蔽計算
課題 6: 分散低減法を用いた輸送計算
課題 7: 空気の放射化計算
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 23 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
計算体系の確認
[ T i t l e ]
・ ・ ・ ・ ・ ・
[Parameters]
icntl    =           8
maxcas   =        1000
maxbch   =          10
[Material]
$   Concrete   2.302 g/cm^3, taken from ANL-5800 Type 02-a
m1     H     -0.023
         C     -0.0023
         O     -1.22
         Na    -0.0368
         Mg    -0.005
         Al    -0.078
         Si    -0.775
         K     -0.0299
         Ca    -0.1
         Fe    -0.032

$   Air at ground level  1.21e-3 g/cm^3
m2      N   4.0586E-05
          O   1.0800E-05
         Ar   2.4255E-07
yz-track.eps
accelerator/accelerator.inpを実行して計算体形を確認

--- SLIDE 24 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
高エネルギー核データライブラリJENDL-4.0/HE
高エネルギー加速器の遮蔽計算には、より計算精度の高いJENDL-4.0/HEを用いることを奨励

PHITSパッケージには、H, C, N, O, Al, S, Fe, Cu, Pbに対するJENDL-4.0/HEが格納されている

JENDL-4.0/HEがない核種を使っている場合、左図のようなwarningが出るが、無視してよい
JENDL-4.0/HEは、現在のところ、放射化計算には使えない
https://rpg.jaea.go.jp/main/en/ACE-J40HE/index.html
Y. Iwamoto et al., J. Nucl. Sci. Technol. (2021) DOI: 10.1080/00223131.2021.1993372
→ベンチマーク結果は下記論文参照
→それ以外の核種は下記URLからダウンロード
[Parameters]
…
 dmax(1)  =  200.0  # (D=emin(1)) data max. energy of proton (MeV)
 dmax(2)  =  200.0  # (D=20.0) data max. energy of neutron (MeV)
JENDL-4.0/HEの上限エネルギーは200MeV
→DCHAIN用の放射化断面積ライブラリが20MeVまでしか整備されていないため

--- SLIDE 25 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１: 通常の粒子輸送計算を実行
[Parameters]
icntl     =           0
maxcas   =        1000
maxbch   =          10

[ S o u r c e ]
 totfact = 250e3/400e6/1.602e-19
基本計算条件
入射粒子：
体系：
タリー：
400 MeV陽子のペンシルビーム（s-type=1）
円柱状の銅（厚さ10cm）、コンクリート、空気、真空
[t-track]による線量率空間分布、検出器における線量率とエネルギー分布
[t-cross]による上部コンクリート領域へ入射する中性子エネルギー分布とダンプファイル作成
[t-wwg]による上部コンクリート領域のウェイトウィンドウ自動作成
#  num    reg     volume     neutron     r.err
    1      11   1.4137E+04   1.0838E+00  0.4665
dose-detector.out
Accelerator.inp
出力単位変換
(1/source)       (1/sec)
効率良く計算を行ってみよう
yz-track.eps
MENTIONED_INPUT_NAMES: Accelerator.inp
ANSWER_FILE: accelerator/input/accelerator-2.inp

--- SLIDE 26 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Dump dataを用いた線源
指定した領域に入射した放射線の情報を蓄え、それを線源とした2段階計算をすることができる
空気の部分を通過した位置に遮へい体を置き、その厚さを変えながら遮へい効果を調べたい
コンクリート
空気
1段階目の計算では1度だけPHITSを実行し、
コンクリートに入射する中性子の情報を記録する
2段階目の計算の線源
コンクリートの厚さを変えて、
2段階目の計算を何度も行うことが可能
陽子ビーム
詳細は、マニュアル、及び /phits/lecture/advanced/sourceB を参照

--- SLIDE 27 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Dump定義文
dump = -11
      1 2 3 4 5 6 7 8 9 18 19
Dump定義文によって、dump dataとして出力するデータの種類と順番を指定します
順番を変えることもできる

--- SLIDE 28 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題２: Dump data作成のための外部ボイドの設定
空気の部分を通過した粒子の情報をdump dataとして蓄えるため、上部のコンクリート部分（y軸の正の側）を外部ボイドとして設定しましょう
Dump領域 上部コンクリート
（外部ボイドとして定義）
上部コンクリートの領域を外部ボイドとして定義する（セル番号4）
[cell]セクションにおいて外部ボイドとして設定する場合は、物質番号の箇所を-1とする（密度の項目は必要ない）
icntl=8として体系を確認する
ANSWER_FILE: accelerator/input/accelerator-3.inp

--- SLIDE 29 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題２の解答
[ T i t l e ]
・ ・ ・ ・ ・ ・
[Parameters]
icntl     =           8
maxcas   =        1000
maxbch   =          10
[Cell]
3 -8.90          -1
2    0          -2 4  -3
3    2 -1.21e-3 -5 #1 #2
$  4    1 -2.302   -6
 4   -1     -6
 5    1 -2.302   -7
11    2 -1.21e-3 -11
Dump領域 上部コンクリート
（外部ボイドとして定義）
yz-track.eps
外部ボイドの領域は白で表示される
ANSWER_FILE: accelerator/input/accelerator-3.inp

--- SLIDE 30 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題３: Dump data作成
中性子が外部ボイド（コンクリート）に入る直前の情報をdump dataに蓄えてみよう
２つの[t-cross]セクションを有効にする。（1つ目はdump data用で、2つ目は蓄えたdataが十分かどうかを調べるため）
icntl=0としてPHITSを実行
[ T - C r o s s ]
mesh =  reg
reg =    1            # number of crossing regions
      non     r-from  r-to       area
        1      3        4      400*400
......
       ne =   100            # number of e-mesh points
     unit =    1            # unit is [1/cm^2/source]
     axis =  eng            # axis of output
     file = cross_neutron.out
   output = flux            # surface crossing flux
     part =  neutron
   epsout =    0
   dump =   -11
1  2  3  4  5  6  7  8  9 18 19
セル3(空気)からセル4(上部コンクリート)に移動する中性子をdumpする
(areaはdumpするためだけなら設定不要）
蓄積するデータは９種類の粒子情報（粒子種・位置・方向ベクトル・エネルギー・ウェイト）とイベント番号[番号18]とバッチ番号[番号19]の合計11種類
ANSWER_FILE: accelerator/input/accelerator-4.inp

--- SLIDE 31 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
yz-track.eps
cross_eng.eps
セル3(空気)からセル4(上部コンクリート)に移動する中性子をdumpする。
（dumpデータの統計誤差確認用）
cross_neutron_dmp.out
cross_neutron.out
課題３の解答
（２段階目の線源データとして利用）
ANSWER_FILE: accelerator/input/accelerator-4.inp

--- SLIDE 32 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題4: Dump dataの統計誤差を小さくする
線源として十分な量のdump dataを作成しましょう
maxcasを増やしてdump data量を大きくする
maxcas   =        1000
maxbch   =          10
maxcas   =        5000
maxbch   =          10
本講習時間の制限上、maxcas=5000とする。計算時間の掛かる方は、もう少し小さくても問題ありません
cross_eng.eps
ANSWER_FILE: accelerator/input/accelerator-5.inp

--- SLIDE 33 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5: Dump dataを線源とした遮蔽計算
Dump dataを線源とした輸送計算を実行しよう
s-type=17を用いる新しい[source]セクションを有効にする（陽子を線源とする方はoffにする）
セル番号4の領域をコンクリート（物質番号1、密度2.302g/cm3)に戻す
2つの[t-cross]はoffにする
計算が完了したら、yz-track.epsとdose-detector.outを確認する
dumpデータを用いた[source]セクションの入力形式
[ S o u r c e ]
s-type =   17
 idmpmode = 1
     file = cross_neutron_dmp.out
    dump = 0
cross_neutron_dmp.outと
cross_neutron.outが必要
idmpmode = 1の場合、1段階目の計算結果(cross_neutron.out）から自動的に１段階目のmaxcasとmaxbchを読み込む（2段階目のmaxcasとmaxbchは無視される）
ANSWER_FILE: accelerator/input/accelerator-6.inp

--- SLIDE 34 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題5の解答
yz-track.eps
#  num    reg     volume     neutron     r.err
    1      11   1.4137E+04   7.3578E-01  0.2487
dose-detector.out
同じDump data線源を用いて、様々な厚さの遮蔽体に対する計算が可能
2段階目計算では陽子入射核反応計算を行わないため、効率的な計算が可能
2段階目計算では試行回数は変更できないので、１段階目の試行回数はできるだけ多い方が良い。 足りない場合は1段階目計算で再開始計算機能を使ってダンプを拡充すること。
ANSWER_FILE: accelerator/input/accelerator-6.inp

--- SLIDE 35 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
Step6: 分散低減法を用いた輸送計算
例：track length タリー
ウェイト： モンテカルロ計算における粒子の重要度、通常の計算は１*。

ウェイトを操作して、統計上発生しにくいイベントを人為的に発生させる。

ただし、ウェイトを操作した場合、ヒストリー毎の頻度分布（[t-deposit], output = depositなど）の計算ができなくなるので注意が必要。
Li: i番目の粒子の軌跡長さ
Wi: i番目の粒子のウェイト
n0: 総ヒストリー数
モンテカルロ計算におけるWeightの概念
詳細は、マニュアル、及び /phits/lecture/advanced/weightA, weightB を参照

--- SLIDE 36 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題6: 分散低減法を用いた輸送計算
Weight Window機能を用いて統計誤差を小さくしよう
[T-WWG]を有効にして、１回目のPHITSを実行
infl: {WWG.out}コマンドを有効にして、WWG.outを読み込んだ２回目のPHITSを実行
上部コンクリートと検出器をカバーする領域を、x,y,z方向に10分割（合計100分割）して、ウェイトを生成
[ T - WWG ]  off
   mesh = xyz y-type = 2
    ymin =  100
    ymax =  100+c2+2*c3
      ny = 10
  z-type = 2
    zmin = -200
    zmax =  200
      nz = 10
  x-type = 2
    xmin = -200
    xmax =  200
      nx =   10
   part = neutron
   e-type = 1
       ne = 2
     0    0.01   1e5
   axis   =  wwg
    file  =  WWG.out
詳細は、マニュアル、及び /phits/lecture/advanced/weightB を参照
各領域の最適なウェイトウィンドウの値を自動で生成するタリー
各領域のウェイトウィンドウの値を出力
2回目の計算で、1回目の計算で得たweight windowの値を用いる。
消す
ANSWER_FILE: accelerator/input/accelerator-end.inp

--- SLIDE 37 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題6の解答
yz-track.eps（２回目の結果）
#  num    reg     volume     neutron     r.err
 1      11   1.4137E+04   7.0707E-01  0.2604
dose-detector.out
[Parameters]
 icntl    =           0
..........
$ infl: {WWG.out}
消す
2回目の計算結果
（1回目の計算で得たweight windowの値を読み込む）
分散低減法を用いて効率的に計算可能
ただし、Dump線源利用の場合、モンテカルロ試行回数(maxcas x maxbch)は増やせない
Dump線源の数を増やすため、２段階計算の１段階目の試行回数は多い方が良い
本実習では時間制限のため、増やさない
ANSWER_FILE: accelerator/input/accelerator-end.inp

--- SLIDE 38 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
計算値のまとめ
以下の表を完成させよう。PHITSの線量率は、誤差も記載。
検出器位置を管理区域境界とすると、この地点における評価値が、3月間の実効線量限度値1.3mSvを下回る必要がある。3月間を500時間として想定すると、2.6μSv/hを下回る必要がある。
検出器位置における線量率（Sv/sec)の比較

--- SLIDE 39 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
計算結果
50 cmのコンクリートでは全く不十分（線量率が約109倍高い）
参考：Teschの式によると、ダンプ-天井距離1m, 800cmのコンクリート厚さで1.1μSv/h
実際の遮蔽設計では、簡易式や並列計算を活用して計算を繰り返し、最適な遮蔽体の厚さを決定する必要があります
検出器位置における線量率（Sv/sec)の比較
2.55 kSv/hに相当するので2.6μSv/hよりはるかに高い

--- SLIDE 40 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
空気の放射化計算
ターゲットなどで核反応が生じ、中性子が発生することによる放射化
空気中の原子を起源とするものについては、
Ｎ、Ｏ、Ａｒの核破砕反応、熱中性子捕獲反応等により生成する
Ｈ-3 (半減期１２.３年)
Ｂｅ-7（半減期５３日) 、 Ｃ-11（半減期２０分) 、
Ｎ-13（半減期１０分) 、 Ｏ-15（半減期２分) 、
Ａｒ-41（半減期１．８時間、熱中性子捕獲Ar-40(n,γ)）等がある。
①PHITSの[t-dchain]を用いて、DCHAINの入力ファイル生成、核反応による中性子エネルギースペクトルや核種生成を計算する。
②上記結果とDCHAINを用いて、照射中、及び照射後の核種の放射能を計算する。
PHITSと放射化計算コードDCHAINを用いて、照射中、及び照射後のこれら核種の放射能を調べよう。
＊詳細は、マニュアル(\phits\dchain-sp\manual)、例題（\phits\lecture\advanced\DCHAIN1、DCHAIN2)
（\phits\recommendation\DCHAIN)を参照してください。
放射化計算の手順
DCHAINにおける核種生成量
放射化断面積

--- SLIDE 41 ---
PPTX_FILE: PHITS-shielding-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
課題7: 空気の放射化計算
400MeV, 250kWの陽子ビームが銅ターゲットで完全に止まるとき、１日照射、照射後１日冷却したときの、領域３における空気の放射化を調べよう。
[ T - D C H A I N ]
.........
    reg =  3
     file = air.out
  timeevo =    2
    1.0 d  1.0
    1.0 d 0.0
  outtime =    10
  1.0 h
    2.0 h
    6.0 h
   12.0 h
   1.0 d
   25 h
   26 h
   31 h
   1.5 d
   2.0 d
  amp=1
ビーム出力
1
0
照射
冷却
24h
48h
出力時間
領域３の体積を400 x 400 x 200 cm3とする
照射履歴(timeevo)と出力時間(outtime)の関係
DCHAINの入力ファイル
→DCAHINを実行
① ”activation/activation.inp”を入力として、 PHITSを走らせよう
② 出力された”air.out”を入力として、DCHAINを走らせよう
領域３
[ S o u r c e ]
totfact = 250e3/400e6/1.602e-19
PHITSの出力単位変換(1/source)→(1/sec)
今回は[source]で定義しているため、amp=1とする。
MENTIONED_INPUT_NAMES: activation.inp
ANSWER_FILE: accelerator/input/accelerator-end.inp

--- SLIDE 42 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
主な出力ファイル(*.act)
主な出力ファイル(*.act)を開いて、生成核種の放射能、崩壊熱、線量率を確認しよう
<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>
 <>-<>   no.     1  regionwise calculation data     <>-<>
 <>-<>   region label : DUMMY001                    <>-<>
 <>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>
beam current ......  1.6022E-16 [mA]
beam energy .......  3.0000E+00 [GeV]
beam power ........  4.8066E-16 [MW]
neutron flux ...... 5.1994E+10 [n/cm**2/s]
region volume .....  3.1969E+07 [cm**3]
irradiation time ..          24 [h]
region number .....           3  (in nmtc yield file)

 --- output time ---         60 [m]   ( 3.6000000E+03 [s])
  nuclide         atoms     radioactivity                    relative        rate                decay heat [W/cc]                                      half-life   dose-rate
             [atoms/cc]      [Bq/cc]         [Bq]            error            [%]            beta       gamma          alpha          total                [s]  [uSv*m^2/h]
 H   3     1.4693E+08   2.6194E-01   8.3739E+06  6.2688E-01          2.388E-16  0.000E+00  0.000E+00  2.388E-16    3.888E+08   0.000E+00
 He  6     1.2360E-08   1.0620E-08   3.3950E-01  8.3851E-01          2.667E-21  0.000E+00  0.000E+00  2.667E-21    8.067E-01   0.000E+00
 Li  5     2.7133E-30   6.1288E-09   1.9593E-01  1.0004E+00          0.000E+00  0.000E+00  1.930E-21  1.930E-21    3.069E-22   0.000E+00
..............
・出力時間毎に、生成核種の情報が出力される。欲しい情報を抜き出して利用する。
・主要な生成核種top10の情報もある。
領域（セル）番号
照射時間
領域の体積
中性子フラックス
出力時間
生成放射能(Bq/cm3 & Bq)
生成核種
崩壊熱
(W/cm3)
線量率(µSv*m2/hr)
air.act

--- SLIDE 43 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
描画出力ファイル(*.eps)
描画ファイル(*.eps)を開いて、生成核種の放射能、崩壊熱、線量率を確認しよう
air.eps
放射能、崩壊熱（ベータ線、ガンマ線、α線崩壊による崩壊）、線量率（実効線量または周辺線量当量H*(10))の時間変化
air.angファイルに数値データあり
線量率(μSv m2/hr)は、核種の光子放出率と線量換算係数の積として与えられる。
線量換算係数は、IDOSECFパラメータによりICRP103準拠のAP照射実効線量と周辺線量当量から選択可能
IDOSECF=1, ICRP103準拠の実効線量 （出典：ICRP116、デフォルト）
      =7, 周辺線量当量（出典：ICRP74）

--- SLIDE 44 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
主要核種の放射能時間変化
! --- output option for ANGEL ---
  phitsout =   1
......
angelout_nuclides   = 4
O-15, Ar-41, Be-7, H-3
air.out
air.act
①air.actから主要な生成核種Top10を確認
②代表的な核種をair.outの最後の行に追加して、dchainを実行
今回、O-15, Ar-41, Be-7, H-3の放射能時間変化を描画する。
dominant nuclides (top 10)
--- -------- Activity ------------------------------
no. nuclide     [Bq/cc]       [Bq]          rel. err.       [%]
    1   O  15   2.5913E+04 8.2841E+11 5.9010E-01  28.50
    2   N  13   2.2529E+04 7.2023E+11 5.7259E-01  24.78
    3   O  14   1.3238E+04 4.2321E+11 4.0690E-01  14.56
    4   C  11   1.2916E+04 4.1291E+11 2.5650E-01  14.21
    5   B   8   1.2203E+04 3.9011E+11 1.0000E+00  13.42
    6   C  10   2.6257E+03 8.3941E+10 2.9140E-01   2.89
    7   Ar 41   6.4660E+02 2.0671E+10 2.7185E-02   0.71
    8   N  16   5.6968E+02 1.8212E+10 2.6076E-02   0.63
    9   Be 11   1.3945E+02 4.4581E+09 2.7590E-01   0.15
   10   Be  7   8.7756E+01 2.8055E+09 2.5250E-01   0.10
dominant nuclides (top 10)
--- -------- Activity ------------------------------
no. nuclide     [Bq/cc]       [Bq]         rel. err.        [%]
1   C  11   1.6791E+03 5.3681E+10 2.5650E-01  65.49
2   Ar 41   4.4244E+02 1.4144E+10 2.7185E-02  17.26
3   N  13   3.4691E+02 1.1090E+10 5.7259E-01  13.53
4   Be  7   8.7709E+01 2.8040E+09 2.5250E-01   3.42
5   H   3   6.2860E+00 2.0096E+08 6.2688E-01   0.25
照射終了時(出力時間：24時間)
照射終了１時間後 (出力時間：25時間)

--- SLIDE 45 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
主要核種の放射能時間変化
air.eps
縦軸の最小値を105 [Bq}とする。
air.angを開いて、18行目にymin(1e5)を追加
                 p: xlin ylog ymin(1e5)
air.angを入力として描画プログラムangelを実行
描画出力ファイル(*.eps)を開いて、主要核種の放射能の時間変化を確認しよう
縦軸の範囲を変更して、図をわかりやすくする。

--- SLIDE 46 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
主要核種の放射能時間変化
長半減期Be-7は、放射性エアロゾルとなって存在するため、排気の際はフィルターで除去。
H-3は、HTO及びHTの化学形で存在するためフィルターで除去されず、大気中へ放出。
air.eps
描画出力ファイル(*.eps)を開いて、主要核種の放射能の時間変化を確認しよう
Ar-41,O-15等はフィルターでトラップできない。
加速器室の空気を閉じ込めて（循環させて）運転。
運転中の空気中濃度が法令値の1/10を超えなければ空気を常に入れ替えて運転。
例：濃度限度の1/10(Bq/cm3): 2e-2(O-15), 1e-2(Ar-41)
今回、44ページの結果2.59e4(O-15), 6.47e2(Ar-41)から空気閉じ込め運転が必須

--- SLIDE 47 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
内容
1. コンクリートの迷路構造におけるγ線ストリーミング計算

2. 陽子加速器施設のビームダンプ周辺における中性子遮蔽と空気の放射化計算

3. まとめ

--- SLIDE 48 ---
PPTX_FILE: PHITS-shielding-en.pptx
SLIDE_TEXT:
まとめ
遮蔽計算では、[t-track]にmultiplier機能を使って線量評価（イベントジェネレータモードや電子輸送は不要）
全てモンテカルロで遮蔽計算をするのは現実的でなく、簡易式とモンテカルロを組み合わせて実施
[t-point]タリー、ダンプ線源ファイル、分散低減法を活用して効率的に計算を行うことが重要
PHITSとDCHAINのつなぎ計算により空気や材料の放射化の評価が可能
PHITS計算結果には統計誤差のみならず系統誤差があるため、実際の許認可申請では施設固有の安全尤度（ファクター２程度）を考慮することがあります

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: maze/input/maze-2.inp
FILE: maze/input/maze-3.inp
FILE: maze/input/maze-end.inp

[BONUS_TEXT_FILES]
NOTE: None
