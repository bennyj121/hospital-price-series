"""HEAD cms-hpt.txt URLs from indexes.md and diff Last-Modified vs tonight's baseline.

Change feed for the $40 offer. Do not auto-commit. Do not add hospitals.
"""
import os
from email.utils import parsedate_to_datetime
import re
import subprocess
import sys
from pathlib import Path

UA = os.environ.get(
    "UA",
    "hospital-mrf-index/0.1.1 (Rogue AI agent; +https://github.com/bennyj121/hospital-price-series)",
)
BASELINE = Path("data/index-head-2026-08-26.txt")


def urls_from_indexes():
    text = Path("indexes.md").read_text(encoding="utf-8")
    urls = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 2:
            continue
        m = re.search(r"https://\S+", parts[1])
        if m:
            urls.append((parts[0], m.group(0).rstrip(")")))
    return urls


def load_baseline():
    out = {}
    for line in BASELINE.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 3:
            out[parts[0]] = parts[2].strip()
    return out


def head_url(url):
    r = subprocess.run(
        ["curl", "-sI", "-A", UA, "-L", "--max-time", "20", url],
        capture_output=True,
        text=True,
    )
    status = last_mod = date = ""
    for raw in (r.stdout or "").splitlines():
        k, _, v = raw.partition(":")
        key = k.strip().lower()
        val = v.strip()
        if key.startswith("http/") or raw.upper().startswith("HTTP/"):
            bits = raw.split()
            if len(bits) >= 2:
                status = bits[1]
        elif key == "last-modified":
            last_mod = val
        elif key == "date":
            date = val
    which = "Last-Modified" if last_mod else "Date"
    value = last_mod or date or "(no Last-Modified or Date)"
    return status, which, value



def classify_move(old, new):
    """Forward Last-Modified is a $40 change. Backward is noise, not a $40 change."""
    try:
        o = parsedate_to_datetime(old)
        n = parsedate_to_datetime(new)
    except (TypeError, ValueError, IndexError, OverflowError):
        return "noise"
    if n > o:
        return "changed"
    return "noise"


def main():
    urls = urls_from_indexes()
    if len(urls) < 5:
        print("expected at least 5 URLs in indexes.md, got", len(urls), file=sys.stderr)
        return 1
    baseline = load_baseline()
    failed = []
    changed = []
    noise = []
    for name, url in urls:
        status, which, value = head_url(url)
        print(f"{status}  {name}  {url}  {which}={value}")
        if status != "200":
            failed.append((name, url, status))
        old = baseline.get(url)
        if old is None:
            changed.append((name, url, "(no baseline)", f"{which} {value}"))
            continue
        if old == value:
            continue
        kind = classify_move(old, value)
        row = (name, url, old, f"{which} {value}")
        if kind == "changed":
            changed.append(row)
        else:
            noise.append(row)
    print(f"checked={len(urls)} failed={len(failed)} changed={len(changed)} noise={len(noise)}")
    print("Built by Rogue, an AI agent. Do not email hospital staff. Do not auto-commit.")

    lines = [
        "## $40 change watch",
        "",
        f"Baseline: `{BASELINE}` (2026-08-26 Last-Modified). Do not auto-commit. Do not add hospitals.",
        "",
        "Forward Last-Modified is a $40 change. Backward Last-Modified is noise, not a $40 change.",
        "",
        f"checked={len(urls)} failed={len(failed)} changed={len(changed)} noise={len(noise)}",
        "",
    ]
    if changed:
        lines.append("Changed URLs (forward, $40 watch):")
        lines.append("")
        for name, url, old, new in changed:
            lines.append(f"- {name} `{url}`: {old} -> {new}")
        lines.append("")
    else:
        lines.append("Changed URLs: none")
        lines.append("")
    if noise:
        lines.append("Noise (backward Last-Modified, not a $40 change):")
        lines.append("")
        for name, url, old, new in noise:
            lines.append(f"- {name} `{url}`: {old} -> {new}")
        lines.append("")
    else:
        lines.append("Noise: none")
        lines.append("")
    lines.append("")
    lines.append("Built by Rogue, an AI agent. Not a quote. Do not email hospital staff.")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        Path(summary).write_text("\n".join(lines) + "\n", encoding="utf-8")
    else:
        print("--- summary ---")
        print("\n".join(lines))

    # Machine-readable feed for own-repo mrf-change issues (CI only).
    import json
    payload = [
        {"name": name, "url": url, "old": old, "new": new}
        for name, url, old, new in changed
    ]
    Path("changed.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote changed.json count={len(payload)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
