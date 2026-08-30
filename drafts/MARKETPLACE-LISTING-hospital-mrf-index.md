# HITL DRAFT ONLY — GitHub Marketplace listing copy

Status: HITL DRAFT ONLY. Do not open the Marketplace listing UI. Do not publish. This is an EDIT of the existing hospital-mrf-index card, not a new listing. Rogue does not open listing editor.

Listing this draft is for: EDIT of the EXISTING Marketplace card hospital-mrf-index (HTTP 200, Latest v0.1.6). Repo bennyj121/hospital-price-series. Do not create a new listing. Do not invent a new Marketplace URL.

AI disclosure: an AI (Rogue) drafted this. Benjamin/Atlas reviews before any listing UI. Marketplace listings stay morning HITL.

## Action

- Action/card: hospital-mrf-index @ v0.1.6
- uses: bennyj121/hospital-price-series@v0.1.6
- Repo: https://github.com/bennyj121/hospital-price-series
- Release tag: v0.1.6 (annotated tag object 5ff4fd46e230639ae2c0679ef4ae853392b40c19)
- Peel SHA: 3dea121c23ad93299aeeb2a4f550e92cc14f6b0d (short 3dea121) — do not retag
- SAMPLE SHA: 0f333c48d0b20402be2d19800cbd9f1531f0151b (short 0f333c48) — examples/paid-pull-sample
- FUNDING SHA: d212fc16ee67e045c592790814c72a0e10d07f04 (short d212fc16)

Marketplace URL (fetched live, HTTP 200, Latest v0.1.6): https://github.com/marketplace/actions/hospital-mrf-index

Do not invent a new Marketplace URL. Existing card is hospital-mrf-index Latest v0.1.6 HTTP 200. This draft is paste copy for an EDIT of that card only.

## Current short description to replace

Live card About / og:description (fetched from https://github.com/marketplace/actions/hospital-mrf-index, HTTP 200):

```
Fetch a hospital cms-hpt.txt and write published MRF URLs. Built by Rogue, an AI agent. Not endorsed by CMS or any hospital
```

HITL rank 1 (drafts/HITL-2026-08-29.md): card still Fetch. Set short description to $40 hospital MRF-change extract.

Live action.yml `description:` is already `$40 hospital MRF-change extract. Free index: fetch cms-hpt.txt, write MRF URLs, optional CPT extract.` The Marketplace listing short-description field is separate and still shows the Fetch-cms-hpt wording above. This EDIT pastes the short string only; do not retag; do not change action.yml from this draft.

## Suggested Marketplace fields (ready to paste)

Name (leave as live action.yml `name:`; do not rename the card):

```
Hospital MRF index
```

Short description (Marketplace card subtitle, keep <=125 chars; this string is 31). REPLACE the Fetch-cms-hpt wording with:

```
$40 hospital MRF-change extract
```

Primary / secondary category: leave existing. This is an EDIT of the short description, not a recategorization.

Release tag already attached: v0.1.6 (Latest). Do not retag. Peel stays 3dea121.

Release title (already shipped; do not retag):

```
hospital-mrf-index v0.1.6
```

Branding (already in action.yml; listing UI reads it): icon `file-text`, color `blue`.

## Long description (ready to paste)

Leave the live long description unless Atlas also wants a paste. Below matches live README + action.yml if the long field is edited in the same pass. Do not invent a new Marketplace URL.

```
$40 hospital MRF-change extract

The free GitHub Action is hospital-mrf-index: https://github.com/marketplace/actions/hospital-mrf-index.

uses: bennyj121/hospital-price-series@v0.1.6

Free path: fetch a hospital cms-hpt.txt (45 CFR 180.50) and write published mrf-url lines. Optional CPT extract from a CMS wide CSV already in the workspace (no zip download). Outputs mrf-count and extract-rows.

Paid path: $40 hospital MRF-change extract (not a quote) — https://ko-fi.com/benjaminjohnston/commissions (alias 621b4c7e76; title: Custom public-data pull). In the order note write exactly "monthly MRF-change extract" and the hospital name. Buyer-facing SAMPLE: https://github.com/bennyj121/hospital-price-series/blob/main/examples/paid-pull-sample/README.md

What it does: curl the hospital cms-hpt.txt; parse mrf-url lines to mrf-urls.txt; optional shoppable-extract on a local CSV + CPT list. Not a zip download.

Built by Rogue, an AI agent, not a human. Not endorsed by CMS or any hospital. Not a quote, bill, or coverage determination. Do not email hospital staff listed in an index.
```

## Free vs paid (do not blur)

- Free: hospital-mrf-index fetches cms-hpt.txt and writes MRF URLs; optional CPT extract from a CSV already in the workspace.
- Paid: $40 Custom public-data pull, alias 621b4c7e76 = https://ko-fi.com/benjaminjohnston/commissions — hospital MRF-change extract (not a quote).
- Secondary offer page: https://bennyj121.github.io/hospital-price-series/offer.html
- SAMPLE of a $40 order: https://github.com/bennyj121/hospital-price-series/blob/main/examples/paid-pull-sample/README.md
- FUNDING SHA d212fc16 custom CTA: https://ko-fi.com/benjaminjohnston/commissions

## Example (from live README)

```yaml
- uses: bennyj121/hospital-price-series@v0.1.6
  with:
    index-url: https://www.nahealth.com/cms-hpt.txt
```

Index, then a CSV already in the workspace (no zip download):

```yaml
- uses: actions/checkout@v4
- uses: bennyj121/hospital-price-series@v0.1.6
  with:
    index-url: https://www.nahealth.com/cms-hpt.txt
    csv: data/fmc_standardcharges_sample_1000.csv
    cpts: 90371,90378,90380,90381
```

## Out of scope for this draft

Do not open listing UI. Do not publish.
Do not invent a new Marketplace URL. Existing card is hospital-mrf-index Latest v0.1.6 HTTP 200 at https://github.com/marketplace/actions/hospital-mrf-index.
Do not retag v0.1.6 (peel stays 3dea121).
Do not ship Action 022.
No registry ship. No PRs. No email.
Do not fold this into drafts/HITL-2026-08-29.md.

Built by Rogue, an AI agent.
