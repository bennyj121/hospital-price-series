# HITL DRAFT ONLY — not published

Status: human-in-the-loop draft for Atlas. Do not publish to muonarc.com. Do not list, merge, or ship. Checkout URL below is a placeholder and is **not live**. This is candidate #2 only (Friday COT Pack). Not the $40 hospital MRF-change extract. Not a GitHub, Ko-fi, or Marketplace storefront.

AI-prepared brief (Rogue + helper bots). Benjamin/Atlas reviews before any Note goes live.

---

# Friday COT Pack — 12 liquid futures (CFTC public)

**As-of Tuesday 2026-08-25 · CFTC released Friday 2026-08-28 3:30pm ET · Legacy Futures-Only COT**

## Pitch

Every Friday after the CFTC 3:30pm ET Commitments of Traders release, regenerate a one-pager template (net spec / commercial / non-reportable; 1-week and 4-week change; 52-week percentile) for a fixed 12-contract set (CL, NG, GC, SI, ZC, ZS, ZW, ES, NQ, 6E, 6J, BTC) from CFTC public COT files only. Filled template + CSV; same product next Friday. Not a one-off zip; not freelancer-tools.

## Price band

**$12–$25 / Friday pack**, or **$20–$40 / month retain** (4 packs).

No GitHub paid listing. No Ko-fi storefront for this SKU. Live Ko-fi 621b4c7e76 stays OpenFEMA and is not this product.

## Delivery format (Friday pack)

Markdown/HTML Note (this one-pager) plus CSV of the 12-contract table (zip if more than one file). Same 12 names every Friday. Not a GitHub issue form.

**What the buyer gets each Friday**

1. This one-pager: net spec / net commercial / net non-reportable, 1-week change, 4-week change, 52-week percentile of net spec, open interest, and category long/short.
2. A CSV with one row per contract and the same fields (for desks that paste into a workbook).
3. Named CFTC market + contract-market code so the row can be audited against the public file.
4. As-of Tuesday date and Friday release date on the header.

## Pay (HITL / not live)

This Note would be sold on **muonarc.com Notes** (not GitHub, not Ko-fi as storefront, not Marketplace).

Placeholder checkout (not live, do not share as a URL that works): `muonarc.com/notes/friday-cot-pack` — HITL only.

---

## How this week is built

| Item | Value |
| --- | --- |
| Report | CFTC Legacy **Futures-Only** Commitments of Traders (non-commercial / commercial / non-reportable). Not the Disaggregated (PMAN / swap / managed-money) file. Matches candidate #2's "net spec / commercial / non-reportable" template. |
| As-of | Tuesday **2026-08-25** |
| Release | Friday **2026-08-28** (CFTC 3:30pm ET) |
| 1-week change | CFTC published week-over-week change columns (vs prior Tuesday 2026-08-18) |
| 4-week change | This week's net minus as-of **2026-07-28** net (four Tuesdays back) |
| 52-week percentile | Trailing **52** Tuesday as-of weeks **2025-09-02 through 2026-08-25**. Percent of those weeks where net spec ≤ this week's net spec. 100 = highest net spec in the window. |
| Sources (public, no login) | Current week: [deafut.txt](https://www.cftc.gov/dea/newcot/deafut.txt). History: [deacot2026.zip](https://www.cftc.gov/files/dea/history/deacot2026.zip), [deacot2025.zip](https://www.cftc.gov/files/dea/history/deacot2025.zip). Index: [Commitments of Traders](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm). |
| Units | Futures contracts (CFTC "All" columns). Spreading is reported separately and is **not** inside net spec. |

CFTC market names used for the 12 CME/NYMEX/COMEX/CBOT tickers (codes are stable; display names drift):

| Ticker | CFTC market name | Code |
| --- | --- | --- |
| CL | WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE | 067651 |
| NG | NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE | 023651 |
| GC | GOLD - COMMODITY EXCHANGE INC. | 088691 |
| SI | SILVER - COMMODITY EXCHANGE INC. | 084691 |
| ZC | CORN - CHICAGO BOARD OF TRADE | 002602 |
| ZS | SOYBEANS - CHICAGO BOARD OF TRADE | 005602 |
| ZW | WHEAT-SRW - CHICAGO BOARD OF TRADE | 001602 |
| ES | E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE | 13874A |
| NQ | NASDAQ MINI - CHICAGO MERCANTILE EXCHANGE | 209742 |
| 6E | EURO FX - CHICAGO MERCANTILE EXCHANGE | 099741 |
| 6J | JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE | 097741 |
| BTC | BITCOIN - CHICAGO MERCANTILE EXCHANGE | 133741 |

Not Micro Bitcoin, not Micro E-minis, not ICE WTI, not Henry Hub last-day financial.

**Definitions:** net spec = non-commercial long − short. Net commercial = commercial long − short. Net non-reportable = non-reportable long − short.

---

## One-pager: week of 2026-08-25

Headline: **corn specs at a 52-week high**; **gold specs still heavy long** and adding; **nat-gas specs still deep short** (9.6th percentile) even after a small cover; **euro specs still short** (11.5th) while covering; **E-mini S&P specs sold** on the week.

### Net spec / commercial / non-reportable (contracts)

| Ticker | OI | Δ OI 1w | Net spec | Δ 1w | Δ 4w | 52w %ile | Net comm | Δ 1w | Δ 4w | Net n.rpt | Δ 1w | Δ 4w | Traders |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| CL | 1,906,740 | +17,780 | +123,449 | +1,359 | +3,341 | 63.5 | −156,246 | −3,159 | +2,576 | +32,797 | +1,800 | −5,917 | 287 |
| NG | 1,747,730 | +20,352 | −197,932 | +5,571 | −7,133 | 9.6 | +187,737 | −589 | +8,073 | +10,195 | −4,982 | −940 | 319 |
| GC | 427,957 | +21,697 | +243,334 | +21,145 | +61,264 | 86.5 | −279,585 | −21,167 | −67,276 | +36,251 | +22 | +6,012 | 295 |
| SI | 113,801 | −6,316 | +25,261 | +1,636 | +3,044 | 53.8 | −45,053 | −261 | −6,244 | +19,792 | −1,375 | +3,200 | 162 |
| ZC | 1,707,706 | −20,297 | +440,915 | +138,773 | +186,595 | 100.0 | −374,608 | −129,008 | −170,677 | −66,307 | −9,765 | −15,918 | 869 |
| ZS | 972,531 | −17,198 | +221,427 | +30,466 | +9,670 | 82.7 | −199,936 | −30,299 | −7,729 | −21,491 | −167 | −1,941 | 627 |
| ZW | 443,531 | −13,617 | −6,779 | +11,986 | −4,787 | 94.2 | +7,475 | −8,906 | +3,016 | −696 | −3,080 | +1,771 | 408 |
| ES | 2,045,669 | −26,689 | −67,994 | −57,434 | −50,798 | 78.8 | −64,065 | +49,488 | +31,864 | +132,059 | +7,946 | +18,934 | 435 |
| NQ | 301,987 | +4,056 | +10,039 | +20,455 | +5,125 | 40.4 | −37,136 | −24,789 | −22,190 | +27,097 | +4,334 | +17,065 | 291 |
| 6E | 818,524 | +13,584 | −36,352 | +22,736 | +36,095 | 11.5 | +440 | −23,615 | −51,274 | +35,912 | +879 | +15,179 | 321 |
| 6J | 384,216 | +3,405 | −63,298 | −10,405 | +100,114 | 36.5 | +67,837 | +6,763 | −90,188 | −4,539 | +3,642 | −9,926 | 154 |
| BTC | 22,216 | +456 | +1,949 | −787 | −1,955 | 61.5 | −1,790 | +658 | +1,772 | −159 | +129 | +183 | 126 |

52w %ile is **net spec only**. Δ 1w / Δ 4w on net columns are contract changes in that net (not percent).

### Category longs / shorts (this Tuesday)

| Ticker | NC long | NC short | NC spread | Comm long | Comm short | N.rpt long | N.rpt short |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| CL | 323,243 | 199,794 | 616,707 | 892,144 | 1,048,390 | 74,646 | 41,849 |
| NG | 313,777 | 511,709 | 804,662 | 572,041 | 384,304 | 57,250 | 47,055 |
| GC | 277,159 | 33,825 | 33,620 | 62,453 | 342,038 | 54,725 | 18,474 |
| SI | 37,871 | 12,610 | 13,005 | 33,970 | 79,023 | 28,955 | 9,163 |
| ZC | 593,012 | 152,097 | 314,008 | 669,606 | 1,044,214 | 131,080 | 197,387 |
| ZS | 303,519 | 82,092 | 177,748 | 446,393 | 646,329 | 44,871 | 66,362 |
| ZW | 121,212 | 127,991 | 133,296 | 154,565 | 147,090 | 34,458 | 35,154 |
| ES | 241,495 | 309,489 | 40,332 | 1,493,154 | 1,557,219 | 270,688 | 138,629 |
| NQ | 88,632 | 78,593 | 5,771 | 156,048 | 193,184 | 51,536 | 24,439 |
| 6E | 198,919 | 235,271 | 39,356 | 493,442 | 493,002 | 86,807 | 50,895 |
| 6J | 128,340 | 191,638 | 24,270 | 197,062 | 129,225 | 34,544 | 39,083 |
| BTC | 16,582 | 14,633 | 4,133 | 380 | 2,170 | 1,121 | 1,280 |

### Percent of open interest (this Tuesday)

| Ticker | NC L % | NC S % | Comm L % | Comm S % | N.rpt L % | N.rpt S % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CL | 17.0 | 10.5 | 46.8 | 55.0 | 3.9 | 2.2 |
| NG | 18.0 | 29.3 | 32.7 | 22.0 | 3.3 | 2.7 |
| GC | 64.8 | 7.9 | 14.6 | 79.9 | 12.8 | 4.3 |
| SI | 33.3 | 11.1 | 29.9 | 69.4 | 25.4 | 8.1 |
| ZC | 34.7 | 8.9 | 39.2 | 61.1 | 7.7 | 11.6 |
| ZS | 31.2 | 8.4 | 45.9 | 66.5 | 4.6 | 6.8 |
| ZW | 27.3 | 28.9 | 34.8 | 33.2 | 7.8 | 7.9 |
| ES | 11.8 | 15.1 | 73.0 | 76.1 | 13.2 | 6.8 |
| NQ | 29.3 | 26.0 | 51.7 | 64.0 | 17.1 | 8.1 |
| 6E | 24.3 | 28.7 | 60.3 | 60.2 | 10.6 | 6.2 |
| 6J | 33.4 | 49.9 | 51.3 | 33.6 | 9.0 | 10.2 |
| BTC | 74.6 | 65.9 | 1.7 | 9.8 | 5.0 | 5.8 |

Spreading % of OI is omitted here; longs + shorts + spreading do not sum to 100 because spreading is counted on both sides of OI.

---

## Read-through (this Friday only; not advice)

- **ZC (corn):** net spec **+440,915**, 52-week percentile **100.0**, +138,773 on the week. Largest spec add in the pack. Commercials are the other side (−129,008 net on the week).
- **GC (gold):** net spec **+243,334** (86.5th percentile), +21,145 week / +61,264 four-week. Commercials remain heavily net short (−279,585).
- **NG (nat gas):** net spec **−197,932** (9.6th percentile). Specs covered +5,571 on the week but are still near the short end of the 52-week window. Commercials net long +187,737.
- **6E (euro):** net spec **−36,352** (11.5th percentile) but covering (+22,736 week / +36,095 four-week).
- **ES vs NQ:** ES specs **sold** (−57,434 week, net −67,994). NQ specs **bought** back to net long (+20,455 week, net +10,039) — 40.4th percentile, not stretched.
- **6J (yen):** still net spec short (−63,298) and a bit shorter on the week (−10,405), but the four-week change is a large cover (+100,114) from a deeper short.
- **BTC:** small net spec long (+1,949), trimmed on the week (−787). Thin vs the rest of the pack (OI 22,216; 126 traders).
- **CL / SI / ZS / ZW:** CL spec long modest and little changed (63.5th). SI mid-pack (53.8th). ZS spec long 82.7th and adding. ZW still a small spec short (−6,779) but 94.2nd percentile — the short is mild vs the last year of readings.

Not investment advice. Public positioning snapshot only.

---

## Sample CSV schema (same 12 rows every Friday)

Columns the Friday CSV would carry (this week's values are the tables above):

`as_of,release,ticker,cftc_name,cftc_code,oi,d_oi_1w,nc_long,nc_short,nc_spread,comm_long,comm_short,nr_long,nr_short,net_spec,net_comm,net_nr,d_net_spec_1w,d_net_comm_1w,d_net_nr_1w,d_net_spec_4w,d_net_comm_4w,d_net_nr_4w,net_spec_52w_percentile,traders,source`

Source field this week: `https://www.cftc.gov/dea/newcot/deafut.txt` plus the two annual history zips for the 4-week and 52-week columns.

---

## What this is / is not

- **Is:** a retainable Friday one-pager + CSV from **public CFTC COT** for a **fixed 12-contract** set.
- **Is not:** hospital MRF, hospital-price-series paid SKU, Kaiser/UCLA/HN extract, OpenFEMA, NHC, USAspending, NCUA, GitHub Marketplace Action, or Ko-fi 621b4c7e76.
- **Is not:** Disaggregated managed-money / producer-merchant tables. Those are a different CFTC file; this SKU is Legacy net spec / commercial / non-reportable as named in candidate #2.

---

*HITL draft. Not published. AI-prepared (Rogue + helper bots); Benjamin/Atlas review required before any muonarc.com Note goes live. Public CFTC data only. No PHI.*
