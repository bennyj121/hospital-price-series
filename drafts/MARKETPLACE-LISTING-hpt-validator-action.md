# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is morning-pack item 3 paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for hpt-validator-action@v0.1.0 (repo bennyj121/hpt-validator-action). Not published. No Marketplace card URL exists for this Action — do not invent one.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: hpt-validator-action@v0.1.0
- uses: bennyj121/hpt-validator-action@v0.1.0
- Repo: https://github.com/bennyj121/hpt-validator-action
- Release tag: v0.1.0 (annotated tag object 94431b6f0afffd4a5ad7a7e75d717ad898360d3f)
- Peel SHA: 70962b754943e8c6ec6793e7fcdd50226d60f508 (short 70962b7) — do not retag
- SAMPLE SHA: 1eaef808a0be11c503120a9e0177a2a1713b968a (short 1eaef808) — official CMS example CSV; no fixture
- FUNDING SHA: 0fb8c199e79e8d9a6a582d60af684372767cddb3 (short 0fb8c199)

Marketplace URL: none. Listing is morning HITL, not published. Do not invent a live Marketplace URL.

Sister published listing (different Action, already live): https://github.com/marketplace/actions/hospital-mrf-index — do not treat that as this listing.

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`):

```
CMS HPT Validator
```

Short description (from live action.yml `description:`; Marketplace card subtitle, keep <=125 chars; this string is 73):

```
$40 multi-hospital HPT report. Free Action wraps @cmsgov/hpt-validator-cli.
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title:

```
hpt-validator-action v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `shield`, color `blue`.

## Long description (ready to paste)

```
GitHub Action that wraps the official CMS Hospital Price Transparency CLI (@cmsgov/hpt-validator-cli) so CI can validate MRF CSV/JSON files.

uses: bennyj121/hpt-validator-action@v0.1.0

Free path: single-file validate. One MRF CSV/JSON in CI (url or a local path). Outputs valid, error-count, alert-count, report-path (writes hpt-validate-report.json). Official CLI: https://github.com/CMSgov/hpt-validator-cli

Paid path: multi-hospital batch/remediation (several files, dated digest) — not a single-file validate. $40 Custom public-data pull: https://ko-fi.com/benjaminjohnston/commissions (alias 621b4c7e76). Buyer-facing SAMPLE: https://github.com/bennyj121/hpt-validator-action/blob/main/examples/paid-pull-sample/README.md

What it checks: official CMS HPT dictionary (v2.1 / v2.2 / v3.0) via the pinned @cmsgov/hpt-validator-cli. Sample URL is the official CMS Wide CSV example — no fixture.

Built by Rogue, an AI agent, not a human. Not affiliated with or endorsed by CMS or any hospital. Not a quote, bill, or coverage determination. Do not email hospital staff.
```

## Free vs paid (do not blur)

- Free: single MRF CSV/JSON validate in CI (`url` or `path`).
- Paid: $40 Custom public-data pull, alias 621b4c7e76 = https://ko-fi.com/benjaminjohnston/commissions — multi-hospital batch/remediation.
- Secondary offer page: https://bennyj121.github.io/hospital-price-series/offer.html
- SAMPLE of a $40 order: https://github.com/bennyj121/hpt-validator-action/blob/main/examples/paid-pull-sample/README.md
- SAMPLE SHA 1eaef808 uses the official CMS example CSV (no fixture).

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
Do not invent a live Marketplace URL.
Do not retag v0.1.0 (peel stays 70962b7).
Do not ship Action 022.
No registry ship. No PRs. No email.

Built by Rogue, an AI agent.
