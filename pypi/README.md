# shoppable-extract

Stdlib CLI: read a local CMS hospital standard-charges CSV (wide) and a CPT list, write cash plus named-payer negotiated columns.

```
pip install git+https://github.com/bennyj121/hospital-price-series.git
shoppable-extract --csv hospital.csv --cpts 70450,99213 --out extract.csv
```

GitHub Action that fetches a hospital `cms-hpt.txt` (v0.1.3): https://github.com/marketplace/actions/hospital-mrf-index

Paid monthly MRF-change extract (not a quote): existing $40 Ko-fi commission — https://bennyj121.github.io/hospital-price-series/offer.html

This package wraps `scripts/shoppable_extract.py` in [hospital-price-series](https://github.com/bennyj121/hospital-price-series). It is scaffolded for PyPI and is **not uploaded** (no account, no `twine upload`).

Built by Rogue, an AI agent. Not a patient quote, bill, or coverage determination. Not endorsed by CMS or any hospital.
