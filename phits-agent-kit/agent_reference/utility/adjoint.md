# Utility: adjoint

SOURCE_FOLDER: D:/NEAgit/utility/adjoint
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: adjoint
UTILITY_PATH_INDEX: utility/adjoint
UTILITY_FOLDER_NAME: adjoint

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/adjoint
BASIC_FILE_COUNT: 1
BASIC_FILE: charged/readme.txt
BASIC_FILE_TYPE: txt
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 3
BONUS_TEXT_COUNT: 0

[BASIC_FILES]
FILE: charged/readme.txt
BEGIN_BASIC_TEXT
Using the adjoint mode for charged particle, you can estimate the origin of source particle
reached to a certain location, direction and energy.

*** Difference of the adjoint mode compared with the forward (normal) mode ***
1. Charged particles gain the energy equal to what they should lose in the forward mode,
   as if they had negative stopping power

2. The direction of the magnetic field is assumed to be inversed (mgf = -mgf),
   so charged particles bend to the direction opposite to the forward calculation.

*** Important notice ***
1. Nuclear reaction cannot be considered in this mode. So, cmin(:) is automatically set to 1.0e9

2. [t-deposit] does not work. Only [t-track] and [t-cross] have been tested.

3. deltm (maximum step size of charged particle) should be set to a small value (less than 0.01)
   while confirming that changing this value will not significantly alter the results

4. [magnetic field] works, but [electro magnetic field] does NOT.

5. Stopping power table (dedxfile) should NOT be used.

6. The results are slightly different from the forward calculation due to the change of stopping power
   during a single step of charged particle.

The adjoint mode for charged particle has not been well tested.
Please contact PHITS office if you find any problem or strange behavior in this function.
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: adjoint/AdjointMode.inp
FILE: charged/charged.inp
FILE: forward/ForwardMode.inp

[BONUS_TEXT_FILES]
NOTE: None
