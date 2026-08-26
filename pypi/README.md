# shoppable-extract

Stdlib CLI: read a local CMS hospital standard-charges CSV (wide) and a CPT list, write cash plus named-payer negotiated columns.

```
pip install shoppable-extract
shoppable-extract --csv hospital.csv --cpts 70450,99213 --out extract.csv
```

This package wraps `scripts/shoppable_extract.py` in [hospital-price-series](https://github.com/bennyj121/hospital-price-series). It is scaffolded for PyPI and is **not uploaded** (no account, no `twine upload`).

Built by Rogue, an AI agent. Sample extract, not a patient quote, bill, or guarantee. Not endorsed by CMS or any hospital.