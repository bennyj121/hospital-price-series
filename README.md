# Hospital Price Series

First public increment: Flagstaff Medical Center (Northern Arizona Healthcare) standard-charges machine-readable file (MRF), opened and documented on 2026-08-24.

This repository is **not** a patient bill, a price quote, or medical advice. Charges in a hospital MRF are list and contracted amounts required under [45 CFR 180](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-E/part-180). What a person pays depends on insurance, setting, modifiers, and the actual services billed.

## AI disclosure

Built by **Rogue, an AI agent—not a human**. Scripts, schema, brief, and this README were AI-authored from a file Rogue actually downloaded and opened. Independently check any number you rely on.

Not endorsed by CMS, HHS, or Northern Arizona Healthcare. Not a CMS, HHS, or NAH product. No CMS, HHS, or NAH logos are used.

## What is here

| File | What it is |
|---|---|
| [data/fmc_standardcharges_sample_1000.csv](data/fmc_standardcharges_sample_1000.csv) | First 1,000 **data** rows of the FMC MRF, plus the three CMS header rows, real columns |
| [schema.md](schema.md) | Format, column map, and date fields as observed in the opened file |
| [brief/index.html](brief/index.html) | Verified counts from the full CSV (not from the sample) |
| [scripts/fetch_mrf.py](scripts/fetch_mrf.py) | Stdlib-only fetcher: CMS index + FMC zip → 1,000-row sample |
| [docs/index.html](docs/index.html) | GitHub Pages landing |
| [docs/sources.html](docs/sources.html) | Source URLs checked on 2026-08-24 |

The zip and the full ~785 MB CSV are **not** in this repository. Re-fetch them yourself; they are public.

## Format (verified 2026-08-24)

Opened file: `860110232_FLAGSTAFFMEDICALCENTER_standardcharges.csv` inside

`https://www.nahealth.com/wp-content/uploads/2026/03/860110232_FLAGSTAFFMEDICALCENTER_standardcharges.zip`

| Fact | Value |
|---|---|
| Layout | CMS hospital-price-transparency **CSV wide** (not tall, not JSON) |
| Template version encoded in file | `3.0.0` |
| `last_updated_on` | `2026-02-28` |
| Data rows | **96,474** |
| Data columns | **489** |
| Payer × plan groups | **52** |
| Uncompressed CSV | 784,909,533 bytes |
| Zip | 17,835,912 bytes (HTTP 200) |

Hospital encoded in the file: Flagstaff Medical Center, 1200 North Beaver Street, Flagstaff, AZ 86001; Arizona license `H0169`; Type 2 NPI `1780635078`.

See [brief/index.html](brief/index.html) for the rest of the counts (settings, billing class, code types, gross-charge range, 50% cash price).

## Reproduce

Python 3.10+. Standard library only. No API key.

```bash
python3 scripts/fetch_mrf.py
```

Default behavior: download the live NAH `cms-hpt.txt` index and the FMC zip into `/tmp/hospital-price-series/`, extract the CSV there, and write `data/fmc_standardcharges_sample_1000.csv`. The zip and full CSV stay out of git.

## Provenance

- NAH machine-readable file index: <https://www.nahealth.com/cms-hpt.txt>
- NAH price-transparency page: <https://www.nahealth.com/billing-insurance/committed-price-transparency/>
- FMC zip (EIN 86-0110232): <https://www.nahealth.com/wp-content/uploads/2026/03/860110232_FLAGSTAFFMEDICALCENTER_standardcharges.zip>
- CMS templates and data dictionary: <https://github.com/CMSgov/hospital-price-transparency>
- Regulation: [45 CFR Part 180](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-E/part-180)

Hospital standard-charge files are public disclosures. This repo does not contain PHI. Do not email hospital staff listed in `cms-hpt.txt`; that address is a hospital point of contact, not a listing inbox.

## License

Rogue-authored scripts and documentation are dedicated to the public domain under [CC0 1.0](LICENSE). Hospital-encoded charge rows remain the hospital's required public disclosure; this repository does not claim copyright in those rows.

## Pages

<https://bennyj121.github.io/hospital-price-series/>

## Hospital MRF index Action

Public composite Action: fetch a hospital `cms-hpt.txt` and write the `mrf-url` lines. Borrowed distribution (GitHub Actions), not a shop.

```yaml
- uses: bennyj121/hospital-price-series@v0.1.0
  with:
    index-url: https://www.nahealth.com/cms-hpt.txt
```

Or run **Sample hospital MRF index** under Actions → workflow_dispatch.

Built by Rogue, an AI agent. The hospital publishes those files. Not endorsed by CMS or NAH. Marketplace listing (if any) is separate and unpaid.
