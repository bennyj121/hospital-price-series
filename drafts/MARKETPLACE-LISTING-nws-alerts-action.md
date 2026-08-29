# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is HITL draft paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for nws-alerts-action@v0.1.0 (repo bennyj121/nws-alerts-action). Not published. No Marketplace card URL exists for this Action — do not invent one.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: nws-alerts-action@v0.1.0
- uses: bennyj121/nws-alerts-action@v0.1.0
- Repo: https://github.com/bennyj121/nws-alerts-action
- Release tag: v0.1.0 (annotated tag object 271cf1b8b0fcf5c820baabecbbaf771ae5a37140)
- Peel SHA: cc3ee4baeab6d8abc684d258cfc21d3b224f47cc (short cc3ee4b) — do not retag
- SAMPLE SHA: 364ab85b5ff3f73870b3fa66baf26e7075c234c8 (short 364ab85)
- FUNDING SHA: 7972f4480a55b108157f05ee682770b8a26aac0c (short 7972f44)

Marketplace URL: none. Listing is morning HITL, not published. Do not invent a live Marketplace URL.

Sister published listing (different Action, already live): https://github.com/marketplace/actions/hospital-mrf-index — do not treat that as this listing.

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`):

```
NWS Active Alerts
```

Short description (from live action.yml `description:`; Marketplace card subtitle, keep <=125 chars; this string is 90):

```
$40 custom public-data pull. Free Action: fetch NWS active alerts, optional change-detect.
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title:

```
nws-alerts-action v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `cloud`, color `blue`.

## Long description (ready to paste)

```
Fetch official NWS active alerts from api.weather.gov (public GeoJSON, no API key) with optional area / status / event filters and optional since change-detect on sent, effective, or onset. Composite GitHub Action. Live pulls are capped (default 200, max 500). Official api.weather.gov only — this Action does not scrape weather.gov HTML.

uses: bennyj121/nws-alerts-action@v0.1.0

Free path: fetch NWS active alerts in CI (live api.weather.gov or a committed GeoJSON fixture). Optional area (2-letter state or marine), status, and event filters. Optional since change-detect. Outputs count, change-count, newest-alert, newest-sent, newest-effective, source (live or fixture), report-path (writes nws-alerts.json). Live endpoint: https://api.weather.gov/alerts/active

Paid path: $40 Custom public-data pull (NWS alerts extract or similar): https://ko-fi.com/benjaminjohnston/commissions (alias 621b4c7e76). In the order note write exactly "NWS alerts extract" and the area (e.g. AZ) or event filter wanted. Buyer-facing SAMPLE: https://github.com/bennyj121/nws-alerts-action/blob/main/examples/paid-pull-sample/README.md

What it does: live fetch of official NWS active-alert GeoJSON (User-Agent required by NWS); optional area / status / event filters; optional since change-detect on sent, effective, or onset; hard cap on live alerts (default 200, max 500); fixture fallback when api.weather.gov is unreachable from CI.

Built by Rogue, an AI agent, not a human. Not an NWS or NOAA product. NWS and NOAA do not endorse this Action.
```

## Free vs paid (do not blur)

- Free: fetch official NWS active alerts in CI (live api.weather.gov or `fixture`), optional `area` / `status` / `event` filters, optional `since` change-detect. Live cap default 200, max 500.
- Paid: $40 Custom public-data pull, alias 621b4c7e76 = https://ko-fi.com/benjaminjohnston/commissions — NWS alerts extract (or similar public-data pull).
- Secondary offer page: https://bennyj121.github.io/hospital-price-series/offer.html
- SAMPLE of a $40 order: https://github.com/bennyj121/nws-alerts-action/blob/main/examples/paid-pull-sample/README.md
- FUNDING SHA 7972f44 custom CTA: https://ko-fi.com/benjaminjohnston/commissions

## Example (from live README)

```yaml
- uses: bennyj121/nws-alerts-action@v0.1.0
  with:
    area: 'AZ'                 # optional 2-letter state
    # status: 'actual'         # optional
    # event: 'Excessive Heat Warning'
    since: '2026-08-01'        # optional YYYY-MM-DD or ISO change-detect
```

If the live API is unreachable, pass a committed NWS-shaped GeoJSON fixture:

```yaml
- uses: bennyj121/nws-alerts-action@v0.1.0
  with:
    fixture: fixtures/sample.json
    since: '2026-08-01'
```

## Out of scope for this draft

Do not open listing UI. Do not publish.
Do not invent a live Marketplace URL.
Do not retag v0.1.0 (peel stays cc3ee4b).
Do not ship Action 022.
No registry ship. No PRs. No email.

Built by Rogue, an AI agent.
