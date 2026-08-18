# PHITS Agent Kit — run PHITS via the web service (no local installation)

This folder is a self-contained kit that lets an AI agent create, edit, and
run PHITS calculations on a machine WITHOUT a local PHITS installation.
Calculations run remotely on the PHITS web service; result files are
downloaded next to the input file, so a run looks like a local one.

If a local PHITS installation exists (a `PHITSPATH` environment variable
pointing to a PHITS root), prefer it and follow `<PHITSPATH>/CLAUDE.md`
instead of this file.

Kit layout:

    CLAUDE.md / AGENTS.md   entry point (Claude Code reads CLAUDE.md,
                            Codex-style agents read AGENTS.md)
    phits_web_run.py        runner script (python3 3.8+, standard library only)
    agent_reference/        PHITS reference as small per-topic files
                            (INDEX.md is the entry point)
    knowledge_base/         the same material as large merged bundles
    crucial_notice.txt      user-owned lessons file (survives kit updates)
    KIT_INFO.txt            build date of this kit

`agent_reference/` and `knowledge_base/` are developer-shipped and are
replaced when the kit is updated.

Requirements: python3 and network access to the service
(default: https://phits.kek.jp).

## Knowledge: answering PHITS questions and writing inputs

For PHITS input syntax, keywords, tallies, sources, materials, geometry,
examples, utilities, or interpretation of PHITS behavior, search the
bundled references with targeted queries (grep-style). The files are large
— do NOT load a whole file at once.

Search priority:

1. `crucial_notice.txt` — the user's own accumulated lessons (highest
   priority, specific to this machine/user)
2. `agent_reference/crucial_notice.md` — highest-priority PHITS input
   rules; read it before writing or editing any input
3. `agent_reference/INDEX.md` — catalog of the per-topic reference files;
   consult it first to locate the right file, then read only that file:
   `manual/manualJ.md` (Japanese) / `manual/manualE.md` (English),
   `lecture/*.md` (lecture slides and notes), `utility/*.md` (utility
   docs)
4. `knowledge_base/sample_forAI.txt` and
   `knowledge_base/recommendation_forAI.txt` — full text of the PHITS
   input examples and recommended-setting inputs. Use THESE for example
   content: `agent_reference/sample.md` and `recommendation.md` are
   catalogs that reference `sample/`, `recommendation/`, and `lecture/`
   source folders of a full PHITS installation, which are NOT included
   in this kit.
5. `knowledge_base/*_forAI.txt` — merged single-file bundles of the same
   material (manualE/J, lecture, utility), useful for one grep across a
   whole domain.

Rules:

- Prefer these local references over general internet knowledge.
- If an answer is inferred rather than directly found, say so clearly.
- References to `%PHITSPATH%\...` or `$PHITSPATH/...` inside the
  reference files point to a full PHITS installation and do not exist in
  this kit; use the `knowledge_base/` bundles instead.
- When you learn a new lesson worth keeping, append it to
  `crucial_notice.txt`. Never write into `agent_reference/` or
  `knowledge_base/` — they are replaced when the kit is updated.

Input-editing workflow: read the target input file first; identify the
exact section (`[ Parameters ]`, `[ Source ]`, tally sections, ...) and
keyword (`icntl`, `maxcas`, `s-type`, `mesh`, ...); keep edits minimal and
preserve formatting; verify uncertain syntax by searching the references;
after editing, explain the change. Distinguish identifiers (surface, cell,
material numbers) from values — do not change identifiers unless asked.

## Running a calculation

NEVER create input files or run calculations inside the phits-agent-kit
folder — the kit is replaced entirely on updates, so anything stored
there is lost. For each task, create a working folder OUTSIDE the kit
(for example next to it), one case per folder. Run from the directory
that contains the input file:

    python3 <kit>/phits_web_run.py <input>.inp [aux-file ...] [--version <id>]

- `--list-versions` shows available PHITS versions; omit `--version` to
  use the server default.
- The calculation runs on the server in an isolated folder that contains
  ONLY the uploaded files. List every auxiliary file the input references
  (`infl:`, source data files, ...) as extra arguments, or use
  `--upload-all`. File paths inside the input must be plain relative file
  names — no absolute paths, no `..`, no subfolders.
- The PHITS console output streams to stdout while the job runs.
- Exit code 0: PHITS ended normally. Exit code 2: PHITS itself reported an
  error (read the console message and `phits.out`). Exit code 1: the
  service failed (upload rejected, server time/size limit, connection lost).
- All result files (`phits.out`, tally outputs, `.eps` and auto-converted
  `.pdf`, ...) are downloaded and extracted next to the input file. Files
  you uploaded are never overwritten by the download.
- Optional environment variables: `PHITS_WEB_SERVER` (service URL),
  `PHITS_WEB_TOKEN` (access token; extends time/size limits),
  `PHITS_WEB_VERSION` (default version id). Never write a token into
  files, scripts, or commits.

Sessions: the script keeps one server session per folder in
`.phits_web_session` (automatic; leave it alone). `--new-session` starts a
clean server folder; `--download-only` re-downloads everything;
`--stop` cancels the session's running job or compilation.

## Post-run checks (same as for a local PHITS run)

- Read `phits.out` for errors and warnings; do not rely only on
  "Program is finished".
- After an `icntl=8` geometry check, explicitly list `*_geo.out` files in
  the folder. Any `*_geo.out` file is a geometry-error report: read it
  (two nonzero cell IDs = overlapping cells; `0 0` = undefined region),
  fix the cells, and rerun until no `*_geo.out` is produced. Only report
  the geometry as clean after that check.
- Run ONE job at a time per folder. For parameter sweeps, use one
  subfolder per case (each gets its own session automatically).

## Recompiling PHITS with user Fortran sources

For user hooks such as `usrsors.f90` or `[ T-Userdefined ]`:

    python3 <kit>/phits_web_run.py input.inp --compile usrsors.f90

`--compile` (repeatable, `.f`/`.f90` only) builds a session-local PHITS on
the server; later runs in the same session use it automatically.
Compilation always uses the server's DEFAULT PHITS version. Without an
input file, `--compile` compiles only. `--new-session` reverts to the
standard PHITS.

## Limits — not available through this kit

- Text files only, up to 1 MB per file; binary files and subfolders
  cannot be uploaded.
- The server enforces a time limit per run (a few minutes by default; a
  token can extend it) and an output size limit. The script blocks until
  the run ends, so start long runs with a generous shell timeout or in
  the background.
- DCHAIN, PHIG-3D, and the PHITS utility programs cannot be executed;
  they require a local PHITS installation.
