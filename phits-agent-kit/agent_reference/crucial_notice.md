# CRITICAL NOTICE FOR AI (HIGHEST PRIORITY)

This file contains critical rules for generating PHITS input files using AI.
If there is any conflict between this file and sample files/examples, follow this file.


## Creating a new PHITS input file:
- At least, [parameters], [source], [material], [surface], [cell], [t-track] must be included
- If the user does not specify how to write a section, follow the style and structure written in lecture/basic/lec01.inp
- In [t-track], xmin, xmax, ymin, ymax, zmin, and zmax must be adjusted so that all objects in the geometry are included, except for air, void, and outer void.
- Do not include [t-3dshow] unless the user explicitly requests it.


## Regarding the [Cell] section:
- Strictly distinguish between surface numbers and cell numbers when using the complement operator (#).
- Strictly distinguish between identifiers and values. Identifiers include surface numbers, cell numbers, material numbers, tally names, and file names. Values include radii, densities, positions, energies, mesh limits, and parameter values. If the user asks to change a value associated with an identifier, do not change the identifier unless explicitly requested.
- To define a region "outside" a surface, use the positive surface number directly (e.g., use "10" to mean outside surface 10). Do not use "#" followed directly by a surface number.
- The operator "#" must only be followed by a Cell ID (to exclude that specific cell) or a grouped surface definition enclosed in parentheses (e.g., "#(-10 -11)").
- Double-check for unnecessary or missing "#" operators; for simple spatial logic using surfaces, prefer using positive/negative signs (surface sense) over the complement operator to avoid geometry errors and improve calculation speed.
- In complex or decorative geometries, do not blindly exclude all previously defined cells using long chains such as "#100 #101 #102 #103 ...". Use only local, intentional exclusions where cells actually overlap and where one cell should take priority over another.


## Regarding comment remark:
- Do not use # as comment remark in [cell] and [surface] section
- Do not use c as comment remark anywhere in input file


## Regarding Citations and PHITS Syntax:
- Strictly distinguish between PHITS internal syntax (e.g., MAT[n] in the [Material] section) and grounding citations (e.g., [i]). Never merge or confuse these two types of brackets.
- Within PHITS code blocks, all citations MUST be placed after a comment mark ($) at the end of the line to prevent syntax errors. 
- Correct format example: "MAT[2] H 2 O 1 $ [i, j]". 
- Never output a citation bracket [i] as part of an active PHITS command or parameter line without a leading comment remark.


## Regarding Source Definition and Geometry Boundaries:
- Never define a source location (point, disk, or plane) exactly on a geometry boundary or cell surface
- If a source is positioned exactly on a boundary, PHITS may misidentify the starting cell due to numerical precision issues, which often results in "Lost particle" errors and calculation termination.
- Always shift the source coordinates slightly (e.g., by 0.01 or 0.001 cm) to ensure it starts definitively inside the intended cell.
- Example: If a boundary exists at Z = 100.0 and you want to emit particles into the air above it, use z0 = 100.001 instead of 100.0.


## Final confirmation:
- Confirm that each tally section contains all non-omissible parameters for the tally written in manual.
- Confirm that there is no double-defined region, particularly when adding new cells in [cell]
