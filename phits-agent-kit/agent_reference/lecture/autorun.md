# Lecture: advanced/autorun

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/autorun
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: autorun
LECTURE_PATH_INDEX: lecture/advanced/autorun
PPTX_FILES: phits-lec-autorun-en.pptx, phits-lec-autorun-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: autorun, density, phits
SECTION_KEYWORDS: anatally, cm, t-track

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/autorun
LECTURE_PATH_INDEX: lecture/advanced/autorun
PPTX_FILES: phits-lec-autorun-en.pptx, phits-lec-autorun-jp.pptx
INPUT_DIR_COUNT: 0
MAIN_INPUT_COUNT: 3
SLIDE_COUNT: 46
EXERCISE_SLIDE_COUNT: 18
BONUS_INPUT_COUNT: 0
BONUS_TEXT_COUNT: 4

[MAIN_INPUT_FILES]
- autorun.inp
- density.inp
- phits.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: PHITS
- SLIDE 02: Purpose
- SLIDE 03: Contents
- SLIDE 04: What is script file?
- SLIDE 05: EXERCISE 1 | Exercise 1: Run a script file
  ANSWER_FILE: (missing)
- SLIDE 06: What is written in eachrun.bat?
- SLIDE 07: phits.inp
- SLIDE 08: EXERCISE 2 | Exercise 2
  ANSWER_FILE: (missing)
- SLIDE 09: EXERCISE 3 | Exercise 3
  ANSWER_FILE: (missing)
- SLIDE 10: EXERCISE 4 | *Backslash is something like        in your keyboard
  ANSWER_FILE: (missing)
- SLIDE 11: EXERCISE 5 | Exercise 5
  ANSWER_FILE: (missing)
- SLIDE 12: Contents
- SLIDE 13: “autorun.bat” & “autorun.sh” in PHITS
- SLIDE 14: EXERCISE 6 | Exercise 6
  ANSWER_FILE: (missing)
- SLIDE 15: EXERCISE 7 | Exercise 7
  ANSWER_FILE: (missing)
- SLIDE 16: Contents
- SLIDE 17: What is [anatally] & ANOVA?
- SLIDE 18: EXERCISE 8 | Exercise 8
  ANSWER_FILE: (missing)
- SLIDE 19: Answer 8
- SLIDE 20: EXERCISE 9 | Exercise 9
  ANSWER_FILE: (missing)
- SLIDE 21: Answer 9
- SLIDE 22: Contents
- SLIDE 23: Script files can significantly reduce your effort on running PHITS simulations for a variety of conditions
- SLIDE 01: PHITS
- SLIDE 02: PHITS入力ファイル内の特定のパラメータ(ci)を連続的に変化させながらPHITSを自動で実行する方法を学習する
- SLIDE 03: 本実習の流れ
- SLIDE 04: スクリプト（script）ファイルって何?
- SLIDE 05: EXERCISE 1 | エクスプローラを開いてphits/lecture/advanced/autorunフォルダに移動
  ANSWER_FILE: (missing)
- SLIDE 06: 実際に実行するコマンド（eachrun.bat/shの中身）
- SLIDE 07: 計算条件（phits.inp）
- SLIDE 08: EXERCISE 2 | 課題２
  ANSWER_FILE: (missing)
- SLIDE 09: EXERCISE 3 | 課題３
  ANSWER_FILE: (missing)
- SLIDE 10: EXERCISE 4 | \マークはUSキーボードだと   こんな感じのキーになる
  ANSWER_FILE: (missing)
- SLIDE 11: EXERCISE 5 | 課題５
  ANSWER_FILE: (missing)
- SLIDE 12: 本実習の流れ
- SLIDE 13: autorun.bat/shの概要
- SLIDE 14: EXERCISE 6 | 課題６
  ANSWER_FILE: (missing)
- SLIDE 15: EXERCISE 7 | 課題７
  ANSWER_FILE: (missing)
- SLIDE 16: 本実習の流れ
- SLIDE 17: [anatally]とANOVAの概要
- SLIDE 18: EXERCISE 8 | 課題８
  ANSWER_FILE: (missing)
- SLIDE 19: 回答８
- SLIDE 20: EXERCISE 9 | 課題９
  ANSWER_FILE: (missing)
- SLIDE 21: 回答９
- SLIDE 22: 本実習の流れ
- SLIDE 23: スクリプトファイルを作成することにより、様々な条件に対してPHITSを実行する際の労力が大幅に削減できる

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: autorun.inp
FILE: density.inp
FILE: phits.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
PHITS
Automated execution of PHITS by changing simulation conditions using script files
Multi-Purpose Particle and Heavy Ion Transport code System
Title
July 2025 revised
/phits/lecture/advanced/autorun
SPEAKER_NOTES:
PHITS講習会 基礎実習

--- SLIDE 02 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
Purpose
Learn how to run multiple PHITS simulations at once by changing a certain parameter
Purpose of This Lecture
Analysis of the energy dependence of nuclear reaction
Shielding calculation by changing the target thickness
Calculation of dose conversion coefficient for various irradiation geometries
For example…
Make script file by yourself,
or use “autorun.bat” or “autorun.sh” with icntl = 16

--- SLIDE 03 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
Contents
Table of Contents
Make your own script files
Use “autorun.bat/sh”
Use [anatally] and ANOVA
Summary

--- SLIDE 04 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
What is script file?
A text file that consists of series of commands to be executed by command-line interpreter or terminal
Windows: Batch file (*.bat)
*Mac/Linux: Shell script (*.sh)
Grammars of batch file and shell script are similar but different
PHITS is executed by phits.bat or phits.sh in “phits/bin” folder
@echo off
title PHITS: %1
set PHITS_Single_EXE="C:\phits/bin/phits324_win.exe“
…
phits.bat
phits.sh
#!/bin/sh
OMP=1
# OMP = 0 -> OpenMP with default OMP_NUM_THREADS
…
If you want to run a different version of PHITS, you must change the executable file name in the script
*When you create a new shell script, you have to add executable status by “chmod u+x *.sh”

--- SLIDE 05 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1: Run a script file
Open “Explore” and move to “phits/lecture/advanced/autorun”
Type “cmd” and press “enter” → terminal window is opened
Type “eachrun.bat” in the terminal window and press “enter”
*Simply double-click “eachrun.bat” also works, but terminal window disappears after the execution
Type “cmd” here
Open “Terminal” and move to “phits/lecture/advanced/autorun”
Type “./eachrun.sh” or “eachrun.sh”
If you encounter “command not found”, type “chmod u+x *.sh” to add executable status for all .sh files and try again
To repeat the same command, press “↑” and “enter”*
*If you press “↑” twice, you can go back two-previous command
Mac
Windows
ANSWER_FILE: (missing)

--- SLIDE 06 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
What is written in eachrun.bat?
1st line: write “PHITS simulation using eachrun.bat” in the terminal
2nd line: write “set:c1[2.3]” into a file named “density.inp”
3rd line: execute PHITS with “phits.inp”
“echo” means write the following message
“>” means “to the following file” (Overwrite if the file exists)
“call” is necessary for running another batch script in a batch script
echo PHITS simulation using eachrun.bat
echo set:c1[2.3] > density.inp
call phits.bat phits.inp
eachrun.bat
echo PHITS simulation using eachrun.sh
echo set:c1[2.3] > density.inp
phits.sh phits.inp
eachrun.sh
Role of each line
Important notices
Example of terminal Window
*To see a batch file, right click the file and “open with” a text editor or “Edit”
*
MENTIONED_INPUT_NAMES: density.inp, phits.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
phits.inp
Basic setup
20 MeV neutron at (0,0,-10) going to +z-axis
Cylindrical concrete with thickness of 50 cm and radius of 10 cm
[t-track] for calculating the effective dose using multiplier function
Source：
Geometry：
Tally：
Important point
Density of concrete is specified by –c1, which is defined in density.inp
track_rz.eps
[ Cell ]
infl:{density.inp}
  1     1 -c1  -10  101  -102
 100    0      -999  #1
 101   -1       999
…
phits.inp
MENTIONED_INPUT_NAMES: density.inp, phits.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
Open eachrun.bat/sh with text editor
Change c1 parameter written in density.inp from 2.3 to 2.0
Save eachrun.bat/sh
Execute eachrun.bat/sh (Press “↑” and “enter” in the terminal)
Change the concrete density from 2.3 g/cm3  to 2.0 g/cm3
echo PHITS simulation using eachrun.bat
echo set:c1[2.3] > density.inp
call phits.bat phits.inp
eachrun.bat
echo PHITS simulation using eachrun.sh
echo set:c1[2.3] > density.inp
phits.sh phits.inp
eachrun.sh
*
*To see a batch file, right click the file and “open with” a text editor
track_rz.eps
0
0
MENTIONED_INPUT_NAMES: density.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 09 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
Exercise 3
Change “c1[2.0]” to “c1[%1]” for Windows, “c1[$1]” for Mac/Linux
Save eachrun.bat/sh
Type “eachrun.bat 3.0” for Windows, “./eachrun.sh 3.0” for Mac/Linux in the terminal
Use variable in the script
echo PHITS simulation using eachrun.bat
echo set:c1[2.0] > density.inp
call phits.bat phits.inp
eachrun.bat
echo PHITS simulation using eachrun.sh
echo set:c1[2.0] > density.inp
phits.sh phits.inp
eachrun.sh
track_rz.eps
%1]
$1]
%1 indicates the 1st argument specified after eachrun.bat (separated by space)
MENTIONED_INPUT_NAMES: density.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 10 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
*Backslash is something like        in your keyboard
Exercise 4
Add commands to “eachrun.bat” or “eachrun.sh” to make a new folder in “eachout” and copy all output files (*.out and *.eps) to the folder
Type “eachrun.bat 2.0” for Windows, “./eachrun.sh 2.0” for Mac/Linux in the terminal
Check eachout/2.0 folder by “explore” or “finder”
Automatically save output files by adding commands to “eachrun.bat/sh”
echo PHITS simulation using eachrun.bat
echo set:c1[%1] > density.inp
call phits.bat phits.inp
mkdir eachout\%1
copy *.out eachout\%1
copy *.eps eachout\%1
eachrun.bat
echo PHITS simulation using eachrun.sh
echo set:c1[$1] > density.inp
phits.sh phits.inp
mkdir -p eachout/$1
cp *.out eachout/$1
cp *.eps eachout/$1
eachrun.sh
“*.out” means all files having the extension of “.out”
Folder name should be separated by
\ (backslash) for batch file*
/ (slash) for shell script
Tips
“-p” after mkdir may not be necessary depending on your environment
MENTIONED_INPUT_NAMES: density.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 11 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Open “multirun.bat” for Windows, “multirun.sh” for Mac/Linux by text editor
Copy the 1st line and paste it by 4 times
Change the number from 2.0 to 2.2, 2.4, 2.6, & 2.8, respectively
Type “multirun.bat” for Windows, “./multirun.sh” for Mac/Linux in the terminal
Check the dependence of concrete density on the attenuation factor
Run PHITS with various conditions at once
call eachrun.bat 2.0
call eachrun.bat 2.2
call eachrun.bat 2.4
call eachrun.bat 2.6
call eachrun.bat 2.8
multirun.bat
multirun.sh
./eachrun.sh 2.0
./eachrun.sh 2.2
./eachrun.sh 2.4
./eachrun.sh 2.6
./eachrun.sh 2.8
2.0 g/cm3
2.2 g/cm3
2.4 g/cm3
2.6 g/cm3
2.8 g/cm3
ANSWER_FILE: (missing)

--- SLIDE 12 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
Contents
Table of Contents
Make your own script files
Use “autorun.bat/sh”
Use [anatally] and ANOVA
Summary

--- SLIDE 13 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
“autorun.bat” & “autorun.sh” in PHITS
Execute PHITS for various conditions by automatically changing a parameter (ci)
Analyze the dependence of tally results on ci using [anatally] (optional)
Original script files are included in phits/bin folder
How to use?
Make a PHITS input file (e.g. phits.inp) with variable ci
Set “icntl = 16” in the PHITS input file
Make a input file for autorun.bat/sh (e.g. autorun.inp) to specify how to change the variable
Run autorun.bat/sh with the input file
PHITS are iteratively executed until the simulations for all conditions are finished, and the results are moved to ‘1’, ‘2’, ‘3’ … folders in “outfiles”
Similar to “multirun.bat/sh”, but you can automatically change the parameter without the knowledge of batch file / shell script
MENTIONED_INPUT_NAMES: autorun.inp, phits.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6
Change “icntl = 16” in phits.inp (script mode)
Type “autorun.bat” for Windows, “autorun.sh” for Mac/Linux in the terminal*
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=1        $ 1: data point, 2: linear, 3: log interpolation
nc=3            $ Number of data points
2.0  2.3  2.8
autorun.inp
phits.inp
[ Parameters ]
 icntl  =  16
 …
Run PHITS with “file=phits.inp“ by changing “set:c1” by “nc=3” times
The format of “c-type” is similar to that of the tally mesh
Calculated results for c1 = 2.0, 2.3 and 2.8 are moved to “1”, “2”, “3” folders in “outfiles”
Variable can be check by varfile.inp in each folder
Run autorun.bat /autorun.sh
*You can specify the input file name as the 1st variable (e.g. autorun.bat autorun.inp)
./ should be removed to be found from the registered path (phits/bin)
MENTIONED_INPUT_NAMES: autorun.inp, phits.inp, varfile.inp
ANSWER_FILE: (missing)

--- SLIDE 15 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Exercise 7
Change c1 from 2.0 to 2.8 by 0.2 step (nc = 5)
Use c-type = 2 ( linear interpolation)
Minimum & maximum values of c1 can be specified by cmin & cmax
Save “autorun.inp” and run “autorun.bat” or “autorun.sh” with autorun.inp
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=1        $ 1: data point, 2: linear, 3: log interpolation
nc=3            $ Number of data points
2.0  2.3  2.8
autorun.inp
Change autorun.inp
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=2        $ 1: data point, 2: linear, 3: log interpolation
nc=5            $ Number of data points
cmin = 2.0
cmax = 2.8
Check the consistency between “outfiles/1” and “eachout/2.0”, … “outfiles/5” and “eachout/2.8”
MENTIONED_INPUT_NAMES: autorun.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 16 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
Contents
Table of Contents
Make your own script files
Use “autorun.bat/sh”
Use [anatally] and ANOVA
Summary

--- SLIDE 17 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
What is [anatally] & ANOVA?
Total uncertainty
(0.5553)
Systematic uncertainty
(0.5481)
Statistical error
(0.0894)
[anatally]: Special tally for analyzing multiple tally results based on ANOVA or user-defined function*.
ANOVA (ANalysis Of VAriance): A collection of statistical models for analyzing the differences among the means.
In PHITS, ANOVA is used for evaluating the systematic uncertainty associated with a certain variable (ci) in the input file
Doses at the end of concrete
ANOVA
*defined in phits/src/usranatal.f. Compilation of PHITS is required when it is changed

--- SLIDE 18 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Exercise 8
→ Check “track_rz_anatally.eps”
Delete “$” for the anatally subsection written in [t-track] of phits.inp
Save “phits.inp” and run “autorun.bat” or “autorun.sh” with autorun.inp
phits.inp
Activate anatally function
[ T-track ]
…
 angel  =  ymax(3.0)  ymin(0.01)
$ anatally start                $ Anatally subsection starts here
$ manatally = 1                 $ Type of Anatally (0: user-defined, 1:ANOVA)
$ sfile=track_rz_anatally.out   $ Anatally output file name
$ anatally end                  $ Anatally subsection ends here
After finishing all simulations, “anatally.inp” is automatically created and executed by PHITS, and the results from ANOVA is output in a file specified by “sfile” parameter
MENTIONED_INPUT_NAMES: anatally.inp, autorun.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 19 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
Answer 8
track_rz_anatally.out
x: z [cm]
y: effective dose [psv/source]
p: xlin ylog afac(0.8) form(0.9)
p: ymax(3.0)  ymin(0.01)
h: n            x            y1(all     ),hh0l   ny21 dy1=[y1*y21]
#  z-lower               z-upper                 all      r.err
   0.0000E+00   1.0000E+00   1.9613E+00  0.0221  0.0210  0.0067
   1.0000E+00   2.0000E+00   2.0248E+00  0.0230  0.0217  0.0077
…
Mean, total, systematic, statistical uncertainties
Only mean and total uncertainties are shown

--- SLIDE 20 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
Exercise 9
Simulations only for 3 conditions (mean & mean ± 1σ) are generally sufficient to evaluate the systematic uncertainty*
Evaluate the total uncertainty when the mean and uncertainty of the concrete density is known to be ρ = 2.3 ± 0.1 (g/cm3)
Try three-condition method
*S. Hashimoto and T. Sato, J. Nucl. Sci. Technol. 56, 345 (2019)
autorun.inp
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=2        $ 1: data point, 2: linear, 3: log interpolation
nc=5            $ Number of data points
cmin = 2.0
cmax = 2.8
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=2        $ 1: data point, 2: linear, 3: log interpolation
nc=3            $ Number of data points
cmin = 2.2
cmax = 2.4
MENTIONED_INPUT_NAMES: autorun.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 21 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
Answer 9
track_rz_anatally.eps
Total uncertainties including systematic uncertainties are not so significant

--- SLIDE 22 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
Contents
Table of Contents
Make your own script files
Use “autorun.bat/sh”
Use [anatally] and ANOVA
Summary

--- SLIDE 23 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
Script files can significantly reduce your effort on running PHITS simulations for a variety of conditions
As for the sample script files, you can select either the combination of “eachrun.bat/sh” and “multirun.bat/sh”, or “autorun.bat/sh”
“autorun.bat/sh” is useful particularly when the systematic uncertainties of a certain variable in PHITS input file must be evaluated
Summary

--- SLIDE 01 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
PHITS
スクリプトファイルを用いた
PHITSの連続実行方法
Multi-Purpose Particle and Heavy Ion Transport code System
2024年12月改訂
/phits/lecture/advanced/autorun
SPEAKER_NOTES:
PHITS講習会 基礎実習

--- SLIDE 02 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
PHITS入力ファイル内の特定のパラメータ(ci)を連続的に変化させながらPHITSを自動で実行する方法を学習する
本実習の目的
原子核反応の入射エネルギー依存性を解析する
遮蔽体の厚さを変化させて最適な遮蔽条件を探査する
照射ジオメトリを変化させて様々な条件に対する線量換算係数を計算する
例えば…
自分自身でスクリプト(script)ファイルを作成する
“autorun.bat” or “autorun.sh”を利用する

--- SLIDE 03 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
本実習の流れ
自作スクリプトファイルの利用方法
autorun.bat/shの利用方法
[anatally]とANOVAの利用方法
まとめ

--- SLIDE 04 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
スクリプト（script）ファイルって何?
コマンドプロンプト（Windows）もしくはターミナル（Mac/Linux）上で実行するコマンド（命令）が書かれたテキストファイル
Windows: バッチファイル (*.bat)
*Mac/Linux: シェルスクリプト (*.sh)
バッチファイルとシェルスクリプトの文法は似ているが多少異なる
PHITSを実行する際に利用している/phits/bin/phits.bat or phits.shもスクリプトファイル
@echo off
title PHITS: %1
set PHITS_Single_EXE="C:\phits/bin/phits324_win.exe“
…
phits.bat
phits.sh
#!/bin/sh
OMP=1
# OMP = 0 -> OpenMP with default OMP_NUM_THREADS
…
別のバージョンのPHITSを利用する場合は、スクリプト内に書かれた実行ファイル名を変更
*シェルスクリプトを新しく作った場合、ターミナル上で “chmod u+x *.sh”と入力して実行権限を与える必要がある

--- SLIDE 05 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
エクスプローラを開いてphits/lecture/advanced/autorunフォルダに移動
フォルダ名入力欄にcmdと書いてenterキーを押す→ コマンドプロンプトが開く
コマンドプロンプト上でeachrun.batと入力してenterキーを押す
単純にeachrun.batをダブルクリックしても実行されるが、実行後にコマンドプロンプトが消えるためエラーが発生しても気づかないので非奨励
ここでcmdと入力してenterキーを押す
ターミナルを開いてcdコマンドを使ってphits/lecture/advanced/autorunに移動
./eachrun.shと入力してenterキーを押す
command not foundというエラーが出る場合はchmod u+x *.shを実行して全てのスクリプトファイルに実行権限を与えて再挑戦
同じコマンドを再度実行したい場合は↑キーを押してenterキーを押すと便利*
*↑キーを２回押せば、２つ前のコマンドが表示される
Mac
Windows
課題１:スクリプトファイルの実行
ANSWER_FILE: (missing)

--- SLIDE 06 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
実際に実行するコマンド（eachrun.bat/shの中身）
1行目: ターミナル上にPHITS simulation using eachrun.batと書き出す
2行目: density.inpというファイルにset:c1[2.3]と書き込む
3行目: このフォルダにあるphits.inpをPHITSで実行する
echoは次に書かれる文言を繰り返す（やまびこ）コマンド
> は、コマンドの実行結果を書き出す先を指定したファイルに変更
callはバッチファイルから別のバッチファイルを呼び出すときに必要（シェルスクリプトでは不要）
echo PHITS simulation using eachrun.bat
echo set:c1[2.3] > density.inp
call phits.bat phits.inp
eachrun.bat
echo PHITS simulation using eachrun.sh
echo set:c1[2.3] > density.inp
phits.sh phits.inp
eachrun.sh
各行の役割
重要ポイント
コマンドプロンプトの例
*バッチファイルの中身を編集する際は右クリックして「編集」もしくは「開く→テキストエディタ（PHITS-Padなど）」を選択
*
MENTIONED_INPUT_NAMES: density.inp, phits.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
計算条件（phits.inp）
基本条件
20MeV中性子（0,0,-10の点より+z方向(dir = 1)に進む
円柱状コンクリート（厚さ50cm、半径10cm）
[t-track]とmultiplier functionを組み合わせた実効線量の深さ分布
線源：
体系：
タリー：
重要ポイント
コンクリートの密度が–c1で指定され、その数値はdensity.inpに書かれている
track_rz.eps
[ Cell ]
infl:{density.inp}
  1     1 -c1  -10  101  -102
 100    0      -999  #1
 101   -1       999
…
phits.inp
MENTIONED_INPUT_NAMES: density.inp, phits.inp

--- SLIDE 08 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
課題２
eachrun.bat/shをテキストエディタで開く*
density.inpに書き出すc1パラメータの値を2.3から2.0に変更
eachrun.bat/shを保存（忘れずに！）
eachrun.bat/shを実行する（ターミナルで↑を押してからenterキーを押す）
コンクリートの密度を2.0g/cm3に変更してPHITSを実行しよう
echo PHITS simulation using eachrun.bat
echo set:c1[2.3] > density.inp
call phits.bat phits.inp
eachrun.bat
echo PHITS simulation using eachrun.sh
echo set:c1[2.3] > density.inp
phits.sh phits.inp
eachrun.sh
track_rz.eps
0
0
*バッチファイルの中身を編集する際は右クリックして「編集」もしくは「開く→テキストエディタ（PHITS-Padなど）」を選択
MENTIONED_INPUT_NAMES: density.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 09 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
課題３
c1[2.0]をWindowsの場合はc1[%1]に、Mac/Linuxの場合はc1[$1]に変更
編集したファイル（eachrun.batもしくはeachrun.sh）を保存
ターミナルでWindowsの場合はeachrun.bat 3.0、Mac/Liuxの場合は./eachrun.sh 3.0と入力して実行
スクリプトファイルで変数を利用しよう
echo PHITS simulation using eachrun.bat
echo set:c1[2.0] > density.inp
call phits.bat phits.inp
eachrun.bat
echo PHITS simulation using eachrun.sh
echo set:c1[2.0] > density.inp
phits.sh phits.inp
eachrun.sh
track_rz.eps
%1]
$1]
%1（もしくは$1）はeachrun.bat/shの後ろにスペース区切りで指定する１つ目の引数
MENTIONED_INPUT_NAMES: density.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 10 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
\マークはUSキーボードだと   こんな感じのキーになる
課題４
PHITS実行後に新しいフォルダeachout\%1を作成し、そのフォルダ内に全ての計算結果（*.out及び*.epsファイル）をコピーするコマンドをeachrun.bat/shに追加
ターミナルでWindowsの場合はeachrun.bat 2.0、Mac/Liuxの場合は./eachrun.sh 2.0と入力して実行
eachout/2.0フォルダの中身をエクスプローラもしくはFinderで確認
計算結果を別フォルダに自動的に保存するようにスクリプトを変更しよう
echo PHITS simulation using eachrun.bat
echo set:c1[%1] > density.inp
call phits.bat phits.inp
mkdir eachout\%1
copy *.out eachout\%1
copy *.eps eachout\%1
eachrun.bat
echo PHITS simulation using eachrun.sh
echo set:c1[$1] > density.inp
phits.sh phits.inp
mkdir -p eachout/$1
cp *.out eachout/$1
cp *.eps eachout/$1
eachrun.sh
*はワイルドカードを表し、例えば*.outは拡張子.outを持つ全てのファイルが対象であることを意味する
フォルダ名を表す記号はWindowsの場合は\マーク、Mac/Linuxの場合は/マークとなる
補足情報
eachrun.shにあるmkdirの-pオプションは不要な場合が多い
MENTIONED_INPUT_NAMES: density.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 11 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
課題５
テキストエディタでmultirun.bat/shを開く
１行目をコピーして４回ペーストする
１つ目の引数（c1の値）を2.0, 2.2, 2.4, 2.6, 2.8として保存する
ターミナルでmultirun.batもしくは./multirun.shと入力して実行
eachoutフォルダに出来た結果（track_rz.eps）を確認
複数のコンクリート密度に対して連続してPHITSを実行しよう
call eachrun.bat 2.0
call eachrun.bat 2.2
call eachrun.bat 2.4
call eachrun.bat 2.6
call eachrun.bat 2.8
multirun.bat
multirun.sh
./eachrun.sh 2.0
./eachrun.sh 2.2
./eachrun.sh 2.4
./eachrun.sh 2.6
./eachrun.sh 2.8
2.0 g/cm3
2.2 g/cm3
2.4 g/cm3
2.6 g/cm3
2.8 g/cm3
ANSWER_FILE: (missing)

--- SLIDE 12 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
本実習の流れ
自作スクリプトファイルの利用方法
autorun.bat/shの利用方法
[anatally]とANOVAの利用方法
まとめ

--- SLIDE 13 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
autorun.bat/shの概要
自動的にciパラメータを変化させてPHITSを連続実行するスクリプト
タリー結果のciパラメータに対する依存性を[anatally]を使って解析 （省略可）
autorun.bat及びautorun.shファイルはphits/binフォルダにある
使用手順
ciパラメータを使うPHITS入力ファイル（例: phits.inp）を作成
そのPHITS入力ファイルのicntlを16に設定
ciパラメータの変化方法を設定するautorun.bat/sh専用の入力ファイル（例: autorun.inp）を作成
ターミナル上でautorun.bat/shを実行
PHITSを連続的に実行し、その計算結果をoutfilesフォルダ内に自動的に作成される ‘1’, ‘2’, ‘3’ …フォルダに移動させる
multirun.bat/shと似たいような目的で使えるが、数多くの条件に対して計算したい場合に便利
MENTIONED_INPUT_NAMES: autorun.inp, phits.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
課題６
phits.inpのicntlを16に変更（autorunモード）
ターミナル上でWindowsの場合は、autorun.bat、Mac/Linuxの場合はautorun.shと入力して実行*
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=1        $ 1: data point, 2: linear, 3: log interpolation
nc=3            $ Number of data points
2.0  2.3  2.8
autorun.inp
phits.inp
[ Parameters ]
 icntl  =  16
 …
fileで定義した入力ファイル（phits.inp）に対して、set:で定義した変数（c1）をnc（=3）回変更してPHITSを実行する。
c-typeの書式はタリーのメッシュ定義方法と同じ。c-type=1の場合は、全ての値を定義する
c1 = 2.0, 2.3, 2.8の結果は、それぞれoutfilesフォルダの “1”, “2”, “3” フォルダに移動される
実際に使ったパラメータ値は、各フォルダにあるvarfile.inpに出力される
autorun.bat/shを使ってPHITSを連続実行しよう
*デフォルト（autorun.inp）以外の条件設定ファイル名の場合は第一引数で指定
登録パス(phits/bin)から検索するため、ここではコマンドの頭に./を付けない。
MENTIONED_INPUT_NAMES: autorun.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 15 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
課題７
c1の値を2.0から2.8まで0.2ステップで５回変更して(nc=5)PHITSを実行する
c-type = 2を使う（線形内挿モード）
c1の最小値と最大値は、それぞれcminとcmax で定義する
autorun.inpを保存し、ターミナル上でautorun.batもしくはautorun.sh”を再実行する
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=1        $ 1: data point, 2: linear, 3: log interpolation
nc=3            $ Number of data points
2.0  2.3  2.8
autorun.inp
autorun.inpを変更して再実行してみよう
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=2        $ 1: data point, 2: linear, 3: log interpolation
nc=5            $ Number of data points
cmin = 2.0
cmax = 2.8
“outfiles/1”と“eachout/2.0”, … “outfiles/5”と“eachout/2.8”に格納された結果が一致していることを確認
MENTIONED_INPUT_NAMES: autorun.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 16 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
本実習の流れ
自作スクリプトファイルの利用方法
autorun.bat/shの利用方法
[anatally]とANOVAの利用方法
まとめ

--- SLIDE 17 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
[anatally]とANOVAの概要
全不確かさ (0.5553)
系統的不確かさ
(0.5481)
統計誤差
(0.0894)
[anatally]: 複数のタリー結果をまとめて解析する専用タリー。ANOVAもしくはユーザーが独自に定義した関数*を使う方法がある
ANOVA (ANalysis Of VAriance): 平均値とその分散について解析する様々な統計モデルを集約したツール
PHITSでは、ANOVAはautorunで変化させたciパラメータの不確実性によるタリー結果の系統誤差を評価する目的で利用
コンクリート背面における実効線量
ANOVA
*phits/src/usranatal.fで定義。変更した場合はPHITSの再コンパイルが必要

--- SLIDE 18 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
課題８
→ 実行が終わったらtrack_rz_anatally.epsを確認
phits.inpの[t-track]に書かれたanatallyサブセクションを有効化（$を消す）
phits.inpを保存し、ターミナルでautorun.batもしくはautorun.shを実行
phits.inp
anatally機能を使ってみよう
[ T-track ]
…
 angel  =  ymax(3.0)  ymin(0.01)
$ anatally start                $ Anatally subsection starts here
$ manatally = 1                 $ Type of Anatally (0: user-defined, 1:ANOVA)
$ sfile=track_rz_anatally.out   $ Anatally output file name
$ anatally end                  $ Anatally subsection ends here
全ての条件に対するPHITS計算が終了した後にanatally.inpが自動的に作成・実行され、ANOVAで解析した結果がsfileで定義したファイルに出力される
MENTIONED_INPUT_NAMES: phits.inp
ANSWER_FILE: (missing)

--- SLIDE 19 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
回答８
track_rz_anatally.out
x: z [cm]
y: effective dose [psv/source]
p: xlin ylog afac(0.8) form(0.9)
p: ymax(3.0)  ymin(0.01)
h: n            x            y1(all     ),hh0l   ny21 dy1=[y1*y21]
#  z-lower               z-upper                 all      r.err
   0.0000E+00   1.0000E+00   1.9613E+00  0.0221  0.0210  0.0067
   1.0000E+00   2.0000E+00   2.0248E+00  0.0230  0.0217  0.0077
…
平均値、全不確かさ、系統的不確かさ、統計誤差
平均値と全不確かさのみepsファイルには表示される

--- SLIDE 20 ---
PPTX_FILE: phits-lec-autorun-en.pptx
EXERCISE_NO: 9
SLIDE_TEXT:
課題９
不確実性のあるパラメータに対して３条件（平均値、及び平均値±1σ）計算すれば、ANOVAにより全不確かさを求められることが分かっている*
コンクリート密度が 2.3 ± 0.1 (g/cm3)と推定できる場合の実効線量の不確かさを評価してみよう
３条件法により不確かさを推定してみよう
*S. Hashimoto and T. Sato, J. Nucl. Sci. Technol. 56, 345 (2019)
autorun.inp
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=2        $ 1: data point, 2: linear, 3: log interpolation
nc=5            $ Number of data points
cmin = 2.0
cmax = 2.8
file=phits.inp  $ PHITS input file name
set:c1          $ Variable parameter
c-type=2        $ 1: data point, 2: linear, 3: log interpolation
nc=3            $ Number of data points
cmin = 2.2
cmax = 2.4
MENTIONED_INPUT_NAMES: autorun.inp, phits.inp
ANSWER_FILE: (missing)

--- SLIDE 21 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
回答９
track_rz_anatally.eps
密度の誤差が± 0.1 (g/cm3) 程度であれば、50cm厚コンクリートの遮蔽能力に大きな不確かさはないことが分かる

--- SLIDE 22 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
本実習の流れ
自作スクリプトファイルの利用方法
autorun.bat/shの利用方法
[anatally]とANOVAの利用方法
まとめ

--- SLIDE 23 ---
PPTX_FILE: phits-lec-autorun-en.pptx
SLIDE_TEXT:
スクリプトファイルを作成することにより、様々な条件に対してPHITSを実行する際の労力が大幅に削減できる
計算する条件が多い場合は、全自動スクリプトファイル“autorun.bat/shを使うと便利
autorun.bat/shとANOVAを使えば、統計誤差のみならず、不確実性のあるパラメータのタリー結果への影響を含めた全不確かさを評価することができる
まとめ

[BONUS_INPUT_FILES]
NOTE: None

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: eachrun.bat
FILE: eachrun.sh
FILE: multirun.bat
FILE: multirun.sh
