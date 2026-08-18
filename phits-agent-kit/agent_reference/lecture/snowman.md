# Lecture: exercise/snowman

SOURCE_FOLDER: D:/NEAgit/lecture/exercise/snowman
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: snowman
LECTURE_PATH_INDEX: lecture/exercise/snowman
PPTX_FILES: phits-snowman-en.pptx, phits-snowman-jp.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: snowman
SECTION_KEYWORDS: t-deposit, t-track, volume

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/exercise/snowman
LECTURE_PATH_INDEX: lecture/exercise/snowman
PPTX_FILES: phits-snowman-en.pptx, phits-snowman-jp.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 1
SLIDE_COUNT: 38
EXERCISE_SLIDE_COUNT: 0
BONUS_INPUT_COUNT: 6
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- snowman.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Melt a snowman by a proton beam
- SLIDE 02: Purpose of this exercise
- SLIDE 03: snowman.inp
- SLIDE 04: [Title]
- SLIDE 05: Flow chart of this exercise
- SLIDE 06: Geometry setup of a snowman
- SLIDE 07: Step 1: Construct a big ice ball
- SLIDE 08: (1) Geometry check
- SLIDE 09: Step 2: Construct a small ice ball
- SLIDE 10: (1) Add a spherical surface centering on z axis
- SLIDE 11: Step 3: Set aluminum plate
- SLIDE 12: Define aluminum (Al) at [material] section
- SLIDE 13: Step 4: Set proton beam condition
- SLIDE 14: [ P a r a m e t e r s ]
- SLIDE 15: Default PHITS output is normalized to per particle emitted from source
- SLIDE 16: Answer 5
- SLIDE 17: Step 6: Calculate beam current to melt central sphere by 1-second irradiation
- SLIDE 18: Answer 6
- SLIDE 19: Construct geometry and tally
- SLIDE 01: 陽子ビームで雪だるまを溶かそう
- SLIDE 02: 実習目的
- SLIDE 03: snowman.inpの確認
- SLIDE 04: [Title]
- SLIDE 05: 本演習の流れ
- SLIDE 06: 雪だるま体系の作成
- SLIDE 07: ステップ１：雪玉（大玉）を作る
- SLIDE 08: 大きい雪玉（半径20cm）を芯の周りに作る（中心 z = 0 cm）
- SLIDE 09: ステップ２：雪玉（小玉）を作る
- SLIDE 10: ステップ2の解答
- SLIDE 11: ステップ３：アルミプレートを乗せる
- SLIDE 12: ステップ3の解答
- SLIDE 13: ステップ４：陽子ビームのエネルギーを調整する
- SLIDE 14: ステップ4の解答
- SLIDE 15: PHITSの計算結果は線源が１つ発生する当たりに規格化されている
- SLIDE 16: ステップ５の解答
- SLIDE 17: ステップ６：雪だるまの芯を溶かすために必要となる電流を計算する
- SLIDE 18: ステップ６の回答
- SLIDE 19: 雪だるま体系を作り，それを陽子ビームで溶かすための最適な条件をPHITSで計算した

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: snowman.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Melt a snowman by a proton beam
Jul. 2026 revised
phits/lecture/exercise/snowman
SPEAKER_NOTES:
In this exercise, titled Let’s Melt a Snowman with a Proton Beam, we will run a simulation in which a proton beam is irradiated onto a snowman model.

Through this hands-on activity, you will gain more practical experience with PHITS, especially in how to create geometries and how to modify the energy of incident radiation.

In addition, we will use the PHITS output data to perform numerical analysis, so you can see how simulation results are processed and interpreted.

The PHITS input file used in this exercise has been provided in the directory

phits / lecture / exercise

Let’s get started and explore how a proton beam can melt a snowman through simulation.

--- SLIDE 02 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Purpose of this exercise
Let’s consider how realistic the beam rifle in Gundam is based on the current accelerator technology by performing proton transport simulation in snowman
Geometry setup
Change of source
Concept of normalization
Lecture on
Courtesy of D. Satoh at JAEA
SPEAKER_NOTES:
The purpose of this exercise is to explore how feasible a beam rifle
something that might sound futuristic but could have potential practical applications one day
would be with current science and technology.

To do this, we will carry out a numerical experiment in which we attempt to melt a snowman using a proton beam, and then evaluate the required conditions.

In the figure shown below, you can see an illustration of a snowman, along with a scene inspired by a famous Japanese anime character using a beam rifle to irradiate it.

In this exercise, we will use PHITS to simply model a similar situation and think about what irradiation conditions would be necessary for a proton beam to actually melt the snowman.

Through this study, we will learn how to create geometries, how to modify the source settings, and how to understand and apply the concept of normalization in simulations.

Let’s see what today’s contents and start this excercise.

--- SLIDE 03 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
snowman.inp
Basic setup
Projectile：
Geometry：
Tally：
track.eps
100-MeV proton (pencil beam with a radius of 1.0 cm)
Water sphere of a 5-cm radius at the origin
[t-track] fluence distribution
[t-deposit] absorbed dose (Gy/source) in water sphere
deposit.out
Definition of volume of sphere is necessary at [volume] section
…
x: Serial Num. of Region
y: Dose [Gy/source]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n
#  num    reg     volume        all      r.err
    1       1   5.2360E+02   2.9789E-11  0.0023
29.789 (pGy/source)
SPEAKER_NOTES:
Now, let’s take a closer look at the contents of the input file used in this exercise, snowman dot inp.

As the basic calculation condition, the simulation is set up so that 100 M e V protons are incident as a pencil beam with a radius of 1 cm.  In the three-dimensional geometry, a water sphere with a radius of 5 cm is placed at the origin. This sphere represents the core of snowman.

For the detectors, tallies, we have defined two types. To obtain the spatial distribution of particle flux, t-track is used. To calculate the absorbed dose inside the water sphere, t-deposit is defined. When we use t-deposit to calculate the absorbed dose within a specific region, the physical quantities are sampled using a region mesh. However, in order to obtain the dose in units of gray, we need to define the volume of the target region in the volume section of the input file. This step is essential for proper normalization of the absorbed dose.

Now, as a first step, let’s go ahead and run PHITS using snowman dot inp as the input file. After running the simulation, you will obtain two output files, track dot e p s and deposit dot out. If you open the track dot e p s file, you can see the spatial distribution of the particle flux. The proton beam is entering the snowman from the left-hand side, and you can visually confirm how it penetrates into the water sphere.

Next, let’s open deposit dot out and take a look at line 27. On this line, the absorbed dose per single proton is printed. You can confirm that each proton deposits a dose of 29.789 pico-gray in the defined region. With this information, we are now ready to move on to the next step of the analysis.
MENTIONED_INPUT_NAMES: snowman.inp

--- SLIDE 04 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
[Title]
 Title of the simulation
[Parameters]
 Define history number etc.
[Source]
 Define source
[Material]
 Define materials
[Surface]
 Define surfaces
[Cell]
 Define cells
[Volume]
 Define volume of cells
[T-Track]
 Draw particle trajectory
[T-Deposit]
 Calculate deposition energy
snowman.inp
II. Source
I. Geometry
III. Tally
   (Detector)
Sections in snowman.inp
SPEAKER_NOTES:
Let’s see the structure of snowman dot inp

First, you can define the 3D geometry by combining the material, cell, and surface sections.

In this exercise, you’ll modify these sections to gradually turn the water sphere into a snowman shape.

second, the source section defines the irradiation conditions. For this exercise, the initial setup uses 100 M e V protons. Later on, you’ll get a chance to try changing the proton beam energy.

Third, the detectors are set up with two types of tallies, t-track and t-deposit. Tallies are where you specify what physical quantities you want to observe. The t-track tally is used to get the flux spatial distribution, while the t-deposit tally calculates the absorbed dose inside the water sphere.

One thing to note: if you want to calculate the absorbed dose in Gray in a specific region using t-deposit, you also need to define that region in the volume section.
MENTIONED_INPUT_NAMES: snowman.inp

--- SLIDE 05 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Flow chart of this exercise
Set geometry of a snowman
Set beam condition
Determine beam current and power to melt a snowman
SPEAKER_NOTES:
Now, let see the flow of this exercise.

First, you’ll edit the material, cell, and surface sections to try making the 3D snowman geometry.

Once the snowman setup is complete, the next step is to adjust the irradiation conditions by modifying the source section.
This time, you’ll be changing the energy of the proton beam.

Finally, you’ll determine the beam current and output needed to melt the snowman.
In this part of the analysis, you’ll also work on rescaling the output from the tallies and doing some numerical calculations.

--- SLIDE 06 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Geometry setup of a snowman
Instruction
A simple structure with big and small ice balls, and an aluminum plate
Material of the ice balls is 1-g/cm3 water (without temperature option*)
The aluminum plate is placed on top of the small ice ball
The existing cells (cell numbers 1, 98, 99) should not be changed
Ideal geometry of snowman
(phits/sample/misc/snowman)
Geometry setup in this exercise
*Temperature option influence only motion of low-energy neutrons
SPEAKER_NOTES:
Let’s get started by making the snowman setup.

For the snowman, the left figure shows a realistic illustration. In this exercise, we won’t be creating such a detailed model. Instead, we’ll make a simple snowman like the one on the right, two snowballs of different sizes with an aluminum plate on top. If you’re curious, the realistic snowman model can be found in

phits / sample / misc / Snowman

So feel free to check it out.

To make the setup shown on the right, treat the snowballs as water with a density of 1 gram per cubic centimeter, and place the aluminum plate so that it fits perfectly on top of the smaller snowball.

Also, when you’re editing the input file, make sure not to change the existing cells, that is, cell numbers 1, 98, and 99.

--- SLIDE 07 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Step 1: Construct a big ice ball
Set a big ice ball (radius 20 cm, center at z = 0 cm)
surrounding the original 10-cm sphere
Hint
Geometry check can be done with icntl = 8
A spherical surface centering the origin is defined by ”so  radius”
Define the region of the big ice ball not to overlap the region of the original sphere of 5-cm radius (avoid double defined region)
Check *_geo.out when you encounter an error
SPEAKER_NOTES:
Step 1.

Start by editing the cell and surface sections of the Snowman input file you have. Place a large snowball with a radius of 20 cm at the origin, around the core, and build the 3D setup as shown in the figure.

Here’s a hint for checking your setup,
once you’ve made it, set icntl to 8 and run phits to verify the geometry.

Next, the sphere shown as 2 in the figure, centered at the origin with a radius of 20 cm, can be defined using S O radius.

A couple of important points
make sure the large snowball doesn’t overlap with the original 5 cm sphere. To do this, define the large snowball’s region excluding the 5 cm sphere, and also make sure it doesn’t overlap with the vacuum region, so remove the large snowball’s region from the vacuum as well.
It’s noted in red in the instructions, but if you accidentally double-define a region, you can check it in the _geo dot out file.

--- SLIDE 08 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
(1) Geometry check
(2) Add a spherical surface centering the origin in [surface]
(3) Define a cell for the big ice ball in [cell] (Be careful with double defined)
Answer 1
Set a big ice ball (radius 20 cm, center at z = 0 cm)
surrounding the original 10-cm sphere
[ P a r a m e t e r s]
 icntl    =      8
 maxcas   =        2000
 maxbch   =           1

[ S u r f a c e ]
   1   so     5.0
   2   so    20.0
 999   so   200.0

[ C e l l ]
 1   %WATER%  0.0  -1   $ Target
 2   %WATER%  0.0  -2  1 $ Big ball
98   0       #all  -999  $ Void
99  -1              999  $ Outer region
(1)
(2)
(3)
SPEAKER_NOTES:
Here’s an example of how to complete Step 1.

In this step, we’ll make a new large snowball with a radius of 20 cm, centered at z = 0 cm.

First, in the initial setup, particles are set to transport by default. To check the geometry, change icntl to 8 in the parameter section. This allows you to check the setup of geometry.

Second, in the surface section, add surface number 2 to define a sphere with a radius of 20 cm.
A sphere centered at the origin is defined using SO, so for this case, you would write 2 S O 20.

Third, in the cell section, define the large snowball. Make sure to subtract the region of the original small sphere, region 1, from the large snowball, region 2, so they don’t overlap.

Similarly, to prevent the large snowball from overlapping with the void region, add #ALL to cell 98. You could also write #1 #2, but using #ALL removes all overlapping parts at once.

Then let’s run phits using this modified input file. After it finishes, open track dot eps and you should see an image matching the figure, confirming that the geometry was set up correctly.

--- SLIDE 09 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Step 2: Construct a small ice ball
Set a small ice ball on top of the big ice ball
(radius 15 cm, center at z = -25 cm)
Hint
A spherical surface centering on z axis is defined by
”sz  center-z-position  radius”
Exclude the region of big ice ball from small ice ball or vise versa, otherwise double defined region is created by two ice balls
SPEAKER_NOTES:
Step 2.
Next, we’ll edit the Snowman input file again to add a smaller snowball with a radius of 15 cm at z = -25 cm, sitting on top of the large snowball, creating the geometry shown in the figure.

Here’s a hint for defining the geometry.
A sphere centered along the z-axis can be defined using s z radius.

Be careful, using S O radius only works for spheres centered at the origin.

Also, just like in Step 1, you can’t simply add the small sphere on top of the large one. If you do, the two spheres will overlap and you’ll get a double definition. To avoid this, remove the region of the large snowball from the small one.

--- SLIDE 10 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
(1) Add a spherical surface centering on z axis
(2) Define a cell for the small ice ball in [cell] (Be careful with double defined)
Answer 2
Set a small ice ball on top of the big ice ball
(radius 15 cm, center at z = -25 cm)
[ S u r f a c e ]
   1   so     5.0
   2   so    20.0
   3   sz   -25.0 15.0
 999   so   200.0

[ C e l l ]
 1   %WATER%  0.0  -1       $ Target
 2   %WATER%  0.0  -2  1   $ Big ball
 3   %WATER%  0.0  -3  2   $ Small ball
98   0       #all -999  $ Void
99  -1              999           $ Outer region
(2)
(1)
SPEAKER_NOTES:
Here’s an example of how to complete Step 2.

In this step, we’ll add the small snowball with a radius of 15 cm on top of the large snowball. The center of the small snowball will be at z = -25 cm.

First, in the surface section, add surface number 3 and define the 15 cm sphere using S Z radius.

Second, in the cell section, define the small snowball. Just like in Step 1, be careful to avoid overlapping with the void region. Since in the previous step you added #ALL to cell 98, you don’t need to add #3 this time. However, if you used #1 #2 before, then you should add #3 here.

After editing, please execute phits using the modified input file. When it’s done, open track dot e p s and you should see an image matching the figure, confirming that the geometry was set up correctly.

--- SLIDE 11 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Step 3: Set aluminum plate
Define aluminum (Al) at [material] section
Put an aluminum plate of a 10-cm radius and 4-cm thickness
(-40 cm < z < -36 cm) on top of the small ball
Hint
A cylindrical surface along the z axis is defined  by “cz  radius”
A plane perpendicular to z axis is defined by ”pz  z-position”
Predefined material name of Al is @ALUMINUM@
Exclude region of the aluminum plate from that of the small ice ball
SPEAKER_NOTES:
Step 3

Next, we’ll edit the Snowman input file to define aluminum in the material section and create a cylindrical aluminum plate with a radius of 10 cm and a thickness of 4 cm, making the geometry shown in the figure.

Here’s a hint for defining the geometry.

A cylinder parallel to the z-axis can be defined using C Z radius, and a plane perpendicular to the z-axis can be defined using P Z z coordinate. If you’re defining materials by mass density, remember to use a negative number.

The predefined material name of aluminum is at aluminum at. Also, make sure to remove the aluminum plate region from the snowball region so that the plate is embedded in the snowball without any overlapping or double definition.

--- SLIDE 12 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Define aluminum (Al) at [material] section
Put an aluminum plate on top of the small ball
Answer 3
(1) Define aluminum at [material] section
(2) A cylindrical surface along the z axis
(3) Two planes perpendicular to the z axis
(4) Define the region of aluminum plate
(5) Exclude the aluminum plate from the small ball
[ M a t e r i a l ]
MAT[ 1 ]  @WATER@
MAT[ 2 ]  @ALUMINUM@

[ S u r f a c e ]
   1   so     5.0
   2   so    20.0
   3   sz   -25.0 15.0
  11   cz    10.0
  21   pz   -40.0
  22   pz   -36.0
 999   so   200.0

[ C e l l ]
 1   %WATER%  0.0  -1     $ Target
 2   %WATER%  0.0  -2  1  $ Big ball
 3   %WATER%  0.0  -3  2  #4  $ Small ball
 4   %ALUMINUM%  0.0  -11 21 -22  $ Al plate
98   0       #all  -999  $ Void
99  -1              999  $ Outer region
(1)
(2)
(3)
(4)
(5)
SPEAKER_NOTES:
Here’s an example of how to complete Step 3.

In this step, we’ll define aluminum in the material section and create a cylindrical aluminum plate with a radius of 10 cm and a thickness of 4 cm.

First, in the material section, add mat2 and define aluminum as a new material.

Second, in the surface section, add surface number 11 and define a cylindrical surface. This defines an infinite cylinder along the z-axis.

Third, add surface numbers 21 and 22 to define the top and bottom planes of the cylinder at z = -40 cm and z = -36 cm, respectively.

Since these planes are perpendicular to the z-axis, they can be defined using P Z z coordinate.

Fourth, in the cell section, define the aluminum plate. Up to now, we have been using material number 1, water with a density of 1.0 gram per cubic cm.

Here, we’ll use the newly defined material number 2, aluminum with a density of 2.7  gram per cubic cm.

Fifth, to prevent overlap between the small snowball and the aluminum plate, add #4 at the end of cell number 3. Also, make sure the aluminum plate doesn’t overlap with the void region, but since we added #ALL to cell 98 in the previous step, any overlap is already avoided.

After editing, please run phits. Once it finishes, open track dot e p s and you should see an image matching the figure. At this point, you’ve completed making the 3D snowman geometry required for this exercise.

From here on, we’ll move on to simulating the proton beam irradiating the snowman using the simple setup you’ve created.

--- SLIDE 13 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Step 4: Set proton beam condition
Tune the proton beam energy maximize the absorbed dose of cell No.1
Hint
Transport calculation can be executed with icntl = 0
Beam energy is given by e0 parameter at [source] section
Absorbed dose at central sphere can be checked by deposit.out
Proton absorbed dose is maximized at the Bragg peak
SPEAKER_NOTES:
Step 4

Next, we’ll increase the proton beam energy and adjust the input file so that the absorbed dose in cell number 1, the core region, is maximized.

To change the energy, you’ll need to edit the source section of the input file.

Here’s a hint,
First, to run particle transport, set ICNTL to 0.

Then, to adjust the incident energy, simply change the value of e0 in the source section.

You can check the absorbed dose in the core by looking at deposit dot out.

Since the absorbed dose from protons is highest near the Bragg peak, your goal is to adjust the proton beam energy so that the Bragg peak lines up with the position of the core.

--- SLIDE 14 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
[ P a r a m e t e r s ]
icntl    =           0
[ S o u r c e ]
totfact =   1.0000
 s-type =   1
    proj =   proton
      e0 =   200.00
      r0 =   1.0000
Change the icntl parameter
Change e0 parameter
Check the phits output files
       ・  track.eps
       ・  deposit.out (the 27th line)
Answer 4
Find a proton beam energy so that the absorbed dose at central sphere is maximized
(3) Check the output file
SPEAKER_NOTES:
Here’s an example of how to complete Step 4.

In this step, we’ll adjust the proton beam energy so that the absorbed dose in the core is maximized.

First, to enable particle transport, change ICNTL to 0. This allows the particles to actually move through the geometry.

Next, to adjust the proton energy, change e0 in the source section.

For example, try increasing it from 100 M e V to 200 M e V. After making the change, run phits and open track dot e p s to check the results.

By looking at where the protons stop, you’ll see that they currently stop near the large snowball. You can check the absorbed dose in the core by looking at line 27 in deposit dot out.

Repeat this process, adjusting the proton energy each time, until the Bragg peak of the proton beam lines up with the core position.

Eventually, by setting the proton energy to about 293 M e V, you should see that the Bragg peak coincides with the core, as shown in the figure.

--- SLIDE 15 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Default PHITS output is normalized to per particle emitted from source

Set totfact at [source] section to change the normalization factor

1 Ampere = 1 Coulomb / 1 second
The electric charge of a proton is 1.6x10-19 Coulomb
Step 5: Normalize the result
Calculate absorbed dose (Gy) by 1-second irradiation of a proton beam with current of 1 Ampere (A)
Hint
Maxcas and maxbch control only statistical uncertainty, and they have no relation with normalization
e.g. Absorbed dose for 100 source particles is given by setting totfact = 100.0
SPEAKER_NOTES:
Step 5

Next, in Step 5, we’ll learn about renormalization.

Here, we’ll adjust the beam current to calculate the absorbed dose in the core for a 1 ampere beam irradiating for 1 second.

Originally, the calculations in phits are normalized per particle. That means MAXCAS and MAXBCH only affect calculation precision. They don’t affect the normalization.

If you want to simulate multiple particles, you need to change the TOTFACT parameter in the source section.

For example, if you want to calculate the absorbed dose for 100 protons, set TOTFACT = 100. Essentially, you calculate the number of protons generated by a 1 ampere current and then enter that number into TOTFACT.

Here’s a quick reminder, 1 ampere corresponds to 1 coulomb of charge per second, and each proton carries a charge of one point six times ten to the negative nineteen 1 coulomb.

--- SLIDE 16 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Answer 5
Check the scale change with totfact
Number of emitted protons for 1 ampere in 1 second is
1.0 / 1.6E-19 = 6.25E18 (particles)
Absorbed dose with totfact = 6.25E18 is 1.28E8 (Gy) (for 293-MeV protons)
[ S o u r c e ]
  totfact =   1.0/1.6e-19   # (D=1.0) global factor
h:   x      n     n          y(all     ),l3 n
#  num    reg     volume       all       r.err
    1       1   5.2360E+02   1.2785E+08  0.0178
deposit.out （27行目）
snowman.inp
track.eps
SPEAKER_NOTES:
Now, let’s go over the solution for Step 5.

First, to calculate the number of protons generated when irradiating with 1 ampere for 1 second, simply divide 1 ampere into 1 coulomb by the charge of a single proton.

That is, 1 divided into one point six times ten to the negative nineteen coulomb equals to 6.25 times ten to the eighteen protons.

By entering this number into TOTFACT in the Snowman input file, all previous results are rescaled. This allows phits to calculate the absorbed dose for a 1 ampere beam irradiating for 1 second.

Next, run phits using the modified input file.

After the run, open track dot e p s and you’ll see that the flux scale has changed, as shown in the figure.

Then, check deposit.dot out, you should see the absorbed dose in the core as approximately 1.28 times ten to the eight in Gray.

Comparing this to the initial phits result of 29 pico gray, you can see that the results have been successfully rescaled to reflect the effect of multiple protons hitting the target.
MENTIONED_INPUT_NAMES: snowman.inp

--- SLIDE 17 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Step 6: Calculate beam current to melt central sphere by 1-second irradiation
Assume the snowman is made of ice at -10C
Calculate the proton beam current (A) and the power (MW) necessary to melt the central ice by 1 second
Hint (assumption for simplicity)
Specific heat of ice is 0.5 (cal/g/K) = 2.1 (J/g/K)
Latent heat of ice (heat necessary for phase transition from ice to water) is 333.5（J/g）
1Gy = 1（J/kg） = 0.001（J/g）
Beam power (MW) can be estimated by
Particle energy (MeV)  Beam current (A)
For comparison…
The maximum power of J-PARC (one of the most powerful accelerators in the world) is approximately 1 MW
*In a strict sense, acceleration voltage (MV) x beam current (A)
SPEAKER_NOTES:
Step 6

Finally, in Step 6, we’ll calculate the beam current needed to melt the core of the snowman.

For this calculation, assume the snowman is made of ice at minus 10 degrees centigrade.

The goal is to determine, by hand, the beam current, ampere, and beam power, watt, required to heat the ice to 0 degrees centigrade and melt it completely in 1 second.

Here are some hints for the calculation.

The specific heat of ice is 0.5 calorie per gram par kelvin, which equals 2.1 jules per gram per kelvin.

The latent heat of ice, heat necessary for phase transition from ice to water, is 333.5 jules per gram. And 1 gray equals to 1 jule per kilogram equals to 0.001 jules per gram.

Beam power in megawatts can be calculated as

Power, megawatt equals particle energy M e V times beam current, ampere

For reference, Japan’s highest-power accelerator, J-PARC, has a maximum beam power of about 1 megawatt. You can use this as a benchmark to see whether it would be enough to melt the snowman’s core.

--- SLIDE 18 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Answer 6
Melting a snowman is all we can do with current accelerators

Gundam’s beam rifle is far beyond current technology !
(Nonetheless, we can melt metals with longer irradiation)
How large is the absorbed dose in central sphere by a 293-MeV proton beam with 1 A in 1 second?
How large is the heat needed to heat up the ice by 10 K and melt the ice?
What current is required to give that heat in 1 second?
How large is the power at this beam current?

       To be precise,
      [ 293 (MeV/particle) x 1.6E-19 (J/eV) ] x [ 2.77E-3 (C/s) / 1.6E-19 (C/particle) ] = 0.811 (MJ/s)
								  = 0.811 (MW)
≒ Maximum power of the biggest accelerator facilities (1MW)
1.28E8（Gy/A）＝1.28E5（J/g/A）
2.1（J/g/K） x 10（K) + 333.5（J/g） = 354.5（J/g）
354.5（J/g） / 1.28E5（J/g/A） = 2.77E-3（A）
293 (MeV)     x     2.77E-3 (A)     = 0.811 (MW)
Conversion from eV to Joule
Amount of proton charge
SPEAKER_NOTES:
Now, let’s go over the calculation flow and the hand-calculated results for Step 6.

First, we calculate the absorbed dose in jules per gram for a 293 M e V proton beam at 1 ampere for 1 second.

This gives, 1.28 times ten to the five jules per gram per ampere.

Next, we calculate the total heat required to raise the ice temperature by 10 kelvin and melt it. Using the specific heat of ice, 2.1 jules per gram per kelvin, multiplied by 10 kelvin, plus the heat of fusion, 333.5 jules per gram , we get

354.5  jules per gram

Third, we calculate the beam current needed to deliver this energy in 1 second

333.5 jules per gram divided into 1.28 times ten to the five jules per gram per ampere equals 2.77 times ten to the negative three ampere

Finally, we calculate the beam power at this current as

0.811 mega watt

For comparison, this is roughly equivalent to the maximum beam power of J-PARC, about 1  mega watt
From this, we can conclude that with current accelerator technology, melting the snowman is about the limit.

To create a beam capable of blasting a Gundam-class mobile suit, we’d still need significant technological advances.

However, this calculation also shows that with longer irradiation times, it is possible to melt metals as well.

--- SLIDE 19 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
Construct geometry and tally
Define source particles
Normalize the tally results
Summary
PHITS simulation should be conducted with following order:
SPEAKER_NOTES:
Summary of the Exercise

In this exercise, we tried to make the snowman geometry and used a proton beam to calculate the optimal conditions to melt it using the phits code.

Remember that phits tally results are normally normalized per source.

To simulate real irradiation conditions, you need to rescale the tally results using the TOTFACT parameter.

That’s all. Thank you very much for listing to the video of exercise snowman.

--- SLIDE 01 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
陽子ビームで雪だるまを溶かそう
2026年7月改訂
phits/lecture/exercise/snowman
SPEAKER_NOTES:
この演習では、「プロトンビームで雪だるまを溶かそう」というタイトルで、雪だるまへプロトンを照射する シミュレーションを行います。

この演習を通じて、これまでフィッツで生んだ、ジオメトリの作成方法や、放射線のエネルギーの変更方法についてより実践的に学び、フィッツの出力結果を使用した数値解析を行います。

この演習で使用するフィッツのインプットファイルは、フィッツ/lecture/exerciseのディレクトリに配布されています。

--- SLIDE 02 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
実習目的
将来，実用化が期待される（？）ビームライフルが現在の技術でどの程度実現可能か，陽子ビームで雪だるまを溶かす数値実験を行って検討してみよう
ジオメトリの作成
線源の変更
規格化の概念
について
実習します
写真提供：佐藤大樹氏
SPEAKER_NOTES:
この実習の目的は、将来、実用化の可能性のある、ビームライフルが、現在の科学技術で、どの程度、実現可能か、プロトンビームで雪だるまを溶かす数値実験を行い、検討することです。

下の図には、雪だるまのイラストと、日本のアニメで有名なガンダムがビームライフルを使用して照射している様子が描かれています。このようなシチュエーションをフィッツで簡単に模擬し、雪だるまを溶かすプロトンビームの照射条件を考えてみます。

この検討の中で、ジオメトリの作成、センゲンの変更、規格化の概念について学んでいきます。

--- SLIDE 03 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
snowman.inpの確認
基本計算条件
入射粒子：
体系：
タリー：
track.eps
100MeV陽子（半径1.0cmのペンシルビーム）
原点に半径5cmの水
[t-track]によるフラックス空間分布
[t-deposit]による水球内の吸収線量(Gy/source)
deposit.out
…
x: Serial Num. of Region
y: Dose [Gy/source]
p: xlin ylog afac(0.8) form(0.9)
h:   x      n     n          y(all     ),l3   n
#  num    reg     volume        all      r.err
    1       1   5.2360E+02   2.9784E-11  0.0023
29.784 (pGy/source)
[volume]セクションで体積を定義する必要有り
SPEAKER_NOTES:
この実習で使用する、snowman ドット インプの中身について確認します。基本計算条件として、100 メブのプロトンが、半径1.0センチメートルのペンシルビームで入射する設定になっています。3次元体系には、原点に半径5センチメートルの水球が配置されています。

検出器であるタリーには、フラックス空間分布を得るためにt-trackが、水球内の吸収線量を計算するためにt-depositが定義されています。t-depositを用いて、特定の領域内の吸収線量を計算する際には、リージョンメッシュで物理量をサンプリングしますが、単位としてグレイを計算するには、計算対象の領域の体積を、volumeセクションで定義する必要があります。

ここで、まず最初に、スノーマン. ドット インプをインプットファイルとしてフィッツを実行してみましょう。
 
実行すると、トラック ドット イーピーエスと、depositドット アウトの2種類の出力ファイルが得られます。trackドット イーピーエスファイルを確認すると、フラックス空間分布が描写されています。左側からプロトンビームが雪だるまへ入射しています。

次に、depositドット アウトを開いて、そのファイルの27行目を確認してみましょう。27行目には、プロトン一本当たりの線量が出力されており、プロトン一本当たりで29.789 ピコグレイの線量が付与されたことが確認できます。

--- SLIDE 04 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
[Title]
 計算のタイトル
[Parameters]
 ヒストリ数・核データの定義など
[Source]
 線源の定義
[Material]
 物質の定義
[Surface]
 面の定義
[Cell]
 容れ物の定義
[Volume]
 容れ物の体積の定義
[T-Track]
 飛跡の描画
[T-Deposit]
 吸収線量の計算
snowman.inp
snowman.inpの構成
SPEAKER_NOTES:
snowmanドット インプの構成は、4ページ目のようになっています。

まず、マルイチでは、materialセクション、cellセクション、surfaceセクションを組み合わせて、３次元体系を定義することができます。この実習では、これらのセクションを書き換えることで、水球を雪だるまに作り変えていきます。

次に、マルニのsourceセクションには、照射条件が定義されています。今回の場合、初期設定では、100メブのプロトンが設定されています。後半では、プロトンビームのエネルギー変更にトライしてもらいます。

さらに、マルサンの検出器では、t-trackとt-depositの、2種類のタリーが設定されています。タリーは観察したい物理量について設定する部分で、フラックス空間分布を得るためにt-trackが、水球内の吸収線量を計算するためにt-depositが定義されています。注意すべきこととして、t-depositにて、水球内、特定領域内の吸収線量 グレイを計算するため、volumeセクションを定義する必要があります。
MENTIONED_INPUT_NAMES: snowman.inp

--- SLIDE 05 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
本演習の流れ
雪だるま体系を作る
照射条件を調整する
雪だるまを溶かすために必要となるビーム電流・出力を決定する
SPEAKER_NOTES:
では、この演習の流れを説明します。

はじめに、materialセクション、cellセクション、surfaceセクションを編集していくことで、雪だるまの3次元体系の作成に挑戦してもらいます。

雪だるまの体系を完成させたのち、次に、sourceセクションを編集することで照射条件を調整します。今回は、プロトンビームのエネルギーを変更していきます。

そして最後に、雪だるまを溶かすために必要となるビーム電流・出力を決定します。この解析では、タリーによる出力結果の再規格化や、数値解析を行なっていきます。

--- SLIDE 06 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
雪だるま体系の作成
方針
大小２つの雪玉にアルミプレートを乗せたシンプルなものとする
雪玉は，密度１g/cm3の水とする（温度の指定はしない*）
アルミプレートは，小玉の上にピッタリと乗せる
元々定義されているターゲット（領域１）、真空（領域98）、外部ボイド（領域99）は変更しない
この実習で作成するジオメトリ
*温度は，低エネルギー中性子の挙動にのみ影響する
理想的な雪だるま体系
(phits/sample/misc/snowman)
SPEAKER_NOTES:
早速、雪だるまの体系を作りましょう。

雪だるまの体系ですが、左図にリアルな雪だるまのイラストが載っています。本実習では、このようなリアルな体系を作成せず。右の図に示すように、大小２つの雪玉にアルミプレートを乗せた、シンプルなものとします。なお、リアルな雪だるまはフィッツ サンプル ミス スノーマン にありますので、興味のある方はご確認ください。

右図の体系を作成するにあたり、雪玉は，密度１グラムパー立方センチメートルの水とし、アルミプレートは小玉の上にピッタリと乗せることとします。

--- SLIDE 07 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ１：雪玉（大玉）を作る
大きい雪玉（半径20cm）を芯の周りに作る（中心 z = 0 cm）
ヒント
ジオメトリの描画はicntl = 8
原点を中心とした球面は”so 半径”で定義
元からあった半径5cmの球の領域と重ならない（二重定義を防ぐ）ように大玉の領域から半径5cmの球の領域を除く
二重定義が出たら*_geo.outファイルをチェック
SPEAKER_NOTES:
ステップ１です。

現在手元にある、snowmanドット インプの、cellセクションとsurfaceセクションを編集して、原点に半径20㎝の大きい雪玉を、芯の周辺に配置し、図に示すような3次元体系を作ります。

体系作成のヒントですが、まず、作成した体系は、アイシーエヌティーエルを8に設定し、フィッツを実行することで確認できます。

次に、図の2番で示される、原点を中心とした半径20㎝の球面は、s o 半径、で定義することが可能です。

ここで注意点として、元からあった半径5cmの球の領域と重ならないように、大玉の領域から、半径5cmの球の領域を除き、さらに、大玉と真空も重ならないよう、真空から、大玉の領域を除くよう、定義してください。

赤字で記載されていますが、二重定義となってしまった場合、*アンダーバー ジオ ドット アウトファイルで確認することが可能です。

--- SLIDE 08 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
大きい雪玉（半径20cm）を芯の周りに作る（中心 z = 0 cm）
ステップ1の解答
[ P a r a m e t e r s]
 icntl    =      8
 maxcas   =        2000
 maxbch   =           1

[ S u r f a c e ]
   1   so     5.0
   2   so    20.0
 999   so   200.0

[ C e l l ]
 1   %WATER%  0.0  -1   $ Target
 2   %WATER%  0.0  -2  1 $ Big ball
98   0       #all  -999  $ Void
99  -1              999  $ Outer region
(1)
(1) ジオメトリの描画
(2) [surface]セクションに原点を中心とした球面を”so 半径”で追加
(3) [cell]セクションに大玉を追加（二重定義に注意）
(2)
(3)
SPEAKER_NOTES:
では、ステップ１の回答例を示します。

このステップでは、新たに、大きい雪玉 半径20cm を中心 z = 0 cm に作ります。

まず、1番目に、初期設定では粒子が輸送する設定になっているので、カッコ１のように parameterセクションのアイシーエヌティーエルを8に変更します。これにより、体系が確認できるようになります。

2番目に、surfaceセクションに、カッコ２のように surface番号２を追加して、半径20cmの球面を定義します。原点を中心とした球面は、s o で表現し、今回は半径が20 cmですので、2 s o 20 と記載します。

3番目に、cellセクションで、カッコ３のように大玉を定義します。この際、大玉と水球、こだま領域が二十定義とならないように、領域2から領域1を取り除くようにしてください。

同様に、大玉とvoid領域が二十定義とならないように、ハッシュマーク オール、を98番のcellに記載します。ハッシュマーク 1、ハッシュマーク2と記載しても良いのですが、ハッシュマーク オールと記載することで、重複部分を全て取り除くことができます。

では、変更したこのインプットファイルを使用して、フィッツを実行します。実行後、trackドット イーピーエスを開くと、図と同じ画像が得られ、正しくジオメトリを組めたことが確認できます。

--- SLIDE 09 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ２：雪玉（小玉）を作る
小さい雪玉（半径15cm）を大きい雪玉の上に乗せる（中心 z = -25cm)
ヒント
ｚ軸上を中心とした球面は”sz  中心z座標  半径”で定義
２つの雪玉が重なってニ重定義になってしまうので，小玉から大玉の領域を除く（もしくは逆でもよい）
SPEAKER_NOTES:
ステップ2です。

次に、snowmanドット インプをさらに編集して、z=-25cmの位置に、半径15㎝の小さい雪玉を、大きい雪玉の上に乗せた、図に示すようなジオメトリを、作成します。

体系作成時のヒントですが、ｚ軸上を中心とした球面は、s z  中心z座標  半径 により定義することができます。注意してほしいことは、s o 半径 では原点を中心とした球のみ定義可能でした。

また、ステップ１と同様ですが、単純に球体を追加するだけですと、図に示しているように、２つの雪玉が重なり、二重定義となってしまうため，小玉から大玉の領域を除いてください。

--- SLIDE 10 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ2の解答
[ S u r f a c e ]
   1   so     5.0
   2   so    20.0
   3   sz   -25.0 15.0
 999   so   200.0

[ C e l l ]
 1   %WATER%  0.0  -1       $ Target
 2   %WATER%  0.0  -2  1   $ Big ball
 3   %WATER%  0.0  -3  2   $ Small ball
98   0       #all -999  $ Void
99  -1              999           $ Outer region
(2)
(1)
(1)  [surface]セクションにｚ軸上を中心とした球面を ”sz  中心z座標  半径” で追加
(2)  [cell]セクションに小玉を追加（二重定義に注意）
小さい雪玉（半径15cm）を大きい雪玉の上に乗せる（中心 z = -25cm)
SPEAKER_NOTES:
では、ステップ２の回答例を示します。

このステップでは、小さい雪玉 半径15cm を大きい雪玉の上に乗せます。ただし、追加する小さい雪玉は、中心 z = -25cmに設置することになります。

1番目に、surfaceセクションに、カッコ１のようにsurface番号3を追加して、s z  中心z座標  半径 で 半径15㎝の球面を定義します。

2番目に、cellセクションで、カッコ２のように 小玉を定義します。先ほどのステップ1と同様に、小玉とvoid領域が二十定義とならないように注意してください。前のステップで、ハッシュマーク オール、と98番のcellに記載したため、新たにハッシュマーク 3 と記載する必要はありませんが、ハッシュマーク 1、ハッシュマーク2 と記載された方は、ハッシュマーク 3 を追記してください。

編集後、フィッツを実行してみましょう。 実行後、trackドット イーピーエスを開くと、図と同じ画像が得られ、正しくジオメトリを組めたことが確認することが可能です。

--- SLIDE 11 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ３：アルミプレートを乗せる
[material]セクションでアルミ（Al）を定義する
半径10cm，厚さ4cmの円柱アルミプレートを作る（-40cm < z < -36cm）
ヒント
z軸に平行な円柱面は”cz 半径”で定義
z軸に垂直は平面は”pz  z座標”で定義
アルミの既定物質名は@ALUMINUM@
雪玉領域からアルミプレート領域を除くことにより雪玉に埋め込む
SPEAKER_NOTES:
ステップ３です。

さらにsnowmanドット インプを編集して、materialセクションでアルミを定義し、半径10cm，厚さ4cmの、円柱アルミプレートを作成し、図に示すようなジオメトリを作成します。

体系作成時のヒントですが、z軸に平行な円柱面は、c z 半径 で定義し、z軸に垂直な平面は、p z  z座標 で定義することが可能です。なお、重量密度で定義する場合は、マイナスの数値にて記載する必要があります。

アルミの既定物質名はアット アルミニウム アットです。さらに、雪玉領域からアルミプレート領域を除いて、雪玉にアルミプレートを埋め込むため、アルミプレートと雪玉が二重定義とならないよう注意してください。

--- SLIDE 12 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ3の解答
[material]セクションでアルミ（Al）を定義する
半径10cm，厚さ4cmの円柱アルミプレートを作る（-40cm < z < -36cm）
[ M a t e r i a l ]
MAT[ 1 ]  @WATER@
MAT[ 2 ]  @ALUMINUM@

[ S u r f a c e ]
   1   so     5.0
   2   so    20.0
   3   sz   -25.0 15.0
  11   cz    10.0
  21   pz   -40.0
  22   pz   -36.0
 999   so   200.0

[ C e l l ]
 1   %WATER%  0.0  -1     $ Target
 2   %WATER%  0.0  -2  1  $ Big ball
 3   %WATER%  0.0  -3  2  #4  $ Small ball
 4   %ALUMINUM%  0.0  -11 21 -22  $ Al plate
98   0       #all  -999  $ Void
99  -1              999  $ Outer region
(1) [material]セクションでアルミ（Al）を定義
(2) z軸に平行な円柱面を”cz 半径”で追加
(3) z軸に垂直は平面を”pz  z座標”で追加
(4) アルミプレートを追加
(5) 小玉からアルミプレート領域を除く
(1)
(2)
(3)
(4)
(5)
SPEAKER_NOTES:
では、ステップ３の回答例を示します。

このステップでは、materialセクションでアルミを定義し、半径10cm，厚さ4cmの円柱アルミプレートを作ります。

1番目に、materialセクションにおいて、カッコ１のようにmat2を追加し、アルミニウムの物質を追加します。

2番目に、surfaceセクションに、surface番号11 を追加して、カッコ２のように円柱面を定義します。これにより、Z軸に無限長の円柱を定義することができます。

3番目に、surface番号21と22を追加して、円柱面のジョウメン zイコールマイナス40 cm と カメン zイコールマイナス36 cm を定義します。Z軸に垂直な面の定義には、pz z座標 で定義可能なため、カッコ3のように定義します。

4番目に、cellセクションで、アルミプレートを定義します。これまで、material番号１ 密度1.0グラムパー立法センチメートルの水を使用してきましたが、ここでは、新たに定義したmaterial番号２ 密度2.7グラムパー立法センチメートル のアルミを使用します。

5番目に、小玉とアルミプレートが二十定義とならないように、cell番号3の最後に、ハッシュマーク４ と記載を加えます。さらに、アルミプレートもvoid領域が二十定義とならないように注意しますが、先のステップで、ハッシュマーク オール、と98番のcellに記載したため、これで二十定義の回避はできています。

編集後、フィッツを実行します。実行後、trackドット イーピーエスを開くと、図と同じ画像が得られます。ここまでの作業で、この演習で必要な雪だるまの3次元体系の作成を終えました。

次からは、作成したシンプルな体系の雪だるまに対し、プロトンビームを照射するシミュレーションを行っていきます。

--- SLIDE 13 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ４：陽子ビームのエネルギーを調整する
陽子ビームのエネルギーを調整し，芯での吸収線量が最も大きくなるようにする
ヒント
粒子輸送を実行するにはicntl = 0とする
入射エネルギーは[source]セクションのe0パラメータで決定
芯での吸収線量はdeposit.outで確認
陽子による吸収線量はブラッグピーク付近で最も高くなる
SPEAKER_NOTES:
ステップ4です。

次に陽子線ビームのエネルギーを大きくし、cell番号1の、芯領域に対する吸収線量が最も大きくなるよう、インプットファイルを調整しましょう。

エネルギー調整を行うには、sourceセクションを編集する必要があります。

ヒントですが、まず、粒子輸送を実行するには、アイシーエヌティーエルを 0に変更します。

次に、入射エネルギーを調整するには、sourceセクションのe0の数値を変えることで変更することができます。

芯に付与される吸収線量は、depositドット アウトで確認できます。

陽子線による吸収線量はブラッグピーク付近で最も高くなることから、最終的には、芯の位置とブラッグピーク位置が重なるように、プロトンビームのエネルギーを調整しましょう。

--- SLIDE 14 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ4の解答
[ P a r a m e t e r s ]
icntl    =           0
[ S o u r c e ]
totfact =   1.0000
 s-type =   1
    proj =   proton
      e0 =   200.00
      r0 =   1.0000
陽子ビームのエネルギーを調整し，芯での吸収線量が最も大きくなるようにする
(1)
(2)
粒子輸送を実行できるよう変更
陽子線のエネルギーを調整
出力結果の確認
       ・  track.eps
       ・  deposit.out (27行目)
track.eps
(3) 出力結果の確認
SPEAKER_NOTES:
では、ステップ４の回答例を示します。

ここでは、芯での吸収線量が最も大きくなるように、陽子ビームのエネルギーを調整していきます。

まず、粒子輸送を実行できるよう、カッコ１のように、アイシーエヌティーエルを 0に変更します。この変更により、粒子輸送ができるようになります。

次に、陽子線のエネルギーを調整するために、sourceセクションのe0を100メブから、試しに200メブに変更します。

変更後、フィッツを実行し、trackドット イーピーエスを開いて結果を確認します。

プロトンの止まった位置を確認すると、プロトンが大玉付近で止まっています。芯の吸収線量は、depositドット アウトの27行目の数値で確認することができます。

この作業を繰り返して、陽子線のブラッグピーク位置が、芯の位置と重なるまで、陽子線エネルギーの調整を行います。

すると、陽子線エネルギーを約293メブに変更することで、図に示すように、陽子線のブラッグピークと芯の位置が重なることが確認できると思います。

--- SLIDE 15 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
PHITSの計算結果は線源が１つ発生する当たりに規格化されている

複数の線源が発生する状況を模擬するには，[source]セクションのtotfactパラメータを変更する

1A（アンペア）は，1秒当たり1C（クーロン）の電流が流れる状態を表す
素電荷（陽子1つ当たりの電荷）は1.6x10-19Cとする
ステップ５：陽子ビーム電流を調整する
1A（アンペア）の陽子ビームで1秒間照射したときの芯での吸収線量（Gy）を計算しよう
ヒント
maxcas, maxbchは計算精度（統計誤差）に関係する値で規格化とは無関係！
例） 陽子が100個発生した場合の吸収線量を計算する場合はtotfact = 100.0
SPEAKER_NOTES:
次に、ステップ5です。ステップ５では、再規格化について学んでいきます。

ここでは、ビーム電流を調整して、1アンペア で1秒間照射したときの、芯での吸収線量を計算します。

フィッツの計算結果は、粒子が１つ発生する当たりに規格化されています。そのため、maxcas と maxbchは、計算精度に関係する値で 規格化とは無関係となります。

複数の粒子が発生する状況を模擬するには、sourceセクションにおいて totfactパラメータを変更する必要があります。

例として、陽子線が100個発生した場合の吸収線量を計算する場合は、totfactを100と 変更します。 すなわち、1アンペア流れた際に発生する陽子数を手で計算し、totfactへ入力することになります。

ここで、1アンペアは，1秒当たり1クーロンの電流が流れる状態を表し、陽子1つ当たりの電荷は1.6×10の-19乗クーロンとします。

--- SLIDE 16 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ５の解答
Totfactを変えるとスケールが変わる
1アンペアで1秒照射するときの発生陽子数は1.0 / 1.6E-19 = 6.25E18（個）
Totfact = 6.25E18としたときの吸収線量は1.28E8(Gy) （陽子293MeV入射の場合）
[ S o u r c e ]
  totfact =   1.0/1.6e-19   # (D=1.0) global factor
h:   x      n     n          y(all     ),l3 n
#  num    reg     volume       all       r.err
    1       1   5.2360E+02   1.2785E+08  0.0178
deposit.out （27行目）
snowman.inp
track.eps
SPEAKER_NOTES:
ステップ５の解答にうつります。

まず、1アンペアで 1秒照射するときの発生プロトン数を計算する場合、1アンペアを素電荷で割ればよいので、1÷1.6×10の-19乗、よって、6.25×10の18乗個と算出することが出来ます。

この数値を、snowmanドット インプのtotfactへ入力することで、これまでの結果が再規格化され、フィッツの結果が、1アンペアで 1秒照射するときの発生プロトン数を計算することが可能となります。

では、変更したフィッツの入力ファイルを使用し、フィッツを実行しましょう。

実行後、trackドット イーピーエスを確認すると、図に示すように、フラックスのスケールが変わり、depositドット アウトを確認すると吸収線量が1.28 カケル 十の８乗 グレイと出力されていることが、確認できるかと思います。

この結果から、最初のフィッツの結果 29 ピコグレイ と異なり、実際に複数本の放射線が入射した結果に、再規格化されていることを確認できると思います。
MENTIONED_INPUT_NAMES: snowman.inp

--- SLIDE 17 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ６：雪だるまの芯を溶かすために必要となる電流を計算する
雪だるまは-10℃の氷と仮定する
1秒間の陽子ビーム照射で一気に氷を0℃に加熱して溶かすために必要なビーム電流（アンペア）及び出力（ワット）を手計算で求めよう
ヒント
氷の比熱は0.5 (cal/g/K) = 2.1 (J/g/K)とする
氷の融解熱（相転移に必要な熱量）は333.5（J/g）とする
1Gy = 1（J/kg） = 0.001（J/g）
*ビーム出力（MW）は粒子エネルギー（MeV）×電流（A）
ちなみに…
国内最大出力を誇るJ-PARCの最大ビーム出力は約1MW
*厳密には加速電圧(MV) x 電流(A)
SPEAKER_NOTES:
最後に、ステップ6です。

ここでは、雪だるまの芯を溶かすために、必要となる電流値を計算します。

この計算を進めるにあたり、雪だるまは、-10℃の氷と仮定します。
次に、1秒間の照射で一気に氷を0℃に加熱して溶かすために必要なビーム電流 アンペア 及び出力 ワット を、手計算で求めていくことになります。

この計算のヒントですが、氷の比熱は 0.5カロリーパーグラムパーケルビン、イコール、2.1 ジュールパーグラムパーケルビンとします。

氷の融解熱は、333.5ジュールパーグラムとします。

1グレイは0.001ジュールパーグラムであり、ビーム出力 メガワットは、粒子エネルギー メブ  かける  電流 アンペア とします。

ちなみに、国内最大出力を誇る ジェーパークの 最大ビーム出力は、約 1メガワットであり、この数値を基準に、雪だるまの芯が溶けるのかを、評価してみます。

--- SLIDE 18 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
ステップ６の回答
現在の加速器技術では，雪だるまを溶かすのが精一杯

ガンダム級のビームライフル（一瞬でモビルスーツを爆破する）を作るためには，まだまだ技術革新が必要！
（ただし，長時間照射すれば金属も溶かせる）
1Aで293MeV陽子ビームを1秒間照射したときの吸収線量は

氷の温度を10K上昇させ，溶かすために必要な熱量は

1秒間でその熱量を与えるために必要な電流は

このときのビーム出力は

より正確には
[ 293 (MeV/particle) x 1.6E-19 (J/eV) ] x [ 2.77E-3 (C/s) / 1.6E-19 (C/particle) ] = 0.811 (MJ/s)
							      = 0.811 (MW)
1.28E8（Gy/A）＝1.28E5（J/g/A）

2.1（J/g/K） x 10（K) + 333.5（J/g） = 354.5（J/g）

354.5（J/g） / 1.28E5（J/g/A） = 2.77E-3（A）

293 (MeV) x 2.77E-3 (A) = 0.811 (MW) ≒ J-PARCの最大出力
SPEAKER_NOTES:
では、ステップ6の計算について、流れと 手計算結果 を説明します。

まず、1アンペアで 293メブの陽子線ビームを、1秒間照射したときの 吸収線量 ジュールパーグラム を計算します。
すると、1.28 かける ジュウの5乗 ジュールパーグラムパーアンペア となります。

次に、氷の温度を10ケルビン上昇させ、氷を溶かすために必要な熱量 ジュールパーグラム を計算します。
すると、氷の比重 2.1 ジュールパーグラムパーケルビン に 10ケルビンをかけ 氷の融解熱、333.5ジュールパーグラム を足し、354.5 ジュールパーグラム となります。

1と２の結果から、3つ目に、1秒間の照射で、その熱量を与えるために必要な 電流を計算します。
つまり、354.5 ジュールパーグラム わる  1.28 かける ジュウの8乗 ジュールパーグラムパーアンペア イコール  2.77 かけるジュウのマイナス３乗 アンペア となります。

最後に、このときのビーム出力を計算してみます。
すると、293 メブ カケル 2.77 かけるジュウのマイナス３乗 アンペア イコール 0.811 メガワット となり、これは、国内最大出力を誇るJ-PARCの最大出力、約1メガワットに相当します。

以上より、現在の加速器技術では，雪だるまを溶かすのが精一杯で、ガンダム級のビームライフル  モビルスーツを爆破するビームを作るためには，まだまだ技術革新が必要であるという結論になります。 ただし、長時間照射すれば、金属は溶かすことができるということがわかると思います。

--- SLIDE 19 ---
PPTX_FILE: phits-snowman-en.pptx
SLIDE_TEXT:
雪だるま体系を作り，それを陽子ビームで溶かすための最適な条件をPHITSで計算した
PHITSのタリー結果は，通常，線源１つ発生当たりに規格化される
実際の条件を模擬するためには，totfactパラメータを用いてタリー結果を再規格化する必要がある
まとめ
SPEAKER_NOTES:
最後に、本実習のまとめです。

雪だるまの体系を作り，それを陽子線ビームで溶かすための 最適な条件をフィッツで計算しました。

フィッツのタリー結果は，通常，粒子１つが発生する当たりに規格化されています。

実際の照射条件を模擬するためには，totfactパラメータを用いて、タリー結果を再規格化する必要があります。

以上で、この演習を終わります。動画をご覧いただき、ありがとうございました。

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/snowman1.inp
FILE: input/snowman2.inp
FILE: input/snowman3.inp
FILE: input/snowman4.inp
FILE: input/snowman5.inp
FILE: input/snowman-end.inp

[BONUS_TEXT_FILES]
NOTE: None
