# Lecture: fluka-user/startup

SOURCE_FOLDER: D:/NEAgit/lecture/fluka-user/startup
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: startup
LECTURE_PATH_INDEX: lecture/fluka-user/startup
PPTX_FILES: flair-startup-en.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: homework1, snowman_original
SECTION_KEYWORDS: (none)

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/fluka-user/startup
LECTURE_PATH_INDEX: lecture/fluka-user/startup
PPTX_FILES: flair-startup-en.pptx
INPUT_DIR_COUNT: 0
MAIN_INPUT_COUNT: 2
SLIDE_COUNT: 29
EXERCISE_SLIDE_COUNT: 0
BONUS_INPUT_COUNT: 0
BONUS_TEXT_COUNT: 1

[MAIN_INPUT_FILES]
- homework1.inp
- snowman_original.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: How to use Flair for PHITS
- SLIDE 02: Installation and Setup
- SLIDE 03: Installation of Flair
- SLIDE 04: Launch Flair
- SLIDE 05: (2) Click “Flair” tab
- SLIDE 06: (6) Only for Windows users …
- SLIDE 07: Installation and Setup
- SLIDE 08: Load PHITS input file in Flair
- SLIDE 09: After loaded PHITS input file, contents are saved in the project file of Flair (*.flair). So loaded PHITS input file rem
- SLIDE 10: /home/user/work/homework1.inp: PHITS input file loaded by Flair
- SLIDE 11: When *.flair is saved with the other name and/or in the other directory, homework1.flair and homework1.pht are generated
- SLIDE 12: (1) Select “Run” tab
- SLIDE 13: Difference between running FLUKA and PHITS
- SLIDE 14: Check output files of PHITS
- SLIDE 15: File extension association (for Windows)
- SLIDE 16: (1) Select “Input” tab
- SLIDE 17: Confirm the updated results
- SLIDE 18: Note: Warning message for Flair project
- SLIDE 19: Installation and Setup
- SLIDE 20: Open Flair Project for FLUKA
- SLIDE 21: (1) Select “Input” tab
- SLIDE 22: Run PHITS by combining *.pht and *.inp
- SLIDE 23: Check Output Files
- SLIDE 24: Installation and Setup
- SLIDE 25: Summary
- SLIDE 26: Notes
- SLIDE 27: FLUKA-PHITS Jargon I
- SLIDE 28: FLUKA-PHITS Jargon II
- SLIDE 29: FLUKA-PHITS Unit

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: homework1.inp
FILE: snowman_original.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
How to use Flair for PHITS
June 2025 revised
phits/lecture/fluka-user/startup
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Installation and Setup
Run PHITS via Flair
Summary
Table of Contents
SPEAKER_NOTES:
「実習」 前の基本的な話から

--- SLIDE 03 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Installation of Flair
For Windows users:
* https://flair.cern/download.html
Install WSL (Windows Subsystem for Linux) by launching Windows Powershell and typing “wsl --install“
Launch WSL
Follow “Only once instructions” for “UBUNTU systems” given in the download page of Flair-CERN*
For Linux users:
Access the download page of Flair-CERN*
Follow the instruction for your Linux system (Fedora, UBUNTSU etc.)
For Mac users:
Access the download page of Flair-CERN*
Follow the instruction for “Mac OsX”

--- SLIDE 04 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Launch Flair
Open WSL       (for Windows) or Terminal (Mac or Linux)
Change directory (cd) to phits/lecture/fluka-user/startup*
Launch Flair in the directory (type “flair”)
Note for Windows users
*Typical locations of the phits directory
Windows: /mnt/c/phits/lecture/fluka-user/startup
Mac: /Users/username/phits/lecture/fluka-user/startup
Linux: /usr/local/phits/lecture/fluka-user/startup
You should NOT use directory under WSL directory (e.g. /home/username) for working directory because it cannot be accessed by command prompt

--- SLIDE 05 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
(2) Click “Flair” tab
(3) Click “Config” button
(4) Click “Phits” category
(1) Start Flair in some directory
Setting to run PHITS in Flair (1)

--- SLIDE 06 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
(6) Only for Windows users …
Replace “mac” by “win” in the exe file names defined in “C:/phits/bin/phits.sh“
Line 14:  PHITS_SINGLE_EXE=phits335_win.exe
If PHITS does not run, please set the absolute path of “phits.sh” in Executable
e.g.,
(5) Set path of PHITS directory
(* Preferences may be initialized when Flair is updated.)
Setting to run PHITS in Flair (2)
Line 20:  PHITS_OMP_EXE=phits335_win_openmp.exe
Line 23:  PHITS_MPI_EXE=phits335_win_mpi.exe
Windows: /mnt/c/phits
Mac: /Users/username/phits
Linux: /usr/local/phits
e.g.,
*The version number (335 in this case) should not be changed
Windows: /mnt/c/phits/bin/phits.sh
Mac: Users/username/phits/bin/phits.sh
Linux: /usr/local/phits/bin/phits.sh

--- SLIDE 07 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Installation and Setup
Run PHITS via Flair
Summary
Table of Contents
SPEAKER_NOTES:
「実習」 前の基本的な話から

--- SLIDE 08 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Load PHITS input file in Flair
(3) Click “Load” button
(1) Click “Input” tab
(4) Select homework.inp and open
MENTIONED_INPUT_NAMES: homework.inp

--- SLIDE 09 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
After loaded PHITS input file, contents are saved in the project file of Flair (*.flair). So loaded PHITS input file remains as it is.
Load PHITS input file in Flair
You can ignore warnings, e.g., “>w> Warning: Card #4,1,1 item 'Al' do not exist”

--- SLIDE 10 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
/home/user/work/homework1.inp: PHITS input file loaded by Flair

/home/user/work/homework1.flair: Project file of Flair
/home/user/work/homework1.pht: PHITS input file generated by Flair*
It is strongly recommended to save the project file of Flair (*.flair) with the same name and in the same directory as loaded PHITS input file.
e.g.)
(* When homework1.flair is saved, homework1.pht is automatically generated according to the contents of homework1.flair.)
Default setting
Save project file of Flair
MENTIONED_INPUT_NAMES: homework1.inp

--- SLIDE 11 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
When *.flair is saved with the other name and/or in the other directory, homework1.flair and homework1.pht are generated in the directory where homework1.inp is located.

*.flair just refers to homework1.flair, and edited contents are saved in homework1.flair.

When *.flair saved in the other directory, it might not be run because homework1.inp is not generated in the directory where *.flair is located.
directory A
directory B
run
*.flair
homework1.flair
homework1.pht
send ./homework1.pht to PHITS
save and update
refer to
failed
return to original directory
Note: Save project file of Flair
MENTIONED_INPUT_NAMES: homework1.inp

--- SLIDE 12 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
(1) Select “Run” tab
(2) Select “Runs” view
(3) Click “Start” button
Run PHITS in Flair

--- SLIDE 13 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Difference between running FLUKA and PHITS
When run PHITS for the first time, status shows “Not Running” even though PHITS run correctly.

--- SLIDE 14 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Check output files of PHITS
[project file name].out: Calculation summary from Flair
[project file name].pht: PHITS input file generated by Flair
phits.out: Calculation summary from PHITS
batch.out: Batch information
track_xz.eps: Image of particle trajectories
track_xz.out: Numerical data of particle trajectories
deposit.eps: Image of depth dose distribution
deposit.out: Numerical data of depth dose distribution
If these files do not exist, please check the setting of Flair.
track_xz.eps

--- SLIDE 15 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
File extension association (for Windows)
PHITS input file created by Flair has an extension of *.pht
It is preferable to associate files with those extensions to PHITS-Pad or Notepad++

Procedures of file association
Right-click the file of interest (input, output, etc.)
「Open with」→ 「Select a program from a list of ….」
Check 「Always use the selected…」 in the dialogue
Select the text editor or Click “Browse” to find the executable file of PHITS-Pad (c:/phits/phitspad/windows-x64/phitspad.exe) or NotePad++ (C:\Program Files\Notepad++ or your user folder)

After association, please confirm that the icons of *.pht files are properly changed to the icon of your selected editor

--- SLIDE 16 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
(1) Select “Input” tab
(2) Select “icntl”
(3) Select “gshow xyz”
(4) Check actual value
(5) Run PHITS using “Run” tab
Edit PHITS input file in Flair

--- SLIDE 17 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Confirm the updated results
icntl = 8 (gshow xyz in flair) is geometry drawning mode
track_xz.eps

--- SLIDE 18 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Note: Warning message for Flair project
Following warning message might appear when you return to Flair window.
Please click “No” during tutorial, otherwise disable sections and user-defined parameters disappear.
(*.flair is overwritten by contents of *.pht.)

--- SLIDE 19 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Installation and Setup
Run PHITS via Flair
Export FLUKA geometry to PHITS
Summary
Table of Contents
SPEAKER_NOTES:
「実習」 前の基本的な話から

--- SLIDE 20 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Open Flair Project for FLUKA
(3) Click “Open” button
(4) Select snowman.flair and open
(1) Click “Flair” tab
*Save “homework1.flair” for future revision
(2) Click “Save” button*
snowman.flair contains the geometry used for phits/lecture/exercise/snowman in FLUKA format

--- SLIDE 21 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
(1) Select “Input” tab
(2) Click “Export”
(3) Select “Phits”
(4) Save as “snowman.pht”
Export to PHITS input file (*.pht)
(5) Select “Yes” only for “Convert Geometry and Materials” & “… use microbodies (RCC, BOX…)”
*You can completely convert FLUKA to PHITS format, but it is irreversible

--- SLIDE 22 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Run PHITS by combining *.pht and *.inp
See phits/lecture/basic/lec03 for “infl” commands
Open “phits/lecture/fluka-user/startup/snowman_original.inp”* by PHITS-Pad or NotePad++ (Not via Flair)
Check “infl:{snowman.pht}” command in the input file
Execute PHITS with snowman_original.inp
Prepare PHITS input file without geometry definitions ([material], [surface] & [cell]) and include *.pht into it
*The file name “snowman.inp” cannot be used because it is interpreted as a FLUKA input file based on the project name “snowman.flair”
MENTIONED_INPUT_NAMES: snowman.inp, snowman_original.inp

--- SLIDE 23 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Check Output Files
track.eps
100 MeV protons are incident to water sphere with 5 cm radius
phits.out, batch.out, deposit.out, track.eps, track.out, track_err.eps, track_err.out are generated

--- SLIDE 24 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Installation and Setup
Run PHITS via Flair
Export FLUKA geometry to PHITS
Summary
Table of Contents
SPEAKER_NOTES:
「実習」 前の基本的な話から

--- SLIDE 25 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Summary
Flair can read and edit PHITS input files and execute PHITS via its GUI.
It can also export geometry from the FLUKA format to the PHITS format (*.pht).
If you are a FLUKA user or want to use Flair exclusively to create PHITS input files, please refer to lec01–03 in the fluka-user folder.
The PHITS support functions in Flair are still under development, and more features will be available in the future.
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 26 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
Notes
Signs in region definitions are opposite in FLUKA and PHITS

The fundamental units for expressing energy are GeV in FLUKA and MeV in PHITS
Pre-defined materials (element, water etc.) are not recognized when a PHITS input file is loaded by Flair
FLUKA: +(include), –(exclude)
PHITS: +(outside or positive), –(exclude or negative)
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 27 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
FLUKA-PHITS Jargon I
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 28 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
FLUKA-PHITS Jargon II
SPEAKER_NOTES:
《休憩はさむ》
まとめ

--- SLIDE 29 ---
PPTX_FILE: flair-startup-en.pptx
SLIDE_TEXT:
FLUKA-PHITS Unit
FLUKA
Energy: GeV
Exceptions:
DPA threshold: eV or GeV
LET: keV(mm g/cm3)
In some cards:
+XXX = momentum GeV/c
-XXX = kinetic energy GeV
Length: cm
Density: g/cm3
Time: s
Angle: deg
Solid Angle: sr
Magnetic Field: Tesla (Tesla/cmn)
Electric Field: kV/cm
Temperature: K
Dose Equivalent: pSv
PHITS
Energy: MeV
Length: cm
Density: g/cm3 or 1024 atoms/cm3
Time: ns
Angle: deg
Solid Angle: sr
Magnetic Field: kG
Electric Field: kV/cm
Temperature: MeV
Dose Equivalent: pSv
SPEAKER_NOTES:
《休憩はさむ》
まとめ

[BONUS_INPUT_FILES]
NOTE: None

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: snowman.flair
