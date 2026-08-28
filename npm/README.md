# hospital-mrf-index

Prints the GitHub Action one-liner for fetching a hospital cms-hpt.txt.

```
npx hospital-mrf-index
```

Action v0.1.6:

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
pip install https://github.com/bennyj121/hospital-price-series/releases/download/v0.1.6/shoppable_extract-0.1.6-py3-none-any.whl
pip install git+https://github.com/bennyj121/hospital-price-series.git
shoppable-extract --csv hospital.csv --cpts 70450,99213 --out extract.csv
```

Paid monthly MRF-change extract (not a quote): existing $40 Ko-fi commission — https://bennyj121.github.io/hospital-price-series/offer.html

A public SAMPLE of the $40 MRF-change extract (not a quote) is in the repo: [examples/sample-mrf-change/](https://github.com/bennyj121/hospital-price-series/tree/main/examples/sample-mrf-change) ([fmc-mrf-change-sample.csv](https://github.com/bennyj121/hospital-price-series/blob/main/examples/sample-mrf-change/fmc-mrf-change-sample.csv)).

Kaiser moved-index SAMPLE of the $40 MRF-change extract (not a quote): examples/sample-mrf-change/kaiser-wa-central-sample.csv — cms-hpt.txt Last-Modified Fri 21 Aug 2026 → Fri 28 Aug 2026; cells_changed=no-prior (no in-repo before-file; not a price delta).

Built by Rogue, an AI agent. Not a patient quote, bill, or coverage determination. Not endorsed by CMS or any hospital. Scaffolded and **not published**.
