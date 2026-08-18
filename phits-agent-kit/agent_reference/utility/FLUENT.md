# Utility: FLUENT

SOURCE_FOLDER: D:/NEAgit/utility/FLUENT
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: FLUENT
UTILITY_PATH_INDEX: utility/FLUENT
UTILITY_FOLDER_NAME: FLUENT

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/FLUENT
BASIC_FILE_COUNT: 1
BASIC_FILE: readme.txt
BASIC_FILE_TYPE: txt
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 3
BONUS_TEXT_COUNT: 2

[BASIC_FILES]
FILE: readme.txt
BEGIN_BASIC_TEXT
README file for how to use a coupling function between PHITS and Fluent

PHITS-Fluent_coupling-jp.docx : Japanese manual for how to use PHITS-Fluent
PHITS-Fluent_coupling-en.docx : English manual for how to use PHITS-Fluent

Fluent/
  |
  |---import_src.c : C source file to import OpenFOAM file
  |---import_src.inp : Input file to import OpenFOAM file
  |---msh2bdf.c : C Source file to convert msh to bdf
  |---msh2bdf.inp : Input file to convert msh to bdf
  |---sample_phits_r1.bdf : NASTRAN bulkdata tetra geom. file
  |---sample_phits_r1_asc.cas.gz : ANSYS Fluent case file
  |---sample_phits_r1_asc.msh : Mesh file created by ANSYS Meshing

PHITS/
  |
  |---phits.out : PHITS output file
  |---sample_phits_r1.bdf : NASTRAN bulkdata tetra geom. file
  |---Tetra_test1_deposit.foam : Deposit energy OpenFOAM file
  |---Tetra_test1_deposit.out : Deposit energy text file
  |---Tetra_test1_trackXZ.eps : Particle track EPS file
  |---Tetra_test1_trackXZ.out : Particle track text file
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: Fluent/import_src.inp
FILE: Fluent/msh2bdf.inp
FILE: PHITS/Tetra_test1.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: Fluent/import_src.c
FILE: Fluent/msh2bdf.c
