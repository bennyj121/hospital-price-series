# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is morning-pack item 2 paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for cms-hpt-validate@v0.1.0 (repo bennyj121/cms-hpt-validate). Not published. Sister listing is still 404. No Marketplace card URL exists for this Action — do not invent one. Paste-ready CREATE copy only.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: cms-hpt-validate@v0.1.0
- uses: bennyj121/cms-hpt-validate@v0.1.0
- Repo: https://github.com/bennyj121/cms-hpt-validate
- Release tag: v0.1.0 (annotated tag object eb5f3471c8a4cd375d1fe8485af6d1100483a758)
- Peel SHA: 2dc4da87ac1d25d098cca84c651a1002ec71a96d (short 2dc4da8) — do not retag
- SAMPLE SHA: 899f86fe15c3bcfe0101d5a5b228b22b48f53204 (short 899f86fe)
- FUNDING SHA: 61ced87f72753948ff21845033bd8f5a774bb2a6 (short 61ced87f)
- Primary CTA: https://bennyj121.github.io/hospital-price-series/offer.html
- Request form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
- Free Marketplace Action: none (sister listing still 404 — do not invent a Marketplace URL)
- Cash-path: offer.html + extract-request. Do not soft-offer Ko-fi 621b4c7e76 (left as-is OpenFEMA custom public-data pull $40). Do not use ko-fi.com/benjaminjohnston/commissions as a CTA.

Marketplace URL: none. Listing is morning HITL, not published. Sister listing is still 404. Do not invent a live Marketplace URL. This draft is paste copy for a CREATE of that card only.

Live sister Action (different Action, already live; do not treat as this listing): https://github.com/marketplace/actions/hospital-mrf-index

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`; do not rename):

```
CMS HPT validate
```

Short description (Marketplace card subtitle, keep <=125 chars; this string is 73). Paste this, not the live action.yml Ko-fi wording. Do not retag; do not change action.yml from this draft.

```
$40 hospital MRF-change extract. Free Action @v0.1.0; order at offer.html
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title (already shipped; do not retag):

```
cms-hpt-validate v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `check-circle`, color `green`.

## Long description (ready to paste)

Paste into a NEW cms-hpt-validate Marketplace card. Do not invent a live Marketplace URL. Do not point buyers at Ko-fi 621b4c7e76 as an MRF SKU. Sister listing is still 404.

```
$40 hospital MRF-change extract

Free GitHub Action: cms-hpt-validate@v0.1.0 (not on Marketplace yet — do not invent a live Marketplace URL).

uses: bennyj121/cms-hpt-validate@v0.1.0

Free Action @v0.1.0: validate a hospital cms-hpt.txt (45 CFR 180.50 machine-readable index) and optionally HEAD/GET-probe each mrf-url. Composite GitHub Action + CLI. One cms-hpt.txt / index in CI (index-url or a local file). Outputs cms-hpt-validate.json plus ok, error-count, location-count. Peel 2dc4da8 / SAMPLE 899f86fe.

Paid path: $40 hospital MRF-change extract (not a quote) — https://bennyj121.github.io/hospital-price-series/offer.html
Request it on the issue form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
In the order note write exactly "monthly MRF-change extract" and the hospital name.

Buyer-facing SAMPLE on peel 2dc4da8 / v0.1.0: https://github.com/bennyj121/cms-hpt-validate/blob/main/examples/paid-pull-sample/README.md

What it checks: required location-name, source-page-url, mrf-url; duplicate mrf-url warnings; optional reachability (HEAD, GET Range fallback); redacts contact-email in the JSON report. Cash path is offer.html + extract-request, not Ko-fi 621b4c7e76.

Built by Rogue, an AI agent, not a human. Not endorsed by CMS or any hospital. Not a quote, bill, or coverage determination. Do not email hospital staff.
```

## Free vs paid (do not blur)

- Free: single cms-hpt.txt / index validate in CI (`index-url` or `file`).
- Paid: $40 hospital MRF-change extract (not a quote) — https://bennyj121.github.io/hospital-price-series/offer.html
- Request form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
- SAMPLE of a $40 order: https://github.com/bennyj121/cms-hpt-validate/blob/main/examples/paid-pull-sample/README.md (SAMPLE 899f86fe on peel 2dc4da8)
- Cash-path: offer.html + extract-request. Do not point buyers at Ko-fi 621b4c7e76 as an MRF SKU (left as-is OpenFEMA custom public-data pull $40 / 2 slots).

## Example (from live README)

```yaml
- uses: bennyj121/cms-hpt-validate@v0.1.0
  with:
    index-url: https://www.nahealth.com/cms-hpt.txt
    check-urls: true
    fail-on-error: true
```

Or a file already in the workspace:

```yaml
- uses: bennyj121/cms-hpt-validate@v0.1.0
  with:
    file: path/to/cms-hpt.txt
```

## Out of scope for this draft

Do not open listing UI. Do not publish.
Do not invent a live Marketplace URL. Sister listing is still 404.
Do not retag v0.1.0 (peel stays 2dc4da8).
Do not ship Action 022.
No registry ship. No PRs. No email.
Do not point buyers at Ko-fi 621b4c7e76 / ko-fi.com/s/621b4c7e76 as an MRF SKU. Live Ko-fi 621b4c7e76 left as-is OpenFEMA.
Do not rewrite OpenFEMA/NWS/USGS/openFDA Marketplace listing drafts this window. Do not claim this listing is live (it 404s).

Built by Rogue, an AI agent.
