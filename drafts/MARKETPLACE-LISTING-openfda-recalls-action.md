# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is HITL draft paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for openfda-recalls-action@v0.1.0 (repo bennyj121/openfda-recalls-action). Not published. No Marketplace card URL exists for this Action — do not invent one.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: openfda-recalls-action@v0.1.0
- uses: bennyj121/openfda-recalls-action@v0.1.0
- Repo: https://github.com/bennyj121/openfda-recalls-action
- Release tag: v0.1.0 (annotated tag object 44d2c96ac5ae65995c5b9fa347a08856de19ad0a)
- Peel SHA: dcad0cde5e761391d46c0ecd8c0b98e6606f29a1 (short dcad0cde) — do not retag
- SAMPLE SHA: 7ca132d96dcad74040b4931f93b43c3e49a0a714 (short 7ca132d)
- FUNDING SHA: 7666cd04c9bdf8fc70d9ac2595e97e9e55636795 (short 7666cd0)

Marketplace URL: none. Listing is morning HITL, not published. Do not invent a live Marketplace URL.

Sister published listing (different Action, already live): https://github.com/marketplace/actions/hospital-mrf-index — do not treat that as this listing.

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`):

```
openFDA Drug Recalls
```

Short description (from live action.yml `description:`; Marketplace card subtitle, keep <=125 chars; this string is 93):

```
$40 custom public-data pull. Free Action: fetch openFDA drug recalls, optional change-detect.
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title:

```
openfda-recalls-action v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `alert`, color `red`.

## Long description (ready to paste)

```
Fetch official openFDA drug enforcement (recall) records from api.fda.gov (public JSON, no API key required for light use) with optional since report_date and classification Class I/II/III filters and optional change-detect. Composite GitHub Action. Live pulls are capped (default 100, max 200). Official api.fda.gov only — this Action does not scrape FDA HTML.

uses: bennyj121/openfda-recalls-action@v0.1.0

Free path: fetch openFDA drug recalls in CI (live api.fda.gov/drug/enforcement.json or a committed fixture). Optional since report_date and classification (Class I / Class II / Class III). Optional since change-detect. Outputs count, change-count, newest recall fields, source (live or fixture), report-path (writes openfda-recalls.json). Live endpoint: https://api.fda.gov/drug/enforcement.json

Paid path: $40 Custom public-data pull (openFDA recalls extract or similar): https://ko-fi.com/benjaminjohnston/commissions (alias 621b4c7e76). In the order note write exactly "openFDA recalls extract" and the filter wanted (e.g. since date or Class I). Buyer-facing SAMPLE: https://github.com/bennyj121/openfda-recalls-action/blob/main/examples/paid-pull-sample/README.md

What it does: live fetch of official openFDA drug enforcement JSON; optional since report_date and classification filters; optional since change-detect; hard cap on live records (default 100, max 200); fixture fallback when api.fda.gov is unreachable from CI.

Built by Rogue, an AI agent, not a human. Not an FDA or openFDA product. FDA and openFDA do not endorse this Action. Not medical advice.
```

## Free vs paid (do not blur)

- Free: fetch official openFDA drug enforcement JSON in CI (live api.fda.gov or `fixture`), optional `since` report_date / `classification` Class I/II/III, optional change-detect. Live cap default 100, max 200.
- Paid: $40 Custom public-data pull, alias 621b4c7e76 = https://ko-fi.com/benjaminjohnston/commissions — openFDA recalls extract (or similar public-data pull).
- Secondary offer page: https://bennyj121.github.io/hospital-price-series/offer.html
- SAMPLE of a $40 order: https://github.com/bennyj121/openfda-recalls-action/blob/main/examples/paid-pull-sample/README.md
- FUNDING SHA 7666cd0 custom CTA: https://ko-fi.com/benjaminjohnston/commissions

## Example (from live README)

```yaml
- uses: bennyj121/openfda-recalls-action@v0.1.0
  with:
    # since: '2026-08-01'
    # classification: 'Class I'
    limit: '100'
```

If the live API is unreachable, pass a committed openFDA-shaped JSON fixture:

```yaml
- uses: bennyj121/openfda-recalls-action@v0.1.0
  with:
    fixture: fixtures/sample.json
    since: '2026-08-01'
```

## Out of scope for this draft

Do not open listing UI. Do not publish.
Do not invent a live Marketplace URL.
Do not retag v0.1.0 (peel stays dcad0cde).
Do not ship Action 022.
No registry ship. No PRs. No email.

Built by Rogue, an AI agent.
