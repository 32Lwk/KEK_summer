# Lecture: therapy/BNCT

SOURCE_FOLDER: D:/NEAgit/lecture/therapy/BNCT
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: BNCT
LECTURE_PATH_INDEX: lecture/therapy/BNCT
PPTX_FILES: phits-lec-BNCT-en.pptx, phits-lec-BNCT-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: BNCT
SECTION_KEYWORDS: 1, 2, anatally, t-deposit

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/therapy/BNCT
LECTURE_PATH_INDEX: lecture/therapy/BNCT
PPTX_FILES: phits-lec-BNCT-en.pptx, phits-lec-BNCT-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 1
SLIDE_COUNT: 30
EXERCISE_SLIDE_COUNT: 8
BONUS_INPUT_COUNT: 2
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- BNCT.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: BNCT dose calculation using PHITS
- SLIDE 02: Boron Neutron Capture Therapy
- SLIDE 03: Application of PHITS to BNCT
- SLIDE 04: H. Kumada et al. Ther. Radiol. Oncol. 2, 50 (2018)
- SLIDE 05: BNCT.inp
- SLIDE 06: Tally Results from BNCT.inp
- SLIDE 07: EXERCISE 1 | Increase 10B concentration in tumor (region 2) from 10 ppm to 20 ppm
  ANSWER_FILE: input/BNCT-2.inp
- SLIDE 08: Answer 1
- SLIDE 09: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/BNCT-3.inp
- SLIDE 10: EXERCISE 3 | Exercise 3
  ANSWER_FILE: input/BNCT-4.inp
- SLIDE 11: Answer 3
- SLIDE 12: Photon Isoeffective Dose
- SLIDE 13: EXERCISE 4 | Exercise 4
  ANSWER_FILE: input/BNCT-4.inp
- SLIDE 14: Answer 4
- SLIDE 15: Summary
- SLIDE 01: PHITSを用いたBNCT線量計算
- SLIDE 02: BNCTとは？
- SLIDE 03: PHITSのBNCT応用
- SLIDE 04: 4
- SLIDE 05: BNCT.inp
- SLIDE 06: BNCT.inpの実行結果
- SLIDE 07: EXERCISE 1 | 課題１
  ANSWER_FILE: input/BNCT-2.inp
- SLIDE 08: 回答１
- SLIDE 09: EXERCISE 2 | 課題２
  ANSWER_FILE: input/BNCT-3.inp
- SLIDE 10: EXERCISE 3 | 課題３
  ANSWER_FILE: input/BNCT-4.inp
- SLIDE 11: 回答３
- SLIDE 12: 光子等効果線量（Photon Isoeffective Dose)
- SLIDE 13: EXERCISE 4 | 課題４
  ANSWER_FILE: input/BNCT-4.inp
- SLIDE 14: 回答４
- SLIDE 15: まとめ

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: BNCT.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
BNCT dose calculation using PHITS
Mar. 2025 revised
/phits/lecture/therapy/bnct

--- SLIDE 02 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
Boron Neutron Capture Therapy
BNCT is a radiation therapy for treating invasive tumors using a large neutron capture cross section of 10B. A tumor-localizing drug containing 10B is injected to patients and neutron beams are externally irradiated. Then, alpha and 7Li produced by 10B capture reaction selectively kill the tumor cells due to their short ranges.
Tumor cell
Normal cell
10B drug
Li ion
α particle
Neutron Beam
Before irradiation
During irradiation
After irradiation
Cell death
Capture reaction

--- SLIDE 03 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
Application of PHITS to BNCT
3
Estimation of therapeutic effect
nucleus
cytoplasm
nucleus
cytoplasm
Dose analysis in cellular scale
BPA in
cytoplasm
BSH on
membrane
T. Sato et al. Sci. Rep. 8, 988 (2018)
Treatment Planning System
NeuCureTM by S.H.I.
Approved by PMDA：30200BZX00083000
Tsukuba Plan
Kumada et al. Radiat. Prot. Dosim. 180, 286 (2018)

--- SLIDE 04 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
H. Kumada et al. Ther. Radiol. Oncol. 2, 50 (2018)
Boron dose from n + 10B -> α + Li ion (CBE=2.5~3.8)
Photon dose from γ + X -> electron (RBE=1)
Hydrogen dose from n + H -> n’ + p (RBE=2.5~3.2)
Nitrogen dose from n + 14N -> p +14C (RBE=2.5~3.2)
Dose from each component must be evaluated separately
because their relative biological effectiveness (RBE) is different
Relative Biological Effectiveness (RBE) = 1, i.e., Reference radiation
In principle, RBE depends on neutron fields because of the difference in recoil proton spectra
RBE is independent of neutron fields because of the constant proton energy (0.58 MeV)
Compound Biological Effectiveness (CBE) concept is adopted instead of RBE because biological effectiveness depends not only on radiation quality but also intra- and inter-cellular heterogeneity of 10B compound
For tumor, CBE is 3.8 and 2.5 for BPA and BSH, respectively
Four dose components in BNCT

--- SLIDE 05 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
BNCT.inp
Basic setup
Source：

Geometry：

Tally：
Epi-thermal neutron beam  (E = 10-5 MeV, r = 10 cm)
(Intensity is normalized to give approximately 10 Gy at surface)
Cylindrical ICRU soft tissue with 10 ppm 10B  (t = 10cm, r = 10 cm)
(Tumor region is assumed to be located at the depth of 3 to 4 cm)
[t-deposit] X ４: Calculate BNCT four dose components
（Kerma factor* for each nuclide can be specified by mother parameter)
Neutron
10-5 MeV
ICRU soft tissue
with 10 ppm 10B
[t-deposit]
…
   file = boron.out
   mother = 1
            B
     part = neutron
E.g. Tally for calculating
the boron dose component
Tumor
Region
*e-mode and EGS should not be used when the kerma approximation is used
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 06 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
Tally Results from BNCT.inp
boron.eps
hydro.eps
nitro.eps
photon.eps
Boron and nitrogen doses are proportional to each other because they depend on the thermal neutron flux
Hydrogen doses are almost zero because no high-energy neutron exists in the phantom
Photon doses are higher at deeper locations compared with other components
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Increase 10B concentration in tumor (region 2) from 10 ppm to 20 ppm
[ M a t e r i a l ]
…
m2    $ Tumor (region 2)
            H     -0.101
            C     -0.111
            N     -0.026
            O     -0.762
          10B     -1.0e-5
mt2   lwtr.20t
BNCT.inp
Change the material composition of m2 (for tumor)
Molecular structures influence the behavior of thermal neutrons; therefore, when calculating the behavior of thermal neutrons in water (or biological materials) accurately, proper definitions are required (lwtr.20t refers to light water).
Thermal neutron scattering kernel
Exercise 1
MENTIONED_INPUT_NAMES: BNCT.inp
ANSWER_FILE: input/BNCT-2.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
Answer 1
boron.eps
hydro.eps
nitro.eps
photon.eps
Boron dose at 3~4 cm becomes double
The rests are almost the same
[ M a t e r i a l ]
…
m2    $ Tumor (region 2)
            H     -0.101
            C     -0.111
            N     -0.026
            O     -0.762
          10B     -2.0e-5
mt2   lwtr.20t
BNCT.inp
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
[ S o u r c e ]
   s-type =   1
     proj =  neutron
       e0 =   1.0e-5
…
[ S o u r c e ]
   s-type =   1
     proj =  neutron
       e0 =   1.0e-2
…
BNCT.inp
hydro.eps
nitro.eps
photon.eps
Boron.eps
Increase neutron energy from 10 eV to 10 keV
Neutrons can penetrate deeper locations
Hydrogen doses increase dramatically owing to larger high-energy neutron fluences
MENTIONED_INPUT_NAMES: BNCT.inp
ANSWER_FILE: input/BNCT-3.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
Calculate equivalent dose using anatally function (icntl = 17)
[ P a r a m e t e r s ]
 icntl    =           0
...
[anatally]  $ for RBE-CBE weighted dose
 set: c99[0.0]   $ Weighted sum (=0)
 set: c90[1.0]   $ dose scaling factor
 set: c1[1.0*c90]   $ RBE for photon dose
 set: c2[2.5*c90]   $ RBE for hydrogen dose
 set: c3[2.5*c90]   $ RBE for nitrogen dose
 set: c4[3.8*c90]   $ CBE for boron dose
anatally start    1
manatally = 0
sfile=RBEdose.out
nfile =       4
photon.out
hydro.out
nitro.out
boron.out
BNCT.inp
[Anatally] must be used for analyzing multiple tally results
[Anatally] is activated only when icntl = 17.
Analysis procedure can be revised by changing usranatal.f*
Default program is to calculate the weighted sum of each tally results using the weighting factors c1-cn
RBEdose.out  = photon.out x c1
           + hydro.out x c2
                    + nitro.out x c3
                    + boron.out x c4
*Please see \phits\utility\usranatal in more detail
MENTIONED_INPUT_NAMES: BNCT.inp
ANSWER_FILE: input/BNCT-4.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
Answer 3
BNCT.inp
RBEdose.out
  = photon.out x c1
  + hydro.out x c2
  + nitro.out x c3
  + boron.out x c4
RBEdose.eps
Equivalent doses are higher than absorbed doses by 2~3 times
[ P a r a m e t e r s ]
 icntl    =           17
   ireschk = 1 $ (D=0) Restart calculation check
...
[anatally]  $ for RBE-CBE weighted dose
 set: c99[0.0]   $ Weighted sum (=0)
 set: c90[1.0]   $ dose scaling factor
 set: c1[1.0*c90]   $ RBE for photon dose
 set: c2[2.5*c90]   $ RBE for hydrogen dose
 set: c3[2.5*c90]   $ RBE for nitrogen dose
 set: c4[3.8*c90]   $ CBE for boron dose
anatally start    1
manatally = 0
sfile=RBEdose.out
nfile =       4
photon.out
hydro.out
nitro.out
boron.out
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
Photon Isoeffective Dose
RBE should be lower with increase of the absorbed dose
For considering the dose dependence of RBE, the concept of photon isoeffective dose (DISO) was proposed by Gonzalez et al. (2012)*
Although the RBE-weighted dose is still used in TPS of BNCT, many studies have been published for estimating DISO for BNCT
*Gonzalez et al. Radiat Res. 178, 609 (2012); **Sato et al. Radiat. Res. 178, 341 (2012)
In PHITS, the DISO for BNCT and carbon-ion therapy can be calculated by Stochastic Microdosimetric Kinetic (SMK) Model**, using anatally function
In the calculation, the absorbed dose should be normalized to the actual irradiation condition (e.g. 10 Gy at skin), using totfact in [source] or c90 parameter written in [anatally]
RBE as a function of absorbed dose

--- SLIDE 13 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
Let’s calculate photon isoeffective dose
BNCT.inp
For calculating photon-isoeffecitve dose, set c99 parameter in [anatally] to 1 for utilizing the FFT-based SMK model [1]
FFT-based SMK model can estimate the biological effectiveness by considering the intra- and inter-cellular heterogeneity of 10B compounds
In default, the SMK model parameters are set to reproduce the results of cell survival experiment [2] in which BPA was administered to mice bearing Squamous Cell Carcinoma
[anatally]  $ for RBE-CBE weighted dose
$ parameters used in anatally (icntl=17) (same as default value)
 set: c99[0.0]    $ Weighted sum (=0) FFT SMK (=1), Taylor-expansion SMK (=2),…
Change c99 to 1.0, run PHITS, and check RBEdose.eps
[1] T. Sato et al. Int. J. Radiat. Biol. 97, 1450-1460 (2021)
[2] S. Masunaga et al. Springerplus 3, 128 (2014)
MENTIONED_INPUT_NAMES: BNCT.inp
ANSWER_FILE: input/BNCT-4.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
Answer 4
BNCT.inp
[anatally]  $ for RBE-CBE weighted dose
$ parameters used in anatally (icntl=17) (same as default value)
 set: c99[1.0]    $ Weighted sum (=0) FFT SMK (=1), Taylor-expansion SMK (=2),…
RBEdose.eps
Equivalent dose: c99[0.0]
RBEdose.eps
Photon isoeffective dose: c99[1.0]
The photon isoeffective dose becomes smaller than the equivalent dose, particularly at higher doses, because the dose dependency of RBE is considered
*Please see \phits\utility\usranatal\smk_bnct in more detail
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
Summary
Four dose components must be evaluated separately using [t-deposit] with mother parameter.
The equivalent dose, based on fixed RBE and CBE factors, can be estimated for each dose component using the anatally function.
The photon-isoeffective dose can also be calculated with the anatally function by utilizing the FFT-based SMK model.
For BNCT simulation using PHITS…

--- SLIDE 01 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
PHITSを用いたBNCT線量計算
2025年3月改訂
/phits/lecture/therapy/bnct

--- SLIDE 02 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
BNCTとは？
BNCT（Boron Neutron Capture Therapy、ホウ素・中性子捕捉療法）とは、高い中性子捕捉断面積を持つ10Bを用いた浸潤性がんに対する放射線治療法
がん細胞に集積性を持つ10B化合物をあらかじめ患者に投与し、中性子を照射してその補足反応により発生した飛程の短いα粒子とLiイオンにより選択的にがん細胞のみを死滅させる
がん細胞
正常細胞
ホウ素薬剤
Liイオン
α粒子
中 性 子 ビ ー ム
照射前
照射中
照射後
細胞死
核反応

--- SLIDE 03 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
PHITSのBNCT応用
3
Tsukuba Plan
Kumada et al. Appl. Radiat. Iso. 166, 109222 (2020)
薬剤治療効果推定モデル
細胞核
細胞質
細胞核
細胞質
細胞レベルの線量解析結果
細胞内浸潤
薬剤（BPA）
細胞膜付着
薬剤（BSH）
T. Sato et al. Sci. Rep. 8, 988 (2018)
BNCT用治療計画システム
NeuCureTM (住友重機械工業)
医療機器製造販売承認番号 ：30200BZX00083000
薬剤集積性を考慮した治療効果比の評価

--- SLIDE 04 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
4
BNCT線量評価の特徴
H. Kumada et al. Ther. Radiol. Oncol. 2, 50 (2018)
n + 14N -> p +14C
γ + X -> electron
n + H -> n’ + p
n + 10B -> α + Li ion
ホウ素線量（CBE=2.5～3.8）
光子線量（RBE=1）
水素線量（RBE=2.5～3.2）
窒素線量（RBE=2.5～3.2）
反応チャンネル毎に生物効果比（RBE）が異なるため、４つの成分に分けて線量を評価する必要がある
基準放射線のため生物学的効果比（RBE） は 1
反跳陽子スペクトルが異なるため、RBEは中性子場に依存。ただし、その依存性は考慮しない場合が多い
0.58MeVの陽子による線量寄与のため、RBEは水素線量とほぼ同じ
生物効果は10B薬剤の細胞内分布に依存するため、その違いを考慮したCompound Biological Effectiveness (CBE) で表現
例えば、腫瘍に対するCBEは、BPAが3.8、BSHが2.5くらい
正常組織に対するCBEは一般に低い（薬剤が取り込まれにくいため）

--- SLIDE 05 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
BNCT.inp
基本設定
熱外中性子ビーム  (E = 10-5 MeV, r = 10 cm)
(照射表面の線量がおおよそ10Gyとなるように規格化）
円柱状のICRU軟組織＋10 ppmの10B  (t = 10cm, r = 10 cm)
（深さ３～4cmに腫瘍があると仮定し、領域を分割）
[t-deposit]×４：BNCTの線量４成分の深さ分布をそれぞれ計算
（motherパラメータを指定することにより元素別のカーマファクタを利用*）
入射粒子：

体系：

タリー：
中性子
10-5 MeV
ICRU軟組織
＋10 ppm 10B
*カーマ近似を使うためe-modeやEGSは使用しない
[t-deposit]
…
   file = boron.out
   mother = 1
            B
     part = neutron
例：ホウ素線量の計算方法
腫瘍を
想定
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 06 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
BNCT.inpの実行結果
boron.eps
hydro.eps
nitro.eps
photon.eps
ホウ素線量と窒素線量は、どちらも熱中性子フラックスにほぼ比例するので同じ深さ分布
高エネルギー中性子が存在しないため水素線量はほとんどない
光子線量は、中性子線量よりも深い位置まで届く

--- SLIDE 07 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
課題１
腫瘍（領域２）における10B濃度を10 ppmから20 ppmに増やそう
[ M a t e r i a l ]
…
m2    $ Tumor (region 2)
            H     -0.101
            C     -0.111
            N     -0.026
            O     -0.762
          10B     -1.0e-5
mt2   lwtr.20t
BNCT.inp
熱中性子の挙動は分子構造の影響を受けるため、水（もしくは生体物質）中の熱中性子挙動を正確に計算したい場合は定義が必要（lwtr.20tは軽水を意味する）
熱中性子散乱測データライブラリ名
m2（Tumorの方）を変更する
MENTIONED_INPUT_NAMES: BNCT.inp
ANSWER_FILE: input/BNCT-2.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
回答１
boron.eps
hydro.eps
nitro.eps
photon.eps
ホウ素線量の３～４ｃｍのみ線量が３倍になる
それ以外の線量にほとんど影響はない
[ M a t e r i a l ]
…
m2    $ Tumor (region 2)
            H     -0.101
            C     -0.111
            N     -0.026
            O     -0.762
          10B     -2.0e-5
mt2   lwtr.20t
BNCT.inp
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 09 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題２
入射中性子エネルギーを10 eVから10 keVに変更しよう
[ S o u r c e ]
   s-type =   1
     proj =  neutron
       e0 =   1.0e-5
…
[ S o u r c e ]
   s-type =   1
     proj =  neutron
       e0 =   1.0e-2
…
BNCT.inp
より深くまで線量が届くようになる
特に高エネルギー中性子による寄与の大きい水素線量が大きくなる
hydro.eps
nitro.eps
photon.eps
Boron.eps
MENTIONED_INPUT_NAMES: BNCT.inp
ANSWER_FILE: input/BNCT-3.inp

--- SLIDE 10 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題３
各成分の線量にRBE/CBEを乗じて等価線量を計算しよう
[ P a r a m e t e r s ]
 icntl    =           0
...
[anatally]  $ for RBE-CBE weighted dose
 set: c99[0.0]   $ Weighted sum (=0)
 set: c90[1.0]   $ dose scaling factor
 set: c1[1.0*c90]   $ RBE for photon dose
 set: c2[2.5*c90]   $ RBE for hydrogen dose
 set: c3[2.5*c90]   $ RBE for nitrogen dose
 set: c4[3.8*c90]   $ CBE for boron dose
anatally start    1
manatally = 0
sfile=RBEdose.out
nfile =       4
photon.out
hydro.out
nitro.out
boron.out
BNCT.inp
複数のタリー結果に対する演算を行うには[Anatally]を使う
[Anatally]はicntl = 17で動作する。
演算方法は、usranatal.fを編集してコンパイルすることにより変更可能*
初期プログラムは、各タリー結果をc1-cnパラメータで重みづけてして加算し、結果をsfileに出力
RBEdose.out  = photon.out x c1
           + hydro.out x c2
                    + nitro.out x c3
                    + boron.out x c4
*詳細は\phits\utility\usranatalを参照
MENTIONED_INPUT_NAMES: BNCT.inp
ANSWER_FILE: input/BNCT-4.inp

--- SLIDE 11 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
回答３
BNCT.inp
RBEdose.out
  = photon.out x c1
  + hydro.out x c2
  + nitro.out x c3
  + boron.out x c4
吸収線量より２～３倍、大きい
[ P a r a m e t e r s ]
 icntl    =           17
   ireschk = 1 $ (D=0) Restart calculation check
...
[anatally]  $ for RBE-CBE weighted dose
 set: c99[0.0]   $ Weighted sum (=0)
 set: c90[1.0]   $ dose scaling factor
 set: c1[1.0*c90]   $ RBE for photon dose
 set: c2[2.5*c90]   $ RBE for hydrogen dose
 set: c3[2.5*c90]   $ RBE for nitrogen dose
 set: c4[3.8*c90]   $ CBE for boron dose
anatally start    1
manatally = 0
sfile=RBEdose.out
nfile =       4
photon.out
hydro.out
nitro.out
boron.out
RBEdose.eps
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
光子等効果線量（Photon Isoeffective Dose)
RBEは、線量の増加とともに下がるが、その効果は等価線量では考慮されていない
RBEの線量依存性を考慮可能な光子等効果線量(DISO)がGonzalezら*により提案されている
実際の治療計画ではDISOは使われていないが、数多くのモデルがDISOを評価するために開発されている
*Gonzalez et al. Radiat Res. 178, 609 (2012); **Sato et al. Radiat. Res. 178, 341 (2012)
PHITSでは、Stochastic Microdosimetric Kinetic (SMK)モデル**に基づいて BNCTと炭素線治療に対するDISOを計算可能
DISOの計算には、吸収線量の絶対値が必要なため、実際の照射条件を[source]のtotfactや[anatally]のc90パラメータで再現する必要がある
吸収線量の関数として表したRBE

--- SLIDE 13 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
課題４
光子等効果線量（Photon-Isoeffective Dose）を評価しよう
BNCT.inp
光子等効果線量を計算するには、[anatally]のc99パラメータを1にしてFFT-based SMKモデル[1]を使う
FFT-based SMKモデルは、薬剤の細胞内・細胞間不均一性や対象細胞の放射線感受性の違いなどを考慮できる
初期設定では、扁平上皮がん(Squamous Cell Carcinoma）を担ったマウスにBPAを投与した細胞生存率実験結果[2]を再現するように設定されている
[anatally]  $ for RBE-CBE weighted dose
$ parameters used in anatally (icntl=17) (same as default value)
 set: c99[0.0]    $ Weighted sum (=0) FFT SMK (=1), Taylor-expansion SMK (=2),…
c99を1.0としてPHITSを実行し、RBEdose.epsの変化を確認
詳細は\phits\utility\usranatal\smk_bnctを参照
[1] T. Sato et al. Int. J. Radiat. Biol. 97, 1450-1460 (2021)
[2] S. Masunaga et al. Springerplus 3, 128 (2014)
MENTIONED_INPUT_NAMES: BNCT.inp
ANSWER_FILE: input/BNCT-4.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
回答４
BNCT.inp
[anatally]  $ for RBE-CBE weighted dose
$ parameters used in anatally (icntl=17) (same as default value)
 set: c99[1.0]    $ Weighted sum (=0) FFT SMK (=1), Taylor-expansion SMK (=2),…
RBEdose.eps
等価線量: c99[0.0]
RBEdose.eps
光子等効果線量: c99[1.0]
光子等効果線量は、RBEの線量依存性を考慮するため、特に高線量側で等価線量と比べて小さくなる
MENTIONED_INPUT_NAMES: BNCT.inp

--- SLIDE 15 ---
PPTX_FILE: phits-lec-BNCT-en.pptx
SLIDE_TEXT:
まとめ
[t-deposit]とmotherを組み合わせ、ホウ素・水素・窒素・光子線量に分けて吸収線量を評価する
RBEやCBEを考慮した等価線量や光子等効果線量は、[anatally]を使って評価する
SMKモデルを使えば、薬剤の細胞内・細胞間不均一性や対象細胞の放射線感受性の違いなどを考慮した解析が可能となる
PHITSを用いたBNCT線量評価のためには…

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/BNCT-1.inp
FILE: input/BNCT-final.inp

[BONUS_TEXT_FILES]
NOTE: None
