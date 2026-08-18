# Utility: HDF5

SOURCE_FOLDER: D:/NEAgit/utility/HDF5
NOTE: Code and other plain-text files are referenced by path only; read them directly from SOURCE_FOLDER.

UTILITY_BUNDLE: HDF5
UTILITY_PATH_INDEX: utility/HDF5
UTILITY_FOLDER_NAME: HDF5

[INDEX]
SOURCE_TYPE: utility
UTILITY_PATH_INDEX: utility/HDF5
BASIC_FILE_COUNT: 1
BASIC_FILE: RecompilePHITSenablingHDF5.docx
BASIC_FILE_TYPE: docx
PPTX_COUNT: 0
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 1

[BASIC_FILES]
FILE: RecompilePHITSenablingHDF5.docx
BEGIN_BASIC_TEXT
Compilation of PHITS with enabling the HDF5 function
Last revised 2024/08/09
Preface:
HDF5 (Hierarchical Data Format version 5) is a file format where data is stored in hierarchical structure ( https://portal.hdfgroup.org/ ). This format is adopted as one of the formats for tetrahedral-mesh geometry in PHITS.
The PHITS executables contained in the PHITS package were prepared to work without installing HDF5. Thus, installation of HDF5 is NOT required just to use PHITS with HDF5 files. Recompilation of PHITS with disabling the HDF5 function also does not require the HDF5 installation. The following procedures are required ONLY when you want to recompile PHITS with enabling HDF5 function.
Windows
Phase I: Download HDF5 library and tools.
I-1 Access to download site of HDF. ( https://portal.hdfgroup.org/downloads/index.html ).
I-2 Download the latest version of HDF.
I-3 Unzip the downloaded package.
I-4 Copy these three folders into phits/utility/HDF5 or remember the path to modify the following settings.
Phase II: Modify the PHITS project file for Visual Studio.
Note: Installation of Intel OneAPI and Visual Studio is required. Please install them following the instruction given in phits/document/Install-IntelFortran-OneAPI-en.pdf.
For the compilation using makefile, please follow the instruction for Linux.
II-0 Launch Visual Studio
II-1 Select the PHITS project file.
From "Open a project or solution", open phits/bin/phits-intel.vfproj.
II-2 Add HDF5 lib folder into "Additional Library directory"
II-3 Add hdf5.lib and hdf5_fortran.lib to "Additional Dependencies"
Note: We do not know why but we failed in statistical linking with libhdf5.lib and libhdf5_fortran.lib. If you succeed in statistical linking of HDF5 libraries, please let us know!! To overcome this difficulty, some dll files are placed in phits/bin.
II-4 Add HDF5 Include and Mod/shared folders to "Additional include directories" and add hdf5 to "Preprocessor definitions".
III Create executable file by
Build > Build solution
To launch the created executable, from "send to" or "Run" from editor, open phits/bin/phits.bat with a text editor.
Modify the 3rd line to direct the new executable file and save this file.
Mac
Note: Phase I & II may be skipped by using Homebrew to install HDF5. Then the HDF installed path will be the path of Homebrew such as /opt/homebrew.
Phase I: Download HDF5 library and tools.
I-1 Access to download site of HDF. ( https://portal.hdfgroup.org/downloads/index.html ).
I-2 Download the latest version of HDF.
Phase II: Compile HDF5 from source.
II-1 Expand the hdf5-***.tar.gz file and install HDF5 following the instruction.
The instruction to install using "configure" & "make" is given in INSTALL_Auto.txt. For this installation, "--enable-fortran" and FORTRAN compiler specification "FC" are necessary at "configure".
For example, the following commands in the HDF5 directory
mkdir build
FC=ifort ./configure --prefix=build --enable-fortran
make
make install
make check-install
will create the HDF5 library and tools (bin/, include/, lib/, share/) in the "build" directory.
Copy include/ and lib/ directories into phits/utility/HDF5 or remember the installation path for the following "makefile" modification.
Note: In order to make an executable with linking the HDF5 library statistically, the dynamical libraries ***.dylib become obstacle. So ***.dylib should be deleted in lib directory to make a statistic-link executable. Please let us know better way if you know !!
Phase III: Modify "makefile" in phits/src for PHITS compilation.
III-1 Modify the environmental flag
III-2 Set "true" for USEHDF5 and adjust HDF5PATH to your environment.
Please see Sec. 10 of the PHITS manual for other optional flags such as parallelization.
Phase IV: The command "make" will create the executable in the parent directory.
Linux
Phase I: Download HDF5 library and tools.
I-1 Access to download site of HDF. ( https://portal.hdfgroup.org/downloads/index.html ).
I-2 Download the latest version of HDF.
Phase II: Compile HDF5 from source.
II-1 Expand the hdf5-***.tar.gz file and install HDF5 following the instruction.
The instruction to install using "configure" & "make" is given in INSTALL_Auto.txt. For this installation, "--enable-fortran" and FORTRAN compiler specification "FC" are necessary at "configure".
For example, the following commands in the HDF5 directory
mkdir build
FC=ifort ./configure --prefix=build --enable-fortran
make
make install
make check-install
will create the HDF5 library and tools (bin/, include/, lib/, share/) in the "build" directory.
Copy include/ and lib/ directories into phits/utility/HDF5 or remember the installation path for the following "makefile" modification.
Phase III: Modify "makefile" in phits/src for PHITS compilation.
III-1 Modify the environmental flag
III-2 Set "true" for USEHDF5 and adjust HDF5PATH to your environment.
Please see Sec. 10 of the PHITS manual for other optional flags such as parallelization.
Phase IV: The command "make" will create the executable in the parent directory.
END_BASIC_TEXT

[PPTX_CONTENTS]
NOTE: No .pptx files found.

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: sample/sample.inp

[BONUS_TEXT_FILES]
NOTE: Read these text files directly from the source folder.
FILE: sample/Readme.txt
