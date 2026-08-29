# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is HITL draft paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for openfema-pa-action@v0.1.0 (repo bennyj121/openfema-pa-action). Not published. No Marketplace card URL exists for this Action — do not invent one.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: openfema-pa-action@v0.1.0
- uses: bennyj121/openfema-pa-action@v0.1.0
- Repo: https://github.com/bennyj121/openfema-pa-action
- Release tag: v0.1.0 (annotated tag object 3ccc52509f19749e582de9910a4d55178422e38c)
- Peel SHA: 74987b1eaf35a16e4ee202c8de7111ed39153458 (short 74987b1) — do not retag
- SAMPLE SHA: 2e9cfb6174fe2b2ae5e87fb1ec77c3652cd88dd7 (short 2e9cfb6)
- FUNDING SHA: d9864291fcbcf9c175fdcdd05dfb01b1fd387421 (short d9864291)

Marketplace URL: none. Listing is morning HITL, not published. Do not invent a live Marketplace URL.

Sister published listing (different Action, already live): https://github.com/marketplace/actions/hospital-mrf-index — do not treat that as this listing.

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`):

```
OpenFEMA Public Assistance Projects
```

Short description (from live action.yml `description:`; Marketplace card subtitle, keep <=125 chars; this string is 124):

```
$12 analysis-ready OpenFEMA Public Assistance projects. Free Action: fetch PA worksheets, optional since-date change detect.
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title:

```
openfema-pa-action v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `cloud`, color `blue`.

## Long description (ready to paste)

```
Fetch OpenFEMA Public Assistance Funded Projects Details v2 (public JSON, no API key) and optionally count records whose lastObligationDate or lastRefresh is on or after a since-date. Composite GitHub Action. Live pulls are a recent-first slice (default cap 5,000 rows of ~848k). The full analysis-ready file is the paid SKU.

uses: bennyj121/openfema-pa-action@v0.1.0

Free path: fetch PA project worksheets in CI (live OpenFEMA API or a committed fixture). Optional disaster-number and state filters (AND-combined). Outputs count, change-count, newest-project, newest-date, federal-share-sum, source (live or fixture), report-path (writes openfema-pa-projects.json). Live endpoint: https://www.fema.gov/api/open/v2/PublicAssistanceFundedProjectsDetails

Paid path: $12 analysis-ready OpenFEMA Public Assistance funded projects SKU: https://ko-fi.com/s/6fbe55e6f2. Secondary: $40 Custom public-data pull (OpenFEMA or similar): https://ko-fi.com/benjaminjohnston/commissions (alias 621b4c7e76). Buyer-facing SAMPLE: https://github.com/bennyj121/openfema-pa-action/blob/main/examples/paid-pull-sample/README.md

What it does: paginated live fetch ($skip / $top, $count=true, $orderby=lastRefresh desc); optional since-date change detect; optional disaster-number and state filters; fixture fallback when FEMA.gov is unreachable from CI.

Built by Rogue, an AI agent, not a human. Not a FEMA or DHS product. The Federal Government or FEMA cannot vouch for the data or analyses derived from these data after the data have been retrieved from the Agency’s website(s).
```

## Free vs paid (do not blur)

- Free: fetch OpenFEMA Public Assistance Funded Projects Details v2 in CI (live API or `fixture`), optional `since-date` change detect, optional `disaster-number` and `state` filters. Recent-first cap (default 5,000 of ~848k).
- Primary paid: $12 PA SKU https://ko-fi.com/s/6fbe55e6f2 — analysis-ready OpenFEMA Public Assistance funded projects.
- Secondary paid: $40 Custom public-data pull, alias 621b4c7e76 = https://ko-fi.com/benjaminjohnston/commissions — OpenFEMA or similar extract.
- Secondary offer page: https://bennyj121.github.io/hospital-price-series/offer.html
- SAMPLE of a $12 order: https://github.com/bennyj121/openfema-pa-action/blob/main/examples/paid-pull-sample/README.md
- FUNDING SHA d9864291 custom CTAs: https://ko-fi.com/s/6fbe55e6f2 and https://ko-fi.com/benjaminjohnston/commissions

## Example (from live README)

```yaml
- uses: bennyj121/openfema-pa-action@v0.1.0
  with:
    since-date: '2026-08-01'   # optional YYYY-MM-DD change detect
    # disaster-number: '4834'  # optional
    # state: 'FL'               # optional
```

If the live API is unreachable, pass a committed OpenFEMA-shaped JSON fixture:

```yaml
- uses: bennyj121/openfema-pa-action@v0.1.0
  with:
    fixture: fixtures/sample.json
    since-date: '2026-08-01'
```

## Out of scope for this draft

Do not open listing UI. Do not publish.
Do not invent a live Marketplace URL.
Do not retag v0.1.0 (peel stays 74987b1).
Do not ship Action 022.
No registry ship. No PRs. No email.

Built by Rogue, an AI agent.
