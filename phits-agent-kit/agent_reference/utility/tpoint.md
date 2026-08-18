# Utility: tpoint

SOURCE_FOLDER: D:/NEAgit/utility/tpoint
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: tpoint
UTILITY_PATH_INDEX: utility/tpoint
UTILITY_FOLDER_NAME: tpoint

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/tpoint
BASIC_FILE_COUNT: 2
BASIC_FILE: readme-en.docx
BASIC_FILE_TYPE: docx
BASIC_FILE: readme-jp.docx
BASIC_FILE_TYPE: docx
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 0

[BASIC_FILES]
FILE: readme-en.docx
BEGIN_BASIC_TEXT
Instruction for using [t-point]
1. Introduction
It is impractical to calculate particle fluence at a certain point or line, using [t-track] tally. Hence, the point estimator tally [t-point] was introduced to estimate such quantities in a short computational time. However, the following conditions must be satisfied in the PHITS simulation using [t-point]:
Particle energy should not exceed the maximum energy of the data library used, i.e. dmax
Only fluence of neutron and photon can be calculated by [t-point]
Neither event generator mode nor EGS5 should not be used (e-mode=0, negs=0)
Material should be uniform within a certain distance around the point detector due to singularity of equation described in the next section.
Reflection or white boundary surface should not be used.
This tally was constructed based on the "Flux at a Detector" function written in the manual of MCNP5 (LA-UR-03-1987, Los Alamos National Laboratory).
2. Calculation Procedure
There are two kinds of detectors, namely "point" and "ring", in [t-point]. In this manuscript, the calculation procedure for the point detector is described first, then, that for ring detector will be given next. When a point detector is defined in the PHITS input file, PHITS deterministically estimate the flux contribution of every source or collision event, using the scattering probability at the event location toward the detector point, P, the distance between event and detector points, R, and the transmission probability T without any interaction between event and detector points. Considering the point detector to be a  sphere whose radius is shrinking to 0, the scattering probability P can be determined from the differential scattering probability to the direction to the point detector Ω, as written by
,                                                                   (1)
where dΩ is the solid angle subtended by the imaginary sphere around the point detector. The transmission probability can be determined from the macroscopic cross section at a location s between event and detector points, Σ(s), as written by
.                                                           (2)
When the sphere shrinks to a point, the solid angle dΩ can be determined from the intersection of an arbitrary plane passing through the detector point and the collapsing cone, dA, as written by
,                                                                 (3)
where η is the cosine of the angle between the particle direction and the unit normal to area dA. When a particle with weight w reaches the detector point, the fluxes to be estimated by [t-point], Φ, can be calculated by
(4)
Assuming azimuthal symmetry, the scattering probability can be expressed by the cosine of polar angle μ and azimuthal angle φ, as written by
(5)
(6)
(7)
Then, Eq. (4) can be replaced by
(8)
Note that p(μ) and Σ(s) can be determined from the cross section data library.
However, Eq.(8) has the singularity at R=0. Thus, the mean flux in a fictitious sphere with radius R0 is calculated for the event occurred near the detector point, as written by
(9)
The numerical value of R0 for each point detector can be defined in the input file of PHITS. Substituting Eq.(8) into Eq.(9), one can obtain:
,                                      (10)
where Σ is the macroscopic cross section of material near the point detector. It is evident from this equation that the material within the fictitious sphere should be uniform, otherwise Eq. (10) cannot give the correct answer.
A ring detector tally is a point detector tally in which the point detector location is not fixed but rather sampled from some location on a ring. Most of the previous section on point detectors applies to ring detectors as well. When a point is sampled from the ring, PHITS biases the probability based on 1/R2, i.e. closer locations tend to be selected. Thus, ring detector is more efficient than point detector when the azimuthal symmetry is established in the geometry and source of the simulation, particularly for larger ring radii.
3. Sample Input
"tpoint.inp" is a sample input file using [t-point]. The [Pamraeters] section is almost the same as that given in "recommendation/shielding/shielding.inp". Use of data library is mandatory in this tally, and thus, dmax(2) and/or dmax(14) must be specified. Other variance reduction techniques such as [importance] and [weight window] are not recommended to use in combination with [t-point]. (Biased source by changing weight such as e-type = 4 is OK).
The geometry defined in "tpoint.inp" consists of concentric iron sphere and air shell with radius of 20 and 100 cm, respectively, and spherical air near the point detector to be utilized in [t-track] as described later. Neutron with energy of 1 MeV are isotropically emitted from the origin. Point and ring detectors are respectively defined using [t-point]. The coordinate of the point detector is x = 10 cm, y = 0 cm, and z = 50 cm. The ring radius is 10 cm, its axis is along to z-axis, and the distance from the origin to the center of the ring is 50 cm. Note that the location of the point detector is included in the ring detector. For comparison, [t-track] is also defined to calculate the particle fluence within a sphere of 1 cm radius around the point detector.
In [t-point], you have to define the number of points or rings, instead of "mesh" in other tallies. For example, you have to write "point = 3" when you would like to define 3 point detectors. The maximum number of points or rings per [t-point] is 20. If you would like to set more detectors, you have to define another [t-point] tally. The point and ring detectors cannot be combined in one [t-point] tally. The information on each point and ring must be defined in the successive lines after the definition of "point" or "ring" parameter. The definition of the point detector given in tpoint.inp is:
point = 1
x   y    z  r0
10   0   50   1
where "x", "y", "z" indicate the coordinate of the point detector, "r0" is the radius of the fictitious sphere, i.e. R0 parameter described in the previous section. The unit of these parameters are in cm. The definition of the ring detector given in tpoint.inp is:
ring = 1
axis  ar  rr  r0
z  50  10   1
where "axis" indicates the direction of ring axis specified by x, y or z, "ar" is the distance from the origin to the center of the ring, "rr" is the ring radius, and "r0" is the radius of the fictitious sphere. You can change the order of these parameters by change the order of its denotation, e.g. "x y z  r0" to "z y x r0".  Except for this information, the parameters to be defined in [t-point] are the same as those in [t-track], including the multiplier option. Thus, radiation dose at a certain point can be estimated using [t-point]. However, you cannot specify material, two-dimensional plot option, and transform in [t-point].
4 Results of Sample Input
Figures 1 to 3 show the results of calculated neutron and photon fluxes obtained using [t-point] and [t-track]. It is evident from the figures that the statistical uncertainties in the results of [t-track] are much larger than those of [t-point], particularly photon fluxes where no photon was detected in [t-track]. This tendency clearly indicates the superiority of [t-point] in comparison to [t-track] in terms of the computational efficiency in the case of small tally regions. On the other hand, the results obtained from the point and ring detectors are nearly identical to each other. This is because the radius of the ring detector is not so large that the consideration of the 1/R2 bias does not result in the increase of detection efficiency in this case.
Fig. 1. Neutron and photon fluence calculated by [t-point] with point detector (point.eps)
Fig. 2. Neutron and photon fluence calculated by [t-point] with ring detector (ring.eps)
Fig. 3. Neutron and photon fluence calculated by [t-track] (track.eps)
END_BASIC_TEXT

FILE: readme-jp.docx
BEGIN_BASIC_TEXT
[t-point]の使い方
1 概要
PHITSは,通常,設定した領域に確率的に入ってくる放射線をタリーするため,タリー領域が小さくなると,十分な統計精度を得るためには極めて長い計算時間を要する。極端な例として,タリー領域を点や線分に設定した場合,どれだけ計算時間を費やしても結果を得ることはできない。
そこで,そのようなニーズに応えるため,ある点(point detector)やリング状の線分(ring detector)におけるフラックスを計算するポイントタリー[t-point]を導入した。ポイントタリーは, [t-track]タリーや[t-cross]タリーのように,ある領域を実際に通過する粒子を測定する方法とは異なり,線源位置,もしくは,散乱によって粒子が発生した地点で,ポイントタリー位置への方向確率,また,発生位置からタリー点までの透過確率を計算して評価する。従って,粒子の存在確率が小さい領域での測定に有効である。ただし,散乱点での生成粒子の角度分布,エネルギー分布があらかじめ分かっていないと評価できない。また,物質中での荷電粒子のエネルギー損失があると透過確率の評価が難しいので,評価粒子は,核データの存在する中性子と光子に限られる。したがって,ポイントタリーの利用条件は,
輸送計算の上限エネルギーは,ライブラリを使う上限エネルギー(dmax)とする。
ポイントタリーにより検出可能な粒子は中性子・光子のみとする。
Event Generator及びEGSモード を使用しない。
面定義で全反射や白色反射の面を利用しない。
となる。また,後述の特異点問題があるため,タリーポイントの近くに複数の物質が混在する場合は,結果に注意が必要となる。なお、この[t-point]タリーは,MCNP5のマニュアル(LA-UR-03-1987, Los Alamos National Laboratory)に基づいて開発しました。
2 計算原理
ポイントタリーにはpoint detectorとring detectorの2種類がある。本稿では,まず,point detectorについてその計算原理を説明する。Point detectorが定義された場合,線源,もしくは,衝突点から発生した粒子が指定したポイントに寄与する確率を,発生点からポイントまでの方向確率P,距離R,及び透過係数Tを用いて評価する。方向確率Pは,角度Ωに対するその微分値p(Ω) を用いて
,                  (1)
と表される。ここでdΩは,ポイントの周辺に仮想的な球を想定したときの発生点から見た立体角を表す。透過係数Tは,粒子の現在位置とポイントの間の座標sにおける巨視的断面積Σ(s)を用いて,
,                (2)
と表される。立体角dΩは,ポイント周辺の仮想的な球の半径が0の極限を考えると,ポイントを通る任意の面要素dAと粒子方向とその面要素の法線との余弦値ηを用いて,
,                  (3)
と表される。また,ウェイトwの粒子がポイントを通過したときのフルエンスはとなるため,ポイントタリーで測定するべきフラックスΦは,この値と(1)と(2)の積
(4)
と表される。方向確率Pは,方位角φの対称性を仮定すれば,
(5)
(6)
(7)
となり余弦μの関数として表されるため,式(4)は
(8)
となる。p(μ)及びΣ(s)は,断面積ライブラリより参照可能な量である。
式(8)はR=0で特異点になるので,ポイント周辺の特異領域の半径R0以内では,以下のようにフラックスの平均を取ることとする。
(9)
この特異領域の半径R0は,各point detectorに対して入力ファイルで設定することができる。式(9)に式(8)を代入すると
(10)
が得られる。ここでΣは,タリーポイント周辺の物質に対する巨視的断面積を表す。したがって,特異領域内で複数の物質(例えば空気と鉄)などが混じってしまうと,正しい結果が得られない場合があるため注意が必要となる。
Point detectorが1点の固定された座標でタリーするのに対し, ring detectorは,リング状の位置の中からに1点を選んでタリーする。従って,上述したpoint detectorの説明はそのままring detectorに当てはまる。リングの中からタリーするポイントを選ぶ際は,なるべく反応点から近いリング状の点を選択するよう,1/R2のバイアスが掛けられている(Rは反応点とリング状のある点までの距離)。したがって,計算モデル(線源,体系)に軸対称性があり,リングが大きい場合は,point detectorよりも効率の良い計算が可能となる。なお,結果は,リング状の線分に対して平均したものであり,リング内の円面上で平均したものでないことに注意する必要がある。
3 例題
[t-point]を使った例題をtpoint.inpに示す。[t-point]を使うためには,データライブラリの使用が必須なため,[parameters]セクションでdmax(2),dmax(14)を設定する(中性子もしくは光子の輸送のみ必要な場合は,どちらか一方のみでも可)。これらの設定は,奨励設定のshieldingと同じ設定である。また,ポイントタリーは分散低減に対して有効な手段であるが,他の分散低減の機能,importance,forced collision,weight windows等との併用は,設定によっては誤差の収束性が保障できないので推奨しない。ただし,Weightで線源にバイアスを掛けること(e-type=4など)は可能である。
本例題の体系は,原点を中心とする半径20cmの鉄球,及びその外側にある半径100cmの空気層より構成される。線源は,原点から等方的に1.0MeVの中性子を放出する放射線源とした。この条件に対して,x=10cm, y=0cm, z=50cmのpoint detector,及びその点を含む半径10cm,z=50cmのring detectorをそれぞれ[t-point]を使って定義し,中性子及び光子のエネルギー分布を評価した。また,比較のため, x=10cm, y=0cm, z=50cmを中心とする半径1cmの領域での中性子及び光子のエネルギー分布を[t-track]を用いて評価した。
[t-point]では,他のダリ-のようにmeshパラメータを指定する必要はなく,最初に検出器の形状(pointもしくはring)と数を設定する(例えばpoint = 3)。ひとつのポイントタリーセクションで定義できるポイントやリングの上限数は20である。これ以上のポイントやリングを定義するときは,複数のポイントタリーセクションを用いる必要がある。また,ひとつのポイントタリーに,pointとringの併用はできない。次の行以降では,ポイントもしくはリングの情報を指定する。Point detectorの例題の場合
point = 1
x   y    z  r0
10   0   50   1
となっている。x,y,zは,point detectorの座標(cm),r0はポイント周辺の特異領域半径R0(cm)を示す。一方,ring detectorの例題の場合は
ring = 1
axis  ar  rr  r0
z  50  10   1
となっている。axisはリングの軸(x,y,zで指定), arは原点からリング中心までの距離(cm), rrはリングの半径(cm),r0は特異領域半径R0(cm)を示す。データを指定する順番は,x y z r0もしくはaxis ar rr r0と書く順番を変えることにより変更可能である。また,読み飛ばしを意味するnonも利用可能である。pointもしくはringを2つ以上定義する場合は,次行以降に継続してその情報を与える。
[t-point]の書式は,上記を除いて基本的に[t-track]の入力書式と同じである。ただし,material指定,2次元表示関係,座標変換の指定は,[t-point]では使用不可である。Multiplierの指定は可能である。従って,ポイント測定値位置での線量や反応率等の計算はできる。
4 例題の結果
[t-point]のpoint detector及びring detector,並びに[t-track]で計算した中性子及び光子のエネルギー分布を図1~3に示す。図より,[t-point]の結果と比べて[t-track]の結果は,統計が十分でないことが分かる。特に,光子に関しては,[t-track]では1粒子も検出されていない。このように,体系が大きく検出器が小さい場合,[t-point]が計算時間を短縮するために極めて有効となる。また,[t-point]のpoint detectorとring detectorの統計精度は,本例題の場合はほぼ同等である。これは,リングの半径がそれほど大きくなく,1/R2バイアスの効果が小さいためである。
図1 [t-point] point detectorの結果(point.eps)
図2 [t-point] ring detectorの結果(ring.eps)
図3 [t-track]の結果(track.eps)
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: t-point.inp

[BONUS_TEXT_FILES]
NOTE: None
