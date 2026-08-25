#!/usr/bin/env python3
"""Fetch the NAH CMS hospital-price index and the Flagstaff Medical Center zip.

Writes a 1,000-row sample CSV (first 1,000 data rows, real columns) and
prints the format facts from the file that was actually opened.

Standard library only. The zip and full CSV stay in a work directory
(default /tmp/hospital-price-series) and are not written into git.

Built by Rogue, an AI agent. Not endorsed by CMS, HHS, or NAH.
Charges are not a patient bill. No PHI is fetched.
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen

INDEX_URL = "https://www.nahealth.com/cms-hpt.txt"
FMC_LOCATION = "Flagstaff Medical Center"
DEFAULT_WORK = Path("/tmp/hospital-price-series")
DEFAULT_SAMPLE = Path("data/fmc_standardcharges_sample_1000.csv")
DEFAULT_ROWS = 1000
USER_AGENT = "hospital-price-series/0.1 (+https://github.com/bennyj121/hospital-price-series)"


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=120) as resp:
        return resp.read()


def parse_index(text: str) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            if current:
                records.append(current)
                current = {}
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current[key.strip()] = value.strip()
    if current:
        records.append(current)
    return records


def pick_fmc(records: list[dict[str, str]]) -> dict[str, str]:
    for rec in records:
        if rec.get("location-name") == FMC_LOCATION:
            if not rec.get("mrf-url"):
                raise SystemExit("FMC index record has no mrf-url")
            return rec
    raise SystemExit("Flagstaff Medical Center not found in cms-hpt.txt")


def extract_csv(zip_bytes: bytes, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        names = zf.namelist()
        if len(names) != 1:
            print(f"zip members ({len(names)}): {names}", file=sys.stderr)
        member = names[0]
        if not member.lower().endswith(".csv"):
            raise SystemExit(f"expected a CSV member, got {member!r}")
        out = dest_dir / Path(member).name
        with zf.open(member) as src, open(out, "wb") as dst:
            while True:
                chunk = src.read(1024 * 1024)
                if not chunk:
                    break
                dst.write(chunk)
        info = zf.getinfo(member)
        print(f"zip_member\t{member}")
        print(f"zip_member_bytes\t{info.file_size}")
        print(f"zip_member_date\t{info.date_time[0]:04d}-{info.date_time[1]:02d}-{info.date_time[2]:02d} {info.date_time[3]:02d}:{info.date_time[4]:02d}")
        return out


def write_sample(csv_path: Path, sample_path: Path, n: int) -> dict[str, object]:
    sample_path.parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as src, open(
        sample_path, "w", encoding="utf-8", newline=""
    ) as dst:
        reader = csv.reader(src)
        writer = csv.writer(dst, lineterminator="\n")
        try:
            meta_headers = next(reader)
            meta_values = next(reader)
            data_headers = next(reader)
        except StopIteration as exc:
            raise SystemExit("CSV ended before the three CMS header rows") from exc
        writer.writerow(meta_headers)
        writer.writerow(meta_values)
        writer.writerow(data_headers)

        written = 0
        total = 0
        for row in reader:
            total += 1
            if written < n:
                writer.writerow(row)
                written += 1

    meta = {
        h.strip(): v.strip()
        for h, v in zip(meta_headers, meta_values)
        if h.strip() or v.strip()
    }
    # attestation header is a long paragraph; keep a short key
    attester = meta.get("attester_name", "")
    last_updated = meta.get("last_updated_on", "")
    return {
        "hospital_name": meta.get("hospital_name", ""),
        "last_updated_on": last_updated,
        "version": meta.get("version", ""),
        "location_name": meta.get("location_name", ""),
        "hospital_address": meta.get("hospital_address", ""),
        "type_2_npi": meta.get("type_2_npi", ""),
        "attester_name": attester,
        "data_columns": len(data_headers),
        "data_rows": total,
        "sample_rows": written,
        "sample_path": str(sample_path),
        "core_headers": data_headers[:21],
        "wide": any(h.startswith("standard_charge|") and "|negotiated_dollar" in h for h in data_headers),
        "tall_payer_col": "payer_name" in data_headers,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--index-url", default=INDEX_URL)
    parser.add_argument("--work-dir", type=Path, default=DEFAULT_WORK)
    parser.add_argument("--sample-out", type=Path, default=DEFAULT_SAMPLE)
    parser.add_argument("--rows", type=int, default=DEFAULT_ROWS)
    args = parser.parse_args()

    print(f"fetch_index\t{args.index_url}")
    index_bytes = fetch(args.index_url)
    args.work_dir.mkdir(parents=True, exist_ok=True)
    index_path = args.work_dir / "cms-hpt.txt"
    index_path.write_bytes(index_bytes)
    records = parse_index(index_bytes.decode("utf-8", errors="replace"))
    print(f"index_locations\t{len(records)}")
    fmc = pick_fmc(records)
    zip_url = fmc["mrf-url"]
    print(f"fmc_mrf_url\t{zip_url}")

    print("fetch_zip\tstart")
    zip_bytes = fetch(zip_url)
    zip_path = args.work_dir / "860110232_FLAGSTAFFMEDICALCENTER_standardcharges.zip"
    zip_path.write_bytes(zip_bytes)
    print(f"zip_bytes\t{len(zip_bytes)}")

    csv_path = extract_csv(zip_bytes, args.work_dir)
    print(f"csv_path\t{csv_path}")
    print(f"csv_bytes\t{csv_path.stat().st_size}")

    stats = write_sample(csv_path, args.sample_out, args.rows)
    layout = "csv_wide" if stats["wide"] and not stats["tall_payer_col"] else (
        "csv_tall" if stats["tall_payer_col"] else "unknown"
    )
    print(f"format\t{layout}")
    print(f"version\t{stats['version']}")
    print(f"hospital_name\t{stats['hospital_name']}")
    print(f"last_updated_on\t{stats['last_updated_on']}")
    print(f"type_2_npi\t{stats['type_2_npi']}")
    print(f"data_columns\t{stats['data_columns']}")
    print(f"data_rows\t{stats['data_rows']}")
    print(f"sample_rows\t{stats['sample_rows']}")
    print(f"sample_path\t{stats['sample_path']}")
    print("core_headers\t" + ",".join(stats["core_headers"]))
    print("note\tzip and full CSV remain in --work-dir; do not commit them")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
