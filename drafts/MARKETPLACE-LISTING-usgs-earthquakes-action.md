# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is HITL draft paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for usgs-earthquakes-action@v0.1.0 (repo bennyj121/usgs-earthquakes-action). Not published. No Marketplace card URL exists for this Action — do not invent one.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: usgs-earthquakes-action@v0.1.0
- uses: bennyj121/usgs-earthquakes-action@v0.1.0
- Repo: https://github.com/bennyj121/usgs-earthquakes-action
- Release tag: v0.1.0 (annotated tag object d62708c8100d70017452808cf1fcfd5fdf05025a)
- Peel SHA: bbb9454d3b7cb0ac6125df43b5dad775e86f2c56 (short bbb9454) — do not retag
- SAMPLE SHA: 45863d8eff2f999a84d40e8e82e229e44ea8f84b (short 45863d8)
- FUNDING SHA: 513ea9f4e7102c49e0d8cd9a0019d1f543ddbb1f (short 513ea9f)

Marketplace URL: none. Listing is morning HITL, not published. Do not invent a live Marketplace URL.

Sister published listing (different Action, already live): https://github.com/marketplace/actions/hospital-mrf-index — do not treat that as this listing.

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`):

```
USGS Earthquakes
```

Short description (from live action.yml `description:`; Marketplace card subtitle, keep <=125 chars; this string is 90):

```
$40 custom public-data pull. Free Action: fetch USGS earthquakes, optional change-detect.
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title:

```
usgs-earthquakes-action v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `activity`, color `yellow`.

## Long description (ready to paste)

```
Fetch official USGS earthquake events from earthquake.usgs.gov FDSN Event GeoJSON (public, no API key) with optional minmagnitude / since / circle search and optional change-detect. Composite GitHub Action. Live pulls are capped (default 100, max 200). Official USGS FDSN Event API only — this Action does not scrape earthquake.usgs.gov HTML.

uses: bennyj121/usgs-earthquakes-action@v0.1.0

Free path: fetch USGS earthquakes in CI (live FDSN Event GeoJSON or a committed fixture). Optional minmagnitude, since, and circle search (latitude / longitude / maxradiuskm). Optional since change-detect. Outputs count, change-count, newest event fields, source (live or fixture), report-path (writes usgs-earthquakes.json). Live endpoint: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson

Paid path: $40 Custom public-data pull (USGS earthquakes extract or similar): https://ko-fi.com/benjaminjohnston/commissions (alias 621b4c7e76). In the order note write exactly "USGS earthquakes extract" and the filter wanted (e.g. minmagnitude, since, or circle). Buyer-facing SAMPLE: https://github.com/bennyj121/usgs-earthquakes-action/blob/main/examples/paid-pull-sample/README.md

What it does: live fetch of official USGS FDSN Event GeoJSON; optional minmagnitude / since / circle search; optional since change-detect; hard cap on live events (default 100, max 200); fixture fallback when earthquake.usgs.gov is unreachable from CI.

Built by Rogue, an AI agent, not a human. Not a USGS product. USGS does not endorse this Action.
```

## Free vs paid (do not blur)

- Free: fetch official USGS FDSN Event GeoJSON in CI (live earthquake.usgs.gov or `fixture`), optional `minmagnitude` / `since` / circle search, optional change-detect. Live cap default 100, max 200.
- Paid: $40 Custom public-data pull, alias 621b4c7e76 = https://ko-fi.com/benjaminjohnston/commissions — USGS earthquakes extract (or similar public-data pull).
- Secondary offer page: https://bennyj121.github.io/hospital-price-series/offer.html
- SAMPLE of a $40 order: https://github.com/bennyj121/usgs-earthquakes-action/blob/main/examples/paid-pull-sample/README.md
- FUNDING SHA 513ea9f custom CTA: https://ko-fi.com/benjaminjohnston/commissions

## Example (from live README)

```yaml
- uses: bennyj121/usgs-earthquakes-action@v0.1.0
  with:
    # minmagnitude: '2.5'
    # since: '2026-08-01'
    # latitude: '33.45'
    # longitude: '-112.07'
    # maxradiuskm: '250'
    limit: '100'
```

If the live API is unreachable, pass a committed USGS-shaped GeoJSON fixture:

```yaml
- uses: bennyj121/usgs-earthquakes-action@v0.1.0
  with:
    fixture: fixtures/sample.json
    since: '2026-08-01'
```

## Out of scope for this draft

Do not open listing UI. Do not publish.
Do not invent a live Marketplace URL.
Do not retag v0.1.0 (peel stays bbb9454).
Do not ship Action 022.
No registry ship. No PRs. No email.

Built by Rogue, an AI agent.
