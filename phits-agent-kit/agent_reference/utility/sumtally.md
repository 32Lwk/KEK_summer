# Utility: sumtally

SOURCE_FOLDER: D:/NEAgit/utility/sumtally
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: sumtally
UTILITY_PATH_INDEX: utility/sumtally
UTILITY_FOLDER_NAME: sumtally

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/sumtally
BASIC_FILE_COUNT: 2
BASIC_FILE: readme-eng.txt
BASIC_FILE_TYPE: txt
BASIC_FILE: readme-jpn.txt
BASIC_FILE_TYPE: txt
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 7
BONUS_TEXT_COUNT: 3

[BASIC_FILES]
FILE: readme-eng.txt
BEGIN_BASIC_TEXT
List of Contents
  example1 folder: example input file for isumtally=1
  example2 folder: example input file for isumtally=2
  readme-eng.txt: Instruction written in English (this file)
  old-sumtally folder: old version of sumtally program

1.General
  Sample input files for a function to sum up two (or more) tally results (sumtally function).

2.How to use
 1. icntl is set to 13 in [parameters] section
 2. The parameters for each tally results such as mesh, axis, and part,
   are identical to one another.
 3. Sumtally subsection is defined in the tally section that outputs one
   of the summing up tallies.

3.Contents
  1. Sumtally.inp in example1 can be used with isumtally=1 to perform
    integration of tally results.
  2. Sumtally.inp in example2 can be used with isumtally=2 to obtain
    sum of tally results weighted by user defined ratios.
END_BASIC_TEXT

FILE: readme-jpn.txt
BEGIN_BASIC_TEXT
List of Contents
  example1 folder: example input file for isumtally=1
  example2 folder: example input file for isumtally=2
  readme-jpn.txt: Instruction written in Japanese (this file)
  old-sumtally folder: old version of sumtally program

1.概要
  複数のタリー結果を足し合わせるsumtally機能を実行するためのサンプルインプットファイルです。

2.使い方
 1. [parameters]セクションにおいてicntl=13とする
 2. 足しあわせたいタリー結果のファイルを用意し、
  そのタリー条件が書かれたタリーセクションにおいてsumtally subsectionを設定する
 3. PHITSを実行

3.内容
  1. example1にあるSumtally.inpは、isumtally=1を用いた手動並列計算用のサンプルインプットです。
 同フォルダにあるresult-1.outとresult-2.outの内容を足しあわせ、
 これらの計算を一つのインプットファイルで計算した場合と同様の結果を得ることができます。
 2. example2にあるSumtally.inpは、isumtally=2を用いた加重平均を計算するサンプルインプットです。
 z=5cm-15cmの位置にある標的に対しz=0cmの位置から照射した結果result-l.outと
 z=20cmの位置から照射した結果result-r.outを2:3の比率で足しあわせます。
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: example1/calc1/Sumtally.inp
FILE: example1/calc2/Sumtally.inp
FILE: example1/Sumtally.inp
FILE: example2/calc1/Sumtally.inp
FILE: example2/calc2/Sumtally.inp
FILE: example2/Sumtally.inp
FILE: old-sumtally/sumtally.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: old-sumtally/src/sumtally.f
FILE: old-sumtally/sumtally_mac.command
FILE: old-sumtally/sumtally_win.bat
