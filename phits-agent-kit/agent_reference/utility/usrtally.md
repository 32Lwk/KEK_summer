# Utility: usrtally

SOURCE_FOLDER: D:/NEAgit/utility/usrtally
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: usrtally
UTILITY_PATH_INDEX: utility/usrtally
UTILITY_FOLDER_NAME: usrtally

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/usrtally
BASIC_FILE_COUNT: 2
BASIC_FILE: readme-en.docx
BASIC_FILE_TYPE: docx
BASIC_FILE: readme-jp.docx
BASIC_FILE_TYPE: docx
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 10
BONUS_TEXT_COUNT: 33

[BASIC_FILES]
FILE: readme-en.docx
BEGIN_BASIC_TEXT
Examples of usrtally.f and [t-userdefined]
[t-userdefined] is very useful when you would like to deduce physical quantities that cannot be directly calculated by the implemented tallies of PHITS. It also enables users to output the particle transport information in the format of other codes such as ROOT. In order to use "usrtally.f", users must revise it and re-compile PHITS by themselves, but it is very difficult to revise the program without the detailed knowledge of the PHITS source code. Thus, we provide examples of "usrtally.f" that work similar to several tallies such as [t-deposit], [t-cross], [t-product] and [t-interact].
The procedure for using these examples are as follows:
copy "usrtally.f" in the zip file to that in "src" folder, and recompile PHITS.
execute the re-compiled PHITS using "usrtally.inp" in each folder, and check the equivalence between the last value written in "userdefined.out" and the result of each tally.
revise "usrtally.f" and "usrtally.inp" for your own purpose
Details of each "usrtally.f" are written in readme-en.docx in each folder. If you have any request to develop other examples of "usrtally.f", please let us know.
Important notice!
usrtally.f developed before PHITS version 3.22 may not be compatible with the later version because of the change of memory usage in PHITS. In that case, you have to revise your usrtally.f as follows:
1.Delete (or comment out) the definitions below:
common /ipomp0/ipomp,npomp
!$OMP THREADPRIVATE(/ipomp0/)
2.Change the definition of common/randtp/ as below:
integer*8 :: iransb64 ! S.H. xorshift (2020.2.6)
common /randtp/ rijk,rans,ranb, iransb64
!$OMP THREADPRIVATE(/randtp/)
3.Replace (no) by (no,ipomp+1), e.g.
e(no) -> e(no,ipomp+1)
xc(no) -> xc(no,ipomp+1)
Notes on Using OpenMP
When performing parallel computation with OpenMP options, make sure to carefully check whether any newly added variables in usrtally.f should be declared as THREADPRIVATE (or as PRIVATE/SHARED/REDUCTION, etc.). The subroutine usrtally is called from analyz.f, but immediately before the call, an !$OMP CRITICAL section is placed to ensure that multiple threads do not execute the contents of usrtally simultaneously. If higher parallel performance is required, you may remove the CRITICAL section around the call site and instead implement proper thread-safety measures inside usrtally.f itself (e.g., by specifying variable attributes, using REDUCTION, or applying minimal CRITICAL/ATOMIC/LOCK constructs where needed). Be sure to confirm that no data races or order dependencies occur when removing the CRITICAL section.
END_BASIC_TEXT

FILE: readme-jp.docx
BEGIN_BASIC_TEXT
ユーザー定義タリー[t-userdefined]の使い方に関する例題
ユーザー定義タリー[t-userdefined]は、通常のタリーでは得ることができない様々な物理量をタリーする機能です。ユーザー定義タリーを使うためには,各ユーザーが,自分の目的に合わせてusrtally.fファイルを変更し,PHITSを再コンパイルする必要があります。ただし,その変更には,FORTRANとPHITSの変数に関する知識が必要なため,ユーザーが自力で行うことは極めて困難でした。そこで,いくつかのタリーと似たような機能を持ち,かつそれに関連するイベント情報を全て書き出すusrtally.fの例題を作りましたので,ぜひご活用下さい。
使い方の手順は以下の通りです。
各フォルダのusrtally.fをsrcフォルダにあるusrtally.fと入れ替えて再コンパイル
各フォルダのusrtally.inpを再コンパイルしたPHITSで実行し,userdefined.outの最後に出力された値とサンプルタリー結果が一致することを確認する(サンプルタリーがある場合)
usrtally.fやusrtally.inpを自分の目的に合わせて変更する。
詳細は,各フォルダのreadme-jp.docxをご参照下さい。また,これら以外にも作ってほしい例題がありましたら,PHITS事務局までご連絡下さい。
注意点!
PHITS 3.22以降、メモリの使用方法が変更になったため、過去に作ったusrtally.fが動作しない可能性があります。その際は、以下の手順に従ってプログラムを修正してください。
1.以下の定義文を削除
common /ipomp0/ipomp,npomp
!$OMP THREADPRIVATE(/ipomp0/)
2.commonブロック randtpを使っている場合は、以下のように変更。
integer*8 :: iransb64 ! S.H. xorshift (2020.2.6)
common /randtp/ rijk,rans,ranb, iransb64
!$OMP THREADPRIVATE(/randtp/)
3.引数(no)を(no,ipomp+1)に置換。以下、その例を示す。
e(no) -> e(no,ipomp+1)
xc(no) -> xc(no,ipomp+1)
OpenMP使用時の注意!
OpenMP のオプションで並列計算を行う場合は、usrtally.f を修正する際に、追加した変数を THREADPRIVATE にすべきか(あるいは PRIVATE/SHARED/REDUCTION などの属性にすべきか)を十分に確認してください。サブルーチンusrtallyはanalyz.fから呼び出されますが、その直前に !$OMP CRITICAL 区間を設けており、複数のスレッドが同時に usrtally 内の処理を実行しないようにしています。より高い並列性能が必要な場合は、呼び出し側の CRITICAL 区間を外し、代わりに usrtally.f 内で適切にスレッド安全化(例:変数属性の明示、REDUCTION の利用、必要最小限の CRITICAL/ATOMIC/LOCK の使用)を施してください。CRITICAL を外す場合は、データ競合や順序依存が生じないことを必ず確認してください。
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: ChemCode/phits.inp
FILE: DNAdamage/phits.inp
FILE: scinful-qmd/ResponseFunction.inp
FILE: scinful-qmd/ResponseFunction_PlasticScinti.inp
FILE: t-cross/usrtally.inp
FILE: t-deposit-event/usrtally.inp
FILE: t-deposit/usrtally.inp
FILE: t-interact/usrtally.inp
FILE: t-product/usrtally.inp
FILE: trajectory/userdefined.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: ChemCode/ChemCode.bat
FILE: ChemCode/ChemCode.sh
FILE: ChemCode/chemmode.f90
FILE: ChemCode/mod/BranchingRatio.csv
FILE: ChemCode/mod/DiffusionCoefficients.csv
FILE: ChemCode/mod/modChemical.f90
FILE: ChemCode/mod/modhead.f90
FILE: ChemCode/mod/modPhysicoChem.f90
FILE: ChemCode/mod/modrandom.f90
FILE: ChemCode/mod/ReactionRadius.csv
FILE: ChemCode/readme-eng.txt
FILE: ChemCode/readme-jpn.txt
FILE: ChemCode/usrtally.f90
FILE: DNAdamage/DNAdamage.bat
FILE: DNAdamage/DNAdamage.sh
FILE: DNAdamage/mod/modclesions.f90
FILE: DNAdamage/mod/moddamageSDD.f90
FILE: DNAdamage/mod/modrandom.f90
FILE: DNAdamage/readme-eng.txt
FILE: DNAdamage/readme-jpn.txt
FILE: DNAdamage/tsmode.f90
FILE: DNAdamage/usrtally.f90
FILE: scinful-qmd/usrtally.f90
FILE: t-cross/usrtally.f90
FILE: t-deposit-event/usrtally.f90
FILE: t-deposit/usrtally.f90
FILE: t-interact/usrtally.f90
FILE: t-product/usrtally.f90
FILE: trajectory/geometry.vtk
FILE: trajectory/trajectory_neutron.vtk
FILE: trajectory/trajectory_photon.vtk
FILE: trajectory/trajectory_proton.vtk
FILE: trajectory/usrtally.f90
