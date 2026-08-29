# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is morning-pack item 4 paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for openfema-declarations-action@v0.1.0 (repo bennyj121/openfema-declarations-action). Not published. No Marketplace card URL exists for this Action — do not invent one.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: openfema-declarations-action@v0.1.0
- uses: bennyj121/openfema-declarations-action@v0.1.0
- Repo: https://github.com/bennyj121/openfema-declarations-action
- Release tag: v0.1.0 (annotated tag object bc87df67a01f88e6b8d052e0c658a0f8cf5ba30f)
- Peel SHA: 25b4c0c2234149a6d3b4995637852644ad267cf5 (short 25b4c0c) — do not retag
- SAMPLE SHA: dc13299d13e6758c614dbc8ced04f59cb518d2f6 (short dc13299)
- FUNDING SHA: 40b4b3e65d0e75d193d1d4192cba849538002c8d (short 40b4b3e)

Marketplace URL: none. Listing is morning HITL, not published. Do not invent a live Marketplace URL.

Sister published listing (different Action, already live): https://github.com/marketplace/actions/hospital-mrf-index — do not treat that as this listing.

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`):

```
OpenFEMA Disaster Declarations
```

Short description (from live action.yml `description:`; Marketplace card subtitle, keep <=125 chars; this string is 118):

```
$12 analysis-ready OpenFEMA disaster declarations. Free Action: fetch declarations, optional since-date change detect.
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title:

```
openfema-declarations-action v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `cloud`, color `blue`.

## Long description (ready to paste)

```
Fetch OpenFEMA Disaster Declarations Summaries v2 (public JSON, no API key) and optionally count records whose declarationDate or lastRefresh is on or after a since-date. Composite GitHub Action.

uses: bennyj121/openfema-declarations-action@v0.1.0

Free path: fetch declarations in CI (live OpenFEMA API or a committed fixture). Outputs count, change-count, newest-declaration, newest-date, source (live or fixture), report-path (writes openfema-declarations.json). Live endpoint: https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries

Paid path: $12 analysis-ready OpenFEMA disaster declarations SKU: https://ko-fi.com/s/ec52718a6b. Secondary: $40 Custom public-data pull (OpenFEMA or similar): https://ko-fi.com/benjaminjohnston/commissions (alias 621b4c7e76). Buyer-facing SAMPLE: https://github.com/bennyj121/openfema-declarations-action/blob/main/examples/paid-pull-sample/README.md

What it does: paginated live fetch ($skip / $top, $count=true); optional since-date change detect; fixture fallback when FEMA.gov is unreachable from CI.

Built by Rogue, an AI agent, not a human. Not a FEMA or DHS product. The Federal Government or FEMA cannot vouch for the data or analyses derived from these data after the data have been retrieved from the Agency’s website(s).
```

## Free vs paid (do not blur)

- Free: fetch OpenFEMA Disaster Declarations Summaries v2 in CI (live API or `fixture`), optional `since-date` change detect.
- Primary paid: $12 Declarations SKU https://ko-fi.com/s/ec52718a6b — analysis-ready OpenFEMA disaster declarations.
- Secondary paid: $40 Custom public-data pull, alias 621b4c7e76 = https://ko-fi.com/benjaminjohnston/commissions — OpenFEMA or similar extract.
- Secondary offer page: https://bennyj121.github.io/hospital-price-series/offer.html
- SAMPLE of a $40 order: https://github.com/bennyj121/openfema-declarations-action/blob/main/examples/paid-pull-sample/README.md
- FUNDING SHA 40b4b3e custom CTAs: https://ko-fi.com/s/ec52718a6b and https://ko-fi.com/benjaminjohnston/commissions

## Example (from live README)

```yaml
- uses: bennyj121/openfema-declarations-action@v0.1.0
  with:
    since-date: '2026-08-01'   # optional YYYY-MM-DD change detect
```

If the live API is unreachable, pass a committed OpenFEMA-shaped JSON fixture:

```yaml
- uses: bennyj121/openfema-declarations-action@v0.1.0
  with:
    fixture: fixtures/sample.json
    since-date: '2026-08-01'
```

## Out of scope for this draft

Do not open listing UI. Do not publish.
Do not invent a live Marketplace URL.
Do not retag v0.1.0 (peel stays 25b4c0c).
Do not ship Action 022.
No registry ship. No PRs. No email.

Built by Rogue, an AI agent.
