# Utility: SuperMC

SOURCE_FOLDER: D:/NEAgit/utility/SuperMC
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: SuperMC
UTILITY_PATH_INDEX: utility/SuperMC
UTILITY_FOLDER_NAME: SuperMC

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/SuperMC
BASIC_FILE_COUNT: 1
BASIC_FILE: SolidWorks_to_SuperMC-jp.docx
BASIC_FILE_TYPE: docx
PPTX_COUNT: 1
BONUS_INPUT_COUNT: 2
BONUS_TEXT_COUNT: 3

[BASIC_FILES]
FILE: SolidWorks_to_SuperMC-jp.docx
BEGIN_BASIC_TEXT
SolidWorksを使ってSuperMCとの親和性の高いCADファイルを作成するための参考資料
2017/07/11
*.step(*.stp)ファイルをSuperMCで変換できない(「Splineを使っているので変換できない」)場合、下記の手順でファイルをエクスポートする。また、SOLIDWORKSで開いた際に各パーツが<インポート>の状態となっていた場合も下記手順を実施する。なお、ここでは、SOLIDWORKS® Premium2016 x64Edition SP2.0を使用した。
【保存(インポート)方法】
stepファイルを読み込んだ後、インポート診断を行う。「はい」を選択。
必要に応じで、修復を実施する。「全てを修復」を選択。
左上の[OK]を選択。
フィーチャー認識を行う。「はい」を選択。
左上の[OK]を選択。
これで、SOLIDWORKSに形状が認識される。
【step形式の場合】
「指定保存」からSTEP AP203の*.step形式を選択し、「オプション」を開く。
「ソリッド/サーフェスジオメトリ」を選択。「OK」で保存する。
(「3Dカーブフィーチャーのエクスポート」を同時に選択してもよい)
「ワイヤーフレーム」ではSupeMCが読み込めない。
【ACIS(*.sat)形式の場合】
「指定保存」から「オプション」を開く。
「ソリッド/サーフェスジオメトリ」を選択。「OK」で保存する。
「3Dカーブ」を選択するとSuperMCが読み込めない。
以上により、図中のオレンジの線で示したフィレット形状があってもSupeMCで変換できた。
基本的には、ソリッドでエクスポートすると良いようである。
表1 保存形式まとめ
†これが一番シンプルと思われる。
謝辞
本資料は,宇宙航空研究開発機構(JAXA)島﨑一紀氏のご協力のもと,作成いたしました。
[TABLE]
 | STEP AP203(*.step)形式 | ACIS(*.sat)形式
ソリッド/サーフェスジオメトリ | [[[○]]]† | [[[○]]]
ソリッド/サーフェスジオメトリ 及び / 3Dカーブフィーチャーのエクスポート | [[[○]]] | ―
ワイヤーフレーム | × | ―
3Dカーブ | ― | ×
END_BASIC_TEXT

[PPTX_CONTENTS]
FILE: phits-SuperMC-jp.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-SuperMC-jp.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
PHITS
SuperMCを用いたCADジオメトリのPHITS入力形式への変換
Multi-Purpose Particle and Heavy Ion Transport code System
title
1
2017年6月改訂

SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
Purpose
2
実習目的
中国科学院原子力安全研究所が開発する登録制フリーソフトSuperMCを使ってCAD形式のジオメトリをPHITSの入力形式に変換する方法を実習します
SuperMC
PHITS

SPEAKER_NOTES:
「実習」 前の基本的な話から

--- SLIDE 03 ---
注意事項
3
Important Notice
SuperMCはWindows及びLinuxでのみ動作する (ただしLinuxでの動作は未確認)

基本的にはフリーソフトだが,ライセンスの取得には1週間ほど時間を要する。またライセンスは毎年更新する必要がある

変換できるCAD形式は*.sat, *.sab, *.stp, *.step形式のみである

スプライン曲面を利用したセルの変換はできない

--- SLIDE 04 ---
SuperMCのインストール
4
Install
SuperMCの事務局にメールを送る
メールの返信に書かれたFTPサイトにアクセスし,インストーラ及びライセンス同意書などをダウンロード
ライセンス同意書に必要事項を記入する
SuperMCをインストールし,ライセンス要求ファイルを作成する    (この段階ではPHITS形式への変換機能は使えない)
ライセンス同意書及びライセンス要求ファイルをSuperMC事務局にメールで送る
SuperMC事務局よりライセンス許諾ファイルが送られてくる     (この過程で1週間ほど時間を要する場合がある)
SuperMCを起動して,ライセンス許諾ファイルを有効にする
ハンコを押したライセンス同意書をSuperMC事務局に郵送する
詳しくはLicenseフォルダのreadme.docxを参照

--- SLIDE 05 ---
物質ファイルの準備
5
Preparation of compound.txt
このフォルダにあるcompound.txtをSuperMCをインストールしたフォルダのProgram\Modeling\DataBaseにコピー
新しい物質を定義したい場合は,compound.txtをテキストエディタで直接編集する必要がある(将来的には,SuperMCのGUIを使って直接編集できるようにする予定だが,現在はバグのためその機能が使えない)
c =======================
#Teflon
c =======================
cinfo:
c1*mass density:2.15
c2*volume fraction:100%
c3*
c =======================
    6000.50c    0.333333  1.0
    9019.50c    0.666667  1.0
c =======================
->物質名
->物質密度(g/cm3)
->元素.断面積拡張子 相対原子密度
元素の定義方法はZ*1000 + A
JENDL-4.0の拡張子は「.50c」
今のところ重量密度での定義は不可

--- SLIDE 06 ---
CADファイルを開く
6
1
1 Openボタンを押してmodel1.stepを選択
サンプルCADファイルmodel01.stepは,(株)竹中工務店の鈴木正樹様よりご提供いただきました

--- SLIDE 07 ---
セルのPropertyを表示する
7
1
1 1つのセルを左クリックで選択し,右クリック->Property
2 PhysicsタブにあるEdit Material Cardボタンをクリック
2

--- SLIDE 08 ---
使用する物質リストを作成する
8
1
compound.txtで定義した物質がMaterial.libに表示されるので,このジオメトリに必要な物質を選択
「 >> 」ボタンを押して物質をMaterial Listに追加
このジオメトリで利用する全ての物質を追加したらOKボタンを押す
2
3

--- SLIDE 09 ---
物質を選択する
9
Numberをクリックし,セルに対応する物質を選択する
Applyボタンを押す。全てのセルに対してこの手順を繰り返して物質を選択
物質情報を含むジオメトリデータをSuperMCのフォーマット(*.fds形式)で保存する
  (「File」->「Save as」->ファイル名を入力して保存)
1
2
3

--- SLIDE 10 ---
PHITS入力形式に変換する
10
1
Convertメニューを選択
Write PHITSをクリック
Generate void spaceをチェック
出力ファイル名を決めてOKボタンをクリック
2
3
4

--- SLIDE 11 ---
PHITSを実行する
11
出力されたPHITS入力形式(model01.inp)をTeraPadなどテキストエディタ(ノートパットは不可)で確認し,保存する                       (現在のSuperMCは,リターンコードに関するバグがあり保存が必須)
[cell], [surface], [material]セクションを含まないPHITS入力ファイル(phits.inp)を準備し,inflコマンドを使って出力ファイル(model01.inp)を組み込む
phits.inpを入力ファイルとしてPHITSを実行する
[Cell]
1   -2.70000005e+000   ( -2 25 -24)
...
[Surface]
1        C/Z  0.0  -150.00 ...
...
[Material]
m1
     13027.50c     1.00000e+000
...
model01.inp
file=phits.inp
[ T i t l e ]
Sample input for reading SuperMC geometry

[ P a r a m e t e r s ]
 icntl    =          11
...

infl: {model01.inp}
...
phits.inp
-> inflコマンドを使う
  ために必要

--- SLIDE 12 ---
PHITSの結果
12
3dshow.eps
deposit.eps
ictl  = 11
ictl  = 0

--- SLIDE 13 ---
エラー対処方法1
13
例: model01.inp         12 :
   Description of [cell] is wrong
原因: リターンコードの問題が解決されていない
対策: TeraPadでSuperMCの出力ファイルを開いて保存
1.真空のcell定義でエラーが生じる
2.Lost particleが頻発する,もしくは2重定義領域が発生する
例: *** Lost partice in CG/GG *** lost = 1
   nbch ncs no  =  1   13   43
原因: CADデータそのものに隙間や2重定義がある場合が多い
対策: SuperMCで「Preprocess」->「Check」->「Yes」とすれば修正
    される可能性がある。ただし,修正されるとmaterial情報が
    消去されてしまうので注意が必要。

--- SLIDE 14 ---
エラー対処方法2
14
PHITS入力形式に変換する際,変換できないセルがある
例:Error: 2 Cells 1(1) 2(2) contain spline surface, the solids will not be converted
原因: スプライン曲面を使っているためPHITSが対応できない
対策: スプライン曲面を使わないようにCADファイルを修正する
SuperMCでは修正できないのでSolidWorksやSpaceClaimなど市販のCADソフトウェアを利用する必要がある。
SolidWorksを使う場合のCADファイル出力方法に関してはSolidWorks_to_SuperMC-jp.docxを参照
例:特性のセルを変換中に無限ループに陥る,もしくは強制終了される
原因: 1つのセルが複雑すぎてSuperMCで扱える限界を超えてしまっている
対策: Decompose機能を用いて複数のセルに分割する
    「Preprocess」->「Decompose」->分割するセルやレベルを入力->「OK」

--- SLIDE 15 ---
15
SuperMCを使えば,CAD形式のジオメトリをPHITS入力形式に簡単に変換することができる
変換できるCAD形式は*.sat, *.sab, *.stp, *.stepに限定されている
スプライン曲面は変換できない
今後,線源やタリーの設定など,より親和性を高めていく予定
SuperMCとPHITSを組み合わせて計算した結果を発表する場合は,必ず下記の文献も引用して下さい
まとめ
Summary
Y. Wu et al. CAD-based Monte Carlo program for integrated simulation of nuclear system SuperMC, Ann. Nucl. Energy, 82, 161-168 (2015)
END_PPTX_TEXT

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: model01.inp
FILE: phits.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: compound.txt
FILE: License/FirstEmail.txt
FILE: model01.step
