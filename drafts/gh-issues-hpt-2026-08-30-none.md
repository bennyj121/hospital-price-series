NONE

GitHub ISSUES hunt 2026-08-30 (America/Phoenix, ~3:56 AM PT / 10:56 UTC). Window 2026-08-16 through 2026-08-30 inclusive. Search: GitHub Search API via `gh api` (`is:issue`, not Discussions, not PRs). No clone.

Target: ONE live unanswered human GitHub ISSUE (state open, a real person asking for help parsing/automating CMS HPT / cms-hpt.txt / hospital MRF / chargemaster / shoppable / standardcharges files). Not a promo, not our issue, not a bot dump. Unanswered = 0 comments preferred, or no useful reply.

Did not post, comment, star, or open issues. Did not fold this NONE into drafts/HITL-2026-08-29.md (pack stays parent b33155ba). Did not ship Action 022. Did not stack. Live Ko-fi 621b4c7e76 left as-is OpenFEMA custom public-data pull $40 / 2 slots. offer.html HEAD HTTP 200 (https://bennyj121.github.io/hospital-price-series/offer.html). Did not hunt Software Recs SE, Open Data SE, Cross Validated, Data Science SE, Dev.to, Hashnode, Stack Overflow, Reddit, GitHub Discussions, PRs, cold email, killed rails (r/datasets, DIP, OpenFEMA, NHC), Marketplace 4–8 retarget, CREATE Ko-fi, listing UI, Action 022, SourceHut/Gitea/Gitee.

Queries (`gh api` search/issues, created:>=2026-08-16 unless noted)
- cms-hpt.txt is:issue is:open → total 2: only bennyj121/hospital-price-series #1 Kaiser and #2 UCLA (github-actions[bot] mrf-change dumps). Skip already-drafted.
- cms-hpt is:issue is:open → same 2 bot issues.
- hpt.txt is:issue is:open → same 2 bot issues.
- "cms-hpt" is:issue (any state) → same 2 bot issues.
- "hospital price transparency" parse OR parsing OR automate is:issue is:open → total 0
- "hospital price transparency" is:issue is:open → total 0
- "hospital price transparency" is:issue (any state) → total 0
- chargemaster MRF OR "machine-readable" is:issue is:open → total 0
- chargemaster is:issue is:open → total 0
- chargemaster is:issue (any state) → 1: medprice-ai/mcp-medprice-ai #39 (closed; MCP SDK migrate; not HPT parse). False positive.
- chargemaster in:title is:issue → total 0
- "hospital chargemaster" is:issue → same #39 false positive.
- shoppable standardcharges hospital is:issue is:open → total 0
- shoppable hospital is:issue is:open → 6 unrelated (recipe baskets, TikTok shoppable, Adobe sample page). Not CMS shoppable-services files.
- shoppable is:issue is:open → same unrelated set.
- standardcharges is:issue is:open → total 0
- standardcharges is:issue (any state) → total 0
- standardcharges hospital is:issue is:open → total 0
- "cms hospital price" json OR csv parse is:issue is:open → total 0
- "cms hospital price" is:issue is:open → total 0
- "hospital price" is:issue is:open → 6: our #1/#2 plus unrelated (careguard agent buttons, Paraguay briefing, Noida real estate). No human HPT parse ask.
- hospital MRF parse OR parsing OR parser OR automate is:issue is:open → 4: our #1/#2, ChelseaKR/mrf-honest #28 (skip already-drafted), dharmesh2002/neo-cortex #91 stock-screener bot. None qualify as a new human parse ask.
- "hospital MRF" OR "hospital mrf" is:issue is:open → only our #1/#2.
- "machine-readable" hospital is:issue is:open → 14 false positives (EHR/interoperability/deck validators; not CMS HPT MRF).
- "machine readable file" OR hospital-mrf OR hospital-price is:issue is:open → noisy 427 (unquoted hospital-price); only HPT-adjacent hits were our #1/#2 and mrf-honest #28.
- "price transparency" is:issue is:open → 42; first page all non-CMS (hotel/tutor/POS/HBOT Pune/watches). in:title "price transparency" → 3: databayt/mkan #52 hotel dialog, solo-ist/prose #849 co-op pricing page, manmohanml1/consensus #84 fee transparency. None are CMS HPT files.
- "gross charge" OR "discounted cash" OR standardcharges.json OR standardcharges.csv is:issue is:open → noisy; only HPT hit mrf-honest #28 (skip).
- "standard charges" is:issue is:open → 18 unrelated (gym IAP, AWS KMS, chemistry charges). No CMS standardcharges files.
- "payer-specific" OR estimated_amount OR negotiated_dollar OR "code|1|type" is:issue is:open → noisy; only HPT hit mrf-honest #28 (skip).
- "standard_charge" is:issue is:open → only mrf-honest #28 (skip).
- transparency.cms.gov is:issue is:open → total 0
- "shoppable services" is:issue is:open → total 0
- hpt-validator is:issue is:open → total 0
- mrf-parser hospital is:issue is:open → total 0
- hospital-mrf-index OR cms-hpt-validate is:issue is:open → total 0
- mrf-honest OR hospital-mrf-index OR cms-hpt-validate OR "hospital-chargemaster" OR "price-transparency-guide" is:issue is:open → only mrf-honest #28 (skip).
- hospital-price-transparency is:issue (any state) → 13 hyphen-token noise (Pune builders, German portal, job-room bots). No CMS HPT issue.
- in:title HPT hospital is:issue → total 0
- cms-hpt.txt is:issue created:2026-08-16..2026-08-30 → same 2 bot issues (when run).

Repo-scoped
- repo:CMSgov/hospital-price-transparency is:issue created:>=2026-08-16 → 0. is:issue is:open (no date) → 0. GET issues/219 → HTTP 404 (not an issue; skip already-drafted discussions/issues #219).
- repo:CMSgov/price-transparency-guide created:>=2026-08-16 → 0
- repo:CMSgov/price-transparency-guide-validator created:>=2026-08-16 → 0
- org:CMSgov is:issue is:open created:>=2026-08-16 hospital OR hpt OR mrf OR chargemaster OR transparency → 0
- repo:ChelseaKR/mrf-honest is:issue created:>=2026-08-16 → #28 open (skip already-drafted), #26 closed maintainer bug (not a human parse-help ask). GET issues/42 → open PR "fix: a charged row still owes a description and a setting (#28)" (skip already-drafted; PRs out of scope).
- repo:bennyj121/hospital-price-series is:issue created:>=2026-08-16 → #1 Kaiser and #2 UCLA, both github-actions[bot] (skip already-drafted; not human help-asks).
- repo:vsoch/hospital-chargemaster created:>=2026-08-16 → 0
- repo:nathansutton/hospital-price-transparency created:>=2026-08-16 → 0
- repo:onefact/hospitalprice / dolthub/hospital-price-transparency-v3 / ariadnelabs/hospital-price-transparency / TurquoiseHealth/os-data → search 422 (repo missing or private); no in-window issue recovered.

Opened / dated (in-window; none qualified as a new human parse/automate ask)
- https://github.com/bennyj121/hospital-price-series/issues/1 created 2026-08-28 — bot mrf-change Kaiser. Skip already-drafted.
- https://github.com/bennyj121/hospital-price-series/issues/2 created 2026-08-28 — bot mrf-change UCLA. Skip already-drafted.
- https://github.com/ChelseaKR/mrf-honest/issues/28 created 2026-08-23 — maintainer CSV-inspector bug. Skip already-drafted.
- https://github.com/ChelseaKR/mrf-honest/issues/26 created 2026-08-22 — closed; maintainer narrate bug, not a parse-help ask.
- https://github.com/ChelseaKR/mrf-honest/pull/42 created 2026-08-28 — PR (not an issue). Skip already-drafted.
- https://github.com/CMSgov/hospital-price-transparency/issues/219 — HTTP 404. Skip already-drafted.
- False positives opened enough to reject: databayt/mkan#52, medprice-ai/mcp-medprice-ai#39, skerishKang/ai-revenue-lab#753, NolanFoster/seasoned-app#495, solo-ist/prose#849, manmohanml1/consensus#84.

No qualifying live unanswered human GitHub ISSUE about parsing/automating CMS HPT / cms-hpt.txt / hospital MRF / chargemaster / shoppable / standardcharges files in 2026-08-16..2026-08-30. Remaining HPT-adjacent hits were already-drafted threads or our own bot dumps. Did not draft a HITL comment. Did not post. Did not fold into HITL pack.
