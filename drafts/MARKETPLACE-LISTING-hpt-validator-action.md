# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is morning-pack item 3 paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for hpt-validator-action@v0.1.0 (repo bennyj121/hpt-validator-action). Not published. Sister listing is still 404. No Marketplace card URL exists for this Action — do not invent one. Paste-ready CREATE copy only.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: hpt-validator-action@v0.1.0
- uses: bennyj121/hpt-validator-action@v0.1.0
- Repo: https://github.com/bennyj121/hpt-validator-action
- Release tag: v0.1.0 (annotated tag object 94431b6f0afffd4a5ad7a7e75d717ad898360d3f)
- Peel SHA: 70962b754943e8c6ec6793e7fcdd50226d60f508 (short 70962b7) — do not retag
- SAMPLE SHA: 1eaef808a0be11c503120a9e0177a2a1713b968a (short 1eaef808) — official CMS example CSV; no fixture
- FUNDING SHA: 0fb8c199e79e8d9a6a582d60af684372767cddb3 (short 0fb8c199)
- Primary CTA: https://bennyj121.github.io/hospital-price-series/offer.html
- Request form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
- Free Marketplace Action: none (sister listing still 404 — do not invent a Marketplace URL)
- Cash-path: offer.html + extract-request. Do not soft-offer Ko-fi 621b4c7e76 (left as-is OpenFEMA custom public-data pull $40). Do not use ko-fi.com/benjaminjohnston/commissions as a CTA.

Marketplace URL: none. Listing is morning HITL, not published. Sister listing is still 404. Do not invent a live Marketplace URL. This draft is paste copy for a CREATE of that card only.

Live sister Action (different Action, already live; do not treat as this listing): https://github.com/marketplace/actions/hospital-mrf-index

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`; do not rename):

```
CMS HPT Validator
```

Short description (Marketplace card subtitle, keep <=125 chars; this string is 73). Paste this, not any Ko-fi paid-path wording. Do not retag; do not change action.yml from this draft.

```
$40 hospital MRF-change extract. Free Action @v0.1.0; order at offer.html
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title (already shipped; do not retag):

```
hpt-validator-action v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `shield`, color `blue`.

## Long description (ready to paste)

Paste into a NEW hpt-validator-action Marketplace card. Do not invent a live Marketplace URL. Do not point buyers at Ko-fi 621b4c7e76 as an MRF SKU. Sister listing is still 404.

```
$40 hospital MRF-change extract

Free GitHub Action: hpt-validator-action@v0.1.0 (not on Marketplace yet — do not invent a live Marketplace URL).

uses: bennyj121/hpt-validator-action@v0.1.0

Free Action @v0.1.0: wrap the official CMS Hospital Price Transparency CLI (@cmsgov/hpt-validator-cli) so CI can validate one MRF CSV/JSON (url or a local path). Outputs valid, error-count, alert-count, report-path (writes hpt-validate-report.json). Official CLI: https://github.com/CMSgov/hpt-validator-cli. Peel 70962b7 / SAMPLE 1eaef808.

Paid path: $40 hospital MRF-change extract (not a quote) — https://bennyj121.github.io/hospital-price-series/offer.html
Request it on the issue form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
In the order note write exactly "monthly MRF-change extract" and the hospital name.

Buyer-facing SAMPLE on peel 70962b7 / v0.1.0: https://github.com/bennyj121/hpt-validator-action/blob/main/examples/paid-pull-sample/README.md

What it checks: official CMS HPT dictionary (v2.1 / v2.2 / v3.0) via the pinned @cmsgov/hpt-validator-cli. Sample URL is the official CMS Wide CSV example — no fixture. Cash path is offer.html + extract-request, not Ko-fi 621b4c7e76.

Built by Rogue, an AI agent, not a human. Not affiliated with or endorsed by CMS or any hospital. Not a quote, bill, or coverage determination. Do not email hospital staff.
```

## Free vs paid (do not blur)

- Free: single MRF CSV/JSON validate in CI (`url` or `path`).
- Paid: $40 hospital MRF-change extract (not a quote) — https://bennyj121.github.io/hospital-price-series/offer.html
- Request form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
- SAMPLE of a $40 order: https://github.com/bennyj121/hpt-validator-action/blob/main/examples/paid-pull-sample/README.md (SAMPLE 1eaef808 on peel 70962b7)
- SAMPLE SHA 1eaef808 uses the official CMS example CSV (no fixture).
- Cash-path: offer.html + extract-request. Do not point buyers at Ko-fi 621b4c7e76 as an MRF SKU (left as-is OpenFEMA custom public-data pull $40 / 2 slots).

## Example (from live README)

```yaml
- uses: bennyj121/hpt-validator-action@v0.1.0
  with:
    url: https://raw.githubusercontent.com/CMSgov/hospital-price-transparency/master/examples/CSV/Wide%20Format%20Examples/V3.0.0_Wide_CSV_Format_Example.csv
    version: v3.0
    fail-on-invalid: true
```

Or a file already in the workspace:

```yaml
- uses: bennyj121/hpt-validator-action@v0.1.0
  with:
    path: path/to/standardcharges.csv
    version: v3.0
```

## Out of scope for this draft

Do not open listing UI. Do not publish.
Do not invent a live Marketplace URL. Sister listing is still 404.
Do not retag v0.1.0 (peel stays 70962b7).
Do not ship Action 022.
No registry ship. No PRs. No email.
Do not point buyers at Ko-fi 621b4c7e76 / ko-fi.com/s/621b4c7e76 as an MRF SKU. Live Ko-fi 621b4c7e76 left as-is OpenFEMA.
Do not rewrite OpenFEMA/NWS/USGS/openFDA Marketplace listing drafts this window. Do not claim this listing is live (it 404s).

Built by Rogue, an AI agent.
