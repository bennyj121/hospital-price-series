# hospital-mrf-extract GHCR publish (morning HITL)

HITL draft only. Benjamin or Atlas morning. Rogue does not docker push and does not create a GHCR package.

Status: HITL DRAFT ONLY. Do not docker push. Do not push GHCR.

Do not retry GitHub Packages npm from this draft.

Image is `ghcr.io/bennyj121/hospital-mrf-extract` tags `0.1.6` and `latest` (NOT `0.1.0`). Peel v0.1.6 stays 3dea121 (3dea121c23ad93299aeeb2a4f550e92cc14f6b0d). Do not retag. SAMPLE SHA 0f333c48d0b20402be2d19800cbd9f1531f0151b (0f333c48; examples/paid-pull-sample/; FMC + Kaiser + UCLA). FUNDING SHA d212fc16ee67e045c592790814c72a0e10d07f04 (d212fc16).

Paid path: $40 hospital MRF-change extract (not a quote) — https://bennyj121.github.io/hospital-price-series/offer.html
Request it on the issue form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
In the order note write exactly "monthly MRF-change extract" and the hospital name.
Cash-path: offer.html + extract-request. Do not point buyers at Ko-fi 621b4c7e76 as an MRF SKU (left as-is OpenFEMA custom public-data pull $40 / 2 slots). Do not use ko-fi.com/benjaminjohnston/commissions as a CTA.

Package description LEADS with `$40 hospital MRF-change extract` (not a quote). Point buyers at `https://bennyj121.github.io/hospital-price-series/offer.html` and the SAMPLE at `examples/paid-pull-sample` (SAMPLE SHA 0f333c48).

Dry-run 2026-08-26 12:58 AM PT: local `docker build -t hospital-mrf-extract:dry` succeeded (image 474a04cefd75, 227MB). Run on `data/fmc_standardcharges_sample_1000.csv` wrote 4 rows. Rogue did not docker push and did not create a GHCR package.

Image name stays `ghcr.io/bennyj121/hospital-mrf-extract` (public). Human `write:packages` token required. `latest` tag also ok. Nothing is published yet. Do not invent a GHCR URL as published. Do not invent a Marketplace URL.

An AI drafted this; Benjamin/Atlas reviews before any post.

## Morning commands (Benjamin / Atlas only)

1. GitHub PAT with `write:packages` and `read:packages` (classic) or the packages write scope. User `bennyj121`. Do not let a bot mint the token.

2. From a clone of `bennyj121/hospital-price-series` on main (Dockerfile already on main):

```
docker build -t ghcr.io/bennyj121/hospital-mrf-extract:0.1.6 -t ghcr.io/bennyj121/hospital-mrf-extract:latest .
echo "$GHCR_PAT" | docker login ghcr.io -u bennyj121 --password-stdin
docker push ghcr.io/bennyj121/hospital-mrf-extract:0.1.6
docker push ghcr.io/bennyj121/hospital-mrf-extract:latest
gh api --method PATCH /user/packages/container/hospital-mrf-extract -f visibility=public
```

3. On the GHCR package page, set description: $40 hospital MRF-change extract (not a quote). https://bennyj121.github.io/hospital-price-series/offer.html. SAMPLE: live FMC + Kaiser WA Central + UCLA Ronald Reagan under examples/paid-pull-sample (SAMPLE SHA 0f333c48, not a quote). Built by Rogue, an AI agent. Not endorsed by CMS or any hospital. Public image. No zip download. Paid path: offer.html + extract-request, not Ko-fi 621b4c7e76.

4. After push, pull is `docker pull ghcr.io/bennyj121/hospital-mrf-extract:0.1.6`. Until then stay local: `docker build -t hospital-mrf-extract .` (README one-liner). Nothing is published yet. Do not invent a GHCR URL as published. Do not invent a Marketplace URL.

Do not run these commands from a bot session. Do not pay a publisher fee. CC0-1.0.
