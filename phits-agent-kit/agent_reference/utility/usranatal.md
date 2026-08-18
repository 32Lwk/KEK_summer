# Utility: usranatal

SOURCE_FOLDER: D:/NEAgit/utility/usranatal
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: usranatal
UTILITY_PATH_INDEX: utility/usranatal
UTILITY_FOLDER_NAME: usranatal

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/usranatal
BASIC_FILE_COUNT: 2
BASIC_FILE: readme-eng.docx
BASIC_FILE_TYPE: docx
BASIC_FILE: readme-jpn.docx
BASIC_FILE_TYPE: docx
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 8
BONUS_TEXT_COUNT: 11

[BASIC_FILES]
FILE: readme-eng.docx
BEGIN_BASIC_TEXT
Examples of user-defined anatally "usranatal.f"
The user-defined anatally function is designated for analyzing multiple tally results, using user-defined program written in usranatal.f. It works only when icntl = 17. The mesh numbers, e.g., nx, ny, nz, ne, for each tally must be the same for one another. The tally consistence check option must be disabled, i.e., ireschk = 1 when this function is used. The followings are the list of important variables used in usranatal.f.
jmax: Number of tally output files to be analyzed, i.e., nfile specified in [anatally] section.
rdata(2,jmax): Tally results, rdata(1,*), and their relative errors, rdata(2,*), to be analyzed.
answer: Output data to be written in sfile specified in [anatally] section.
rerr: Relative error to be written in sfile specified in [anatally] section.
cval: User-defined constants, c1-c99, specified in the PHITS input file. If these parameters are specified by multiple times in the input file, the lastly defined value is effective in usranatal.f.
The default program of usranatal.f can deduce the weighted sum of each tally result in similar to the sumtally function, or the photon isoeffective dose for BNCT based on the SMK model,,. The toggle to switch these two modes is c99. Their sample inputs are included in "weighted_sum" and "smk_bnct" folders, respectively. The sample program and input file for calculating the dose-mean LET, the biological dose for charged particle therapy and targeted alpha therapy based on the SMK model are also included in "LETd", "smk_ion" and "smk_tat" folders, respectively, though the compilation of PHITS is needed to use this program. The instructions to use these samples are given below.
Weighted sum mode: "weighted_sum"
This mode works when c99 is equal to 0 or not specified. The sample input file (weighted_sum/phits.inp) outputs dose_all.out and dose_primary.out, which contain the total doses Dall and primary-ion doses Dpri for carbon-ion therapy, respectively. By setting icntl = 17 in the input file, [anatally] is activated and it calculates the weighted sum of the total and primary-ion doses, where the weighted factors are 1.0 and -1.0 as defined by c1 and c2 parameters, respectively. Thus, answer obtained from the program is Dall - Dpri = Dsec, which corresponds to the secondary particle dose. Note that the relative error is simply obtained from the uncertainty propagation rule for independent variables, and thus, it is not correct in the cases that each tally result is correlated with one another, e.g., in this sample, a part of the total dose is contributed from the primary particles.
Photon isoeffective dose calculation mode for BNCT: "smk_bnct"
The therapeutic and side effects of BNCT are generally estimated from the RBE-weighted dose, which can be calculated from the absorbed doses of boron, hydrogen, nitrogen, and photon components multiplied with their relative biological effectiveness, RBE (or compound biological effectiveness, CBE, for boron dose). However, this method cannot consider the dose dependence of RBE and the synergetic effect of each dose component. Thus, the use of photon isoeffective dose was proposed instead of the RBE-weighted dose. This sample input file (smk_bnct/phits.inp) can output both the RBE-weighted dose and the photon isoeffective dose using [anatally]. The calculation procedures are given as below:
Execute PHITS with smk_bnct/phits.inp -> Four dose components of BNCT are outputted in photon.out, hydro.out, nitro.out, and boron.out (see recommendation/bnct in more detail).
Set icntl = 17 in the input file and execute PHITS again with the revised input file -> The RBE-weighted doses are outputted in RBEdose.out, using the weighted-sum mode (c99 = 0).
Disable the 1st [anatally] and enable the 2nd [anatally] using off command, and execute PHITS again with the revised input file -> The photon-isoeffective doses are outputted in IsoEdose.out, using the FFT-SMK mode (c99=1).
Step 2 is omissible if you are interested only in calculating the photon isoeffective dose. The relative error is simply obtained from the uncertainty propagation rule for independent variables, i.e., the four dose components are assumed to be independent from one another. However, this assumption is not true except for the photon dose component, and thus, the actual uncertainties are expected to be larger than the values obtained from this program.
The followings are the user-defined constants used in this program.
c99: Model selection parameter. RBE-weighted dose (=0) or photon isoeffective dose (=1,2,3). For calculating the photon isoeffective dose, three models can be selected, which are the Fast Fourier Transform (FFT)-based SMK (=1), the Taylor Expansion (TE)-based SMK2 (=2), and z*-based MK model (=3). The TE-based SMK model was developed in National Institute of Radiological Sciences (NIRS), QST, for reducing the computational time of the original SMK model in order to implement it in the treatment planning system of active scanning carbon-ion therapy in HIMAC. The FFT-based SMK model is another improved SMK model with shorter computational time. The z*-based MK model considers the saturation correction due to the overkill effect by introducing the z* parameter, but ignores the stochastic nature of cell nucleus dose.
c1-c4: RBE or CBE value for each dose component. They are effective only for the RBE-weighted dose calculation mode (c99=0).
c11, c21, c31, c41, c51: zd in Gy for photon, hydrogen, nitrogen, boron (extracellular), boron (intracellular) doses. Their default values are 2.06, 51.5, 49.2, 185.0, and 185.0, respectively.
c12, c22, c32, c42, c52: z* in Gy for photon, hydrogen, nitrogen, boron (extracellular), boron (intracellular) doses. Their default values are the same as those for zd.
c13, c23, c33, c43, c53: zn in Gy for photon, hydrogen, nitrogen, boron (extracellular), boron (intracellular) doses. Their default values are 0.00265, 0.29, 0.38, 1.33, and 1.33, respectively
c44, c54: Microscopic dose correction factor, κextra and κintra. Their default values are 0.0908 and 0.693, respectively, which are calculated from microdosimetric simulation for BPA.
c90: Normalization constant that converts the relative dose (Gy/source) to the absolute dose (Gy). If a negative value is specified, the 1st tally result is automatically normalized to its absolute value. The default value is 1.0. It is not necessary to define this parameter when the tally results have already normalized to their absolute value using totfact.
c91: The α0 parameter used in the SMK model in Gy-1. Its default value is 0.0422.
c92: The β0 parameter used in the SMK model in Gy-2. Its default value is 0.00822.
c93: The α parameter for the reference treatment in Gy-1. Its default value is 0.0633.
c94: The β parameter for the reference treatment in Gy-2. Its default value is 0.00822 in the same as c92.
c95: The fraction size (dose per fraction) of the reference treatment in Gy. Its default value is 1000, and the value over 100 indicates the one-time irradiation.
c96: The standard deviation of the Gaussian distribution for expressing the intracellular heterogeneity of 10B compounds. Its default value is 0, indicating that the 10B compounds are homogeneously distributed to all cells.
c97: The dose rate coefficient γ0 in h-1. Its default value is 4.33.
c98: Irradiation time in hour. Its default value is 0, which means that the dose rate effect is not considered in the calculation.
The default values of the most parameters were evaluated from the least-square fitting of the cell surviving fractions of SCC VII murine squamous cell carcinomas obtained from in vivo/in vitro experiments of tumor-bearing mice treated by BNCT. The parameters zd, z*, zn defined by c11-c43 are the dose-mean specific energy in domain, saturation-corrected specific energy, dose-mean specific energy in cell nucleus, respectively, which can be evaluated by the cellular scale microdosimetric simulation (see nucleus_dose folder).
Biological dose calculation mode for charged particle therapy: "smk_ion"
The therapeutic and side effects of charged particle therapy are generally estimated from the biological doses, which is the product of the absorbed dose and RBE. PHITS can calculate the biological dose directly using [t-deposit] coupled with the default usrdfn2.f on the basis of the conventional MK model. However, this method cannot consider the dose dependence of RBE because the absolute value of the doses at each tally point cannot be determined until the PHITS simulation is finished. In contrast, the biological doses obtained from this sample input file (smk_ion/phits.inp) are calculated based on the SMK model with the dose-dependent RBE. The calculation procedure is given as below:
Copy usranatal.f, usrdfn1.f, usrdfn2.f, and usrdfn3.f in smk_ion/src folder to the PHITS source folder, and recompile PHITS
Execute the re-compiled PHITS with smk_ion/phits.inp -> The absorbed dose and dose-weighted zd, z*, and zn are outputted in dose.out, zd.out, zs.out, and zn.out, respectively.
Set icntl = 17 in the input file and execute re-compiled PHITS again with the revised input file -> The biological doses are outputted in EQDX.out.
EQDX denotes the Equi-effective dose for fraction size X, which represents the absorbed dose to give the same biological effect of the reference treatment, e.g. fractionated X-ray therapy. The relative error of the calculated biological dose is simply assumed to be the same as that of the absorbed dose because it is very difficult to evaluate the uncertainty of RBE.
The user-defined constants of c81-c83, c90-c95, and c97-c99 are used in this sample. The meaning of each parameter after c90 is the same as that for "smk_bnct", but the default values of some parameters are different because they were evaluated based on the surviving fractions of HSG cells irradiated with various heavy ions. The parameters c81-c83 are used in the particle transport simulation (icntl = 0) with usrdfn1-3.f. The followings are the meaning and default value of each parameter.
c81: The radius of domain, rd, used in the SMK model in μm. Its default value is 0.274.
c82: The radius of domain, rn, used in the SMK model in μm. Its default value is 6.20.
c83: The saturation parameter z0 in Gy, or y0 in keV/μm in the case of negative value. Its default value is 89.0.
c90: Normalization constant that converts the relative dose (Gy/source) to the absolute dose (Gy). If a negative value is specified, the 1st tally result is automatically normalized to its absolute value. The default value is 1.0. It is not necessary to define this parameter when the tally results have already normalized to their absolute value using totfact.
c91: The α0 parameter used in the SMK model in Gy-1. Its default value is 0.156.
c92: The β0 parameter used in the SMK model in Gy-2. Its default value is 0.0607.
c93: The α parameter for the reference treatment in Gy-1. Its default value is0.313.
c94: The β parameter for the reference treatment in Gy-2. Its default value is 0.0607 in the same as c92.
c95: The fraction size (dose per fraction) of the reference treatment in Gy. Its default value is 1000, and the value over 100 indicates the one-time irradiation.
c97: The dose rate coefficient γ0 in h-1. Its default value is 4.33.
c98: Irradiation time in hour. Its default value is 0, which means that the dose rate effect is not considered in the calculation.
c99: Model selection parameter. The default model is the FFT-SMK model (=1).
EQDX calculation mode for targeted alpha therapy: "smk_tat"
Targeted alpha therapy (TAT) is gaining grounds as a novel treatment for refractory cancer. Recently, we developed a model for calculating equi-effective dose to X-ray therapy with fraction size X, so-called EQDX, using RT-PHITS. Basic calculation procedures for converting the absorbed dose to EQDX for TAT are almost the same as those for BNCT, though there are only two dose components, α and β doses, in TAT instead of four in BNCT. This mode is originally designated to be used in tandem with RT-PHITS because the biological decay constant database (decaybio.out) generated by RT-PHTIS is indispensable in the calculation. However, phits.inp included in smk_tat folder can be used as a standalone input because it generates decaybio.out by itself using a dummy [t-deposit] tally. The calculation procedure is given as below:
Copy usranatal.f in smk_tat/src folder to the PHITS source folder, and recompile PHITS
Execute either pre-compiled or re-compiled PHITS with smk_tat/phits.inp -> α and β dose components of TAT are outputted in deposit_alpha.out and deposit_beta.out, respectively.
Set icntl = 17 in the input file and execute re-compiled PHITS with the revised input file -> The EQDX are outputted in EQDX.out, using the FFT-SMK mode (c99=1).
If you would like to calculate EQDX using PET/CT data, please see the Appendix in phits/utility/RTphits/phits-lec-RTphits-jp.pptx.
The meanings of each user-defined parameters are similar to those for "smk_bnct", but the default values of some parameters are different because they were evaluated based on the surviving fractions of HSG cells irradiated with various heavy ions. Their descriptions are as follows:
c11, c21, c31: zd in Gy for β dose, α dose (extracellular), and α dose (intracellular), respectively. Their default values are 2.90, 92.2, and 92.2, respectively.
c12, c22, c32: z* in Gy for β dose, α dose (extracellular), and α dose (intracellular), respectively. Their default values are 2.90, 47.4, and 47.4, respectively.
c13, c23, c33: zn in Gy for β dose, α dose (extracellular), and α dose (intracellular), respectively. Their default values are 1.45e-4, 0.191, and 0.191, respectively.
c24, c34: Microscopic dose correction factor, κextra and κintra. Their default values are 0.440 and 0.554, respectively, which are calculated under assumption of homogeneously distributed 211At in all cell compartments.
c90: Normalization constant that converts the relative dose (Gy/source) to the absolute dose (Gy). If a negative value is specified, the 1st tally result is automatically normalized to its absolute value. The default value is 1.0. It is not necessary to define this parameter when the tally results have already normalized to their absolute value using totfact.
c91: The α0 parameter used in the SMK model in Gy-1. Its default value is 0.156.
c92: The β0 parameter used in the SMK model in Gy-2. Its default value is 0.0607.
c93: The α parameter for the reference treatment in Gy-1. Its default value is 0.313.
c94: The β parameter for the reference treatment in Gy-2. Its default value is 0.0607 in the same as c92.
c95: The fraction size (dose per fraction) of the reference treatment in Gy. Its default value is 1000, and the value over 100 indicates the one-time irradiation.
c96: The standard deviation of the Gaussian distribution for expressing the intracellular heterogeneity of RI. Its default value is 0, indicating that RI are homogeneously distributed to all cells.
c97: The dose rate coefficient μ or γ0 in h-1. Its default value is 1.5.
c98: Half-life of RI in h. The sum of the physical and biological half-life should be provided. Its default value is 7.214, which is the physical half-life for 211At. Note that the meaning of this parameter is completely different from that in the case of BNCT.
c99: Model selection parameter. The default model is the FFT-SMK model (=1).
RBE-weighted dose calculation mode for tissue reaction using MK model: "mk_tissue"
Estimation of RBE-weighted dose for tissue reactions is important for the purposes of not only medical physics but also radiological protection. This sample enables to calculate the RBE-weighted dose for tissue reactions using an improved version of the MK model. The calculation procedure is given as below:
Copy usranatal.f and usrdfn2.f in mk_tissue/src folder to the PHITS source folder, and recompile PHITS
Execute the re-compiled PHITS with mk_tissue/phits.inp -> The absorbed dose and dose-weighted z* are outputted in dose.out and zs.out, respectively.
Set icntl = 17 in the input file and execute re-compiled PHITS again with the revised input file -> The RBE-weighted dose is outputted in RBEdose.out.
The relative error of the calculated RBE-weighted dose is simply assumed to be the same as that of the absorbed dose. For evaluating the uncertainties of the calculated RBE, you have to change the domain radius and z* values, and perform Step 2 & 3 again. Please read Ref. 10 in more detail.
The user-defined constants of c81, c83, c90-c93, and c99 are used in this sample. The parameters c81 and c83 are used in the particle transport simulation (icntl = 0) with usrdfn2.f. The followings are the meaning and default value of each parameter.
c81: The radius of domain, rd, used in the MK model in μm. Its default value is 0.1886.
c83: The saturation parameter z0 in Gy, or y0 in keV/μm in the case of negative value. Its default value is -100, i.e., 100 keV/μm.
c90: Normalization constant that converts the relative dose (Gy/source) to the absolute dose (Gy). If a negative value is specified, the 1st tally result is automatically normalized to its absolute value. The default value is 1.0. It is not necessary to define this parameter when the tally results have already normalized to their absolute value using totfact.
c91: Saturation corrected specific energy for the reference radiation, z*ref, in Gy. Its default value is 3.512.
c92: Saturation corrected specific energy for typical clinical radiation field, z*c, in Gy. Its default value is 3.401
c93: The α/β ratio of the tissue reaction evaluated from the clinical data, (α/β)c, in Gy. Its default value is 10.0.
c94: The threshold dose level for changing the LQ to linear functions for expressing the dose response of the reference radiation, Dt, in Gy. Its default value is 7.0.
c99: Model selection parameter. So far, only one option (=1) is available.
Dose-mean LET calculation mode: "LETd"
In principle, dose-mean LET can be estimated from the result of [t-let] by calculating their LET-weighted mean value. However, this method is rather difficult because it requires to develop a user's own program for analyzing the tally result. Thus, we provide a sample usranatally program for easily determining the dose-mean LET by calculating the ratio of dose-weighted LET and dose. The calculation procedure is given as below:
Copy usranatal.f and usrdfn1.f in LETd/src folder to the PHITS source folder, and recompile PHITS
Execute the re-compiled PHITS with LETd/phits.inp -> The absorbed dose and dose-weighted LET are outputted in dose.out and doseLET.out, respectively.
Set icntl = 17 in the input file and execute re-compiled PHITS again with the revised input file -> The dose-mean LET are outputted in LETd.out.
END_BASIC_TEXT

FILE: readme-jpn.docx
BEGIN_BASIC_TEXT
ユーザー定義anatallyの使い方
ユーザー定義anatallyとは、1つもしくは複数のタリー結果にusranatal.fで書かれた演算処理を行って新たなタリー結果を出力する機能です。解析するタリー結果は、同じ物理量である必要はありませんが、メッシュ数は等しい必要があります。演算可能なのは、それぞれのファイルの同じメッシュに相当する値のみで、異なるメッシュの値を参照することはできません。また、再開始計算時のタリー条件同一チェックオプションは外しておく必要があります(ireschk=1)。以下、usranatal.fで使うパラメータの一覧です。
jmax: 解析するタリーファイル数([anatally]のnfileで指定)
rdata(2,jmax): 各タリー結果及びその相対誤差。1つ目の引数は、タリー数値(=1)及びその相対誤差(=2)を表します。
answer: 演算処理後の値(sfileで指定したファイルにタリー値として書き出されます)
rerr: 演算処理後の誤差(sfileで指定したファイルの相対誤差として書き出されます)
cval: インプットファイルで定義したc1-c99。複数回定義された場合は、インプットの最後で定義された値が有効となります。
usranatal.fには、既定プログラムとして、ユーザー定義定数に従って各タリー値を重み付けして加算するモードと、確率論的マイクロドジメトリ(SMK)モデル,,に従ってBNCTにおける光子等効果線量を計算するモードが組み込まれています。2つのモードはc99パラメータで使い分けることができ、それぞれのサンプルがweighted_sum及びsmk_bnctフォルダにあります。また、PHITSの再コンパイルが必要となりますが、粒子線治療及び標的α線核医学治療の生物学的線量をSMKモデルに従って計算するサンプルプログラムがsmk_ion及びsmk_tatフォルダに、線量平均LETを計算するサンプルプログラムがLETdフォルダにそれぞれ格納されています。以下、各サンプルの説明です。
加重加算モード(weighted_sum)
加重加算モードは、c99[0]もしくは定義しない場合に動作します。通常のPHITS計算(icntl=0)により炭素線治療の全吸収線量(dose_all.out)及び1次イオンによる吸収線量(dose_primary.out)を計算し、anatally機能(icntl=17)でそれらを差し引くことにより2次粒子の吸収線量(dose_secondary.out)を出力するサンプルです。c1[1.0], c2[-1.0]とすることにより、全吸収線量Dallに1.0を乗じ、1次イオンによる吸収線量Dpriに-1.0を乗じて足し合わせるため、結果としてDall - Dpri = Dsec(2次粒子による吸収線量)が算出されます。ただし、誤差は、単純に2つの独立変数の誤差伝播により計算しているため、このサンプルのように独立変数でない2つの変数(Dallの一部がDpri)を加算する場合は正しく値とならないことにご注意ください。
ホウ素中性子捕捉療法(BNCT)の光子等効果線量計算モード(smk_bnct)
BNCTの治療効果は、4つの線量成分(ホウ素・窒素・水素・光子線量)にそれぞれの生物学的効果比(Relative Biological Effectiveness, RBE、もしくはホウ素線量に対してはCompound Biological Effectiveness, CBE)を乗じて導出するRBE加重線量(等価線量)を使うのが一般的です。しかし、この手法だと、CBEやRBEの線量依存性や異なる線量成分間での相乗効果を考慮できない問題があります。そこで、それらを考慮可能な光子等効果線量(Photon isoeffective dose)の利用が提案されています。本サンプルプログラムでは、RBE加重線量及び確率的マイクロドジメトリモデルに基づく光子等効果線量を計算することができます。以下、その流れです。
smk_bnctに含まれるphits.inpをそのまま実行 -> BNCT線量4成分(photon.out, hydro.out, nitro.out, boron.out)が出力されます(詳細はrecommendation/bnctも参照)。
icntl=17としてanatallyモードで実行 -> 加重加算モード(c99 = 0)でanatallyが実行され、RBE加重線量がRBEdose.outに出力されます。
1つ目の[anatally]をoffにし、2つ目の[anatally]のoffを削除して実行 -> 光子等効果線量計算モード(c99 = 1)でanatallyが実行され、光子等効果線量がIsoEdose.outに出力されます。
光子等効果線量のみ求めたい場合は、ステップ2は省略可能です。相対誤差は、どちらのモードでも単純に各線量成分の相対誤差の誤差伝播で計算しており、各成分が独立変数でないことから正しい値とならないことにご注意下さい。
このサンプルで用いるユーザー定義定数を以下に示します。
c99: モデル選択パラメータ。0の場合はRBE加重線量、1以上の場合は光子等効果線量を計算します。光子等効果線量の計算モデルは、高速フーリエ変換SMK(=1)、テイラー展開SMK(=2)2、z*-based MK(=3)から選択可能です。テイラー展開SMKモデルは、利便性に欠ける従来型SMKモデルを臨床現場で応用するために放射線医学総合研究所で開発されたモデルで、現在、HIMACのActive Scanning手法の治療計画に利用されています。テイラー展開を導入することにより、従来型SMKモデルで計算コストの掛かる畳み込み積分を簡略化しています。z*-based MKモデルは、細胞核線量の分散を考慮しない古いタイプのMKモデルです。
c1-c4: RBE及びCBE値(RBE加重線量計算モードのみで有効)。
c11, c21, c31, c41, c51: 光子、水素、窒素、ホウ素(細胞外)、ホウ素(細胞内)線量に対するzd (Gy)。デフォルトは2.06, 51.5, 49.2, 185.0, & 185.0。ホウ素(細胞外)とホウ素(細胞内)は基本的に同じ値ですが、異なる値を指定することも可能。
c12, c22, c32, c42, c52: 光子、水素、窒素、ホウ素(細胞外)、ホウ素(細胞内)線量に対するz* (Gy)。デフォルトはzdと同じ値。ホウ素(細胞外)とホウ素(細胞内)は基本的に同じ値ですが、異なる値を指定することも可能。
c13, c23, c33, c43, c53: 光子、水素、窒素、ホウ素(細胞外)、ホウ素(細胞内)線量に対するzn (Gy)。デフォルトは0.00265, 0.29, 0.38, 1.33, & 1.33。ホウ素(細胞外)とホウ素(細胞内)は基本的に同じ値ですが、異なる値を指定することも可能。
c44, c54: 微視的線量補正係数(microscopic dose correction factor), κextra & κintra。デフォルトは0.0908 & 0.693(BPAに対応)。
c90: 規格化定数。dose.outに出力された吸収線量の相対値(Gy/source)にこの値を乗じて絶対値(Gy)に変換します。負値を定義した場合は、最初のメッシュに対する線量がc90の絶対値となるように規格化定数を自動調整します。デフォルトは1.0で、totfactで既に線量を絶対値に規格化している場合は、定義する必要はありません。
c91: SMKモデルで使うα0(Gy-1)。デフォルトは0.0422
c92: SMKモデルで使うβ0(Gy-2)。デフォルトは0.00822
c93: 基準放射線治療に対するα(Gy-1)。デフォルトは0.0633
c94: 基準放射線治療に対するβ(Gy-2)。デフォルトはc92と同じ0.00822
c95: 基準放射線治療の分割照射線量(Fraction size, Gy)。100 以上は1回照射と見なし、デフォルト値は1000。
c96: 細胞間薬剤不均一性を表すガウス分布の標準偏差σ。デフォルトは0、すなわち細胞間不均一性を考慮しない。
c97: 線量率係数γ0(h-1)。デフォルトは4.33。
c98: 照射時間(h)。デフォルトは0(h)、すなわち線量率効果を考慮しない。
各パラメータのデフォルト値は、基本的に担がんマウス(SCC VII squamous cell carcinomas)に対するBNCT照射実験により得られた細胞生存率より推定した値です3。c11~c43で定義するzd, z*, znは、それぞれdose-mean specific energy in domain, saturation-corrected specific energy, dose-mean specific energy in cell nucleusを表し、別の細胞に対する光子等効果線量を計算するためには、nucleus_doseフォルダを参考にユーザー自身で細胞スケールのマイクロドジメトリ計算を実施する必要があります。
粒子線治療の生物学的線量計算モード(smk_ion)
粒子線治療の治療効果は、吸収線量にRBEを乗じて計算した生物学的線量により推定します。PHITSでは、[t-deposit]でusrdfn=2とすることにより生物学的線量を直接計算することが可能ですが、その手法では、計算中に線量の絶対値が分からないためRBEの線量依存性は無視されます。anatally機能を使えば、線量の絶対値が特定できるため、RBEの線量依存性を考慮可能なSMKモデルにより生物学的線量を計算可能となります。以下、その計算の流れです。
smk_ion/srcに含まれるusranatal.f, usrdfn1.f, usrdfn2.f, usrdfn3.fをPHITSのsrcフォルダにコピーしてPHITSを再コンパイル
再コンパイルしたPHITSでsmk_ion/phits.inpを実行(dose.out, zd.out, zs.out, zn.outが出力されます)
phits.inpのicntlを0から17に変更して、再コンパイルしたPHITSで実行(生物学的線量の計算結果がEQDX.outに出力されます)。EQDX(Equi-effective dose for fraction size X)とは、ICRUが提案した基準放射線治療の分割数やα/β比を明確に示した生物学的線量です。
dose.outは吸収線量の相対値、zd.out, zs.out, zn.outは、それぞれ線量加重zd, z*, znの計算値が出力されており、usranatal.fでそれらの値を組み合わせて生物学的線量を計算します。相対誤差に関しては、SMKモデルに起因する誤差を導出することができないため、吸収線量の相対誤差と同じと仮定しています。
このサンプルで用いるユーザー定義定数はc81~c83、c90~c95及びc97~c99で、c90以降はBNCTの場合と同じ意味を持ちます。ただし、そのデフォルト値は、HSG細胞に対する様々な重イオン照射実験で得られた細胞生存率より推定した値で、BNCTの場合とは異なります。また、c81~c83は、通常の粒子輸送モード(icntl=0)で有効となるパラメータで、usrdfn1~3.fの中で利用します。以下、各パラメータの意味とデフォルト値を示します。
c81: ドメイン半径rd(μm)。デフォルトは0.274
c82: 細胞核半径rn(μm)。デフォルトは6.2
c83: Saturation parameter z0(Gy)。負値を入力した場合はy0(keV/μm)。デフォルトは89
c90: 規格化定数。dose.outに出力された吸収線量の相対値(Gy/source)にこの値を乗じて絶対値(Gy)に変換します。負値を定義した場合は、最初のメッシュに対する線量がc90の絶対値となるように規格化定数を自動調整します。デフォルトは1.0で、PET測定の線量を推定したい場合は、既に規格化されていますので変更する必要はありません。
c91: SMKモデルで使うα0(Gy-1)。デフォルトは0.156
c92: SMKモデルで使うβ0(Gy-2)。デフォルトは0.0607
c93: 基準放射線治療に対するα(Gy-1)。デフォルトは0.313
c94: 基準放射線治療に対するβ(Gy-2)。デフォルトはc92と同じ0.0607
c95: 基準放射線治療の分割照射線量(Fraction size, Gy)。100 以上は1回照射と見なし、デフォルト値は1000。
c97: 線量率係数γ0(h-1)。デフォルトは4.33。
c98: 照射時間(h)。デフォルトは0(h)、すなわち線量率効果を考慮しない。
c99: モデル選択パラメータ。デフォルトはFFT-SMK(=1)。
標的α線核医学治療の生物学的線量計算モード(smk_tat)
標的α線核医学治療(Targeted Alpha Therapy, 通称TAT)は、がん細胞に集まる性質を持つ薬剤に225Acや211Atなどのα核種を標識し、そこから放出されるα線でがん細胞を殺傷する手法です。α線は、高いRBEを持つため、BNCTや粒子線治療と同じくそのRBEを考慮した生物学的線量評価が必要となります。その基本的な計算手法は、BNCTに対する生物学的線量評価手法と同じですが、BNCTがホウ素・窒素・水素・光子線量の4成分あるのに対して、TATはα線とβ線(陽電子の寄与含む)線量の2成分しかありません。また、RT-PHITと連動して使うことを想定しており、RT-PHITSで出力される生物学的崩壊定数(decaybio.out)も必要とします。ただし、このサンプルでは、単純化するためdecaybio.outは全て0となるようにダミーの[t-deposit]で出力するようにしています。以下、その計算の流れです。
smk_tat/srcに含まれるusranatal.fをPHITSのsrcフォルダにコピーしてPHITSを再コンパイル
smk_tat/phits.inpをPHITS(通常版、コンパイル版どちらでも可)で実行(α線線量deposit-alpha.outやβ線線量deposit-beta.outが出力されます)。
phits.inpのicntlを0から17に変更して、再コンパイルしたPHITSで実行(生物学的線量の計算結果がEQDX.outに出力されます)。
RT-PHITSと連動させた計算方法に関しては、phits/utility/RTphits/phits-lec-RTphits-jp.pptxのAppendixや文献を参照ください。
このサンプルで用いるパラメータは、基本的にはBNCTに対するユーザー定義anatallyと同じ意味を持ちます。ただし、そのデフォルト値は、HSG細胞に対する様々な重イオン照射実験で得られた細胞生存率より推定した値で、BNCTの場合とは異なります。以下、各パラメータの意味とそのデフォルト値を示します。
c99: モデル選択パラメータ。
c11, c21, c31: β線、α線(細胞外)、α線(細胞内)線量に対するzd (Gy)。デフォルトは2.90, 92.2, & 92.2。細胞外と細胞内のα線線量に対するzdは基本的に同じ値ですが、異なる値を指定することも可能。
c12, c22, c32: β線、α線(細胞外)、α線(細胞内)線量に対するz*(Gy)。デフォルトは2.90, 47.4, & 47.4。細胞外と細胞内のα線線量に対するz*は基本的に同じ値ですが、異なる値を指定することも可能。
c13, c23, c33: β線、α線(細胞外)、α線(細胞内)線量に対するzn (Gy)。デフォルトは1.45e-4, 0.191, & 0.191。細胞外と細胞内のα線線量に対するznは基本的に同じ値ですが、異なる値を指定することも可能。
c24, c34: 微視的線量補正係数(microscopic dose correction factor), κextra & κintra。デフォルトは0.440 & 0.554(211Atが細胞内に均一に分布すると仮定して計算)。
c90: 規格化定数。dose.outに出力された吸収線量の相対値(Gy/source)にこの値を乗じて絶対値(Gy)に変換します。負値を定義した場合は、最初のメッシュに対する線量がc90の絶対値となるように規格化定数を自動調整します。デフォルトは1.0で、PET測定の線量を推定したい場合は、既に規格化されていますので変更する必要はありません。
c91: SMKモデルで使うα0(Gy-1)。デフォルトは0.156
c92: SMKモデルで使うβ0(Gy-2)。デフォルトは0.0607
c93: 基準放射線治療に対するα(Gy-1)。デフォルトは0.313
c94: 基準放射線治療に対するβ(Gy-2)。デフォルトはc92と同じ0.0607
c95: 基準放射線治療の分割照射線量(Fraction size, Gy)。100 以上は1回照射と見なし、デフォルト値は1000。
c96: 細胞間薬剤不均一性を表すガウス分布の標準偏差σ。デフォルトは0、すなわち細胞間不均一性を考慮しない。
c97: 線量率係数μもしくはγ0(h-1)。デフォルトは1.5。
c98: RIの半減期(h)。生物学的半減期も含めて入力する必要があります。デフォルトは7.214(211Atに対する物理半減期)。この変数のみBNCTの場合と意味合いが異なりますのでご注意ください。
c99: モデル選択パラメータ。デフォルトはFFT-SMK(=1)。
組織反応に対するRBE加重線量計算モード(mk_tissue)
改良型MKモデルに基づいて推定した組織応答に対するRBE加重線量を計算します。サンプルとして、皮膚に対する平均RBEを推定するパラメータが設定されています。以下、その計算の流れです。
mk_tissue/srcに含まれるusranatal.f, usrdfn2.fをPHITSのsrcフォルダにコピーしてPHITSを再コンパイル
再コンパイルしたPHITSでmk_tissue/phits.inpを実行(dose.out, zs.outが出力されます)
phits.inpのicntlを0から17に変更して、再コンパイルしたPHITSで実行(RBE加重線量の計算結果がRBEdose.outに出力されます)。
dose.outは吸収線量の相対値、zs.outは線量で重み付けしたz*が出力されており、usranatal.fでそれらの値を組み合わせてRBE加重線量を計算します。相対誤差に関しては、RBEの誤差を無視して吸収線量の相対誤差と同じと仮定しています。RBEの誤差範囲は、ドメインサイズを変更することにより推定可能です(詳細は文献10を参照)。
このサンプルで用いるユーザー定義定数はc81, c83、c90~c94及びc99です。このうち、c81, c83は、通常の粒子輸送モード(icntl=0)で有効となるパラメータで、usrdfn2.fの中で利用します。以下、各パラメータの意味とデフォルト値を示します。
c81: ドメイン半径rd(μm)。デフォルトは0.1886
c83: Saturation parameter z0(Gy)。負値を入力した場合はy0(keV/μm)。デフォルトは-100(すなわち100 keV/μm)
c90: 規格化定数。dose.outに出力された吸収線量の相対値(Gy/source)にこの値を乗じて絶対値(Gy)に変換します。負値を定義した場合は、最初のメッシュに対する線量がc90の絶対値となるように規格化定数を自動調整します。デフォルトは1.0で、totfactで既に線量を絶対値に規格化している場合は、定義する必要はありません。。
c91: 基準放射線に対するz*ref (Gy)。デフォルトは3.512
c92: 治療用放射線に対するz*c (Gy)。デフォルトは3.401
c93: 治療用放射線に対する(α/β)c (Gy)。デフォルトは10.0
c94: 基準放射線の線量応答関数がLQモデルから線型モデルに切り替わる線量Dt (Gy)。デフォルトは7.0。
c99: モデル選択パラメータ。現在のところ1のみ選択可能
線量平均LET計算モード(LETd)
線量平均LETは、原理的には[t-let]で計算した線量分布をLETで加重して平均することにより計算可能です。しかし、この手法は、自作プログラム等により[t-let]の結果を解析する必要があり、容易ではありません。そこで、[t-deposit]のユーザー定義関数でLET加重付与エネルギーを計算し、通常の[t-deposit]で計算した付与エネルギーで除することにより、線量平均LETを計算するユーザー定義anatallyを作成しました。以下、その流れです。
LETd/srcに含まれるusranatal.f及びusrdfn1.fをPHITSのsrcフォルダにコピーしてPHITSを再コンパイル
再コンパイルしたPHITSでLETd/phits.inpを実行(dose.out, doseLET.outが出力されます)
phits.inpのicntlを0から17に変更して、再コンパイルしたPHITSで実行(線量平均LETがLETd.outに出力されます)。
なお、本usranatally.fは、単純に1つ目と2つ目のタリーの比を計算するようプログラミングされていますので、線量平均LETの計算のみならず、2つのタリー結果の比を出力したい場合にそのまま利用することができます。
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: LETd/phits.inp
FILE: mk_tissue/phits.inp
FILE: smk_bnct/nucleus_dose/phits.inp
FILE: smk_bnct/nucleus_dose/region.inp
FILE: smk_bnct/phits.inp
FILE: smk_ion/phits.inp
FILE: smk_tat/phits.inp
FILE: weighted_sum/phits.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: LETd/src/usranatal.f90
FILE: LETd/src/usrdfn1.f90
FILE: mk_tissue/src/usranatal.f90
FILE: mk_tissue/src/usrdfn2.f90
FILE: smk_bnct/nucleus_dose/nucleus_dose.f90
FILE: smk_bnct/nucleus_dose/readme.txt
FILE: smk_ion/src/usranatal.f90
FILE: smk_ion/src/usrdfn1.f90
FILE: smk_ion/src/usrdfn2.f90
FILE: smk_ion/src/usrdfn3.f90
FILE: smk_tat/src/usranatal.f90
