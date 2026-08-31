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

**Week label (example, not a live issue):** Week of 2026-08-24 → drop Monday 2026-08-31. Window: action_date 2026-08-24 through 2026-08-30.

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

One short block at the top:

- Window dates (start–end, ET).
- Row count (n primes).
- Sum of awarded amounts this window.
- Count and sum split by awarding toptier (DoD / HHS / DHS).
- Largest single prime (awardee + amount + PIID).
- Source pull timestamp and USAspending API/bulk vintage.

No commentary beyond those facts. No "hot take." No BD advice.

### Section 2 — Agency totals table

| Awarding agency | n primes | sum awarded | largest awardee | largest amount |
| --- | --- | --- | --- | --- |
| Department of Defense | … | … | … | … |
| Department of Health and Human Services | … | … | … | … |
| Department of Homeland Security | … | … | … | … |
| **Total** | … | … | — | — |

### Section 3 — Prime awards table (the week's rows)

One row per prime that passed the filters. Sorted by awarded amount descending, then PIID.

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

CSV columns match this field list exactly, plus `generated_unique_award_id` for join-back. UTF-8. Header row. One file: `usaspending-541512-dod-hhs-dhs-YYYY-MM-DD.csv` where the date is the Monday drop date.

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
