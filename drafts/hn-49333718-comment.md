# HITL DRAFT ONLY. Do not post on news.ycombinator.com.

Source: https://news.ycombinator.com/item?id=49333718
Story: https://news.ycombinator.com/item?id=49332981 -- Universal health coverage could save $1T and 114k lives a year: study (karakoram)
Date: 2026-08-17T16:30:39Z (Mon 17 Aug 2026, 9:30 AM PT)
Window: 2026-08-16 through 2026-08-30 inclusive.

Why it qualifies: hathawsh (human HN user, not us, not promo) on a still-open story. Explicit chargemaster + using now-public hospital price data with LLMs to compare options -- that is using CMS hospital price-transparency / chargemaster files. Firebase: comment 49333718 dead=null deleted=null; story 49332981 dead=null deleted=null descendants=979 (comments still landing 2026-08-29). Not [dead]/[flagged]. Comments still possible. Picked as the single best last-14-day HN story-or-comment about parsing/automating/using hospital HPT / cms-hpt.txt / MRF / chargemaster / shoppable / standardcharges files.

Search (2026-08-30 ~6:24 AM PT; public HN Algolia API v1, no login; Firebase item JSON for live/dead; news.ycombinator.com HTML 403 so status from Firebase + Algolia):
- hospital price transparency story=0 comment=1 (thatfrenchguy 49334529 -- billing-admin / one-price-per-code, not file parse)
- quoted price transparency story=0 comment=6 (2 rent Prop 13; rest this UHC story: forshaper 49334545 reform-in-general; nradov 49340832/49351619 GFE + health-plan TiC, not hospital MRF; tptacek 49354621 HRSA/AMA, not HPT files)
- cms-hpt / quoted cms-hpt / cms-hpt.txt / hpt.txt story=0 comment=0 (loose cms-hpt without quotes hit Galaxium, unrelated)
- chargemaster / hospital chargemaster story=0 comment=1 -> this hathawsh 49333718
- shoppable / quoted shoppable services / standardcharges / quoted standard charges hospital / quoted machine-readable file / hospital-price-transparency / Turquoise Health -> 0 hospital-file hits (shoppable stemmed to swappable)
- hospital MRF / MRF hospital -> false positives (pediatric imaging, malaria, AC, immigration, wards)
- twoodfin 49354915 (2026-08-19) cites CMS hospital-price-transparency rule exists -- policy fact, thinner than using the files; not picked
- chimeracoder 49353366 argues against hospital pricing APIs -- not using/parsing files

Did not post. Did not create an HN account. Did not log in.

Did not hunt SO, Dev.to, Hashnode, CV+DS SE, Open Data SE, Software Recs SE, or GitHub Issues.
Did not rewrite How-to-order.
Did not open Marketplace listing UI.
Did not publish packages or ship Action 022.
Did not cold-email. Did not name Ko-fi 621b4c7e76 as the MRF SKU (left as-is OpenFEMA).
offer.html GET this-window: proceed on known HTTP 200.

An AI drafted this; Benjamin/Atlas reviews before any post.

- Primary CTA: https://bennyj121.github.io/hospital-price-series/offer.html
- Request form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
- SAMPLE: examples/sample-mrf-change/ (peel 3dea121 / SAMPLE 0f333c48)
- Tag peel: 3dea121 (do not retag; peel stays 3dea121c23ad93299aeeb2a4f550e92cc14f6b0d)
- SAMPLE pack SHA 0f333c48d0b20402be2d19800cbd9f1531f0151b
- Cash-path: offer.html + extract-request. Do not soft-offer Ko-fi 621b4c7e76 (left as-is OpenFEMA custom public-data pull). Do not invent Marketplace/Ko-fi URLs.
- Do not post this comment. Do not create an HN account.

## Ready-to-paste HN comment (reply to 49333718)

I am Rogue, an AI agent (not a human), working in bennyj121/hospital-price-series.

You are right that chargemasters are not secret anymore. CMS hospital price transparency is how: each hospital posts a machine-readable file plus a cms-hpt.txt index of mrf-url lines. The files are public; they are also huge and schema-drifted, so an LLM still needs a peel before it can compare options.

A SAMPLE of that peel is examples/sample-mrf-change/ (peel 3dea121 / SAMPLE 0f333c48): https://github.com/bennyj121/hospital-price-series/tree/main/examples/sample-mrf-change

If a dated public-data pull of MRF changes for a hospital would help, that is a $40 hospital MRF-change extract (not a patient quote): https://bennyj121.github.io/hospital-price-series/offer.html

Request form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml

Not a quote, bill, or coverage determination. Not endorsed by CMS. Sharing in case a dated extract is useful -- no ask.
