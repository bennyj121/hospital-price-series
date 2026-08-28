# hospital-mrf-extract GHCR publish (morning HITL)

HITL draft only. Benjamin or Atlas morning. Rogue does not docker push and does not create a GHCR package.

Do not retry GitHub Packages npm from this draft.

Image is `ghcr.io/bennyj121/hospital-mrf-extract` tags `0.1.6` and `latest` (NOT `0.1.0`).

Package description LEADS with `$40 hospital MRF-change extract` (not a quote). Point buyers at `https://bennyj121.github.io/hospital-price-series/offer.html` and the SAMPLE at `examples/sample-mrf-change/ (fmc-mrf-change-sample.csv)`.

Dry-run 2026-08-26 12:58 AM PT: local `docker build -t hospital-mrf-extract:dry` succeeded (image 474a04cefd75, 227MB). Run on `data/fmc_standardcharges_sample_1000.csv` wrote 4 rows. Rogue did not docker push and did not create a GHCR package.

Image name: `ghcr.io/bennyj121/hospital-mrf-extract` (public). Human `write:packages` token required. `latest` tag also ok.

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

3. On the GHCR package page, set description: $40 hospital MRF-change extract (not a quote). https://bennyj121.github.io/hospital-price-series/offer.html. SAMPLE: live FMC + Kaiser WA Central + UCLA Ronald Reagan under examples/sample-mrf-change/ on Release v0.1.6 (SAMPLE, not a quote). Built by Rogue, an AI agent. Not endorsed by CMS or any hospital. Public image. No zip download.

4. After push, pull is `docker pull ghcr.io/bennyj121/hospital-mrf-extract:0.1.6`. Until then stay local: `docker build -t hospital-mrf-extract .` (README one-liner).

Do not run these commands from a bot session. Do not pay a publisher fee. CC0-1.0.
