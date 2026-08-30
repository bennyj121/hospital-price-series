NONE

Open Data Stack Exchange (opendata.stackexchange.com) hunt 2026-08-30 (America/Phoenix, ~3:45 AM PT / 10:45 UTC). Window 2026-08-16 through 2026-08-30 inclusive (fromdate=1786838400 todate=1788134400 UTC).

Target: ONE live unanswered human question (real person asking for help parsing/automating CMS HPT / cms-hpt.txt / hospital MRF / chargemaster / shoppable / standardcharges files). Not a promo, not our own post. Unanswered = no accepted answer, preferably zero answers. Must be readable without an SE account.

Did not post, comment, log in, or register an SE account. Did not fold this NONE into drafts/HITL-2026-08-29.md (pack stays parent b33155ba). Did not ship Action 022. Did not stack. Live Ko-fi 621b4c7e76 left as-is OpenFEMA custom public-data pull $40 / 2 slots. offer.html HEAD HTTP 200 (https://bennyj121.github.io/hospital-price-series/offer.html). Did not hunt closed package-registry, HPT CI social, Dev.to+Hashnode, CV+DS SE, stalled SO, Reddit r/datasets, DIP, OpenFEMA, NHC, cold email, Open Source SE, HN, Kaggle, SourceHut/Gitea/Gitee, Marketplace 4–8 retarget, CREATE Ko-fi, listing UI, Action 022.

Queries (public Stack Exchange API 2.3, no auth; also public HTML search pages)
- GET /2.3/search/advanced?site=opendata&fromdate=1786838400&todate=1788134400&sort=creation&order=desc&pagesize=100&filter=withbody
  Full window census: 3 questions, has_more=false. Keyword scan of title+tags+body: hospital | price.?transpar | cms-hpt | chargemaster | machine-readable | \bmrf\b | shoppable | standardcharges | standard.charges | negotiated.rate | cms.gov | hpt → 0 hits.
- GET /2.3/search/advanced?site=opendata&fromdate=1786838400&todate=1788134400&answers=0&sort=creation&order=desc
  q= hospital price transparency → items=[]
- Same window (sort=creation) q= cms-hpt | chargemaster | shoppable | standardcharges | hospital MRF | machine-readable file | cms-hpt.txt | hospital chargemaster | standard charges | hospital | CMS | MRF → all items=[]
- GET /2.3/search?site=opendata&intitle=hospital (no date) → older medical/hospital threads only (IT spend, COVID boundaries, respiratory cases, MIMIC, US hospital lists). All created 2016–2023; none are CMS HPT / cms-hpt.txt / hospital MRF / chargemaster / shoppable / standardcharges file parsing.
- All-time (no date) advanced search:
  q=hospital price transparency → items=[]
  q=cms-hpt → items=[]
  q=chargemaster → 1 item, Q3487 (created 1407346575 ≅ 2014-08-06) "Any dataset containing the price/charge that patients actually pay for their health care service?" — answered/accepted; pre-HPT-rule; not a live 14-day CMS HPT / cms-hpt.txt / hospital MRF file question.
  q=shoppable → unrelated stemming hits (online user behavior Q23178 2026-06-16, tech hubs, Costco plates). None are CMS shoppable-services files. Out of window.
- Public HTML (no login):
  https://opendata.stackexchange.com/search?q=hospital+price+transparency+is%3Aquestion+created%3A2026-08-16..2026-08-30 → HTTP 200, "0 results"
  https://opendata.stackexchange.com/search?q=cms-hpt+created%3A2026-08-16..2026-08-30 → HTTP 200, "0 results"
  https://opendata.stackexchange.com/search?q=chargemaster+created%3A2026-08-16..2026-08-30 → HTTP 200, "0 results"
  https://opendata.stackexchange.com/search?q=shoppable+created%3A2026-08-16..2026-08-30 → HTTP 200, "0 results"
  https://opendata.stackexchange.com/questions?tab=Newest → HTTP 403 (bot wall); census taken from API + opened question URLs below.

Opened / dated (in-window census; none qualified)
- https://opendata.stackexchange.com/questions/23204 (creation 1787305628 ≅ 2026-08-21) "Recovering audio lecture recordings from Wayback Machine" — tags data-request/audio/archive.org; accepted answer 23205; Latin lecture mp3s, not HPT.
- https://opendata.stackexchange.com/questions/23203 (creation 1787266826 ≅ 2026-08-20) "Dataset of finger/stylus-written digits" — tags data-request/language/ocr/writing; answers=0; OCR digits, not hospital price files.
- https://opendata.stackexchange.com/questions/23200 (creation 1787121082 ≅ 2026-08-19) "Dataset of handwritten vertical arithmetic, with answers" — tags ocr/mathematics; answers=0; kids' arithmetic images, not HPT.

No qualifying live unanswered human HPT/MRF parse/automate question on Open Data SE in 2026-08-16..2026-08-30. Did not draft a HITL answer. Did not post. Did not fold into HITL pack.
