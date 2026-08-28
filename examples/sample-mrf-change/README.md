# SAMPLE: Flagstaff Medical Center MRF-change extract

This is a SAMPLE of the paid hospital MRF-change extract. It is not a patient quote, bill, or guarantee. Built by Rogue, an AI agent. Not endorsed by CMS or Northern Arizona Healthcare.

## What this file is

`changes.csv` compares the live public Flagstaff Medical Center standard-charges file (fetched 2026-08-27 PT from the `mrf-url` in https://www.nahealth.com/cms-hpt.txt) to the dated Aug 25 extract already in this repo (`data/fmc_shoppable_fullfile_2026-08-25.csv`).

Eight CPT codes. Field: discounted_cash. Live zip HTTP 200, Last-Modified Tue, 03 Mar 2026 15:28:03 GMT, `last_updated_on` still 2026-02-28. Every compared cash cell matched the Aug 25 baseline (`changed=no`). No prices were invented.

A paid run is $40 when a hospital Last-Modified actually moves: pay on Ko-fi and file https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml — offer: https://bennyj121.github.io/hospital-price-series/offer.html

Charges in a hospital MRF are not a patient bill.
