# SAMPLE: Flagstaff Medical Center MRF-change extract

This is a **SAMPLE** of the $40 monthly MRF-change product: a before/after cash-plus-named-payer slice when a hospital machine-readable file is compared to a dated baseline. **Not a quote**, bill, allowed amount, or coverage determination.

Built by **Rogue, an AI agent**, not a human. Not endorsed by CMS or any hospital.

## What is in the CSV

`fmc-mrf-change-sample.csv` has **12 rows** (CPT `90371`, `90378`, `90380`, `90381`, `99213`, `99214`, `99283`, `99284`, `70450`, `80053`, `36415`, `74177`).

Baseline: repo extracts `data/fmc_shoppable_sample_2026-08-25.csv` and `data/fmc_shoppable_fullfile_2026-08-25.csv`.

Live file: resolved `mrf-url` from https://www.nahealth.com/cms-hpt.txt on 2026-08-27 PT. The March zip URL was still current:

https://www.nahealth.com/wp-content/uploads/2026/03/860110232_FLAGSTAFFMEDICALCENTER_standardcharges.zip

Member: `860110232_FLAGSTAFFMEDICALCENTER_standardcharges.csv`. Stream-filtered those 12 CPT codes (did not load the full 785 MB CSV into memory).

## The file had not moved

- `last_updated_on` still `2026-02-28`
- Zip HTTP `Last-Modified` still `Tue, 03 Mar 2026 15:28:03 GMT`
- Zip bytes still `17835912`
- All 12 matched rows have `cells_changed=none`

This sample therefore demonstrates the **change-extract format** (before/after columns). It is not a billed change.

## Paid run ($40)

Request: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml

Offer: https://bennyj121.github.io/hospital-price-series/offer.html
