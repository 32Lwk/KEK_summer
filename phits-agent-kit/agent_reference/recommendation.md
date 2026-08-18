# Recommendation — input catalog

These are PHITS input examples under `recommendation/` in the PHITS
root. This is a catalog only — **read the actual `.inp` files
directly from that folder**; they are not duplicated here.

## Overview (English)

Recommendations of Parameter Setting in PHITS Input Files
Followings are the examples of PHITS input files with recommended parameter setting for each simulation. Each file is contained in its folder, together with its output files.
List
BNCT:　Recommended setting for boron neutron capture therapy
CosmicRay:　Recommended setting for cosmic-ray transport analysis
DCHAIN: Recommended setting for using [t-chain]
DetectorResponse: Recommended setting for detector response calculation
Fusion: Recommended setting for fusion facility shielding
H10multiplier: Sample setting for calculating doses using Multiplier & [t-deposit]
Light: Example of light emission and transport ([Light] section)
muon: Recommended setting for muon transport analysis
NeutronSource: Sample setting for accelerator-based neutron source calculation
NuclearReaction: Sample setting for nuclear reaction cross section calculation
ParticleTherapy: Recommended setting for dose estimation of particle therapy
PhotonTherapy: Recommended setting for dose estimation of X-ray therapy
SemiConductor: Recommended setting for soft-error rate calculation
Shielding: Recommended setting for shielding calculation
TrackStructure: Recommended setting for track structure mode
XrayDiagnostic: Recommended setting for dose estimation of X-ray diagnostic
Update information
2026/7/3: Revised all input files to use predefined materials as much as possible. Also moved counter.inp to sample/misc.
2026/3/23 “light” is added.
2025/10/30 NuclearReaction.inp has been simplified and modified to use [forced collision]. The previous version has been moved to sample/misc/DDX_calculation.
2025/3/11 In “BNCT”, [t-deposit] with mother parameter is adopted for calculating the BNCT four dose components, instead of [t-track] with multiplier.
2022/12/16 In “cosmic-ray” and “muon”, a new option negs = 2 was introduced to transport high-energy electrons, positrons, and photons.
2022/3/10 In shielding and NeutronSource, JENDL-4.0/HE is adopted to simulate proton- and neutron-induced reactions up to 200 MeV. Consequently, jendlHE folder is deleted.
2021/3/22 We added a new sample setting for accelerator-based neutron source calculation (NeutronSource).
2019/10/30 Definition of file(1)=c:/phits was removed from all input files because file(1) is automatically read from the environmental variable PHITSPATH, which is automatically set by the PHITS installer.
2019/6/9 We added a new recommendation setting for medical physics simulation of boron neutron capture therapy (BNCT).
2019/3/14 We added a new recommendation setting to use a high-energy nuclear data library JENDL-4.0/HE.
2018/3/7 From ver. 3.05, a function to calculate the deposition energy using Kerma approximation, which used to be implemented only in [t-heat], became available in [t-deposit]. Then, we recommend to use [t-deposit] instead of [t-heat] in all situations of deposition energy calculations, and deleted/replaced [t-heat] tallies in h10multiplier.inp and XrayDiagnostic.inp.
2018/2/16 Trackstructure.inp was revised to calculate the probability density of ionizations and electronic excitations in certain regions by adding a new tally [t-interact].
2018/1/30 From ver. 3.03, the dose calculation method using predefined [multiplier] sections became available. “H10multiplier” was revised so as to use the new method. It was also revised to consider [weight window] with mesh = xyz, which became also available from ver. 3.03.
2017/8/4 We added a new recommendation setting for cosmic-ray simulation. [magnetic field] was introduced in “Counter” setting. [importance] was introduced in “Shielding” setting.
2016/6/10 From version 2.93, “file(1)” is introduced to specify PHITS installation folder name. When you properly set this parameter, you do not have to specify the name of other input files i.e. “file(7, 20, 21, 24, and 25)” unless you have changed the folder structure of PHITS. In addition, “emin” and “dmax” generally need not to be specified after this version, owing to the introduction of “nucdata” as well as the change of the default value of “negs”. Thus, [parameters] sections for all input files are revised.
2016/6/9　We added a new recommendation setting for track-structure simulation.
2016/12/16 We added a new recommendation setting for medical physics particularly for X-ray diagnostic.
2016/08/18 Owing to the implementation of “natural” parameter, the definition of elements in [material] section were revised.
2015/09/02 EGS5 is not used in neutron and photon transport simulations, i.e. shielding.inp, h10multiplier.inp, and fusion.inp
2015/3/12 We added a new recommendation setting for muon transport.
2015/3/10 In version 2.76, we introduce ascat1 and ascat2 parameters to adjust the magnitude of angular straggling calculated by Lynch’s equation (nspred = 2). Consequently, we recommend to use nspred = 2 in ParticleTherapy.inp. In addition, letmat for each tally is changed to -5, where negative letmat indicates that dE/dx of electron is automatically estimated from the databased developed based on the SRIM calculation for 1 g/cm3 water.
2015/1/29 In version 2.74, we recommend to use EGS5 (negs = 1) instead of the PHITS original algorithm for transporting electrons, positrons and photons for all recommendation settings. Consequently, you need to specify fil(20) parameter. On the other hand, you do not have to specify “file(14)” parameter after version 2.74, because the gamma de-excitation data contained in “trxcrd.dat” was incorporated in the source files of PHITS.
2014/9/26　Event generator mode version 2 is recommended (e-mode = 2) to be used for event-generator calculation.
2014/8/29　In version 2.70, we incorporated the photon, electron and positron transport algorithm of EGS5, and you can use EGS5 by setting negs = 1 as shown in PHITS-EGS5.inp. The function to consider the detector resolution was implemented in [t-deposit] tally, as shown in DetectorResponse.inp. We added a new recommendation setting for nuclear fusion reactor calculation.
2013/8/21 In version 2.60, we improved the algorithm for de-excitation of nucleus after the evaporation process by implementing EBITEM (ENSDF-Based Isomeric Transition and isomEr production Model). In reply to this improvement, “igamma” parameter in several recommendation settings was changed.
2012/12/17 In version 2.52, we improved the photon and electron transport algorithm. Thus, emin(12) and emin(13) were set to 100 keV. You can also decrease the value down to 1 keV, but if you set such low cut-off energies, the computational time becomes very long. A sample input for [t-dchain], which is used for generating input files of DCHAIN-SP, was added.
2012/9/24 Default values of some parameters were changed in PHITS 2.50. For example, the default model for describing nucleon-nucleus interaction was switched to INCL, and cut-off energies for deuteron, triton, He-3, alpha and nucleus were set to 1.0. Thus, some recommendation settings were revised. Please use PHITS 2.50 (or later) coupled with the latest data libraries for running these input files. Note that electron-atomic data library, which is included in PHITS package only after version 2.50, is utilized in several recommendations setting ‘emin(12)=1.0’.
2012/8/10 We changed the recommended cut-off energy of electron and positron i.e. emin(12) and emin(13) from 1 keV to 1 MeV, since we found bug in their transport algorithm. The sample inputs for ‘SimpleGEO’ are moved to ‘Tool’ section.
Description of each input file
1. DetectorResponse.inp
A sample input file for calculating the detector responses for the isotropic irradiation. The detailed descriptions of some important parameters are given below:
e-mode in [parameters]: You have to activate the event-generator mode when you would like to obtain the event-by-event information such as the response function of a detector.
dir in [source]: You have to set “dir = iso” instead of “dir = -all” for simulating the isotropic source using the event-generator mode. The source particle flux inside the sphere with the radius of c3 should be pi*(c3)2.
dresol, dfano: Parameters for representing detector resolution introduced after ver. 2.70. When you set dresol=σr and dfano=F, the deposition-energy E of each event is fluctuated by following the Gaussian with standard deviation sqrt(σr 2 + FE).
dedxfnc = 1: Consider Birk’s law using [multiplier], which expresses the response of detector as a function of LET in keV/um. c900 is assigned to specify the multiplier ID in the case of dedxfnc = 1.
2. Shielding.inp
A sample input file for radiation shielding calculation. The high-energy nuclear data library JENDL-4.0/HE [1] is adopted in the transport of neutrons and protons up to 200 MeV. You do not have to activate the event-generator mode, since event-by-event information is generally not requested in the shielding calculation. Radiation doses are directly calculated from the flux of neutrons and photons multiplied with the pre-installed fluence-to-effective-dose conversion coefficients for AP irradiation geometry, using “multiplier” function in the [t-track] tally. You can reduce the computational time of shielding calculation by appropriately setting [importance] or [weight window] section. See lecture/advanced/weightA & weightB in more detail. Note that JENDL-4.0/HE only for several nuclei are included in the PHITS package, and those for other nuclei can be downloaded from the JAEA website [2].
References
Matsuda et al. Prog. Nucl. Sci. Technol. 6, 225-229 (2019).
https://rpg.jaea.go.jp/main/en/ACE-J40HE/index.html
3. ParticleTherapy.inp
A sample input file for simulating charged-particle therapy. Using this input file, you can calculate the spatial distributions of dose and dose-equivalent, and probability densities of LET and lineal energy y. The detailed descriptions of some important parameters are given below:
e-mode in [parameters]: You have to activate the event-generator mode when you use the [t-let] or [t-sed] tallies.
nedisp in [parameters]: In order to calculate the depth-dose distribution precisely, you have to consider the energy straggling of charged particle.
nspred in [parameters]: In order to calculate the lateral divergence of doses from the beam axis, you have to consider the angular straggling of charged particle. For nspred = 2, you can adjust the magnitude of scattering angle by changing ascat1 and ascat2 parameters.
dedxfnc in [t-deposit]: The [t-deposit] tallies with dedxfnc = 0 and 1 give the absorbed dose and dose equivalent, respectively, where the dose equivalent can be obtained from the absorbed dose multiplied with the Q(L) relationship defined in ICRP60.
letmat: Negative value for letmat indicates that dE/dx of electron is automatically estimated from the databased developed based on the SRIM calculation for 1 g/cm3 water. If the material specified by letmat is not used in the [cell] section, its absolute density will be taken from the value defined in the [material] section. For example, if you define water as H 2 O 1, it will correspond to extremely heavy water. Instead, please define it as, for example, H -0.1118983441 O -0.8881016559.
4. PhotonTherapy.inp
A sample input file for calculating the spatial distribution of doses in xyz-mesh for photon therapy. 20 MeV electrons are irradiated into W target to generate X-rays, and dose and track-length distributions are calculated inside W target and a phantom composed of ICRU soft tissue. The detailed descriptions of some important parameters are given below:
ipnint in [parameters]: High-energy photons can induce the giant dipole resonance, and produce neutrons. In this sample, the giant dipole resonance is considered, though the contributions of neutron to the energy deposition are generally not so large.
5. SemiConductor.inp
A sample input file for calculating the probability density of deposit energy in microscopic sites such as semi-conductor devices. The detailed descriptions of some important parameters are given below:
esmin: In order to calculate the deposit energy in microscopic site, you have to decrease the “esmin” parameter, which specifies the minimum energy for range calculation in PHITS.
e-mode: You have to activate the event-generator mode when you would like to obtain the event-by-event information such as the probability density of deposit energy.
[ Delta Ray ]: You have to consider the production of knock-out electrons so-called “-rays” when you would like to estimate the deposit energy in microscopic sites. In this sample, the -rays with energies above 0.01 MeV generated in the target region (reg = 1) are explicitly transported in the PHITS simulation.
6. NuclearReaction.inp
This is a sample input file for calculating double-differential nuclear reaction cross sections (DDX). A particle of interest is irradiated onto a thin-foil target, and the resulting secondary particles are tallied with [t-product] and converted to units of mb/MeV/sr for output. To improve computational efficiency, [forced collision] is enabled. Parameters related to nuclear reactions are explicitly specified so that various reaction models can be tested.
7. H10multiplier.inp
There are 3 methods for calculating ‘dose’ in PHITS, and this input file was made for describing the difference of them. The followings are the description of the 3 methods.
[t-track]: In this tally, dose is calculated from the particle fluence at a certain location multiplied with the dose conversion coefficients defined in [multiplier] section. The 3 dose conversion coefficients are used, which are H*(10) defined in this input file, and H*(10) and the effective dose for AP irradiation predefined in data/multiplier folder.
[t-deposit]: In this tally, dose is calculated from the ionization of charged particles as well as the Kerma approximation of neutral particles. Stopping powers and Kerma factors depend on the material density, and thus, there is a gap between doses in concrete and air regions.
8. Counter.inp
A sample input file for using [counter] section. It calculates the event-by-event deposition energy distributions inside NaI scintillator located behind Al radiator. In the calculation, the contribution from primary particles that did not cause nuclear interaction in the Al radiator “primary.out” is separated by those from secondary particles that were generated in the radiator “secondary.out”, using [counter] section. This function is very useful for analyzing the systematic uncertainties in your experiments.
9. dchain.inp
A sample input file for connecting calculation between PHITS and DCHAIN-SP, using [t-dchain]. Please see readme-eng.pdf in the folder in detail.
10. fusion.inp
A sample input file for nuclear-fusion related calculation. Only neutrons and photons are transported. In general, nuclear-fusion facilities are very large, and the [importance] section is specified in this input file.
11. muon.inp
A sample input file for the muon transport calculation. In this sample, terrestrial muon fluxes at ground level are reproduced, using the cosmic-ray source mode. High-energy muons can generate a lot of high-energy photons and electrons, and thus, it is recommended to use high-energy EGS mode (negs = 2) and activate photonuclear reaction (ipnint = 1).
12. XrayDiagnostic
A sample input file for the use of medical physics particularly for X-ray diagnostic. Low-energy photons (approximately below 1 MeV) cannot generate secondary electrons with long ranges, and thus transport of electron and positron is not necessary to be considered in low-energy photon simulation except when extremely high spatial resolution is required such as microdosimetric simulation. The transport of neutrons is also not necessary to be considered because only high-energy photon can induce photon-nuclear reaction Thus, “nucdata” is set to 0. For calculating the absorbed dose due to low-energy photon irradiation, Kerma approximation is more suitable than directly transporting electrons. Thus, the EGS5 mode should not be activated for the calculation because the algorithm of EGS5 is not suit for Kerma approximation.
13. TrackStructure
A sample input file for the use of track-structure simulation. Using the track structure mode, PHITS can analyze ionization, excitation, and oscillation induced by electrons and positrons event-by-event. Currently, the cross sections only for liquid water are prepared in PHITS, and those for other materials are simply scaled based on their electron density. Track-structure simulation takes so long time that we cannot recommend to activate this mode in a conventional-scale particle transport simulation (~cm orders). The followings are the important parameters for this mode.
etsmax, etsmin in [parameters]: Maximum and minimum energies of particles simulated by track structure mode. You can set 'etsmin = 0', but we do not recommend the setting because computational time becomes extremely long. You have to set etsmax > 1.0 keV. We recommend to set this parameter below 1 MeV, otherwise the computational time becomes extremely long.
emin(12-13) in [parameters]: For the track structure mode, emin(12) and emin(13) should be set to 1.0e-3, and EGS5 should be activated (negs=1).
[trackstrucutre]: In this section, you have to specify the cells where you would like to perform track-structure simulation. “mID” represents the index of the cross section database used in the track-structure simulation, and currently you can select only 0 (no track structure simulation) or 1 (track structure simulation using liquid water cross section database). We are planning to prepare the cross section databases for other materials in future.
angel = cmum in [t-deposit]: You can change the unit of length scale from cm to μm using ANGEL parameter “cmum”. You can also change the scale unit to nm by “cmnm”, to mm by “cmmm”, to meter by “cmmt”, to km by “cmkm”.
14. CosmicRay
A sample input file for cosmic-ray transport simulation. In this sample, proton and iron ion fluxes of galactic cosmic-rays are reproduced, using the cosmic-ray source mode. The followings are the important parameters for this mode.
mdbatima and maxbnk: Extremely high-energy protons and heavy ions exist in space, and such high-energy particles can produce a large number of secondary particles by successively inducing nuclear reactions. Thus, default values of “mdbatima” and “maxbnk” might be too small, which are the maximum database size of ATIMA and the maximum banking memory size for secondary particle information, respectively. Thus, they are increased in this input file.
e-mode: The dose equivalent based on the Q(L) relationship is frequently evaluated for cosmic-ray dosimetry, and thus, the event generator mode is activated (e-mode=2).
irqmd: The accuracy for simulating nucleus-nucleus interaction is very important for cosmic-ray transport simulation, and thus, JQMD2.0 is used instead of its original version (irqmd=1).
iMeVperU: In general, cosmic-ray fluxes are calculated in the unit of /(MeV/u)/cm2/s, and thus, iMeVperU is set to 1.
negs = 2: High energy cosmic-rays occasionally generate electrons, positrons and photons with energy above 1 GeV. Thus, their dmax should be extended up to 10 TeV by setting negs = 2.
16. BNCT
A sample input file for medical physical simulation of boron neutron capture therapy (BNCT). In this input, the absorbed doses from 4 dose components (boron, hydrogen, nitrogen and photon) are separately calculated using the Kerma approximation. More detailed instruction can be found in /phits/lecture/therapy/bnct. The followings are the important parameters used in this input file.
e-mode and irescheck in [parameters]: Event generator mode should not be used because it is not necessary to transport secondary charged particles generated by neutrons. “irescheck” should be 1 when icntl = 17.
c1 – c5: Mass fractions of H, C, N, O, and 10B. This sample input assumes ICRU soft tissue with 10 ppm of 10B.
c10 – c15: Atomic density (1024 atom/g) calculated from c1 – c5. These parameters are used in multiplier subsection in [t-track]
mset1 in [t-track]: Boron, hydrogen, and nitrogen doses can be calculated by not [t-deposit] but [t-track] with the multiplier subsection. The format of mset is
(normalization_factor  material_ID_for_kerma_factor  -5  -6) or
(normalization_factor  material_ID_for_kerma_factor  1  -4)
The last two numbers “-5 -6” and “1 -4” indicate that the weighting factors should be photon and neutron kerma factors, respectively. The kerma factor is normalized to give absorbed dose in MeV when the atomic density is 1 x 1024 atom/cm3 and the flux is 1/cm2. Thus, if you would like to estimate the dose in Gy, you have to set the normalization_factor to the product of 1.602e-10 (c9) and the atomic density of the material in 1024 atom/g. Please see manual “5.24.1 Multiplier subsection” in more detail.
[anatally]: This section is activated only when icntl = 17. RBE-weighted doses are calculated from the four dose components multiplied with their RBE or CBE factors. Please see /phits/utility/usranatal/smk_bnct in more detail.
17. NeutronSource
A sample input file for accelerator-based neutron source using activation cross section data. In this simulation, a 100MoO3 sample is irradiated by produced neutrons from the 9Be(d,n) reaction, and yield of 99Mo by 100Mo(n,2n)99Mo is estimated using activation cross section data. The high-energy nuclear data library JENDL-4.0/HE is adopted in the transport of not only for neutrons and protons but also deuteron [3] up to 200 MeV. The yield of 99Mo in the sample can be estimated by the multiplication of neutron energy spectra and an excitation function of activation cross sections. In the sample input, the excitation function of 100Mo(n,2n)99Mo is given as a multiplier set. PHITS calculates the neutron spectra in the sample by [t-track] tally, and then multiplies the spectra by the excitation function using multiplier. The 99Mo yield estimated by this method is output in “yield-99Mo_multiplier.out”.
References
[3] S. Nakayama, O. Iwamoto, Y. Watanabe, and K. Ogata, "JENDL/DEU-2020: deuteron nuclear data library for design studies of accelerator-based neutron sources", J. Nucl. Sci. Technol. 58, 805-821 (2020), DOI:10.1080/00223131.2020.1870010.
18. Light
A sample input file for light generation and transport. Light is produced when a particle travels faster than the speed of light in the material (Cherenkov light), when a charged particle deposits its energy in the material (scintillation light), and when light is absorbed and re-emitted. Therefore, it is recommended to specify negs and e-mode; otherwise, light emission via charged particles may be ignored.

## Overview (Japanese)

PHITS奨励設定ファイル
「マニュアルを読んでも自分が必要とする計算でどのようなパラメータを設定して良いかわからない」という質問が多数ありましたので，いくつか代表的な問題に関して，その奨励設定ファイルを作成しました。各インプットファイルは，その名前を付けたフォルダの中に，そのアウトプットとともに格納されています。
一覧
BNCT:　ホウ素中性子捕捉療法の線量評価用の奨励設定
CosmicRay:　宇宙線挙動解析用の奨励設定
DCHAIN: PHITS-DCHAIN接続計算用の奨励設定
DetectorResponse: 検出器応答関数計算用の奨励設定
Fusion: 核融合施設の設計計算の奨励設定
H10multiplier: Multiplierや[t-deposit]などを使った線量計算手法の例題
light: 光の発生と輸送（[Light] セクション）の例題
muon: ミューオン挙動解析用の奨励設定
NeutronSource: 加速器中性子源の例題
NuclearReaction: 核反応断面積計算の例題
ParticleTherapy: 粒子線治療線量評価用の奨励設定
PhotonTherapy: X線治療線量評価用の奨励設定
SemiConductor: 半導体ソフトエラー計算用の奨励設定
Shielding: 遮蔽計算用の奨励設定
TrackStructure: 飛跡構造解析モードを使う場合の奨励設定
XrayDiagnostic: 診断用X線挙動解析用の奨励設定
更新履歴
2026/7/3 既定物質をできるだけ使うように全ての入力ファイルを修正。また、counter.inpをsample/miscに移動
2026/3/23 lightを追加。
2025/10/30 nuclearreactionの入力ファイルを単純化して、[forced collision]を使うように変更しました。従来の入力ファイルはsample/misc/DDX_calculationに移動しました。
2025/3/11 BNCTの線量４成分を[t-track]のmultiplierではなく[t-deposit]のmotherパラメータを使って計算するように変更しました。
2022/12/16 Cosmic-ray, muonでnegs=2（高エネルギーオプション）を使うようにしました。これに伴い、dmax(12-14)の定義は削除しました。
2022/3/10 shielding, NeutronSourceでJENDL-4.0/HEを使うようにしました。また、これに伴いjendlHEフォルダは削除しました。
2021/3/22　加速器中性子源の例題（NeutronSource）を追加しました。
2019/10/30 環境変数PHITSPATHからfile(1)を読み込むようにしたため，全てのインプットからfile(1)=c:/phitsの指定を削除しました。
2019/6/9　BNCT医学物理計算用の奨励設定（BNCT）を追加しました。
2019/3/14 Version 3.10より，一部の核種に対して高エネルギー核データライブラリJENDL-4.0/HEが使えるようになりましたので，その奨励設定(jendlHE)を追加しました。
2018/3/7 Version 3.05より，従来は[t-heat]でしか行えなかったカーマ近似による付与エネルギー計算機能を[t-deposit]にも追加しました。この改良により，付与エネルギー計算は全て[t-deposit]で行えるようになりましたので，[t-heat]を利用していたインプット(h10multiplier, XrayDiagnostic)から[t-heat]を削除しました。
2018/2/16 Trackstructureに[t-interact]を加えて，ある領域内に起きる電離や励起イベントの頻度分布を計算するようにしました。
2018/1/30　内蔵の線量換算係数を使って線量計算する手法が変更されましたので，新しい手法に対応するようh10multiplierを変更しました。また，ver.3.03より導入したmesh = xyzに対する[weight window]を使うように設定しました。
2017/8/4　宇宙線挙動解析に対する奨励設定CosmicRayを追加しました。奨励設定Counterで磁場を考慮するようにしました。奨励設定Shieldingに[importance]セクションを追加しました。
2017/6/10 Version 2.93よりfile(1)でPHITSインストールフォルダを指定することにより，それ以外の入力ファイルfile(7,20,21,24,25)を指定する必要がなくなりました。これに合わせて全ての奨励設定を変更しました。また，nucdataパラメータの導入やnegsのデフォルト値の変更により，特殊な場合を除いてeminやdmaxを指定する必要がなくなりました。
2017/6/9　飛跡構造解析モードに対する奨励設定TrackStrucutreを追加しました。
2016/12/16　診断系の医学物理応用のサンプルとしてXrayDiagnosticを追加しました。カーマ近似が成立する低エネルギー光子のみの挙動解析を効率よく行うための設定になっています。
2016/8/18 天然元素を自動展開する機能を組み込んだため，[material]セクションの指定方法を変更しました。
2015/9/2 Fusion, H10multiplier, Shieldingなど巨大な体系の中性子・光子輸送をメインとする計算では，計算時間短縮のためEGS5を使わないようにしました（EGS5を使うと，電子まで輸送するので計算時間が掛かってしまうため）
2015/3/12 PHITS2.76よりミューオンの核反応及び捕獲反応を模擬できるようになったため，ミューオン輸送計算用の奨励設定ファイルmuonを追加した。
2015/3/10 particletherapyに荷電粒子の角度分散を調整するパラメータascat1とascat2を導入した。これに伴い，nspredの奨励値を1（オリジナルモデル）から2（Lynchの式）に変更した。また，水に対するLETをより正確に計算するため，各タリーのletmatパラメータを-5とした（負値の場合，電子のdE/dxはSRIMで計算した1g/cm3の水に対する値を使うようになる）。
2015/1/29 電子・光子の輸送計算にEGS5を使うことを奨励するようにした（negs=1パラメータの導入）。これに伴い，file(20)の指定が必要となりました。また，γ脱励起に関するデータベース”trxcrd.dat”をソースファイルに組み込みましたので，file(14)の指定が不要となりました。
2014/9/26 イベントジェネレータモードを使う場合の奨励設定値を2とした(e-mode=1からe-mode=2へ変更）。
2014/8/29 核融合用の奨励設定ファイルfusionを追加。DetectorResponseで検出器の分解能を考慮するdresolとdfanoパラメータを導入。negsパラメータを導入し，PHITS-EGS5を最新版で実行できるようにした。
2013/8/21 Version2.60で新しい脱励起モデルEBITEMを導入したことにより，いくつかの奨励設定ファイルのigammaパラメータを変更しました。
2012/12/17 Version2.52では，電子輸送計算アルゴリズムを改訂したので，電子のカットオフエネルギーを低くしても正しい計算結果が得られるようになりました。ただし，電子のカットオフエネルギーを低くしすぎると，計算時間が膨大になるため，極めて高い空間分解能が要求されるsemiconductor.inpを除いて100keVとしています。また，DCHAIN-SPとの接続計算を解説したdchain.inpを追加しました。
2012/9/21　Version2.50では，計算を高精度化・高速化するため，いくつかのデフォルトパラメータを変更しました。大きな変更ポイントは，核子に対する初期核反応モデルをBertiniモデルからINCLに変更した点と，重イオン（重陽子やα粒子含む）に対するカットオフエネルギーを109MeVから1MeVに引き下げた点です。これに合わせて，いくつかの奨励設定のパラメータも変更しました。したがって，これらのファイルを実行する際は，必ずPHITS2.50（もしくは，より新しいversion）をご使用ください。なお，電子輸送を行う計算には，以前のversionでは付録されていなかった電子-原子相互作用断面積ライブラリが必要になりますのでご注意ください。
2012/8/10　電子輸送のバグがあったため，電子輸送を行う奨励設定のカットオフエネルギーを1 keVから1 MeVに変更しました。SimpleGEOの奨励設定を「ツール」の方に移動しました。
各奨励設定の解説
1. DetectorResponse.inp
シンチレータなど，放射線検出器の応答関数を計算するための奨励設定ファイルです。以下，重要なパラメータの説明です。
e-mode in [parameters]：検出器の応答関数計算では，イベント毎の情報が必要となる場合が多いので，イベントジェネレータモード(e-mode=2)に設定しています。
dir in [source]：イベントジェネレータモードで等方照射線源を再現するためには，dirを”-all”ではなく”iso”に設定する必要があります。その際，半径c3の球内における平均入射粒子フラックスは，π*(c3)2となります。
dresol, dfano：実際の検出器はエネルギー分解能を持ち，dresol及び dfanoは，その分解能を表すパラメータです。dresol=σr, dfano=Fの場合，付与エネルギーEのイベントは標準偏差が√（σr 2 + FE）のガウス分布に従って分散されます。
dedxfnc = 1: Birksの式で計算した応答関数R(L)を考慮することができます。応答関数は、LET (keV/um)の関数として[multiplier]セクションで与え、c900にそのmultiplier ID（-200～-299まで利用可能）を指定する必要があります。
2. Shielding.inp
遮へい計算用の奨励設定ファイルです。イベント毎の情報は必要ありませんので，イベントジェネレータモードで計算する必要はありません。また、高エネルギー加速器の遮蔽設計には、高エネルギー核データライブラリJENDL-4.0/HE[1]の利用を奨励しています。PHITSパッケージには限られた核種に対するライブラリしか含まれておりませんので、warningが多数出力されます。足りない核種に対しては、下記ホームページ[2]よりダウンロード可能ですので、必要に応じてダウンロードしてその情報をxsdir.jndに追加してください。中性子及び光子のフラックスに内蔵の線量換算係数を乗じて実効線量を導出するため，電子の輸送は必要ありません。したがって，negsはデフォルト値から変更していません（光子のみ輸送）。また[importance]や[weight window]セクションを導入することにより，遮へい体後方における線量も比較的短時間で計算できるようになります。詳しくはlecture\advanced\weightA及びweightBをご参照下さい。
参考文献
Matsuda et al. Prog. Nucl. Sci. Technol. 6, 225-229 (2019).
https://rpg.jaea.go.jp/main/en/ACE-J40HE/index.html
3. ParticleTherapy.inp
粒子線治療時の吸収線量や線量当量の空間分布(r-z mesh)，及びLETやyの確率密度分布を計算するための奨励設定ファイルです。[t-sed]タリーは，比較的計算時間が掛かりますので，y分布の情報が不要な方は，offにして下さい。以下，重要なパラメータの説明です。
e-mode in [parameters]：[t-LET]や[t-SED]タリーを行うためには，イベントジェネレータモード(e-mode=1 or 2)に設定する必要があります。
nedisp in [parameters]：粒子線治療におけるブラッグピークの深さを正確に計算するためには，阻止能（dE/dx）の確率的な分散(Energy straggling)を考慮する必要があります。
nspred in [parameters]：粒子線治療における線量のビーム中心から横方向への空間的な拡がりを正確に計算するためには，その角度分散(Angular straggling)を考慮する必要があります。nspred=2の場合は，角度分散の大きさをascat1とascat2で調整することができます。
dedxfnc in [t-deposit]：dedxfnc=0の場合は，計算したdeposit energyをそのまま出力し，dedxfnc=1の場合は，計算したdeposit energyをICRP60で定義されたQ(L)関係で重み付けして出力します。したがって，1つ目の[t-deposit]タリーでは吸収線量を，2つ目の[t-deposit]タリーでは線量当量を計算します。
letmat: この値が負の場合は，電子に対するdE/dxは，SRIMで計算した1g/cm3の水に対する値を自動的に使うようになります。また，letmatで指定した物質を[cell]セクションで使わない場合、その絶対値は[material]セクションで定義された値となるのでご注意ください。例えば、H 2 O 1と定義すると極めて重い水となってしまいますので、H -0.1118983441 O -0.8881016559のように定義してください。
4. PhotonTherapy.inp
光子線治療時の吸収線量の空間分布(xyz-mesh)を計算するための奨励設定ファイルです。20MeV の電子Linacを想定し，WターゲットでX線を発生させ，下流側にある組織等価物質内での吸収線量を計算しています。以下，重要なパラメータの説明です。
ipnint in [parameters]: 約7MeV以上の光子は，原子核と巨大共鳴を引き起こして中性子を発生します。中性子による吸収線量への寄与はそれほど大きくありませんが，奨励設定では，中性子の発生を考慮するようipnint=1としています。
電子の輸送が必須ですのでnegs = 1としています。
5. SemiConductor.inp
半導体のソフトエラー発生率評価など，微少空間における付与エネルギーを計算する奨励設定ファイルです。以下，重要なパラメータの説明です。
esmin in [parameters]：微少空間における荷電粒子の挙動を正確に計算するためには，荷電粒子の飛程を計算する最小エネルギー（esmin）を小さく設定する必要があります。
e-mode in [parameters]：微少空間における付与エネルギー計算にはカーマ近似は使えませんので，イベントジェネレータモード(e-mode=1 or 2)に設定する必要があります。
[ Delta Ray ]セクション：微少空間における付与エネルギーを正確に計算するためには，ノックアウト電子（δ線）発生による荷電粒子飛跡周辺のエネルギー付与の空間的な拡がりを考慮する必要があります。この例では，ターゲット領域（reg=1）で発生する0.01MeV以上のδ線の挙動を解析します。
6. NuclearReaction.inp
二重微分核反応断面積（DDX）を計算するサンプルインプットファイルです。断面積を計算したい粒子を薄膜ターゲットに照射して，そこで発生する2次粒子を[t-product]タリーして単位をmb/MeV/srに変換して出力します。計算を効率化するために[forced collision]を設定しています。様々な核反応モデルをテストできるよう，核反応に関連するパラメータを明示的に指定しています。
7. H10multiplier.inp
PHITSには，３つの線量計算方法があり，その違いを明確にするために作った奨励設定ファイルです。[t-wwg]で作った[Weight Window]を使うサンプルにもなっています。以下，各方法の説明です。
[t-track]セクション：計算したフルエンスに[Multiplier]セクションで定義した線量換算係数を乗じて周辺線量当量H*(10)を導出します。また，data/multiplierフォルダ内に含まれる換算係数を使ってH*(10)(k=-200)と実効線量(k=-201)も同時に計算します。この手法で計算した線量は，フルエンスのみに依存しますので，コンクリート・空気間で差はほとんどありません。
[t-deposit]セクション：荷電粒子の電離損失と，中性子・光子のKermaファクターを用いて領域内の付与エネルギーを計算します。Kermaファクターは，物質の密度に大きく依存するので，コンクリート・空気間で線量に大きなギャップが見られます。
9. dchain.inp
[t-dchain]を使ったPHITSとDCHAIN-SPのつなぎ計算のための設定ファイルです。詳細は，フォルダ内に含まれるreadme-jpn.pdfをご参照下さい。
10. fusion.inp
核融合に関連する計算のための奨励設定ファイル。計算時間短縮のため，電子・陽電子は輸送しない設定になっています。また，核融合施設での計算は，体系が大きい場合が多いので分散低減法（[importance]セクション）を利用しています。
11 muon.inp
ミューオンの輸送を計算するための奨励設定ファイルです。宇宙線線源モードを使って、地表面におけるミューオンのエネルギー・角度分布を再現しています。高エネルギーミューオンを輸送すると高エネルギー光子や電子が発生しますので、高エネルギーEGSモードの利用(negs = 2)と光核反応の考慮(ipnint = 1)を奨励しています。また、大量の2次粒子を発生する場合がありますので、2次粒子情報を保存するメモリサイズ（maxbnk）を大きくしています。
12. XrayDiagnostic.inp
低エネルギー光子を使った診断系の医学物理応用サンプルです。レントゲン写真のように，低エネルギー光子を組織等価物質に照射し，その中に含まれている金属（アルミ，鉄）を検知しています。低エネルギー光子（おおよそ1MeV以下）は，2次電子の飛程が短いため，電子の輸送を行わなくても精度の高い計算が可能です（ただし，細胞レベルのシミュレーションなど極めて高い空間分解能が必要になる場合を除く）。また，光核反応も起きないため，中性子の輸送も必要ありません（nucdata=0）。低エネルギー光子による吸収線量を計算するには，計算時間の観点から，カーマ近似を使って光子によるエネルギー付与を計算するPHITS従来アルゴリズム（negs = -1，デフォルト）を使っています。PHITS従来アルゴリズムは，電子・陽電子に対する計算精度に問題がありますが，光子に対しては十分に高い精度を有します。
13. TrackStructure.inp
飛跡構造解析用のサンプルです。飛跡構造解析モードを使えば，熱化するまでに電子・陽電子が引き起こす電離・励起・振動などの個々のイベントを正確に模擬することができます。ただし，断面積は水に対する値のみ整備されており，それ以外の物質に対しては，単純に電子密度で断面積をスケーリングします。また，従来アルゴリズムと比較して計算時間が膨大に掛かりますので，通常の大きさの体系（cmオーダー）における放射線挙動解析には適しません。以下、重要なパラメータの説明です。
etsmax, etsmin in [parameters]：飛跡構造解析を実施する電子（もしくは陽電子）のエネルギーの上限・下限値です。etsminは，原理的には0でも設定可能ですが，計算時間が膨大になりますので，特に熱化した電子の挙動などを解析したい場合を除いて1eV程度に設定することをお勧めします。etsmaxは，1keVよりも大きく設定する必要があります。原理的には極めて大きい値も設定可能ですが計算時間が膨大になりますので，現実的には1MeV以下に設定することをお勧めします。
emin(12-13) in [parameters]：飛跡構造解析の場合は，必ずEGS5モードを用いて1keVまで電子輸送を行う必要があります。
[trackstructure]：飛跡構造解析を行うセルを指定します。mIDは，利用する断面積データのID番号で，今のところは0（=飛跡構造解析を行わない）か1（＝液体の水）しか指定できません。今後，様々な物質に対する断面積データを順次整備していく予定です。
angel = cmum in [t-deposit]：ANGELでプロットする軸スケールをcmからμmに変換するパラメータです。飛跡構造解析モードでは，小さい領域に対する空間分布を出力する場合が多いので，あらかじめ軸スケールを調整しておくと便利です。なお，cmumはcm to umを意味し，これ以外にcmnm (cm to nm), cmmm (cm to mm), cmmt (cm to m), cmkm(cm to km)が使えます。
14. CosmicRay
宇宙線挙動解析用のサンプルです。このサンプルでは、宇宙空間における銀河宇宙線（ただし、陽子及び鉄イオンのみ）を模擬しています。以下、重要なパラメータです。
mdbatima, maxbnk: 宇宙線には，極めてエネルギーの高い陽子や重イオンが含まれるため，核反応により大量の2次粒子が発生する場合があります。そのような場合，ATIMAが作るデータベースの数(mdbatima)や2次粒子の情報を記憶するメモリ容量(maxbnk)がデフォルト値では足りなくなる可能性がありますので，それらのパラメータを大きくしています。e-mode: 宇宙放射線防護ではQ(L)関係に基づく線量当量を計算する必要があるため，中性子核反応による2次粒子の特定が不可欠となります。したがって，e-mode=2としてイベントジェネレータモードを使用しています。
irqmd: 宇宙線挙動解析では重イオン核反応モデルの計算精度が重要になりますので，irqmd=1として最新版JQMD（version 2.0）を使用しています。
iMeVperU: 宇宙線フラックスはMeV/u単位で評価する場合が多いのでiMeVperU=1としてタリーの単位をMeVからMeV/uに変換しています。
negs=2: 高エネルギー宇宙線が引き起こす核反応により1GeV以上の電子・陽電子・光子が生成される可能性がありますので、EGSの高エネルギーモードを使用しています。
16. BNCT
BNCT医学物理計算用の奨励設定です。BNCTでは，ホウ素線量，窒素線量，水素線量，光子線量を区別して求めることが要求されるため，[t-track]のmultiplier subsectionを使ってそれぞれの寄与に分けて線量を導出するよう設定されています。また、一度、icntl = 17として[anatally]セクションを有効にすることにより、RBE加重線量を計算できます。以下、重要なパラメータの説明です。
e-mode & irescheck in [parameters]：カーマ近似を用いて線量計算を行うため、e-modeを定義する必要はありません。irescheck = 1は、icntl = 17とした際に必須となります。
c1 – c5：線量を計算したい領域の水素、炭素、窒素、酸素、10Bの重量比を定義します。このサンプルでは、ICRU soft tissueに10ppmの10Bを加えています。
c10 – c15：上記、重量比から計算した原子数密度1024(atom/g)です。Multiplier subsectionで利用します。
[material]：m2001-2003は体系中では使用しませんが，[t-track]でこれらの物質に対するカーマファクターを使って線量計算するために定義が必要です。
mset1 in [t-track]：[t-track]で計算したフルエンスにカーマファクターを乗じて積分することにより、光子線量、水素線量，窒素線量、ホウ素線量をそれぞれ計算します。mset内のパラメータは
(規格化定数　カーマファクターを参照する物質番号 -5 -6)
(規格化定数　カーマファクターを参照する物質番号 1 -4)
となります。最後の-5 -6及び1 -4は，光子及び中性子のカーマファクターを使う際のおまじないと思ってください（詳細はマニュアル5.21.1を参照）。カーマファクターは，対象物質密度が1 x 1024 atom/cm3，フラックスが1/cm2だった場合にMeV単位で出力するよう規格化されていますので，それをGyに変換するためには，規格化定数を1.602e-10 (c9) x 対象物質の元素密度(1024 atom/g) に設定する必要があります。なお，msetの中で数式に括弧は利用できませんのでご注意ください。
[anatally]：計算した各線量コンポーネントからRBE加重線量を計算するためのセクションです。詳しくは/phits/utility/usranatal/smk_bnctをご参照ください。
anatally start, anatally end：このコメントがあるタリーをベースに[anatally]の出力フォーマットが決定されます。
17. NeutronSource
加速器中性子源のサンプルインプットです。陽子、中性子の核反応にはJENDL-4.0/HE、重陽子の核反応にはJENDL/DEU-2020[3]を利用するように設定しています。また、99Moの生成量は（中性子スペクトル）×（放射化断面積）により計算できます。[t-track]によりサンプル中の中性子スペクトルを求め、その結果にmultiplierに登録した放射化断面積の励起関数を掛けることで放射化量を計算しています。サンプルインプットの励起関数は、JENDL-4.0（20 MeV以下）とJENDL-4.0/HE（20 から200 MeV）の値です。この方法で計算した結果は” yield-99Mo_multiplier.out”に出力されます。
参考文献
S. Nakayama, O. Iwamoto, Y. Watanabe, and K. Ogata, "JENDL/DEU-2020: deuteron nuclear data library for design studies of accelerator-based neutron sources", J. Nucl. Sci. Technol. 58, 805-821 (2020), DOI:10.1080/00223131.2020.1870010.
18. Light
光生成および光輸送のためのサンプル入力ファイルです。光は、粒子が物質中でその媒質中の光速を超えて進むとき（チェレンコフ光）、荷電粒子が物質中にエネルギーを付与するとき（シンチレーション光）、および吸収された光が再放出されるときに生成されます。したがって、negs および e-mode の設定を推奨します。これらを指定しない場合、荷電粒子による光の発生が無視されることがあります。

## Files

### BNCT
- `recommendation/BNCT/BNCT.inp` — PURPOSE: Sample input for BNCT calculation | KEYWORDS: T-Deposit

### CosmicRay
- `recommendation/CosmicRay/CosmicRay.inp` — PURPOSE: Sample input file for cosmic-ray transport simulation | KEYWORDS: T-Deposit, T-Track

### Counter
- `recommendation/Counter/Counter.inp` — PURPOSE: Sample input using [ Counter ] section for distinguishing primary and secondary particles in the estimate of detector response | KEYWORDS: Counter, Transform, Magnetic Field, T-Deposit, T-Track

### DCHAIN
- `recommendation/DCHAIN/dchain.inp` — PURPOSE: sample input for dchain: 150MeV proton into water | KEYWORDS: Volume, Mat Name Color, T-DCHAIN, T-Track

### DetectorResponse
- `recommendation/DetectorResponse/DetectorResponse.inp` — PURPOSE: Sample input for detector response calculation using isotropic source | KEYWORDS: T-Deposit

### Fusion
- `recommendation/Fusion/Fusion.inp` — PURPOSE: Sample input for radiation shielding | KEYWORDS: Importance, T-Track

### H10multiplier
- `recommendation/H10multiplier/H10multiplier.inp` — PURPOSE: Sample input for calculating H*(10) using [Multiplier] section | KEYWORDS: T-Track, T-Deposit

### Light
- `recommendation/Light/Light.inp` — PURPOSE: Count Cherenkov photons generated in optical glass that reflect inside the glass and reach the photocathode. Tally outputs: - product.out Emission spectrum of optical photons - cross.out Spectrum crossing the photocathode through the PMT window - cross_with_Multiplier.out Result weighted by quantum efficiency via Multiplier | KEYWORDS: Light, T-Product, T-Cross, Multiplier, T-Track

### NeutronSource
- `recommendation/NeutronSource/NeutronSource.inp` — PURPOSE: Sample input for accelerator-based neutron source | KEYWORDS: Forced Collisions, T-Cross, T-Track, Multiplier

### NuclearReaction
- `recommendation/NuclearReaction/NuclearReaction.inp` — PURPOSE: Sample input for calculating double differential cross section | KEYWORDS: Forced Collisions, T-Product, T-Track

### ParticleTherapy
- `recommendation/ParticleTherapy/ParticleTherapy.inp` — PURPOSE: Sample input for dose calculation for charged particle therapy | KEYWORDS: T-Deposit, T-LET, T-SED

### PhotonTherapy
- `recommendation/PhotonTherapy/PhotonTherapy.inp` — PURPOSE: Sample input for dose calculation for photon therapy | KEYWORDS: T-Deposit, T-Track

### SemiConductor
- `recommendation/SemiConductor/SemiConductor.inp` — PURPOSE: Sample input for calculating deposition energy distribution in semi-conductor device | KEYWORDS: Volume, Delta Ray, T-Deposit

### Shielding
- `recommendation/Shielding/Shielding.inp` — PURPOSE: Sample input for radiation shielding | KEYWORDS: Mat Name Color, Transform, Importance, T-Track

### TrackStructure
- `recommendation/TrackStructure/TrackStructure.inp` — PURPOSE: input file for lecture about [ Parameters ] section | KEYWORDS: Track Structure, T-Interact, T-Deposit

### XrayDiagnostic
- `recommendation/XrayDiagnostic/XrayDiagnostic.inp` — PURPOSE: Sample input for dose calculation for X-ray diagnostic | KEYWORDS: T-Deposit, T-Track

### muon
- `recommendation/muon/muon.inp` — PURPOSE: Sample input for muon transport | KEYWORDS: T-Track, T-Product
