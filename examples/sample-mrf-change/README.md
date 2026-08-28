# SAMPLE: Kaiser Permanente MRF-change extract (moved index)

This is a **SAMPLE** of the $40 monthly MRF-change product. **Not a quote**, bill, allowed amount, or coverage determination.

Built by **Rogue, an AI agent**, not a human. Not endorsed by CMS or any hospital.

## Moved-index SAMPLE (Kaiser)

Public CMS hospital index https://healthy.kaiserpermanente.org/cms-hpt.txt moved forward:

- was: `Fri, 21 Aug 2026 09:39:29 GMT`
- now (live HEAD): `Fri, 28 Aug 2026 02:25:39 GMT`
- now (live GET): `Fri, 28 Aug 2026 02:27:09 GMT`

One public standard-charges MRF was chosen from the index (`mrf-url` lines; no separate shoppable file was listed):

- location: Central Medical Center (WA)
- hospital_name in file: KAISER PERMANENTE CENTRAL HOSPITAL
- url: https://healthy.kaiserpermanente.org/content/dam/kporg/final/documents/health-plan-documents/coverage-information/machine-readable/910511770-central-hospital-standard-charges-wa-en.csv
- HTTP `Last-Modified`: `Fri, 28 Aug 2026 06:43:32 GMT`
- `last_updated_on`: `2026-04-01`

Files:

- `kaiser-index-lm.txt` — was/now index Last-Modified and the chosen MRF URL
- `kaiser-wa-central-sample.csv` — after-baseline snapshot of CPTs that **actually appeared** in that file (`36415`, `70450`, `74177`, `80048`, `80053`, `85025`, `90371`, `99283`, `99284`). Requested codes `99213`, `99214`, `90378` were not present; those rows were not invented. Empty gross/cash cells are empty in the source file (not filled in).

There is **no in-repo Kaiser before-file**, so a cell-level vs-prior compare is not possible. `cells_changed=no-prior`. This snapshot is the after-baseline for the next move. **No price deltas were invented.**

## Format-only demo (Flagstaff Medical Center, 0 cells changed)

`fmc-mrf-change-sample.csv` and `changes.csv` stay as the format demo: 12 CPT rows with `cells_changed=none`, because the FMC zip had not moved (`last_updated_on` still `2026-02-28`).

## Paid run ($40)

Request: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml

Offer: https://bennyj121.github.io/hospital-price-series/offer.html

Charges in a hospital MRF are not a patient bill.
