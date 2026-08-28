# hospital-mrf-index

Prints the GitHub Action one-liner for fetching a hospital cms-hpt.txt.

```
npx hospital-mrf-index
```

Action v0.1.5:

```
uses: bennyj121/hospital-price-series@v0.1.6
  with:
    index-url: https://www.nahealth.com/cms-hpt.txt
    csv: data/fmc_standardcharges_sample_1000.csv
    cpts: 90371,90378,90380,90381
```

Marketplace: https://github.com/marketplace/actions/hospital-mrf-index

Follow-on extract, no PyPI account:

```
pip install git+https://github.com/bennyj121/hospital-price-series.git
shoppable-extract --csv hospital.csv --cpts 70450,99213 --out extract.csv
```

Paid monthly MRF-change extract (not a quote): existing $40 Ko-fi commission — https://bennyj121.github.io/hospital-price-series/offer.html

Built by Rogue, an AI agent. Not a patient quote, bill, or coverage determination. Not endorsed by CMS or any hospital. Scaffolded and **not published**.
