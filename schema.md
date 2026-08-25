# Schema — Flagstaff Medical Center standard charges

Observed in the file opened on 2026-08-24 (PT), not copied from a template.

Source CSV: `860110232_FLAGSTAFFMEDICALCENTER_standardcharges.csv`
inside `860110232_FLAGSTAFFMEDICALCENTER_standardcharges.zip`.

CMS reference (not a substitute for the opened file):
[CMSgov/hospital-price-transparency CSV data dictionary v3.0](https://github.com/CMSgov/hospital-price-transparency/blob/master/documentation/CSV/README.md).

## File format

| Property | Observed value |
|---|---|
| Container | ZIP, one member |
| Member name | `860110232_FLAGSTAFFMEDICALCENTER_standardcharges.csv` |
| Member uncompressed size | 784,909,533 bytes |
| Member timestamp in zip | 2026-03-02 21:20 |
| Zip HTTP size | 17,835,912 bytes |
| Zip HTTP `Last-Modified` | 2026-03-03 15:28:03 GMT |
| Character encoding | UTF-8, no BOM |
| Delimiter | comma |
| Line endings | CRLF |
| Quoting | RFC 4180; attestation header and hospital address are quoted |
| Layout | **CSV wide** (payer and plan names are in column headers, not rows) |
| Not | CSV tall, not JSON |
| CMS template version (row 2, `version`) | `3.0.0` |
| Data rows | 96,474 |
| Data columns | 489 |
| Column-count mismatches | 0 |

## Row layout (CSV wide)

CMS wide files put general hospital elements in rows 1–2 and item/service columns starting at row 3.

| Row | Role |
|---|---|
| 1 | Hospital metadata **headers** (most cells after `attester_name` are empty placeholders so the row is 489 cells wide) |
| 2 | Hospital metadata **values** |
| 3 | Item/service and payer-plan **column headers** |
| 4+ | One item/service/setting row each (96,474 rows) |

There is **no per-row date column**. The only date field in the file is `last_updated_on` in the metadata block.

## Date fields

| Field | Where | Value in this file | Notes |
|---|---|---|---|
| `last_updated_on` | row 2, column 2 | `2026-02-28` | ISO 8601 date. The raw cell has leading spaces (`    2026-02-28`); strip before parsing. |
| Zip HTTP `Last-Modified` | response header | 2026-03-03 15:28:03 GMT | Not inside the CSV. |
| Zip member timestamp | zip central directory | 2026-03-02 21:20 | Not inside the CSV. |
| NAH index `Last-Modified` | `cms-hpt.txt` header | 2026-03-03 16:52:56 GMT | Not inside the CSV. |

## Hospital metadata (rows 1–2)

Non-empty pairs in this file:

| Header (row 1) | Value (row 2) |
|---|---|
| `hospital_name` | Flagstaff Medical Center |
| `last_updated_on` | 2026-02-28 (leading spaces in file) |
| `version` | 3.0.0 |
| `location_name` | Flagstaff Medical Center |
| `hospital_address` | 1200 North Beaver Street, Flagstaff, AZ 86001 |
| `license_number\|AZ` | H0169 |
| `type_2_npi` | 1780635078 |
| *(CMS attestation statement; full 45 CFR 180.50 text is the header)* | `TRUE` |
| `attester_name` | Dave Cheney |

The attestation header is the CMS-required paragraph beginning “To the best of its knowledge and belief…”. This repository treats the encoded boolean as a file fact, not as an endorsement.

## Core item/service columns (row 3, positions 0–20)

These 21 columns are not payer-specific.

| # | Header | Role in this file |
|---|---|---|
| 0 | `description` | Item/service text. 28,609 distinct values. Never blank. |
| 1 | `code\|1` | Primary code. Usually a chargemaster (CDM) number. |
| 2 | `code\|1\|type` | `CDM` (93,398), `APR-DRG` (1,330), `RC` (953), `MS-DRG` (766), blank (27). |
| 3 | `code\|2` | Secondary code (often revenue code `RC`, sometimes `CPT`). |
| 4 | `code\|2\|type` | `RC` (93,398), `CPT` (953), blank (2,123). |
| 5 | `code\|3` | Tertiary code (often `NDC` or `HCPCS`). |
| 6 | `code\|3\|type` | Matching type for `code\|3`. |
| 7 | `code\|4` | Optional fourth code. |
| 8 | `code\|4\|type` | Matching type. |
| 9 | `code\|5` | Optional fifth code. |
| 10 | `code\|5\|type` | Matching type. |
| 11 | `modifiers` | CPT/HCPCS modifiers when present. |
| 12 | `setting` | `inpatient` (36,846) or `outpatient` (59,628). No `both`. |
| 13 | `billing_class` | Optional CMS field. `facility` (74,144) or `professional` (22,330). |
| 14 | `drug_unit_of_measurement` | Numeric drug unit when the row is a drug. |
| 15 | `drug_type_of_measurement` | `EA` and other CMS drug units when present. |
| 16 | `standard_charge\|gross` | Gross / chargemaster amount. Present on 94,351 rows. |
| 17 | `standard_charge\|discounted_cash` | Cash price. Present on the same 94,351 rows. |
| 18 | `standard_charge\|min` | De-identified minimum negotiated charge. |
| 19 | `standard_charge\|max` | De-identified maximum negotiated charge. |
| 20 | `additional_generic_notes` | Free text. Often empty. |

Gross and discounted-cash cells are unquoted decimal numbers (no `$`, no thousands separators). Example from data row 1: gross `783.9`, cash `391.95`.

On every row that has a gross charge, discounted cash equals **exactly half** of gross (94,351 / 94,351). That is an observation about this file, not a CMS rule.

Gross is blank on all 1,330 inpatient `APR-DRG` rows, all 766 inpatient `MS-DRG` rows, and 27 outpatient rows with a blank `code\|1\|type`.

## Payer-plan columns (row 3, positions 21–488)

52 payer × plan groups. Each group uses the CMS wide nine-column set:

```
standard_charge|{payer}|{plan}|negotiated_dollar
standard_charge|{payer}|{plan}|negotiated_percentage
standard_charge|{payer}|{plan}|negotiated_algorithm
standard_charge|{payer}|{plan}|methodology
median_amount|{payer}|{plan}
10th_percentile|{payer}|{plan}
90th_percentile|{payer}|{plan}
count|{payer}|{plan}
additional_payer_notes|{payer}|{plan}
```

21 + 52 × 9 = 489.

Payer and plan names as they appear in the headers (order of first appearance):

| Payer | Plan |
|---|---|
| Aetna Banner | Aetna Banner |
| Aetna Healthcare | Aetna Commercial |
| Aetna Healthcare | Aetna Med Advantage |
| AHCCCS | AHCCCS |
| Health Net of Arizona | AHCCCS AZCH COMPLETE HEALTHCARE |
| AHCCCS Other | AHCCCS Other |
| Ambetter Marketplace | Ambetter Marketplace |
| Auto Insurance | Auto Insurance |
| Health Choice Arizona | BCBS Health Choice Standard Health ACA |
| BCBS AZ | BCBS HMO |
| CareFirst | CareFirst |
| Cigna Healthcare | Cigna HMO |
| Copperpoint | Copperpoint |
| Devoted | Devoted |
| FMC 90/10 | FMC 90/10 |
| FMC IHS | FMC IHS |
| FMC Jail | FMC Jail |
| Health Choice | Health Choice AHCCCS |
| Health Choice | Health Choice Commercial |
| Health Choice | Health Choice Generations |
| Health Choice Integrated Care | Health Choice Integrated Care |
| Health Net Federal | Health Net Federal - Tricare |
| Humana ChoiceCare | Humana ChoiceCare |
| Humana | Humana Managed Medicare |
| Medicare | Medicare |
| FMC 30/70 | Medicare Other |
| United Healthcare | Medicare UHC |
| Mercy Care | Mercy Care |
| Mercy Care Advantage | Mercy Care Advantage |
| Mercy Care RHBA | Mercy Care RHBA |
| NaphCare | NaphCare |
| NAU Athletic Department | NAU Athletic Department |
| BCBS AZ | Neighborhood Network BCBS |
| NHI Out of State AHCCCS | NHI Out of State AHCCCS |
| Self Pay | Northern Arizona Healthcare Self Pay |
| PNOA | PNOA-Provider Network of America |
| Rehabilitation Hospital of Northern Arizona | Rehabilitation Hospital of Northern Arizona |
| Rural Arizona Network Multiplan | Rural Arizona Network Multiplan |
| Self-Pay 50% Discount | Self-Pay 50 Discount |
| Self Pay | Self-Pay No Discount |
| SNF FMC | SNF FMC |
| VA PCCC TriWest | Triwest Healthcare Alliance |
| UMR NAH UHC | UMR NAH UHC |
| United Behavioral Health | United Behavioral Health (Commercial) |
| United Behavioral Health | United Behavioral Health (Medicare) |
| United Healthcare | United Healthcare APIPA AHCCCS |
| United Healthcare | United Healthcare Commercial |
| University of Arizona Health Plans | University of Arizona Health Plans Med Advantage |
| University of Arizona Health Plans | University of Arizona Health Plans Medicaid |
| Wellcare | Wellcare |
| Wellcare by Allwell | Wellcare by Allwell |
| Workers Comp | Workers Comp |

Non-empty `methodology` cells across all 52 groups (cell counts, not row counts):

| Value | Cells |
|---|---|
| `percent of total billed charges` | 964,553 |
| `other` | 627,869 |
| `fee schedule` | 396,302 |
| `case rate` | 37,286 |
| `per diem` | 14 |

These are the CMS v3.0 enum values.

## Sample file

`data/fmc_standardcharges_sample_1000.csv` keeps rows 1–3 exactly as in the source (so metadata and all 489 headers survive) and then the **first 1,000 data rows in file order**.

That slice is pharmacy/CDM-heavy (210 distinct descriptions; all 1,000 rows are `billing_class=facility`). It is a preview, not a random or representative sample. Full-file counts belong in [brief/index.html](brief/index.html).

## What this schema is not

- Not a claim form, chargemaster extract for billing, or patient estimate.
- No patient identifiers, encounter IDs, or PHI.
- Header spelling follows the opened file (`license_number|AZ`, pipe separators, no spaces around pipes).
