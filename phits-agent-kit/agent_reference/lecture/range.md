# Lecture: exercise/range

SOURCE_FOLDER: D:/NEAgit/lecture/exercise/range
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: range
LECTURE_PATH_INDEX: lecture/exercise/range
PPTX_FILES: phits-range-en.pptx, phits-range-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: answer1, range
SECTION_KEYWORDS: t-cross, t-track

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/exercise/range
LECTURE_PATH_INDEX: lecture/exercise/range
PPTX_FILES: phits-range-en.pptx, phits-range-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 2
SLIDE_COUNT: 38
EXERCISE_SLIDE_COUNT: 1
BONUS_INPUT_COUNT: 10
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- answer1.inp
- range.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: EXERCISE 1 | How to stop a, b, g-rays and neutrons?
  ANSWER_FILE: input/range-2.inp
- SLIDE 02: α particles can be stopped by a piece of paper
- SLIDE 03: Check Range.inp
- SLIDE 04: Source with Energy Distribution
- SLIDE 05: Procedure
- SLIDE 06: Step 1：Change Source
- SLIDE 07: Step 2: Change the Thickness
- SLIDE 08: Step 3：Change Tally Region
- SLIDE 09: Step 3
- SLIDE 10: Step 4: How about α-rays?
- SLIDE 11: Step 5: Change Target to a Piece of Paper
- SLIDE 12: Step 6: How about γ-rays?
- SLIDE 13: Step 7
- SLIDE 14: Step 8: Consider Statistical Uncertainty
- SLIDE 15: Step 9
- SLIDE 16: Step 10
- SLIDE 17: Common sense on the shielding profiles of α, β, γ rays and neutrons has been confirmed by PHITS simulations.
- SLIDE 18: Homework
- SLIDE 19: Homework
- SLIDE 01: α線，β線，γ線，中性子線を止めるには？
- SLIDE 02: α線は紙1枚で止まる
- SLIDE 03: Range.inpの確認
- SLIDE 04: エネルギー分布を持つ線源
- SLIDE 05: 本演習の流れ
- SLIDE 06: ステップ１：線源をβ線に変更
- SLIDE 07: ステップ２：遮へい体厚さの変更
- SLIDE 08: ステップ３：タリー領域の変更
- SLIDE 09: 透過した光子のスペクトルは？
- SLIDE 10: ステップ４：α線入射の場合は？
- SLIDE 11: ステップ５：遮へい体を紙に変更
- SLIDE 12: ステップ６：γ線入射の場合は？
- SLIDE 13: ステップ７：γ線を遮へいできる鉛の厚さは？
- SLIDE 14: ステップ８：統計的に正しい答えを得る
- SLIDE 15: ステップ９：中性子入射の場合は？
- SLIDE 16: ステップ１０：中性子を効果的に遮へいする
- SLIDE 17: PHITSを用いてα線，β線，γ線，中性子線の透過力を計算し，通説が（ほぼ）正しいことを確認できた
- SLIDE 18: Homework
- SLIDE 19: Homework

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: answer1.inp
FILE: range.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-range-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
How to stop a, b, g-rays and neutrons?
Note: The results shown in this lecture note were obtained using an earlier version of PHITS and may not be identical to those obtained using the latest version.
Jul. 2026 revised
phits/lecture/exercise/range
SPEAKER_NOTES:
We would like to start an exercise 1. The title is How to stop alpha, beta, gamma rays and neutrons?
ANSWER_FILE: input/range-2.inp

--- SLIDE 02 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
α particles can be stopped by a piece of paper
β rays can be stopped by an aluminum plate
γ rays can be stopped by a lead block
neutrons can penetrate all of these materials
Contents
Purpose of this Exercise
It is generally said that …
Let’s check whether they are correct or not, using PHITS!
SPEAKER_NOTES:
It is generally said that alpha particles can be stopped by a piece of paper, beta rays can be stopped by an aluminum plate, gamma rays can be stopped by a lead block, neutrons can penetrate all of these materials. In this section, let’s check whether they are correct or not, using PHITS.

--- SLIDE 03 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Check Range.inp
*Error bar is depicted when epsout = 2
Calculation Condition
track.eps
Photons with an energy distribution (r = 0.01cm)
Cylindrical Al shielding (t = 0.1cm, r = 5cm) & Void
[t-track] for visualizing particle trajectories
[t-cross] for calculating particle fluences behind the shielding
(Error bars are plotted by setting epsout = 2)
cross.eps*
Geometry
Incident particles：
Geometry：
Tally：
Photon
Al
Void
SPEAKER_NOTES:
In this section, we use range dot inp. At first, we should check the input file. Incident particle is a photon with the energy distribution. The beam radius is 0.01 Centimeter. A geometry consists of cylindrical aluminum shielding and a void. An aluminum target of thickness 0.1 Centimeter and radius 5 Centimeter is prepared here. We use [ t track ] tally for visualizing particle trajectories and [ t cross ] Tally for calculating particle fluences behind the shielding. Using the [ t cross ] Tally, error bars are plotted by setting epsout Equal 2. We can see those figures from the track dot eps and cross dot eps of the output files.
MENTIONED_INPUT_NAMES: Range.inp

--- SLIDE 04 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Source with Energy Distribution
Energy distribution is defined by e-type subsection.
[ S o u r c e ]
   s-type =   1
     proj =  photon
       r0 =   0.0100
       x0 =   0.0000
       y0 =   0.0000
       z0 =  -20.000
       z1 =  -20.000
      dir =   1.0000
 e-type =   21
       ne =   3
$ E_low  Flux(/MeV)
      0.0     1.0
      1.0     3.0
      2.0     1.0
      3.0
e-type = 21: number of energy bins (ne)
        lower boundary of each bin (MeV)
        Relative fluence in each energy bin (/MeV)
Lower boundary of each energy bin (ne+1)
Relative fluence in each bin (/MeV)
1   :   3    :   1
See manual or lecture\advanced\sourceA for more detail
SPEAKER_NOTES:
Next, we demonstrate a setting of source with energy distribution. The energy distribution is defined by e type subsection. We should set as e type Equal 21 here. In this type, it is necessary to give number of energy bins ( n e ), lower boundary of each bin ( M e V ) and relative fluence in each energy bin ( Slash M e V ) as parameters. In this sample, we set as n e Equal 3, so three energy groups exist as shown in this figure. And lower boundary of each energy bin is number of ne Plus 1, so number of the bin is four. The relative fluences are given by a ratio of 1 to 3 to 1 as shown in this figure.

--- SLIDE 05 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Procedure
Change the source to β-rays
Change the thickness of the Al shielding
Change the tallied region
Change the source to α-rays
Change the target to a piece of paper
Change the source to γ-rays, and the target to a lead block
Find an sufficient thickness of the lead block
Reduce the statistical uncertainty
Change the source to neutrons
Find an sufficient  shielding material for neutrons
The input file for each procedure are prepared as “range*.inp”
Procedure for this exercise
SPEAKER_NOTES:
Procedure for this exercise is as follow. Change the source to beta rays. Change the thickness of the aluminum shielding. Change the tallied region. Change the source to alpha rays. Change the target to a piece of paper. Change the source to gamma rays, and the target to a lead block. Find an appropriate thickness of the lead block. Reduce the statistical uncertainty. Change the source to neutrons. Find an appropriate shielding material for neutrons. The input file for each procedure is prepared as range Star dot inp.

--- SLIDE 06 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 1：Change Source
Step 1
1. Change energy distribution according to Table 1 → Check cross.eps
[ S o u r c e ]
   s-type =   1
     proj =  photon
       r0 =   0.0100
       x0 =   0.0000
       y0 =   0.0000
       z0 =  -20.000
       z1 =  -20.000
      dir =   1.0000
 e-type =   21
       ne =   3
$ E_low  Flux(/MeV)
      0.0     1.0
      1.0     3.0
      2.0     1.0
      3.0
Table 1 Relative fluence of β-rays
cross.eps after step1
track.eps after step2
(2nd page)
Change parameters in red
2. Change particle to electron (proj) → Check track.eps
SPEAKER_NOTES:
Let’s go on step 1 change source. At first, please change energy distribution according to Table 1, and check cross dot eps after step 1. Change parameters are shown in a sample file by red color. Next, please change from the photon to a electron, and check the track dot eps on second page. You can see those sample figures.

--- SLIDE 07 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 2: Change the Thickness
Step 2
Thickness of target is defined as the variable c1
Find an sufficient  thickness of the Al plate,
which can fully stop electrons (check by a 1-mm step)
Electron fluence (track.eps, 2nd page)
3 mm is thick enough!
[ S u r f a c e ]
set: c1[0.1]  $ Thickness of Target (cm)
 1            pz     0.0
 2            pz      c1
 3            pz    50.0
 11           cz     5.0
 999          so   100.0
SPEAKER_NOTES:
Let’s go on step 2 change the thickness. In this step, we find an appropriate thickness of the aluminum plate, which can fully stop electrons by check by a 1 Millimeter step. From this input file, the thickness is defined by a variable c1, so please change this value. This figure shows a calculated result of electron fluence at c1 Equal 0.3 in the track dot eps on second page. We can confirm that 3 Millimeter is thick enough.

--- SLIDE 08 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 3：Change Tally Region
Step 3
Target thickness (c1) should be 0.3 cm
Tally from -c1 to +c1 cm for X&Y directions
Tally from 0 to c1*2 cm for Z direction
[ T - T r a c k ]
  title = Track in
  mesh =  xyz
  x-type =    2
  xmin =  -1.5
  xmax =   1.5
  nx =   50
  y-type =    2
  ymin =  -1.5
  ymax =   1.5
  ny =    1
  z-type =    2
  zmin =   0.0
  zmax =   3.0
  nz =   90
Let’s see the fluence distribution inside the target in more detail!
Electron fluence
Stopped close to the distal edge
Photon fluence
Penetrated
SPEAKER_NOTES:
Let’s go on step 3 Change Tally Region. In this step, let’s see the fluence distribution inside the target in more detail. At firstly, target thickness c1 should be 0.3 Centimeter. Next, please change Tally from Minus c1 to Plus c1 Centimeter for X and Y directions and Tally from 0 to c1 times 2 Centimeter for Z direction. Change parameters are shown in this sample file by red color. Those figures in the track dot eps show electron and photon fluences after the change. We can confirm that the electrons stopped close to the distal edge and the photons penetrated.

--- SLIDE 09 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 3
Particle fluence behind the target（cross.eps）
Photons with energies from 10 keV to 500 keV escape
Integrated value?
You can find the integrated fluence per source at ”# sum over” at the 71 line of cross.out
0.024 photons/incident electron escape from the aluminum plate
An aluminum plate, which is thick enough to stop β-ray, is not thick enough to stop secondary photons!
Check Energy Spectrum
photon      r.err
…
#   sum over    2.4091E-02  0.2997
SPEAKER_NOTES:
We can see the photon penetration. Let’s check the energy spectrum. We can check particle fluence behind the target from cross dot eps as shown in this figure. From the result, you can find that photons with energies from 10 k e V to 500 k e V escape from the target. You can find the integrated fluence per source at Hash sum over at the 70 line of cross dot out as shown in the output sample. The result shows that 0.024 photons or incident electron escape from the aluminum plate. We can confirm that an aluminum plate, which is thick enough to stop beta ray, is not thick enough to stop secondary photons.

--- SLIDE 10 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 4: How about α-rays?
Fluence of α particles
(3rd page of track.eps)
Change the source to α particles emitted from 210Po decay
Particle type is defined by “proj” (α-ray is “alpha”)
Use RI source function (e-type = 28)*
Replace # of energy bins (ne) by # of Isotopes (ni)
Define RI & its activity in Bq (e.g. Po-210  1.0)
[ S o u r c e ]
 s-type =   1
     proj =  electron
       r0 =   0.0100
       x0 =   0.0000
       y0 =   0.0000
       z0 =  -20.000
       z1 =  -20.000
      dir =   1.0000
   e-type =  21
       ne =   3
$  E_low  Flux(/MeV)
     0.0     2.0
     0.5     1.0
     1.0     0.5
     1.5
e-type =  28
       ni =   1
Po-210   1.0
alpha
*See lecture\advanced\SourceA for more detail
SPEAKER_NOTES:
Let’s go on step 4 How about alpha particles ? Please change the source to alpha particles emitted from Polonium 210 decay. Particle type is defined by pro j in a sample input file. Alpha particle is written as alpha. We use R I source function. This is e type Equal 28. Please replace Hash of energy bins ( n e ) by Hash of Isotopes ( n i ). We should define R I and its activity in becquerel. Change parameters are shown in this sample file by red color. We can see fluence of alpha particles in third page of track dot eps.

--- SLIDE 11 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 5: Change Target to a Piece of Paper
Fluence of α particle (page 4)
Paper consists of cellulose with chemical form of C6H10O5
Predefined material name of cellulose is @C6H10O5@
Thickness of paper is assumed to be 0.01 cm
[ M a t e r i a l ]
MAT[ 1 ]   @ALUMINUM@

[ C e l l ]
 1          1  0.0    1 -2 -11   $ Target
 2          0          2 -3 -11   $ Void
98          0         #1 #2 -999  $ Void
99         -1             999  $ Outer region

[ S u r f a c e ]
set: c1[  0.3   ]  $ Thickness of Target (cm)
 1            pz     0.0
 2            pz      c1
 3            pz    50.0
 11           cz     5.0
 999          so   100.0
Stop at 0.003 cm in paper & no secondary particles are generated
It is also registered as @CELLULOSE_ACETATE_CELLOPHANE_(C6_H10_O5)N@
Not necessary to change the material ID of the target because it is always 1
SPEAKER_NOTES:
Let’s go on step 5 Change target to a piece of paper. In this step, we assume that paper consists of cellulose with chemical form of C 6 H 10 O 5, with predefined material name at C 6 H 10 O 5 at. Geometry. Then, thickness of paper is assumed to be 0.01 Centimeter. Therefore, please change material name and change c1 in surface section along red color. Please note that it is not necessary to change the material ID of the target because it is always 1 in this exercise. We can see fluence of alpha particle as shown in this figure. We find that the particle stop at 0.005 Centimeter and no secondary particles are generated.

--- SLIDE 12 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 6: How about γ-rays?
Step 6
Change the source to g-rays at 0.662 MeV

Change the target to a 1 cm lead (Pb) block (11.34 g/cm3)
Photon fluence
Target thickness is not enough
Energy spectra behind the target
Most of source photons penetrate the target without reactions
Use mono-energetic source (e0) instead of RI source (e-type=28)
SPEAKER_NOTES:
Let’s go on Step 6 How about gamma rays? At first, please change the source to gamma rays at 0.662 M e V. We should Use mono-energetic source ( e 0 ) instead of R I source ( e type Equal 28 ). And, change the target to a 1 cm lead ( P b ) block. The density is 11.34 gram Slash Centimeter cubic. From photon fluence of a left figure, we find that the target thickness is not enough. From energy spectra behind the target of a right figure, we find that most of source photons penetrate the target without reactions.

--- SLIDE 13 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 7
Photon fluence for
the 4.4-cm lead target case
Change the target thickness to decrease the direct penetration rate of photons down to 0.01
Check the 46th line (0.6 MeV < E < 0.7 MeV) in cross.out
Energy spectrum
Penetration rate = 0.009
Step 7: Find an sufficient  thickness
Statistically insignificant!
SPEAKER_NOTES:
Let’s go on step 7 Find an appropriate thickness. At first, please change the target thickness to decrease the direct penetration rate of photons down to 0.01. In this exercise, please check the 45th line from 0.6 M e V to 0.7 M e V in cross dot out. In case of 4.4 Centimeter lead target, photon fluence is shown as this figure. A right figure shows a calculated results of energy spectrum of penetrated photon. From the output data of cross dot out, we find that penetration rate is 0.009. The value is less than 0.01, but, an error bar exceeds 0.01. We cannot judge to be reached less than 0.01 significantly statistically.

--- SLIDE 14 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 8: Consider Statistical Uncertainty
Step 8
Estimate a statistically-significant shielding thickness that has a penetration rate < 0.01, by changing maxcas, maxbch, batch.out, istdev etc.
Elow(MeV)     Ehigh(MeV)         Photon      r.err
  2.0000E-01   3.0000E-01   0.0000E+00  0.0000
  3.0000E-01   4.0000E-01   0.0000E+00  0.0000
  4.0000E-01   5.0000E-01   1.5326E-03  0.7118
  5.0000E-01   6.0000E-01   1.1820E-03  0.7078
  6.0000E-01   7.0000E-01   9.1494E-03  0.2348
See the 46th line in cross.out
Statistical uncertainty is too large (~23%)
2.0000E-01   3.0000E-01   8.2372E-05  0.5927
  3.0000E-01   4.0000E-01   7.6987E-04  0.2574
  4.0000E-01   5.0000E-01   1.4078E-03  0.1351
  5.0000E-01   6.0000E-01   2.9153E-03  0.0810
  6.0000E-01   7.0000E-01   9.5422E-03  0.0407
Thickness = 4.4 cm，maxcas = 2000, maxbch = 1
Thickness = 4.2 cm，maxcas = 2000, maxbch =32
SPEAKER_NOTES:
Let’s go on step 8  Consider Statistical Uncertainty. We should estimate a statistically-significant shielding thickness that has a penetration rate less than 0.01, by changing maxcas, maxbch, batch.out, istdev etc. We show a sample case of Thickness Equal 4.4 Centimeter, maxcas Equal 2000 and maxbch Equal 1. Please see the 45th line in cross dot out. We find that statistical uncertainty is too large, the value is 23 Percent. In case of Thickness Equal 4.2 Centimeter, maxcas Equal 2000 and maxbch Equal 32, we can confirm that the penetration rate is below 0.01 with statistical significance.

--- SLIDE 15 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 9
Step 9: How about neutrons?
Change the source projectile to neutron at 1.0 MeV
Set “maxbch = 3”
Neutron fluence
Penetrate!
Energy spectra
80% of neutrons penetrate the
target without reactions
SPEAKER_NOTES:
Let’s go on step 9 How about neutrons ? Please change the source to neutron at 1.0 M e V, and set maxbch Equal 3. From the calculated results of Neutron fluence of the track dot eps and energy spectra of the cross dot eps, we can see 80 Percent of neutrons penetrate the target without reactions.

--- SLIDE 16 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Step 10
Step 10: Shielding material for neutrons
C ~27 cm
@GRAPHITE@
Change the target material and thickness to decrease the penetration rate of neutrons down to 0.01 (see ”# sum over” at the 71st line)
Try various materials for the target. Find shielding materials efficient for neutrons
H2O ~17 cm
@WATER@
Light nuclei (particularly H) are suitable for neutron shielding
Al ~40 cm
@ALUMIMUM@
SPEAKER_NOTES:
Let’s go on step 10 Shielding material for neutrons. At first, please change the target material and thickness in order to decrease the penetration rate of neutrons down to 0.01. We can judge neutron shielding from a value of Hash sum over of 71th line in cross dot out. Next, please try various materials for the target, and find out an appropriate shielding material for neutrons. We show some examples of calculated results. We can confirm that Light nuclei are suitable for neutron shielding.

--- SLIDE 17 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Common sense on the shielding profiles of α, β, γ rays and neutrons has been confirmed by PHITS simulations.

PHITS is useful for particle transport simulation in a mixed radiation field owing to its applicability to various radiation types.
Summary
Summary
SPEAKER_NOTES:
In summary. Common sense on the shielding profiles of alpha, beta, gamma rays and neutrons has been confirmed by Phits simulations. Phits is useful for particle transport simulation in a mixed radiation field owing to its applicability to various radiation types.

--- SLIDE 18 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Homework
Let’s design a shielding for high-energy neutrons (100 MeV)
Index for the effectiveness of shielding is not the fluence but the effective dose
Find the thinnest shielding that can reduce the doses by 2 order of magnitude
Combine 2 materials for the shielding
Homework (challenge!)
Hints
Use [t-track] in “h10multiplier.inp”  in the recommendation settings
See the histogram of the dose by changing the axis from “xz” to “z”
Change “nx” parameter to 1 to simplify the files
Low-energy neutrons are effectively shielded by light nuclei, while high-energy neutrons are shielded by intermediate-mass nuclei
SPEAKER_NOTES:
Finally, we present a challenging homework. Let’s design a shielding for high-energy neutrons ( 100 M e V ). Index for the effectiveness of shielding is not the fluence but the effective dose. Find the thinnest shielding that can reduce the doses by 2 order of magnitude. Combine 2 materials for the shielding. We show some of hints is this home work. Please try if you are interests.
MENTIONED_INPUT_NAMES: h10multiplier.inp

--- SLIDE 19 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Homework
Example of Answer（answer1.inp）
Let’s Think
How much of the total dose is contributed by photon?
Why 2-layer shielding is more effective than a mono-layer one?
What happens when the order of the 2 layers is inverted?
2-layer shielding that consists of 80 cm iron and 25 cm concrete
Iron
Concrete
Air
SPEAKER_NOTES:
We show example of answer used answer1 dot inp. We will finish this exercise.
MENTIONED_INPUT_NAMES: answer1.inp

--- SLIDE 01 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
α線，β線，γ線，中性子線を止めるには？
2026年7月改訂
phits/lecture/exercise/range
この資料に示した計算結果は、古いバージョンのPHITSを用いて得られたものであり、最新版を用いた結果と完全には一致しない可能性があることにご留意ください
SPEAKER_NOTES:
それでは、総合実習1を開始します。タイトルは アルファ線，ベータ線，ガンマ線，中性子線を止めるにはです。

--- SLIDE 02 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
α線は紙1枚で止まる
β線はアルミ板1枚で止まる
γ線は鉛ブロックで止まる
中性子線は，それら全てを透過する
実習目的
と言われています。
本当かどうかPHITSを使って確認してみよう
SPEAKER_NOTES:
放射線の良く知られた一般的な性質として、アルファ線は紙1枚で止まる、ベータ線はアルミ板1枚で止まる、ガンマ線は鉛ブロックで止まる、中性子線はそれら全てを透過すると言われています。これが本当かどうかPHITSを使って確認することが、このセッションの実習目的です。

--- SLIDE 03 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Range.inpの確認
*epsout = 2とすると誤差棒を出力
基本計算条件
入射粒子：
体系：

タリー：
光子
Al
計算体系
track.eps
エネルギー分布を持つ光子（ビーム半径0.01cm）円柱の遮へい体と真空のみが存在
（厚さ0.1cm，半径5cmのアルミターゲット）
[t-track]によるフラックス空間分布
[t-cross]による遮へい体後方のエネルギー分布
（epsout=2とすることにより誤差棒も表示）
cross.eps*
Void
SPEAKER_NOTES:
このセッションで利用するインプットファイルはレンジドットインプです。まず初めに、このインプットファイルを確認していきます。入射粒子は、エネルギー分布を持つ光子（ビーム半径0.01センチメートル）です。体系は、円柱の遮へい体と真空のみから構成されています。ここでは、厚さ0.1センチメートル、半径5センチメートルのアルミターゲットが用意されております。タリーは[ティートラック]、[ティークロス]の2つが用意されており、インプットファイルを実行すると、フラックス空間分布や遮へい体後方のエネルギー分布が出力されます。ここで、イーピーエスアウトイコール2とすることにより誤差棒も表示されます。

--- SLIDE 04 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
エネルギー分布を持つ線源
e-typeサブセクションにより分布を定義する。
[ S o u r c e ]
   s-type =   1
     proj =  photon
       r0 =   0.0100
       x0 =   0.0000
       y0 =   0.0000
       z0 =  -20.000
       z1 =  -20.000
      dir =   1.0000
 e-type =   21
       ne =   3
$ E_low  Flux(/MeV)
      0.0     1.0
      1.0     3.0
      2.0     1.0
      3.0
e-type = 21: エネルギー群数(ne)
        各エネルギー群の下限値（MeV)
        相対フラックス(/MeV)を与える
各エネルギー群の下限値(群数＋１個）
各エネルギー群の相対フラックス(/MeV)
1   :   3    :   1
詳しくはマニュアルもしくはlecture\advanced\sourceAを参照
SPEAKER_NOTES:
次に、エネルギー分布を持つ線源をどのように設定するか説明します。具体的には、イータイプサブセクションにより分布を定義することになります。ここでは、イータイプイコール21と設定します。あとはパラメータとして、エネルギー群数（エヌイー）、各エネルギー群の下限値（メブ)、相対フラックス(スラッシュメブ)を与える必要があります。このサンプルでは、エヌイーイコール3としていますので、こちらの図にありますように、エネルギー群が3つ存在します。そして、各エネルギー群の下限値は、群数プラス1ですので、0、1、2、3のように4つ存在します。相対フラックスは、このように設定しますと、こちらの図にありますように、1対3対1になります。

--- SLIDE 05 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
本演習の流れ
Procedure
線源をβ線に変更する
遮へい体の厚さを変更する
タリー領域の変更する
線源をα線に変更する
遮へい体を紙に変更する
線源をγ線に変更し，遮へい体を鉛に変更する
γ線を遮へいできる鉛の厚さを最適化する
統計誤差を小さくする
線源を中性子に変更する
中性子遮へいに最適な素材を探す
各ステップで変更するインプットは「range*.inp」として準備されています
SPEAKER_NOTES:
本演習の流れですが、線源をベータ線に変更する、遮へい体の厚さを変更する、タリー領域を変更する、線源をアルファ線に変更する、遮へい体を紙に変更する、線源をガンマ線に変更し，遮へい体を鉛に変更する、ガンマ線を遮へいできる鉛の厚さを最適化する、統計誤差を小さくする、線源を中性子に変更する、中性子遮へいに最適な素材を探す、となります。これまでと同様、各ステップで変更するインプットはレンジスタードットインプとして準備しておりますので、先に進みたい場合や、分からなくなった場合にご利用下さい。

--- SLIDE 06 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ１：線源をβ線に変更
Step 1
① 相対フラックスを表１になるように変更 → 透過スペクトルを確認
[ S o u r c e ]
   s-type =   1
     proj =  photon
       r0 =   0.0100
       x0 =   0.0000
       y0 =   0.0000
       z0 =  -20.000
       z1 =  -20.000
      dir =   1.0000
 e-type =   21
       ne =   3
$ E_low  Flux(/MeV)
      0.0     1.0
      1.0     3.0
      2.0     1.0
      3.0
表１ β線源の相対フラックス
①の後のcross.eps
②の後のtrack.eps
（2ページ目）
赤字を修正
② 入射粒子を光子からβ線(=electron)に変更（proj）→ 飛跡を確認
SPEAKER_NOTES:
それでは、ステップ1の線源をベータ線に変更するに移ります。ここでは、①②と2段階に分けて実習していきます。まず初めに、①相対フラックスを表1になるように変更してください。ここでは、赤字を修正することになります。確認する出力ファイルはクロスドットイーピーエスです。こちらのような図が出力されているかと思います。次に②入射粒子を光子からベータ線に変更してください。ここでは、フォトンをエレクトロンに変更することになります。確認する出力ファイルはトラックドットイーピーエスです。こちらのような図が出力されているかと思います。

--- SLIDE 07 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ２：遮へい体厚さの変更
Step 2
ターゲット厚は変数（c1）で定義している
遮へい体の厚さを1mm刻みで変更し，電子が完全に止まる厚さを調べてみよう
電子フラックス(track.epsの2ページ目)
厚さ3mmあれば止まる！
[ S u r f a c e ]
set: c1[0.1]  $ Thickness of Target (cm)
 1            pz     0.0
 2            pz      c1
 3            pz    50.0
 11           cz     5.0
 999          so   100.0
SPEAKER_NOTES:
それでは、ステップ2の遮へい体厚さの変更に移ります。ここでは、遮へい体の厚さを1ミリメートル刻みで変更し、電子が完全に止まる厚さを調べてみましょう。インプットファイルの[サーフェイス]セクションをみますと、ターゲットあつは変数（シー1）で定義していますので、この赤字を変更します。こちらの図はシー1イコール0.3のときの結果となります。このように、アルミの厚さが3ミリメートルあれば電子は止まることが確認できたかと思います。

--- SLIDE 08 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ３：タリー領域の変更
Step 3
電子フラックス(2ページ目）
ぎりぎり止まっている
遮へい体内での放射線挙動を詳しく見てみよう
光子フラックス（1ページ目）
止まっていない!!
ターゲット厚（c1）は0.3cmとする
X,Y方向は-c1からc1までとする
Z方向は0cmからc1の2倍までとする
[ T - T r a c k ]
  title = Track in
  mesh =  xyz
  x-type =    2
  xmin =  -1.5
  xmax =   1.5
  nx =   50
  y-type =    2
  ymin =  -1.5
  ymax =   1.5
  ny =    1
  z-type =    2
  zmin =   0.0
  zmax =   3.0
  nz =   90
SPEAKER_NOTES:
ステップ3のタリー領域の変更に移ります。ここでは、遮へい体内での放射線挙動を詳しく見ていきます。ターゲットあつ（シー1）は0.3センチメートルとします。そして、[ティートラック]タリーを変更していきます。エックス,ワイ方向はマイナスシー1からシー1までとします。Z方向は0センチメートルからシー1の2倍までとします。具体的には、こちらの赤字を修正していくことになります。修正後の[ティートラック]タリーはこのようになり、トラックドットイーピーエスを開くと、このような結果が出力されているかと思います。トラックドットイーピーエスの1ページ目は光子フラックスで、2ページ目は電子フラックスです。このように、電子はぎりぎり止まるのですが、電子線照射の結果生じた光子は透過することが確認できたかと思います。

--- SLIDE 09 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
透過した光子のスペクトルは？
透過粒子エネルギー
スペクトル（cross.eps）
数10keV～数100keVの光子が透過している
photon      r.err
…
#   sum over    2.4091E-02  0.2997
透過率は？
cross.outの71行目に”# sum over”として積分値（1線源当たりにその面を横断した粒子数）が出力される
電子1入射当たり0.024個の光子が3mmのアルミ板を透過する
β線はアルミ板で止まるが，放射線を完全に遮へいできるわけではない！
Step 3
SPEAKER_NOTES:
それでは、透過した光子のスペクトルについて調べていきたいと思います。透過粒子エネルギースペクトルは[ティークロス]タリーから出力されるクロスドットイーピーエスで確認することができます。こちらの結果から、数10ケブから数100ケブの光子が透過していることを確認することができます。ここで、透過率についてですが、クロスドットアウトの70行目にシャープサムオーバーとして積分値（1線源当たりにその面を横断した粒子数）が出力されています。このデータは、電子1入射当たり0.024個の光子が3ミリメートルのアルミ板を透過することを意味しています。つまり、ベータ線はアルミ板で止まりますが、放射線を完全に遮へいできるわけではないことが確認できたかと思います。

--- SLIDE 10 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ４：α線入射の場合は？
α線フラックス(track.epsの3枚目）
表面で全て止まっている
入射粒子をβ線から210Poのα崩壊によるα線（5.3MeV）に変更する
[ S o u r c e ]
 s-type =   1
     proj =  electron
       r0 =   0.0100
       x0 =   0.0000
       y0 =   0.0000
       z0 =  -20.000
       z1 =  -20.000
      dir =   1.0000
   e-type =  21
       ne =   3
$  E_low  Flux(/MeV)
     0.0     2.0
     0.5     1.0
     1.0     0.5
     1.5
粒子の種類はprojで指定（α線はalpha）
RI線源機能を使う（e-type=28）*
エネルギー群数(ne)の代わりにRI核種数（ni）を指定する
核種（元素記号-質量数） 放射能（Bq）を定義する
e-type =  28
       ni =   1
Po-210   1.0
alpha
210Poが1Bq
*単色の場合はe0で指定することも可能
SPEAKER_NOTES:
ステップ４のアルファ線入射の場合に移ります。ここでは、入射粒子をベータ線からポロニウム210のアルファ崩壊によるアルファ線（5.3メブ）に変更します。粒子の種類は、プロジェイで指定します。ここでは、アールアイ線源機能を使います。この利用方法ですが、イータイプを変更する必要があり、ここでは28とします。エネルギー群数(エヌイー)の代わりにアールアイ核種数（エヌアイ）を指定します。最後に、核種（元素記号ハイフン質量数）と放射能（ベクレル）を定義します。具体的には、サンプルのように変更して頂けたらと思います。トラックドットイーピーエスの3枚目ですが、図のような結果が出力されているかと思います。このように、アルファ線は表面で全て止まっていることが確認できたかと思います。

--- SLIDE 11 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ５：遮へい体を紙に変更
@CELLULOSE_ACETATE_CELLOPHANE_(C6_H10_O5)N@でも登録されています
紙（セルロース、C6H10O5）の既定物質名は@C6H10O5@
厚さは0.01cmと仮定
α線フラックス（４ページ目）
本当に紙1枚（0.003cm）で止まる
2次粒子も発生しない
[ M a t e r i a l ]
MAT[ 1 ]   @ALUMINUM@

[ C e l l ]
 1          1  0.0    1 -2 -11   $ Target
 2          0          2 -3 -11   $ Void
98          0         #1 #2 -999  $ Void
99         -1             999  $ Outer region

[ S u r f a c e ]
set: c1[  0.3   ]  $ Thickness of Target (cm)
 1            pz     0.0
 2            pz      c1
 3            pz    50.0
 11           cz     5.0
 999          so   100.0
常に物質1を使うので変更の必要なし
SPEAKER_NOTES:
ステップ５の遮へい体を紙に変更に移ります。ここでは、標的をアルミから紙（セルロース）に変更します。その既定物質名は、化学式通りでアット シー6エイチ10オー5 アットですので、[マテリアル]セクションのアルミをこの文字列に変更してください。厚さは0.01センチメートルと仮定します。そのため、 [surface]セクションで、厚みを定義するシー1を赤字のように変更してください。なお、セルセクションで定義する物質IDは、常に物質番号１を使うので変更の必要はありません。トラックドットイーピーエスの4枚目ですが、図のような結果が出力されているかと思います。このように、紙1枚（0.003センチメートル程度）で止まり、2次粒子も発生しないことが確認できたかと思います。

--- SLIDE 12 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ６：γ線入射の場合は？
Step 6
光子フラックス
遮へいが十分でない
入射粒子をα線から0.662MeVの γ線(=photon) に変更する

遮へい体を厚さ1cmの鉛（既定物質名@LEAD@）に変更する
透過エネルギースペクトル
一度も散乱せずに
透過した光子が多数存在
RI線源ではなく単色線源(e0）で指定 → e-typeに関連する部分を削除
SPEAKER_NOTES:
ステップ６のガンマ線入射の場合に移ります。ここでは、入射粒子をアルファ線から0.662メブのガンマ線に変更します。そのため、アールアイ線源ではなく、単色線源(イー0）で指定しますので、イータイプに関連する部分を削除してください。そして、遮へい体を厚さ1センチメートルの鉛に変更してください。鉛は、Pbで、密度が11.34グラムパー立方センチメートルとなります。トラックドットイーピーエスの1ページ目を見ると、光子フラックスの結果が出力されており、左図のような結果が得られているかと思います。光子が十分に遮へいされていないことが確認できます。さらに、透過エネルギースペクトルも確認してみたいと思います。クロスドットイーピーエスを開くと、右図のような結果が得られているかと思います。この分布から、0.6メブ程度の成分が確認できますので、一度も散乱せずに透過した光子が多数存在していることも分かるかと思います。

--- SLIDE 13 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ７：γ線を遮へいできる鉛の厚さは？
Step 7
鉛4.4cmの場合の光子フラックス
遮へい体の厚さを変更する
一度も散乱されずに透過する確率が0.01以下になれば遮へいできたとする → cross.outの46行目（0.6～0.7MeV）で確認
透過エネルギースペクトル
透過率0.009
統計的に有意に0.01以下とは言えない
SPEAKER_NOTES:
ステップ７のガンマ線を遮へいできる鉛の厚さについて調べたいと思います。ここでは、遮へい体の厚さを変更していきます。そして、一度も散乱されずに透過する確率が0.01以下になれば遮へいできたとします。鉛の厚さを4.4センチメートルにすると、左図のような結果が得られます。右図は、トラックドットイーピーエスの結果です。この結果を見ますと、透過率は0.009となっていますが、誤差棒は0.01を超えていますので、統計的に有意に0.01以下に到達したとは言えないことも確認できるかと思います。

--- SLIDE 14 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ８：統計的に正しい答えを得る
Step 8
maxcas, maxbch, batch.out, istdevなどを駆使して，
統計的に有意な差で透過率が0.01以下になる厚さを探す
Elow(MeV)     Ehigh(MeV)         Photon      r.err
  2.0000E-01   3.0000E-01   0.0000E+00  0.0000
  3.0000E-01   4.0000E-01   0.0000E+00  0.0000
  4.0000E-01   5.0000E-01   1.5326E-03  0.7118
  5.0000E-01   6.0000E-01   1.1820E-03  0.7078
  6.0000E-01   7.0000E-01   9.1494E-03  0.2348
cross.outの46行目に透過率と統計誤差が出力されている
統計誤差を考えると，透過率が0.01以下とは言えない
2.0000E-01   3.0000E-01   8.2372E-05  0.5927
  3.0000E-01   4.0000E-01   7.6987E-04  0.2574
  4.0000E-01   5.0000E-01   1.4078E-03  0.1351
  5.0000E-01   6.0000E-01   2.9153E-03  0.0810
  6.0000E-01   7.0000E-01   9.5422E-03  0.0407
0.00954 ± 4.07%なので，透過率が0.01以下と考えてよい
厚さ4.4ｃｍ，maxcas = 2000, maxbch = 1の場合
厚さ4.2cm，maxcas = 2000, maxbch = 32の場合
SPEAKER_NOTES:
そこで、ステップ８の統計的に正しい答えを得るに移ります。これまで学習してきたマックスキャス、マックスバッチ、バッチドットアウト, アイエスティーデブなどを駆使して，統計的に有意な差で透過率が0.01以下になる厚さを探していきます。厚さ4.4センチメートル、マックスキャスイコール2000、マックスバッチイコール1の場合、表のような計算結果が得られ、クロスドットアウトの45行目に透過率と統計誤差が出力されています。この統計誤差を考えると、やはり、0.01を超えてしまいますので、透過率が0.01以下に到達したと判定できなくなります。厚さ4.2センチメートル、マックスキャスイコール2000、マックスバッチイコール32の場合、下表のような結果が得られ、0.00959 プラスマイナス 4.06パーセントなので，透過率が0.01以下と考えてよいと判定できるかと思います。

--- SLIDE 15 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ９：中性子入射の場合は？
Step 9
中性子フラックス
ほとんど遮へいできない
入射粒子をγ線から1.0MeVの中性子（=neutron）に変更する
maxbchを3に変更
透過エネルギースペクトル
ほとんど散乱せずに
透過した中性子が80％以上！
SPEAKER_NOTES:
ステップ９の中性子入射の場合に移ります。ここでは、入射粒子をガンマ線から1メブの中性子に変更します。そして、マックスバッチを3に変更してください。トラックドットイーピーエスの4ページ目が中性子フラックスになっています。この結果からも容易に分かりますように、中性子はほとんど遮へいされていないことが確認できるかと思います。また、クロスドットイーピーエスの透過エネルギースペクトルの結果を見てみますと、ほとんど散乱せずに透過した中性子が80パーセント以上であることも確認できるかと思います。

--- SLIDE 16 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
ステップ１０：中性子を効果的に遮へいする
Step 10
黒鉛 約27cm
@GRAPHITE@
遮へい体の素材と厚さを変更して，中性子の透過率が0.01以下になるようにする（71行目sum overの値を見る）
様々な素材を試して，どのような物質が効果的に中性子を遮へいできるか検討してみよう
アルミ 約40cm
@ALUMIMUM@
水 約17cm
@WATER@
元素番号の軽い原子の方が効果的に中性子を遮へい可能
SPEAKER_NOTES:
ステップ10の中性子を効果的に遮へいするに移ります。ここでは、遮へい体の素材と厚さを変更して、中性子の透過率が0.01以下になるようにします。ここでは、クロスドットアウトの71行目のサムオーバーの値を見ていきます。次に、様々な素材を試して、どのような物質が効果的に中性子を遮へいできるか検討してみましょう。こちらは、計算結果の一例で、これらの傾向から、元素番号の軽い原子のほうが効果的に中性子を遮へいできることが確認できたかと思います。

--- SLIDE 17 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
PHITSを用いてα線，β線，γ線，中性子線の透過力を計算し，通説が（ほぼ）正しいことを確認できた

PHITSは，様々な放射線の挙動を解析可能なので，それぞれの特性を包括的に評価することができる
まとめ
Summary
SPEAKER_NOTES:
まとめです。総合実習1では、フィッツを用いてアルファ線、ベータ線、ガンマ線、中性子線の透過力を計算し，通説が（ほぼ）正しいことを確認できたかと思います。フィッツは，様々な放射線の挙動を解析可能なので，それぞれの特性を包括的に評価することができることも実感できたかと思います。

--- SLIDE 18 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Homework
高エネルギー中性子（100MeV）ビームの遮へい設計をする
遮へい設計の指標は，フルエンスではなく実効線量とする
遮へい体内での実効線量を計算し，表面と背面での線量比が1/100以下となる遮へい体で，できるだけ薄いものを探す
遮へい体は，2種類以上の素材を組み合わせてもよい
宿題（難題！）
ヒント
奨励設定「h10multiplier」にある[t-track]を使う
axisをxzからzに変更し，深さ方向の線量をヒストグラムで見る
グラフがたくさん出力されすぎないよう，nx=1とする
低エネルギー中性子は軽い元素の方が遮へいできるが，高エネルギー中性子はある程度重い元素の方が遮へいできる
SPEAKER_NOTES:
最後に宿題です。高エネルギー中性子（100メブ）ビームの遮へい設計をする。遮へい設計の指標は、フルエンスではなく実効線量とする。遮へい体内での実効線量を計算し、表面と背面での線量比が1/100以下となる遮へい体で、できるだけ薄いものを探す。遮へい体は，2種類以上の素材を組み合わせてもよい。とします。ヒントはこちらです。興味のある方は挑戦してみてください。

--- SLIDE 19 ---
PPTX_FILE: phits-range-en.pptx
SLIDE_TEXT:
Homework
回答例（answer1.inp）
考えてみよう
光子による線量寄与はどれくらいあるのか？
鉄遮へい体後方の中性子エネルギースペクトルはどうなっているか？
コンクリートと鉄の順番を逆にするとどうなるか？
鉄（80cm）とコンクリート（25cm）を組み合わせた遮へい体内の線量率深さ分布
鉄
コンクリート
空気
SPEAKER_NOTES:
回答例はこちらになり、answer1.inpを用意しております。以上で、総合実習1を終了致します。
MENTIONED_INPUT_NAMES: answer1.inp

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/range-1.inp
FILE: input/range-3.inp
FILE: input/range-4.inp
FILE: input/range-5.inp
FILE: input/range-6.inp
FILE: input/range-7.inp
FILE: input/range-8.inp
FILE: input/range-9.inp
FILE: input/range-10.inp
FILE: input/range-end.inp

[BONUS_TEXT_FILES]
NOTE: None
