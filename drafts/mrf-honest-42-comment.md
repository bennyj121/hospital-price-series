# HITL DRAFT ONLY. Do not post on ChelseaKR/mrf-honest#42.

Target: https://github.com/ChelseaKR/mrf-honest/pull/42
Title: fix: a charged row still owes a description and a setting (#28)
Repo: ChelseaKR/mrf-honest (other people's; public; not archived; PR open; locked: false)
Author: ChelseaKR (human, OWNER) — created 2026-08-28T23:44:58Z / 2026-08-28 4:44 PM PT (inside 2026-08-16..2026-08-30 America/Phoenix)
Updated: 2026-08-29T19:04:50Z / 2026-08-29 12:04 PM PT. Comments at draft: 1 (ChelseaKR self-review, left open for a publishing decision). State: open. merged: false. locked: false.
Picked as the single best last-14-day commentable GitHub Pull Request on someone else's repo about parsing CMS hospital MRF / cms-hpt.txt files.

Search (2026-08-30 12:00 AM PT; gh api search/issues + gh search prs + WebSearch/WebFetch; GitHub Issues / Discussions / other-forge not searched):
- cms-hpt.txt / cms-hpt / "hospital price transparency" / "hospital MRF" / chargemaster / hospital-price-transparency / "machine-readable file" hospital / "standard charges" is:pr created:>=2026-08-16
- is:pr is:open variants of the same terms
- repo:CMSgov/hospital-price-transparency, repo:CMSgov/hpt-validator-cli, repo:ChelseaKR/mrf-honest, repo:EndurantDevs/healthcare-mrf-api, repo:jatishay07/everyfront, repo:nathansutton/hospital-price-transparency, repo:medprice-ai/mcp-medprice-ai

Skipped (do not draft, do not post):
- bennyj121 repos; hospital-price-series#1 Kaiser / #2 UCLA (our issues; out of scope). Do not invent issue #3.
- ChelseaKR/mrf-honest#28 (already HITL drafted SHA aec54f49) — this draft is the open PR that closes it, not the issue
- CMSgov/hospital-price-transparency discussions/219 (already HITL drafted SHA c90f198b)
- EndurantDevs/healthcare-mrf-api#767 (open; CodeRabbit-only comment; facility-alias registry dump, not a human support thread). #766 ptg2 payer NPI / #762 plan-pricing census (payer, not hospital HPT). Merged hospital-prices PRs 702–765: rapid-fire, CodeRabbit, already have drafts/healthcare-mrf-api-comment.md
- jatishay07/everyfront PRs 6/12/27/42 (merged; already have drafts/everyfront-comment.md)
- ChelseaKR/mrf-honest#22/#23/#24 (merged/closed 2026-08-19; not currently an open support thread)
- medprice-ai/mcp-medprice-ai PRs in window (closed; MCP protocol, not CMS HPT parse)
- natalialuzuriaga-testing-org/automated-codejson-generator-list#2 (github-actions[bot] dump)
- cha1mhn/ClaudeTest#4 (closed 2026-08-17; crowdsourced bills, not cms-hpt.txt / hospital MRF parse)
- CMSgov/hospital-price-transparency and CMSgov/hpt-validator-cli: 0 PRs in window
- Open hospital-website / cursor[bot] noise (eddylin07/Hospital, Disione838/trpo_jules, keithkahurakamau/HMS-2): not CMS HPT
- Open PRs outside window (ross0nline/acis#9 2026-07-07, dmojisola848/Healthcare-price-transparency#1 2025-11)
- GitHub Issues, GitHub Discussions, GitLab/Bitbucket/Codeberg NONEs (stay unfolded). Do not fold this hunt into HITL pack ef6df064. Do not stack extra NONEs.

An AI drafted this; Benjamin/Atlas reviews before any post.

- uses: bennyj121/hospital-price-series@v0.1.6 (hospital-mrf-index)
- Tag peel: 3dea121 (do not retag; peel stays 3dea121c23ad93299aeeb2a4f550e92cc14f6b0d)
- SAMPLE pack SHA 0f333c48d0b20402be2d19800cbd9f1531f0151b — examples/paid-pull-sample (FMC + Kaiser + UCLA)
- FUNDING SHA d212fc16ee67e045c592790814c72a0e10d07f04
- Primary CTA: https://ko-fi.com/s/621b4c7e76
- Secondary (house style): https://ko-fi.com/benjaminjohnston/commissions
- Do not invent a Marketplace URL. Marketplace listings stay morning HITL. Do not claim the $40 short-description edit is live.
- Do not retag v0.1.6. Do not ship Action 022. Do not open listing UI. Do not open PRs. Do not email. Do not post this comment.

## Ready-to-paste GitHub PR comment

I am Rogue, an AI agent (not a human), working in bennyj121/hospital-price-series.

This PR is the CSV completeness fix for charged rows that still owe `description` and `setting` when the code pairing is missing — on the same inspect path that already streams CMS hospital Tall/Wide MRFs discovered from cms-hpt.txt. We keep a thin Action that fetches one cms-hpt.txt and writes the mrf-url lines: `uses: bennyj121/hospital-price-series@v0.1.6` (hospital-mrf-index; peel 3dea121).

A SAMPLE of the follow-on monthly MRF-change extract is on peel 3dea121 / v0.1.6 under `examples/paid-pull-sample`: https://github.com/bennyj121/hospital-price-series/tree/main/examples/paid-pull-sample

If a dated public-data pull of MRF changes would help next to the CSV cohort re-assess this branch is waiting on, there is a $40 custom extract: https://ko-fi.com/s/621b4c7e76

In the order note write “monthly MRF-change extract”. Not a quote, bill, or coverage determination. Not endorsed by CMS or any hospital. An AI drafted this; Benjamin reviews before any post.
