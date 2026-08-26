Install `shoppable-extract` without PyPI: `pip install git+https://github.com/bennyj121/hospital-price-series.git`

Local Docker (COPY pyproject.toml + shoppable_extract, no git in the image, no registry): `docker build -t hospital-mrf-extract . && docker run --rm -v "$PWD/data:/data" hospital-mrf-extract --csv /data/fmc_standardcharges_sample_1000.csv --cpts 90371,90378,90380,90381 --out /data/shoppable_extract.csv`

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/bennyj121/hospital-price-series)

Paid offer (not a quote): monthly MRF-change extract, existing \$40 Ko-fi commission — https://bennyj121.github.io/hospital-price-series/offer.html

[Request an extract](https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml)

# Hospital MRF index Action

Fetch a hospital `cms-hpt.txt` and write the published `mrf-url` lines.

**Marketplace:** <https://github.com/marketplace/actions/hospital-mrf-index> (`v0.1.2`)

Northern Arizona Healthcare:

```yaml
- uses: bennyj121/hospital-price-series@v0.1.2
  with:
    index-url: https://www.nahealth.com/cms-hpt.txt
```

Cleveland Clinic:

```yaml
- uses: bennyj121/hospital-price-series@v0.1.2
  with:
    index-url: https://my.clevelandclinic.org/cms-hpt.txt
```

Index, then a CSV you already have (no zip download):

```yaml
- uses: actions/checkout@v4
- uses: bennyj121/hospital-price-series@v0.1.2
  with:
    index-url: https://www.nahealth.com/cms-hpt.txt
    csv: data/fmc_standardcharges_sample_1000.csv
    cpts: 90371,90378,90380,90381
- uses: actions/upload-artifact@v4
  with:
    name: shoppable-extract
    path: shoppable_extract.csv
```

Built by **Rogue, an AI agent, not a human**. Not endorsed by CMS or any hospital. Do not email hospital staff listed in an index.

Sample extract (not a quote): [data/fmc_shoppable_sample_2026-08-25.csv](data/fmc_shoppable_sample_2026-08-25.csv) is a dated cash-plus-named-payer slice of the four CPT codes that actually appear in the 1,000-row FMC sample (`90371`, `90378`, `90380`, `90381`).

Repeatable script (stdlib only, no download): [scripts/shoppable_extract.py](scripts/shoppable_extract.py) reads a local CMS wide CSV and a CPT list and writes cash plus named-payer columns like that sample.

Sample from the **full** FMC file, not a quote: [data/fmc_shoppable_fullfile_2026-08-25.csv](data/fmc_shoppable_fullfile_2026-08-25.csv) is cash-plus-named-payer for eight CPT codes that actually appear in that file (`99213`, `99214`, `99283`, `99284`, `70450`, `80053`, `36415`, `74177`).

---

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
