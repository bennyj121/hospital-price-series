#!/usr/bin/env python3
"""Write a dated cash-plus-named-payer extract from a CMS CSV-wide MRF.

Reads a local hospital standard-charges CSV (wide layout) and a CPT list.
Does not download anything. Standard library only.

Built by Rogue, an AI agent. Not a patient quote, bill, or guarantee.
Not endorsed by CMS or any hospital.
"""

from __future__ import annotations

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

DEFAULT_PAYERS = [
    ("discounted_cash", "standard_charge|discounted_cash"),
    ("aetna_commercial_negotiated_dollar", "standard_charge|Aetna Healthcare|Aetna Commercial|negotiated_dollar"),
    ("bcbs_az_hmo_negotiated_dollar", "standard_charge|BCBS AZ|BCBS HMO|negotiated_dollar"),
    ("united_healthcare_commercial_negotiated_dollar", "standard_charge|United Healthcare|United Healthcare Commercial|negotiated_dollar"),
]


def parse_cpts(raw: str) -> list[str]:
    parts = [p.strip() for p in raw.replace("\n", ",").split(",")]
    return [p for p in parts if p]


def open_wide(path: Path) -> tuple[str, str, csv.DictReader]:
    fh = path.open(encoding="utf-8", newline="")
    first = fh.readline()
    second = fh.readline()
    if first.startswith("hospital_name"):
        hospital = "Flagstaff Medical Center"
        last_updated = "2026-02-28"
        rest = second.split(",")
        if len(rest) > 1:
            hospital = rest[0] or hospital
            last_updated = rest[1].strip() or last_updated
        reader = csv.DictReader(fh)
        return hospital, last_updated, reader
    fh.seek(0)
    reader = csv.DictReader(fh)
    return "", "", reader


def first_cpt(row: dict[str, str]) -> str | None:
    for i in range(1, 6):
        t = (row.get(f"code|{i}|type") or "").strip().upper()
        c = (row.get(f"code|{i}") or "").strip()
        if t == "CPT" and c:
            return c
    return None


def main() -> int:
    p = argparse.ArgumentParser(
        description="CMS wide CSV → cash + named-payer extract",
        epilog=(
            chr(36)
            + "40 hospital MRF-change extract (not a quote)\n"
            + "https://bennyj121.github.io/hospital-price-series/offer.html\n"
            + "SAMPLE at examples/sample-mrf-change/ (fmc-mrf-change-sample.csv)"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--csv", required=True, help="Local CMS CSV-wide file")
    p.add_argument("--cpts", required=True, help="Comma-separated CPT codes that must appear")
    p.add_argument("--out", required=True, help="Output CSV path")
    args = p.parse_args()
    wanted = parse_cpts(args.cpts)
    if not wanted:
        print("no CPT codes", file=sys.stderr)
        return 2
    src = Path(args.csv)
    hospital, last_updated, reader = open_wide(src)
    picked: dict[str, dict[str, str]] = {}
    for row in reader:
        cpt = first_cpt(row)
        if cpt and cpt in wanted and cpt not in picked:
            picked[cpt] = row
    fields = [
        "hospital_name",
        "last_updated_on",
        "extract_date",
        "description",
        "cpt",
        "setting",
        "billing_class",
        "gross",
        *[name for name, _ in DEFAULT_PAYERS],
        "note",
    ]
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for cpt in wanted:
            row = picked.get(cpt)
            if not row:
                continue
            rec = {
                "hospital_name": hospital,
                "last_updated_on": last_updated,
                "extract_date": date.today().isoformat(),
                "description": row.get("description", ""),
                "cpt": cpt,
                "setting": row.get("setting", ""),
                "billing_class": row.get("billing_class", ""),
                "gross": row.get("standard_charge|gross", ""),
                "note": "Sample extract, not a patient quote. Built by Rogue, an AI agent.",
            }
            for name, col in DEFAULT_PAYERS:
                rec[name] = row.get(col, "")
            w.writerow(rec)
            n += 1
    print(f"rows={n} out={out} cpts_requested={len(wanted)} cpts_found={n}")
    print(chr(36) + "40 hospital MRF-change extract (not a quote)")
    print("https://bennyj121.github.io/hospital-price-series/offer.html")
    print("SAMPLE at examples/sample-mrf-change/ (fmc-mrf-change-sample.csv)")
    return 0 if n else 1


if __name__ == "__main__":
    raise SystemExit(main())