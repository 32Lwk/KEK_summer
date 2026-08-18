#!/usr/bin/env python3
"""Run PHITS on the PHITS web service from the command line.

Python 3.8+ standard library only — no installation required beyond python3.

Typical usage:

    python3 phits_web_run.py input.inp
    python3 phits_web_run.py input.inp aux1.dat aux2.dat --version phits336
    python3 phits_web_run.py input.inp --compile usrsors.f90
    python3 phits_web_run.py --list-versions

The PHITS console output streams to the terminal while the job runs, and
all result files (phits.out, tally outputs, .eps / auto-converted .pdf, ...)
are downloaded and extracted next to the input file, so the folder ends up
looking like after a local PHITS run.

Environment variables (overridden by the corresponding options):
    PHITS_WEB_SERVER    service URL         (default: https://phits.kek.jp)
    PHITS_WEB_TOKEN     access token        (--token)
    PHITS_WEB_VERSION   PHITS version id    (--version)
"""

import argparse
import json
import os
import random
import re
import shutil
import string
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

DEFAULT_SERVER = "https://phits.kek.jp"
SESSION_FILE = ".phits_web_session"
RESULT_ZIP = ".phits_web_result.zip"
USER_AGENT = "phits-web-cli/1.0"


def info(msg):
    print(f"[phits-web] {msg}", flush=True)


def die(msg, code=1):
    print(f"[phits-web] ERROR: {msg}", file=sys.stderr, flush=True)
    sys.exit(code)


# ---------------------------------------------------------------- HTTP helpers

def http_json(method, url, session_id=None, body=None, timeout=60):
    """Send a request and return (status, parsed-JSON dict)."""
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if session_id:
        headers["x-session-id"] = session_id
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status, raw = resp.status, resp.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, e.read()
    except urllib.error.URLError as e:
        raise ConnectionError(f"cannot reach {url}: {e.reason}") from e
    try:
        parsed = json.loads(raw.decode("utf-8", errors="replace"))
        if isinstance(parsed, dict):
            return status, parsed
        return status, {"success": False, "error": str(parsed)[:300]}
    except json.JSONDecodeError:
        text = raw.decode("utf-8", errors="replace").strip()
        return status, {"success": False, "error": text[:300] or f"HTTP {status}"}


def download_session(server, session_id, dest_dir, skip=frozenset()):
    """Download the session ZIP and extract it into dest_dir.

    Files whose (flat) name is in `skip` are not extracted, so locally
    uploaded input files are never overwritten by their server copies.
    Returns the number of extracted files.
    """
    url = server + "/api/download-session"
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "x-session-id": session_id})
    tmp = os.path.join(dest_dir, RESULT_ZIP)
    try:
        try:
            with urllib.request.urlopen(req, timeout=None) as resp, open(tmp, "wb") as out:
                ctype = resp.headers.get("Content-Type", "")
                if "zip" not in ctype:
                    raise ConnectionError(f"unexpected response type: {ctype}")
                shutil.copyfileobj(resp, out)
        except urllib.error.HTTPError as e:
            raise ConnectionError(f"download failed: HTTP {e.code}") from e
        except urllib.error.URLError as e:
            raise ConnectionError(f"download failed: {e.reason}") from e

        extracted = 0
        with zipfile.ZipFile(tmp) as zf:
            for member in zf.infolist():
                if member.is_dir():
                    continue
                norm = os.path.normpath(member.filename.replace("\\", "/"))
                # guard against path traversal in archive entries
                if os.path.isabs(norm) or norm.startswith(".."):
                    continue
                if norm in skip:
                    continue
                target = os.path.join(dest_dir, norm)
                parent = os.path.dirname(target)
                if parent:
                    os.makedirs(parent, exist_ok=True)
                with zf.open(member) as src, open(target, "wb") as f:
                    shutil.copyfileobj(src, f)
                extracted += 1
        return extracted
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass


# ---------------------------------------------------------------- live log

class LiveLog(threading.Thread):
    """Streams the server-side console output (SSE) to the terminal.

    kind="run" follows the PHITS run log; kind="compile" follows the Fortran
    compilation log. Best-effort: if the stream cannot be opened, the full
    console output is printed from the final response instead.
    """

    def __init__(self, server, session_id, kind="run"):
        super().__init__(daemon=True)
        endpoint = "/api/phits-logs/" if kind == "run" else "/api/compile-logs/"
        self.url = (server + endpoint
                    + urllib.parse.quote(session_id, safe=""))
        self.kind = kind
        self.got_output = False

    def run(self):
        req = urllib.request.Request(
            self.url,
            headers={"User-Agent": USER_AGENT, "Accept": "text/event-stream"})
        try:
            with urllib.request.urlopen(req, timeout=None) as resp:
                for raw_line in resp:
                    line = raw_line.decode("utf-8", errors="replace").strip()
                    if not line.startswith("data:"):
                        continue
                    try:
                        event = json.loads(line[5:].strip())
                    except json.JSONDecodeError:
                        continue
                    self._handle(event)
        except Exception:
            pass

    def _handle(self, event):
        etype = event.get("type")
        if self.kind == "compile":
            if etype and etype.startswith("compile_"):
                sys.stdout.write(event.get("output", ""))
                sys.stdout.flush()
                if etype == "compile_output":
                    self.got_output = True
            return
        if etype in ("stdout", "stderr"):
            stream = sys.stdout if etype == "stdout" else sys.stderr
            stream.write(event.get("data", ""))
            stream.flush()
            self.got_output = True
        elif etype == "phits_execution_start":
            sys.stdout.write(event.get("output", ""))
            sys.stdout.flush()
        elif etype == "cpu_wait_start":
            info(f"server busy (CPU above {event.get('threshold')}%) — waiting for a free slot ...")
        elif etype == "cpu_wait_continue":
            info(f"still waiting (server CPU {event.get('cpuUsage')}%) ...")
        elif etype == "timeout":
            info(f"server time limit reached ({event.get('timeoutMinutes')} min) — job killed")
        elif etype == "size_limit_exceeded":
            info(f"output size limit exceeded (max {event.get('maxSizeDisplay')}) — job killed")


# ---------------------------------------------------------------- helpers

def read_text_file(path):
    """Return (content, note). content is None if the file is not text.

    Content is normalized to UTF-8 with LF line endings, which is what the
    server stores. Non-UTF-8 Japanese text is converted from CP932.
    """
    with open(path, "rb") as f:
        data = f.read()
    if b"\x00" in data:
        return None, "binary file"
    for enc in ("utf-8-sig", "cp932"):
        try:
            text = data.decode(enc)
        except UnicodeDecodeError:
            continue
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        note = None if enc == "utf-8-sig" else f"converted from {enc} to UTF-8"
        return text, note
    return None, "cannot decode as text (binary file?)"


def new_session_id():
    rand = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"cli_{int(time.time())}_{rand}"


def load_session_state(workdir):
    """Read .phits_web_session: {"sessionId": str, "uploaded": [names]}."""
    path = os.path.join(workdir, SESSION_FILE)
    state = {"sessionId": "", "uploaded": []}
    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read().strip()
    except OSError:
        return state
    try:
        data = json.loads(raw)
        state["sessionId"] = str(data.get("sessionId", ""))
        state["uploaded"] = [str(n) for n in data.get("uploaded", [])]
    except (json.JSONDecodeError, AttributeError):
        state["sessionId"] = raw  # tolerate a bare session-id string
    return state


def save_session_state(workdir, state):
    try:
        with open(os.path.join(workdir, SESSION_FILE), "w", encoding="utf-8") as f:
            json.dump(state, f, indent=1)
            f.write("\n")
    except OSError:
        pass


def resolve_session(workdir, args):
    """Pick the session: --session > per-folder session file > new one.

    Returns the state dict; state["uploaded"] remembers every file name this
    folder has uploaded, so downloads never overwrite local originals.
    """
    state = load_session_state(workdir)
    if args.session:
        sid = args.session.strip()
        if sid != state["sessionId"]:
            state = {"sessionId": sid, "uploaded": []}
    elif args.new_session:
        state = {"sessionId": "", "uploaded": []}
    sid = state["sessionId"]
    if not re.fullmatch(r"[A-Za-z0-9_-]{5,}", sid or ""):
        state["sessionId"] = new_session_id()
    save_session_state(workdir, state)
    return state


def fetch_config(server):
    status, cfg = http_json("GET", server + "/api/config")
    if status != 200 or "phits" not in cfg:
        die(f"{server} does not look like a PHITS web service "
            f"(GET /api/config failed: {cfg.get('error', status)})")
    return cfg


def check_version(cfg, version_id):
    versions = cfg["phits"]["versions"]
    if version_id and version_id not in [v["id"] for v in versions]:
        listing = "\n".join(f"  {v['id']:<22} {v['name']} {v.get('description', '')}"
                            for v in versions)
        die(f"unknown PHITS version id: {version_id}\navailable versions:\n{listing}")


def print_versions(cfg):
    default = cfg["phits"].get("defaultVersion")
    for v in cfg["phits"]["versions"]:
        mark = "  (default)" if v["id"] == default else ""
        print(f"{v['id']:<22} {v['name']:<16} {v.get('description', '')}{mark}")


def collect_uploads(input_path, aux_paths, upload_all, workdir, cfg):
    """Return {flat-name: content} for the input file and all auxiliary files."""
    max_size = cfg["upload"]["maxUploadSize"]
    blocked = {e.lower() for e in cfg["upload"]["blockedExtensions"]}
    allowed = {e.lower() for e in cfg["upload"]["allowedExtensions"]}

    def check_name(name, size):
        ext = os.path.splitext(name)[1].lower()
        if size > max_size:
            return f"exceeds the server upload limit ({max_size} bytes)"
        if ext in blocked:
            return f"file type {ext} is blocked by the server"
        if allowed and ext not in allowed:
            return f"file type {ext} is not in the allowed list"
        return None

    uploads = {}

    def add(path, required):
        name = os.path.basename(path)
        if name in uploads:
            if required:
                die(f"duplicate upload name: {name}")
            return
        if not os.path.isfile(path):
            die(f"file not found: {path}")
        content, note = read_text_file(path)
        if content is None:
            if required:
                die(f"{path}: {note} — only text files can be uploaded")
            info(f"skipped {name}: {note}")
            return
        reason = check_name(name, len(content.encode("utf-8")))
        if reason:
            if required:
                die(f"{name}: {reason}")
            info(f"skipped {name}: {reason}")
            return
        if note:
            info(f"{name}: {note}")
        uploads[name] = content

    add(input_path, required=True)
    for p in aux_paths:
        add(p, required=True)
    if upload_all:
        for entry in sorted(os.listdir(workdir)):
            if entry.startswith("."):
                continue
            path = os.path.join(workdir, entry)
            if os.path.isfile(path):
                add(path, required=False)
    return uploads


def compile_fortran(server, session_id, compile_paths, state, workdir):
    """Compile .f/.f90 sources into a session-local PHITS executable.

    Uses the same server endpoint as the browser's compile button: the
    server copies its src_for_browser_single tree into the session, adds
    the uploaded sources, and runs make. Later runs in the same session
    automatically use the resulting executable.
    """
    files = []
    for p in compile_paths:
        name = os.path.basename(p)
        if os.path.splitext(name)[1].lower() not in (".f", ".f90"):
            die(f"{name}: only .f and .f90 files can be compiled")
        if not os.path.isfile(p):
            die(f"file not found: {p}")
        content, note = read_text_file(p)
        if content is None:
            die(f"{p}: {note}")
        if note:
            info(f"{name}: {note}")
        files.append({"fileName": name, "content": content})

    state["uploaded"] = sorted(set(state["uploaded"])
                               | {f["fileName"] for f in files})
    save_session_state(workdir, state)

    live = LiveLog(server, session_id, kind="compile")
    live.start()
    time.sleep(0.3)

    names = ", ".join(f["fileName"] for f in files)
    info(f"compiling {names} into a session-local PHITS "
         f"(a first compilation can take several minutes) ...")
    start = time.time()
    try:
        status, res = http_json("POST", server + "/api/compile-all-fortran",
                                session_id, {"fortranFiles": files},
                                timeout=None)
    except KeyboardInterrupt:
        print(file=sys.stderr)
        info("interrupted — asking the server to stop the compilation ...")
        try:
            http_json("POST", server + "/api/stop-compile", session_id, {},
                      timeout=15)
        except ConnectionError:
            pass
        sys.exit(130)
    elapsed = time.time() - start

    time.sleep(1.0)  # let the live log drain
    ok = status == 200 and res.get("success") is True
    if not live.got_output:
        if res.get("stdout"):
            sys.stdout.write(res["stdout"])
            sys.stdout.flush()
        if res.get("stderr"):
            sys.stderr.write(res["stderr"])
            sys.stderr.flush()
    if not ok:
        die(f"compilation FAILED after {elapsed:.0f} s: "
            f"{res.get('error', f'HTTP {status}')}")
    info(f"compilation finished in {elapsed:.0f} s — runs in this session "
         f"now use the compiled PHITS (--new-session reverts to standard)")


# ---------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(
        description="Run PHITS on the PHITS web service and download the results.",
        epilog="Results are extracted next to the input file, like a local PHITS run.")
    parser.add_argument("input", nargs="?",
                        help="PHITS input file (.inp)")
    parser.add_argument("aux", nargs="*",
                        help="auxiliary files referenced by the input "
                             "(uploaded under their basename)")
    parser.add_argument("--server",
                        default=os.environ.get("PHITS_WEB_SERVER", DEFAULT_SERVER),
                        help="service URL (default: %(default)s)")
    parser.add_argument("--version", dest="phits_version",
                        default=os.environ.get("PHITS_WEB_VERSION"),
                        help="PHITS version id (see --list-versions; "
                             "default: server default)")
    parser.add_argument("--token", default=os.environ.get("PHITS_WEB_TOKEN"),
                        help="access token (extends server time/size limits)")
    parser.add_argument("--session", help="session ID to use "
                        "(default: reuse the one in .phits_web_session, else new)")
    parser.add_argument("--new-session", action="store_true",
                        help="start a fresh server session for this folder")
    parser.add_argument("--upload-all", action="store_true",
                        help="also upload every eligible text file in the input folder")
    parser.add_argument("--compile", action="append", metavar="F90",
                        default=[],
                        help=".f/.f90 source to compile into a session-local "
                             "PHITS before the run (repeatable; without an "
                             "input file, compile only)")
    parser.add_argument("--no-download", action="store_true",
                        help="do not download the results after the run")
    parser.add_argument("--download-only", action="store_true",
                        help="download the current session results and exit")
    parser.add_argument("--stop", action="store_true",
                        help="stop the session's running job and exit")
    parser.add_argument("--list-versions", action="store_true",
                        help="list available PHITS versions and exit")
    parser.add_argument("--timeout", type=float, default=None,
                        help="client-side wait limit for the run, in seconds "
                             "(default: wait until the server finishes)")
    args = parser.parse_args()

    server = args.server.rstrip("/")

    try:
        if args.list_versions:
            print_versions(fetch_config(server))
            return

        workdir = (os.path.dirname(os.path.abspath(args.input))
                   if args.input else os.getcwd())
        state = resolve_session(workdir, args)
        session_id = state["sessionId"]

        if args.stop:
            for endpoint, label in (("/api/stop-phits", "run"),
                                    ("/api/stop-compile", "compile")):
                _, res = http_json("POST", server + endpoint, session_id, {},
                                   timeout=30)
                info(f"{label}: "
                     + (res.get("message") or res.get("error") or "stop requested"))
            return

        if args.download_only:
            n = download_session(server, session_id, workdir)
            info(f"downloaded {n} file(s) from session {session_id} into {workdir}")
            return

        if not args.input and not args.compile:
            parser.error("an input file or --compile is required "
                         "(or use --list-versions / --download-only / --stop)")

        if args.token:
            _, res = http_json(
                "GET", server + "/api/validate-token?token="
                + urllib.parse.quote(args.token, safe=""))
            if not res.get("valid"):
                die(f"token rejected by the server: {res.get('reason', 'unknown')}")
            s = res.get("settings") or {}
            info(f"token accepted: {res.get('name')} "
                 f"(time limit: {s.get('timeoutMinutesDisplay') or 'default'}, "
                 f"output limit: {s.get('maxOutputSizeDisplay') or 'default'})")

        cfg = fetch_config(server)
        check_version(cfg, args.phits_version)

        if args.compile:
            if (args.phits_version
                    and args.phits_version != cfg["phits"].get("defaultVersion")):
                info("note: compilation always uses the server's default "
                     "PHITS version, regardless of --version")
            compile_fortran(server, session_id, args.compile, state, workdir)
            if not args.input:
                return

        input_path = os.path.abspath(args.input)
        input_name = os.path.basename(input_path)
        uploads = collect_uploads(input_path, args.aux, args.upload_all,
                                  workdir, cfg)
        state["uploaded"] = sorted(set(state["uploaded"]) | set(uploads))
        save_session_state(workdir, state)

        for name, content in uploads.items():
            if name == input_name:
                continue  # run-phits uploads the input itself
            _, res = http_json("POST", server + "/api/save-file", session_id,
                               {"filename": name, "content": content})
            if not res.get("success"):
                die(f"upload of {name} failed: {res.get('error', 'unknown error')}")
            if res.get("filename") and res["filename"] != name:
                info(f"note: {name} was stored as {res['filename']} on the server")
        if len(uploads) > 1:
            info(f"uploaded {len(uploads) - 1} auxiliary file(s)")

        live = LiveLog(server, session_id)
        live.start()
        time.sleep(0.3)  # let the log stream attach before the run starts

        body = {"filename": input_name, "content": uploads[input_name]}
        if args.phits_version:
            body["phitsVersion"] = args.phits_version
        if args.token:
            body["token"] = args.token

        info(f"running {input_name} on {server} (session {session_id}) ...")
        start = time.time()
        try:
            status, res = http_json("POST", server + "/api/run-phits",
                                    session_id, body, timeout=args.timeout)
        except KeyboardInterrupt:
            print(file=sys.stderr)
            info("interrupted — asking the server to stop the job ...")
            try:
                http_json("POST", server + "/api/stop-phits", session_id, {},
                          timeout=15)
            except ConnectionError:
                pass
            sys.exit(130)
        except ConnectionError as e:
            die(f"connection lost while waiting for the run ({e}).\n"
                f"  The job may still be running on the server. Retrieve the "
                f"results later with:\n"
                f"    python3 {os.path.basename(sys.argv[0])} --download-only")
        elapsed = time.time() - start

        time.sleep(1.0)  # let the live log drain
        ok = status == 200 and res.get("success") is True
        if not live.got_output:
            if res.get("stdout"):
                sys.stdout.write(res["stdout"])
                sys.stdout.flush()
            if res.get("stderr"):
                sys.stderr.write(res["stderr"])
                sys.stderr.flush()

        # phits.sh exits 0 even on PHITS input errors, so detect the banner
        console = (res.get("stdout") or "") + (res.get("stderr") or "")
        phits_error = ok and "Error Message from" in console

        if ok and not phits_error:
            out_files = res.get("outputFiles") or []
            info(f"PHITS finished normally in {elapsed:.0f} s "
                 f"— {len(out_files)} output file(s) on the server")
        elif phits_error:
            info(f"PHITS reported an ERROR after {elapsed:.0f} s "
                 f"(see the message above and phits.out)")
        else:
            info(f"PHITS run FAILED after {elapsed:.0f} s: "
                 f"{res.get('error', f'HTTP {status}')}")

        if not args.no_download:
            skip = frozenset(state["uploaded"])
            n = download_session(server, session_id, workdir, skip=skip)
            info(f"downloaded {n} result file(s) into {workdir}")
            if not ok or phits_error:
                info("check phits.out for the PHITS error message")

        sys.exit(0 if ok and not phits_error else 2 if phits_error else 1)

    except ConnectionError as e:
        die(str(e))
    except KeyboardInterrupt:
        print(file=sys.stderr)
        sys.exit(130)


if __name__ == "__main__":
    main()
