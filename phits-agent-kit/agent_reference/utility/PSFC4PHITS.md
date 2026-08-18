# Utility: PSFC4PHITS

SOURCE_FOLDER: D:/NEAgit/utility/PSFC4PHITS
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: PSFC4PHITS
UTILITY_PATH_INDEX: utility/PSFC4PHITS
UTILITY_FOLDER_NAME: PSFC4PHITS

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/PSFC4PHITS
BASIC_FILE_COUNT: 2
BASIC_FILE: README-en.txt
BASIC_FILE_TYPE: txt
BASIC_FILE: README-jp.txt
BASIC_FILE_TYPE: txt
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 2
BONUS_TEXT_COUNT: 18

[BASIC_FILES]
FILE: README-en.txt
BEGIN_BASIC_TEXT
Phase space file converter for PHITS, version 1.03 (2020.11.10)

PSFC4PHITS/
   |
   |---README-en.txt : README in English
   |---README-jpn.txt : README in Japanese
   |---bin/ : Binary executable files
   |---binSAVE/ : Backup directory of bin/
   |---phits.inp : Sample input for PHITS
   |---psfc4phits.inp : Sample input for psfc4phits
   |---psfc4phits_lin.sh : Shell command file to execute psfc4phits (Linux)
   |---psfc4phits_mac.command : Shell command file to execute psfc4phits (Mac)
   |---psfc4phits_win.bat : Batch file to execute psfc4phits (Windows)
   |---src/
        |
        |-IAEA-PHSP_README.TXT : Original README of IAEA-PHSP
        |-compile_lin.sh : Shell command file to compile (Linux)
        |-compile_mac.sh : Shell command file to compile (Mac)
        |-compile_win.bat : Batch file to compile (Windows)
        |-iaea_config.h : Header file (IAEA)
        |-iaea_header.cpp : c++ source file (IAEA)
        |-iaea_header.h : Header file (IAEA)
        |-iaea_phsp.cpp : c++ source file (IAEA)
        |-iaea_phsp.h : Header file (IAEA)
        |-iaea_record.cpp : c++ source file(IAEA)
        |-iaea_record.h : Header file (IAEA)
        |-psfc4phits.F : fortran source file (PHITS original)
        |-utilities.cpp : c++ source file (IAEA)
        |-utilities.h : Header file (IAEA)
          * These source files are originally produced by IAEA Nuclear
            Data Service and modified to adapt to dump data in PHITS format.
            For the details, please refer to the original IAEA
            document which is available from the following URL:
            https://www-nds.iaea.org/reports-new/indc-reports/indc-nds/indc-nds-0484.pdf

**************************************************************************************
  Purpose
**************************************************************************************
PSFC4PHITS is a program to convert a phase space file written in IAEA
format into the format to be used in PHITS as radiation source data.

**************************************************************************************
  Preparation
**************************************************************************************
1. Obtain IAEA phase space file and its header file from somewhere
   such as downloading from IAEA Nuclear Data service HP
   https://www-nds.iaea.org/phsp/phsp.htmlx
   and copy these to PSFC4PHITS/ directory
   (e.g. Varian_Clinac_600C_6MV_1x1.IAEAphsp and Varian_Clinac_600C_6MV_1x1.IAEAheader
    which can be downloaded from the URL below.
    https://www-nds.iaea.org/phsp/photon/Varian_Clinac_600C_6MV/Varian_Clinac_600C_6MV_1x1.IAEAphsp
    https://www-nds.iaea.org/phsp/photon1/Varian_Clinac_600C_6MV_1x1.IAEAheader
   )

2. Create input file (e.g. psfc4phits.inp) containing 5 lines as below.

----------
Varian_Clinac_600C_6MV_1x1  $ input phase space file name without suffix extension
dmp-PHITS.out               $ output file name
1                           $ start particle ID (if you want to convert all PSF, you have to set 1)
9414373                     $ last particle ID (if you want to convert all PSF, you have to set $PARTICLES written in header file)
2                           $ iopt: 1 (w/o weight) 2 (w weight), please see below in detail
----------

* iopt=1: without particle weight value, iopt=2: with particle weight
  value. The converted file is written in binary. Specification of
  jpsf = 1, 2 are necessary when you use the file as the dump
  source. With iopt=-1, the dump data was created in ASCII format so
  that you can check the dump data using text editor. The file size of
  the converted data is almost same as the original data for the
  binary while the size becomes more than 6 times for ASCII (iopt=-1).

**************************************************************************************
  How to RUN PSFC4PHITS
**************************************************************************************

--- Windows --------------------------------------------------------------------------
Drag the created inputfile (psfc4phits.inp) and drop to psfc4phits_win.bat

--- Mac ------------------------------------------------------------------------------
Double click psfc4phits_mac.command and Type the name of the created
inputfile (psfc4phits.inp) into the appeared terminal

--- Linux ----------------------------------------------------------------------------
Execute psfc4phits_lin.sh on terminal and type the name of the created
inputfile (psfc4phits.inp)
--------------------------------------------------------------------------------------

Then the converted data (dmp-PHITS.out), which can be used as a source
file for PHITS, will be created.

**************************************************************************************
  How to use the converted data
**************************************************************************************
In order to use the converted data as a source file, you need to set
the source section of the PHITS input file as follows:
(Note that set dump=9 when you set iopt=1.)

[ S o u r c e ]
set:c1[69184770]  $ $ORIG_HISTORIES (copy & paste the number written in the header file.)
set:c2[9414373]   $ $PARTICLES (copy & paste the number written in the header file.)
  totfact =  c2/c1          $ (D=1.0) global factor
   s-type =  17             $ external source with PHITS dump file
     file =  dmp-PHITS.out  $ file name of dump file
     jpsf =  2              $ >0 special option for Phase Space File
       z0 =  0.0            $ beam starting position

The specification of option for phase space file: jpsf and the beam
starting position: z0 are necessary.

For ASCII file (iopt=-1), description of the dump data is same as
normal dump source otpion as

     dump =   -9            # number of dumped data <0: ascii, >0: binary
                1   2   3   4   5   6   7   8   9

instead of jpsf line of the above.

Settting of the number of total history (maxcas * maxbch) less than the
number of the converted sources is recommended. The phase space file
will be reused when the number of total history is more than the
converted sources. Please be aware the possiblity of baias due to the
reuse of the phase space file.

**************************************************************************************
  How to RE-COMPILE
**************************************************************************************
Change directory to src/

--- Windows --------------------------------------------------------------------------
Double-click compile_win.bat Windows]

--- Mac ------------------------------------------------------------------------------
Execute ./compile_mac.sh in terminal [Mac]

--- Linux ----------------------------------------------------------------------------
Execute ./compile_lin.sh in terminal [Linux]

**************************************************************************************
  Acknowledgement
**************************************************************************************
We modified IAEA Nuclear Data Service's original program to make PSFC4PHITS.
We would like to thank Dr. Roberto Capote Noy (IAEA) and
Dr. Iwan Kawrakow (National Research Council of Canada Ottawa)
for providing the original code.
END_BASIC_TEXT

FILE: README-jp.txt
BEGIN_BASIC_TEXT
Phase space file converter for PHITS, version 1.03 (2020.11.10)

PSFC4PHITS/
   |
   |---README-jpn.txt : 日本語版README
   |---bin/ : 実行形式バイナリファイル
   |---binSAVE/ : バイナリディレクトリのバックアップ
   |---phits.inp : PHITSサンプルインプット
   |---psfc4phits.inp : psfc4phitsサンプルインプット
   |---psfc4phits_lin.sh : psfc4phits実行用シェルコマンドファイル(Linux用)
   |---psfc4phits_mac.command : psfc4phits実行用シェルコマンドファイル(Mac用)
   |---psfc4phits_win.bat : psfc4phits実行用バッチファイル(Windows用)
   |---src/
        |
        |-IAEA-PHSP_README.TXT : IAEA-PHSPオリジナルREADME
        |-compile_lin.sh : コンパイル用シェルコマンドファイル(Linux用)
        |-compile_mac.sh : コンパイル用シェルコマンドファイル(Mac用)
        |-compile_win.bat : コンパイル用バッチファイル(Windows用)
        |-iaea_config.h : ヘッダーファイル(IAEA)
        |-iaea_header.cpp : c++ソースファイル(IAEA)
        |-iaea_header.h : ヘッダーファイル(IAEA)
        |-iaea_phsp.cpp : c++ソースファイル(IAEA)
        |-iaea_phsp.h : ヘッダーファイル(IAEA)
        |-iaea_record.cpp : c++ソースファイル(IAEA)
        |-iaea_record.h : ヘッダーファイル(IAEA)
        |-psfc4phits.F : fortranソースファイル(PHITSオリジナル)
        |-utilities.cpp : c++ソースファイル(IAEA)
        |-utilities.h : ヘッダーファイル(IAEA)
          *これらのソースファイルはIAEAのNuclear Data Serviceにより公開されている
           変換プログラムを元に、PHITS形式のdump dataを作成するよう改変したものです。
           改変元のプログラムについては、下記のURLにより入手できるドキュメントをご覧ください。
           https://www-nds.iaea.org/reports-new/indc-reports/indc-nds/indc-nds-0484.pdf

**************************************************************************************
  Purpose
**************************************************************************************
IAEAにより定められた形式で作成されたphase space fileをPHITSの
線源データとして利用できる形式に変換するプログラムです。

**************************************************************************************
  Preparation
**************************************************************************************
1. フォルダ/PSFC4PHITS/に2種類のIAEAのphase space fileをコピーする。
(ここでは、例として
Varian_Clinac_600C_6MV_1x1.IAEAphsp
Varian_Clinac_600C_6MV_1x1.IAEAheader
とします。これらはそれぞれ、
https://www-nds.iaea.org/phsp/photon/Varian_Clinac_600C_6MV/Varian_Clinac_600C_6MV_1x1.IAEAphsp
https://www-nds.iaea.org/phsp/photon1/Varian_Clinac_600C_6MV_1x1.IAEAheader
からダウンロードできます。)

2. 下記のような内容のPSFC4PHITSのインプットファイル(例psfc4phits.inp)を作成します。

----------
Varian_Clinac_600C_6MV_1x1  $ phase space fileのファイル名(ただし拡張子の前まで)
dmp-PHITS.out               $ PHITS形式のデータを保存するファイル名
1                           $ 変換する最初の粒子ID (全てのデータを変換する場合は1)
9414373                     $ 変換する最後の粒子ID (全てのデータを変換する場合はヘッダーファイルに書かれている$PARTICLESの数字)
2                           $ iopt: 1 (w/o weight) 2 (w weight), 変換後のデータ形式。下記の説明をご覧ください
----------

*iopt=1はウェイトの値を含まない場合、iopt=2はウェイトの値を含む場合で、
 ともにバイナリ(正確にはunformatted形式)で出力します。それぞれ、dumpソース
 として使用する際ににjpsf=1,2としてください。iopt=-1でASCII形式で出力
 し、テキストエディタで数値データを確認することができます。
 変換後のデータ容量は、バイナリの場合に元データと同程度の大きさですが、ASCII形式
 の場合には約6倍となりますのでご注意ください。
 (目安として、1から100000までを変換すると、ASCII形式の場合に約20MB、
 バイナリの場合に約4MBのデータが作成されます。)

**************************************************************************************
  PSFC4PHITSの動作方法
**************************************************************************************

--- Windows --------------------------------------------------------------------------
作成したpsfc4phits.inpをドラッグし、psfc4phits_win.batにドロップする。

--- Mac ------------------------------------------------------------------------------
psfc4phits_mac.commandをダブルクリックし、現れるウィンドウにpsfc4phits.inpを入力

--- Linux ----------------------------------------------------------------------------
psfc4phits_lin.shをターミナルで実行し、psfc4phits.inpを入力
--------------------------------------------------------------------------------------

変換プログラムが実行されると、PHITSで利用できる線源データファイルdmp-PHITS.outが作成されます。

**************************************************************************************
  変換したデータの使用方法
**************************************************************************************
作成された線源データを利用する場合は、PHITSのインプットファイルにおいて、
以下のようにsourceセクションを設定してください。(phits.inpを参照)
(iopt=1の場合はdump=9としてください。)

[ S o u r c e ]
set:c1[69184770]  $ $ORIG_HISTORIES (copy & paste the number written in the header file.)
set:c2[9414373]   $ $PARTICLES (copy & paste the number written in the header file.)
  totfact =  c2/c1          $ (D=1.0) global factor
   s-type =  17             $ external source with PHITS dump file
     file =  dmp-PHITS.out  $ file name of dump file
     jpsf =  2              $ >0 special option for Phase Space File
       z0 =  0.0            $ beam starting position

jpsfの指定とビームの開始位置z0の情報が必ず必要になります。

iopt=-1のファイルのdumpソースの指定方法は、PHITSの通常のdumpソースと同
様で、jpsfの行の代わりに

     dump =   -9            # number of dumped data <0: ascii, >0: binary
                1   2   3   4   5   6   7   8   9

の指定をしてください。

また、上の例で作成される線源データは9414373個分なので、
計算で使用する総ヒストリー数(maxcas * maxbch)がこの数字以下を推奨しま
す。これ以上のヒストリー数を指定すると、phase space fileは使い切った時
点でrewindされて、使いまわされることになります。この使いまわしにより、
統計的に偏った結果になる可能性があることを留意ください。

**************************************************************************************
  再コンパイルの仕方
**************************************************************************************
src/フォルダに移動
(Windowsの場合)compile_win.batをダブルクリック
(Macの場合)ターミナルで./compile_mac.shを実行
(Linuxの場合)ターミナルで./compile_lin.shを実行

**************************************************************************************
  謝辞
**************************************************************************************
PSFC4PHITSは、IAEAのNuclear Data Serviceにより公開されている
変換プログラムを改変し作成しました。このオリジナルの変換プログラムを
作成し公開していただいているIAEAのRoberto Capote Noy氏と
National Research Council of Canada OttawaのIwan Kawrakow氏に
この場を借りて深く御礼申し上げます。
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: phits.inp
FILE: psfc4phits.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: CHANGELOG.txt
FILE: psfc4phits_lin.sh
FILE: psfc4phits_mac.command
FILE: psfc4phits_win.bat
FILE: src/compile_lin.sh
FILE: src/compile_mac.sh
FILE: src/compile_win.bat
FILE: src/iaea_config.h
FILE: src/iaea_header.cpp
FILE: src/iaea_header.h
FILE: src/iaea_phsp.cpp
FILE: src/iaea_phsp.h
FILE: src/IAEA_PHSP_README.TXT
FILE: src/iaea_record.cpp
FILE: src/iaea_record.h
FILE: src/psfc4phits.F
FILE: src/utilities.cpp
FILE: src/utilities.h
