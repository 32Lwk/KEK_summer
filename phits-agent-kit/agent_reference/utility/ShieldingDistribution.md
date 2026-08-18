# Utility: ShieldingDistribution

SOURCE_FOLDER: D:/NEAgit/utility/ShieldingDistribution
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: ShieldingDistribution
UTILITY_PATH_INDEX: utility/ShieldingDistribution
UTILITY_FOLDER_NAME: ShieldingDistribution

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/ShieldingDistribution
BASIC_FILE_COUNT: 2
BASIC_FILE: ShieldingDistribution-en.docx
BASIC_FILE_TYPE: docx
BASIC_FILE: ShieldingDistribution-jp.docx
BASIC_FILE_TYPE: docx
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 3
BONUS_TEXT_COUNT: 0

[BASIC_FILES]
FILE: ShieldingDistribution-en.docx
BEGIN_BASIC_TEXT
Instruction for calculating shielding thickness in PHITS using the Ray-Trace method
2018/10/11
There are two ways to calculate the shielding thickness in PHITS. If you want to calculate the average shielding thickness in a single region (or point), the combination of [t-track] and multiplier is simple and convenient (see Mean.inp). If you want to calculate the shielding thickness distribution, you need to combine [t-track] and ismode, which makes the calculation method a little more complicated. Please refer to Point-Distribution.inp if you want to calculate the shielding thickness distribution from a single point, or Area-Distribution.inp if you want to calculate the shielding thickness distribution within a specific area (or multiple areas).
Mean.inp
By isotropically generating a source from the region for which you want to calculate the average shielding thickness and using the multiplier's -120 option (multiplying the track length by the density) in [t-track], the total mass of the track generated outward from the region is calculated and the average value (i.e., average shielding thickness) is Outputs the average value (i.e., average shielding thickness). The mesh of [t-track] must be xyz and must be very large (in this case ±c99 = 10000 cm) to include all areas except the void.
Area-Distribution.inp
A virtual proton (10 GeV in the setup) is generated isotropically (dir=all) inward from a spherical surface (s-type=9) and its energy decay is calculated using [t-track] to derive the shielding thickness distribution for a specific region (points are not allowed). Virtual protons are tuned so that their stopping power is proportional to their density and do not cause nuclear reactions. For example, if a virtual particle flies 3 cm in a density of 10 g/cm2, its energy will always decay by 30 MeV. To convert a proton into a virtual proton, ismode=1, ndedx=2, and cmin(1) must be set to extremely large values (e.g., 1.0e10) in the [parameters] section. The radius of the spherical source should be adjusted with c99 and set to a size that covers all areas except the void. Note, however, that if the radius is set too large, it will take time for the statistics to accumulate.
In [t-track], the range from 10000-c98 MeV to 10000 MeV is tallied by dividing the range into c98/c97 equal parts. By using this setting, the shielding thickness distribution up to c98 (g/cm2) can be output with a resolution of c97 (g/cm2). For example, the track length from 9999 MeV to 10000 MeV corresponds to a shielding thickness distribution from 0 to 1 g/cm2, and the shielding thickness increases by 1 g/cm2 as the energy decreases by 1 MeV. Note that the shielding thickness distribution in various regions can be tallied simultaneously, but the smaller the region, the harder it is to accumulate statistics. Therefore, in principle, the shielding pressure distribution at a specific point cannot be calculated. Also, since there is no normalization, the integral value should be set to 1 by dividing by the sum over value.
Point-Distribution.inp
Similar to Area-Distribution.inp, [t-track] tally the energy decay of virtual protons, but since virtual protons isotropically emitted from a point source are tallied in a 1 cm thick spherical shell region, the shielding thickness at the source location can be calculated. The source coordinates are defined in [transform], and the coordinates are set to be linked to the center coordinates of the tally region. This ensures that all particles fly 1 cm through the tally region, so the result is normalized to 1 and the probability density can be derived directly. Specify the coordinates (x,y,z) of the point (c94,c95,c96) at which you want to evaluate the shielding thickness. Also, specify the radius from that point that includes all material by c99. The interpretation of the data is the same as in Area-Distribution.inp, except that the integral value of the distribution is normalized to 1.
Translated with www.DeepL.com/Translator (free version)
END_BASIC_TEXT

FILE: ShieldingDistribution-jp.docx
BEGIN_BASIC_TEXT
RayTrace法を用いてPHITSで遮蔽厚を計算するための手引き
2018/10/11
PHITSで遮蔽厚を計算する方法は2通りあります。ある1つの領域(点でも可)での遮蔽厚の平均値を計算したい場合は[t-track]とmultiplierを組み合わせた計算手法が簡単で便利です(Mean.inp参照)。遮蔽厚分布を計算したい場合は,[t-track]とismodeを組み合わせる必要があり,計算手法が多少複雑になります。ある1つの点からの遮蔽厚分布を計算したい場合はPoint-Distribution.inpを,特定の領域(複数でも可)内での遮蔽厚分布を計算したい場合はArea-Distribution.inpをご参照下さい。
Mean.inp
遮蔽厚の平均値を計算したい領域から線源を等方的に発生させ,[t-track]でmultiplierの-120番(飛跡長に密度を乗じるオプション)を使うことにより,その領域から外側に向かって発生する飛跡が通る合計質量を計算し,その平均値(すなわち平均遮蔽厚)を出力します。[t-track]のmeshはxyzとし,Voidを除く全ての領域が含まれるような極めて大きい範囲(この場合は±c99 = 10000cm)を指定する必要があります。
Area-Distribution.inp
球面(s-type=9)から内側に等方的(dir=all)に仮想的な陽子(設定上は10GeV)を発生させ,そのエネルギー減衰を[t-track]で計算することにより,特定の領域(点は不可)に対する遮蔽厚分布を導出します。仮想陽子は,その阻止能が密度に比例するように調整され核反応は引き起こしません。例えば,仮想粒子が密度10g/cm2の中を3cm飛行した場合,そのエネルギーは常に30MeV減衰します。陽子を仮想陽子に変換するには[parameters]セクションでismode=1, ndedx=2, cmin(1)を極端に大きい値(例えば1.0e10)に設定する必要があります。また,球面線源の半径はc99で調整し,Voidを除く全ての領域をカバーする大きさを設定する必要があります。ただし,半径を大きくしすぎると統計が溜まるのに時間が掛かりますので,ご注意ください。
[t-track]では,10000-c98 MeVから10000 MeVまでの範囲をc98/c97等分してタリーします。このように設定することにより,分解能c97(g/cm2)で最大c98(g/cm2)までの遮蔽厚分布を出力できます。例えば,エネルギー9999 MeVから10000 MeVまでの飛跡長は遮蔽厚0~1g/cm2の遮蔽厚分布に対応し,エネルギーが1MeV低くなるに従って遮蔽厚が1g/cm2厚くなります。様々な領域における遮蔽厚分布を同時にタリーできますが,領域が小さくなると統計が溜まりにくくなるのでご注意ください。したがって,特定の点における遮蔽圧分布は原理的に計算することができません。また,規格化はされていませんので,sum overの値で割ることにより積分値を1としてください。
Point-Distribution.inp
Area-Distribution.inpと同様に仮想的な陽子のエネルギー減衰を[t-track]でタリーしますが,点線源から等方的に放出された仮想陽子を厚さ1cmの球殻領域でタリーしているため,線源位置における遮蔽厚を計算できます。線源座標は[transform]で定義し,その座標とタリー領域の中心座標を連動するように設定されています。これにより,全ての粒子はタリー領域を必ず1cm飛行するため,結果が1に規格化されProbability densityを直接導出することが可能となります。遮蔽厚を評価したい点の座標(x,y,z)を(c94,c95,c96)で指定してください。また,その点から全ての物質が含まれる半径をc99で指定してください。データの解釈方法は,分布の積分値が1に規格化されている点を除いてArea-Distribution.inpと同じです。
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: Area-Distribution.inp
FILE: Mean.inp
FILE: Point-Distribution.inp

[BONUS_TEXT_FILES]
NOTE: None
