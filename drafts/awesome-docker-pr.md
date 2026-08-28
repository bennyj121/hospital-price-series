# HITL draft only. Do not open this PR.

Target: https://github.com/veggiemonk/awesome-docker (best-fit public awesome-docker; 36k stars; already lists small CLI images under In-Container Tooling: su-exec, microcheck, gosu).
Section: In-Container Tooling (alphabetically after GoSu, before is-docker).
Format: `- [Name](link) - one sentence, lead with the verb` per .github/CONTRIBUTING.md. One entry per PR. Link the repo (not GHCR; image is not published yet). Local-only / no GHCR yet.
Note: their "for Docker" test is strict (reject apps that only ship in a container). This draft still fits the asked list. Do not open if Atlas wants a softer list later.

## PR title

Add hospital-mrf-extract Dockerfile

## PR body

Adds one In-Container Tooling entry (alphabetically after GoSu).

Proposed line:

- [hospital-mrf-extract](https://github.com/bennyj121/hospital-price-series) - Build a local 129MB CLI image (COPY pyproject.toml + shoppable_extract, no git) that extracts cash and named-payer CPT rates from a CMS hospital CSV. $40 hospital MRF-change extract (not a quote); SAMPLE at examples/sample-mrf-change/. Local-only / no GHCR yet.

Repo: https://github.com/bennyj121/hospital-price-series
Dockerfile: https://github.com/bennyj121/hospital-price-series/blob/main/Dockerfile
Local one-liner: docker build -t hospital-mrf-extract . && docker run --rm -v "$PWD/data:/data" hospital-mrf-extract --csv /data/fmc_standardcharges_sample_1000.csv --cpts 90371,90378,90380,90381 --out /data/shoppable_extract.csv

Built by Rogue, an AI agent, not a human. Not endorsed by CMS or any hospital. Not a patient quote, bill, or coverage determination. Image is local-only until Atlas HITL pushes GHCR. Do not open this PR.

Do not open this PR from this draft. Atlas HITL only. No emails, no comments, no docker push. Local-only / no GHCR yet.
