# Utility: HighPerformanceComputing

SOURCE_FOLDER: D:/NEAgit/utility/HighPerformanceComputing
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: HighPerformanceComputing
UTILITY_PATH_INDEX: utility/HighPerformanceComputing
UTILITY_FOLDER_NAME: HighPerformanceComputing

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/HighPerformanceComputing
BASIC_FILE_COUNT: 0
BASIC_FILE: (none)
BASIC_FILE_TYPE: none
PPTX_COUNT: 2
BONUS_INPUT_COUNT: 0
BONUS_TEXT_COUNT: 0

[BASIC_FILES]
FILE: (not found)
NOTE: No readme* file and no .docx file found.

[PPTX_CONTENTS]
FILE: phits-lec-HPC-en.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-lec-HPC-en.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
PHITS
PHITS Tutorial
PHITS simulation on High Performance Computing (HPC)
Multi-Purpose Particle and Heavy Ion Transport code System
Title
1
Sep. 2025 revised

--- SLIDE 02 ---
Table of Contents
2
Good statistics requires heavy computations in Monte Carlo transport simulation
HPC will help achieving this goal !!
Required directories
Recompile of PHITS
PHITS parallel executions
Parallelization efficiency
Additional tips for PHITS parallel execution
You can use PHITS in HPC as long as you have a valid PHITS license. You do not have to ask a new license for HPC.
However, PHITS is exclusively licensed to individual so please install PHITS to your personnel account which only you can access.
Table of contents
Because HPC (supercomputers or cluster computers) are usually operated with Linux, following explanations are given for Linux but some are applicable for Windows and Mac

--- SLIDE 03 ---
Required directories
3
phits/
    |
    |---bin/ : Directory containing executable binaries
    |---data/ : Directory containing data files required for PHITS
    |---src/: Directory containing source files
    |---XS/: Nuclear/Atomic cross section data library
PHITS executables with MPI and with OpenMP is prepared in bin/
(phits_mpi_lin, phits_omp_lin.exe)
In case the library is incompatible or OpenMP-MPI hybrid is required, recompilation of the source is required
Directories required for PHITS execution
To use PHITS in HPC environment,
install PHITS using the PHITS installer for LINUX
or copy required directories from the other PHITS installed PC
Required directories
Please keep the directory structure of phits as it is to keep the consistency of the path including phits directory

--- SLIDE 04 ---
Recompile of PHITS
4
=> Executables will be created in the parent directory
How to recompile PHITS
### Machine Dependent variables, please set your environment
ENVFLAGS = LinIfort
# Linux Intel Fortran: LinIfort
# Linux gfortran:       LinGfort

...

### If you want to use MPI, delete # in the next line
# USEMPI = true
### If you want to use OpenMP, delete # in the next line.
# USEOMP = true
makefile
Fortran compiler such as Intel OneAPI* or GNU fortran
GNU make
Requirements
*How to install Intel OneAPI is explained in phits/document/InstallFortran-OneAPI-en.pdf
1. Modify the makefile in phits/src
2. "make" in the terminal at phits/src to recompile PHITS
Erase # to activate OpenMP parallelization
Erase # to activate MPI parallelization
Erasing both # for hybrid parallelization
Change ENVFLAGS to fit your environment
phits_($ENVFLAGS)                      : Single
phits_($ENVFLAGS)_MPI             : MPI
phits_($ENVFLAGS)_OMP           : OpenMP
phits_($ENVFLAGS)_OMP_MPI  : Hybrid
make -j ncore
allows parallelized compilation with ncore cores

--- SLIDE 05 ---
Recompile of PHITS
5
Compiler options may need to modify according to your environment
But the options for PHITS are simple so please modify following to the current "makefile"
Compiler options
...
### Linux Intel Fortran
ifeq ($(ENVFLAGS),LinIfort)
 IntelFortran = true
 SRCS8  += mdp-uni90.f
 ifeq ($(DEBUG),true)
  FFLAGS = -O0 -fpconstant -g -traceback -fpe0 -fp-stack-check -check uninit
 else
  FFLAGS = -O3 -fpconstant
 endif
 ifeq ($(USEOMP),true)
  FFLAGS += -qopenmp  ### if -qopenmp does not work, try -openmp
  LD = $(FC) -static-intel
 endif
 ifeq ($(USEMPI),true)
  FC = mpiifort
  LDLIBS = -lmpi ### -lmpi sometimes -lmpich, or not necessary
 else
  FC = ifort
 endif
endif
...
makefile
Here $ENVFLAGS=LinIfort is assumed
Compiler options
An option to enable OpenMP
MPI compile command
MPI library linker option

--- SLIDE 06 ---
PHITS parallel execution
6
Required file path setting and PHITS execution
PHITS installation directory name "file(1)" should be specified in [parameter] section of the input file
e.g.  file(1) = /home/user/phits
This process can be skipped by installing PHITS using the PHITS installer
 or setting the directory path in the PHITSPATH environmental variable
A file named "phits.in" is required where the input file is specification as
file = ***.inp
Single
./phits_LinIfort < ***.inp
Here ($ENVFLAGS) = LinIfort is assumed.
OpenMP
export OMP_NUM_THREADS = 4
./phits_LinIfort_OMP < ***.inp
nOpneMP: # of OpenMP parallelization
MPI
mpiexec -n 5 ./phits_LinIfort_MPI
The executable specification with path. The current directory existence is assumed
nMPI: # of MPI parallelization but the parallelized calculation processes are nMPI-1
The command may differ such as mpirun
Installation of MPI protocol in the system is required
For BASH, modification may be required for other SHELL
PHITS adopts "master-slave system" so 1 master is used to control nMPI-1 calculation slaves

--- SLIDE 07 ---
PHITS parallel execution
7
PHITS parallel execution
Pre-process (Reading input file and some pre-calculation)

nobch=1, maxbch

    nocas=1, maxcas

          Particle transport calculation of 1 history

    nocas loop end

nobch loop end

Post-process (Summarizing data, creating output files including figures)
At each step of the batch end, tally data is sent to master and summarized
The data output at this time is controlled by "itall" parameter
  -1: No output, 0: Only text data, 1 Text data & image file, ...

--- SLIDE 08 ---
PHITS parallel execution
8
How to confirm parallelization run
OpenMP
OpenMP PARALLEL PROCESS 1/   2 @ IP(MPI)=   0
OpenMP PARALLEL PROCESS 2/   2 @ IP(MPI)=   0
bat[     1] ncas =         50. : date = 2024-06-24 : time = 14h 29m 45s
bat[     2] ncas =       100. : date = 2024-06-24 : time = 14h 29m 46s
OpenMP FINALIZE 1/   2 @ IP(MPI)=   0
OpenMP FINALIZE 2/   2 @ IP(MPI)=   0
Standard output
nOpneMP = 2
MPI
phits.out
nMPI = 3
Bottom line of PHITS logo
End of phtis.out file
(nMPI - 1) = 2
Summary of MPI status

--- SLIDE 09 ---
Parallelization efficiency
9
PHITS parallelization efficiency
Recommendation file "ParticleTherapy"
Recommendation file "PhotonTherapy"
Time loss by OMP enabled executable due to overhead
Heavy calculation in one history
= "Good" with OpenMP
(Nuclear interactions by models, Heavy ion transport)
Light calculation in one history
= "Bad" with OpenMP
 (Transport by data library such as neutrons & photons)

--- SLIDE 10 ---
Parallelization efficiency
10
PHITS parallelization efficiency for very large # of nodes
T. Furuta et al., Proceedings of SNA+MC2015
Hybrid calculation with nOpenMP = 8 for each node
Almost no communication are required among MPI processes in PHITS
=> Good scaling until 4000 nodes where communication overhead can not be neglected

--- SLIDE 11 ---
Additional TIPS
11
Sample of job script for HPC
#!/bin/sh
#PBS -q p48
#PBS -l select=1:ncpus=24:mpiprocs=12:ompthreads=2
#PBS -P job
#PBS -l walltime=00:30:00
#PBS -N PHITS

EXE=/home/user/phits/bin/phits_LinIfort_OMP_MPI

cd $PBS_O_WORKDIR

mpijob $EXE
Job queue specification
Total number of CPUs
Number of MPI processes
Number of OpenMP threads
Move to home directory
Job execution
This is just an example
The specification highly depends on cases
A typical example of a job script

--- SLIDE 12 ---
Additional TIPS
12
Parallel calculation with dump source
[ source ]
s-type=17
file=***_dmp.out
dump=9
1 8 9 2 3 4 5 6 7
The file with "_dmp" should be specified
OpenMP: No special care is required
MPI: The dump files for each MPI process are required*
         ***_dmp.out.001, ***_dmp.out.002, ...
# of data specification
Data sequence specification
* When the number of MPI processes has been changed from that
obtained the  dump files,  the resorting of the dump data to the proper number of MPI processes is required
 => Please see and use executable in phits/utilitiy/dump-a

--- SLIDE 13 ---
Summary
13
Summary
Use of HPC is recommended to achieve good statistics
Re-compile of PHITS may be required
MPI and OpenMP parallelization is available with PHITS
With MPI, good parallelization efficiency but large memory requirement
With OpenMP, less memory requirement but low parallelization efficiency for cases with light calculation in one history
MPI + OpenMP hybrid calculation is also available
GPU application was tried but results were unsatisfactory*
Reference
OpenMP implementation: T. Furuta et al., IFMBE Proceedings 39, 2099-2102 (2012)
Parallelization efficiency: T. Furuta et al., Proceedings of SNA+MC2015 (https://www.researchgate.net/publication/374263105_Pallalel_computing_with_particle_and_heavy_ion_transport_code_system_PHITS)
Parallelization efficiency: T. Furuta et al., Jpn. J. Med. Phys. Vol. 35 No. 3: 264-268 (2015) in Japanese
=> It requires improvements in algorithm level
* The option is available in makefile with PGI Fortran
END_PPTX_TEXT

FILE: phits-lec-HPC-jp.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-lec-HPC-jp.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
PHITS
PHITS Tutorial
高性能計算機(HPC)を用いたPHITSシミュレーション
Multi-Purpose Particle and Heavy Ion Transport code System
Title
1
Sep. 2025 revised
(utility/HighPerformanceComputing)

--- SLIDE 02 ---
Table of Contents
2
モンテカルロ計算で十分な統計量の結果を得るためには非常に長時間の計算が必要である
高性能計算機(HPC)の利用が一つの解決策
PHITS実行に必要なディレクトリ
PHITSの再コンパイル
PHITSでどう並列計算されているのか
PHITS並列計算の効率
PHITS並列計算のコツ
PHITSの有効ライセンスを保有する限り、PHITSをHPCで利用可能
(=新たなライセンスを取得する必要無し)。
但し、PHITSのライセンスは個人ライセンスであることからユーザー個人のみがアクセスできる領域にPHITSをインストールする必要あり。
内容
HPC (クラスター計算機やスパコン)は通常Linuxで運用されているので、ここではLinuxを例に説明する(但し、同様のことがWindowsやMacでも実行可能)

--- SLIDE 03 ---
Required directories
3
phits/
    |
    |---bin/ : 実行バイナリが含まれるディレクトリ
    |---data/ : PHITS用データファイルが含まれるディレクトリ
    |---src/: PHITSのソースコードが含まれるディレクトリ
    |---XS/: 核・原子断面積データライブラリ
PHITS並列計算用実行ファイル(MPIおよびOpenMP版)はbin/ディレクトリに既に用意済み
(phits_mpi_lin, phits_omp_lin.exe)
ライブラリの不整合等が起きる場合やOpenMP-MPIハイブリッドの実行ファイル作成のためには、ソースコードからの再コンパイルが必要
PHITS実行に必要なディレクト
高性能計算機でPHITSを実行するための環境を用意するため、
Linux用PHITSインストーラを利用してPHITSをインストール
もしくはインストール済み別PCから必要ディレクトリをコピー
必要ディレクトリ
ファイルパスは既存のディレクトリ構造を想定しているので、PHITS以下のディレクトリ構造は変更しないでください

--- SLIDE 04 ---
Recompile of PHITS
4
=> 親ディレクトリに実行ファイル生成
PHITSの再コンパイルの仕方
### Machine Dependent variables, please set your environment
ENVFLAGS = LinIfort
# Linux Intel Fortran: LinIfort
# Linux gfortran:       LinGfort

...

### If you want to use MPI, delete # in the next line
# USEMPI = true
### If you want to use OpenMP, delete # in the next line.
# USEOMP = true
makefile
Intel OneAPI*やGNU fortran等のFortranコンパイラ
GNU make
必要要件
*Intel OneAPIのインストールの仕方はphits/document/InstallFortran-OneAPI-en.pdfを参照
1. phits/srcのmakefileを修正
2. ターミナル上でphits/srcディレクトリに移動し"make"を実行
OpenMP並列を有効にするには#を削除
MPI並列を有効にするには#を削除
ハイブリッド並列にするには両方の#を削除
ENVFLAGSを環境に合わせて修正
phits_($ENVFLAGS)                      : Single
phits_($ENVFLAGS)_MPI             : MPI
phits_($ENVFLAGS)_OMP           : OpenMP
phits_($ENVFLAGS)_OMP_MPI  : Hybrid
make -j ncore
のコマンドでncoreを使った並列コンパイル可能

--- SLIDE 05 ---
Recompile of PHITS
5
コンパイラオプションは環境に従って変更する必要あり
ただ、単純なオプションしかPHITSには必要無いので、"makefile"に従った変更は容易
コンパイラオプション
...
### Linux Intel Fortran
ifeq ($(ENVFLAGS),LinIfort)
 IntelFortran = true
 SRCS8  += mdp-uni90.f
 ifeq ($(DEBUG),true)
  FFLAGS = -O0 -fpconstant -g -traceback -fpe0 -fp-stack-check -check uninit
 else
  FFLAGS = -O3 -fpconstant
 endif
 ifeq ($(USEOMP),true)
  FFLAGS += -qopenmp  ### if -qopenmp does not work, try -openmp
  LD = $(FC) -static-intel
 endif
 ifeq ($(USEMPI),true)
  FC = mpiifort
  LDLIBS = -lmpi ### -lmpi sometimes -lmpich, or not necessary
 else
  FC = ifort
 endif
endif
...
makefile
ここでは$ENVFLAGS=LinIfortが選択された場合を想定
コンパイラオプション
OpenMP並列を有効化するオプション
MPI並列を有効化するオプション
MPIライブラリのリンカーオプション

--- SLIDE 06 ---
PHITS parallel execution
6
PHITSの実行のために必要なパス設定
PHITSのインストールディレクトリパスをインプットファイルの[parameter]セクションの"file(1)"に設定
e.g.  file(1) = /home/user/phits
PHITSインストーラーを使ってインストールした場合、もしくはPHITSPATH環境変数にそのパス設定を行った場合はfile(1)の設定必要無し
"phits.in"の名前で以下の様にインプットファイルを指定するファイルが必要
file = ***.inp
Single
./phits_LinIfort < ***.inp
ここで($ENVFLAGS) = LinIfortでコンパイルされた実行ファイル名を想定
OpenMP
export OMP_NUM_THREADS = 4
./phits_LinIfort_OMP < ***.inp
nOpneMP: OpenMPの並列コア数
MPI
mpiexec -n 5 ./phits_LinIfort_MPI
パス込みで実行ファイルを指定。./は現在のディレクトリに実行ファイルがあることを想定
nMPI: MPIの並列プロセス数。但し、実際の計算プロセス数は nMPI-1
コマンド名がmpirunになったりする場合 も
MPIプロトコルを事前にインストールすることが必須
BASHの場合の環境変数設定を想定。Shellが違う場合は合わせて変更必要
PHITSは"マスタースレーブ方式"を採用しているため、1つのマスターがnMPI-1のスレーブをコントロールする

--- SLIDE 07 ---
PHITS parallel execution
7
どう並列計算されているのか
プリプロセス (インプットファイルの読み込み、いくつかの前段階計算)

nobch=1, maxbch

    nocas=1, maxcas

          線源1個分(1ヒストリ)の粒子輸送計算

    nocas loop end

nobch loop end

ポストプロセス (データ集計、画像も含めた出力ファイル生成)
各batch計算の終了時にタリーデータはマスターに送信され集計される。
この時点でのデータ出力は"itall"パラメータで制御
  -1: 出力しない, 0: テキストデータのみ出力, 1: テキストと画像出力, ...

--- SLIDE 08 ---
PHITS parallel execution
8
並列実行の確認
OpenMP
OpenMP PARALLEL PROCESS 1/   2 @ IP(MPI)=   0
OpenMP PARALLEL PROCESS 2/   2 @ IP(MPI)=   0
bat[     1] ncas =         50. : date = 2024-06-24 : time = 14h 29m 45s
bat[     2] ncas =       100. : date = 2024-06-24 : time = 14h 29m 46s
OpenMP FINALIZE 1/   2 @ IP(MPI)=   0
OpenMP FINALIZE 2/   2 @ IP(MPI)=   0
ターミナル出力
nOpneMP = 2
MPI
phits.out
nMPI = 3
PHITSロゴでの最後の行
phtis.out最後辺り
(nMPI - 1) = 2
MPI並列計算のステータス

--- SLIDE 09 ---
Parallelization efficiency
9
PHITS並列計算の効率
"ParticleTherapy" recommendationファイル
"PhotonTherapy" recommendationファイル
OpenMPを有効化したことによるオーバヘッドの時間ロス
1ヒストリが重い計算
= OpenMPで"十分良い効率"
(重い計算:原子核反応のモデル計算)
1ヒストリが軽い計算
= OpenMPで"効率低下"
 (軽い計算:データライブラリを使用した中性子や光子の輸送計算)

--- SLIDE 10 ---
Parallelization efficiency
10
PHITS大規模並列計算での並列化効率
T. Furuta et al., Proceedings of SNA+MC2015
各ノードでnOpenMP = 8を指定したハイブリッド計算
PHITSでは並列計算中のMPIプロセス間のやり取りをほぼ必要としない
=> 非常に良いスケーリング (4000ノードまで:それ以降はオーバーヘッドが無視できない)

--- SLIDE 11 ---
Additional TIPS
11
HPC用サンプルジョブスクリプト
#!/bin/sh
#PBS -q p48
#PBS -l select=1:ncpus=24:mpiprocs=12:ompthreads=2
#PBS -P job
#PBS -l walltime=00:30:00
#PBS -N PHITS

EXE=/home/user/phits/bin/phits_LinIfort_OMP_MPI

cd $PBS_O_WORKDIR

mpijob $EXE
ジョブキューの指定
使用全CPU数の指定
MPIプロセス数の指定
OpenMPコア数の指定
ホームディレクトリへの移動
ジョブ実行
これは一例。指定の仕方は環境依存。
典型的なジョブスクリプト

--- SLIDE 12 ---
Additional TIPS
12
並列計算時のダンプ線源の指定法
[ source ]
s-type=17
file=***_dmp.out
dump=9
1 8 9 2 3 4 5 6 7
ダンプファイル取得で"_dmp"の付いたファイルを指定
OpenMP: 特に処理必要無し
MPI: 各MPIプロセスに分かれたダンプファイルが必要*
         ***_dmp.out.001, ***_dmp.out.002, ...
ダンプ変数の数
データ並びの指定
* MPIプロセス数がダンプファイル取得時と異なる場合、MPIプロセス数に合わせたダンプデータの再配分が必要。
 => phits/utilitiy/dump-aに用意された実行ファイルを使用

--- SLIDE 13 ---
まとめ
13
Summary
高性能計算機を使用することで統計精度を向上
場合に依ってPHITSの再コンパイルが必要
PHITSではMPIおよびOpenMPの両方の並列計算が可能
MPI並列計算では大容量の物理メモリが要求されるが、比較的良い並列化効率が望める
OpenMP並列計算ではメモリが節約できるが、1ヒストリの計算が軽い場合には並列化効率が低下する場合あり
PHITSではMPI + OpenMPハイブリッド計算も可能
GPUへの対応も試行したが、効果無し(むしろ計算効率低下)*
Reference
OpenMP implementation: T. Furuta et al., IFMBE Proceedings 39, 2099-2102 (2012)
Parallelization efficiency: T. Furuta et al., Proceedings of SNA+MC2015 (https://www.researchgate.net/publication/374263105_Pallalel_computing_with_particle_and_heavy_ion_transport_code_system_PHITS)
Parallelization efficiency: T. Furuta et al., Jpn. J. Med. Phys. Vol. 35 No. 3: 264-268 (2015) in Japanese
=> 十分な効果を得るにはアルゴリズムレベルの改良が必要
* makefile中にPGI Fortranによるオプションあり
END_PPTX_TEXT

[BONUS_INPUT_FILES]
NOTE: None

[BONUS_TEXT_FILES]
NOTE: None
