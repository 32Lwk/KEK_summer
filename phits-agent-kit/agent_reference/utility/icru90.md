# Utility: icru90

SOURCE_FOLDER: D:/NEAgit/utility/icru90
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: icru90
UTILITY_PATH_INDEX: utility/icru90
UTILITY_FOLDER_NAME: icru90

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/icru90
BASIC_FILE_COUNT: 1
BASIC_FILE: readme.txt
BASIC_FILE_TYPE: txt
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 0

[BASIC_FILES]
FILE: readme.txt
BEGIN_BASIC_TEXT
How to use ICRU90 stopping power

1. for proton & carbon ion
  Set dedxfile = ***_icru90.txt, where *** should be
  water_liquid, graphite, or air

2. for electron and positron
  Set epstfl in [parameters] section, then
  PHITS automatically finds liquid water, graphite, and air
  in the [material] section, and use density correction
  factor defined in ICRU90 for those materials.

  The criterions to judge the materials are
  liquid water: a material composed by H and O with density between 0.9 and 1.1 g/cm3
  graphite: a material composed by only C with density between 1.55 and 2.40 g/cm3
  air: a material composed by C, N, O, and Ar with density below 0.03 g/cm3, which can be changed by gasegs parameter
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: icru90.inp

[BONUS_TEXT_FILES]
NOTE: None
