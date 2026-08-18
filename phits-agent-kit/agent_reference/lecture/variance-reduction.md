# Lecture: advanced/variance-reduction

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/variance-reduction
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: variance-reduction
LECTURE_PATH_INDEX: lecture/advanced/variance-reduction
PPTX_FILES: phits-variance-reduction-en.pptx, phits-variance-reduction-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: CI-concept, CI-practice, force, source, WW-concept, WW-practice, WW-practice - コピー
SECTION_KEYWORDS: 25, 26, counter, importance, t-cross, t-let, t-product, t-track, t-wwg

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/variance-reduction
LECTURE_PATH_INDEX: lecture/advanced/variance-reduction
PPTX_FILES: phits-variance-reduction-en.pptx, phits-variance-reduction-jp.pptx
INPUT_DIR_COUNT: 6
MAIN_INPUT_COUNT: 7
SLIDE_COUNT: 118
EXERCISE_SLIDE_COUNT: 30
BONUS_INPUT_COUNT: 16
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- CI-concept/input
- CI-practice/input
- force/input
- source/input
- WW-concept/input
- WW-practice/input

[MAIN_INPUT_FILES]
- CI-concept/CI-concept.inp
- CI-practice/CI-practice.inp
- force/force.inp
- source/source.inp
- WW-concept/WW-concept.inp
- WW-practice/WW-practice - コピー.inp
- WW-practice/WW-practice.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Improvement of Computational Efficacy using Variance Reduction Techniques
- SLIDE 02: Purpose of This Lecture
- SLIDE 03: What is “Variance Reduction Technique”?
- SLIDE 04: In what situation VR is encouraged?
- SLIDE 05: Table of Contents
- SLIDE 06: Source Sampling Methods in PHITS
- SLIDE 07: Cosmic-ray Source Mode
- SLIDE 08: EXERCISE 1 | Exercise 1:Use weight control method
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 09: Answer 1
- SLIDE 10: EXERCISE 2 | [ S o u r c e ]
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 11: Answer 2
- SLIDE 12: Summary for Source Generation with Weight Control
- SLIDE 13: Table of Contents
- SLIDE 14: “Importance” of each cell and particle type is specified in [importance] section.
- SLIDE 15: EXERCISE 1 | Exercise 1：Check trajectory of a neutron
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 16: Answer 1
- SLIDE 17: EXERCISE 2 | Exercise 2: Experience an Inappropriate Setting
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 18: Answer 2
- SLIDE 19: Table of Contents
- SLIDE 20: EXERCISE 1 | Exercise 1：Shielding calculation using [Importance]
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 21: Answer 1
- SLIDE 22: Answer 1 (Cont.)
- SLIDE 23: EXERCISE 2 | [importance]
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 24: Answer 2
- SLIDE 25: Summary for [Importance]
- SLIDE 26: Table of Contents
- SLIDE 27: What is the Weight Window Method?
- SLIDE 28: Comparison of Weight Window and Cell Importance
- SLIDE 29: Parameters Related to Weight Window
- SLIDE 30: EXERCISE 1 | [weight window]
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 31: Answer 1
- SLIDE 32: EXERCISE 2 | [weight window]
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 33: Answer 2
- SLIDE 34: EXERCISE 3 | Exercise 3: Set different WW for each energy mesh
  ANSWER_FILE: WW-practice/input/WW-practice-4.inp
- SLIDE 35: Answer 3
- SLIDE 36: Table of Contents
- SLIDE 37: Automatic Determination of [Weight Window]
- SLIDE 38: How to use [t-wwg]
- SLIDE 39: EXERCISE 1 | Exercise 1: Shielding calculation using [t-wwg]
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 40: Answer 1
- SLIDE 41: set:  c71[0.0000E+00+2.10873E-08]  c72[4.46309E-04]
- SLIDE 42: Special features in [t-wwg]: Part 1
- SLIDE 43: EXERCISE 2 | Exercise 2: Use Low-energy Unbiased Method
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 44: Answer 2
- SLIDE 45: EXERCISE 3 | Exercise 3: Use Particle Navigation Function
  ANSWER_FILE: WW-practice/input/WW-practice-4.inp
- SLIDE 46: Special features in [t-wwg]: Part 2
- SLIDE 47: Answer 3
- SLIDE 48: EXERCISE 4 | Exercise 4: Use Extended Statistical Indicators
  ANSWER_FILE: WW-practice/input/WW-practice-end.inp
- SLIDE 49: Answer 4 (track-reg_StD.eps)
- SLIDE 50: Summary for [weight window] & [t-wwg]
- SLIDE 51: Table of Contents
- SLIDE 52: What is Forced Collision?
- SLIDE 53: EXERCISE 1 | Exercise 1: Reproduce a Thin Target Experiment
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 54: Answer 1
- SLIDE 55: EXERCISE 2 | Exercise 2:
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 56: Answer 2
- SLIDE 57: Summary for [forced collisions]
- SLIDE 58: Table of Contents
- SLIDE 59: Summary
- SLIDE 01: 分散低減法を用いた計算の効率化
- SLIDE 02: 本実習の目標
- SLIDE 03: 分散低減法とは？
- SLIDE 04: どんなときに便利？
- SLIDE 05: 実習内容
- SLIDE 06: 線源のサンプリング方法
- SLIDE 07: 宇宙線線源モード
- SLIDE 08: EXERCISE 1 | 課題１：ウェイト調整法によるエネルギー分布の再現
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 09: 解答1
- SLIDE 10: EXERCISE 2 | 課題2：マルチソースに対するウェイト調整法
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 11: 解答2
- SLIDE 12: 「分散低減法を用いた線源発生」のまとめ
- SLIDE 13: 実習内容
- SLIDE 14: Cell Importance法とは？
- SLIDE 15: EXERCISE 1 | 課題1：１ヒストリーのときの中性子飛跡を確認
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 16: 解答1
- SLIDE 17: EXERCISE 2 | 課題2：不適切なImportance設定を体感する
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 18: 解答2
- SLIDE 19: 実習内容
- SLIDE 20: EXERCISE 1 | 課題1：[Importance]を使った遮蔽計算
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 21: 解答1
- SLIDE 22: 解答1（続き）
- SLIDE 23: EXERCISE 2 | 課題2：不適切なImportance設定を体感する
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 24: 解答2
- SLIDE 25: [Importance]のまとめ
- SLIDE 26: 実習内容
- SLIDE 27: Weight Window法とは？
- SLIDE 28: Weight WindowとCell Importanceの違い
- SLIDE 29: Weight Window法に関連するパラメータ
- SLIDE 30: EXERCISE 1 | 課題1：１ヒストリーのときの中性子飛跡を確認
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 31: 解答1
- SLIDE 32: EXERCISE 2 | 課題2：不適切なweight window設定を体感する
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 33: 解答2
- SLIDE 34: EXERCISE 3 | 課題3：エネルギー群毎に異なるWeight Windowを設定
  ANSWER_FILE: WW-practice/input/WW-practice-4.inp
- SLIDE 35: 解答3
- SLIDE 36: 実習内容
- SLIDE 37: [Weight Window]の自動決定機能
- SLIDE 38: [t-wwg]の利用手順と注意点
- SLIDE 39: EXERCISE 1 | 課題1：[t-wwg]を使った遮蔽計算
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 40: 解答1
- SLIDE 41: set:  c71[0.0000E+00+2.10873E-08]  c72[4.46309E-04]
- SLIDE 42: 計算効率を更に高める工夫①
- SLIDE 43: EXERCISE 2 | 課題2：低エネルギー・アンバイアス法を活用
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 44: 解答2
- SLIDE 45: 計算効率を更に高める工夫②
- SLIDE 46: EXERCISE 3 | 課題3：粒子誘導機能を活用
  ANSWER_FILE: WW-practice/input/WW-practice-4.inp
- SLIDE 47: 解答3
- SLIDE 48: EXERCISE 4 | 課題4：統計指標出力機能を活用
  ANSWER_FILE: WW-practice/input/WW-practice-end.inp
- SLIDE 49: 解答4（track-reg_StD.eps）
- SLIDE 50: [weight window]&[t-wwg]のまとめ
- SLIDE 51: 実習内容
- SLIDE 52: 強制衝突法とは？
- SLIDE 53: EXERCISE 1 | 課題１:薄膜を用いた断面積測定実験を模擬しよう
  ANSWER_FILE: WW-practice/input/WW-practice-2.inp
- SLIDE 54: 解答1
- SLIDE 55: EXERCISE 2 | 課題2:強制衝突で生成された2次粒子を輸送しよう
  ANSWER_FILE: WW-practice/input/WW-practice-3.inp
- SLIDE 56: 解答2
- SLIDE 57: [forced collisions]のまとめ
- SLIDE 58: 実習内容
- SLIDE 59: 全体のまとめ

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: CI-concept/CI-concept.inp
FILE: CI-practice/CI-practice.inp
FILE: force/force.inp
FILE: source/source.inp
FILE: WW-concept/WW-concept.inp
FILE: WW-practice/WW-practice - コピー.inp
FILE: WW-practice/WW-practice.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Improvement of Computational Efficacy using Variance Reduction Techniques
Jan. 2025 revised
phits/lecture/advanced/variance-reduction
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Purpose of This Lecture
Learn how to speed up time-consuming calculations such as shielding calculation using various variance reduction techniques
Without variance reduction
With variance reduction
(Most radiation stop at a shallow depth)
(Radiation reach the depth of shield)

--- SLIDE 03 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
What is “Variance Reduction Technique”?
Artificially increase the occurrence probability of the event of interest and, in turn, reduce the Monte Carlo weight, wi , of the generated particles to lower their contribution to the tally for each particle.
The average value of the tally results does not change significantly, but its statistical error is reduced* because the tallying frequency increases and the variance between histories in the tally results decreases.
*In contrast, the statistical error due to non-biased events sometimes increases
Increase xi & decrease wi

--- SLIDE 04 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
In what situation VR is encouraged?
The source spectrum is so soft that high-energy particles, which are important for tallies, are rarely generated
Solution : Produce an equal number of particles for each source energy bin and adjust their weights to match the original source spectrum → [source]
Most particles stop at a shallow depth in shielding. Consequently, the statistical uncertainties of tally results at deeper locations are excessively  large
Solution : Split particles to let fraction of particles reach depth of shielding → [importance], [weight window], [t-wwg]
The probability of nuclear reaction is so low that secondary particles are rarely tallied
Solution : Enforce nuclear reactions to happen in the target region. The resulted secondary particle weights are reduced to conserve statistical significance → [forced collision]

--- SLIDE 05 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Table of Contents
Source Generation with Weight Control (source)
Cell Importance Method

Weight Window Method

Forced Collision (force)
Summary
Concept (CI-concept)
Practice (CI-practice)
Concept (WW-concept)
Practice (WW-practice)
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 06 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Source Sampling Methods in PHITS
Number control method (useful in most cases)

Weight control method (useful when sources with low intensity have high impact to tally)
e-type in [source] section*
*No rule in the numbering. No relation with e-type in tally sections
Sample sources with particle number proportional to the source intensity
Sample sources uniformly with weight proportional to the source intensity

--- SLIDE 07 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Cosmic-ray Source Mode
PHITS has a function to reproduce cosmic-ray environments in space and in the atmosphere by simply specifying the time and location of interest*
Protons with several GeV are the main component of cosmic rays, but high-energy particles over 100 GeV and heavy ions (e.g., Fe) are also present
*See phits/lecture/advanced/cosmicray in more detail
Example of cosmic-ray flux in space
Such high-energy / heavy ions are very important in cosmic-ray dosimetry, but they are rarely produced by sampling-number control method due to their low abundance
The weight control method is useful for improving the efficacy of the cosmic-ray simulation

--- SLIDE 08 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1:Use weight control method
Cosmic-ray mode with number control method
(e-type =25).
Define proton, He, Fe ions as multi-sources
Target: Si detector with 1cm2 and 0.2 mm thickness
Tally：[t-track] Energy distribution in Si detector
        [t-let] LET distribution in Si detector
source-track.eps
[ S o u r c e ]
set:c1[1.0]  $ Radius
set:c2[25]   $ e-type

  totfact =  pi*c1**2
 <source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  c2
    icenv =   0
 solarmod =   0.0000
    rigid =   0.0000
   proj   = proton
…
source.inp
Si
source-let.eps
Large uncertainties at high energy and LET ranges
Let’s use the weight control method (e-type = 26) for source generation
Source:

Target:
Tally:
Simulation Conditions
MENTIONED_INPUT_NAMES: source.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 09 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 1
source-track.eps
[ S o u r c e ]
set:c1[1.0]  $ Radius
set:c2[26]   $ e-type

  totfact =  pi*c1**2
 <source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  c2
    icenv =   0
 solarmod =   0.0000
    rigid =   0.0000
   proj   = proton
…
source.inp
The statistical uncertainty at higher energies is improved.
Conversely, the statistical accuracy in the intermediate energy range is compromised.
Fe ions are still rarely generated
Uncertainties become slightly larger
Much smaller
MENTIONED_INPUT_NAMES: source.inp

--- SLIDE 10 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
[ S o u r c e ]
set:c1[1.0]  $ Radius
set:c2[26]   $ e-type

  totfact =  pi*c1**2
 <source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  c2
    icenv =   0
 solarmod =   0.0000
    rigid =   0.0000
   proj   = proton
…
source.inp
When totfact is negative, the weight control method is used to sample a source from multiple sources.
Exercise 2
Let’s use weight control method for multi-source sampling
Equal number of sources are sampled from each multi-source and their weights are adjusted based on their relative intensities
MENTIONED_INPUT_NAMES: source.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 11 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 2
source-track.eps
[ S o u r c e ]
set:c1[1.0]  $ Radius
set:c2[26]   $ e-type

  totfact =  -pi*c1**2
source.inp
Fe ions are generated and the peak due to Fe ions is observed in LET distribution
source-let.eps
Peak due to Fe ions
MENTIONED_INPUT_NAMES: source.inp

--- SLIDE 12 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Summary for Source Generation with Weight Control
When multi-source is used, source particles are sampled using either number or weight control methods.
The weight control method for energy distributions can be invoked by using designated e-type.
The weight control method for multi-source, use negative totfact.
The weight control method can be also applied to angular and time distributions by using designated a-type and t-type parameters, respectively.

--- SLIDE 13 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Table of Contents
Source Generation with Weight Control (source)
Cell Importance Method

Weight Window Method

Forced Collision (force)
Summary
Concept (CI-concept)
Practice (CI-practice)
Concept (WW-concept)
Practice (WW-practice)
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 14 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
“Importance” of each cell and particle type is specified in [importance] section.
Default value of importance is 1.0 except for outer void cell where importance = 0.
When particles enter a region of higher importance from a region of lower importance, particle splitting occurs according to the ratio of importance, and the weight of all particles decreases.
When particles enter a region of lower importance from a region of higher importance, Russian roulette is performed according to the ratio of importance, and the weight of the surviving particles increases.
W=1
W=1/3
W=1/3
W=1/3
I1=1
I2=3
Split into I2/I1*
Particle splitting
*Decide the splitting numbers using a random number when I2/I1 is not an integer
W=1
I1=1
I2=1/2
Survive with the probability of I2/I1
Russian Roulette
W=1
W=2
Killed
What is Cell Importance Method?

--- SLIDE 15 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1：Check trajectory of a neutron
[importance]
part = neutron
reg imp
10  1.0
1   1.0
2   1.0
CI-concept.inp
Run CI-concept.inp and check importance-track.eps
Increase “imp” of reg 1 to 2.0 and reg 2 to 4.0 and confirm the change of trajectory
I10=1.0
I1=1.0
I2=1.0
Air
5MeV
neutron
Concrete
(radius 20 cm,
depth 8 cm x 2)
importance-track.eps (Initial setting)
MENTIONED_INPUT_NAMES: CI-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 16 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 1
[importance]
part = neutron
reg imp
10  1.0
1   2.0
2   4.0
importance-hist.inp
importance-track.eps
Splitting into two neutrons here
One neutron causes a reaction here
I10=1.0
I1=2.0
I2=4.0
Air
5MeV
neutron
Concrete
(radius 20 cm,
depth 8 cm x 2)
MENTIONED_INPUT_NAMES: importance-hist.inp

--- SLIDE 17 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2: Experience an Inappropriate Setting
[importance]
part = neutron
reg imp
10  1.0
1   2.0
2   4.0
CI-concept.inp
If the importance ratio between two neighboring cells is too large, a particle splits into too many particles, wasting computational resources.
Let’s change the importance of cell 2 to 100 and check the trajectory
I10=1.0
I1=2.0
I2=4.0
Air
5MeV
neutron
Concrete
(radius 20 cm,
depth 8 cm x 2)
MENTIONED_INPUT_NAMES: CI-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 18 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 2
[importance]
part = neutron
reg imp
10  1.0
1   2.0
2   100.0
importance-hist.inp
importance-track.eps
Warning message due to too much splitting
Fluence become higher around the point of entrance by chance
*Reference：“A Sample Problem for Variance Reduction in MCNP” LA-10363-MS DE86 004380
I10=1.0
I1=2.0
I2=100.0
Air
5MeV
neutron
Concrete
(radius 20 cm,
depth 8 cm x 2)
It is advisable to set the importance so as to make their ratio 2-3 between neighboring cells.
MENTIONED_INPUT_NAMES: importance-hist.inp

--- SLIDE 19 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Table of Contents
Source Generation with Weight Control (source)
Cell Importance Method

Weight Window Method

Forced Collision (force)
Summary
Concept (CI-concept)
Practice (CI-practice)
Concept (WW-concept)
Practice (WW-practice)
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 20 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1：Shielding calculation using [Importance]
[importance] off
part = neutron
reg imp
1   2.5**0
2   2.5**1
3   2.5**2
4   2.5**3
5   2.5**4
6   2.5**5
7   2.5**6
8   2.5**7
9   2.5**8
10   2.5**9
11   2.5**10
12   2.5**11
CI-practice.inp
Run PHITS with CI-practice.inp and check the results including computational time*
Activate [importance] by removing “off”, run PHITS, and check the results and computational time
Cylindrical concrete with radius of 50 cm and depth of 180 cm
Concrete is divided into 12 layers to assign different importance values
Source is 14 MeV neutrons directed to +z axis.
Simulation condition
14MeV
neutron
Set Ii+1/Ii = 2.5
*Computational time is found around line 400 of phits.out
MENTIONED_INPUT_NAMES: CI-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 21 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 1
importance-dose-xz_err.eps
Without [importance], total cpu time = 5.36 sec*
With [importance], total cpu time = 24.39 sec*
importance-dose-xz.eps

--- SLIDE 22 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 1 (Cont.)
Without [importance]
With [importance]
importance-dose-rz.eps
With an increase of depth by (1/macroscopic cross section) (cm), fluence of incident neutrons is expected to decrease by 1/e
By dividing the shielding material into sections with a width of approximately (1/macroscopic cross section) and setting the importance ratio to 𝑒, particles are delivered almost uniformly to each layer.*
*In practice, it is necessary to consider secondary particles,
  therefore the ideal width is slightly larger than (1/macroscopic cross-section)

--- SLIDE 23 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
[importance]
part = neutron
reg imp
1   2.5**0
2   2.5**0
3   2.5**0
4   2.5**0
5   2.5**0
6   2.5**5
7   2.5**6
8   2.5**7
9   2.5**8
10   2.5**9
11   2.5**10
12   2.5**11
CI-practice.inp
Set the importances of cells 1 – 5 to 1.0, while leaving the importance of the other cells as is.
Run PHITS and check the statistical uncertainties of the calculation results.
Exercise 2: Experience an inappropriate Setting
There is a huge importance gap between the cells 5 and 6 (=2.55 ~ approximately 100)
MENTIONED_INPUT_NAMES: CI-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 24 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 2
importance-dose-xz_err.eps
With appropriate [importance] total cpu time = 24.39 sec
importance-dose-xz.eps
With inappropriate [importance] total cpu time = 16.49 sec
Huge gap at the boundary with large Ii+1/Ii

--- SLIDE 25 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Summary for [Importance]
Shielding calculations (especially deep penetration calculations) can be accelerated using the Cell Importance method.
[Importance] must be assigned to each cell, and the shielding material must be divided so that the importance ratio between neighboring cells is 2~3.
To set [Importance] properly, macroscopic cross-section is required.
If the settings are inappropriate, it may result in calculation delays or errors due to insufficient memory.

--- SLIDE 26 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Table of Contents
Source Generation with Weight Control (source)
Cell Importance Method

Weight Window Method

Forced Collision (force)
Summary
Concept (CI-concept)
Practice (CI-practice)
Concept (WW-concept)
Practice (WW-practice)
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 27 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
What is the Weight Window Method?
Users define an acceptable range of weight, called weight window, of each region (cell) or xyz mesh.
Weight window does not have a default setup.
The weight window can be dependent on both particle species and energy.
If a particle with a weight outside the weight window enters or is generated, its weight is adjusted by particle splitting or by Russian roulette*.
Weight
WU=2.5
WU=1.25
WU=0.75
Cell 1
Cell 2
Cell 3
WL=0.5
WL=0.25
WL=0.15
W=1
W=0.5
W=0.5
Cell 4
WU=3.0
W=1.8
WL=0.6
killed
*Weight is adjusted to Wu*0.6 after Russian roulette

--- SLIDE 28 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Comparison of Weight Window and Cell Importance
In the Cell Importance method, only the ratio of importance between the two neighboring cells matters, whereas in the Weight Window method, the absolute value is important.

The Weight Window can be dependent on both particle species and energy.

The Weight Window is compatible with both reg and xyz meshes

Weight window setup is automatized by [t-wwg]
→Particle weights converge to similar values, leading to low statistical errors
→Allows focusing on the transport of high-energy (more penetrating) particles
→No need to divide shielding into many slices in geometry definition
→You don’t have to know macroscopic cross section to use [weight window], though some experience is still necessary

--- SLIDE 29 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Parameters Related to Weight Window
wupn: Ratio of upper to lower limits of allowed weight (D=5.0)
mxspln: Maximum number of split per event (D=5.0)
mwhere: Timing of weight window splitting and RR(D=0)
        -1: reaction, 0: both, 1: surface crossing
These parameters are defined in [parameters] section.
See manual “5.2.4 Cut off time, cut off weight, and weight window” for more detail.

--- SLIDE 30 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
[weight window]
part = neutron
reg ww1
1   0.25
2   0.25
WW-concept.inp
5MeV
neutron
weight-track.eps (initial setting)
Air
Water
（radius 10cm，
Depth 5cm x 2)
Exercise 1：Check trajectory of a neutron
Run WW-concept.inp and check weight-track.eps
Decrease “WW1” of reg 2 to 0.125 and confirm the change of trajectory
MENTIONED_INPUT_NAMES: WW-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 31 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 1
weight-track.eps
[weight window]
part = neutron
reg ww1
1   0.25
2   0.125
WW-concept.inp
Weight
WU=1.25
WU=0.625
Cell 10
Cell 1
Cell 2
WL=0.25
WL=0.125
W=1
W=0.5
W=0.5
(no restriction)
Already splitting into two neutrons here
One neutron causes reaction here
MENTIONED_INPUT_NAMES: WW-concept.inp

--- SLIDE 32 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
[weight window]
part = neutron
reg ww1
1   0.25
2   0.125
WW-concept.inp
weight-track.eps
How will this trajectory change?
Exercise 2: Experience an Inappropriate Setting
If the weight-window ratio between two neighboring cells is too large, a particle splits into too many particles, wasting computational resources.
Let’s change the WW1 of cell 2 to 0.005 and check the trajectory
MENTIONED_INPUT_NAMES: WW-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 33 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 2
weight-track.eps
Numbers of particles gradually increase because the maximum number per splitting is 5（mxspln=5）
[weight window]
part = neutron
reg ww1
1   0.25
2   0.005
WW-concept.inp
Weight
WU=1.25
WU=0.025
WL=0.25
WL=0.005
W=1
W=0.04
W=0.2
W=0.008
Cell 10
Cell 1
Cell 2
(no restriction)
It is advisable to set the weight window so as to make their ratio 2-3 between neighboring cells.
MENTIONED_INPUT_NAMES: WW-concept.inp

--- SLIDE 34 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3: Set different WW for each energy mesh
Deactivate the 1st [weight window], while activate the 2nd [weight window] by adding and removing “off”, respectively, after the section name
[weight window]
part = neutron
reg  ww1
1   0.25
2   0.005

[weight window] off
part = neutron
eng = 2
     0.01     1.0e5
reg  ww1      ww2
1    0.25*10  0.25
2    0.125*10 0.125
WW-concept.inp
Set 10-times higher values for the lower energy bin
Maximum energy of each energy bin
(the lowest energy of the 1st bin is 0 by default)
Number of energy bins (required when eng > 1)
MENTIONED_INPUT_NAMES: WW-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-4.inp

--- SLIDE 35 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 3
weight-track.eps
Neutrons reached 0.01 MeV at these points, being killed by Russian Roulette
WW-concept.inp
[weight window] off
part = neutron
reg  ww1
1   0.25
2   0.005

[weight window]
part = neutron
eng = 2
     0.01     1.0e5
reg  ww1      ww2
1    0.25*10  0.25
2    0.125*10 0.125
without eng parameter
(single energy bin)
By increasing the lower limit of the Weight Window for the low-energy group, low-energy particles that do not contribute to the deep penetration calculation tend to be killed by Russian Roulette. Computational time is consequently reduced.
MENTIONED_INPUT_NAMES: WW-concept.inp

--- SLIDE 36 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Table of Contents
Source Generation with Weight Control (source)
Cell Importance Method

Weight Window Method

Forced Collision (force)
Summary
Concept (CI-concept)
Practice (CI-practice)
Concept (WW-concept)
Practice (WW-practice)
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 37 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Automatic Determination of [Weight Window]
To make the statistical error of tally results uniform within a certain region, the Monte Carlo particle density* must be uniform in the region.
To achieve uniform Monte Carlo particle density, it is advisable to set the lower limit of the weight window proportional to the fluence because particle splitting more frequently occurs in low-fluence regions for increasing Monte Carlo particle density.
We developed [t-wwg] (tally for weight window generator) that calculate the particle fluence like [t-track] and automatically create [weight window] based on the results of [t-track]
*The number of particles that actually passed through a certain region in a Monte Carlo simulation. It is almost synonymous with the particle fluence disregarding weights.
Strategy

--- SLIDE 38 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
How to use [t-wwg]
Procedures
Set [t-wwg] in the region where you want to uniformize the statistical uncertainties of tally results and run PHITS.
Include the output file of [t-wwg] ([weight window] section) into the PHITS input file using “infl” command and run PHITS a few more times.

Perform the final calculation with a large number of histories.
→ Generated [weight window] is gradually optimized
An error occurs if the xyz spatial mesh surface of [t-wwg] completely matches the geometry surface. Note that it is automatically avoided if the overlapping surface coordinate is integer.
If the spatial mesh or energy mesh of [t-wwg] are too small*, the statistical error of the output [weight window] becomes large. → Result in increase in the computational time due to unnecessary particle splitting and Russian roulette.
Care should be taken in defining the region of [t-wwg] because a huge number of particle splittings may occur when particles enter a region with [t-wwg] from a region without [t-wwg].
Notices
*For spatial mesh, approximately 15 cm (1/macroscopic cross-section) is recommended in the case of  concrete.
For energy mesh, it is encouraged to use a single group and apply the low-energy unbiased method.

--- SLIDE 39 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1: Shielding calculation using [t-wwg]
[ T - WWG ]
  mesh = xyz
x-type = 2
  xmin = -c1
  xmax =  c1
    nx = 5
y-type = 2
  ymin = -c1
  ymax =  c1
    ny = 1
z-type = 2
  zmin =  0
  zmax =  c2
    nz =  12
   part = all
   e-type = 1
       ne = 1
     0   1e5
axis = xz
file =  wwg-xz.out
axis =  wwg
file =  wwg.out
WW-practice.inp
Concrete cylinder with 100 cm radius and 180 cm depth*
Two targets at deep upper and lower locations in the cylinder for calculating the doses
Simulation condition
14MeV
neutron
Tally output files
*In different from [importance], it is not necessary to divide the shielding object into many pieces
wwg.out: [weight window] output from [t-wwg]
wwg-xz.eps: Spatial distribution of [weight window] from [t-wwg]
track-xz.eps: Spatial distribution of effective doses
track-rz.eps: Depth distribution of effective doses
track-reg.out: Effective doses in the target regions
Run PHITS with WW-practice.inp and check wwg.out
Activate infl:{wwg.out} at line 11 and run PHITS twice
Check computational time and tally results
MENTIONED_INPUT_NAMES: WW-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 40 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 1
track-xz.eps
Optimized [weight window] is automatically generated
and statistical uncertainties are rather uniform everywhere
track-xz_err.eps
track-rz.eps
#  num    reg     volume       all       r.err
    1       2   1.1310E+05   1.1202E-06  0.4438
    2       3   1.1310E+05   1.5993E-06  0.3036
track-reg.out (line around 45)
sec
total cpu time = 32.01
phits.out (line around 550)

--- SLIDE 41 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
set:  c71[0.0000E+00+2.10873E-08]  c72[4.46309E-04]

   part = all
    eng =  1
         1.00000E+05

   xyz                 ww1
  (1 1  1)  (1.21073E-06+c71)/c72
  (1 1  2)  (2.07578E-06+c71)/c72
  (1 1  3)  (2.27569E-06+c71)/c72
...
Answer 1 (Cont.)
lower 10%ile of fluence
wwg.out (around line 30)
the maximum fluence
× wwmax*
fluence in each mesh
lower limit of weight window in each mesh
fluence in each mesh + lower 10%ile of fluence
the maximum fluence x normalization factor
*specified in input file. Default value is 0.99
Lower 10%ile of fluence is added as a measure to ensure that the weight window lower limit does not become 0 in regions where the fluence is 0.
=

--- SLIDE 42 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Special features in [t-wwg]: Part 1
Low-energy Unbiased Method
A feature that reduces the Monte Carlo particle density on the low-energy side and shortens computation time by multiplying the lower limit of the weight window below a certain threshold energy by a constant factor.
elowthre: (D=0.0) The threshold energy. 0 means “disable this feature”
elowbias: (D=5.0) The constant factor for multiplying the lower limit of weight window for the energy bin below the threshold
Particularly effective for neutron shielding calculations, where a large part of the computational time is spent on low-energy neutron transport

--- SLIDE 43 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2: Use Low-energy Unbiased Method
[ T - WWG ]
axis = xz
file =  wwg-xz.out
axis =  wwg
file =  wwg.out
epsout = 1
$ elowthre = 0.01
WW-practice.inp
Activate “elowthre” in [t-wwg] and run PHITS twice

Check computational time and tally results
(1st run for re-generating wwg.out, while
 2nd run for calculating doses using the updated wwg.out)
80% of secondary particles with energies below 0.01 MeV are killed by Russian Roulette when they are generated
elowthre: (D=0.0) The threshold energy. 0 means “disable this feature”
elowbias: (D=5.0) The constant factor for multiplying the lower limit of weight window for the energy bin below the threshold
Remember…
MENTIONED_INPUT_NAMES: WW-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 44 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 2
track-xz.eps
The same statistical quality was achieved, cutting the computational time in half!
track-xz_err.eps
track-rz.eps
#  num    reg     volume       all       r.err
    1       2   1.1310E+05   1.1040E-06  0.3021
    2       3   1.1310E+05   7.3123E-07  0.4058
sec
total cpu time = 16.12
track-reg.out (line around 45)
phits.out (line around 550)

--- SLIDE 45 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3: Use Particle Navigation Function
[ T - WWG ]
axis = xz
file =  wwg-xz.out
axis =  wwg
file =  wwg.out
epsout = 1
elowthre = 0.01
$ chwei(1) = 10.0
…
[counter]
counter = 1
part=neutron
reg  in
2     1
WW-practice.inp
A [weight window] will be created to guide more particles towards region 2
Counter +1 when a neutron goes into region 2
Activate “chwei(1)” in [t-wwg] and run PHITS twice

Check computational time and tally results
(1st run for re-generating wwg.out, while
 2nd run for calculating doses using the updated wwg.out)
chwei(i): (D=0.0) Magnitude of particle-navigation capability in the generated [weight windows] using i-th history counter. Its approximately value is 10 ~ 100
MENTIONED_INPUT_NAMES: WW-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-4.inp

--- SLIDE 46 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Special features in [t-wwg]: Part 2
Particle Navigation Function
A feature that navigates the particles to a region of interest, using the history-counter function*. This feature is particularly effective in duct streaming calculations.
chwei(i): (D=0.0) Magnitude of particle-navigation capability in the generated [weight windows] using i-th history counter
chplane: (D=all) A plane perpendicular to the duct (xy, yz, xz) in the case of duct streaming calculation
T. Sato et al. Nucl. Instr. Meth. B 557, 165535 (2024)
*A function to tag particles that have followed specific paths or undergone specific reactions.
See phits/lecture/advanced/options for more detail
Particularly effective when you want to improve the statistics at a specific location rather than overall

--- SLIDE 47 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 3
track-xz.eps
The computation time slightly increased, but more particles were guided upward, reducing the statistical error of the dose in region 2 (upper target) compared with that in region 3 (lower target)
track-xz_err.eps
track-rz.eps
#  num    reg     volume       all       r.err
    1       2   1.1310E+05   1.0526E-06  0.2211
    2       3   1.1310E+05   1.7793E-06  0.3509
sec
total cpu time = 32.77
track-reg.out (line around 45)
phits.out (line around 550)

--- SLIDE 48 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4: Use Extended Statistical Indicators
[ P a r a m e t e r s ]
 icntl    =           0
 maxcas   =        1000
 maxbch   =          4
 file(6)  = phits.out
 $ itall = 3
...
[ T-track ]
   mesh = reg
    reg = 2 3
...
iextstat = 1
anatally start
anatally end
WW-practice.inp
Increase maxbch to 20
Activate “itall =3” and run PHITS

Check track-reg_StD.eps
The extended statistical indictor function is applied to tallies with “anatally start”, “anatally end”, and “iextstat = 1”
When [weight window] (or [importance]) is used, only 1 history simulation could significantly change the tally results.
It cannot be always true that the statistics are sufficient when the statistical uncertainties are high.
*See manual “6.10 Extended statistical indicators” in more detail
Procedures
It is advisable to check the variance of tally results with batches using extended statistical indicator function by setting itall = 3*
Effective only when itall = 3
MENTIONED_INPUT_NAMES: WW-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-end.inp

--- SLIDE 49 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 4 (track-reg_StD.eps)
Extended statistical indictors (page 1)
Change of tally results & relative errors with batches (2nd and 3rd pages)
These results suggest…
After a few batches, no batch significantly changed the tally results → The results are likely reasonable.

--- SLIDE 50 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Summary for [weight window] & [t-wwg]
[Weight window] combined with [t-wwg] maximizes the calculation speed.
The spatial and energy meshes of [t-wwg] should not be set too finely.
Low-energy unbiased method and particle navigation function can further improve computational efficiency.
When using variance reduction techniques, rare events may occur that could change the tally results dramatically in one history. Thus, it is advisable to check the variance of tally results with batches using the extended statistical indicator function (itall=3).

--- SLIDE 51 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Table of Contents
Source Generation with Weight Control (source)
Cell Importance Method

Weight Window Method

Forced Collision (force)
Summary
Concept (CI-concept)
Practice (CI-practice)
Concept (WW-concept)
Practice (WW-practice)
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 52 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
What is Forced Collision?
A variance reduction technique to force a radiation collide within a target
Splitting into two particles
Forced collision cell
Weight of uncollided particle:
Wi×exp(-Sd)
Collided particle
Incident particle with Wi
S: Macroscopic cross section
d: Distance across the target
Uncollided particle
Weight of collided particle:
Wi×{1-exp(-Sd)}
Reduces ‘air-shot’ events and minimizes statistical errors with fewer histories.
Effective to calculate reactions in thin targets or those by low-energy charged particles
ｆｃｌ：Forced collision factor
fcl = -1: apply forced collision only to particles entering the cell (weight cut-off is not applied)
fcl =  1: apply forced collision to all particles up to weight cutoff(weight cut-off is applied)
(In most cases, fcl = -1)
d
Collide position is decided by cross section at random

--- SLIDE 53 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1: Reproduce a Thin Target Experiment
[t-product]: Energy distributions of charged particles produced in the target → true cross section
[t-cross]: Energy distributions of charged particles incident to the detector → measured cross section
force.inp
[ P a r a m e t e r s ]
 icntl    =           0
maxcas   =      5000
 maxbch   =           5
…
[Forced Collisions] off
part = proton
reg  fcl
1   -1.0
Si target with 0.5 cm radius & 10μm thickness
100MeV proton
Detector
Void
Run PHITS with force.inp and confirm that few reactions occur in the target
Activate [forced collisions], run PHITS again, and confirm that many reactions occur
track-xz.eps without [forced collisions]
Tallies in force.inp
MENTIONED_INPUT_NAMES: force.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 54 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 1
product.eps
Many secondary particles are generated and scored by [t-product].
However most of them are killed by weight-cut off due to their weights being too low → Not scored by [t-cross] and [t-track]
cross.eps

--- SLIDE 55 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2:
Transport secondary particles created via forced collision
force.inp
[ P a r a m e t e r s ]
 icntl    =           0
maxcas   =      5000
 maxbch   =           5
$ wc2(1)   = 1.0E-12 # weight cutoff of proton
$ wc2(18)  = 1.0E-12 # weight cutoff of Alpha
$ wc2(19)  = 1.0E-12 # weight cutoff of Nucleus
Reduce the weight cut-off parameter “wc2” for protons, alpha, and heavy ions (particle ID = 1, 18, and 19) to be an extremely low value (10-12)
Run PHITS and compare product.eps with cross.eps
*When a particle with weight below wc2 is generated, its fate is determined by Russian Roulette
Do they agree with each other? If not, let’s consider why?
MENTIONED_INPUT_NAMES: force.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 56 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Answer 2
product.eps
Most of secondary protons and alpha particles arrived at the detector (cross.eps ~ product.eps)
The measured cross sections (cross.eps) for Si are much lower than the corresponding true cross sections (product.eps) because most Si ions stopped in the target
This tendency suggests that the production cross sections of recoil nucleus cannot be measured even if the target is very thin (10μm)
cross.eps

--- SLIDE 57 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Summary for [forced collisions]
To calculate reactions of low probability, use [forced collision] to achieve high computation efficiency.

To transport forced collision products, consider decreasing the weight cutoff (wc2) for secondary particles.

--- SLIDE 58 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Table of Contents
Source Generation with Weight Control (source)
Cell Importance Method

Weight Window Method

Forced Collision (force)
Summary
Concept (CI-concept)
Practice (CI-practice)
Concept (WW-concept)
Practice (WW-practice)
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 59 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Summary
Appropriate use of variance reduction methods allows efficient execution of computationally intensive calculations, such as cosmic-ray analysis, shielding design, and thin-target calculations*.
However, wrong settings may cause delay or memory errors.
Additionally, their effectiveness is limited for inherently time-consuming simulations such as track-structure simulations, heavy-ion nuclear reaction calculations, and medical physics simulation requiring very high accuracy.
*Simulation without changing weight
It is important to understand their mechanisms
and to use them appropriately in the right context

--- SLIDE 01 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
分散低減法を用いた計算の効率化
2025年1月改訂
phits/lecture/advanced/variance-reduction
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
本実習の目標
厚いコンクリートに対する遮蔽計算など、通常の手法では計算時間の掛かるシミュレーションを効率的に実施する手法を学習する
分散低減法を利用しない計算
分散低減法を利用した計算
（遮蔽体の浅い場所で粒子が止まってしまう）
（遮蔽体の深い場所まで粒子が到達する）

--- SLIDE 03 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
分散低減法とは？
注目したい事象の発生確率を人為的に高くし、その分、発生した粒子のウェイト wi （モンテカルロ計算におけるその粒子の重要度）を小さくして各粒子のタリーへの寄与を下げる
タリー結果の平均値は大きく変わらないが、タリーされる頻度が上がり、タリー結果の各ヒストリー間における分散が低減されるため、統計誤差が小さくなる*
*逆に、注目しなかった事象に関連するタリーの統計誤差は大きくなる場合がある
xiを上げてwiを下げる

--- SLIDE 04 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
どんなときに便利？
線源スペクトルが低エネルギー側に偏っていて、より重要な高エネルギー粒子がほとんど発生しない
低エネルギーから高エネルギーまで同じ数の粒子を発生させ、そのウェイトを調整することによりスペクトルを再現する → [source]
遮蔽計算でほとんどの粒子が壁の浅い場所で止まってしまい、深い場所における統計が溜まらない
ある程度深い場所に到達した粒子を強制的に分割してウェイトを下げ、より深い場所まで到達する確率を上げる → [importance], [weight window], [t-wwg]
核反応の発生頻度が低すぎてその2次粒子による寄与を評価できない
2次粒子を発生させたいターゲット内で強制的に核反応を発生させ、本来の発生頻度に合わせてウェイトを調整する → [forced collision]

--- SLIDE 05 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
実習内容
分散低減法を用いた線源発生(source)
Cell Importance法

Weight Window法

強制衝突法（force）
まとめ
概念（CI-concept)
実践（CI-practice）
概念（WW-concept）
実践（WW-practice）
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 06 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
線源のサンプリング方法
粒子数調整法: 線源強度に比例して高い頻度で線源をサンプリング
ウェイト調整法：均一の頻度でサンプリングし、ウェイトを強度に比例させる
[source]セクションにおけるe-type*
*番号に法則性はない。タリーのe-typeとは無関係であることに注意。
エネルギー分布の場合はe-typeにより粒子数調整法とウェイト調整法が選択される
→強度は低いが計算結果に大きな影響を与える線源がある場合に有効

--- SLIDE 07 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
宇宙線線源モード
PHITSでは、時間や場所を指定するだけで宇宙空間及び大気圏内における宇宙線フラックスを再現する機能がある*
宇宙線には、100GeV以上の高エネルギー粒子や鉄イオンなどの重い元素が含まれる
*宇宙線線源モードの詳細はphits/lecture/advanced/cosmicray参照
宇宙空間における銀河宇宙線フラックスの例
それらの粒子は宇宙放射線防護上重要だが数が少ないため、存在比に比例した通常のサンプリング方法（粒子数調整法）ではほとんど発生しない
ウェイト調整法を用いて全てのエネルギー範囲やMulti-sourceから均一に線源を発生させることにより計算を効率化できる

--- SLIDE 08 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１：ウェイト調整法によるエネルギー分布の再現
線源：頻度調整法による宇宙線線源（e-type = 25）
     （陽子、He、Feイオンをそれぞれmulti-sourceで定義）
ターゲット：厚さ0.2mmのSi検出器（1cm2)
タリー：[t-track] 検出器内のエネルギー分布
       [t-let] 検出器内のLET分布
source-track.eps
[ S o u r c e ]
set:c1[1.0]  $ Radius
set:c2[25]   $ e-type

  totfact =  pi*c1**2
 <source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  c2
    icenv =   0
 solarmod =   0.0000
    rigid =   0.0000
   proj   = proton
…
source.inp
Si
source-let.eps
高エネルギーや高LET側は頻度が低いため統計誤差が大きい
ウェイト調整法（e-type = 26）を使って宇宙線線源を再現しよう
計算条件
MENTIONED_INPUT_NAMES: source.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 09 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答1
source-track.eps
[ S o u r c e ]
set:c1[1.0]  $ Radius
set:c2[26]   $ e-type

  totfact =  pi*c1**2
 <source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  c2
    icenv =   0
 solarmod =   0.0000
    rigid =   0.0000
   proj   = proton
…
source.inp
フラックスの低い高エネルギー側の統計誤差が劇的に小さくなる
フラックスの高い1GeV付近ではやや誤差が大きくなる
Feイオンはまだほとんど発生しない
誤差が大きくなる
誤差が
小さくなる
MENTIONED_INPUT_NAMES: source.inp

--- SLIDE 10 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2：マルチソースに対するウェイト調整法
[ S o u r c e ]
set:c1[1.0]  $ Radius
set:c2[26]   $ e-type

  totfact =  pi*c1**2
 <source> = 1.0
   s-type =   9
       r1 =   c1
       r2 =   c1
      dir =  iso
   e-type =  c2
    icenv =   0
 solarmod =   0.0000
    rigid =   0.0000
   proj   = proton
…
source.inp
totfactを負値にして各イオンを均一にサンプリングするようにしよう
エネルギー分布と同様に各マルチソースの強度分布に対しても粒子数調整法とウェイト調整法がある
totfactを負値で定義するとウェイト調整法になり、各マルチソースから均一にサンプリングし、そのウェイトを各マルチソース強度に比例するように調整する
MENTIONED_INPUT_NAMES: source.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 11 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答2
source-track.eps
[ S o u r c e ]
set:c1[1.0]  $ Radius
set:c2[26]   $ e-type

  totfact =  -pi*c1**2
source.inp
Feイオンがサンプリングされ、高LET宇宙線よる線量寄与が確認できた
source-let.eps
Feイオンによるピーク
MENTIONED_INPUT_NAMES: source.inp

--- SLIDE 12 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
「分散低減法を用いた線源発生」のまとめ
線源強度は、頻度調整法もしくはウェイト調整法により表現する
マルチソース分布に対してはtotfactの正負で、エネルギー分布に対してはe-typeを変更することにより両調整法を選択することができる。
角度分布や時間分布に対してもa-typeやt-typeを変更することにより両調整法を選択することができる

--- SLIDE 13 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
実習内容
分散低減法を用いた線源発生(source)
Cell Importance法

Weight Window法

強制衝突法（force）
まとめ
概念（CI-concept)
実践（CI-practice）
概念（WW-concept）
実践（WW-practice）
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 14 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Cell Importance法とは？
[importance]にて、領域（Cell）毎にその重要度（Importance）を設定できる
Importanceの初期設定値は１。ただし外部ボイドは0。
Importanceは粒子毎に設定できる
Importanceの低い領域から高い領域に入ると、Importanceの比に従って粒子分割が行われ、全ての粒子のウェイトが下がる
重要度の高い領域から低い領域に入ると、Importanceの比に従ってロシアンルーレットが行われ、生き残った粒子のウェイトが上がる
W=1
W=1/3
W=1/3
W=1/3
I1=1
I2=3
I2/I1個に分割される*
粒子分割
*I2/I1が非整数の場合は乱数を使って分割数を決める
W=1
I1=1
I2=1/2
I2/I1の確率で生き残る
ロシアンルーレット
W=1
W=2
Killed

--- SLIDE 15 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1：１ヒストリーのときの中性子飛跡を確認
[importance]
part = neutron
reg imp
10  1.0
1   1.0
2   1.0
CP-concept.inp
CP-concept.inpを実行して飛跡を確認
領域1と2のImportance（imp）を2と4に増やして再実行し、飛跡の変化を確認
I10=1.0
I1=1.0
I2=1.0
空気
5MeV
中性子
コンクリート
（半径20cm，
深さ8cm×2）
importance-track.eps（初期設定時）
MENTIONED_INPUT_NAMES: CP-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 16 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答1
[importance]
part = neutron
reg imp
10  1.0
1   2.0
2   4.0
importance-hist.inp
I10=1.0
I1=2.0
I2=4.0
空気
5MeV
中性子
コンクリート
（半径20cm，
深さ8cm×2）
importance-track.eps
この時点で既に２つに分かれている
ここで反応が起きた
MENTIONED_INPUT_NAMES: importance-hist.inp

--- SLIDE 17 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2：不適切なImportance設定を体感する
[importance]
part = neutron
reg imp
10  1.0
1   2.0
2   4.0
CP-concept.inp
隣接する２領域間のImportanceの比が大きすぎると、粒子が分割しすぎて無駄な計算が増えてしまう場合がある
領域２のImportanceを100に設定して体感してみよう
I10=1.0
I1=2.0
I2=4.0
空気
5MeV
中性子
コンクリート
（半径20cm，
深さ8cm×2）
MENTIONED_INPUT_NAMES: CP-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 18 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答2
[importance]
part = neutron
reg imp
10  1.0
1   2.0
2   100.0
importance-hist.inp
I10=1.0
I1=2.0
I2=100.0
空気
5MeV
中性子
コンクリート
（半径20cm，
深さ8cm×2）
importance-track.eps
分割数が多すぎるWarningが出力される
たまたま粒子が入った付近のフルエンスが高くなる（統計が良くならない）
セル間のインポータンスの比は最大２～３程度が良い*
*参考文献：“A Sample Problem for Variance Reduction in MCNP” LA-10363-MS DE86 004380
MENTIONED_INPUT_NAMES: importance-hist.inp

--- SLIDE 19 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
実習内容
分散低減法を用いた線源発生(source)
Cell Importance法

Weight Window法

強制衝突法（force）
まとめ
概念（CI-concept)
実践（CI-practice）
概念（WW-concept）
実践（WW-practice）
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 20 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1：[Importance]を使った遮蔽計算
[importance] off
part = neutron
reg imp
1   2.5**0
2   2.5**1
3   2.5**2
4   2.5**3
5   2.5**4
6   2.5**5
7   2.5**6
8   2.5**7
9   2.5**8
10   2.5**9
11   2.5**10
12   2.5**11
CP-practice.inp
CP-practice.inpを実行して計算時間*や結果を確認
[importance]セクションのOffを削除して再実行し、計算時間や結果の違いを確認
半径50cm、深さ180cmのコンクリート円柱
コンクリートは12領域（各層の厚さ15cm）に分割し、それぞれ異なるImportanceを設定
半径1cmの14MeV中性子をz=0からz軸に沿って入射
計算条件
14MeV
中性子
Ii+1/Ii = 2.5 と設定
*計算時間はphits.outの最後の方（400行目付近）で確認可能
MENTIONED_INPUT_NAMES: CP-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 21 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答1
importance-dose-xz_err.eps
[importance] 未使用 total cpu time = 5.36 sec
[importance] 使用 total cpu time = 24.39 sec
importance-dose-xz.eps

--- SLIDE 22 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答1（続き）
[importance] 未使用
total cpu time = 5.36 sec
[importance] 使用
total cpu time = 24.39 sec
importance-dose-rz.eps
入射中性子のフルエンスは、1/巨視的断面積(cm)を進むごとに1/eに減衰する
遮蔽体を(1/巨視的断面積）程度の幅に区切り、そのIi+1/Ii比をeとすれば、各領域におおよそ均一に粒子を届けることが可能*
*実際は2次粒子も考慮する必要があるので（1/巨視的断面積）よりは少し広い方がよい

--- SLIDE 23 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2：不適切なImportance設定を体感する
[importance]
part = neutron
reg imp
1   2.5**0
2   2.5**0
3   2.5**0
4   2.5**0
5   2.5**0
6   2.5**5
7   2.5**6
8   2.5**7
9   2.5**8
10   2.5**9
11   2.5**10
12   2.5**11
CP-practice.inp
左の例のように、領域5までのImportanceを1.0に設定し、領域6で一気に2.55 ≒ 100まで上げる
計算結果（特に統計誤差）を確認する
MENTIONED_INPUT_NAMES: CP-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 24 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答2
importance-dose-xz_err.eps
適切な[importance]を使用 total cpu time = 24.39 sec
importance-dose-xz.eps
不適切な[importance]を使用 total cpu time = 16.49 sec
Ii+1/Ii比の大きい境界にGapができる

--- SLIDE 25 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
[Importance]のまとめ
遮蔽計算（特に深層透過計算）は、Cell Importance法により計算時間を短縮することが可能
[Importance]は領域毎に設定する必要があり、遮蔽体を分割し隣り合う領域のImportance比を2～3以下にする必要がある
[Importance]を適切に設定するためには、巨視的断面積などある程度放射線物理に関する知識が必要
適切でない設定の場合、計算の遅延やメモリ不足によるエラーを引き起こす可能性がある

--- SLIDE 26 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
実習内容
分散低減法を用いた線源発生(source)
Cell Importance法

Weight Window法

強制衝突法（force）
まとめ
概念（CI-concept)
実践（CI-practice）
概念（WW-concept）
実践（WW-practice）
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 27 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Weight Window法とは？
領域（Cell）もしくはxyzメッシュ毎に、ウェイトが取れる幅（Weight Window）を設定できる
Weight Windowの初期設定はない（どんなウェイトでもOK）
Weight Windowは粒子及びエネルギー群ごとに設定できる
Weight Windowから外れたウェイトを持つ粒子が流入もしくは発生すると、粒子分割もしくはロシアンルーレットによりウェイト値が調整される*
ウェイト
WU=2.5
WU=1.25
WU=0.75
領域1
領域2
領域3
WL=0.5
WL=0.25
WL=0.15
W=1
W=0.5
W=0.5
WU=3.0
W=1.8
WL=0.6
killed
領域4
*ロシアンルーレットでは粒子ウェイトがWu*0.6になるように生存確率が調整される

--- SLIDE 28 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Weight WindowとCell Importanceの違い
Cell Importance法は２領域間のImportance比のみが重要となるが、Weight Window法は、絶対値が重要となる

Weight Windowは、粒子種のみならずエネルギー群ごとに設定できる

xyzメッシュに対して設定できる

自動で適切な値を設定する機能（[t-wwg]タリー）がある
→粒子のウェイトが揃うので、統計誤差の収束に有利
→より透過力の高い高エネルギー粒子を重点的に輸送することができる
→分散低減法を実施するために領域を変更する必要がない
→放射線物理の知識がなくても設定できる。ただし、ある程度、経験は必要

--- SLIDE 29 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
Weight Window法に関連するパラメータ
wupn: ウェイトウィンドウの上限値と下限値の比（D=5.0）
mxspln: 1回の粒子分割で分割する粒子の最大数（D=5.0）
mwhere: ウェイトウィンドウが考慮されるタイミング（D=0）
        -1：核反応時，0:両方，1:領域横断時
必要に応じて[parameters]セクションで設定する。
詳細はマニュアル「5.2.4 時間カット，ウェイトカット，ウェイトウィンドウ」を参照。

--- SLIDE 30 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1：１ヒストリーのときの中性子飛跡を確認
[weight window]
part = neutron
reg ww1
1   0.25
2   0.25
WW-concept.inp
WW-concept.inpを実行して飛跡を確認
領域2のWeight Windowの下限値を0.125に下げて再実行し、飛跡の変化を確認
5MeV
中性子
weight-track.eps（初期設定時）
空気
水
（半径10cm，
深さ5cm×2）
MENTIONED_INPUT_NAMES: WW-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 31 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答1
weight-track.eps
この時点で既に２つに分かれている
ここで反応が起きた
[weight window]
part = neutron
reg ww1
1   0.25
2   0.125
WW-concept.inp
ウェイト
WU=1.25
WU=0.625
領域10
領域1
領域2
WL=0.25
WL=0.125
W=1
W=0.5
W=0.5
（制限なし）
MENTIONED_INPUT_NAMES: WW-concept.inp

--- SLIDE 32 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2：不適切なweight window設定を体感する
隣接する２領域間のweight window下限値の比が大きすぎると、粒子が分割しすぎて無駄な計算が増えてしまう場合がある
領域２のweight window下限値を0.005に設定して体感してみよう
[weight window]
part = neutron
reg ww1
1   0.25
2   0.125
WW-concept.inp
weight-track.eps
これがどう変化するか？
MENTIONED_INPUT_NAMES: WW-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 33 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答2
weight-track.eps
１度に５個までしか分割できないので（mxspln=5）、反応するたびに徐々に粒子数が増えていく
セル間のWeight Window下限値の比も最大２～３程度が良い
[weight window]
part = neutron
reg ww1
1   0.25
2   0.005
WW-concept.inp
ウェイト
WU=1.25
WU=0.025
領域10
領域1
領域2
WL=0.25
WL=0.005
W=1
W=0.04
W=0.2
（制限なし）
W=0.008
MENTIONED_INPUT_NAMES: WW-concept.inp

--- SLIDE 34 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題3：エネルギー群毎に異なるWeight Windowを設定
１つ目の[weight window]を無効にし、２つ目の[weight window]を有効にしてＰＨＩＴＳを実行
[weight window]
part = neutron
reg  ww1
1   0.25
2   0.005

[weight window] off
part = neutron
eng = 2
     0.01     1.0e5
reg  ww1      ww2
1    0.25*10  0.25
2    0.125*10 0.125
WW-concept.inp
低エネルギー群のWeight Window下限値を10倍に増やす設定
各エネルギー群の最大値
（最初のエネルギー群の下限値は常に0）
エネルギー群数（２以上のときのみ定義が必要）
MENTIONED_INPUT_NAMES: WW-concept.inp
ANSWER_FILE: WW-practice/input/WW-practice-4.inp

--- SLIDE 35 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答3
weight-track.eps
ここで発生した2次粒子は低エネルギーだったためロシアンルーレットでKillされた
WW-concept.inp
[weight window] off
part = neutron
reg  ww1
1   0.25
2   0.005

[weight window]
part = neutron
eng = 2
     0.01     1.0e5
reg  ww1      ww2
1    0.25*10  0.25
2    0.125*10 0.125
1群のときの結果
低エネルギー群のWeight Window下限値を高くするとロシアンルーレットを実施する回数が増え、深層透過に影響を与えない粒子輸送の時間を短縮することができる
MENTIONED_INPUT_NAMES: WW-concept.inp

--- SLIDE 36 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
実習内容
分散低減法を用いた線源発生(source)
Cell Importance法

Weight Window法

強制衝突法（force）
まとめ
概念（CI-concept)
実践（CI-practice）
概念（WW-concept）
実践（WW-practice）
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 37 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
[Weight Window]の自動決定機能
ある領域内におけるタリー結果の統計誤差をできるだけ均一にしたい場合、その領域内のモンテカルロ粒子密度*をできるだけ均一にするのがよい
モンテカルロ粒子密度を均一にするには、フルエンスに比例してweight window下限値を設定するのがよい
→フルエンスの低い領域は粒子分割が頻繁に行われるようになり、モンテカルロ粒子密度が上がるため
[t-track]と同じように粒子フルエンスを計算し、その結果に比例するように[weight window]セクションを作成するタリー[t-wwg] (Tally for Weight Window Generator)を開発
*モンテカルロシミュレーションで実際にある領域を通過した粒子の数。ウェイトを考慮する前の粒子フルエンスとほぼ同義語。
方針

--- SLIDE 38 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
[t-wwg]の利用手順と注意点
手順
統計誤差の均一なタリー結果を得たい領域に[t-wwg]を設定してPHITS計算を実行する
[t-wwg]タリー結果（[weight window]セクション）をinflコマンドでPHITS入力ファイルに取り込んで、PHITS計算を2～3回実行する。

ヒストリー数を大きくして本計算を実行する。
→出力される[weight window]が徐々に最適化される
注意点
[t-wwg]のxyz空間メッシュ面が体系の面と完全に一致するとエラーが起きる。（ただし面座標が整数の場合は自動で回避される）
[t-wwg]の空間メッシュ・エネルギーメッシュを細かく設定しすぎると出力される[weight window]の統計誤差が大きくなり、無駄に粒子分割及びロシアンルーレットを繰り返して計算時間が長くなる*
[t-wwg]を設定していない領域から設定している領域に粒子が入ると大量に粒子分割が起きる可能性があるので、[t-wwg]の領域設定範囲には注意が必要*
*空間メッシュ幅に関してはコンクリートの場合は約15cm程度（1/巨視的断面積）、
エネルギーメッシュに関しては１群にして低エネルギー・アンバイアス法を利用することを奨励

--- SLIDE 39 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題1：[t-wwg]を使った遮蔽計算
[ T - WWG ]
  mesh = xyz
x-type = 2
  xmin = -c1
  xmax =  c1
    nx = 5
y-type = 2
  ymin = -c1
  ymax =  c1
    ny = 1
z-type = 2
  zmin =  0
  zmax =  c2
    nz =  12
   part = all
   e-type = 1
       ne = 1
     0   1e5
axis = xz
file =  wwg-xz.out
axis =  wwg
file =  wwg.out
WW-practice.inp
半径100cm、深さ180cmのコンクリート円柱*
上下の奥側に線量を計算するターゲット領域を別途定義
計算条件
14MeV
中性子
タリー出力ファイル
*[weight window]や[t-wwg]を使う場合は、[importance]を使う場合と異なり領域を分割する必要はない
wwg.out: [t-wwg]より出力される[weight window]セクション
wwg-xz.eps: [t-wwg]の結果を視覚的に確認する
track-xz.eps: 実効線量の空間分布
track-rz.eps: 実効線量の深さ分布
track-reg.out: ターゲット領域内での実効線量
WW-practice.inpを実行してwwg.outなどを出力する
11行目のinfl:{wwg.out}を有効にして２回PHITSを実行
計算時間や統計誤差を確認
MENTIONED_INPUT_NAMES: WW-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 40 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答1
track-xz.eps
自動である程度最適な[weight window]が作成され、全領域に粒子を届けることができた
track-xz_err.eps
track-rz.eps
#  num    reg     volume       all       r.err
    1       2   1.1310E+05   1.1202E-06  0.4438
    2       3   1.1310E+05   1.5993E-06  0.3036
track-reg.out（45行目付近）
sec
total cpu time = 32.01
phits.out（550行目付近）

--- SLIDE 41 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
set:  c71[0.0000E+00+2.10873E-08]  c72[4.46309E-04]

   part = all
    eng =  1
         1.00000E+05

   xyz                 ww1
  (1 1  1)  (1.21073E-06+c71)/c72
  (1 1  2)  (2.07578E-06+c71)/c72
  (1 1  3)  (2.27569E-06+c71)/c72
...
解答1（つづき）
fluenceの下限10%値
wwg.out（30行目付近）
fluenceの最大値
× wwmax*
各領域のfluence
weight window下限値 =
各領域のfluence + fluenceの下限10%値
fluenceの最大値×規格化定数
*入力ファイルで定義。デフォルトは0.99
fluenceの下限10%値を足しているのは、fluenceが0の領域におけるweight window下限値が0にならないための対策

--- SLIDE 42 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
計算効率を更に高める工夫①
低エネルギー・アンバイアス機能
あるしきい値エネルギー以下のweight window下限値を定数倍することにより、人為的に低エネルギー側のモンテカルロ粒子密度を下げて計算時間を短縮する機能
elowthre: (D=0.0) しきい値エネルギー。0の場合、この機能は使わない
elowbias: (D=5.0) 低エネルギー群のweight window下限値の倍率
低エネルギー輸送計算に時間を要する中性子遮へい計算で特に有効

--- SLIDE 43 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2：低エネルギー・アンバイアス法を活用
[ T - WWG ]
axis = xz
file =  wwg-xz.out
axis =  wwg
file =  wwg.out
epsout = 1
$ elowthre = 0.01
WW-practice.inp
[t-wwg]のelowthreを有効にしてPHITSを２回実行

計算時間や統計誤差を確認
（１回目でwwg.outを作り直し、２回目で低エネルギー・アンバイアス法を活用したシミュレーションを実行）
elowthre: (D=0.0) しきい値エネルギー
elowbias: (D=5.0) 低エネルギー群のweight window下限値の倍率。今回は定義しないので5.0がそのまま採用される
0.01MeV以下の低エネルギー粒子が発生した場合、約4/5の確率でKillされる
MENTIONED_INPUT_NAMES: WW-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 44 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答2
track-xz.eps
約半分の計算時間でほぼ同等の統計誤差を持つ結果を得ることができた
track-xz_err.eps
track-rz.eps
#  num    reg     volume       all       r.err
    1       2   1.1310E+05   1.1040E-06  0.3021
    2       3   1.1310E+05   7.3123E-07  0.4058
track-reg.out（45行目付近）
sec
total cpu time = 16.12
phits.out（550行目付近）

--- SLIDE 45 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
計算効率を更に高める工夫②
*特定の経路や反応を起こした粒子にタグを付ける機能。phits/lecture/advanced/options参照
粒子誘導機能
ヒストリーカウンタ機能*と組み合わせ、特定の領域にモンテカルロ粒子を誘導する機能。
chwei(i): (D=0.0) 粒子誘導機能を利用する際の誘導強度。i はカウンタ番号。
chplane: (D=all) ダクトストリーミング計算に粒子誘導機能を使う場合、ダクトと垂直な面（xy, yz, xzなど）を指定
詳細はT. Sato et al. Nucl. Instr. Meth. B 557, 165535 (2024)を参照
全体的ではなく、特定の場所における統計を良くしたい場合に特に有効

--- SLIDE 46 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題3：粒子誘導機能を活用
[ T - WWG ]
axis = xz
file =  wwg-xz.out
axis =  wwg
file =  wwg.out
epsout = 1
elowthre = 0.01
$ chwei(1) = 10.0
…
[counter]
counter = 1
part=neutron
reg  in
2     1
WW-practice.inp
[t-wwg]のchwei(1)を有効にしてPHITSを２回実行

計算時間や統計誤差を確認
（１回目でwwg.outを作り直し、２回目で粒子誘導機能を活用したシミュレーションを実行）
chwei(i): (D=0.0) 粒子誘導機能を利用する際の誘導強度。i はカウンタ番号。利用する場合は10～100くらいが適切
領域２に中性子が入ったヒストリの飛跡上にできるだけ粒子を多く誘導する[weight window]を作成するようになる
領域２に中性子が入った場合にカウンタ１が+1される
MENTIONED_INPUT_NAMES: WW-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-4.inp

--- SLIDE 47 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答3
track-xz.eps
計算時間は多少長くなるが、より多くの粒子が上側に誘導され、領域２（上側のターゲット）の線量に対する統計誤差が顕著に下がる。
track-xz_err.eps
track-rz.eps
#  num    reg     volume       all       r.err
    1       2   1.1310E+05   1.0526E-06  0.2211
    2       3   1.1310E+05   1.7793E-06  0.3509
track-reg.out（45行目付近）
sec
total cpu time = 32.77
phits.out（550行目付近）

--- SLIDE 48 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題4：統計指標出力機能を活用
[ P a r a m e t e r s ]
 icntl    =           0
 maxcas   =        1000
 maxbch   =          4
 file(6)  = phits.out
 $ itall = 3
...
[ T-track ]
   mesh = reg
    reg = 2 3
...
iextstat = 1
anatally start
anatally end
WW-practice.inp
maxbchを20に増やす
itall =3を有効にしてPHITSを実行する
（iextstat = 1かつanatally start & anatally endがあるタリーに対して統計指標出力機能が有効になる）
分散低減法を使った場合、1ヒストリーでタリー結果を大きく変えるようなイベントが発生し、統計誤差が小さくても必ずしも統計が十分とは言えない可能性がある（特に設定が適切でない場合）
統計指標出力機能（itall = 3）を使ってタリー結果や統計誤差のバッチ変化をチェック
*マニュアル「6.10 拡張された統計指標出力機能」参照
本課題の流れ
track-reg_StD.epsファイルを確認
itall = 3のときのみ有効
MENTIONED_INPUT_NAMES: WW-practice.inp
ANSWER_FILE: WW-practice/input/WW-practice-end.inp

--- SLIDE 49 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答4（track-reg_StD.eps）
統計指標チェック（1ページ目）
平均値のバッチ毎変化（２ページ目）
相対誤差のバッチ毎変化（３ページ目）
これらの結果から分かること
２～３バッチ終了後は極端にタリー結果に変化を与えるバッチはなく、このままバッチ数を増やせば正しい結果が得られると予想される

--- SLIDE 50 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
[weight window]&[t-wwg]のまとめ
[weight window]と[t-wwg]を組み合わせることにより、効率よく分散低減法を利用した遮蔽計算が可能となる
[t-wwg]の空間・エネルギーメッシュは、あまり細かく設定しない。
低エネルギー・アンバイアス機能や粒子誘導機能を用いると、計算効率を更に向上することができる
分散低減法を使うとレアイベントが発生し、タリー結果が急激に大きくなる場合がある。そのようなイベントがないか統計指標出力機能（itall=3）を用いて確認することが望ましい

--- SLIDE 51 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
実習内容
分散低減法を用いた線源発生(source)
Cell Importance法

Weight Window法

強制衝突法（force）
まとめ
概念（CI-concept)
実践（CI-practice）
概念（WW-concept）
実践（WW-practice）
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 52 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
強制衝突法とは？
あるターゲット内で強制的に核反応を引き起こす分散低減法の一種
二つに分割
強制衝突領域
非衝突のウェイト：Wi×exp(-Sd)
衝突粒子
入射粒子 Wi
S: 巨視的断面積
d:セルを横切る距離
非衝突粒子
衝突のウェイト：Wi×{1-exp(-Sd)}
無駄打ちを減らして少ないヒストリーで統計誤差を小さくする
薄膜ターゲットや低エネルギー荷電粒子による核反応の影響を調査したい場合に有効
ｆｃｌ：強制衝突コントロールパラメータ
fcl = -1：強制衝突による生成粒子は通常の衝突をさせる（ウェイトカットオフは考慮しない）
fcl =  1：強制衝突による生成粒子は，ウェイトカットオフになるまで強制衝突させる
（通常 fcl = -1 を使用）
d
衝突位置は断面積に従って確率的に決定

--- SLIDE 53 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１:薄膜を用いた断面積測定実験を模擬しよう
[t-product]: ターゲット内で生成する荷電粒子の生成エネルギー分布 → 真の断面積
[t-cross]：検出器に入射した荷電粒子のエネルギー分布 → 測定上の断面積
force.inp
[ P a r a m e t e r s ]
 icntl    =           0
maxcas   =      5000
 maxbch   =           5
…
[Forced Collisions] off
part = proton
reg  fcl
1   -1.0
半径0.5cm, 10μm厚さSi
100MeV陽子
検出器
真空
force.inpを実行し、ほとんど反応が起きていないことを確認する
[forced collisions]セクションを有効にして、反応が起きることを確認する
track-xz.eps（forced collisionsを利用しない場合）
タリー設定
MENTIONED_INPUT_NAMES: force.inp
ANSWER_FILE: WW-practice/input/WW-practice-2.inp

--- SLIDE 54 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答1
product.eps
核反応が起きて２次粒子が発生し[t-product]でスコアされるが、そのウェイトが低すぎるためほとんどの粒子がウェイトカットオフされ輸送されない
 → [t-cross]や[t-track]ではほとんど検出されない
cross.eps

--- SLIDE 55 ---
PPTX_FILE: phits-variance-reduction-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題2:強制衝突で生成された2次粒子を輸送しよう
force.inp
[ P a r a m e t e r s ]
 icntl    =           0
maxcas   =      5000
 maxbch   =           5
$ wc2(1)   = 1.0E-12 # weight cutoff of proton
$ wc2(18)  = 1.0E-12 # weight cutoff of Alpha
$ wc2(19)  = 1.0E-12 # weight cutoff of Nucleus
陽子・α粒子・原子核（粒子ID 1, 18, 19）のウェイトカットオフパラメータwc2*を極めて低く設定し、強制衝突で生成した2次粒子が輸送されるようにする
PHITSを実行してproduct.epsとcross.epsを比較する
*ウェイトがwc2以下の粒子が生成された場合、ロシアンルーレットを行って生存/消滅を決定する
両者が一致するか確認する。一致しない場合は、その理由を考える
MENTIONED_INPUT_NAMES: force.inp
ANSWER_FILE: WW-practice/input/WW-practice-3.inp

--- SLIDE 56 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
解答2
product.eps
陽子やα粒子は、検出器まで届くようになった（cross.epsで検出）
しかし、Siはほとんど検出器まで届かない（ターゲット内で止まってしまうため）
本シミュレーションより、ターゲット厚10μmの薄膜実験でも反跳原子核のエネルギ分布を測定することは困難であることが分かる
cross.eps

--- SLIDE 57 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
[forced collisions]のまとめ
核反応発生率が低いターゲットから発生した2次粒子の影響を調べる場合、強制衝突法を使うと無駄打ちが減り計算時間が短縮できる
強制衝突法を使って極めて発生確率の低い核反応を再現する場合は、2次粒子のウェイトカットオフ（wc2）を下げる必要がある

--- SLIDE 58 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
実習内容
分散低減法を用いた線源発生(source)
Cell Importance法

Weight Window法

強制衝突法（force）
まとめ
概念（CI-concept)
実践（CI-practice）
概念（WW-concept）
実践（WW-practice）
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 59 ---
PPTX_FILE: phits-variance-reduction-en.pptx
SLIDE_TEXT:
全体のまとめ
分散低減法を適切に利用することにより、宇宙線解析、遮蔽設計、薄膜計算などアナログモンテカルロシミュレーション*では時間の掛かる計算を効率よく行うことが可能となる
ただし、設定を誤ると、計算時間の遅延やメモリ不足によるエラーを引き起こす場合がある
また、飛跡構造解析、重イオン核反応計算、高い計算精度を要求する医学物理計算など、本質的に計算時間の掛かるシミュレーションに対しては効果は限定的となる
*ウェイトをコントロールしない（常に１となる）シミュレーション
原理をよく理解した上で適材適所での利用が重要

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: CI-concept/input/CI-concept-1.inp
FILE: CI-concept/input/CI-concept-2.inp
FILE: CI-concept/input/CI-concept-end.inp
FILE: CI-practice/input/CI-practice-1.inp
FILE: CI-practice/input/CI-practice-2.inp
FILE: CI-practice/input/CI-practice-end.inp
FILE: force/input/force-2.inp
FILE: force/input/force-3.inp
FILE: source/input/source-1.inp
FILE: source/input/source-2.inp
FILE: source/input/source-end.inp
FILE: WW-concept/input/WW-concept-1.inp
FILE: WW-concept/input/WW-concept-2.inp
FILE: WW-concept/input/WW-concept-3.inp
FILE: WW-concept/input/WW-concept-end.inp
FILE: WW-practice/input/WW-practice-1.inp

[BONUS_TEXT_FILES]
NOTE: None
