# Lecture: advanced/detector

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/detector
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: detector
LECTURE_PATH_INDEX: lecture/advanced/detector
PPTX_FILES: phits-detector-en.pptx, phits-detector-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: dE-E_detector, neutron, photon
SECTION_KEYWORDS: mev, t-deposit, t-deposit2, t-track

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/detector
LECTURE_PATH_INDEX: lecture/advanced/detector
PPTX_FILES: phits-detector-en.pptx, phits-detector-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 3
SLIDE_COUNT: 56
EXERCISE_SLIDE_COUNT: 14
BONUS_INPUT_COUNT: 5
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- dE_E_detector/dE-E_detector.inp
- neutron.inp
- photon.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Detector Response Simulation
- SLIDE 02: Goal of this lecture
- SLIDE 03: Table of contents
- SLIDE 04: photon.inp
- SLIDE 05: Parameter Setup
- SLIDE 06: How to interpret [t-deposit] result
- SLIDE 07: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/photon-2.inp
- SLIDE 08: Answer 1
- SLIDE 09: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/photon-3.inp
- SLIDE 10: Answer 2
- SLIDE 11: How to determine dresol & dfano?
- SLIDE 12: Correlated Sources
- SLIDE 13: EXERCISE 3 | Exercise 3
  ANSWER_FILE: input/photon-4.inp
- SLIDE 14: Answer 3
- SLIDE 15: Coincidence Event
- SLIDE 16: EXERCISE 4 | Exercise 4
  ANSWER_FILE: input/photon-5.inp
- SLIDE 17: Answer 4
- SLIDE 18: EXERCISE 5 | Exercise 5
  ANSWER_FILE: input/photon-5.inp
- SLIDE 19: Answer 5
- SLIDE 20: Table of contents
- SLIDE 21: neutron.inp
- SLIDE 22: Important Notice
- SLIDE 23: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/photon-2.inp
- SLIDE 24: Answer 1
- SLIDE 25: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/photon-3.inp
- SLIDE 26: Answer 2
- SLIDE 27: Table of contents
- SLIDE 28: Summary
- SLIDE 01: 検出器応答関数計算演習
- SLIDE 02: 本実習の目的
- SLIDE 03: 目次
- SLIDE 04: photon.inp
- SLIDE 05: 重要パラメータ
- SLIDE 06: [t-deposit]計算結果の解釈
- SLIDE 07: EXERCISE 1 | 課題１
  ANSWER_FILE: input/photon-2.inp
- SLIDE 08: 回答１
- SLIDE 09: EXERCISE 2 | 課題２
  ANSWER_FILE: input/photon-3.inp
- SLIDE 10: 回答２
- SLIDE 11: dresolとdfanoの決定方法
- SLIDE 12: 相関線源オプション
- SLIDE 13: EXERCISE 3 | 課題３
  ANSWER_FILE: input/photon-4.inp
- SLIDE 14: 回答３
- SLIDE 15: 同期（Coincidence）イベント
- SLIDE 16: EXERCISE 4 | 課題４
  ANSWER_FILE: input/photon-5.inp
- SLIDE 17: 回答４
- SLIDE 18: EXERCISE 5 | 課題５
  ANSWER_FILE: input/photon-5.inp
- SLIDE 19: 回答５
- SLIDE 20: 目次
- SLIDE 21: neutron.inp
- SLIDE 22: 重要ポイント
- SLIDE 23: EXERCISE 1 | 課題１
  ANSWER_FILE: input/photon-2.inp
- SLIDE 24: 回答１
- SLIDE 25: EXERCISE 2 | 課題２
  ANSWER_FILE: input/photon-3.inp
- SLIDE 26: 回答２
- SLIDE 27: 目次
- SLIDE 28: まとめ

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: dE_E_detector/dE-E_detector.inp
FILE: neutron.inp
FILE: photon.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Detector Response Simulation
Dec. 2024 revised
phits/lecture/advanced/Detector
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Goal of this lecture
Calculate the response and efficiency of detectors irradiated by photons and neutrons
Pulse-height distribution of organic scintillator signals induced by neutrons
2D pulse-height distribution of a detector pair exposed to 60Co γ-rays

--- SLIDE 03 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Table of contents
Photon detection
Neutron detection
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 04 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
photon.inp
Basic setup
Projectile:
Geometry:
Tally:
track_xz.eps
deposit.eps
γ-rays from 60Co (1.173 and 1.332 MeV)
2 NaI scintillators (2 inch x 2 inch Φ）
[t-track] fluence  distribution
[t-deposit] deposition energy distribution in region 1
(Pulse height distribution)
MENTIONED_INPUT_NAMES: photon.inp

--- SLIDE 05 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Parameter Setup
[ parameters ]
 icntl =  0
maxcas = 10000
maxbch = 5
file(6)  = phits.out
negs = 1
e-mode = 2
…
Do not use Kerma approximation (output = dose) because it only concerns the mean value of deposition energy
Transport electrons → negs = 1
Explicitly transport charged particles from neutron reactions → e-mode = 2
Use [t-deposit] with output = deposit to get detector response
Score the variance of deposition energies in each history
[ t-deposit ]
...
unit =    3
output = deposit
axis = eng
e-type = 2
ne = 300
emin = 0.0
emax = 3.0

--- SLIDE 06 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
How to interpret [t-deposit] result
Pulse height in MCA (Multi-Channel Analyzer)
Full absorption peaks of 1.173 & 1.332 MeV photons
Count / sec
Compton edges of
1.173 & 1.332 MeV photons

--- SLIDE 07 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
Way to consider detector resolutions
Pulse height is not exactly the same as the deposition energy because of electronic noises, fluctuation of W or ε values, quenching effect etc.
Peaks and edges in the measured pulse height distributions are not as sharp as expected from simulations
PHITS can consider the detector resolution by fluctuating the deposition energy in each history (Edep) using a Gaussian distribution with standard deviation σ
Add dresol = 0.01 & dfano = 0.001 in [t-deposit]
*If dresol < 0, user-defined function written in usrresol.f is applied
ANSWER_FILE: input/photon-2.inp

--- SLIDE 08 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Answer 1
[ t-deposit ]
...
 part =  all
 epsout =    1
 dresol = 0.01
 dfano = 0.001
deposit.eps

--- SLIDE 09 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
Let’s increase/decrease the detector resolution by changing dfano parameter
What if the resolution is lower (dfano = 0.01)?
What if the resolution is higher (dfano = 0.0001)?
ANSWER_FILE: input/photon-3.inp

--- SLIDE 10 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Answer 2
dfano = 0.01
dfano = 0.0001
Low resolution
High resolution
deposit.eps
deposit.eps

--- SLIDE 11 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
How to determine dresol & dfano?
Ideal detector
dresol = 0.01
dfano = 0.001
broader
Generally dresol is very small → dfano dominantly determines the resolution
If measured σ at 1.332 MeV is 0.05 MeV, dfano = (0.05)2/1.332 = 0.00187

--- SLIDE 12 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Correlated Sources
60Co
β- 99.88%
β- 0.12%
0.30 ps
0.713 ps
1173.228 keV
99.85%
1332.492 keV
99.98%
60Ni
*Decay scheme of 60Co
Two γ-rays are emitted almost at once from a single decay of 60Co
Detectors occasionally catch energies of both γ-rays emitted from an identical decay, resulting in a “sum-up” peak
Two detectors occasionally absorb the energies of each γ-ray emitted from an identical decay observed as a “coincidence” event
It is necessary to generate two radiations at once as the sources of a history
*At extremely low probability (2x10-8), direct transition from the 2nd level to the ground state occurs by emitting 2.50569 MeV γ-rays

--- SLIDE 13 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
Let’s reproduce 60Co using the correlated source function
Change RI source to mono-energetic source with E = 1.173 MeV
     (delete parameters related to “e-type” and add “e0” parameter)
Copy and paste the multi-source and change the energy to 1.332 MeV
Change iscorr from 0 to 1
     (iscorr = 0: independent multi-source, = 1: correlated multi-source)
Change totfact to reproduce 1,000 Bq = 2,000 photon/sec*
Change dfano = 0.001 (if you have changed)
[ S o u r c e ]
totfact =
iscorr =
<source> = 1.0
・ ・ ・ ・ ・ ・
 e-type = 28
       ni = 1
 Co-60  1.0e3
 e0 =
Find sum-up peak around 2.5 MeV
*In the case of correlated source, two radiations are generated in one history, but tally results are still normalized per source generation
ANSWER_FILE: input/photon-4.inp

--- SLIDE 14 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Answer 3
[ S o u r c e ]
totfact = 2.0e3
iscorr = 1
<source> = 1.0
s-type = 1
proj = photon
...
$ e-type = 28
 $      ni = 1
 $ Co-60  1.0e3
 e0 = 1.173
<source> = 1.0
s-type = 1
proj = photon
...
$ e-type = 28
 $      ni = 1
 $ Co-60  1.0e3
 e0 = 1.332
deposit.eps
Sum-up peak
at 2.505 MeV
(1.173 + 1.332)

--- SLIDE 15 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Coincidence Event
Response of dE-E detector telescope behind a water target irradiated by 100 MeV/n carbon ions calculated by [t-deposit2]*
Pulse-heights in detector pairs are measured in coincidence to identify particle species
Such 2-dimensional plots can be directly reproduced by PHITS using [t-deposit2] tally
dE-E detector telescope
dE
E
dE detector: Measure stopping power
E detector: Measure total energy
*Input and output files are provided in “dE-E_detector” folder
p
d
n
α
Example

--- SLIDE 16 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
Let’s make 2-dimensional plot of the responses of detector #1 & #2
Activate [t-deposit2] & open deposit2.eps
[ T - Deposit2 ] off
 mesh =  reg
      reg =  1 2
  e1-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol1 = 0.01
   dfano1 = 0.001
  e2-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol2 = 0.01
   dfano2 = 0.001
     unit =    1
     axis =    e12
 ...
Cell IDs of the detectors
e-type for detector 1
dresol & dfano for detector 1
e-type for detector 2
dresol & dfano for detector 2
e12 indicates the 2-dimensional plot with x & y axis = deposition energies in regions 1 & 2, respectively
ANSWER_FILE: input/photon-5.inp

--- SLIDE 17 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Answer 4
deposit2.eps
anti-coincidence events
both γ-rays were fully absorbed
anti-coincidence events

--- SLIDE 18 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Let’s calculate the response function of detector #1 for coincidence and anti-coincidence events
Change e2-type subsection to distinguish the deposition energy below and above 0.1 MeV
Change axis to show the response function of detector 1 (i.e., eng1)
Add samepage parameter to show eng2 axis data in the same graph
[ T - Deposit2 ]
mesh =  reg
      reg =  1 2
  e1-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol1 = 0.01
   dfano1 = 0.001
  e2-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol2 = 0.01
   dfano2 = 0.001
     unit =    1
     axis =    e12
 ...
change to e2-type = 1 and distinguish
below and above 0.1 MeV
ANSWER_FILE: input/photon-5.inp

--- SLIDE 19 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Answer 5
deposit2.eps
Sum-up peak is observed only in anti-coincidence events
[ T - Deposit2 ]
mesh =  reg
      reg =  1 2
  e1-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol1 = 0.01
   dfano1 = 0.001
  e2-type =    1
       ne =  2
0  0.1  3.0
$    emin  =  0.0
$   emax  =  3.0
  dresol2 = 0.01
   dfano2 = 0.001
     unit =    1
     axis =   eng1
samepage = eng2
 ...
Peak due to gamma back-scattered in detector #2 (only in coincidence events)

--- SLIDE 20 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Table of contents
Photon detection
Neutron detection
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 21 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
neutron.inp
Basic setup
Projectile:
Geometry:
Tally:
Pencil neutron beam with energy of 20 MeV
Organic scintillator (2 inch x 2 inch Φ）
[t-track] fluence  distribution
[t-deposit] deposition energy distribution in region 1
track_xz.eps
deposit_n.eps
MENTIONED_INPUT_NAMES: neutron.inp

--- SLIDE 22 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Important Notice
How to use SCINFUL mode?
For calculating the response of organic scintillator to neutrons, “SCINFUL” mode* is encouraged to use its precise cross section database for n-C reactions up to 150 MeV
Set iscinful = 1 in [parameters] to activate SCINFUL mode
Set [data max] section to use nuclear reaction model for n-C reaction down to 0.1 MeV (minimum energy of SCINFUL database) because SCINFUL database is regarded as a nuclear reaction model in PHITS
*D. Satoh et al., J. Nucl. Sci. Technol. 59, 1047-1060 (2022)
Advanced application (not done in this lecture)
[ Parameters ]
icntl = 0
...
iscinful = 1
[Data Max]
part = neutron
 mat  nucleus   dmax
   1        C        0.10
material ID of organic scintillator
To convert deposition energy from MeV to MeVee (light output ), recompile PHITS with user-defined tally in phits/utility/usrtally/scinful-qmd

--- SLIDE 23 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
Let’s find the mechanisms responsible for the peaks in the deposition-energy distribution
Distinguish particle-wise contributions to energy deposition by changing part parameter to “part = all proton deuteron alpha C”
Peaks
deposit_n.eps
ANSWER_FILE: input/photon-2.inp

--- SLIDE 24 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Answer 1
deposit_n.eps
In the case of [t-deposit] with output = deposit & deposit = 0 (default)*, “part” indicates the distribution of total deposit energy with the contribution of each particle
Proton 100% (20 MeV)
[ T - Deposit ]
...
file = deposit_n.out
part = all proton deuteron alpha C
...
Proton 50% (~7 MeV)
Alpha 50% (~7 MeV)
Deuteron 80% (~5 MeV)
Proton 20% (~1.2 MeV)
*If deposit = 1, deposition energy distribution from each particle is calculated

--- SLIDE 25 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
Let’s calculate the efficiency of the detector given the threshold is 1 MeV
Efficiency =
Number of radiations incident to the detector
Number of radiations depositing energy more than the threshold
=
Integral number of the deposition energy distribution above the threshold per source (when all sources are directed to the detector)
[ T - Deposit ]
...
  e-type = 2
  ne = 210
  emin = 0.0
  emax = 21.0
...
Change e-type in [t-deposit] to make a single energy bin from 1 MeV to 108 MeV
Check numerical value in deposit_n.out
ANSWER_FILE: input/photon-3.inp

--- SLIDE 26 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Answer 2
[ T - Deposit ]
...
  e-type = 2
  ne = 1
  emin = 1.0
  emax = 1.0e8
...
Approximately 20% of incident neutrons are detected by this organic scintillator if the threshold is 1 MeV
… (lines around 32)
x: Deposit Energy [MeV]
y: Number [1/source]
p: xlin ylog afac(0.8) form(0.9)
h: n            x            y(all     ),hh0l n
#  e-lower      e-upper        all       r.err
   1.0000E+00   1.0000E+08   2.1782E-01  0.0068
...
neutron.inp
deposit_n.out
Neutron fluence at the detector position is approximately 5 times higher than the detected neutrons
MENTIONED_INPUT_NAMES: neutron.inp

--- SLIDE 27 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Table of contents
Photon irradiation
Neutron irradiation
Summary
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 28 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
Summary
[t-deposit] with output = deposit is used for detector response simulation
Use of the EGS mode (negs = 1) and the event generator mode (e-mode = 2) is indispensable for this application
Use of the SCINFUL mode (iscinful = 1 & [data max]) is encouraged for the response calculation of organic scintillators irradiated by neutrons
Detector resolution is defined by dresol and dfano parameters
The correlated-source function (iscorr = 1) and [t-deposit2] are useful when the coincidence events are important in the response calculation

--- SLIDE 01 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
検出器応答関数計算演習
2024年12月改訂
phits/lecture/advanced/Detector
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
本実習の目的
光子及び中性子照射に対する検出器の応答関数及び検出効率を計算できるようになる
中性子を照射した有機シンチレータの応答関数
60Coからのγ線を照射した２つの検出器応答の2次元プロット

--- SLIDE 03 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
目次
光子検出
中性子検出
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 04 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
photon.inp
基本設定
線源：
体系：
タリー：
60Coからのγ線源 (1.173 and 1.332 MeV)
NaIシンチレータ２台 (2 inch x 2 inch Φ）
[t-track]によるフルエンス分布
[t-deposit]による領域１内のエネルギー付与頻度分布
（波高分布）
track_xz.eps
deposit.eps
MENTIONED_INPUT_NAMES: photon.inp

--- SLIDE 05 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
重要パラメータ
[ parameters ]
 icntl =  0
maxcas = 10000
maxbch = 5
file(6)  = phits.out
negs = 1
e-mode = 2
…
このタリーを使う場合、カーマ近似は使用不可 → カーマ近似は付与エネルギーの平均値を推定する手法でその分散は評価できないため
電子輸送が必須 → negs = 1
イベントジェネレータモードを使った荷電粒子生成が必須 → e-mode = 2
検出器応答関数（波高分布）計算には[t-deposit] with output = depositを用いる
各ヒストリーにおける付与エネルギーの頻度分布をタリーする
[ t-deposit ]
...
unit =    3
output = deposit
axis = eng
e-type = 2
ne = 300
emin = 0.0
emax = 3.0

--- SLIDE 06 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
[t-deposit]計算結果の解釈
MCA (Multi-Channel Analyzer)により得た波高分布
全吸収ピーク
それぞれ1.173 & 1.332 MeVのγ線に対応
カウント / sec
コンプトンエッジ
それぞれ1.173 & 1.332 MeVのγ線に対応

--- SLIDE 07 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１
検出器分解能を考慮しよう
付与エネルギーと波高は必ずしも一致しない → 電子的ノイズ、W値やε値のゆらぎ、クエンチング効果などが原因
測定で得られたピークやエッジは、計算で得られたものと比べて拡がりを持ち、ぼやけてしまう
PHITSは、計算した各ヒストリーの付与エネルギーを標準偏差σのガウス分布で強制的にばらつかせることにより、検出器の分解能を再現することができる
dresol = 0.01及びdfano = 0.001を[t-deposit]に加えてPHITSを実行
*dresol < 0の場合はusrresol.fに書かれたユーザー定義分解能が適用される
ANSWER_FILE: input/photon-2.inp

--- SLIDE 08 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
回答１
[ t-deposit ]
...
 part =  all
 epsout =    1
 dresol = 0.01
 dfano = 0.001
deposit.eps

--- SLIDE 09 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題２
dfanoを変更して検出器の分解能変化を実感しよう
より分解能の悪い検出器の応答を再現するには？(dfano=0.01)
より分解能の良い検出器の応答を再現するには？(dfano=0.0001)
ANSWER_FILE: input/photon-3.inp

--- SLIDE 10 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
回答２
dfano = 0.01
dfano = 0.0001
低分解能
高分解能
deposit.eps
deposit.eps

--- SLIDE 11 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
dresolとdfanoの決定方法
理想検出器
dresol = 0.01
dfano = 0.001
broader
一般にdresolは極めて小さい → dfanoが分解能を支配的に決める
例えば測定から推定される標準偏差σが1.332MeVにおいて0.05MeVの場合、dfano = (0.05)2/1.332 = 0.00187 となる

--- SLIDE 12 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
相関線源オプション
60Co
β- 99.88%
β- 0.12%
0.30 ps
0.713 ps
1173.228 keV
99.85%
1332.492 keV
99.98%
60Ni
*60Coの崩壊図式
60Coの１回の崩壊より、（ほぼ）同時に２本のγ線が放出される
時々、１つの検出器が２本のγ線のエネルギーを同時に吸収し、あたかも2.506MeVのγ線を検出したようなサムアップ(sum-up)ピークを形成することがある
検出器が２台ある場合、それぞれの検出器が同時にγ線を検出して同期（coincidence）イベントを形成することがある
２つのγ線を１つのヒストリーとして同時に発生させる必要がある
*極めて低い確率(2x10-8)で第２励起準位から基底状態への遷移が起き、 2.50569 MeVのγ線を放出することがある

--- SLIDE 13 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題３
60Co線源を相関線源オプションを使って表現してみよう
RI線源モードから単色線源モード（E = 1.173 MeV）に切り替える
     （“e-type”サブセクションを削除して“e0”パラメータを[source]に加える）
上記設定した線源をコピペしてmulti-sourceとし、２つ目のエネルギーを1.332 MeVとする
iscorrパラメータを0から1に変更する
     (iscorr = 0: 独立multi-source, = 1: 相関multi-source)
[ S o u r c e ]
totfact =
iscorr =
<source> = 1.0
・ ・ ・ ・ ・ ・
 e-type = 28
       ni = 1
 Co-60  1.0e3
 e0 =
deposit.epsに約2.5 MeVのサムアップピークが出現
totfactを2,000として、1000 Bq（= 2,000 光子/sec）の状態を再現する*
dfanoを0.001に戻す
*相関線源の場合、１ヒストリーで２粒子発生させる（計算時間が倍になる）が、タリー結果の規格化は変わらない（１粒子発生当たり）
ANSWER_FILE: input/photon-4.inp

--- SLIDE 14 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
回答３
[ S o u r c e ]
totfact = 2.0e3
iscorr = 1
<source> = 1.0
s-type = 1
proj = photon
...
$ e-type = 28
 $      ni = 1
 $ Co-60  1.0e3
 e0 = 1.173
<source> = 1.0
s-type = 1
proj = photon
...
$ e-type = 28
 $      ni = 1
 $ Co-60  1.0e3
 e0 = 1.332
deposit.eps
Sum-up peak
at 2.505 MeV
(1.173 + 1.332)

--- SLIDE 15 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
同期（Coincidence）イベント
100 MeV/n炭素イオンで水ターゲットを照射したときのdE-E検出応答2次元プロットの例 （[t-deposit2]で描画*）
原子核実験では、２つの検出器からの出力を2次元プロットとして表し、その相関により入射した粒子を特定する手法がよく用いられる
そのような2次元プロットは、 [t-deposit2]タリーを用いてPHITSで直接再現可能
dE-E検出器
dE
E
dE検出器: 阻止能を測定
E検出器: 全運動エネルギーを測定
*この描画に使ったインプットファイルは “dE-E_detector”フォルダに格納されています
p
d
n
α
実験の例

--- SLIDE 16 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題４
検出器#1と#2の出力に対する2次元プロットを描画しよう
[t-deposit2]を有効化して実行し、deposit2.epsをチェック
[ T - Deposit2 ] off
 mesh =  reg
      reg =  1 2
  e1-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol1 = 0.01
   dfano1 = 0.001
  e2-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol2 = 0.01
   dfano2 = 0.001
     unit =    1
     axis =    e12
 ...
付与エネルギーを計算する２つの領域番号
１つ目の領域に対するe-type
１つ目の領域に対するdresol & dfano
２つ目の領域に対するe-type
２つ目の領域に対するdresol & dfano
軸の指定。e12の場合、X軸に１つ目の領域、Y軸に２つ目の領域に対するタリー結果をプロットする
ANSWER_FILE: input/photon-5.inp

--- SLIDE 17 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
回答４
deposit2.eps
領域１のみ検出
２本のγ線が各領域でそれぞれ全吸収されたイベント
領域２のみ検出

--- SLIDE 18 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題５
検出器#1の応答関数を同期・非同期イベントに弁別して計算しよう
e2-type = 1として、同期（E≧0.1MeV）と非同期（E<0.1MeV）の２群(ne=2)に分けるようにする
  （type=1の場合は、エネルギー分点を直接与える）
axis = eng1として、検出器#1の応答関数を出力するようにする
samepage = eng2を加えて、同じページに同期・非同期イベントに対する応答関数を表示するようにする
[ T - Deposit2 ]
mesh =  reg
      reg =  1 2
  e1-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol1 = 0.01
   dfano1 = 0.001
  e2-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol2 = 0.01
   dfano2 = 0.001
     unit =    1
     axis =    e12
 ...
ANSWER_FILE: input/photon-5.inp

--- SLIDE 19 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
回答５
deposit2.eps
サムアップピークは、非同期イベントの応答関数のみに観測される
[ T - Deposit2 ]
mesh =  reg
      reg =  1 2
  e1-type =    2
       ne =  300
    emin  =  0.0
    emax  =  3.0
  dresol1 = 0.01
   dfano1 = 0.001
  e2-type =    1
       ne =  2
0  0.1  3.0
$    emin  =  0.0
$   emax  =  3.0
  dresol2 = 0.01
   dfano2 = 0.001
     unit =    1
     axis =   eng1
samepage = eng2
 ...
検出器#2で発生したコンプトン散乱によるγ線が検出器#1で全吸収されたピーク（同期イベントのみで観測）

--- SLIDE 20 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
目次
光子検出
中性子検出
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 21 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
neutron.inp
基本設定
単色ペンシルビームの20MeV中性子
有機シンチレータ (2 inch x 2 inch Φ）
[t-track]によるフルエンス分布
[t-deposit]による領域１内のエネルギー付与頻度分布
（波高分布）
track_xz.eps
deposit_n.eps
線源：
体系：
タリー：
MENTIONED_INPUT_NAMES: neutron.inp

--- SLIDE 22 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
重要ポイント
SCINFULモードの利用方法
有機シンチレータの中性子応答関数を計算するためには、150MeV以下の中性子によるn-C反応断面積データベースを利用するSCINFULモード* の利用が奨励
[parameters]セクションにてiscinful = 1と定義しSCINFULモードを有効にする
[data max]セクションを定義し、n-C反応のモデル利用下限値をSCINFUL断面積データベースのある下限値（0.1MeV）に設定する（この設定がないと20MeV以下で通常の核データライブラリが使われてしまう）
*D. Satoh et al., J. Nucl. Sci. Technol. 59, 1047-1060 (2022)
[ Parameters ]
icntl = 0
...
iscinful = 1
[Data Max]
part = neutron
 mat  nucleus   dmax
   1        C        0.10
有機シンチレータを定義した物質ID
発光量分布をMeVee単位で出力したい場合は、SCINFUL専用のユーザー定義タリー（phits/utility/usrtally/scinful-qmd）を使ってPHITSを再コンパイルする
更に上級の使い方

--- SLIDE 23 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１
応答関数に見られる様々なピークの原因を調べよう
[t-deposit]のpartをall proton deuteron alpha Cに変更して、各荷電粒子の応答関数への寄与割合を出力する
これらのピークは何に起因？
deposit_n.eps
ANSWER_FILE: input/photon-2.inp

--- SLIDE 24 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
回答１
deposit_n.eps
[t-deposit]でoutput = depositかつdeposit = 0 (初期値)*の場合、partは、そのエネルギーを付与したイベントにおける各粒子からの寄与割合を示す
陽子 100% (20 MeV)
[ T - Deposit ]
...
file = deposit_n.out
part = all proton deuteron alpha C
...
陽子 50% (~7 MeV)
α粒子 50% (~7 MeV)
重陽子 80% (~5 MeV)
陽子 20% (~1.2 MeV)
*deposit = 1の場合は、各粒子毎の付与エネルギーに対してそれぞれ応答関数を計算する

--- SLIDE 25 ---
PPTX_FILE: phits-detector-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題２
付与エネルギーの検出下限値が1 MeVの場合の検出効率を計算しよう
検出効率 =
検出器に入射した放射線の数
検出下限値以上の付与エネルギーを与えた放射線の数
=
あるしきい値以上の付与エネルギーを与えたイベントの積分値
（ただし、全ての線源が検出器に入射するように設定した場合）
[ T - Deposit ]
...
  e-type = 2
  ne = 210
  emin = 0.0
  emax = 21.0
...
[t-deposit]のe-typeサブセクションを変更して、1 MeVから108MeV までの１群にする
deposit_n.outを開いてタリー結果を確認
ANSWER_FILE: input/photon-3.inp

--- SLIDE 26 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
回答２
[ T - Deposit ]
...
  e-type = 2
  ne = 1
  emin = 1.0
  emax = 1.0e8
...
約20%の入射中性子が検出される
… (lines around 32)
x: Deposit Energy [MeV]
y: Number [1/source]
p: xlin ylog afac(0.8) form(0.9)
h: n            x            y(all     ),hh0l n
#  e-lower      e-upper        all       r.err
   1.0000E+00   1.0000E+08   2.1782E-01  0.0068
...
neutron.inp
deposit_n.out
実際の中性子フルエンスは、検出した数の約５倍と推定できる
MENTIONED_INPUT_NAMES: neutron.inp

--- SLIDE 27 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
目次
光子検出
中性子検出
まとめ
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 28 ---
PPTX_FILE: phits-detector-en.pptx
SLIDE_TEXT:
まとめ
検出器応答関数を計算するには、[t-deposit] with output = depositを利用する
ヒストリー毎の分散を計算するため、EGSモード(negs = 1)とイベントジェネレータモード(e-mode = 2)は必ず利用する
有機シンチレータの中性子応答関数を計算する場合はSCINFULモード(iscinful = 1 & [data max])の利用が奨励される
検出器分解能はdresolとdfanoで定義する
相関線源モード(iscorr = 1)や2次元プロットタリー[t-deposit2]は同期イベントが重要となる応答関数計算で有用となる

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/neutron-1.inp
FILE: input/neutron-2.inp
FILE: input/neutron-final.inp
FILE: input/photon-1.inp
FILE: input/photon-final.inp

[BONUS_TEXT_FILES]
NOTE: None
