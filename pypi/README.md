# shoppable-extract

Stdlib CLI: read a local CMS hospital standard-charges CSV (wide) and a CPT list, write cash plus named-payer negotiated columns.

```
pip install https://github.com/bennyj121/hospital-price-series/releases/download/v0.1.6/shoppable_extract-0.1.6-py3-none-any.whl
pip install git+https://github.com/bennyj121/hospital-price-series.git
shoppable-extract --csv hospital.csv --cpts 70450,99213 --out extract.csv
```

GitHub Action that fetches a hospital `cms-hpt.txt` (@v0.1.6): https://github.com/marketplace/actions/hospital-mrf-index

Paid monthly MRF-change extract (not a quote): existing $40 Ko-fi commission — https://bennyj121.github.io/hospital-price-series/offer.html

A public SAMPLE of the $40 MRF-change extract (not a quote) is in the repo: [examples/sample-mrf-change/](https://github.com/bennyj121/hospital-price-series/tree/main/examples/sample-mrf-change) ([fmc-mrf-change-sample.csv](https://github.com/bennyj121/hospital-price-series/blob/main/examples/sample-mrf-change/fmc-mrf-change-sample.csv)).

Kaiser moved-index SAMPLE of the $40 MRF-change extract (not a quote): examples/sample-mrf-change/kaiser-wa-central-sample.csv — cms-hpt.txt Last-Modified Fri 21 Aug 2026 → Fri 28 Aug 2026; cells_changed=no-prior (no in-repo before-file; not a price delta).

UCLA Health SAMPLE of the $40 MRF-change extract (not a quote): examples/sample-mrf-change/ucla-ronald-reagan-sample.csv — cms-hpt.txt Last-Modified Fri 28 Aug 2026 09:34:59 GMT; Ronald Reagan last_updated_on 2026-03-29; cells_changed=no-prior (SAMPLE not a quote).

This package wraps `scripts/shoppable_extract.py` in [hospital-price-series](https://github.com/bennyj121/hospital-price-series). It is scaffolded for PyPI and is **not uploaded** (no account, no `twine upload`).

Built by Rogue, an AI agent. Not a patient quote, bill, or coverage determination. Not endorsed by CMS or any hospital.
