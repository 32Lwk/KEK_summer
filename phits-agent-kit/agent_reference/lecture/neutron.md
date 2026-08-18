# Lecture: advanced/neutron

SOURCE_FOLDER: D:/NEAgit/lecture/advanced/neutron
NOTE: Input/answer/output files are referenced by path only; read them directly from SOURCE_FOLDER.

LECTURE_BUNDLE: neutron
LECTURE_PATH_INDEX: lecture/advanced/neutron
PPTX_FILES: phits-lec-neutron-en.pptx
SOURCE_TYPE: lecture
DETECTED_TOPIC_PREFIXES: neutron
SECTION_KEYWORDS: t-cross, t-track

[INDEX]
ROOT_FOLDER: D:/NEAgit/lecture/advanced/neutron
LECTURE_PATH_INDEX: lecture/advanced/neutron
PPTX_FILES: phits-lec-neutron-en.pptx
INPUT_DIR_COUNT: 1
MAIN_INPUT_COUNT: 1
SLIDE_COUNT: 30
EXERCISE_SLIDE_COUNT: 9
BONUS_INPUT_COUNT: 1
BONUS_TEXT_COUNT: 0

[INPUT_DIRS]
- input

[MAIN_INPUT_FILES]
- neutron.inp

[SLIDE_AND_EXERCISE_INDEX]
- SLIDE 01: Neutron beam line design
- SLIDE 02: Goal of this lecture
- SLIDE 03: neutron.inp
- SLIDE 04: EXERCISE 1 | Exercise 1
  ANSWER_FILE: input/neutron-2.inp
- SLIDE 05: Answer 1
- SLIDE 06: EXERCISE 2 | Exercise 2
  ANSWER_FILE: input/neutron-3.inp
- SLIDE 07: Answer 2
- SLIDE 08: Duct source
- SLIDE 09: Schematic image
- SLIDE 10: Duct source algorithm
- SLIDE 11: EXERCISE 3 | [ S o u r c e ]
  ANSWER_FILE: input/neutron-4.inp
- SLIDE 12: [ S o u r c e ]
- SLIDE 13: EXERCISE 4 | Exercise 4
  ANSWER_FILE: input/neutron-5.inp
- SLIDE 14: Answer 4
- SLIDE 15: Interpretation of answer 4
- SLIDE 16: Super mirror
- SLIDE 17: [Super mirror] section
- SLIDE 18: EXERCISE 5 | Exercise 5
  ANSWER_FILE: input/neutron-6.inp
- SLIDE 19: EXERCISE 5 | Range of duct source with supermirror: z=2m to 52m
  ANSWER_FILE: input/neutron-6.inp
- SLIDE 20: Answer 5
- SLIDE 21: EXERCISE 6 | Exercise 6
  ANSWER_FILE: input/neutron-7.inp
- SLIDE 22: Answer 6
- SLIDE 23: T0 chopper
- SLIDE 24: EXERCISE 7 | Exercise 7
  ANSWER_FILE: input/neutron-8.inp
- SLIDE 25: Answer 7
- SLIDE 26: Curved guide
- SLIDE 27: EXERCISE 8 | Exercise 8
  ANSWER_FILE: input/neutron-8.inp
- SLIDE 28: Answer 8
- SLIDE 29: Answer 8 (Continued)
- SLIDE 30: Summary

[MAIN_INPUT_FILES_REFERENCE]
NOTE: Read these input files directly from the source folder.
FILE: neutron.inp

[SLIDE_CONTENTS]
--- SLIDE 01 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Neutron beam line design
Title
Sep. 2017 revised
SPEAKER_NOTES:
PHITS講習会 入門実習

--- SLIDE 02 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Goal of this lecture
Purpose
Transport neutrons using
1, Duct source
2, Super mirror
Neutron transport using mirror, chopper and bend
3, T0 chopper
4, Curved guide

--- SLIDE 03 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
neutron.inp
Check Input File
Basic setup
Projectile:
Geometry:
Tally:
Geometry
0.2 meV neutron (5cm radius beam)
Beam pipe (5 cm radius, 50 m long)
[t-track] fluence  distribution
Beam Pipe
(Vacuum)
0.2 meV
Neutron
track.eps
MENTIONED_INPUT_NAMES: neutron.inp

--- SLIDE 04 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 1
SLIDE_TEXT:
Exercise 1
Exercise 1
Calculate flux with parallel beam
Beam Pipe
(Vacuum)
0.2 meV
Neutron
icntl      = 8
 maxcas = 5000
 maxbch = 1
 itall       = 1
 file(1)    = c:/phits
 file(6)    = phits.out
 nucdata  =1
1, Change icntl to
calculate flux
ANSWER_FILE: input/neutron-2.inp

--- SLIDE 05 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Answer 1
Parallel beam
icntl      = 0
 maxcas = 5000
 maxbch = 1
 itall       = 1
 file(1)    = c:/phits
 file(6)    = phits.out
 nucdata  =1
: No spread -> 100% go through the pipe
Answer 1
Beam Pipe
(Vacuum)
0.2 meV
Neutron
icntl      = 8
 maxcas = 5000
 maxbch = 1
 itall       = 1
 file(1)    = c:/phits
 file(6)    = phits.out
 nucdata  =1
1, Change icntl to
calculate flux

--- SLIDE 06 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 2
SLIDE_TEXT:
Exercise 2
Exercise 2
Calculate flux with isotropic beam
Beam Pipe
(Vacuum)
0.2 meV
Neutron
[ source ]
 s-type = 2
 proj   = neutron
 x0     = -2.5
 x1     =  2.5
 y0     = -2.5
 y1     =  2.5
 z0     =  0.0
 z1     =  0.0
 dir    =  ____
 e0     = 2.e-10
1, Change dir in
[source]
ANSWER_FILE: input/neutron-3.inp

--- SLIDE 07 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Answer 2
Isotropic source
[ source ]
 s-type = 2
 proj   = neutron
 x0     = -2.5
 x1     =  2.5
 y0     = -2.5
 y1     =  2.5
 z0     =  0.0
 z1     =  0.0
 dir    =   all
 e0     = 2.e-10
: Very few enter the beam pipe
Answer 2
Beam Pipe
(Vacuum)
0.2 meV
Neutron
[ source ]
 s-type = 2
 proj   = neutron
 x0     = -2.5
 x1     =  2.5
 y0     = -2.5
 y1     =  2.5
 z0     =  0.0
 z1     =  0.0
 dir    =  ____
 e0     = 2.e-10
1, Change dir in
[source]

--- SLIDE 08 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Duct source
If following conditions are met, use Duct source…
1, Source is isotropic low energy neutrons
2, Transported through a long duct
[ S o u r c e ]
s-type = 1 or 2
*
*
*
dom   = -10
 dl0    = _____
 dl1    = _____
 dl2    = _____
 dpf    = _____
 dxw   = _____
 dyw   = _____
 drd    = _____
Usual source specification  (dir, phi are not read)
-> -10 : Duct source flag
-> z coodinate of beam line start
-> z coodinate of duct start
-> z coodinate of duct end
-> fraction of particles which reach z=dl2
-> (if s-type = 2) x-direction duct width
-> (if s-type = 2) y-direction duct width
-> (if s-type = 1) duct radius
Duct source definition

--- SLIDE 09 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Schematic image
Duct source quantities
Usual source specification
z
0
z0
Source
plane
dl0
dl1
dl2
dpf -> Splitting
dxw
dyw
Duct
Attention:
s-type=2 (cylindrical) is not compatible with supermirror
MC bias to score particles in the middle of duct

--- SLIDE 10 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Duct source algorithm
Duct source quantities
1/r2
Repeat
1/r2
3, Select another points for another trajectory

--- SLIDE 11 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 3
SLIDE_TEXT:
[ S o u r c e ]
 s-type = 2
 proj   = neutron
 x0     = -2.5
・・・・・・・
 e0     = 2.e-10
dom   = _____
 dl0    = _____
 dl1    = _____
 dl2    = _____
 dpf    = _____
 dxw   = _____
 dyw   = _____
[ S o u r c e ]
 s-type = 2
 proj   = neutron
 x0     = -2.5
 x1     =  2.5
 y0     = -2.5
 y1     =  2.5
 z0     =  0.0
 z1     =  0.0
 dir    =  all
 e0     = 2.e-10
Exercise 3
Implement a duct source with this specification
200
Source
Duct
500
5cm
5cm
5% of source
       reach here
beam line start
End of duct
Exercise 3
ANSWER_FILE: input/neutron-4.inp

--- SLIDE 12 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
[ S o u r c e ]
 s-type = 2
 proj   = neutron
 x0     = -2.5
 x1     =  2.5
 y0     = -2.5
 y1     =  2.5
 z0     =  0.0
 z1     =  0.0
 dir    =  all
 e0     = 2.e-10
 dom  = -10
 dl0    = 200
 dl1    = 500
 dl2    = 5000
 dpf    = 1.0e-02
 dxw   = 5.0
 dyw   = 5.0
Answer 3
Beam is parallel
before duct
(no loss)
Beam is transported
through the duct
(attenuated)
Answer 3

--- SLIDE 13 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 4
SLIDE_TEXT:
Exercise 4
Score particle current in the duct

Delete “off” to enable T-cross
Define z binning
Z= 0-5000 cm,
1000 mesh points (width = 5 cm)
Show current distribution along z
Score neutrons
[ T - C r o s s ] off
 title = Duct current in
     mesh =  xyz
・・・・・・
   z-type =    2
     zmin =     *********
     zmax =     *********
       nz =       *********
   e-type =    1
       ne =    1
            0.0  1.00
     unit =    1
     axis =     *********
      file = cross-z.out
 output = current
     part =   *********
  epsout =    1
Exercise 4
ANSWER_FILE: input/neutron-5.inp

--- SLIDE 14 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Answer 4
Score particle current in the duct
[ T - C r o s s ]
 title = Duct current in
     mesh =  xyz
・・・・・・
   z-type =    2
     zmin =      0.0
     zmax =   5000
       nz =      1000
   e-type =    1
       ne =    1
            0.0  1.0
     unit =    1
     axis =     z
      file =   cross-z.out
 output =   current
     part =   neutron
  epsout =    1
Wall current can be also scored by scoring particles crossing x (or y) plane of duct
Source is
  2x10-10 MeV
Answer 4

--- SLIDE 15 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Interpretation of answer 4
Duct current
z (cm)
0
Source
plane
200
500
5000
Duct
2002/5002/25=6.4x10-3
Duct cross section
Attenuation
 before duct
2002/5002
0.01
Answer 4
5002/50002
=1/100

--- SLIDE 16 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Super mirror
Use [Super mirror] to define neutron super mirror
Super mirror quantities

--- SLIDE 17 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
[Super mirror] section
Super mirror is defined by using [Super mirror] section
[ Super Mirror ]
   r-in    r-out    mm      r0     qc(Å-1)   am(Å)    wm(Å-1)
      1     100    ****   ****    ****      ****      ****
Region of mirror material
Region of
outside mirror
Particles in region #1
  entering region #2 are reflected
Super mirror section

--- SLIDE 18 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Exercise 5
Define the outer region as glass
Density 2.2 g/cm3
Mirror thickness is 1 cm (now 2.5cm)
Introduce a super mirror section and define its parameters

R0 (r0) = 0.99
α (am) = 3.0
W (wm) = 0.003
Qc (qc)= 0.0217
m (mm) =  3
[ cell ]
 100 -1  (-101:105:202)

$        pz   pz   rpp  rpp
 101  0  101 -102      -202

 102  0  102 -103      -201
 103  0  103 -104      -201
 104  0  104 -105      -201

 105  0 *** 102 -105  201 -202
[ Super Mirror ] off
   r-in    r-out    mm      r0      qc     am    wm
 ****    ****    ****  ****  ****  ****  ****
Define a super mirror
Hint is in the next page
[ surface ]
201 rpp -2.5 2.5  -2.5 2.5  -200 5200
202 rpp -5.0 5.0  -5.0 5.0  -200 5200
Exercise 5
15
ANSWER_FILE: input/neutron-6.inp

--- SLIDE 19 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 5
SLIDE_TEXT:
Range of duct source with supermirror: z=2m to 52m
Source region
Beam line start
The supermirror options are set on the inner surface of the glass.
Exercise 5 hint
Conceptual drawing
Beam size: 5cm X 5cm
Glass: 10mm
Exercise 5
ANSWER_FILE: input/neutron-6.inp

--- SLIDE 20 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Answer 5
[ cell ]
 100 -1  (-101:105:202)

$        pz   pz   rpp  rpp
 101  0  101 -102      -202

 102  0  102 -103      -201
 103  0  103 -104      -201
 104  0  104 -105      -201

 105  1 -2.2 102 -105  201 -202
[ Super Mirror ] ___
   r-in    r-out    mm      r0      qc      am    wm
  103     105      3.0    0.99  0.0217  3.0   0.003
[ surface ]
・・・・・・
201 rpp -2.5 2.5  -2.5 2.5  -200 5200
202 rpp -3.5 3.5  -3.5 3.5  -200 5200
6.4x10-3
6.06x10-3
Very little loss
Answer 5

--- SLIDE 21 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 6
SLIDE_TEXT:
Exercise 6
Change source energy (10-10 - 1 MeV)
energy-distributed source
Change energy binning of t-cross
to see the transport of low/high energy neutrons separately
Check the effect of super mirror
Exercise 6
[ source ]
・・・・・・
$  e0 =  2.00000E-10
 e-type =  1
       ne = -1
    1.e-10    1
       1.0
・・・・・・
[ t-track ]
・・・・・・
 e-type =    1
       ne =    3
  0.0  1.e-8  1. e-3  1.0
angel = ymin(1e-6) ymax(1e-3)
・・・・・・
Low energy
What about
 higher energies?
ANSWER_FILE: input/neutron-7.inp

--- SLIDE 22 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Answer 6
Answer 6
1keV-1MeV
10meV-1keV
0-10meV
Almost no loss
Reflected
No reflection
-> Duct source

--- SLIDE 23 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
T0 chopper
T0 choppers are defined by [Mat time change] section
	→ Section to change materials by time
[ Mat Time Change ]
mat   time    change
  1    50.0        11
  2   100.0       12
  3   1000.0       0
Change material #1 to #11 at 50ns
Change material #3 to vacuum at 1000 ns
By changing materials
       from absorber to vacuum
      		 (or vice versa),
            T0 chopper can be simulated
T0 chopper implementation
https://j-parc.jp/researcher/MatLife/ja/monthly_reports/2016_04.html

--- SLIDE 24 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 7
SLIDE_TEXT:
Exercise 7
Activate [mat time change] section
Define new surfaces, material and cells for chopper
Activate [T-cross] to score energy spectrum before and after the chopper
[ mat time change ] off
 mat   time   change
  2      3.e4     0
Define T0 chopper with [mat time change]
[ surface ]
・・・・・・
 111 pz  710
 112 pz  740
[ cell ]
・・・・・・
103  0  103 -104      -201   #(111  -112  -201)
$T0 chopper
$                    pz   pz    rpp
201  2 -2.52  111 -112  -201
[ material ]
・・・・・・
$ T0 chopper Boron carbide
m2
 B  4
 C  1
Exercise 7
[ T - C r o s s ] off
・・・・・・
   e-type =    3
     emin =  1.e-6
     emax =  1.e0
       ne =  100
     unit =    2
     axis =   eng
     file = cross-eng.out
・・・・・・
ANSWER_FILE: input/neutron-8.inp

--- SLIDE 25 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Answer 7
High energy component is cut by the chopper
Before chopper
z = 700
After chopper
z = 750
Low energy component passes after chopper
Answer 7

--- SLIDE 26 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Curved guide
Curved guide can be implemented by combination of surfaces
Square curved guide
= 2 planes + 2 cylinders
 + 2 cutting planes
＝
Curved guide implementation
Curved guide is useful to cutoff low energy neutrons

--- SLIDE 27 ---
PPTX_FILE: phits-lec-neutron-en.pptx
EXERCISE_NO: 8
SLIDE_TEXT:
Exercise 8
Turn off current [cell] [surface] [super mirror] sections
Activate [cell] [surface] [super mirror] sections in the bottom of the input
Score energy spectra at 6 z-coordinates from 700 to 4900
Define square curved guide
[ surface ] off
 101 pz -100
・・・・・・
[ cell ] off
 100 -1  (-101:105:202)
・・・・・・
[ Super Mirror ] off
103      105     3.0  0.99  0.0217  3.0  0.003
[ T - C r o s s ]
・・・・・・
  zmin  =  700.00000
  zmax =  4900.00000
      nz =    6
・・・・・・
 file = cross-eng.out
・・・・・・
Exercise 8
Replace this part
ANSWER_FILE: input/neutron-8.inp

--- SLIDE 28 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Answer 8
z = 700cm
z =  3500
End of duct
Only low energy neutrons reach the end. All the others were cut by the duct.
Answer 8

--- SLIDE 29 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Answer 8 (Continued)
E < 10 meV
10 meV < E
        < 1 keV
1 keV < E
        < 1 MeV
Answer 8

--- SLIDE 30 ---
PPTX_FILE: phits-lec-neutron-en.pptx
SLIDE_TEXT:
Summary
Summary
Duct source is useful to simulate neutron beam transport in ducts
In [source] section, dom = -10
Use [Super mirror] to define neutron super mirrors
T0 chopper can be implemented by using [mat time change] section
Change neutron absorber<-> Vacuum
To define bending ducts use c/y (square duct) or ty (circular duct).
All the above can work together to define low energy neutron transport line

[BONUS_INPUT_FILES]
NOTE: Read these input files directly from the source folder.
FILE: input/neutron-final.inp

[BONUS_TEXT_FILES]
NOTE: None
