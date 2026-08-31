# HITL / NOT PUBLISHED — do not list, sell, or post

**Status:** HITL draft only. Not published. Not live on muonarc.com. Atlas has not named this as the first live Note. Do not invent a live muonarc.com URL. Do not post, list, merge, email, or ship.

**SKU:** Candidate 1 only — USAspending Weekly NAICS 541512 Prime Awards (DoD / HHS / DHS). Not candidates 2–3. Not the $40 hospital MRF-change extract. Not a hospital-price-series paid SKU. Not OpenFEMA. Not NHC. Not Ko-fi. Not GitHub Marketplace.

**AI disclosure (Rogue):** An AI (Rogue + helper bots) prepared this brief. Benjamin / Atlas reviews before any Note goes live. Any live Note would state it is AI-built.

**Data rail:** Public USAspending.gov APIs and bulk files only. Legal public information. No PHI. No hospital MRF. No scraped private data. No credentials.

---

# USAspending Weekly: NAICS 541512 Prime Awards (DoD, HHS, DHS)

## Pitch

Each Monday, a bot-built Note lists new USAspending.gov prime awards ≥$250k in NAICS 541512 (computer systems design) from DoD, HHS, and DHS in the prior 7 days: awardee, amount, PIID, place of performance, NAICS, awarding office, and source URL. Public bulk/API only. Same pack next Monday. Not hospital MRF, not OpenFEMA, not NHC.

## Price band

**$8–$20 / note**, or **$12–$40 / month retain**.

Per-note is a single Monday pack. Monthly retain is four consecutive Monday packs (same NAICS, same three agencies, same field set). Price is for the digital good on muonarc.com Notes — not GitHub, not Ko-fi, not Marketplace.

## Delivery format

Markdown/HTML Note plus optional CSV of the week's awards (zip if >1 file). Not a GitHub issue form. Not a Marketplace Action. Not a Ko-fi product.

Typical Monday drop:

- One HTML/Markdown Note (the human-readable brief).
- One CSV of that week's prime awards (same rows as the table in the Note).
- Zip only if the week also needs a second file (e.g. agency split + combined table). Most weeks are Note + one CSV.

Cadence: **every Monday**, covering **action dates in the prior 7 days** (Monday–Sunday preceding the drop, US Eastern). Same pack next Monday. Repeatable. A bot team can regenerate it from public USAspending APIs without human scraping.

---

## Sample-week outline (what the buyer actually gets that week)

**Week label:** Week of 2026-08-24 → drop Monday 2026-08-31. Window: action_date 2026-08-24 through 2026-08-30 ET.

**Scope (fixed every week — do not widen):**

| Filter | Value |
| --- | --- |
| Source | USAspending.gov Award Search API (`/api/v2/search/spending_by_award/`) and/or public bulk Award download. Public endpoints only. |
| Award type | Prime **contracts** only (award type codes A, B, C, D). No subawards, no grants, no IDV-only rows unless a funded prime obligation also lands in the window. |
| NAICS | **541512** — Computer Systems Design Services (exact code; do not expand to 54151x). |
| Awarding agencies | **DoD** (toptier 097), **HHS** (toptier 075), **DHS** (toptier 070) only. |
| Floor | Obligation / awarded amount **≥ $250,000** in the row as USAspending reports it. |
| Time | `action_date` in the prior 7 days. New or modified primes that posted in-window. |
| Place of performance | Included as reported (city, state, country). No geocoding beyond USAspending fields. |

If a week has **zero** rows after filters, the Note still ships: headline "0 primes ≥$250k this window," empty CSV with header row, and a one-line "nothing new" callout. Buyer still gets the pack. That is the product.

### Section 1 — Week at a glance

62 primes ≥$250k this window; $2,282,061,723.05 awarded (DoD 0 / $0.00, HHS 32 / $1,148,843,936.91, DHS 30 / $1,133,217,786.14); largest GENERAL DYNAMICS INFORMATION TECHNOLOGY, INC. $541,992,951.00 PIID 75FCMC25FJ022

- Window: action_date 2026-08-24 through 2026-08-30 ET.
- Row count: 62 primes.
- Sum of awarded amounts this window: $2,282,061,723.05 (Award Amount / total_obligation as USAspending reports it).
- Split by awarding toptier: DoD (097) 0 / $0.00; HHS (075) 32 / $1,148,843,936.91; DHS (070) 30 / $1,133,217,786.14.
- Largest single prime: GENERAL DYNAMICS INFORMATION TECHNOLOGY, INC. $541,992,951.00 PIID 75FCMC25FJ022 (Department of Health and Human Services).
- Source pull: 2026-08-30 8:21 PM PT (2026-08-31 03:21:57 UTC). USAspending Award Search API `POST /api/v2/search/spending_by_award/` with `date_type=action_date`; award profile `GET /api/v2/awards/{generated_unique_award_id}/`; in-window `action_date` from `POST /api/v2/transactions/`. Public, no login.

No commentary beyond those facts. No "hot take." No BD advice.

### Section 2 — Agency totals table

| Awarding agency | n primes | sum awarded | largest awardee | largest amount |
| --- | ---: | ---: | --- | ---: |
| Department of Defense | 0 | $0.00 | — | — |
| Department of Health and Human Services | 32 | $1,148,843,936.91 | GENERAL DYNAMICS INFORMATION TECHNOLOGY, INC. | $541,992,951.00 |
| Department of Homeland Security | 30 | $1,133,217,786.14 | GENERAL DYNAMICS INFORMATION TECHNOLOGY, INC. | $307,159,419.42 |
| **Total** | **62** | **$2,282,061,723.05** | — | — |

### Section 3 — Prime awards table (the week's rows)

One row per prime that passed the filters. Sorted by awarded amount descending, then PIID. Description truncated to ~200 chars here; full text in the CSV. CSV path: `drafts/usaspending-541512-dod-hhs-dhs-2026-08-31.csv`.

| Field | Source (USAspending public) | Notes |
| --- | --- | --- |
| awardee | Recipient Name | Legal name as reported |
| uei | Recipient UEI | If present on the award row |
| amount | Award Amount / Awarded Amount | USD; ≥ $250,000 floor already applied |
| piid | Award ID / PIID | Prime identifier |
| awarding_agency | Awarding Agency | DoD / HHS / DHS toptier |
| awarding_sub_agency | Awarding Sub Agency | e.g. Defense Information Systems Agency |
| awarding_office | Awarding Office | Office name + office code if present |
| naics | NAICS | 541512 + official description string |
| pop_city | Place of Performance City | As reported |
| pop_state | Place of Performance State | 2-letter if US |
| pop_country | Place of Performance Country | |
| action_date | Action Date | In-window date that pulled the row |
| start_date | Period of Performance Start | If present |
| end_date | Period of Performance End | If present |
| description | Award Description | Truncate in the Note to ~200 chars; full text in CSV |
| source_url | USAspending award page | `https://www.usaspending.gov/award/{generated_unique_award_id}` — public page, not an API key |

| awardee | uei | amount | piid | awarding_agency | awarding_sub_agency | awarding_office | naics | pop_city | pop_state | pop_country | action_date | start_date | end_date | description | source_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GENERAL DYNAMICS INFORMATION TECHNOLOGY, INC. | SMNWM6HN79X5 | $541,992,951.00 | 75FCMC25FJ022 | Department of Health and Human Services | Centers for Medicare and Medicaid Services | OFC OF ACQUISITION AND GRANTS MGMT | 541512 — Computer Systems Design Services | WINDSOR MILL | MD | UNITED STATES | 2026-08-27 | 2025-02-20 | 2027-06-30 | THE CLOUD PRODUCTS AND TOOLS (CPT) CONTRACT IS USED TO PROVIDE CLOUD-BASED INFRASTRUCTURE FROM COMMERCIAL CLOUD SERVICE PROVIDERS (CSP) SUCH AS MICROSOFT AZURE GOVERNMENT (MAG) AND AMAZON WEB SERVICES… | https://www.usaspending.gov/award/CONT_AWD_75FCMC25FJ022_7530_47QTCK18D0003_4732 |
| GENERAL DYNAMICS INFORMATION TECHNOLOGY, INC. | SMNWM6HN79X5 | $307,159,419.42 | 70RDA124FR0000005 | Department of Homeland Security | Office of Procurement Operations | DEPARTMENTAL OPERATIONS ACQUISITION DIVISION I | 541512 — Computer Systems Design Services | ARLINGTON | VA | UNITED STATES | 2026-08-24 | 2023-12-31 | 2026-12-30 | OPERATE AND MAINTAIN THE OBIM INFRASTRUCTURE COMPONENTS AND ASSOCIATED APPLICATIONS AND OTHER FUNCTIONALITY OF THE PRODUCTION AND NON-PRODUCTION ENVIRONMENTS AND ASSOCIATED BUSINESS SYSTEMS CURRENTLY… | https://www.usaspending.gov/award/CONT_AWD_70RDA124FR0000005_7001_47QTCK18D0003_4732 |
| GENERAL DYNAMICS INFORMATION TECHNOLOGY, INC. | SMNWM6HN79X5 | $219,302,285.42 | 75FCMC23F0156 | Department of Health and Human Services | Centers for Medicare and Medicaid Services | OFC OF ACQUISITION AND GRANTS MGMT | 541512 — Computer Systems Design Services | WINDSOR MILL | MD | UNITED STATES | 2026-08-26 | 2023-09-29 | 2027-05-31 | HEALTHCARE INTEGRATED GENERAL LEDGER ACCOUNTING SYSTEM (HIGLAS) HOSTING, OPERATIONS & MAINTENANCE (HOM) | https://www.usaspending.gov/award/CONT_AWD_75FCMC23F0156_7530_47QTCK18D0003_4732 |
| ACCENTURE FEDERAL SERVICES LLC | C47BNA8GM833 | $202,121,105.74 | 75FCMC21F0001 | Department of Health and Human Services | Centers for Medicare and Medicaid Services | OFC OF ACQUISITION AND GRANTS MGMT | 541512 — Computer Systems Design Services | ARLINGTON | VA | UNITED STATES | 2026-08-26 | 2021-01-11 | 2022-07-15 | FEDERALLY FACILITATED MARKETPLACE (FFM) BRIDGE CONTRACT | https://www.usaspending.gov/award/CONT_AWD_75FCMC21F0001_7530_HHSM500201600003I_7530 |
| ALETHIX, LLC | F4EQF8UKA2K5 | $126,998,077.54 | 70SBUR21F00000121 | Department of Homeland Security | U.S. Citizenship and Immigration Services | USCIS CONTRACTING OFFICE(ERBUR) | 541512 — Computer Systems Design Services | FAIRFAX | VA | UNITED STATES | 2026-08-28 | 2021-07-19 | 2026-10-31 | SERVICES FOR PRODUCT ENGINEERING AND ENTERPRISE DELIVERY (SPEED) | https://www.usaspending.gov/award/CONT_AWD_70SBUR21F00000121_7003_75N98119D00009_7529 |
| SCIENCE APPLICATIONS INTERNATIONAL CORPORATION | MMLKPW9JLX64 | $110,881,128.98 | 70B04C24F00000184 | Department of Homeland Security | U.S. Customs and Border Protection | INFORMATION TECHNOLOGY CONTRACTING DIVISION | 541512 — Computer Systems Design Services | RESTON | VA | UNITED STATES | 2026-08-27 | 2024-03-02 | 2026-04-30 | IT SERVICE AND SUPPORT | https://www.usaspending.gov/award/CONT_AWD_70B04C24F00000184_7014_47QTCK18D0001_4732 |
| HIGHLIGHT TECHNOLOGIES, INC. | C2MSYQALD3E4 | $91,798,601.12 | 70SBUR21F00000124 | Department of Homeland Security | U.S. Citizenship and Immigration Services | USCIS CONTRACTING OFFICE(ERBUR) | 541512 — Computer Systems Design Services | FAIRFAX | VA | UNITED STATES | 2026-08-27 | 2021-07-19 | 2026-10-31 | SERVICES FOR PRODUCT ENGINEERING AND ENTERPRISE DELIVERY (SPEED) | https://www.usaspending.gov/award/CONT_AWD_70SBUR21F00000124_7003_75N98119D00020_7529 |
| CUSTOMER VALUE PARTNERS, LLC | L6R3M86AFBB5 | $88,387,635.95 | 70SBUR21F00000122 | Department of Homeland Security | U.S. Citizenship and Immigration Services | USCIS CONTRACTING OFFICE(ERBUR) | 541512 — Computer Systems Design Services | FAIRFAX | VA | UNITED STATES | 2026-08-27 | 2021-07-19 | 2026-10-31 | SERVICES FOR PRODUCT ENGINEERING AND ENTERPRISE DELIVERY (SPEED) | https://www.usaspending.gov/award/CONT_AWD_70SBUR21F00000122_7003_HHSN316201200125W_7529 |
| EKAGRA PARTNERS, LLC | Q1DVL2FMEYR4 | $75,623,014.54 | 70SBUR21F00000123 | Department of Homeland Security | U.S. Citizenship and Immigration Services | USCIS CONTRACTING OFFICE(ERBUR) | 541512 — Computer Systems Design Services | LEESBURG | VA | UNITED STATES | 2026-08-28 | 2021-07-19 | 2026-10-31 | SERVICES FOR PRODUCT ENGINEERING AND ENTERPRISE DELIVERY (SPEED) | https://www.usaspending.gov/award/CONT_AWD_70SBUR21F00000123_7003_HHSN316201200131W_7529 |
| ACCENTURE FEDERAL SERVICES LLC | C47BNA8GM833 | $63,236,191.56 | 70CTD021FR0000232 | Department of Homeland Security | U.S. Immigration and Customs Enforcement | INFORMATION TECHNOLOGY DIVISION | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-25 | 2021-09-28 | 2027-02-27 | CYBER DEFENSE AND INTELLIGENCE SUPPORT (CDISS) TASK ORDER. 11 MONTH BASE PERIOD AND 4 OPTION YEARS. | https://www.usaspending.gov/award/CONT_AWD_70CTD021FR0000232_7012_HHSN316201200002W_7529 |
| PATRIOT LLC | LYMKSJG6DLQ5 | $45,392,124.77 | 70B04C20F00001438 | Department of Homeland Security | U.S. Customs and Border Protection | INFORMATION TECHNOLOGY CONTRACTING DIVISION | 541512 — Computer Systems Design Services | LORTON | NE | UNITED STATES | 2026-08-25 | 2020-09-29 | 2026-06-15 | PROCUREMENT OF PROGRAM MANAGEMENT, CUSTOMER-FOCUSED TECHNOLOGY SERVICE DESK SUPPORT FOR TIER 1 INTERNAL AND EXTERNAL OPERATIONS, AUTOMATED COMMERCIAL ENVIRONMENT (ACE) ACCOUNT SERVICE DESK (ASD), AND… | https://www.usaspending.gov/award/CONT_AWD_70B04C20F00001438_7014_HHSN316201200065W_7529 |
| ALPHA OMEGA INTEGRATION LLC | NF34JCA2PME3 | $44,147,081.47 | 70CTD020FR0000280 | Department of Homeland Security | U.S. Immigration and Customs Enforcement | INFORMATION TECHNOLOGY DIVISION | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-28 | 2020-09-29 | 2026-03-31 | ICE REQUIRES INFORMATION TECHNOLOGY PROGRAM MANAGEMENT SUPPORT (ITPMS) SERVICES TO SUPPORT THE DEPARTMENT OF HOMELAND SECURITY, IMMIGRATION AND CUSTOMS ENFORCEMENT (ICE), HOMELAND SECURITY INVESTIGATI… | https://www.usaspending.gov/award/CONT_AWD_70CTD020FR0000280_7012_HHSN316201200182W_7529 |
| ANDURIL INDUSTRIES, INC. | KC3CH2MSK7Q3 | $41,852,694.56 | 70B02C25F00000422 | Department of Homeland Security | U.S. Customs and Border Protection | AIR AND MARINE CONTRACTING DIVISION | 541512 — Computer Systems Design Services | COSTA MESA | CA | UNITED STATES | 2026-08-25 | 2025-08-01 | 2027-06-30 | S1 APPROVED AWARD FOR DELIVERY ORDER 18 | https://www.usaspending.gov/award/CONT_AWD_70B02C25F00000422_7014_70B02C20D00000019_7014 |
| DELOITTE CONSULTING LLP | CKV2L9GZKJK3 | $28,578,126.83 | 75N98023F00004 | Department of Health and Human Services | National Institutes of Health | NATIONAL INSTITUTES OF HEALTH OLAO | 541512 — Computer Systems Design Services | ALEXANDRIA | VA | UNITED STATES | 2026-08-25 | 2023-09-15 | 2027-09-14 | DELOITTE CONSULTING LLP:1167543 [23-003351] | https://www.usaspending.gov/award/CONT_AWD_75N98023F00004_7529_HHSN316201200018W_7529 |
| INTERNATIONAL BUSINESS MACHINES CORPORATION | VV9KH3L99VE3 | $27,584,513.80 | 70SBUR25F00000032 | Department of Homeland Security | U.S. Citizenship and Immigration Services | USCIS CONTRACTING OFFICE(ERBUR) | 541512 — Computer Systems Design Services | WILLISTON | VT | UNITED STATES | 2026-08-24 | 2025-08-08 | 2027-03-01 | AWARD, ARCHITECTURE ENGINEERING SUPPORT (AES) SERVICES, USCIS ENTERPRISE INFRASTRUCTURE DIVISION. EXCLUSION 2(D). CONTRACTOR SUPPORT TO DESIGN AND MAINTAIN THE AGENCY'S NETWORKS, SUPPORTING ITS DATA C… | https://www.usaspending.gov/award/CONT_AWD_70SBUR25F00000032_7003_47QTCK18D0014_4732 |
| COMPUTER WORLD SERVICES, CORP. | SELVLQN46MM7 | $22,284,500.54 | 70RDA124FR0000045 | Department of Homeland Security | Office of Procurement Operations | DEPARTMENTAL OPERATIONS ACQUISITIONS DIVISION I | 541512 — Computer Systems Design Services | FALLS CHURCH | VA | UNITED STATES | 2026-08-24 | 2024-09-17 | 2028-09-16 | SYSTEMS ENGINEERING AND TEST SUPPORT (SETS) RECOMPETE | https://www.usaspending.gov/award/CONT_AWD_70RDA124FR0000045_7001_HHSN316201300001W_7529 |
| A1M SOLUTIONS, INC. | ZPGUVM99QXX7 | $21,975,811.53 | 75FCMC24F0170 | Department of Health and Human Services | Centers for Medicare and Medicaid Services | OFC OF ACQUISITION AND GRANTS MGMT | 541512 — Computer Systems Design Services | CHICO | CA | UNITED STATES | 2026-08-27 | 2024-09-09 | 2026-11-06 | DSG HAS MADE IMPROVEMENTS IN PORTFOLIO MANAGEMENT, ENSURING COHESION AND TRACEABILITY. THERE IS AN OPPORTUNITY FOR THE DATA SYSTEMS GROUP (DSG) TO BUILD ON THIS PROGRESS AND ENTER ITS NEXT PHASE OF TR… | https://www.usaspending.gov/award/CONT_AWD_75FCMC24F0170_7530_47QTCA21D006V_4732 |
| GOLDMAN EDWARDS - TANTUS TECHNOLOGIES, LLC | NKRBEEFHXN47 | $18,934,145.78 | 75FCMC26F0065 | Department of Health and Human Services | Centers for Medicare and Medicaid Services | OFC OF ACQUISITION AND GRANTS MGMT | 541512 — Computer Systems Design Services | WINDSOR MILL | MD | UNITED STATES | 2026-08-26 | 2026-04-23 | 2027-04-22 | THE CENTERS FOR MEDICARE & MEDICAID SERVICES (CMS) CENTER FOR CLINICAL STANDARDS AND QUALITY (CCSQ) REQUIRES COMPREHENSIVE SECURITY, INNOVATION, AND OPERATIONS (SIO) SUPPORT TO ADVANCE ITS CRITICAL MO… | https://www.usaspending.gov/award/CONT_AWD_75FCMC26F0065_7530_47QTCA23D003V_4732 |
| OASYS INTERNATIONAL LLC | FJX9CNNLEM21 | $17,872,179.47 | 70Z03825FM0000025 | Department of Homeland Security | U.S. Coast Guard | AVIATION LOGISTICS CENTER (ALC)(00038) | 541512 — Computer Systems Design Services | ELIZABETH CITY | NC | UNITED STATES | 2026-08-26 | 2025-09-18 | 2026-07-17 | PROFESSIONAL INFORMATION TECHNOLOGY SERVICES TO SUPPORT THE AVIATION LOGISTICS CENTER AND INFORMATION SYSTEMS DIVISION. | https://www.usaspending.gov/award/CONT_AWD_70Z03825FM0000025_7008_47QTCH18D0006_4732 |
| INCENTIVE TECHNOLOGY GROUP LLC | CGTWKQ7DSVD7 | $13,277,942.82 | 75P00119F80217 | Department of Health and Human Services | Office of the Assistant Secretary for Administration | PROGRAM SUPPORT CENTER ACQ MGMT SVC | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-25 | 2019-09-30 | 2024-10-11 | INNOVATE  MODERNIZE AND IMPROVE THE HHS FINANCIAL MANAGEMENT ENVIRONMENT | https://www.usaspending.gov/award/CONT_AWD_75P00119F80217_7570_HHSN316201200134W_7529 |
| RELI GROUP INC | ZZEFBLYZN5B1 | $12,859,897.10 | 75FCMC25FJ070 | Department of Health and Human Services | Centers for Medicare and Medicaid Services | OFC OF ACQUISITION AND GRANTS MGMT | 541512 — Computer Systems Design Services | CATONSVILLE | MD | UNITED STATES | 2026-08-26 | 2025-06-30 | 2026-11-29 | NATIONAL PLAN AND PROVIDER ENUMERATION SYSTEM (NPPES) OPERATIONS & MAINTENANCE (O&M). THE GOVERNMENT IS ISSUING A SOLE SOURCE FOLLOW ON UNDER THE STRATEGIC PARTNERS ACQUISITION READINESS CONTRACT (SPA… | https://www.usaspending.gov/award/CONT_AWD_75FCMC25FJ070_7530_HHSM500201700045I_7530 |
| FU ASSOCIATES, LTD. | WA2ND8JX9KQ5 | $12,545,471.16 | 75FCMC23F0145 | Department of Health and Human Services | Centers for Medicare and Medicaid Services | OFC OF ACQUISITION AND GRANTS MGMT | 541512 — Computer Systems Design Services | ARLINGTON | VA | UNITED STATES | 2026-08-27 | 2023-09-13 | 2027-09-12 | THE PURPOSE OF THIS TASK ORDER IS TO REFINE, TEST, IMPLEMENT, AND MAINTAIN THE MCIM SUITE AND RELATED SPECIAL PROJECTS.  THE CONTRACTOR SHALL PROVIDE THE NECESSARY AND ESSENTIAL DEVELOPMENT, OPERATION… | https://www.usaspending.gov/award/CONT_AWD_75FCMC23F0145_7530_GS35F257GA_4732 |
| CANDOR SOLUTIONS LLC | JSL9E59CT6J9 | $10,689,367.15 | 70RTAC23FR0000002 | Department of Homeland Security | Office of Procurement Operations | INFO TECH ACQ CENTER | 541512 — Computer Systems Design Services | UPPER MARLBORO | MD | UNITED STATES | 2026-08-28 | 2023-04-28 | 2027-04-27 | THE PURPOSE OF THIS TASK ORDER IS TO ACQUIRE ASSET MANAGEMENT SUPPORT SERVICES FOR THE DEPARTMENT OF HOMELAND SECURITY (DHS), OFFICE OF THE CHIEF INFORMATION OFFICER (OCIO), INFORMATION TECHNOLOGY OPE… | https://www.usaspending.gov/award/CONT_AWD_70RTAC23FR0000002_7001_HHSN316201200110W_7529 |
| ANDURIL INDUSTRIES, INC. | KC3CH2MSK7Q3 | $9,023,087.16 | 70B02C26F00000661 | Department of Homeland Security | U.S. Customs and Border Protection | AIR AND MARINE CONTRACTING DIVISION | 541512 — Computer Systems Design Services | IRVINE | CA | UNITED STATES | 2026-08-25 | 2026-08-25 | 2027-08-24 | TOWER RELOCATIONS AND SOFTWARE INTEGRATION | https://www.usaspending.gov/award/CONT_AWD_70B02C26F00000661_7014_70B02C20D00000019_7014 |
| NEXTECH LINTECH LLC | E61WLJBALR66 | $8,786,838.88 | 70RTAC24FR0000028 | Department of Homeland Security | Office of Procurement Operations | INFO TECH ACQ CENTER | 541512 — Computer Systems Design Services | SPRINGFIELD | VA | UNITED STATES | 2026-08-26 | 2024-03-06 | 2027-03-10 | THE PURPOSE OF THIS REQUIREMENT IS TO PROCURE HSIN EXTERNAL FACING TIER I, II, AND OPERATIONS SUPPORT. | https://www.usaspending.gov/award/CONT_AWD_70RTAC24FR0000028_7001_47QTCB22D0218_4732 |
| SIKICH FEDERAL INC. | HG5EUM78L3Y9 | $8,622,685.04 | 75N95023F00001 | Department of Health and Human Services | National Institutes of Health | NATIONAL INSTITUTES OF HEALTH NIDA | 541512 — Computer Systems Design Services | ROCKVILLE | MD | UNITED STATES | 2026-08-27 | 2023-08-28 | 2026-09-27 | PLANNING, DEVELOPMENT, AND MAINTENANCE OF A GRANTS AND CONTRACTS INITIATIVE TRACKING SYSTEM FOR THE NATIONAL INSTITUTE ON AGING (NIA) EXTRAMURAL RESEARCH PROGRAM (ERP). | https://www.usaspending.gov/award/CONT_AWD_75N95023F00001_7529_HHSN316201200177W_7529 |
| TRIPLE POINT SECURITY INC | XSJMFUNCEAA8 | $8,467,010.67 | 75N92023F00001 | Department of Health and Human Services | National Institutes of Health | NATIONAL INSTITUTES OF HEALTH NHLBI | 541512 — Computer Systems Design Services | LEESBURG | VA | UNITED STATES | 2026-08-28 | 2023-08-30 | 2026-08-29 | NHLBI ENTERPRISE ARCHITECTURE AND CYBER SECURITY SUPPORT FOR DATA SCIENCE PROGRAMS | https://www.usaspending.gov/award/CONT_AWD_75N92023F00001_7529_75N92023A00005_7529 |
| GLOBAL TECH INC. | HWMKR49GR573 | $7,137,804.64 | HSFE3015J0243 | Department of Homeland Security | Federal Emergency Management Agency | INFORMATION TECHNOLOGY COMMODITIES AND TELECOMMUNICATIONS | 541512 — Computer Systems Design Services | COLLEGE PARK | MD | UNITED STATES | 2026-08-25 | 2015-06-16 | 2016-12-15 | IGF::CT::IGF SYSTEMS ENGINEERING AND TECHNICAL ASSISTANCE: ISSO SUPPORT | https://www.usaspending.gov/award/CONT_AWD_HSFE3015J0243_7022_HSFEHQ10D0390_7022 |
| KARTHIK CONSULTING LLC | FGNNM7KNUPF6 | $6,687,926.99 | 70FA3122F00000068 | Department of Homeland Security | Federal Emergency Management Agency | INFORMATION TECHNOLOGY DEVELOPMENT AND SUSTAINMENT | 541512 — Computer Systems Design Services | FALLS CHURCH | VA | UNITED STATES | 2026-08-27 | 2022-09-30 | 2025-11-16 | HELPDESK SERVICES TO SUPPORT THE GRANTS TECHNOLOGY DIVISION, GMM PROGRAM | https://www.usaspending.gov/award/CONT_AWD_70FA3122F00000068_7022_75N98119D00062_7529 |
| VETS2 SYNERGY LLC | L8KJCAW6D9D4 | $6,143,450.15 | 70CMSD25FR0000112 | Department of Homeland Security | U.S. Immigration and Customs Enforcement | INVESTIGATIONS AND OPERATIONS SUPPORT DALLAS | 541512 — Computer Systems Design Services | LORTON | VA | UNITED STATES | 2026-08-24 | 2025-09-15 | 2027-09-14 | THE PURPOSE OF THIS TASK ORDER IS TO PROVIDE GENERAL SUPPORT SYSTEM NETWORK SERVICES FOR US IMMIGRATION AND CUSTOMS ENFORCEMENT'S TECHNICAL OPERATIONS CENTER. | https://www.usaspending.gov/award/CONT_AWD_70CMSD25FR0000112_7012_47QTCH18D0068_4732 |
| A SQUARE GROUP LLC | K22WGLWY6ZK6 | $5,836,400.39 | 75D30124F19860 | Department of Health and Human Services | Centers for Disease Control and Prevention | CDC OFFICE OF ACQUISITION SERVICES | 541512 — Computer Systems Design Services | FREDERICK | MD | UNITED STATES | 2026-08-24 | 2024-08-22 | 2026-08-22 | OCIO CPIC EA AND DATA POLICY SUPPORT SERVICES | https://www.usaspending.gov/award/CONT_AWD_75D30124F19860_7523_75N98120D00007_7529 |
| DELOITTE CONSULTING LLP | CKV2L9GZKJK3 | $5,589,950.25 | 75D30123F16141 | Department of Health and Human Services | Centers for Disease Control and Prevention | CDC OFFICE OF ACQUISITION SERVICES | 541512 — Computer Systems Design Services | ARLINGTON | VA | UNITED STATES | 2026-08-24 | 2023-04-17 | 2025-02-14 | APEX OPERATIONS AND MAINTENANCE SUPPORT SERVICES | https://www.usaspending.gov/award/CONT_AWD_75D30123F16141_7523_HHSN316201200018W_7529 |
| BELLESE TECHNOLOGIES, LLC | HXBBEPUC48F5 | $5,437,307.80 | 75FCMC26F0143 | Department of Health and Human Services | Centers for Medicare and Medicaid Services | OFC OF ACQUISITION AND GRANTS MGMT | 541512 — Computer Systems Design Services | OWINGS MILLS | MD | UNITED STATES | 2026-08-25 | 2026-09-08 | 2027-09-07 | THE PURPOSE OF THIS MEDICARE COVERAGE TOOLS (MCT) 3.0 CONTRACT IS TO ENHANCE MEDICARE INFORMATION CHANNELS TO PROVIDE A MORE INTEGRATED, PERSONALIZED AND SEAMLESS CUSTOMER SERVICE EXPERIENCE. | https://www.usaspending.gov/award/CONT_AWD_75FCMC26F0143_7530_GS35F356DA_4732 |
| DAS FEDERAL LLC | MCLKHED4JJX5 | $5,017,528.74 | 75F40125F80229 | Department of Health and Human Services | Office of the Assistant Secretary for Financial Resources | OMAS STRATEGIC BUYING CENTER - INFORMATION TECHNOLOGY | 541512 — Computer Systems Design Services | SILVER SPRING | MD | UNITED STATES | 2026-08-25 | 2025-09-24 | 2027-09-28 | FDA TRACK SUPPORT AND SERVICES | https://www.usaspending.gov/award/CONT_AWD_75F40125F80229_7524_47QTCB22D0238_4732 |
| DYNAMIC GOVERNMENT RESOURCES LLC | XUFTMCL9RF78 | $4,999,329.05 | 70B06C26F00000816 | Department of Homeland Security | U.S. Customs and Border Protection | MISSION SUPPORT CONTRACTING DIVISION | 541512 — Computer Systems Design Services | LEESBURG | VA | UNITED STATES | 2026-08-28 | 2026-09-01 | 2027-08-31 | ACE BUSINESS ANALYST SUPPORT | https://www.usaspending.gov/award/CONT_AWD_70B06C26F00000816_7014_47QTCC26DV008_4732 |
| SEKON ENTERPRISE, LLC | NUSGPXRUVS54 | $4,692,973.60 | 75N92022F00001 | Department of Health and Human Services | National Institutes of Health | NATIONAL INSTITUTES OF HEALTH NHLBI | 541512 — Computer Systems Design Services | BETHESDA | MD | UNITED STATES | 2026-08-27 | 2022-09-01 | 2027-08-31 | NHLBI CONTENT MANAGEMENT | https://www.usaspending.gov/award/CONT_AWD_75N92022F00001_7529_HHSN316201200170W_7529 |
| ATTAINX INC. | J6Z9VBSL4219 | $4,656,263.92 | 70FA5024F00000041 | Department of Homeland Security | Federal Emergency Management Agency | NATIONAL CONTINUITY SECTION(CON50) | 541512 — Computer Systems Design Services | HERNDON | VA | UNITED STATES | 2026-08-28 | 2024-04-03 | 2027-04-11 | AWARD A TASK ORDER FOR CBRNRESPONDER NETWORK SUPOORT | https://www.usaspending.gov/award/CONT_AWD_70FA5024F00000041_7022_47QTCB21D0128_4732 |
| CANDOR SOLUTIONS LLC | JSL9E59CT6J9 | $4,222,014.06 | 75N98026F00001 | Department of Health and Human Services | National Institutes of Health | NATIONAL INSTITUTES OF HEALTH OLAO | 541512 — Computer Systems Design Services | ROCKVILLE | MD | UNITED STATES | 2026-08-26 | 2026-07-23 | 2027-06-22 | NIDA APPLICATION DEVELOPMENT AND INFORMATION TECHNOLOGY SERVICES (SADITS) | https://www.usaspending.gov/award/CONT_AWD_75N98026F00001_7529_HHSN316201200110W_7529 |
| RELI GROUP INC | ZZEFBLYZN5B1 | $3,957,776.39 | 75N98126F00001 | Department of Health and Human Services | National Institutes of Health | NIH NITAA DITA-DVI OF INFO TECH ACQ | 541512 — Computer Systems Design Services | CATONSVILLE | MD | UNITED STATES | 2026-08-27 | 2026-02-15 | 2027-02-14 | INFORMATION TECHNOLOGY CYBERSECURITY PROGRAM SUPPORT SERVICES (ITCPSS) | https://www.usaspending.gov/award/CONT_AWD_75N98126F00001_7529_75N98119D00027_7529 |
| AQUILENT, INC. | LKBNKN1EA6J1 | $3,554,895.93 | HHSP23337046 | Department of Health and Human Services | Office of the Assistant Secretary for Administration | PROGRAM SUPPORT CENTER ACQ MGMT SVC | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-27 | 2015-08-20 | 2017-08-25 | IGF::CT::IGF | https://www.usaspending.gov/award/CONT_AWD_HHSP23337046_7555_HHSP233201300057B_7555 |
| UNIQNET S3, LLC | QSREUPJ3Q6Z5 | $3,208,567.68 | 75N93025F00252 | Department of Health and Human Services | National Institutes of Health | NATIONAL INSTITUTES OF HEALTH NIAID | 541512 — Computer Systems Design Services | BETHESDA | MD | UNITED STATES | 2026-08-27 | 2025-09-30 | 2027-09-29 | COLLECTION OF ALTERNATIVE METHODS FOR REGULATORY APPLICATION (CAMERA) DATABASE AND WEB APPLICATION DEVELOPMENT AND SUPPORT, BASE YEAR, PERIOD OF PERFORMANCE 09/30/2025-09/28/2026 | https://www.usaspending.gov/award/CONT_AWD_75N93025F00252_7529_47QTCB22D0415_4732 |
| AUDACIOUS INQUIRY LLC | R1XUKGWGLBD7 | $3,003,152.85 | 75P00119F80100 | Department of Health and Human Services | Office of the Assistant Secretary for Administration | PROGRAM SUPPORT CENTER ACQ MGMT SVC | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-25 | 2019-05-31 | 2024-05-31 | ONC TRACKING PLATFORM | https://www.usaspending.gov/award/CONT_AWD_75P00119F80100_7570_HHSM500201700010I_7530 |
| STRATEGIC OPERATIONAL SOLUTIONS INC | FCJYHNPMDK55 | $2,972,832.46 | 70FA3123F00000052 | Department of Homeland Security | Federal Emergency Management Agency | INFORMATION TECHNOLOGY DEVELOPMENT AND SUSTAINMENT | 541512 — Computer Systems Design Services | DENTON | TX | UNITED STATES | 2026-08-24 | 2023-07-12 | 2026-01-12 | FUSION CENTER SUPPORT | https://www.usaspending.gov/award/CONT_AWD_70FA3123F00000052_7022_47QTCH18D0059_4732 |
| AUDACIOUS INQUIRY LLC | R1XUKGWGLBD7 | $2,733,285.18 | 75P00119F80208 | Department of Health and Human Services | Office of the Assistant Secretary for Administration | PROGRAM SUPPORT CENTER ACQ MGMT SVC | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-27 | 2019-09-30 | 2020-09-29 | IZGATEWAY | https://www.usaspending.gov/award/CONT_AWD_75P00119F80208_7570_HHSM500201700010I_7530 |
| WILLIAMS CONSULTING LLC | CLDPGB3AAN49 | $2,698,782.49 | 75P00125F80152 | Department of Health and Human Services | Office of the Assistant Secretary for Financial Resources | OMAS STRATEGIC BUYING CENTER - HHS MISSION | 541512 — Computer Systems Design Services | CATONSVILLE | MD | UNITED STATES | 2026-08-27 | 2025-09-30 | 2026-09-29 | THE NATIONAL BREASTFEEDING HELPLINE | https://www.usaspending.gov/award/CONT_AWD_75P00125F80152_7570_GS35F227DA_4732 |
| VIM ASSOCIATES INC | RLQHCAUZFQY3 | $2,204,627.72 | 75D30124C19054 | Department of Health and Human Services | Centers for Disease Control and Prevention | CDC OFFICE OF ACQUISITION SERVICES | 541512 — Computer Systems Design Services | SAN ANTONIO | TX | UNITED STATES | 2026-08-28 | 2024-09-20 | 2027-08-31 | NATIONAL ALS REGISTRY WEB PORTAL SUPPORT | https://www.usaspending.gov/award/CONT_AWD_75D30124C19054_7523_-NONE-_-NONE- |
| ACCENTURE FEDERAL SERVICES LLC | C47BNA8GM833 | $2,141,352.84 | 70T03026F7667N065 | Department of Homeland Security | Transportation Security Administration | ENTERPRISE INFORMATION TECHNOLOGY | 541512 — Computer Systems Design Services | ARLINGTON | VA | UNITED STATES | 2026-08-27 | 2026-09-11 | 2027-09-10 | IVS CALL ORDER FOR 12 MONTHS FROM BPA 70T03024A7667N004. | https://www.usaspending.gov/award/CONT_AWD_70T03026F7667N065_7013_70T03024A7667N004_7013 |
| ONEZERO SOLUTIONS, LLC | SL7JJ6EZN3Y3 | $1,524,284.56 | 70Z02322FBSX20002 | Department of Homeland Security | U.S. Coast Guard | HQ CONTRACT OPERATIONS (CG-912)(000 | 541512 — Computer Systems Design Services | HERNDON | VA | UNITED STATES | 2026-08-28 | 2022-09-28 | 2027-03-27 | BARD (BOATING ACCIDENT REPORT DATABASE) SERVICES 8(A) STARS III GWAC CONTRACT: 47QTCB22D0065 / TO: 70Z02322FBSX20002 PERIOD OF PERFORMANCE: 28 SEP 2022 - 27 SEP 2027 | https://www.usaspending.gov/award/CONT_AWD_70Z02322FBSX20002_7008_47QTCB22D0065_4732 |
| METAPHASE CONSULTING LLC | ZH8ACM4ZWDL7 | $1,424,729.33 | 70CMSW26FR0000004 | Department of Homeland Security | U.S. Immigration and Customs Enforcement | MISSION SUPPORT WASHINGTON | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-28 | 2026-01-28 | 2027-01-27 | THE PURPOSE OF THIS AWARD IS TO OBTAIN DATA MANAGEMENT PROFESSIONAL SUPPORT SERVICES FOR THE IMMIGRATION AND CUSTOMS ENFORCEMENT'S FINANCIAL DATA MODERNIZATION PROGRAM. | https://www.usaspending.gov/award/CONT_AWD_70CMSW26FR0000004_7012_47QTCB22D0095_4732 |
| HIGHPOINT DIGITAL, INC. | NLXHVL2Z2967 | $1,384,981.96 | 7571MN26F80085 | Department of Health and Human Services | Office of the Assistant Secretary for Financial Resources | OMAS STRATEGIC BUYING CENTER - HHS MISSION | 541512 — Computer Systems Design Services | INDIANAPOLIS | IN | UNITED STATES | 2026-08-27 | 2026-08-27 | 2027-08-26 | FEDHEALTH IT SOFTWARE LICENSING, OPERATION, AND MAINTENANCE SERVICES FOR FOH | https://www.usaspending.gov/award/CONT_AWD_7571MN26F80085_7571_GS35F533GA_4732 |
| CLEARAVENUE LLC | TZJXKXNHDLX1 | $1,289,159.07 | 70FA3124F00000049 | Department of Homeland Security | Federal Emergency Management Agency | INFORMATION TECHNOLOGY DEVELOPMENT AND SUSTAINMENT | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-24 | 2024-07-23 | 2025-07-22 | FY24 - EMIS SUSTAINMENT AND DEVELOPMENT PR# WX04719Y2024T PERIOD OF PERFORMANCE (POP): BASE YEAR, PLUS TWO (2) 12-MONTH OPTION PERIODS. BASE YEAR: 07/1/2024 - 06/31/2025 OY1:07/1/2025-06/31/2026 OY2:0… | https://www.usaspending.gov/award/CONT_AWD_70FA3124F00000049_7022_75N98120D00191_7529 |
| THE CENTECH GROUP INC. | GB4LSAFPM513 | $1,090,407.03 | 75P00123F80048 | Department of Health and Human Services | Office of the Assistant Secretary for Financial Resources | OMAS STRATEGIC BUYING CENTER - HHS MISSION | 541512 — Computer Systems Design Services | CHANTILLY | VA | UNITED STATES | 2026-08-26 | 2023-03-02 | 2027-02-01 | THE SECURITY MANAGER (SM) APPLICATION IS AN ENTERPRISE SOLUTION THAT SUPPORTS THE ONS DPS AND HHS STAKEHOLDERS. ONS VIA SOFTWARE LICENSES FROM THE INCUMBENT CONTRACTOR, CENTECH, HAS BEEN PROVIDING MAI… | https://www.usaspending.gov/award/CONT_AWD_75P00123F80048_7570_47QTCA18D00GB_4732 |
| TCG INC | DRUNBSXBERD5 | $1,056,679.55 | 75N90022F00001 | Department of Health and Human Services | National Institutes of Health | NATIONAL INSTITUTES OF HEALTH - CC | 541512 — Computer Systems Design Services | BETHESDA | MD | UNITED STATES | 2026-08-25 | 2022-08-25 | 2027-08-31 | BIOSTATISTICIAN SUPPORT SERVICES TCG, INC.:1108529 [22-009001] | https://www.usaspending.gov/award/CONT_AWD_75N90022F00001_7529_HHSN316201200178W_7529 |
| AQUILENT, INC. | LKBNKN1EA6J1 | $1,000,931.14 | HHSP23337050 | Department of Health and Human Services | Office of the Assistant Secretary for Administration | PROGRAM SUPPORT CENTER ACQ MGMT SVC | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-26 | 2015-08-27 | 2016-08-26 | IGF::CT::IGF | https://www.usaspending.gov/award/CONT_AWD_HHSP23337050_7555_HHSP233201300057B_7555 |
| ASCLEPIUS SOLUTIONS INC | LKVVZXZFRHM6 | $974,395.00 | 75N91021F00243 | Department of Health and Human Services | National Institutes of Health | NIH NCI | 541512 — Computer Systems Design Services | KENSINGTON | MD | UNITED STATES | 2026-08-24 | 2021-09-01 | 2022-06-30 | PROJECT MANAGEMENT AND APPLICATION SUPPORT SERVICES FOR DATA MANAGEMENT SYSTEMS MANAGED BY THE NCI OFFICE OF INFORMATION TECHNOLOGY (OIT) | https://www.usaspending.gov/award/CONT_AWD_75N91021F00243_7529_GS06F1077Z_4732 |
| STRATEGIC OPERATIONAL SOLUTIONS INC | FCJYHNPMDK55 | $967,383.50 | 70CTD026FR0000014 | Department of Homeland Security | U.S. Immigration and Customs Enforcement | INFORMATION TECHNOLOGY DIVISION | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-26 | 2026-04-01 | 2027-03-29 | THIS TASK ORDER PROVIDES OPERATIONS & MAINTENANCE SUPPORT SERVICES HOMELAND SECURITY INVESTIGATIONS, COUNTER THREAT LEAD DEVELOPMENT FOR IT SUPPORT TO MAINTAIN THE LEADTRAC APPLICATION AND BUSINESS PR… | https://www.usaspending.gov/award/CONT_AWD_70CTD026FR0000014_7012_75N98119D00004_7529 |
| SAGACITY VENTURES LLC | H1S1ULWVRYK8 | $959,247.88 | 75F40123F80217 | Department of Health and Human Services | Food and Drug Administration | FDA OFFICE OF ACQ  GRANT SVCS | 541512 — Computer Systems Design Services | ALEXANDRIA | VA | UNITED STATES | 2026-08-24 | 2023-07-26 | 2024-09-26 | BIMO PROGRAM STRATEGIC SUPPORT | https://www.usaspending.gov/award/CONT_AWD_75F40123F80217_7524_47QTCB21D0429_4732 |
| HLN CONSULTING, LLC | XNSKEB3136G3 | $946,767.34 | 75D30124F20085 | Department of Health and Human Services | Centers for Disease Control and Prevention | CDC OFFICE OF ACQUISITION SERVICES | 541512 — Computer Systems Design Services | PROVIDENCE | RI | UNITED STATES | 2026-08-25 | 2024-09-17 | 2027-06-30 | RHODE ISLAND KIDSNET OPERATIONS AND MAINTENANCE (O&M) AND SUPPORT SERVICES | https://www.usaspending.gov/award/CONT_AWD_75D30124F20085_7523_47QTCA22D002B_4732 |
| DV UNITED LLC | HCBJCK2G9EM1 | $621,590.31 | 70FA3124F00000078 | Department of Homeland Security | Federal Emergency Management Agency | INFORMATION TECHNOLOGY DEVELOPMENT AND SUSTAINMENT | 541512 — Computer Systems Design Services | WASHINGTON | DC | UNITED STATES | 2026-08-24 | 2024-09-30 | 2025-09-29 | ENTERPRISE ARCHITECTURE TECHNOLOGY INNOVATION PROFESSIONAL SERVICES (EATIPS) | https://www.usaspending.gov/award/CONT_AWD_70FA3124F00000078_7022_HHSN316201200060W_7529 |
| TRIPLE POINT SECURITY INC | XSJMFUNCEAA8 | $595,830.84 | 75N98026F00318 | Department of Health and Human Services | National Institutes of Health | NATIONAL INSTITUTES OF HEALTH OLAO | 541512 — Computer Systems Design Services | BETHESDA | MD | UNITED STATES | 2026-08-28 | 2026-09-01 | 2027-08-31 | NHGRI IT CLOUD SUPPORT SERVICES | https://www.usaspending.gov/award/CONT_AWD_75N98026F00318_7529_47QTCA19D004D_4732 |
| INTEGRATED SECURITY TECHNOLOGIES INC. | SKN4AVY6ZJ53 | $508,496.31 | 70FA5024F00000149 | Department of Homeland Security | Federal Emergency Management Agency | NATIONAL CONTINUITY SECTION(CON50) | 541512 — Computer Systems Design Services | WAIPAHU | HI | UNITED STATES | 2026-08-25 | 2024-09-04 | 2027-09-03 | FOC AND ORR COOP AV MAINTENANCE AGREEMENT | https://www.usaspending.gov/award/CONT_AWD_70FA5024F00000149_7022_47QTCB22D0446_4732 |
| COLOSSAL CONTRACTING LLC | F4M9NB1HD785 | $426,726.10 | 70FA5025F00000018 | Department of Homeland Security | Federal Emergency Management Agency | NATIONAL CONTINUITY SECTION(CON50) | 541512 — Computer Systems Design Services | ANNAPOLIS | MD | UNITED STATES | 2026-08-24 | 2025-01-07 | 2027-01-09 | PROCURE AN EMERGENCY CONFERENCING AND ALERTING NOTIFICATION SYSTEM SOFTWARE PACKAGE | https://www.usaspending.gov/award/CONT_AWD_70FA5025F00000018_7022_75N98118D00006_7529 |

CSV columns match this field list exactly, plus `generated_unique_award_id` for join-back. UTF-8. Header row. One file: `usaspending-541512-dod-hhs-dhs-2026-08-31.csv` (Monday drop date).

### Section 4 — Source and method (every week, same text)

- Pulled from public USAspending.gov APIs / bulk Award files. No login. No FOIA. No non-public feeds.
- Filters: NAICS 541512; awarding toptier DoD, HHS, DHS; prime contracts; amount ≥ $250,000; action_date in the prior 7 days.
- USAspending is the system of record. Rows can lag, correct, or duplicate across weeks if USAspending restates. This Note does not de-duplicate across prior weeks unless the same PIID + action_date already shipped last Monday (then skip).
- Not a substitute for SAM.gov, FPDS, or a paid GovWin/BGOV seat. It is the $250k+ NAICS 541512 slice for three agencies, once a week.

### What the buyer does **not** get

- Hospital MRF, CMS HPT, shoppable-service extracts, or anything from hospital-price-series as a paid SKU.
- PHI, HIPAA datasets, SajaBirth / midwifery CRM.
- Subawards, grants, NAICS other than 541512, agencies other than DoD/HHS/DHS.
- Custom pulls, email alerts, Slack posts, or GitHub issue fulfillment.
- A live Ko-fi listing. Live Ko-fi 621b4c7e76 stays OpenFEMA and is out of scope.

---

## Pay CTA (muonarc.com Notes — HITL / not live)

This product is sold as a **Note on muonarc.com Notes**, not on GitHub, not on Ko-fi, not on GitHub Marketplace, and not via an issue form.

**HITL placeholder path (not live — Atlas places the Note later):** `muonarc.com/notes/usaspending-weekly-naics-541512` — do not treat this path as published.

**CTA copy (paste onto the muonarc.com Note when Atlas publishes):**

> Get this week's USAspending NAICS 541512 prime-award pack — DoD, HHS, and DHS, ≥$250k, prior 7 days — as a muonarc.com Note plus CSV.
>
> **This week:** $8–$20 for Monday's Note + CSV.
> **Retain:** $12–$40 / month for four consecutive Monday packs.
>
> Pay on muonarc.com Notes. You get the Markdown/HTML brief and the week's CSV. Same product next Monday. Public USAspending data only. AI-built (Rogue); human-reviewed before it went live.

Until Atlas publishes, there is **no** live pay link, **no** GitHub Sponsors/Marketplace button, and **no** Ko-fi swap. Do not invent a checkout URL.

---

## HITL close

- File: `drafts/notes-first-usa-spending-2026-08-30.md`
- Candidate 1 only. Candidates 2–3 untouched. Candidates file not rewritten.
- Not published. Not listed. Not emailed. Not merged to Muonarc/muonarc.com.
- Atlas STOP still holds: no $40 hospital MRF-change extract, no GitHub paid storefront, no extract-request outreach.
- Always-disclose-AI on any live Note.

AI-drafted by Rogue. Benjamin / Atlas reviews before any Note goes live.
