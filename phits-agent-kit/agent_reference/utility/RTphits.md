# Utility: RTphits

SOURCE_FOLDER: D:/NEAgit/utility/RTphits
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: RTphits
UTILITY_PATH_INDEX: utility/RTphits
UTILITY_FOLDER_NAME: RTphits

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/RTphits
BASIC_FILE_COUNT: 1
BASIC_FILE: README.txt
BASIC_FILE_TYPE: txt
PPTX_COUNT: 5
BONUS_INPUT_COUNT: 11
BONUS_TEXT_COUNT: 58

[BASIC_FILES]
FILE: README.txt
BEGIN_BASIC_TEXT
README file for RT-PHITS
***********************************************************************
  Contents of RT-PHITS (Last update 2023/08/25)
***********************************************************************

RT-PHITS/
    |
    |---CHANGELOG.txt : Change Log file
    |---README.txt : README file (this file)
    |---bin/ : Directory containing executable binaries and required libraries
    |---binSAVE/ : Backup of the above binary directory
    |---data/ : Directory containing conversion tables
    |    |
    |    |---FacilityInfo.dat : Facility info. file (for PlanReader4PHITS)
    |    |---HumanVoxelTable.data : Conversion table for CT to material
    |    |---HumanVoxelTable-KumamotoUniv.data : Table made by Kumamoto Univ
    |    |---Material.dat : Material info. file (for Plan2PHITS)
    |    |---RIlist.dat : RI list file (for PET2PHITS)
    |    |---sample.dcm : RT-dose format sample (required for PHITS2DICOM)
    |
    |---RTphitsGUI.exe: Executable for RT-PHITS GUI (for windows)
    |---RTphitsGUI.py : Python script for RT-PHITS GUI
    |---RTphitsGUI.pptx : PowerPoint file for explanation of GUI
    |---RTphits_win.bat : Executable batch file (for Windows)
    |---RTphits_mac.command : Executable shell command file (for Mac)
    |
    |---ct2phits.inp : Input example for CT2PHITS
    |---phits2dicom.inp : Input example for PHITS2DICOM
    |---pet2dicom.inp : Input example for PHITS2DICOM
    |---inputcreater4phits.inp : Input example for PHITS2DICOM
    |---simplesource.inp : Input example for SIMPLE source
    |
    |---phits-lec-RTphits-en.ppt : English PowerPoint file for explanation
    |---phits-lec-RTphits-jp.ppt : Japanese PowerPoint file for explanation
    |---picture/ : Directory for image files for GUI
    |---PSFs/ : Directory for phase space files
    |
    |---src/ : Directory containing source files
    |    |
    |    |---clean_lin.sh : Cleanup shell file (for Linux)
    |    |---clean_mac.sh : Cleanup shell file (for Mac)
    |    |---clean_win.bat : Cleanup batch file (for Windows)
    |    |---comile_lin.sh : Compile shell file (for Linux)
    |    |---comile_mac.sh : Compile shell file (for Mac)
    |    |---comile_win.bat : Compile batch file (for Windows)
    |    |---createctmod.f : CT2PHITS subroutine file
    |    |---createmod.f : InputCreater4PHITS subroutine file
    |    |---createpetmod.f : PET2PHITS subroutine file
    |    |---createplanmod.f : Plan2PHITS subroutine file
    |    |---createroimod.f : ROI2PHITS subroutine file
    |    |---ct2phits.f : CT2PHITS main routine file
    |    |---devicemod.f : InputCreater4PHITS subroutine file
    |    |---dicomdict.h : DICOM header tags
    |    |---dicomlib.c : DICOM library subroutine file
    |    |---dicomlib.h : DICOM library header
    |    |---dicomreader.c : DICOMreader main routine file
    |    |---dvhcreater.c : DVHcreater main routine file
    |    |---fitbiomod.f : PET2PHITS subroutine file
    |    |---inputcreater4phits.c : InputCreater4PHITS main routine file
    |    |---interface.c : interface routine between FORTRAN and C
    |    |---nonwinlib.c : OS dependent subroutine file (for Mac&Linux)
    |    |---osDRexe_lin.cpp : OS dependent subroutine file (for Linux)
    |    |---osDRexe_mac.cpp : OS dependent subroutine file (for Mac)
    |    |---osDRexe_win.cpp : OS dependent subroutine file (for Mac)
    |    |---pet2phits.c : PET2DICOM main routine file
    |    |---phits2dicom.c : PHITS2DICOM main routine file
    |    |---phitslib.c : PHITS library subroutine file
    |    |---phitslib.h : PHITS library header
    |    |---plan2phits.f : Plan2PHITS main routine file
    |    |---planreader4phits.cpp : PlanReader4PHITS main routine file
    |    |---psfsplitter.f : PSFsplitter main routine file
    |    |---readctmod.f : CT2PHITS subroutine file
    |    |---readmod.f : InputCreater4PHITS subroutine file
    |    |---readpetmod.f : PET2PHITS subroutine file
    |    |---readplanmod.f : Plan2PHITS subroutine file
    |    |---readroimod.f : ROI2PHITS subroutine file
    |    |---roi2phits.f : ROI2PHITS main routine file
    |    |---roi2phitscmod.c : ROI2PHITS subroutine file
    |    |---simplesource.f : SimpleSource main routine file
    |    |---stdmod.f : Standard inout module file
    |    |---surflistmod.f : Plan2PHITS subroutine file
    |    |---tablemod.f : CT2PHITS subroutine file
    |    |---utllib.c : Utility library subroutine file
    |    |---utllib.h : Utility library header
    |    |---voxelidmodifier.f : Voxel-ID Modifier main routine file
    |    |---winlib.c: OS dependent subroutine file (for Windows)
    |
    |---work/ : Working directory
    |    |
    |    |---sample1/
    |    |    |---CT/ : Directory containing sample CT data
    |    |    |---DATfiles/ : Directory for intermediate files
    |    |    |---PET/ : Directory containing sample PET data
    |    |    |---PHITSinput/ : Directory for creating PHITS inputs
    |    |    |---ROI/ : Directory containing ROI data in CT image format
    |    |
    |    |---sample2/
    |    |    |---CT/ : Directory containing sample CT data
    |    |    |---DATfiles/ : Directory for intermediate files
    |    |    |---PHITSinput/ : Directory for creating PHITS inputs
    |    |    |---Plan/ : Directory containing sample RT plan
    |    |    |---Structure/ : Directory containing sample RT structure

***********************************************************************
  Introduction
***********************************************************************

RadioTherapy package based on PHITS (RT-PHITS) is a dose
reconstruction package to evaluate radiation dose in various types of
radiotherapy using PHITS simulation. RT-PHITS contains several modules
which are able to convert DICOM data into PHITS format so that PHITS
simulation can be performed using these data.

CT2PHITS is a module to convert CT number to material composition and
density referring to a conversion table specified by CT2PHITS input
file.  The file "HumanVoxelTable.data" contained in data
directory is such a table based on W. Schneider,
Phys. Med. Biol. 45(2000) 459-478.  CT2PHTIS creates PHITS geometry
input of the phantom image using the converted data. Information
needed to reconstruct the object such as pixel numbers, pixel size,
slice thickness etc. is automatically taken from the DICOM CT data.

PHITS2DICOM is a program to conert 3D dose distribution calculated by
PHITS to data in DICOM RT-dose format. RT-dose file is created by
modifying header information and voxel data of the sample RT-dose file
(sample.dcm) located in "data" directory. Necessary information is
extracted from PHITS outputs and RT-image data used in the calculation
and RT-dose file having the same "Frame of Reference UID" with
RT-image is created. Owing to this conversion, dose analysis of 3D
dose distribution by simultanous display with RT-image using general
DICOM viewer softwares such as "dicompyler
(http://www.dicompyler.com)".

PET2PHITS is a module to create radioisotope (RI) source distribution
inside patient body by convertting PET image data. By converting the
patient CT image together with CT2PHITS, the RI source distribution
can be defined on the patient body in PHITS.

IinputCreater4PHITS is a module to create PHITS input file by
combining source and geometry information converted from DICOM data by
other modules. It will create a complete set of the PHITS input
containing [parameters], [source], [surface], [cell], [material],
[t-3dshow], [t-deposit] sections and therefore you can check the
success of the conversion of data by running PHITS with this input.
This sample input could be a good starting point to produce more
practical PHITS inputs fitting your purpose.

SimpleSource is a module to create simple source input.

DICOMreader is a module to read DICOM binary file and display in text.

ROI2PHITS is a module to create region of interest (ROI) voxels by
loading ROI data from RT-structure file or mask image files in CT
format. The voxel dimensions are taken same as the voxel phantoms
adopting from "phantominfo.dat".

DVHcreater is a module to create Dose-Volume histogram (DVH) from
RT-dose files. Partial contributions to the DVH can be also
illustrated by the cumulative bar chart of the DVH by choosing the
partial RT-dose files.

PlanReader4PHITS is a module to read RT-plan DICOM binary file and
produce text intermediate files required for Plan2PHITS.

Plan2PHITS is a module to create beam devicegeometry include files
from intermediate files of PlanReader4PHITS.

PSFsplitter is a module to collect existing phase space files (PSF) and
re-distribute to match MPI parallelization numbers.

Voxel-ID Modifier is a module to modify the Voxel-ID in the voxel
phantoms created by CT2PHITS.

***********************************************************************
  System requirements
***********************************************************************

OS: Windows (XP or higher), Mac (OS X v10.5 or higher), Linux Unix
    etc.

***********************************************************************
  How to RUN RT-PHITS
***********************************************************************
RTphitsGUI.py is a python script for a GUI usage of RT-PHITS.
See details in HowToUseRTphitsGUI.pptx.

Followings are the instruction for CUI use.
-- Windows-------------------------------------------------------------
Drag input file for RT-PHITS (e.g. simplesource.inp, pet2phits.inp,
ct2phits.inp, inputcreater4phits.inp or phits2dicom.inp) and drop into
RTphits_win.bat

or

1. Open COMMAND PROMPT and change directory to RTphits directory

2. Run the programs by

   bin\simplesource_win.exe < simplesource.inp
   bin\pet2phits_win.exe < pet2phits.inp
   bin\ct2phits_win.exe < ct2phits.inp
   bin\inputcreater4phits_win.exe < inputcreater4phits.inp
   bin\phits2dicom_win.exe < phits2dicom.inp

-- Mac ----------------------------------------------------------------
1. Double click RTphits_mac.command in FINDER
   This will pop up TERMINAL and show the following message;
   "Input filename for RTphits ? - Type filename & ENTER -"

3. Type a input filename for RTphits
   (e.g. simplesource.inp, pet2phits.inp, ct2phits.inp,
   inputcreater4phits or phits2dicom.inp) and ENTER
   This will initiate each module

or

1. Open terminal and change directory to RTphits directory

2. Run the programs by

   ./bin/simplesource_mac.exe < simplesource.inp
   ./bin/pet2phits_mac.exe < pet2phits.inp
   ./bin/ct2phits_mac.exe < ct2phits.inp
   ./bin/inputcreater4phits_mac.exe < inputcreater4phits.inp
   ./bin/phits2dicom_mac.exe < phits2dicom.inp

For rare cases, the programs fail to execute showing a message that
the following files (RTphits_mac.command, pet2phits_mac.exe,
ct2phits_mac.exe, inputcreater4phits_mac.exe and phits2dicom_mac.exe)
do not have executable property. This situation can be fixed by adding
executable property to those two file by the following steps.

1. Open terminal
2. Change directory to RTphits directory
3. Type and execute the following line

chmod +x RTphits_mac.command bin/pet2phits_mac.exe \
bin/ct2phits_mac.exe bin/inputcreater4phits_mac.exe bin/phits2dicom_mac.exe

-- Linux --------------------------------------------------------------
1. Open terminal and change directory to RT-PHITS directory

2. Run the programs by

   ./bin/simplesource_lin.exe < simplesource.inp
   ./bin/pet2phits_lin.exe < pet2phits.inp
   ./bin/ct2phits_lin.exe < ct2phits.inp
   ./bin/inputcreater4phits_lin.exe < inputcreater4phits.inp
   ./bin/phits2dicom_lin.exe < phits2dicom.inp

***********************************************************************
  How to WRITE input file for CT2PHITS
  (See also ct2phits.inp which is a sample CT2PHITS input)
  (It may be better to quote characters string by double quotation ")
  (In a very rare case, full path may be required for directory & files)
***********************************************************************

Composed of 9 lines

1. Write in CT2PHITS input at the 1st line to show the file is for
   CT2PHITS

2. Filename of the conversion table. (e.g. "HumanVoxelTable.data")

3. Directory name (path) containing DICOM CT files. (e.g. "work/sample1/CT/")

   DICOM CT data files are automatically extracted from the specified
   directory and the data will be ordered by the slice location
   parameter given in the DICOM header.

4. Setting directory name for the creating intermediate files
   (e.g. "work/sample1/DATfiles/")

5. Specify minimum and maximum slice numbers to analyze

   The number should be specified by the slice number.

6. Setting minimum and maximum pixel numbers for x and y directions.

   This parameter is prepared since DICOM CT data normally contains
   marginal space where no object exists. By clipping out a region
   necessary for simulation from the original image, memory space and
   computational time of the PHITS simulation can be reduced. If you
   do not know the pixel size of your DICOM CT files, it is advisory
   to set small number to maximum pixel numbers and run CT2PHITS
   once. The CT2PHITS output shows the pixel size of your DICOM CT
   files, then you can reset the CT2PHITS input.

7. Setting coarse graining voxel numbers in x, y and z directions.

   If you want to faithfully conduct PHITS simulation with the
   original DICOM CT data resolution, set 1 for all these
   parameters. However, reduction of resolution may be required due to
   limitation of memory space or computational time. In this case, set
   integer number larger than 1 to these parameters. The CT data will
   be averaged over the specified number voxels in each direction
   before converting to PHITS materials. If the parameters are set 2 2
   2, two voxels for each direction is averaged and therefore eight
   voxels in total are averaged. If there is remainder data by
   quotient, remained data is just discarded.

8. Setting a option for the origin:

     0: Center of the converted voxel data is set to the origin
     1: Coordinate info is taken from the DICOM header
        (ImagePositionPatient & ImageOrientationPatient) and the system
        is transformed to this coordinate

***********************************************************************
  How to WRITE input file for PHITS2DICOM
  (See also phtis2dicom.inp which is a sample PHITS2DICOM input)
  (Different from CT2PHITS, should not use quote characters string
  by double quotation)
  (In a very rare case, full path may be required for directory & files)
***********************************************************************

Composed of 9 lines

1. Write in PHITS2DICOM input at the 1st line to show the file is for
   PHITS2DICOM

2. Write the name of sample RT-dose file with PATH
   (Normally data/sample.dcm)

3. Write the name of CT-image file with PATH
   (e.g. work/sample1/CT/60592375)

4. Write the name of 3D dose distribution file with PATH obtained by
   PHITS (e.g. work/sample1/PHITSinput/deposit.out)

5. Write the name of phits.out file with PATH obtained by PHITS
   (e.g. work/sample1/PHITSinput/phits.out)

7. Select option for dose normalization

     0: As it is
     1: Normalizaed into 1 for maximum value)
     2: By given factor multiplied
     3: Normalized at the position of next line by the value

The two lines below are active only when option 2 or 3 is selected at the
line 7.

8. (2 in line 7) Specify the normalization factor
   (3 in line 7) Specify the normalization point (x, y, z) in mm
   (e.g. 0.0 0.0 0.0)

9. (3 in line 7) Give the normalized value
   (e.g. 1.0)

***********************************************************************
  How to WRITE input file for PET2PHITS
  (See also pet2phits.inp which is a sample PET2PHITS input)
  (It may be better to quote characters string by double quotation ")
  (In a very rare case, full path may be required for directory & files)
***********************************************************************

Composed of 9 lines

1. Write in PET2PHITS input at the 1st line to show the file is for
   PET2PHITS

2. Write the name of RI list file name with PATH (Normally data/RIlist.dat)

3. Choose RI listed in RIlist.dat (eg. At-211)

4. On/Off of radiation types, all, photon, electron, positron, alpha;
   0:off, 1:on (e.g. 0 1 0 0 1)

5. Setting directory name for the intermediated files
   (e.g. "work/sample1/DATfiles/")

6. Option for skip reading PET files; 0:off, 1:on
   Option 1 required processed intermediate files

The three lines below are active only when option 1 is selected at the
line 6.

7. Directory name (path) containing DICOM PET files.
   (e.g. "work/sample1/PET/")

8. Specify minimum and maximum slice numbers to analyze

   The number should be specified by the slice number.

9. Setting minimum and maximum pixel numbers for x and y directions.

10. Write the biological decay constant.
    (if < 0: Fitting from PET data)

***********************************************************************
  How to WRITE input file for INPUTCREATER4PHITS
  (See also inputcreater4phits.inp which is a sample)
  (It may be better to quote characters string by double quotation ")
  (In a very rare case, full path may be required for directory & files)
***********************************************************************

Composed of 8 lines

1. Write in INPUTCREATER4PHITS input at the 1st line to show the file is for
   INPUTCREATER4PHITS

2. Setting directory name for the intermediated files
   (e.g. "work/sample1/DATfiles/")

3. Setting directory name for the creating PHITS inputs
   (e.g. "work/sample1/PHITSinput/")

4. Parameter option; 0:default (Only 0 is allowed currently)

6. Maxcas, Maxbch for PHITS simulation

7. Parallelization option; 0:off, 1:on

The line below are active only when option 1 is selected at the
line 7.

8. Number of OpenMP processes, Number of MPI processes

***********************************************************************
  How to WRITE input file for SimpleSource
  (See also simplesource.inp which is a sample of SimpleSource)
  (It may be better to quote characters string by double quotation ")
  (In a very rare case, full path may be required for directory & files)
***********************************************************************

Composed of 8 lines

1. Write in SIMPLE SOURCE input at the 1st line to show the file is for
   SimpleSourse

2. Setting directory name for the intermediated files
   (e.g. "work/DATfiles/")

3. Beam option; 0:100 MeV proton, 1:6MV photon, 2: 190MeV proton SOBP

4. Field size; horizontal and vertical (mm)

6. Off set from center; horizontal and vertical (mm)

7. Source distance from center (mm)

8. Beam direction angle; horizontal and vertical (degree)

***********************************************************************
  How to (RE)COMPILE RT-PHITS (gfortran* and gcc required)

  [Windows and Mac(64bit) executable binaries are already prepared in
   binary directory (bin/) and therefore only Linux users (Mac 32bit
   users) and users who wants to modify source program need this
   process]

***********************************************************************

-- Windows-------------------------------------------------------------
Double click compile.bat in source directory (src/)

NOTE: Double clicking clean.bat in source directory (src/) will remove
      this executable file and other object files created during
      compilation.  You may use this command for cleanup previously
      compiled files.

-- Mac ----------------------------------------------------------------
Open terminal and change directory to the source directory (src/) and
compile the programs by typing

   ./compile_mac.sh

   This will create executable files in binary directory (bin/)

NOTE: ./clean_mac.sh will remove this executable file and other object
      files.  created during compilation.  You may use this command
      for cleanup previously compiled files.

-- Linux --------------------------------------------------------------
Open terminal and change directory to the source directory (src/) and
compile the programs by typing

   ./compile_lin.sh

   This will create executable files in binary directory (bin/)

NOTE: ./clean_lin.sh will remove this executable file and other object
      files.  created during compilation.  You may use this command
      for cleanup previously compiled files.

***********************************************************************
  Acknowledgement
***********************************************************************

DICOM image data contained in work/sample1/CT and PET are provided by
Dr. T. Watabe, Mr. H. Sasaki (Osaka University) and DICOM image data
contained in work/sample2/CT/ is provided by Dr. Y. Koba (QST) through
the courtesy.

***********************************************************************
  Reference
***********************************************************************

T. Sato et al., EJNMMI Physics, 8, 4 (2021)

T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)

***********************************************************************
  Contact
***********************************************************************

Please contact to PHITS User's Office (phits-office@jaea.go.jp) for
questions and bug reports for RTphits.
We are trying to improve our programs by listening to user's voices as
much as possible. Comments are highly welcomed.
END_BASIC_TEXT

[PPTX_CONTENTS]
FILE: phits-lec-RTphits-CUI-en.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-lec-RTphits-CUI-en.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
PHITS
PHITS Tutorial
PHITS simulation using DICOM
(CUI)
Multi-Purpose Particle and Heavy Ion Transport code System
Title
1
Aug. 2023 revised
Please try GUI of RT-PHITS first
(phits-lec-RTphits-GUI-en.pptx)

--- SLIDE 02 ---
Table of Contents
2
Contents
How to use RT-PHITS
Application using RT-PHITS
How to use PHITS2DICOM

SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 03 ---
PHITS simulation using DICOM
3
What is RT-PHITS
RadioTherapy package based on PHITS (RT-PHITS)
Radionuclide Therapy
PHITS
General
DICOM software
Detailed analysis
3D view
DVH analysis
DICOM data(RT-Plan, PET-Image, CT-Image, RT-Structure, RT-Dose)
Radiotherapy
RT-PHITS(Plan2PHITS,  PET2PHITS,  CT2PHITS,  PHITS2DICOM)
PHITS input
Dose distribution
or
or
Phase Space File
InputCreater4PHITS
Intermediate files (Beam geom., Source info, Patient geom., Tally setting)
T. Sato et al., EJNMMI Physics, 8, 4 (2021)
T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)

--- SLIDE 04 ---
SIMPLE SOURCE input      Signature for a SimpleSource input
"work/sample1/DATfiles/"Directory for intermediate files
0                    Source option; 0:100MeV proton, 1:6MV photon, 2:190MeV proton SOBP
100.0 100.0         Field size; Horizontal, Vertical (mm)
0.0 0.0              Offset from center; Horizontal, Vertical (mm)
2000.0               Source distance from center (mm)
0.0 0.0              Beam angle; Horizontal, Vertical (degree)
Simple source creation module (SimpleSource)
4
1. Create the input file (simplesource.inp) => See README for details
SimpleSource HowTo
An intermediate file for the PHITS input is created in the specified intermediate file directory (work/sample1/DATfiles/)
   ・sourceinfo.dat     Intermediate file for source info.
Source option=0: test calculation
negs=0: no EGS, no electron transport
2. Execute
   Windows: Drag simplesource.inp and drop into RTphits.bat
   Mac: Double click RTphits.command and type ct2phits.inp + enter

--- SLIDE 05 ---
DICOM format (Binary)
5
1 Header (Information on time, voxel size etc.)
2 CT values(1,1->2,1->3,1->...->nx-1, ny -> nx, ny)
Data for 1 slice (sample001.dcm)
Several files are contained in one folder to represent an object
cross sectional view
3D view
It is necessary to convert from DICOM to PHITS-input format
(CT value, binary)   (Universe number, text)
What is DICOM

--- SLIDE 06 ---
CT2PHITS input               Signature for a CT2PHITS input
"data/HumanVoxelTable.data"  Conversion table
"work/sample1/CT/"          DICOM files are automatically identified in this directory
"work/sampl1/DATfiles/"     Directory for intermediate files
1 47                         Slices to be used (1<=z<=47)
1 512 1 512                  Clipping (1<=x<=512, 1<=y<=512)
8 8 1                        Coarse graining (Average on 8 times 8 voxels in x and y direction)
0                            Origin: 0:Voxel center 1:DICOM center
Phantom creation module (ct2phits*)
6
Convert from Dicom data to PHITS input format (voxel phantom)
Relation between CT value and material density is defined in data/HumanVoxelTable.data
1. Make an input file for CT2PHITS (ct2phits.inp) Details given in README
2. Execute
   Windows: Drag ct2phits.inp and drop into RTphits.bat
   Mac: Double click RTphits.command and type ct2phits.inp + enter
DICOM2PHITS HowTo
[W. Schneider, Phys. Med. Biol. 45(2000)459-478]
*Rename from dicom2phits

--- SLIDE 07 ---
Outputs of CT2PHITS
7
Intermediate files for PHITS include files were created in the specified directory
                                                               (work/sample1/DATfiles)
      ・CTcell.dat         Definition of phantom region
      ・CTmaterial.dat      Material data
      ・CTmatnamecolor.dat  Material color information
      ・CTuniverse.dat      Universe data for phantom region
      ・CTusrparam.dat     User defined parameters for phantom
      ・CTvoxel.dat        Voxel data converted to PHITS format
CT2PHITS outputs
An intermediate file for PHITS input was created in the specified directory
                                                               (work/sample1/DATfiles)
      ・phantominfo.dat    Phantom information intermediate file

--- SLIDE 08 ---
PHITS include file
Refer to "PHTS Tutorial  for making Voxel Phantom" (phits/lecture/advanced/voxel/phits-lec-voxel-jp.ppt) for details
CT2PHITS output
8
$ Voxel phantom
$ Material universe
 infl:{CTuniverse.inp}
$ Voxel universe
 5000 0 -5000 lat=1 u=5000
     fill= 0:63 0:63 0:46
 infl:{CTvoxel.inp}
$ CT parameters
set: c81[   64]  $ number of x pixel
set: c82[   64]  $ number of y pixel
set: c83[   47]  $ number of z pixel
set: c84[     0.78125] $ unit voxel x
set: c85[     0.78125] $ unit voxel y
set: c86[     0.32700] $ unit voxel z
set: c87[-c81*c84/2] $ smallest x
set: c88[-c82*c85/2] $ smallest y
set: c89[-c83*c86/2] $ smallest z
...
$ Voxel phantom
$ Unit voxel at smallest x & y
 5000 rpp c87 c87+c84 c88 c88+c85...
$ Outer region
   99 so 500
$ Main Space
   97 rpp c87 c87+c81*c84 c88 c88+...
   98 500 rpp c87+c90 c87+c81*c84...
Center of voxel phantom is set at the origin of the XYZ coordinate
Size and number of voxels are automatically adjusted
CTusrparam.dat
CTsurf.dat
Include file command
CTsurf.dat

--- SLIDE 09 ---
Conversion table
Table for human voxel based on W. Schneider, Phys. ...
24                        ! Number of universe di ...
-1000.0d0  -1.21e-3  3    ! Lowest CT value, Dens
-950.0d0   -0.26     10   ! Universe 2
-120.0d0   -0.927    8    ! Universe 3
-82.0d0    -0.958    8    ! Universe 4  NOTE: Den   ...
-52.0d0    -0.985    9    ! Universe 5        [10^...
-22.0d0    -1.012    8    ! Universe 6        [g/...
...
1500.0d0   -1.935    11   ! Universe 24
1600.0d0                  ! Highest CT value for...
#1 Air :: Air density is used     ! Composition
  N   -75.5                       ! Element, Ele...
  O   -23.2                       !
  Ar   -1.3                       !
#2 Lung :: Lung density is used   ! Composition o...
  H    -10.3
  C   -10.5
  N   -3.1
...
e.g. data/HumanVoxelTable.data [Ref. W. Schneider, Phys. Med. Biol. 45(2000)459}
3rd line:Definition of material 1
-1000 -  material 1 < -950
< Smallest CT value of material 1          => Show warning msg. and substitute material l
> Largest CT value of the last material => Show warning msg. and substitute the last material
Conversion table
9

--- SLIDE 10 ---
INPUTCREATER4PHITS input   Signature of a InputCreater4PHITS input
"work/sample1/DATfiles/"  Directory for intermediate files
"work/sample1/PHITSinput/"Directory for PHITS input
0                          Parameter option; 0:default
1000 1                    Maxcas, Maxbch
0                          Parallel setting option; 0:off
PHITS input creation module (InputCreater4PHITS)
10
1. Create the input file(inputcreater4phits.inp)=> See README for details
INPUTCREATER4PHITS HowTo
Create PHITS input (phits.inp) based on intermediate files(phantominfo.dat, sourceinfo.dat)
PHITS input(phits.inp) is created in the specified directory (work/sample1/PHITSinput/)
2. Execute
   Windows: Drag inputcreater4phits.inp and drop into RTphits.bat
   Mac: Double click RTphits.command and type inputcreater4phits.inp + enter
CT***.dat files will be copied into the PHITS input directory with the name CT***.inp

--- SLIDE 11 ---
11
icntl = 11
icntl = 8
CT3D.eps
deposit-xy.eps
Geometry check
Geometry check

--- SLIDE 12 ---
12
CT2phits.inp
CT2PHITS input
"data/HumanVoxelTable.data" ! File for conversion of human voxel data
"work/sample1/CT/"          ! DICOM file directory
"work/sample1/DATfiles/"    ! Directory for intermediate files
2 46                        ! Minimum slice number, Maximum slice number
93 432 134 386              ! Clipping: Nxmin, Nxmax, Nymin, Nymax
8 8 1                       ! Coarse graining: Nxc, Nyc, Nzc
1                           ! Origin 0:Voxel center 1:DICOM center
deposit-xy.eps
Change voxelized region
Region specification
[ Transform ]
$ Transform system according to DICOM header
tr500   -12.00770   -12.00775   -117.80000
        1.00000   0.00000   0.00000
        0.00000   1.00000   0.00000
        0.00000   0.00000   1.00000
     1
Object position is extracted from DICOM header and the object is transformed in this position for origin option = 1
1. Execute CT2PHITS
2. Execute InputCreater4PHITS to reflect phantom info (No need to modify inputcreater4phits.inp)

--- SLIDE 13 ---
Rotation & translation
[transform]
13
n: ID of transformation
x0, y0, z0 : Displacement vector
Rz, Ry, Rx : Elements of rotation matrix
M: Parameter to change the equation of the transformation(The case of M=2 is shown here.)
In the case of M=2,
After making [transform] section, you can use this function by setting trcl=n in [cell], [source], and so on.
[ T r a n s f o r m ]
    Trn     x0   y0   z0   ->z   ->y   ->x   0   0  0   0   0  0   M

--- SLIDE 14 ---
14
icntl = 0
Dose calculation
Example of dose calculation
deposit-xy.eps
unit  = 2
=> MeV/source
Proton 100 MeV
Small deposit energy in air due to low density

--- SLIDE 15 ---
Table of Contents
15
Contents
How to use RT-PHITS
Application using RT-PHITS
How to use PHITS2DICOM

SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 16 ---
1. Execute each module of RT-PHITS using modified inputs as follows
Advanced application
16
Further application
2. Execute PHITS with icntl=8 using phits.inp at the folder work/sample2/PHITSinput
deposit-xy.eps
deposit-xz.eps
ct2phits.inp
DICOM2PHITS input
"data/HumanVoxelTable.data"
"work/sample2/CT/"
"work/sample2/PHITSinput/"
1 126
100 420 150 400
8 8 2
1
simplesource.inp
inputcreater4phits.inp
Execute CT2PHITS
Execute SimpleSource
Execute InputCreater4PHITS
SIMPLE SOURCE input
work/sample2/DATfiles/
1  $ 6MV photon
50.0 50.0 $ 50mm x 50mm
0.0 0.0
2000.0
0.0 0.0
INPUTCREATER4PHITS input
"work/sample2/DATfiles/"
"work/sample2/PHITSinput/"
0
10000 1 $ Increased MAXCAS
0

--- SLIDE 17 ---
Reduce computational time
17
It converts its input file to binary, and re-reads the binary file
Make binary file of voxel phantom prior to the PHITS execution
Purpose
Procedure
1 Insert the following 2 lines in the [Parameters] section
ivoxel = 2                 # Convert the "fill" part of lattice to binary and output to file(18)
file(18) = voxel.bin   # Output file name for binary voxel phantom
2 Execute PHITS -> Binary file was successfully generated!!
3 Change "ivoxel = 1"
ivoxel = 1 # Read the "fill" part of lattice from file(18)
Speed up!
Faster execution
It is better to...
Every time PHITS runs...

--- SLIDE 18 ---
Application: Modification of beam profile
Application: Beam modification
SIMPLE SOURCE input
"work/sample2/DATfiles/"
0
100.0 100.0  Field size(mm)
0.0 0.0      Offset; H V (mm)
2000.0       Source distance(mm)
0.0 0.0      Beam angle: H V (degree)
simplesource.inp
1. Execute SimpleSource
2. Execute InputCreater4PHITS to reflect source info
  (No need to modify inputcreater4phits.inp)
50.0 50.0
What is the change ?
Source Position Change
deposit-xz.eps
18
icntl = 0

--- SLIDE 19 ---
SIMPLE SOURCE input
"work/sample2/DATfiles/"
0
100.0 100.0  Field size (mm)
0.0 0.0      Offset: H V (mm)
2000.0       Source distance (mm)
0.0  0.0     Beam angle; H V (degree)
simplesource.inp
0.0 0.0
0-
90-
-90-
90-
90.0
Application: Modification of beam profile
1. Execute SimpleSource
2. Execute InputCreater4PHITS to reflect source info
  (No need to modify inputcreater4phits.inp)
Application: Change the direction of beam
What is the change ?
-90度
0度
deposit-xz.eps
19
icntl = 0

--- SLIDE 20 ---
Notice for many materials with EGS
20
Preparation of cross-section data for EGS takes very long time if simulation geometry contains many materials (the data for all the materials will be prepared at the beginning of PHITS execution).
For repeated PHITS simulation, it is useful to keep the created cross-section data for EGS not to reconstruct the data at each time
1. Set ipegs=-1at the parameter section and execute PHITS
 => The cross-section data for EGS will be created without transport calculation
2. Set ipegs=2 at the parameter section and execute PHITS
 => Transport calculation will be conducted using the created data
For details, please refer to the parameter section for EGS in PHITS manual
How to
Many materials with EGS

--- SLIDE 21 ---
Table of Contents
21
Contents
How to use RT-PHITS
Application using RT-PHITS
How to use PHITS2DICOM

SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 22 ---
PHITS2DICOM input                      Signature of input file for PHITS2DICOM
data/sample.dcm                        Name of RTdose sample file with PATH
work/sample1/CT/60592375               Name of Rtimage file with PATH used in CT2PHITS
work/sample1/PHITSinput/deposit.out    Name of PHITS 3D dose file with PATH
work/sample1/PHITSinput/phits.out      Name of phits.out file with PATH
work/sample1/DATfiles/                 Directory for intermediate files
1                                      Dose normalization 0:One for max 1:Given below
PHITS2DICOM
22
Convert PHITS output (3D dose distribution) into DICOM RT-dose format
2.. Create input file of PHITS2DICOM (phits2dicom.inp)
PHITS2DICOM HowTo
1. Compute 3D dose distribution by PHTIS
=> Run PHITS with phits.inp in work/PHITSinput by eliminating "OFF" at the last t-deposit
=> 3D dose distribution deposit.out will be created
=> RT-dose format file will be created (work/sample1/PHITSinput/deposit.dcm) dcm extension file
3. Execute PHITS2DICOM
   Windows: Drag phits2dicom.inp and drop into RTphits.bat
   Mac: Double click RTphits.command and type phits2dicom.inp + enter

--- SLIDE 23 ---
Check with DICOM viewer
23
DICOM viewer

--- SLIDE 24 ---
Summary
24
Summary
DICOM data can be converted into PHITS format by using RT-PHITS
Adjustment of source profile is required to fit the situation
PHITS 3D dose distribution output can be converted to RT-dose format by using PHITS2DICOM
Dose analysis of RT-dose by simultaneous display with RT-image using DICOM viewer is feasible
T. Sato et al., EJNMMI Physics, 8, 4 (2021)
T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)
Reference

--- SLIDE 25 ---
Instruction for calculating dose and EQDX using PET/CT data
25
Appendix

--- SLIDE 26 ---
PHITS output files from icntl = 0
ct2phits.inp
pet2phits.inp
Basic Flow
CT data (work/CT)
PET data (work/CT)
Intermediate files (work/DATfiles)
phits.inp
PHITS input files (work/PHITSinput)
voxel_src###.inp
Decaybio.out
CTvoxel.inp
Basic input
Geometry
Source
Biological decay
inputcreater4phits.inp
deposit.out
Total dose
α dose
β dose
deposit_alpha.out
deposit_beta.out
Deposit_MeV.out
Deposition energy
PHITS output files from icntl = 17
EQDX.out
Equi-effective dose
phits2dicom.inp
DICOM RT-dose
deposit.dcm
Deposit_MeV.dcm
(optional)
EQDX.dcm

--- SLIDE 27 ---
PET2PHITS input          # Signature of PET2PHITS
"data/RIlist.dat"        # RI list file
At-211                   # Name of RI listed in RIlist.dat;
0 0 1 0 1                # all, photon, electron, positron, alpha; 0:off 1:on
"work/sample1/DATfiles/" # Intermediate file directory
0                        # Skip reading PET files 0:off 1:on
"work/sample1/PET/"      # PET image directory
1 47                     # Minimum slice number, Maximum slice number
55 145 60 140            # Clipping: Xmin, Xmax, Ymin, Ymax
-1.0                     # Biological decay constant (if <0 Fitting from PET data)
1                        # Source activity is normalized per MBq
RI source creation module (pet2phits)
27
Create [source] section (xyz-mesh source) from PET data
Time-integral activity in Bq.s (voxel_src000.inp)
Time-differential activity in Bq (voxel_src###.inp, ###: time step)
1. Make an input file for PET2PHITS (pet2phits.inp) Details given in README
2. Execute
   Windows: Drag pet2phits.inp and drop into RTphits.bat
   Mac: Double click RTphits.command and type pet2phits.inp + enter
PET2PHITS

--- SLIDE 28 ---
What is EQDX?
28
Features of TAT
Relatively low-dose rate
Non-uniform dose within tumor
RBE ≠ 1
Different therapeutic effect even in the same dose
EQuieffective Dose to X-ray therapy with fraction size X, EQDX, was proposed by ICRU*
S: Surviving fraction
*Bentzen et al. Radiother Oncol. (2012)
Example of EQDX

--- SLIDE 29 ---
29
EQDX can be calculated from α and β doses based on the stochastic microdosimetric kinetic (SMK) model*, using user-defined anatally function in PHITS
*T.Sato & Y.Furusawa, Radiat. Res. 178, 341-356 (2012)
Conversion from dose to EQDX
Recompile PHITS with usranatal.f included in phits/utility/usranatal/smk_tat/src
Edit phits.inp created by RT-PHITS by changing icntl = 0 to 17 to activate anatally mode
Copy [anatally] section written in phits/utility/usranatal/smk_tat/phits.inp to phits.inp
Run re-compiled PHITS with phits.inp

Convert EQDX.out to EQDX.dcm using PHITS2DICOM, if you want to visualize the calculated EQDX distribution by DICOM viewer
Please read phits/utility/usranatal/readme-en.docx in more detail
=> 3D EQDX distribution EQDX.out will be created
Conversion procedures

--- SLIDE 30 ---
Check with DICOM viewer
30
DICOM viewer

--- SLIDE 31 ---
Reference
31
Reference
T.Sato, T. Furuta, Y. Liu, S. Naka, S. Nagamori, Y. Kanai, T. Watabe, Individual Dosimetry System for Targeted Alpha Therapy Based on PHITS Coupled with Microdosimetric Kinetic Model, EJNMMI Physics 8: 4 (2021).
https://ejnmmiphys.springeropen.com/articles/10.1186/s40658-020-00350-7
Some differences between the current model and that described in this paper
Use SMK model instead of MK model
ROI function is not included because there is no fixed format for setting ROI
Open Access!!
Important notice
END_PPTX_TEXT

FILE: phits-lec-RTphits-GUI-en.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-lec-RTphits-GUI-en.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
1
PHITS
PHITS Tutorial
PHITS simulation using DICOM
Multi-Purpose Particle and Heavy Ion Transport code System
8. 2023 revised

--- SLIDE 02 ---
2
What is RT-PHITS
RadioTherapy package based on PHITS (RT-PHITS)
Radionuclide Therapy
PHITS
General
DICOM software
Detailed analysis
3D view
DVH analysis
DICOM data(RT-Plan, PET-Image, CT-Image, RT-Structure, RT-Dose)
Radiotherapy
RT-PHITS(Plan2PHITS,  PET2PHITS,  CT2PHITS,  PHITS2DICOM)
PHITS input
Dose distribution
or
or
Phase Space File
InputCreater4PHITS
Intermediate files (Beam geom., Source info, Patient geom., Tally setting)
T. Sato et al., EJNMMI Physics, 8, 4 (2021)
T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)
PHITS simulation using DICOM

--- SLIDE 03 ---
3
Required Software and Libraries
Python installation
Download & Install (version later than 3.0 is required)
https://www.python.org/
Python Library installation
RT-PHITS GUI requires the python libraries
(pydicom, matplotlib,numpy)
The installation can be easily done by "pip install"
Open "Terminal" or "Command prompt"
Type the following command
	pip install pydicom
	pip install matplotlib
	pip install numpy
(If there is an error, try "py -m pip install" instead of "pip install")
Tkinter library may also need to be installed for systems such as Ubuntu
For Windows, no additional software and libraries are required*.
For other Mac and Linux, Python and its libraries are required.
*If the prepared executable is incompatible, installation is required

--- SLIDE 04 ---
4
Folder structure of RT-PHITS
RT-PHITS/
    |
    |---bin/ : Directory containing executable binaries and required libraries
    |---binSAVE/ : Backup of the above binary directory
    |---data/ : Directory containing data files required for RT-PHITS
    |---picture/: Picture images for GUI
    |---PSFs/: Phase space file directory
    |---RTphitsGUI.py : Python GUI program for RT-PHITS
    |---src/ : Directory containing source files
    |---work/ : Working directories
         |---sample1/
              |---CT/ : Directory containing CT dicom data
              |---DATfiles/ : Directory for intermediate files
              |---PET/ : Directory containing PET dicom data
              |---PHITSinput/ : Directory for creating PHITS inputs
              |---ROI/ : Directory containing ROI dicom data in CT format
         |---sample2/
              |---CT/ : Directory containing CT dicom data
              |---DATfiles/ : Directory for intermediate files
              |---PHITSinput/ : Directory for creating PHITS inputs
              |---Plan/ : Directory containing PLAN dicom data
              |---Structure/ : Directory containing STRUCTURE dicom data

--- SLIDE 05 ---
5
Execution of RT-PHITS
Double-Click "RTphitsGUI.py"
 or type "python RTphitsGUI.py" in "Terminal" or "Command Prompt"
Click to navigate
Set working directory
Click "OK"
Choose working directory
|---work/ : Working directory
         |---sample1/
              |---CT/ : Directory containing CT dicom data
              |---DATfiles/ : Directory for intermediate files*
              |---PET/ : Directory containing PET dicom data
              |---PHITSinput/ : Directory for creating PHITS inputs
              |---ROI/ : Directory for ROI dicom data in CT format
= A working directory containing subdirectories
* Dialog appears to confirm creating a new directory if not exist
Double-Click "RTphitsGUI.exe" (for Windows only)
In case of failing Python execution, use CUI execution of RT-PHITS (phits-lec-Rtphits-CUI-en.pptx)

--- SLIDE 06 ---
6
Tab selector
Indicator
Setting field for each tab
Source
        Source setting
Phantom
        Target setting
Tally
        Choice of tallies
PHITS
        Parameter setting and
        PHITS input creation
PHITS2DICOM
        RT-dose creation
        and dose evaluation
Analysis
        DVH analysis
State of each tab
   Not set
   Done
   Old files are used
RT-PHITS GUI Main Frame
Button to load previous setting at each tab

--- SLIDE 07 ---
7
Setting for "Source"
Click
Three source options:
Simple source
         Simple square plane source
RT-Plan
         Accelerator beam with beam device geometry
         based on RT-Plan DICOM data (CIRT only)
PET
         Radionuclide source based on PET images

--- SLIDE 08 ---
8
Setting for "Source" (Simple source)
Click
Beam choice
For other choices, choose the 1st choice and modify the [source] in the PHITS input later.
Field size
Offset from the center
Beam direction angle
Create Intermediate file "sourceinfo.dat" in "DATfiles" directory
Click
A simple plane source is created by specifying the source information such as field size, beam angle etc.
Source to isocenter distance
State become "   Done" if successful
Push button without change

--- SLIDE 09 ---
9
Setting for "Phantom"
Click
Two phantom options:
Water phantom
         Simple rectangular water phantom
CT image
       Patient geometry is reconstructed by converting
         CT image

--- SLIDE 10 ---
10
1 Header (Information on time, voxel size etc.)
2 CT values(1,1->2,1->3,1->...->nx-1, ny -> nx, ny)
Data for 1 slice (sample001.dcm)
Several files are contained in one folder to represent an object
cross sectional view
3D view
It is necessary to convert from DICOM to PHITS-input format
(CT value, binary)   (Universe number, text)
What is DICOM
CT-Image DICOM format (binary)

--- SLIDE 11 ---
11
Click
Setting for "Phantom" (CT image)
CT-voxel conversion table file
CT image field
Click
Selecting CT image directory, push "Load" to load the CT image files.
Field for loaded CT data and additional setting is shown
Coordinate origin option
Set origin at the center of the voxels
Set origin adopting the DICOM information
Voxel patient geometry is constructed by converting patient's CT images.

--- SLIDE 12 ---
12
Setting for "Phantom" (CT image)
Pixel clipping field
Select min. and max. pixels and slices of CT images to clip unnecessary area to save memory and CPU time.
Click
Slice location can be changed by clicking the map
Coordinate and CT value can be checked by placing mouse pointer on the map
Clipping area is shown by square
Coarse graining setting field
Number of voxels average in x, y, z direction to reduce CPU time for tally outputs (recommended for tests)
  e. g. 4 times 4 voxels in x and y direction
Include files adopting CT info. "CT***.dat"
           is created in "DATfiles" directory
Intermediate file "phantominfo.dat"
is created in "DATfiles" directory
CT image
CT2PHITS
work/sample1

--- SLIDE 13 ---
13
Intermediate files for PHITS include files were created in the specified directory
                                                               (work/sample1/DATfiles)
      ・CTcell.dat         Definition of phantom region
      ・CTmaterial.dat      Material data
      ・CTmatnamecolor.dat  Material color information
      ・CTuniverse.dat      Universe data for phantom region
      ・CTusrparam.dat     User defined parameters for phantom
      ・CTvoxel.dat        Voxel data converted to PHITS format
CT2PHITS outputs
An intermediate file for PHITS input was created in the specified directory
                                                               (work/sample1/DATfiles)
      ・phantominfo.dat    Phantom information intermediate file
Outputs of CT2PHITS

--- SLIDE 14 ---
Refer to "PHTS Tutorial  for making Voxel Phantom" (phits/lecture/advanced/voxel/phits-lec-voxel-jp.ppt) for details
CT2PHITS output
14
$ Voxel phantom
$ Material universe
 infl:{CTuniverse.inp}
$ Voxel universe
 5000 0 -5000 lat=1 u=5000
     fill= 0:63 0:63 0:46
 infl:{CTvoxel.inp}
$ CT parameters
set: c81[   64]  $ number of x pixel
set: c82[   64]  $ number of y pixel
set: c83[   47]  $ number of z pixel
set: c84[     0.78125] $ unit voxel x
set: c85[     0.78125] $ unit voxel y
set: c86[     0.32700] $ unit voxel z
set: c87[-c81*c84/2] $ smallest x
set: c88[-c82*c85/2] $ smallest y
set: c89[-c83*c86/2] $ smallest z
...
$ Voxel phantom
$ Unit voxel at smallest x & y
 5000 rpp c87 c87+c84 c88 c88+c85...
$ Outer region
   99 so 500
$ Main Space
   97 rpp c87 c87+c81*c84 c88 c88+...
   98 500 rpp c87+c90 c87+c81*c84...
Center of voxel phantom is set at the origin of the XYZ coordinate
Size and number of voxels are automatically adjusted
CTusrparam.dat
CTsurf.dat
Include file command
CTcell.dat
PHITS include files

--- SLIDE 15 ---
Table for human voxel based on W. Schneider, Phys. ...
24                        ! Number of universe di ...
-1000.0d0  -1.21e-3  3    ! Lowest CT value, Dens
-950.0d0   -0.26     10   ! Universe 2
-120.0d0   -0.927    8    ! Universe 3
-82.0d0    -0.958    8    ! Universe 4  NOTE: Den   ...
-52.0d0    -0.985    9    ! Universe 5        [10^...
-22.0d0    -1.012    8    ! Universe 6        [g/...
...
1500.0d0   -1.935    11   ! Universe 24
1600.0d0                  ! Highest CT value for...
#1 Air :: Air density is used     ! Composition
  N   -75.5                       ! Element, Ele...
  O   -23.2                       !
  Ar   -1.3                       !
#2 Lung :: Lung density is used   ! Composition o...
  H    -10.3
  C   -10.5
  N   -3.1
...
e.g. data/HumanVoxelTable.data [Ref. W. Schneider, Phys. Med. Biol. 45(2000)459}
3rd line:Definition of material 1
-1000 -  material 1 < -950
< Smallest CT value of material 1          => Show warning msg. and substitute material l
> Largest CT value of the last material => Show warning msg. and substitute the last material
Conversion table
15
Conversion table

--- SLIDE 16 ---
16
Setting for "Tally"
Selection of tallies (Put check to activate*)
3D dose distribution
Same dimension and resolution as CT image will be created if CT image option is selected
* All tallies are created but not activated without check. You can activate manually but removing "off" in the PHITS input file.
2D dose distribution at voxel center
Intermediate file "tallyinfo.dat" is created in "DATfiles" directory
Click
Click

--- SLIDE 17 ---
17
Setting for "PHITS"
Input checker
Status of "source", "phantom", "tally" tabs can be checked.
By clicking buttons, previous processed intermediate files can be loaded and checked.
Number of histories field
"maxcas" and "maxbch" for PHITS can be specified
Parallel setting field
With and without parallelization
   Number of OpenMP threads
   Number of MPI processes
Parameter option field
Automatically selected according to source
Custom (read from specified file)
Click
InputCreater4PHITS
Create a PHITS input file "phits.inp" in "PHITSinput" directory adopting the intermediate files
(sourceinfo.dat, phantominfo.dat, tallyinfo.dat)
in "DATfiles" directory
Directory for creating PHITS input files
Push button without change

--- SLIDE 18 ---
18
PHITS execution
All the required input files, "phits.inp", include files, and other files, are created in "PHITSinput" directory.
Tally output files ("***.out") and EPS files ("***.eps") will be created in the same directory.
Execute PHITS within "PHITSinput" directory
PHITSiput directory
PHITSiput directory
High-performance computer
Copy "PHITSinput" directory
Copy "***.out" and "***.eps"
Execute PHITS
Method 1
Method 2
Analysis
Click

--- SLIDE 19 ---
19
icntl = 11
icntl = 8
CT3D.eps
deposit-xy.eps
Geometry check
Geometry check
Open work/sample1/PHITSinput/phits.inp
Change the icntl parameter & execute PHITS

--- SLIDE 20 ---
20
deposit-xy.eps
Region specification
Change voxelized region
Click
Click after the change
Clipping region is indicated by the box
1. Change parameter in "Phantom" tab & execute CT2PHITS
2. Execute InputCreater4PHITS in "PHITS" tab to reflect the change into PHITS input
3. Open work/sample1/PHITSinput/phits.inp. Change to icntl=8 & execute PHITS
icntl = 8
93    432
134  386
2      46
DICOM center

--- SLIDE 21 ---
21
Dose calculation
deposit-xy.eps
unit  = 2
=> MeV/source
Proton 100 MeV
Small deposit energy in air due to low density
Dose distribution in transport calculation
Open work/sample1/PHITSinput/phits.inp. Change icntl=0 & execute PHITS

--- SLIDE 22 ---
22
Setting for "PHITS2DICOM"
CT image directory
"phits.out" file
3D dose distribution tally output file
Dose normalization options
As it is

Max to 1

By norm. factor

By dose at point
No additional factor is considered N=1.0
Normalized such that the max. dose to be 1.0
Normalized by a given factor*
Normalized by a specified value at specified point**
* Previous norm. factor can be loaded by this button
** Load dose normalization info from "sourceinfo.dat" available only for RT-Plan source
Click
Click
Convert PHITS 3D dose distribution into RT-dose
PHITS input/output directory

--- SLIDE 23 ---
23
Setting for "PHITS2DICOM"
PHITS2DICOM
RT-dose file list field
RT-dose file was created by converting the 3D dose output file. The created file name is taken same as 3D dose output file but with changed suffix "dcm".
      e.g. deposit.out => deposit.dcm
Created RT-dose file will be listed
Reset list button
List of RT-dose files in "PHITSinput" directory is displayed by clicking this button
Check RT-dose file button

--- SLIDE 24 ---
24
Setting for "PHITS2DICOM"
Double-click
Dose distribution
Coordinate and dose value can be checked by placing mouse pointer on the map
Slice location can be changed by clicking the map
Color setting field
Linear-scale and log-scale for the color map can be chosen.
Max. and min. are automatically adjusted unless they are specifically defined.
work/sample1

--- SLIDE 25 ---
25
Summary
DICOM data can be converted into PHITS format by using RT-PHITS
Adjustment of source profile is required to fit the situation
PHITS 3D dose distribution output can be converted to RT-dose format by using PHITS2DICOM
Dose analysis of RT-dose by simultaneous display with RT-image using DICOM viewer is feasible
T. Sato et al., EJNMMI Physics, 8, 4 (2021)
T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)
Reference
Summary

--- SLIDE 26 ---
Instruction for calculating dose and EQDX using PET/CT data
26
Appendix

--- SLIDE 27 ---
PHITS output files from icntl = 0
ct2phits.inp
pet2phits.inp
Basic Flow
CT data (work/CT)
PET data (work/CT)
Intermediate files (work/DATfiles)
phits.inp
PHITS input files (work/PHITSinput)
voxel_src###.inp
Decaybio.out
CTvoxel.inp
Basic input
Geometry
Source
Biological decay
inputcreater4phits.inp
deposit.out
Total dose
α dose
β dose
deposit_alpha.out
deposit_beta.out
Deposit_MeV.out
Deposition energy
PHITS output files from icntl = 17
EQDX.out
Equi-effective dose
phits2dicom.inp
DICOM RT-dose
deposit.dcm
Deposit_MeV.dcm
(optional)
EQDX.dcm

--- SLIDE 28 ---
28
Setting for "Source" (PET)
Click
RI list file (can be changed if necessary)
Selection of RI source from pull-down menu
Radiation type selection
PET image field
Selecting PET image directory, push "Load" to load the PET image files.
          => Field for loaded PET data
	and additional setting is shown
Click
Activity distribution of radionuclide source is defined based on PET images.

--- SLIDE 29 ---
29
Setting for "Source" (PET)
Click
Loaded PET data & additional setting field
Pixel clipping field
Select min. and max. pixels and slices of PET images to clip unnecessary area to save memory and CPU time.
Field to check PET image (optional)
Biological decay constant field
Set directory of CT image associated with the PET image and click "View" to check activity distribution on the CT image.
Color map is automatically adjusted by the min. and max. value of the PET data.
Linear and logarithmic scale can be selected.
Two options
Biological decay constant at each voxel can be adopted by fitting the time evolution of activity distribution (at least 3 time frame required)
Use a common constant for all voxels by specified value in the following box

--- SLIDE 30 ---
30
Setting for "Source" (PET)
Activity distribution map
Clipping area is shown by square
Time frame of PET image can be changed
Slice location can be changed by clicking the map
Coordinate and PET value can be checked by placing mouse pointer on the map
Intermediate file "sourceinfo.dat"
Activity (Bq) data file "bqdata.dat"
Biological decay data file "decaybio.dat"
is created in "DATfiles" directory
Click
PET2PHITS
55   145
60   140
1      47
Then execute InputCreater4PHITS at PHITS tab
[Souce] section data in xyz-mesh format is created
Time integrated activity in Bq.s (voxel_src000.inp)
Time differenciated activity in Bq (voxel_src###.inp, ###: time step)
MBq normalization

--- SLIDE 31 ---
What is EQDX?
31
Features of TAT
Relatively low-dose rate
Non-uniform dose within tumor
RBE ≠ 1
Different therapeutic effect even in the same dose
EQuieffective Dose to X-ray therapy with fraction size X, EQDX, was proposed by ICRU*
S: Surviving fraction
*Bentzen et al. Radiother Oncol. (2012)
Example of EQDX

--- SLIDE 32 ---
32
EQDX can be calculated from α and β doses based on the stochastic microdosimetric kinetic (SMK) model*, using user-defined anatally function in PHITS
*T.Sato & Y.Furusawa, Radiat. Res. 178, 341-356 (2012)
Conversion from dose to EQDX
Recompile PHITS with usranatal.f included in phits/utility/usranatal/smk_tat/src
Edit phits.inp created by RT-PHITS by changing icntl = 0 to 17 to activate anatally mode
Copy [anatally] section written in phits/utility/usranatal/smk_tat/phits.inp to phits.inp
Run re-compiled PHITS with phits.inp

Convert EQDX.out to EQDX.dcm using PHITS2DICOM, if you want to visualize the calculated EQDX distribution by DICOM viewer
Please read phits/utility/usranatal/readme-en.docx in more detail
=> 3D EQDX distribution EQDX.out will be created
Conversion procedures

--- SLIDE 33 ---
Check with DICOM viewer
33
DICOM viewer

--- SLIDE 34 ---
Reference
34
Reference
T.Sato, T. Furuta, Y. Liu, S. Naka, S. Nagamori, Y. Kanai, T. Watabe, Individual Dosimetry System for Targeted Alpha Therapy Based on PHITS Coupled with Microdosimetric Kinetic Model, EJNMMI Physics 8: 4 (2021).
https://ejnmmiphys.springeropen.com/articles/10.1186/s40658-020-00350-7
Some differences between the current model and that described in this paper
Use SMK model instead of MK model
ROI function is not included because there is no fixed format for setting ROI
Open Access!!
Important notice
END_PPTX_TEXT

FILE: HowToUseRTphitsGUI.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: HowToUseRTphitsGUI.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
1
PHITS
PHITS Tutorial
How to use RT-PHITS GUI
Multi-Purpose Particle and Heavy Ion Transport code System
Mar. 2024 revised

--- SLIDE 02 ---
2
Required Software and Libraries
Python installation
Download & Install (version later than 3.0 is required)
https://www.python.org/
Python Library installation
RT-PHITS GUI requires the python libraries
(pydicom, matplotlib,numpy)
The installation can be easily done by "pip install"
Open "Terminal" or "Command prompt"
Type the following command
	pip install pydicom
	pip install matplotlib
	pip install numpy
(If there is an error, try "py -m pip install" instead of "pip install")
Tkinter library may also need to be installed for systems such as Ubuntu
For Windows, no additional software and libraries are required*.
For other Mac and Linux, Python and its libraries are required.
*If the prepared executable is incompatible, installation is required

--- SLIDE 03 ---
3
Additionally libraries may be needed to install
Most of the cases these are already installed
Installation examples for Ubuntu are given
Python Tkinter library

Python PIL

Python PIP
apt install python3-pil python3-pil.imagetk
apt install python3-tk
apt install python3-pip

--- SLIDE 04 ---
4
Folder structure of RT-PHITS
RT-PHITS/
    |
    |---bin/ : Directory containing executable binaries and required libraries
    |---binSAVE/ : Backup of the above binary directory
    |---data/ : Directory containing data files required for RT-PHITS
    |---picture/: Picture images for GUI
    |---PSFs/: Phase space file directory
    |---RTphitsGUI.py : Python GUI program for RT-PHITS
    |---src/ : Directory containing source files
    |---work/ : Working directories
         |---sample1/
              |---CT/ : Directory containing CT dicom data
              |---DATfiles/ : Directory for intermediate files
              |---PET/ : Directory containing PET dicom data
              |---PHITSinput/ : Directory for creating PHITS inputs
              |---ROI/ : Directory containing ROI dicom data in CT format
         |---sample2/
              |---CT/ : Directory containing CT dicom data
              |---DATfiles/ : Directory for intermediate files
              |---PHITSinput/ : Directory for creating PHITS inputs
              |---Plan/ : Directory containing PLAN dicom data
              |---Structure/ : Directory containing STRUCTURE dicom data

--- SLIDE 05 ---
5
Execution of RT-PHITS
Double-Click "RTphitsGUI.py" (for Windows only)
Type "python RTphitsGUI.py" or "python3 RTphitsGUI.py"
   in "Terminal" or "Command Prompt"
Click to navigate
Set working directory
Click "OK"
Choose working directory
|---work/ : Working directory
         |---sample1/
              |---CT/ : Directory containing CT dicom data
              |---DATfiles/ : Directory for intermediate files*
              |---PET/ : Directory containing PET dicom data
              |---PHITSinput/ : Directory for creating PHITS inputs
              |---ROI/ : Directory for ROI dicom data in CT format
= A working directory containing subdirectories
* Dialog appears to confirm creating a new directory if not exist
Double-Click "RTphitsGUI.exe" (for Windows only)

--- SLIDE 06 ---
6
Tab selector
Indicator
Setting field for each tab
Source
        Source setting
Phantom
        Target setting
Tally
        Choice of tallies
PHITS
        Parameter setting and
        PHITS input creation
PHITS2DICOM
        RT-dose creation
        and dose evaluation
Analysis
        DVH analysis
State of each tab
   Not set
   Done
   Old files are used
RT-PHITS GUI Main Frame
Button to load previous setting at each tab

--- SLIDE 07 ---
7
Setting for "Source"
Setting for "Phantom"
Setting for "Tally"
Setting for "PHITS"
Setting for "PHITS2DICOM"
Setting for "Analysis"
How to use RT-PHITS

--- SLIDE 08 ---
8
Setting for "Source"
Click
Three source options:
Simple source
         Simple square plane source
RT-Plan
         Accelerator beam with beam device geometry
         based on RT-Plan DICOM data (CIRT only)
PET
         Radionuclide source based on PET images

--- SLIDE 09 ---
9
Setting for "Source" (Simple source)
Click
Beam choice
For other choices, choose the 1st choice and modify the [source] in the PHITS input later.
Field size
Offset from the center
Beam direction angle
Create Intermediate file "sourceinfo.dat" in "DATfiles" directory
Click
A simple plane source is created by specifying the source information such as field size, beam angle etc.
Source to isocenter distance
State become "   Done" if successful
work/sample1

--- SLIDE 10 ---
10
Setting for "Source" (RT-plan)
Click
Facility specific information file
Accelerator beam with beam device geometry is reconstructed based on RT-plan DICOM data.
RT-plan file
Click
Sub-window is opened to show parameters of beam devices
PlanReader4PHITS
Plan.dat: RT-Plan info.
Block-**.dat
FLC-**.dat
MLC-**.dat
PatientSetup-**.dat
Port-**.dat
RangeCompensator-**.dat
RangeShifter-**.dat
Load RT-plan file and produce intermediate files
Beam device info.
is created in "DATfiles" directory
** is the serial number of beams defined in RT-plan
work/sample2

--- SLIDE 11 ---
11
Setting for "Source" (RT-plan)
RT-plan info field
Serial beam selector
Beam info. tab
Parameters for each device
are shown and can be modified
Button for save modification (optional)
RT-plan sub-window
RT-plan info field
Button to confirm
work/sample2

--- SLIDE 12 ---
12
Setting for "Source" (RT-plan)
RT-plan info field
Beam list field
Double-click
Beam normalization is loaded
You can modify the beam list by copy and paste by "right-click" the list.
Push "Apply Plan Modification" to load the modified beam list.
Beam tab will be changed
Beam list modification (optional)
work/sample2

--- SLIDE 13 ---
13
Setting for "Source" (RT-plan)
Beam parameter modification (optional)
Gantry angle check window
Beam device check window
Display on/off of each device can be controlled by check box
work/sample2

--- SLIDE 14 ---
14
Setting for "Source" (PET)
Click
RI list file (can be changed if necessary)
Selection of RI source from pull-down menu
Radiation type selection
PET image field
Selecting PET image directory, push "Load" to load the PET image files.
          => Field for loaded PET data
	and additional setting is shown
          Applicable to PET/SPECT files
          (Applicable to multi-frame file since PET2PHITS ver. 4.00)

By clicking "From Intermediate Files", you can load the previous processed files and skip this process.
Click
Activity distribution of radionuclide source is defined based on PET images.
work/sample1

--- SLIDE 15 ---
15
Setting for "Source" (PET)
Click
Loaded PET data & additional setting field
Pixel clipping field
Select min. and max. pixels and slices of PET images to clip unnecessary area to save memory and CPU time.
Field to check PET image (optional)
Biological decay constant field
Set directory of CT image associated with the PET image and click "View" to check activity distribution on the CT image.
Color map is automatically adjusted by the min. and max. value of the PET data.
Linear and logarithmic scale can be selected.
Two options
Biological decay constant at each voxel can be adopted by fitting the time evolution of activity distribution (at least 3 time frame required)
Use a common constant for all voxels by specified value in the following box
work/sample1
Source activity normalization option field
As it is : activity is assumed as it is
Per MBq : activity is normalized per MBq

--- SLIDE 16 ---
16
Setting for "Source" (PET)
Pixel clipping field
Select min. and max. pixels and slices of PET images to clip unnecessary area to save memory and CPU time.
Activity distribution map
Clipping area is shown by square
Time frame of PET image can be changed
Slice location can be changed by clicking the map
Coordinate and PET value can be checked by placing mouse pointer on the map
Intermediate file "sourceinfo.dat"
Activity (Bq) data file "bqdata.dat"
Biological decay data file "decaybio.dat"
is created in "DATfiles" directory
Click
(pettmpparam.dat, pettmpdata.dat) are also created, which can be used to skip loading PET image for next run
PET2PHITS
work/sample1

--- SLIDE 17 ---
17
Setting for "Source"
Setting for "Phantom"
Setting for "Tally"
Setting for "PHITS"
Setting for "PHITS2DICOM"
Setting for "Analysis"
How to use RT-PHITS

--- SLIDE 18 ---
18
Setting for "Phantom"
Click
Two phantom options:
Water phantom
         Simple rectangular water phantom
CT image
       Patient geometry is reconstructed by converting
         CT image

--- SLIDE 19 ---
19
Setting for "Phantom" (Water Phantom)
Click
Phantom size [mm]
Isocenter depth [mm]
Isocenter shift [mm]
Tally grid size
A simple rectangular water phantom is created according to parameters.
work/sample1

--- SLIDE 20 ---
20
Click
Setting for "Phantom" (CT image)
CT-voxel conversion table file
CT image field
Click
Selecting CT image directory, push "Load" to load the CT image files.
Field for loaded CT data and additional setting is shown
Coordinate origin option
Set origin at the center of the voxels
Set origin adopting the DICOM information
Voxel patient geometry is constructed by converting patient's CT images.
work/sample1

--- SLIDE 21 ---
21
Setting for "Phantom" (CT image)
Pixel clipping field
Select min. and max. pixels and slices of CT images to clip unnecessary area to save memory and CPU time.
Click
Slice location can be changed by clicking the map
Coordinate and CT value can be checked by placing mouse pointer on the map
Clipping area is shown by square
Coarse graining setting field
Number of voxels average in x, y, z direction to reduce CPU time for tally outputs (recommended for tests)
  e. g. 4 times 4 voxels in x and y direction
Click
Include files adopting CT info. "CT***.dat"
           is created in "DATfiles" directory
Intermediate file "phantominfo.dat"
is created in "DATfiles" directory
CT image
CT2PHITS
work/sample1

--- SLIDE 22 ---
22
Voxel-ID Modifier (optional)
work/sample1
Voxel-ID modifier is a module to modify IDs of a part of voxel phantom created by CT2PHITS according to ROI file.
Click
Sub-window is opened for ROI setting
Voxel-ID Modifier setting field is opened
Directory of converted ROI files (PHITSinput)
ROI file
New universe ID number

--- SLIDE 23 ---
23
ROI setting
ROI format option
From RT-structure file

From ROI data in CT-image format
RT-structure file needs to be specified
Directory for ROI data needs to be specified
ROI2PHITS
ROI setting sub-window
ROI file list field
Converted ROI file will be listed
Button to check ROI list
ROI file list is loaded from roiinfo.dat file
Double-click*
Voxel format ROI files "ROIvoxel_***.inp"are produced in "PHITSinput" directory with the ROI name ***.  For CT-image format one file "ROIvoxel.inp" is produced.
ROI file list "roiinfo.dat" is also created
ROI distribution
work/sample1
The file is set to the ROI file box in Voxel-ID Modifier setting field
* By double-click of right button of mouse, the file will be set to the ROI file box without opening ROI distribution window

--- SLIDE 24 ---
24
Voxel-ID Modifier setting
Voxel-ID Modifier
Chang the voxel-ID to the new universe number for voxels with number more than 0 in the ROI file.
If a new universe ID number does not exist in universe list of voxel phantom, the new additional definition in CTuniverse.dat and CTmaterial.dat are required.
Click

--- SLIDE 25 ---
25
Setting for "Source"
Setting for "Phantom"
Setting for "Tally"
Setting for "PHITS"
Setting for "PHITS2DICOM"
Setting for "Analysis"
How to use RT-PHITS

--- SLIDE 26 ---
26
Setting for "Tally"
Selection of tallies (Put check to activate*)
3D dose distribution
Same dimension and resolution as CT image will be created if CT image option is selected
* All tallies are created but not activated without check. You can activate manually but removing "off" in the PHITS input file.
Selection of beam device tallies
Active only if RT-plan source option is selected
Click
Intermediate file "tallyinfo.dat" is created in "DATfiles" directory
work/sample1

--- SLIDE 27 ---
27
Setting for "Source"
Setting for "Phantom"
Setting for "Tally"
Setting for "PHITS"
Setting for "PHITS2DICOM"
Setting for "Analysis"
How to use RT-PHITS

--- SLIDE 28 ---
28
Setting for "PHITS"
Input checker
Status of "source", "phantom", "tally" tabs can be checked.
By clicking buttons, previous processed intermediate files can be loaded and checked.
Number of histories field
"maxcas" and "maxbch" for PHITS can be specified
Parallel setting field
With and without parallelization
   Number of OpenMP threads
   Number of MPI processes
Parameter option field
Automatically selected according to source
Custom (read from specified file)
Click
InputCreater4PHITS
Create a PHITS input file "phits.inp" in "PHITSinput" directory adopting the intermediate files
(sourceinfo.dat, phantominfo.dat, tallyinfo.dat)
in "DATfiles" directory
Directory for creating PHITS input files
work/sample1

--- SLIDE 29 ---
29
Setting for "PHITS" for RT-plan source
Click
Beam device material information file
Plan2PHITS
Create beam geometry include files "PLAN***.inp" in "PHITSinput" directory based on beam device info.
 (Plan.dat, Block-**.dat, FLC-**.dat, MLC-**.dat, PatientSetup-**.dat, Port-**.dat, RangeCompensator-**.dat, RangeShifter-**.dat)
in "DATfiles" directory
work/sample2

--- SLIDE 30 ---
30
Setting for "PHITS" for RT-plan source
Phase space file setting field
Click
Load phase space files
Beam device info. "Plan.dat", "Poat-**.dat" are loaded and the list of phase space files required by the serial beams and found in the PSFs directory is created.
Ctrl + Click to select files
PSFsplitter
Combine phase space files prepared in PSFs directory and create phase space files required by the serial beams in "PHITSinput" directory. Phase space files for each MPI processes are separately prepared for MPI parallelization. in "DATfiles" directory.
work/sample2
Only small phase space file are prepared in RT-PHITS package to test. Need to download complete phase space files. The web-site is under construction.
     (Please check https://phits.jaea.go.jp/).

--- SLIDE 31 ---
31
Setting for "PHITS" for PET source
PET source instance field
Select
Select PET source time frame for the default option.
You can change the time frame by manually modifying the obtained PHITS input later.
The option 0 is a special one, which accounts the time-integrated source considering the biological and physical decays.
work/sample1

--- SLIDE 32 ---
32
PHITS execution
All the required input files, "phits.inp", include files, and other files, are created in "PHITSinput" directory.
Tally output files ("***.out") and EPS files ("***.eps") will be created in the same directory.
Execute PHITS within "PHITSinput" directory
PHITSiput directory
PHITSiput directory
High-performance computer
Copy "PHITSinput" directory
Copy "***.out" and "***.eps"
Execute PHITS
Method 1
Method 2
Analysis
Click

--- SLIDE 33 ---
33
Setting for "Source"
Setting for "Phantom"
Setting for "Tally"
Setting for "PHITS"
Setting for "PHITS2DICOM"
Setting for "Analysis"
How to use RT-PHITS

--- SLIDE 34 ---
34
Setting for "PHITS2DICOM"
CT image directory
"phits.out" file
3D dose distribution tally output file
Dose normalization options
As it is

Max to 1

By norm. factor

By dose at point
No additional factor is considered N=1.0
Normalized such that the max. dose to be 1.0
Normalized by a given factor*
Normalized by a specified value at specified point**
* Previous norm. factor can be loaded by this button
** Load dose normalization info from "sourceinfo.dat" available only for RT-Plan source
Click
Click
Convert PHITS output into RT-dose
PHITS input/output directory
work/sample1

--- SLIDE 35 ---
35
Setting for "PHITS2DICOM"
PHITS2DICOM
RT-dose file list field
RT-dose file was created by converting the 3D dose output file. The created file name is taken same as 3D dose output file but with changed suffix "dcm".
      e.g. deposit.out => deposit.dcm
Created RT-dose file will be listed
Reset list button
List of RT-dose files in "PHITSinput" directory is displayed by clicking this button
Check RT-dose file button
work/sample1

--- SLIDE 36 ---
36
Setting for "PHITS2DICOM"
Double-click
Dose distribution
Coordinate and dose value can be checked by placing mouse pointer on the map
Slice location can be changed by left-clicking the map
Color setting field
Linear-scale and log-scale for the color map can be chosen.
Max. and min. are automatically adjusted unless they are specifically defined.
work/sample1
Dose distribution in 2D

--- SLIDE 37 ---
37
Setting for "PHITS2DICOM"
Right-click on the map opens the dose profile window along the lines
work/sample1
Dose profile
The dose profile will be exported in text file (ex. profile.out) in "PHITSinput".
With "up", "down", "left", and "right" arrow keys of the keyboard, the dose profile positions in the dose distribution can be adjusted.
Dose profile

--- SLIDE 38 ---
38
Setting for "PHITS2DICOM"
work/sample1
2D map on general plane window
Dose distribution on general plane

--- SLIDE 39 ---
39
Setting for "PHITS2DICOM"
work/sample1
Point 1
Point 2
Point 3
x
x
x
Define the drawing plane by two vectors
Set range specification
Yellow box: automatically computed values
Red box: contains errors need to modify
Geometry of the drawing plane in 3D
Dose distribution on general plane
Rotation of the drawing plane can be applied by the buttons

--- SLIDE 40 ---
40
Setting for "PHITS2DICOM"
work/sample1
Another way to define the drawing plane is to set "two points" by SHIFT + left click on 2D figures
1. Reset the values
2. Set two points by SHIFT + left click
Point 1
Point 2
Point 3 is automatically selected to satisfy orthogonality to the vector (point2-point1)
* Range is also automatically selected to cover the selected 2D figure
Dose distribution on general plane

--- SLIDE 41 ---
41
Setting for "PHITS2DICOM"
3D dose distribution tally output file
If the tally file contains more than one particle contribution
e.g. part = all 12C alpha proton
RT-dose file for each contribution was created separately. The created file name is chosen as the output file name + "_***" before suffix "dcm" where *** is the part parameter.
      e.g. deposit.out =>
deposit_all.dcm
deposit_12C.dcm
deposit_alpha.dcm
deposit_proton.dcm
PHITS2DICOM
work/sample2
Dose distribution with various particle contribution

--- SLIDE 42 ---
42
Setting for "PHITS2DICOM"
RuntimeWarning: More than 20 figures have been opened.
...
You can open several files together to compare distributions. But it may consume too much memory if you open too many files and you may see the following warning
Total dose distribution
Primary particle (12C) dose distribution
work/sample2
Dose distribution with various particle contribution

--- SLIDE 43 ---
43
Setting for "Source"
Setting for "Phantom"
Setting for "Tally"
Setting for "PHITS"
Setting for "PHITS2DICOM"
Setting for "Analysis"
How to use RT-PHITS

--- SLIDE 44 ---
44
Setting for "Analysis"
RT-dose file for DVH analysis
Partial contribution option
ROI setting field
Dose bin setting field
Linear and logarithmic scale can be selected.
Max. dose and number of dose bin need to be specified.
Min. dose is necessary for log-scale.
An option to exclude zero dose voxels can be chosen to eliminate void regions.
DVH/DMH setting field
Differential or cumulative DVH/DMH can be chosen
Dose Volume Histogram (DVH)
Dose Mass Histogram (DMH) analysis on dose distribution
DVH/DMHcreater
DVH/DMH analysis is conducted for dose distribution and create a DVH/DMH output file
             ("dvh_***.out", "dmh_***.out")
DVH/DMH file list field
Created DVH/DMH file will be listed
Reset list button
List of DVH/DMH files in "PHITSinput" directory is displayed by clicking this button
Check RT-dose file button
work/sample2
*** will be name of RT dose file
Analysis mode selector (DVH or DMH)

--- SLIDE 45 ---
45
Setting for "Analysis"
RT-dose file list
Click
List of RT-dose files in "PHITSinput" directory is displayed by clicking this button
Check RT-dose file button
Ctrl + Click to select files
By selecting RT-dose files for the partial contribution* to the RT-dose file chosen for DVH analysis, partial dose contributions for voxels at each dose bin are computed.
* The selected files need to be partial contribution to the RT-dose file for DVH and mutually exclusive.
Dose Volume Histogram (DVH)
Dose Mass Histogram (DMH) with partial contributions
DVH/DMHcreater
Fraction of the partial contributions are also shown in the DVH/DMH output file ("dvh.out", "dmh.out")
work/sample2

--- SLIDE 46 ---
46
Setting for "Analysis"
Dose Volume Histogram (DVH)
Dose Mass Histogram (DMH) with region of interest (ROI)
Click
DVH/DMHcreater with ROI*
Sub-window is opened for ROI setting
DVH analysis is conducted for dose distribution with each ROI and create DVH/DMH output files ("dvh_***.out", "dmh_***.out") with the ROI name ***.
* Voxel format ROI file "ROIvoxel.inp" and ROI file list "roiinfo.dat" are required, which are created in ROI setting sub-window.
work/sample2

--- SLIDE 47 ---
47
Setting for "Analysis"
ROI format option
From RT-structure file

From ROI data in CT-image format
RT-structure file needs to be specified
Directory for ROI data needs to be specified
ROI2PHITS
ROI setting sub-window
ROI file list field
Converted ROI file will be listed
Button to check ROI list
ROI file list is loaded from roiinfo.dat file
Double-click
Voxel format ROI files "ROIvoxel_***.inp"are produced in "PHITSinput" directory with the ROI name ***.
ROI file list "roiinfo.dat" is also created
ROI distribution
work/sample2

--- SLIDE 48 ---
48
Setting for "Analysis"
Double-click
Partial contributions are shown by multiplying their energy contribution percentages to the fractional volume computed by the total energy.
DVH distribution
With ROI
With partial contribution
Order is determined by the list order
List order can be changed with a function shown by right-click
work/sample2
END_PPTX_TEXT

FILE: phits-lec-RTphits-CUI-jp.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-lec-RTphits-CUI-jp.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
PHITS
DICOM医療画像を使用したPHITSシミュレーション(CUI)
Multi-Purpose Particle and Heavy Ion Transport code System
Title
1
2023年8月改訂
まずはGUIによるRT-PHITSを試してください。
 (phits-lec-RTphits-GUI-jp.pptx)

SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
Table of Contents
2
講習の流れ
RT-PHITSの使い方
RT-PHITSを用いた応用例
PHITS2DICOMの使い方

SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 03 ---
DICOM医療画像を使用したPHITSシミュレーション
3
What is RT-PHITS
RadioTherapy package based on PHITS (RT-PHITS)
標的核医学治療
PHITS
一般DICOMソフト
詳細解析
3次元表示
DVH 解析
DICOMデータ(RT-Plan, PET-Image, CT-Image, RT-Structure, RT-Dose)
放射線治療計画
RT-PHITS(Plan2PHITS,  PET2PHITS,  CT2PHITS,  PHITS2DICOM)
PHITS input
線量分布
or
or
位相空間ファイル
開発中
InputCreater4PHITS
中間ファイル (ビーム体系、 線源情報、 患者体系、タリー設定)
T. Sato et al., EJNMMI Physics, 8, 4 (2021)
T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)

--- SLIDE 04 ---
SIMPLE SOURCE input      SimpleSource用のインプットであることを明示
"work/sample1/DATfiles/"中間ファイルを格納するディレクトリを指定
0                        線源オプション 0:100MeV陽子, 1:6MV光子, 2:190MeV陽子SOBP,
100.0 100.0             照射野サイズ: 横 縦(mm)
0.0 0.0                  中心オフセット: 横 縦(mm)
2000.0                   中心からの線源距離(mm)
0.0 0.0                  ビーム角度: 水平 垂直(度)
シンプル線源作成モジュール(SimpleSource)
4
1入力ファイルを作成(simplesource.inp)=>詳しくはREADME参照
SimpleSource HowTo
2実行 (Windows) RTphits_win.batにsimplesource.inpをドラッグ&ドロップ
         (Mac) RTphits_mac.commandをダブルクリック、現れる窓にsimplesource.inpと入力
PHITSインプットの中間ファイルを指定ディレクトリ(work/sample1/DATfiles/)に生成
   ・sourceinfo.dat     線源情報の中間ファイル
線源オプション=0: テスト計算用
negs=0: EGS使用無し、電子輸送無し
3: 290MeV炭素SOBP, 4: 400MeV炭素SOBP

--- SLIDE 05 ---
CT-Image (バイナリー)の変換
5
1 Header (撮影日時,ピクセルサイズなどの情報)
2 CT値(1,1->2,1->3,1-> ... -> nx-1, ny -> nx, ny)の順番
1つのスライスに対するデータ(sample001.dcm)
このファイルがスライス数入ったフォルダで1つの物体を表現
1つのファイルを表示
フォルダ全体のデータを3D表示
What is DICOM
Dicom形式からPHITS入力形式に変換する必要有
(CT値・バイナリ)
(Universe番号・テキスト)

--- SLIDE 06 ---
CT2PHITS input                CT2PHITS用のインプットであることを明示
"data/HumanVoxelTable.data"  変換テーブルの指定
"work/sample1/CT/"           指定ディレクトリ内に含まれるCT-Imageファイルを自動判別
"work/sample1/DATfiles/"     中間ファイルを格納するディレクトリを指定
1 47                         指定した番号範囲のスライスファイルを読み込む (1<=z<=20)
1 512 1 512                  DICOMデータの一部を切り出してボクセル化 (1<=x<=512, 1<=y<=512)
8 8 1                        画像を粗くする(分解能を下げる)ことが可能 (x方向8個、y方向8個で平均)
0                            座標系オプション 0:原点を中心 1:DICOMヘッダーから抽出
ファントム生成モジュール(ct2phits*)
6
Dicom形式のデータをPHITS形式のボクセルデータに変換
CT値と物質密度・組成の関係はdata/HumanVoxelTable.data [W. Schneider, Phys. Med. Biol. 45(2000)459-478]を参照
1入力ファイルを作成(ct2phits.inp)=>詳しくはREADME参照
CT2PHITS HowTo
2実行 (Windows) RTphits_win.batにct2phits.inpをドラッグ&ドロップ
          (Mac) RTphits_mac.commandをダブルクリック、現れる窓にct2phits.inpと入力
*dicom2phits
から名前を変更

--- SLIDE 07 ---
CT2PHITS実行結果
7
PHITSインクルードファイル用の中間ファイルを指定ディレクトリ(work/sample1/DATfiles/)に生成
   ・CTcell.dat         ファントム領域の定義
   ・CTmaterial.dat      材質データ
   ・CTmatnamecolor.dat  材質カラー情報
   ・CTuniverse.dat      ファントム領域のユニバースデータ
   ・CTusrparam.dat     ファントム用ユーザー定義変数
   ・CTvoxel.dat        PHITS形式に変換したボクセルデータ
CT2PHITS outputs
PHITSインプットのための中間ファイルを指定ディレクトリ(work/sample1/DATfiles/)に生成
   ・phantominfo.dat     ファントム情報の中間ファイル

--- SLIDE 08 ---
PHITSインクルードファイル
PHITS形式の詳細は /phits/lecture/advanced/voxel/phits-lec-voxel-jp.ppt 「Voxelファントムの作り方」を参照
CT2PHITS output
8
$ Voxel phantom
$ Material universe
 infl:{CTuniverse.inp}
$ Voxel universe
 5000 0 -5000 lat=1 u=5000
     fill= 0:63 0:63 0:46
 infl:{CTvoxel.inp}
$ CT parameters
set: c81[   64]  $ number of x pixel
set: c82[   64]  $ number of y pixel
set: c83[   47]  $ number of z pixel
set: c84[     0.78125] $ unit voxel x
set: c85[     0.78125] $ unit voxel y
set: c86[     0.32700] $ unit voxel z
set: c87[-c81*c84/2] $ smallest x
set: c88[-c82*c85/2] $ smallest y
set: c89[-c83*c86/2] $ smallest z
...
$ Voxel phantom
$ Unit voxel at smallest x & y
 5000 rpp c87 c87+c84 c88 c88+c85...
$ Outer region
   99 so 500
$ Main Space
   97 rpp c87 c87+c81*c84 c88 c88+...
   98 500 rpp c87+c90 c87+c81*c84...
ボクセルファントムの中心がxyz座標の原点にくるように配置されている
ボクセルファントムのピクセル数や大きさはDICOMのヘッダーから自動的に設定
CTusrparam.dat
CTsurf.dat
Include fileコマンド
CTsurf.dat

--- SLIDE 09 ---
CT値⇔物質密度・組成変換表
Table for human voxel based on W. Schneider, Phys....
24                        ! Number of universe di...
-1000.0d0  -1.21e-3  3    ! Lowest CT value, Dens
-950.0d0   -0.26     10   ! Universe 2
-120.0d0   -0.927    8    ! Universe 3
-82.0d0    -0.958    8    ! Universe 4  NOTE: Den ...
-52.0d0    -0.985    9    ! Universe 5        [10^...
-22.0d0    -1.012    8    ! Universe 6        [g/...
...
1500.0d0   -1.935    11   ! Universe 24
1600.0d0                  ! Highest CT value for...
#1 Air :: Air density is used     ! Composition
  N   -75.5                       ! Element, Ele...
  O   -23.2                       !
  Ar   -1.3                       !
#2 Lung :: Lung density is used   ! Composition o...
  H    -10.3
  C   -10.5
  N   -3.1
...
data/HumanVoxelTable.data サンプル表 [W. Schneider, Phys. Med. Biol. 45(2000)459を参照]
3行目:物質1の定義
-1000 -  物質1 < -950
物質1の最小CT値よりも小さい => ワーニングを出して物質1で代用
最後の物質の最大CT値よりも大きい => ワーニングを出して最後の物質で代用
Conversion table
9

--- SLIDE 10 ---
INPUTCREATER4PHITS input   InputCreater4PHITS用のインプットであることを明示
"work/sample1/DATfiles/"  中間ファイルが格納されるディレクトリを指定
"work/sample1/PHITSinput/"PHITSインプットを格納するディレクトリを指定
0                          パラメータオプション 0:デフォルト
1000 1                    Maxcas, Maxbch
0                          並列計算設定オプション 0:off
PHITSインプット作成モジュール(InputCreater4PHITS)
10
1入力ファイルを作成(inputcreater4phits.inp)=>詳しくはREADME参照
INPUTCREATER4PHITS HowTo
2実行 (Windows) RTphits_win.batにinputcreater4phits.inpをドラッグ&ドロップ
   (Mac) RTphits_mac.commandをダブルクリック、現れる窓にinputcreater4phits.inpと入力
中間ファイル(phantominfo.dat, sourceinfo.dat)の情報を基にPHITSのインプットファイル(phits.inp)を生成
PHITSインプットphits.inpを指定ディレクトリ(work/sample1/PHITSinput/)に生成
同時にCT***.datファイルは、指定ディレクトリにCT***.inpとしてコピーされる

--- SLIDE 11 ---
ジオメトリの確認
11
icntl = 11
icntl = 8
CT3D.eps
deposit-xy.eps
Geometry check

--- SLIDE 12 ---
ボクセル化する範囲と座標系の変更
12
CT2phits.inp
CT2PHITS input
"data/HumanVoxelTable.data" ! File for conversion of human voxel data
"work/sample1/CT/"          ! DICOM file directory
"work/sample1/DATfiles/"    ! Directory for intermediate files
2 46                        ! Minimum slice number, Maximum slice number
93 432 134 386              ! Clipping: Nxmin, Nxmax, Nymin, Nymax
8 8 1                       ! Coarse graining: Nxc, Nyc, Nzc
1                           ! Origin 0:Voxel center 1:DICOM center
deposit-xy.eps
Region specification
$ Transform system according to DICOM header
tr500 c91 c92 c93
        1.00000   0.00000   0.00000
        0.00000   1.00000   0.00000
        0.00000   0.00000   1.00000
     1
座標系オプションで1を選択するとDICOMヘッダーから位置情報を抽出し、この座標へ平行移動
1 CT2PHITSを実行
2 ファントム情報を反映するためにInputCreater4PHITSを再実行(inputcreater4phits.inpは修正必要無し)

--- SLIDE 13 ---
回転と平行移動
[transform]
13
nは座標変換番号
x0, y0, z0は平行移動を表すX,Y,Z成分
Rz, Ry, RxはX, Y, Z, 方向の回転行列
Mで変換式を選択 (ここではM=2のみ扱う)
[ T r a n s f o r m ]
    Trn     x0   y0   z0   ->z   ->y   ->x   0   0  0   0   0  0   M
M=2のとき
[Transform]セクションを設定し、[cell], [source]セクション等においてtrcl=nとする。

--- SLIDE 14 ---
14
icntl = 0
線量計算結果
deposit-xy.eps
unit  = 2
=> MeV/source 単位
Dose calculation
陽子線100 MeV
空気は密度が低いので落ちる付与エネルギーは小さい

--- SLIDE 15 ---
Table of Contents
15
講習の流れ
RT-PHITSの使い方
RT-PHITSを用いた応用例
PHITS2DICOMの使い方

SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 16 ---
ct2phits.inp
DICOM2PHITS input
"data/HumanVoxelTable.data"
"work/sample2/CT/"
"work/sample2/DATfiles/"
1 126                      100 420 150 400
8 8 2
1
RT2PHITS応用例
16
Further application
2 フォルダwork/sample2/PHITSinputで、phits.inpをicntl=8でPHITSを実行
deposit-xy.eps
deposit-xz.eps
CT2PHITSを実行
SIMPLE SOURCE input
work/sample2/DATfiles/
1  $ 6MV photon
50.0 50.0 $ 50mm x 50mm
0.0 0.0
2000.0
0.0 0.0
SimpleSourceを実行
simplesource.inp
INPUTCREATER4PHITS input
"work/sample2/DATfiles/"
"work/sample2/PHITSinput/"
0
10000 1 $ Increased MAXCAS
0
InputCreater4PHITSを実行
inputcreater4phits.inp
1 RT-PHITSの各モジュールのインプットを変更して実行

--- SLIDE 17 ---
読込の高速化
17
PHITSでは一度インプットファイルを全てバイナリー化してから再読込
巨大なボクセルデータをあらかじめバイナリー化して読込時間短縮!
目的
手順
1 [Parameters]セクションのivoxelを有効にする(cを消す)
ivoxel = 2                 # LatticeのFill部分をバイナリー化としてfile(18)に出力させるオプション
file(18) = voxel.bin   # 出力するバイナリーファイルのファイル名
2 PHITSを実行する -> Binary file was successfully generated!!
3 ivoxel = 1に変更する
ivoxel = 1 # LatticeのFill部分をfile(18)から読み込むオプション
高速化!
Faster execution

--- SLIDE 18 ---
どう変化するか?
応用例:線源位置の変更
線源位置変更
SIMPLE SOURCE input
"work/sample2/DATfiles/"
0
100.0 100.0 照射野サイズ: 横 縦(mm)
0.0 0.0     中心オフセット: 横 縦(mm)
2000.0      中心からの線源距離(mm)
0.0 0.0     ビーム角度: 水平 垂直(度)
simplesource.inp
50.0 50.0
1 SimpleSourceを実行
2 線源情報を反映するためにInputCreater4PHITSを
  再実行(inputcreater4phits.inpは修正必要無し)
deposit-xz.eps
Application: Modification of beam profile
18
icntl = 0

--- SLIDE 19 ---
応用例:線源の向きの変更
どう変化するか?
SIMPLE SOURCE input
"work/sample2/DATfiles/"
0
100.0 100.0 照射野サイズ: 横 縦(mm)
0.0 0.0     中心オフセット: 横 縦(mm)
2000.0      中心からの線源距離(mm)
0.0  0.0    ビーム角度: 水平 垂直(度)
simplesource.inp
0.0 0.0
1 SimpleSourceを実行
2 線源情報を反映するためにInputCreater4PHITSを
  再実行(inputcreater4phits.inpは修正必要無し)
0度
90度
-90度
90度
-90度
0度
90.0
deposit-xz.eps
19
Application: Modification of beam profile
icntl = 0

--- SLIDE 20 ---
マテリアル数が多い場合の注意点
20
マテリアル数が多い場合にEGSを使用すると、EGS用断面積データを用意するのに非常に時間がかかる(PHITS実行の最初に全てのマテリアルについて用意)。
複数回PHITSを実行する場合には、PHITS実行時にEGS用断面積データを毎回準備するのではなく、一度作成した断面積データを使いまわすことができる。
1 ipegs=-1 をパラメータセクションで設定し、PHITSを実行
   => EGS用断面積データを生成し、輸送計算を実行せずに終了
2 ipegs=2 をパラメータセクションで設定し、PHITSを実行
   => 既存のEGS用断面積データを使用して、輸送計算を実行
詳しくはマニュアルのEGS5用パラメータの項目を参照
実行方法
Many materials with EGS
線源オプション=0 以外 negs=1: EGS使用有り

--- SLIDE 21 ---
Table of Contents
21
講習の流れ
RT-PHITSの使い方
RT-PHITSを用いた応用例
PHITS2DICOMの使い方

SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 22 ---
PHITS2DICOM input                   PHITS2DICOM用のインプットであることを明示
data/sample.dcm                     DICOM RT-doseサンプルファイルを指定
work/sample1/DICOM/60592375         CT2PHITSの変換に使用したDICOMファイルどれでも一つを指定
work/sample1/PHITSinput/deposit.out PHITSで計算した三次元線量分布データを指定
work/sample1/PHITSinput/phits.out   PHITS実行で出力されたphits.outを指定
work/sample1/DATfiles/              中間ファイルが格納されるディレクトリを指定
1                                   線量の規格化を設定 0:しない 1:最大値が1で規格化...
22
PHITSの出力(三次元線量分布)をDICOM RT-dose形式に変換
2入力ファイルを作成(phits2dicom.inp)
PHITS2DICOM HowTo
3 PHITS2DICOM実行
       (Windows) RTphits_win.batにphits2dicom.inpをドラッグ&ドロップ
     (Mac) RTphits_mac.commandをダブルクリック、現れる窓にphits2dicom.inpと入力
1PHITSで三次元線量分布を計算
=> work/PHITSinput内のphits.inpでPHITSを実行
=> 三次元線量分布deposit.outが出力
=> RT-dose形式のファイルが出力
(work/sample1/PHITSinput/deposit.dcm)拡張子dcmのファイルが生成
PHITS計算結果DICOMフォーマット変換モジュール(phits2dicom)

--- SLIDE 23 ---
DICOMビューワーで確認
23
DICOM viewer

--- SLIDE 24 ---
まとめ
24
Summary
RT-PHITSを使用することで、DICOMイメージデータをPHITS形式のボクセルデータに変換
線源を状況に合わせて変更
PHITS2DICOMを使用することで、PHITS出力の三次元線量分布をRT-dose形式に変換
DICOM RTが読み込めるソフトウェアを用いて、CT値と線量値の同時表示や線量解析が可能
T. Sato et al., EJNMMI Physics, 8, 4 (2021)
T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)
参考文献

--- SLIDE 25 ---
PET-CTデータを用いた吸収線量及び生物学的線量(EQDX)の計算手法
25
Appendix

--- SLIDE 26 ---
PHITS output files from icntl = 0
ct2phits.inp
pet2phits.inp
計算の流れ
CT data (work/CT)
PET data (work/CT)
Intermediate files (work/DATfiles)
phits.inp
PHITS input files (work/PHITSinput)
voxel_src###.inp
Decaybio.out
CTvoxel.inp
基本インプット
体系
線源
生物学的崩壊定数
inputcreater4phits.inp
deposit.out
吸収線量
α線量
β線量
deposit_alpha.out
deposit_beta.out
deposit_MeV.out
付与エネルギー
PHITS output files from icntl = 17
EQDX.out
生物学的線量
phits2dicom.inp
DICOM RT-dose
deposit.dcm
Deposit_MeV.dcm
(optional)
EQDX.dcm

--- SLIDE 27 ---
PET2PHITS input             # Signature of PET2PHITS
"data/RIlist.dat"           # RI list file
At-211                      # Name of RI listed in Rilist.dat
0 0 1 0 1                   # all, photon, electron, positron, alpha; 0:off 1:on
"work/sample1/DATfiles/"    # Intermediate file directory
0                           # Skip reading PET files 0:off 1:on
"work/sample1/PET/"         # PET image directory
1 47                        # Minimum slice number, Maximum slice number
55 145 60 140               # Clipping: Xmin, Xmax, Ymin, Ymax
-1.0                        # Biological decay constant (if <0 Fitting from PET data)
1                           # Source activity is normalized per MBq
RI線源作成モジュール (pet2phits)
27
PETデータからxyz-mesh形式での[source]セクションの作成
時間積分放射能 in Bq.s (voxel_src000.inp)
時間微分放射能 in Bq (voxel_src###.inp, ###: time step)
PET2PHITS
1入力ファイルを作成(pet2phits.inp)=>詳しくはREADME参照
2実行 (Windows) RTphits_win.batにpet2phits.inpをドラッグ&ドロップ
          (Mac) RTphits_mac.commandをダブルクリック、現れる窓にpet2phits.inpと入力

--- SLIDE 28 ---
生物学的線量EQDXとは?
28
*Bentzen et al. Radiother Oncol. (2012)
標的核医学治療の特徴
比較的低線量率の長時間1回照射
腫瘍内で線量が不均一
RBE ≠ 1(TATの場合)
全ての治療法を統一の指標で評価できる
EQDX(α/β)の例
同じ吸収線量でも効果が違う
同じ治療効果を得るために必要となる分割X線治療の吸収線量EQuieffective Dose for fraction size X, EQDX(α/β), がICRUより提案*
S:細胞生存率

--- SLIDE 29 ---
29
TATにおけるEQDXは、SMKモデル*に基づくユーザー定義anatallyを用いてα線とβ線による吸収線量から計算可能
*T.Sato & Y.Furusawa, Radiat. Res. 178, 341-356 (2012)
吸収線量からEQDXへの変換
phits/utility/usranatal/smk_tat/srcに含まれるusranatal.fを使ってPHITSを再コンパイル
RT-PHITSで作られたphits.inpのicntlを0から17 (anatallyモード)に変更
phits/utility/usranatal/smk_tat/phits.inpの[anatally]セクションを上記phits.inpにコピー
再コンパイルしたPHITSで上記修正を加えたphits.inpを実行

EQDX分布をDICOM viewerで確認したい場合は、PHITS2DICOMを使ってEQDX.outをEQDX.dcmに変換
詳細はphits/utility/usranatal/readme-jp.docxもご参照ください
=> EQDXの3次元分布 EQDX.out が出力される
変換手順

--- SLIDE 30 ---
30
DICOM viewer
DICOMビューワーで確認

--- SLIDE 31 ---
参考文献
31
Reference
T.Sato, T. Furuta, Y. Liu, S. Naka, S. Nagamori, Y. Kanai, T. Watabe, Individual Dosimetry System for Targeted Alpha Therapy Based on PHITS Coupled with Microdosimetric Kinetic Model, EJNMMI Physics 8: 4 (2021).
https://ejnmmiphys.springeropen.com/articles/10.1186/s40658-020-00350-7
本手法と論文に書かれた手法は、以下の点で異なります
通常のMKモデルではなくSMKモデルを利用しています
ROIを設定する機能は、ROIのフォーマットが決まっていないため含まれていません
オープンアクセス!!
注意点
END_PPTX_TEXT

FILE: phits-lec-RTphits-GUI-jp.pptx
BEGIN_PPTX_TEXT
PPTX_FILE: phits-lec-RTphits-GUI-jp.pptx
NOTE: Images are not included. Only slide text and speaker notes are extracted.

--- SLIDE 01 ---
1
PHITS
DICOM医療画像を使用したPHITSシミュレーション
Multi-Purpose Particle and Heavy Ion Transport code System
2023年8月改訂

--- SLIDE 02 ---
2
What is RT-PHITS
RadioTherapy package based on PHITS (RT-PHITS)
標的核医学治療
PHITS
一般DICOMソフト
詳細解析
3次元表示
DVH 解析
DICOMデータ(RT-Plan, PET-Image, CT-Image, RT-Structure, RT-Dose)
放射線治療計画
RT-PHITS(Plan2PHITS,  PET2PHITS,  CT2PHITS,  PHITS2DICOM)
PHITS input
線量分布
or
or
位相空間ファイル
InputCreater4PHITS
中間ファイル (ビーム体系、 線源情報、 患者体系、タリー設定)
T. Sato et al., EJNMMI Physics, 8, 4 (2021)
T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)
DICOM医療画像を使用したPHITSシミュレーション

--- SLIDE 03 ---
3
必要ソフトウェアとライブラリ
Pythonのインストール
ダウンロード&インストール(バージョン3.0以降が必要)
https://www.python.org/
Pythonライブラリインストール
GUIにライブラリ(pydicom, matplotlib, numpy)が必要
"pip install"を使用することで、簡単にインストール可能
"Terminal" や "Command prompt"を開く
下記コマンド入力によりインストール
	pip install pydicom
	pip install matplotlib
	pip install numpy
(エラーが出る場合は"pip install"の代わりに"py -m pip install"を試す )
Tkinterライブラリのインストールも場合によっては必要(Ubuntu等)
Windows用には特に追加ソフト・ライブラリは必要無し*
Mac、Linux用にはPythonとそのライブラリが必要
*実行ファイルが動作しない場合は必要

--- SLIDE 04 ---
4
RT-PHITS内のディレクトリ構造
RT-PHITS/
    |
    |---bin/ : 実行ファイルディレクトリ
    |---binSAVE/ : bin/ディレクトリのバックアップ
    |---data/ : RT-PHITS用のデータディレクトリ
    |---picture/: GUI用画像イメージデータディレクトリ
    |---PSFs/: Phase space fileディレクトリ
    |---RTphitsGUI.py : RT-PHITS用Python GUIプログラム
    |---src/ : ソースファイルディレクトリ
    |---work/ : ワーキングディレクトリ
         |---sample1/
              |---CT/ : CTデータディレクトリ
              |---DATfiles/ : 中間ファイルディレクトリ
              |---PET/ : PETデータディレクトリ
              |---PHITSinput/ : PHITSインプットファイルディレクトリ
              |---ROI/ : ROIデータディレクトリ
         |---sample2/
              |---CT/ : CTデータディレクトリ
              |---DATfiles/ : 中間ファイルディレクトリ
              |---PHITSinput/ : PHITSインプットファイルディレクトリ
              |---Plan/ : 治療計画RT-Planデータディレクトリ
              |---Structure/ : ROI RT-Structureデータディレクトリ

--- SLIDE 05 ---
5
RT-PHITSの実行
"RTphitsGUI.py"をダブルクリック
 もしくはターミナル上で"python RTphitsGUI.py"
クリックすると選択ウィンドウが開く
1ディレクトリを選択
2"OK"をクリック
ワーキングディレクトリの選択
|---work/ : Working directory
         |---sample1/
              |---CT/ : CTデータディレクトリ
              |---DATfiles/ : 中間ファイルディレクトリ*
              |---PET/ : PETデータディレクトリ
              |---PHITSinput/ : PHITSインプットディレクトリ
              |---ROI/ : ROIデータディレクトリ
= サブディレクトリを含むワーキングディレクトリ
* DATfilesディレクトリが無い場合は作成確認のダイアログが出る
"RTphitsGUI.exe"をダブルクリック (Windows only)
Pythonによる実行が出来ない場合、CUIによるRT-PHITSの実行を試す(phits-lec-Rtphits-CUI.pptx)

--- SLIDE 06 ---
6
選択タブ
状態表示
各タブの設定フィールド
Source
        線源の設定
Phantom
        標的(ファントム)の設定
Tally
        タリーの選択
PHITS
        パラメータの設定
        PHITSインプット作成
PHITS2DICOM
        RT-doseファイルの作成
        線量分布の確認
Analysis
        DVH解析
各タブの状態
   未設定
   設定済み
   前回設定引継ぎ
RT-PHITS GUIメインフレーム
前回設定の読込ボタン
(各タブに存在)

--- SLIDE 07 ---
7
"Source"の設定
Click
三種類の線源オプション:
シンプル線源
         単純な四角面線源
RT-Plan [炭素線治療のみ]
         治療計画装置のRT-Planに基づく加速器ビーム線源
         (ビーム装置体系含む)
PET
         PETイメージに基づく、RI線源設定

--- SLIDE 08 ---
8
シンプル線源の設定
Click
ビーム選択
線源オプション=0: テスト計算用
negs=0: EGS使用無し、電子輸送無し
照射野サイズ
照射野中心のオフセット
ビーム角度
"DATfiles"に中間ファイル "sourceinfo.dat"を生成
Click
照射野やビーム角度等を加味した
単純な四角面線源を設定(テスト用)
アイソセンタからの線源距離
成功すると状態が"   Done" に変わる
複雑な線源設定は生成されるPHITS
インプットファイルの修正により実現
デフォルトで実行

--- SLIDE 09 ---
9
"Phantom"の設定
Click
二種類のオプション:
Water phantom
         単純な水直方体ファントム
CT image
       CTイメージから再構成する患者体系

--- SLIDE 10 ---
10
1 Header (撮影日時,ピクセルサイズなどの情報)
2 CT値(1,1->2,1->3,1-> ... -> nx-1, ny -> nx, ny)の順番
1つのスライスに対するデータ(sample001.dcm)
このファイルがスライス数入ったフォルダで1つの物体を表現
1つのファイルを表示
フォルダ全体のデータを3D表示
What is DICOM
Dicom形式からPHITS入力形式に変換する必要有
(CT値・バイナリ)
(Universe番号・テキスト)
CT-Image (バイナリー)の変換

--- SLIDE 11 ---
11
Click
"Phantom"の設定 (CTイメージ)
CT-voxel 変換表ファイル
CTイメージフィールド
Click
CTデータディレクトリを選択し、"Load" ボタンをクリック
読み込まれたCTデータの内容の表示と
      他の設定のためのフィールドが表示される
座標原点のオプション
ボクセルの中心を原点とする
DICOMタグ情報に従って原点を設定する
患者体系(ボクセルファントム)を患者CTイメージから再構築

--- SLIDE 12 ---
12
ピクセルクくり抜きフィールド
ピクセルおよびスライスの最小min. 最大max.を設定することで、必要領域をくり抜き、メモリとCPU時間をセーブ
Click
ウィンドウをクリックすることで、スライス位置を変更可能
マウスポインタ位置の座標とCT値が表示される
クリッピングの範囲
を四角で表示
粗視化設定フィールド
XYZ方向に平均化するボクセル数を設定
タリー出力のCPU時間をセーブ (テストで推奨)
  例、xとy方向に4×4ボクセルで平均
"CT***.dat":CT情報抽出データ
"phantominfo.dat":ファントム情報データ
CTイメージ
CT2PHITS
"Phantom"の設定 (CTイメージ)
中間ファイルディレクトリ"DATfiles"に生成

--- SLIDE 13 ---
13
PHITSインクルードファイル用の中間ファイルを指定ディレクトリ(work/sample1/DATfiles/)に生成
   ・CTcell.dat         ファントム領域の定義
   ・CTmaterial.dat      材質データ
   ・CTmatnamecolor.dat  材質カラー情報
   ・CTuniverse.dat      ファントム領域のユニバースデータ
   ・CTusrparam.dat     ファントム用ユーザー定義変数
   ・CTvoxel.dat        PHITS形式に変換したボクセルデータ
CT2PHITS outputs
PHITSインプットのための中間ファイルを指定ディレクトリ(work/sample1/DATfiles/)に生成
   ・phantominfo.dat     ファントム情報の中間ファイル
CT2PHITSの実行結果

--- SLIDE 14 ---
PHITS形式の詳細は /phits/lecture/advanced/voxel/phits-lec-voxel-jp.ppt 「Voxelファントムの作り方」を参照
CT2PHITS output
14
$ Voxel phantom
$ Material universe
 infl:{CTuniverse.inp}
$ Voxel universe
 5000 0 -5000 lat=1 u=5000
     fill= 0:63 0:63 0:46
 infl:{CTvoxel.inp}
$ CT parameters
set: c81[   64]  $ number of x pixel
set: c82[   64]  $ number of y pixel
set: c83[   47]  $ number of z pixel
set: c84[     0.78125] $ unit voxel x
set: c85[     0.78125] $ unit voxel y
set: c86[     0.32700] $ unit voxel z
set: c87[-c81*c84/2] $ smallest x
set: c88[-c82*c85/2] $ smallest y
set: c89[-c83*c86/2] $ smallest z
...
$ Voxel phantom
$ Unit voxel at smallest x & y
 5000 rpp c87 c87+c84 c88 c88+c85...
$ Outer region
   99 so 500
$ Main Space
   97 rpp c87 c87+c81*c84 c88 c88+...
   98 500 rpp c87+c90 c87+c81*c84...
ボクセルファントムの中心がxyz座標の原点にくるように配置されている
ボクセルファントムのピクセル数や大きさはDICOMのヘッダーから自動的に設定
CTusrparam.dat
CTsurf.dat
Include fileコマンド
CTcell.dat
インクルードファイル

--- SLIDE 15 ---
Table for human voxel based on W. Schneider, Phys....
24                        ! Number of universe di...
-1000.0d0  -1.21e-3  3    ! Lowest CT value, Dens
-950.0d0   -0.26     10   ! Universe 2
-120.0d0   -0.927    8    ! Universe 3
-82.0d0    -0.958    8    ! Universe 4  NOTE: Den ...
-52.0d0    -0.985    9    ! Universe 5        [10^...
-22.0d0    -1.012    8    ! Universe 6        [g/...
...
1500.0d0   -1.935    11   ! Universe 24
1600.0d0                  ! Highest CT value for...
#1 Air :: Air density is used     ! Composition
  N   -75.5                       ! Element, Ele...
  O   -23.2                       !
  Ar   -1.3                       !
#2 Lung :: Lung density is used   ! Composition o...
  H    -10.3
  C   -10.5
  N   -3.1
...
data/HumanVoxelTable.data サンプル表 [W. Schneider, Phys. Med. Biol. 45(2000)459を参照]
3行目:物質1の定義
-1000 -  物質1 < -950
物質1の最小CT値よりも小さい => ワーニングを出して物質1で代用
最後の物質の最大CT値よりも大きい => ワーニングを出して最後の物質で代用
Conversion table
15
CT値⇔物質密度・組成変換表

--- SLIDE 16 ---
16
"Tally"の設定
タリーの選択 (チェックマークを入れる*)
3D線量分布
CTの範囲および解像度と同様に設定
 (CTイメージオプション選択時)
* 全部のタリー設定はインプットの記述されるので、タリーの"off"を手動で外すことで、後ほど有効にすることが可能
Click
"DATfiles"に中間ファイル"tallyinfo.dat"を生成
Click
ボクセル中心の平面線量分布

--- SLIDE 17 ---
17
"PHITS"の設定
状態チェックフィールド
"source", "phantom", "tally"のタブの実行状況をチェック
ボタンクリックで前回の中間ファイルを読み込むことが可能
ヒストリ数の設定フィールド
PHITSの"maxcas"と"maxbch"を設定
並列実行用設定フィールド
並列の有無
   OpenMPの並列数
   MPIの並列数
パラメータ設定フィールド
線源に従い自動的に設定
カスタム (ファイルから読み込み)
Click
InputCreater4PHITS
"DATfiles"ディレクトリ内の中間ファイル(sourceinfo.dat, phantominfo.dat, tallyinfo.dat)
の情報を基にPHITSインプットファイル"phits.inp"を"PHITSinput" ディレクトリに生成
PHITSインプットファイルのディレクトリ
デフォルトで実行

--- SLIDE 18 ---
18
PHITSの実行
PHITSの実行に必要なインプットファイル "phits.inp", インクルードファイル, その他のファイルは "PHITSinput"ディレクトリに含まれる。
PHITS実行時に得られるタリーファイル("***.out")およびEPSファイル("***.eps")も同じディレクトリに生成される
PHITSを"PHITSinput" ディレクトリ内で実行
PHITSiput directory
PHITSiput ディレクトリ
スパコン等の高性能計算機
"PHITSinput"ディレクトリを丸ごとコピー
"***.out" and "***.eps" をコピーし戻す
PHITSを実行
実行方法 1
実行方法 2
解析
Click

--- SLIDE 19 ---
19
icntl = 11
icntl = 8
CT3D.eps
deposit-xy.eps
Geometry check
体系の確認
work/sample1/PHITSinput/phits.inpを開いて、
icntlパラメータを変更し、PHITSを実行

--- SLIDE 20 ---
20
deposit-xy.eps
Region specification
ボクセル化する範囲と座標系の変更
Click
変更後Click
クリッピングの範囲
を四角で表示
1Phantomタブで修正し、CT2PHITS実行
2ファントム変更の反映のため、PHITSタブでInputCreater4PHITSを再実行(デフォルト)
3work/sample1/PHITSinput/phits.inpを開いて、icntl=8に変更しPHITSを実行
icntl = 8
93    432
134  386
2      46
DICOM座標

--- SLIDE 21 ---
21
deposit-xy.eps
unit  = 2
=> MeV/source 単位
Dose calculation
陽子線100 MeV
線量計算の結果
work/sample1/PHITSinput/phits.inpを開いて、icntl=0に変更しPHITSを実行
空気は密度が低いので落ちる付与エネルギーは小さい

--- SLIDE 22 ---
22
"PHITS2DICOM"の設定
CTデータディレクトリ
"phits.out"ファイル
三次元線量分布タリー出力ファイル
線量規格化オプション
As it is

Max to 1

By norm. factor

By dose at point
線量値をそのまま変換(N=1.0)
最大値が1.0となるように規格化
与えられた値で規格化*
座標点の与えられた線量値で規格化**
* このボタンで前回の規格化定数が自動設定
** RT-Plan sourceの場合は、"sourceinfo.dat"から読み込むことが可能
Click
Click
PHITSの三次元線量分布をRT-doseファイルに変換
PHITS入出力ディレクトリ

--- SLIDE 23 ---
23
"PHITS2DICOM"の設定
PHITS2DICOM
RT-doseファイルリスト
三次元線量分布が変換されてRT-dose file が生成。ファイル名は三次元線量分布ファイルの拡張子を "dcm"に変えたものになる。
      e.g. deposit.out => deposit.dcm
生成されたRT-doseファイルがリストとして表示される
リストのリセットボタン
"PHITSinput" ディレクトリ内のRT-doseファイルがリストアップされる
RT-doseファイルのチェックボタン

--- SLIDE 24 ---
24
"PHITS2DICOM"での三次元分布の確認
ダブルクリック
Dose distribution
ウィンドウをクリックすることで、スライス位置を変更可能
カラーバー設定フィールド
線形・ログスケールの切り替えが可能
最大・最小は明示的に与えない限り自動で設定
マウスポインタ位置の座標と線量値が表示される

--- SLIDE 25 ---
25
Summary
線源を状況に合わせて変更
RT-PHITSを使用することで、DICOMイメージデータをPHITS形式のボクセルデータに変換
PHITS2DICOMを使用することで、PHITS出力の三次元線量分布をRT-dose形式に変換
CT値と線量値の同時表示や線量解析が可能
  (他のDICOMファイル対応ソフトを使った解析も可能)
T. Sato et al., EJNMMI Physics, 8, 4 (2021)
T. Furuta et al., Phys. Med. Biol., 67, 145002 (2022)
参考文献
まとめ

--- SLIDE 26 ---
PET-CTデータを用いた吸収線量及び生物学的線量(EQDX)の計算手法
26
Appendix

--- SLIDE 27 ---
PHITS output files from icntl = 0
ct2phits.inp
pet2phits.inp
計算の流れ
CT data (work/CT)
PET data (work/CT)
Intermediate files (work/DATfiles)
phits.inp
PHITS input files (work/PHITSinput)
voxel_src###.inp
Decaybio.out
CTvoxel.inp
基本インプット
体系
線源
生物学的崩壊定数
inputcreater4phits.inp
deposit.out
吸収線量
α線量
β線量
deposit_alpha.out
deposit_beta.out
deposit_MeV.out
付与エネルギー
PHITS output files from icntl = 17
EQDX.out
生物学的線量
phits2dicom.inp
DICOM RT-dose
deposit.dcm
Deposit_MeV.dcm
(optional)
EQDX.dcm

--- SLIDE 28 ---
28
"Source"の設定 (PET)
Click
RIリストファイル (ファイルの編集可能)
RI線源をプルダウンメニューから選択
線種の選択
PETイメージデータフィールド
PETイメージディレクトリを選択し、"Load"ボタンを押すことでPETイメージ読み込み
          => 読み込まれたPETデータ情報のフィールドが開く
Click
PETイメージデータを基に放射線各種の放射能分布を設定

--- SLIDE 29 ---
29
"Source"の設定 (PET)
Click
PET情報フィールド
ピクセルくり抜きフィールド
PETイメージのチェック(オプション)
生物学的崩壊の設定フィールド
PETイメージに関連するCTイメージデータのディレクトリを選択し、"View"ボタンを押すことで、CTイメージ上で放射能分布をチェックすることが可能。
カラーバーの最大・最小は明示的に与えない限り自動で設定。線形・ログの切り替えも可能。
二種類のオプション
時間経過のPETイメージから各ボクセルごとの時間変化をフィッティングして導出 (最低3フレーム分のPETイメージが必要)
全てのボクセルで共通の定数を使用
ピクセルおよびスライスの最小min. 最大max.を設定することで、必要領域をくり抜き、メモリとCPU時間をセーブ

--- SLIDE 30 ---
30
"Source"の設定 (PET)
放射能分布
Clipping area is shown by square
Time frame of PET image can be changed
Slice location can be changed by clicking the map
Coordinate and PET value can be checked by placing mouse pointer on the map
中間ファイル"sourceinfo.dat"
放射能分布ファイル"bqdata.dat"
生物学的崩壊データファイル "decaybio.dat"
中間ファイルディレクトリ"DATfiles"に生成
Click
PET2PHITS
MBq規格化
55   145
60   140
1      47
続けてPHITSタブでInputCreater4PHITSを実行
PETデータからxyz-mesh形式での[source]セクションの作成
時間積分放射能 in Bq.s (voxel_src000.inp)
時間微分放射能 in Bq (voxel_src###.inp, ###: time step)

--- SLIDE 31 ---
生物学的線量EQDXとは?
31
*Bentzen et al. Radiother Oncol. (2012)
標的核医学治療の特徴
比較的低線量率の長時間1回照射
腫瘍内で線量が不均一
RBE ≠ 1(TATの場合)
全ての治療法を統一の指標で評価できる
EQDX(α/β)の例
同じ吸収線量でも効果が違う
同じ治療効果を得るために必要となる分割X線治療の吸収線量EQuieffective Dose for fraction size X, EQDX(α/β), がICRUより提案*
S:細胞生存率

--- SLIDE 32 ---
32
TATにおけるEQDXは、SMKモデル*に基づくユーザー定義anatallyを用いてα線とβ線による吸収線量から計算可能
*T.Sato & Y.Furusawa, Radiat. Res. 178, 341-356 (2012)
吸収線量からEQDXへの変換
phits/utility/usranatal/smk_tat/srcに含まれるusranatal.fを使ってPHITSを再コンパイル
RT-PHITSで作られたphits.inpのicntlを0から17 (anatallyモード)に変更
phits/utility/usranatal/smk_tat/phits.inpの[anatally]セクションを上記phits.inpにコピー
再コンパイルしたPHITSで上記修正を加えたphits.inpを実行

EQDX分布をDICOM viewerで確認したい場合は、PHITS2DICOMを使ってEQDX.outをEQDX.dcmに変換
詳細はphits/utility/usranatal/readme-jp.docxもご参照ください
=> EQDXの3次元分布 EQDX.out が出力される
変換手順

--- SLIDE 33 ---
33
DICOM viewer
DICOMビューワーで確認

--- SLIDE 34 ---
参考文献
34
Reference
T.Sato, T. Furuta, Y. Liu, S. Naka, S. Nagamori, Y. Kanai, T. Watabe, Individual Dosimetry System for Targeted Alpha Therapy Based on PHITS Coupled with Microdosimetric Kinetic Model, EJNMMI Physics 8: 4 (2021).
https://ejnmmiphys.springeropen.com/articles/10.1186/s40658-020-00350-7
本手法と論文に書かれた手法は、以下の点で異なります
通常のMKモデルではなくSMKモデルを利用しています
ROIを設定する機能は、ROIのフォーマットが決まっていないため含まれていません
オープンアクセス!!
注意点
END_PPTX_TEXT

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: DVKmode/dvkfolder/autorun.inp
FILE: DVKmode/dvkfolder/makeDVK.inp
FILE: work/sample1/ct2phits.inp
FILE: work/sample1/inputcreater4phits.inp
FILE: work/sample1/pet2phits.inp
FILE: work/sample1/phits2dicom.inp
FILE: work/sample1/simplesource.inp
FILE: work/sample2/ct2phits.inp
FILE: work/sample2/inputcreater4phits.inp
FILE: work/sample2/planreader4phits.inp
FILE: work/sample2/simplesource.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: CHANGELOG.txt
FILE: data/FacilityInfo.dat
FILE: data/HumanVoxelTable.data
FILE: data/Material.dat
FILE: data/RIlist.dat
FILE: picture/takenfrom.txt
FILE: PSFs/29OV100060000.txt
FILE: PSFs/40OH100080000.txt
FILE: RTphits_mac.command
FILE: RTphits_win.bat
FILE: src/clean_lin.sh
FILE: src/clean_mac.sh
FILE: src/clean_win.bat
FILE: src/compile_lin.sh
FILE: src/compile_mac.sh
FILE: src/compile_win.bat
FILE: src/createctmod.f
FILE: src/createmod.f
FILE: src/createpetmod.f
FILE: src/createplanmod.f
FILE: src/createroimod.f
FILE: src/ct2phits.f
FILE: src/devicemod.f
FILE: src/dicomdict.h
FILE: src/dicomlib.c
FILE: src/dicomlib.h
FILE: src/dicomreader.c
FILE: src/dmhcreater.c
FILE: src/dvhcreater.c
FILE: src/fitbiomod.f
FILE: src/inputcreater4phits.f
FILE: src/interface.c
FILE: src/nonwinlib.c
FILE: src/osDRexe_lin.cpp
FILE: src/osDRexe_mac.cpp
FILE: src/osDRexe_win.cpp
FILE: src/pet2phits.f
FILE: src/phits2dicom.c
FILE: src/phitslib.c
FILE: src/phitslib.h
FILE: src/plan2phits.f
FILE: src/planreader4phits.cpp
FILE: src/psfsplitter.f
FILE: src/readctmod.f
FILE: src/readmod.f
FILE: src/readpetmod.f
FILE: src/readplanmod.f
FILE: src/readroimod.f
FILE: src/roi2phits.f
FILE: src/roi2phitscmod.c
FILE: src/simplesource.f
FILE: src/stdmod.f
FILE: src/surflistmod.f
FILE: src/tablemod.f
FILE: src/utllib.c
FILE: src/utllib.h
FILE: src/voxelidmodifier.f
FILE: src/winlib.c
