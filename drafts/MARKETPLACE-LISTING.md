# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. Do not invent a live Marketplace URL. This file is morning-pack item 2 paste copy for Atlas. Rogue does not open listing editor.

Listing this draft is for: NEW Marketplace listing for cms-hpt-validate@v0.1.0 (repo bennyj121/cms-hpt-validate). Not published. No Marketplace card URL exists for this Action — do not invent one.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action: cms-hpt-validate@v0.1.0
- uses: bennyj121/cms-hpt-validate@v0.1.0
- Repo: https://github.com/bennyj121/cms-hpt-validate
- Release tag: v0.1.0 (annotated tag object eb5f3471c8a4cd375d1fe8485af6d1100483a758)
- Peel SHA: 2dc4da87ac1d25d098cca84c651a1002ec71a96d (short 2dc4da8) — do not retag
- SAMPLE SHA: 899f86fe15c3bcfe0101d5a5b228b22b48f53204 (short 899f86fe)
- FUNDING SHA: 61ced87f72753948ff21845033bd8f5a774bb2a6 (short 61ced87f)

Marketplace URL: none. Listing is morning HITL, not published. Do not invent a live Marketplace URL.

Sister published listing (different Action, already live): https://github.com/marketplace/actions/hospital-mrf-index — do not treat that as this listing.

## Suggested Marketplace fields (ready to paste)

Name (from live action.yml `name:`):

```
CMS HPT validate
```

Short description (from live action.yml `description:`; Marketplace card subtitle, keep <=125 chars; this string is 101):

```
Validate hospital cms-hpt.txt and HEAD-check mrf-url targets. $40 monthly compliance digest via Ko-fi.
```

Primary category: Continuous integration

Secondary category: Utilities

Release tag to attach: v0.1.0

Release title:

```
cms-hpt-validate v0.1.0
```

Branding (already in action.yml; listing UI reads it): icon `check-circle`, color `green`.

## Long description (ready to paste)

```
Validate a hospital cms-hpt.txt (45 CFR 180.50 machine-readable index) and optionally HEAD/GET-probe each mrf-url. Composite GitHub Action + CLI.

uses: bennyj121/cms-hpt-validate@v0.1.0

Free path: single-index validate. One cms-hpt.txt / index in CI (index-url or a local file). Outputs cms-hpt-validate.json plus ok, error-count, location-count.

Paid path: multi-hospital batch/remediation (several indexes, dated report) — not a single-index validate. $40 Custom public-data pull: https://ko-fi.com/benjaminjohnston/commissions (alias 621b4c7e76). Buyer-facing SAMPLE: https://github.com/bennyj121/cms-hpt-validate/blob/main/examples/paid-pull-sample/README.md

What it checks: required location-name, source-page-url, mrf-url; duplicate mrf-url warnings; optional reachability (HEAD, GET Range fallback); redacts contact-email in the JSON report.

Built by Rogue, an AI agent, not a human. Not endorsed by CMS or any hospital. Not a quote, bill, or coverage determination. Do not email hospital staff.
```

## Free vs paid (do not blur)

- Free: single cms-hpt.txt / index validate in CI (`index-url` or `file`).
- Paid: $40 Custom public-data pull, alias 621b4c7e76 = https://ko-fi.com/benjaminjohnston/commissions — multi-hospital batch/remediation.
- Secondary offer page: https://bennyj121.github.io/hospital-price-series/offer.html
- SAMPLE of a $40 order: https://github.com/bennyj121/cms-hpt-validate/blob/main/examples/paid-pull-sample/README.md

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
Do not invent a live Marketplace URL.
Do not retag v0.1.0 (peel stays 2dc4da8).
Do not ship Action 022.
No registry ship. No PRs. No email.

Built by Rogue, an AI agent.
