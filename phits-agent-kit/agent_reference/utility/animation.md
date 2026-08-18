# Utility: animation

SOURCE_FOLDER: D:/NEAgit/utility/animation
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: animation
UTILITY_PATH_INDEX: utility/animation
UTILITY_FOLDER_NAME: animation

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/animation
BASIC_FILE_COUNT: 2
BASIC_FILE: readme-eng.txt
BASIC_FILE_TYPE: txt
BASIC_FILE: readme-jpn.txt
BASIC_FILE_TYPE: txt
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 4
BONUS_TEXT_COUNT: 5

[BASIC_FILES]
FILE: readme-eng.txt
BEGIN_BASIC_TEXT
List of Contents
  readme-eng.txt: Instruction written in English
  readme-jpn.txt: Instruction written in Japanese (this file)
  animation.inp: Sample input file of PHITS for making animation
  phits.out: Standard PHITS output generated from 'animation.inp'
  track.out: Text output from [t-track] with time mesh
  track.eps: Graphical output from [t-track] with time mesh (20 pages)
  track.gif: GIF animation converted from track.eps
  ezfig.com-gif-make.gif: Cropped GIF animation converted from track.gif
  ezfig.com-gif-make(1).gif: Slow-down GIF animation converted from ezfig.com-gif-make.gif
  logo2021 folder: Another example for making logo animation
  imagemagick folder: Instruction for create animation using Imagemagick (not supported anymore)

Instructions for how to animate the motions of particles simulated by PHITS using online tools
(Please see 'imagemagick' folder if you want to use imagemagick)

1. Execute PHITS
  Make PHITS input file havig [t-track] or [t-deposit] tally with time mesh
  Execute PHITS using the input file, and create EPS file having several pages
  (see 'animation.inp' in detail)

2. Convert track.eps to track.gif using online converter
   https://www.onlineconverter.com/eps-to-gif

3. Adjust GIF animation using EZGIF.com (optional)
   https://ezgif.com/crop    (for cropping)
   https://ezgif.com/speed   (for adjusting speed)
END_BASIC_TEXT

FILE: readme-jpn.txt
BEGIN_BASIC_TEXT
List of Contents
  readme-eng.txt: Instruction written in English
  readme-jpn.txt: Instruction written in Japanese (this file)
  animation.inp: Sample input file of PHITS for making animation
  phits.out: Standard PHITS output generated from 'animation.inp'
  track.out: Text output from [t-track] with time mesh
  track.eps: Graphical output from [t-track] with time mesh (20 pages)
  track.gif: GIF animation converted from track.eps
  ezfig.com-gif-make.gif: Cropped GIF animation converted from track.gif
  ezfig.com-gif-make(1).gif: Slow-down GIF animation converted from ezfig.com-gif-make.gif
  logo2021 folder: Another example for making logo animation
  imagemagick folder: Instruction for create animation using Imagemagick (not supported anymore)

オンラインツールを用いたPHITS出力のGIFアニメーション化
(Imagemagickを使った方法は、imagemagickフォルダを参照、ただし最新版での動作未確認)

1. PHITSを実行する
  [t-track]や[t-deposit]タリーで時間メッシュ(t-type)を導入し,
  フラックスや発熱量の時間変化を出力する(track.out, animation.inpを参照)

2. onlineconverter.comを利用してEPSファイルをGIFアニメーションに変換する
   https://www.onlineconverter.com/eps-to-gif

3. 不要な部分を削除(Crop)したり、アニメーションスピードを変更させたい場合は
   EZGIF.COM(下記URL)を利用する
   https://ezgif.com/crop
   https://ezgif.com/speed
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: animation.inp
FILE: imagemagick/animation.inp
FILE: logo2021/animation.inp
FILE: rotate3dshow/rotate3dshow.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: imagemagick/readme-eng.txt
FILE: imagemagick/readme-jpn.txt
FILE: rotate3dshow/readme-eng.txt
FILE: rotate3dshow/readme-jpn.txt
FILE: rotate3dshow/rotate3dshow.py
