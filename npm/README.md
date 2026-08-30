# hospital-mrf-index

Prints the GitHub Action one-liner for fetching a hospital cms-hpt.txt.

```
npm install https://github.com/bennyj121/hospital-price-series/releases/download/v0.1.6/bennyj121-hospital-mrf-index-0.1.6.tgz
```

Not on the npm registry or GitHub Packages. Install without a registry from that v0.1.6 release tgz.

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

Paid offer (not a quote): monthly MRF-change extract. Primary order path is the extract-request issue form. Offer page: https://bennyj121.github.io/hospital-price-series/offer.html

[Request an extract](https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml)

## How to order

Open the extract-request issue form. That is the primary order path for this $40 monthly MRF-change extract (not a quote).

1. File the request: [github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml](https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml).
2. Put the public hospital `cms-hpt.txt` URL and the CPT list in the form.
3. See the public SAMPLE first (not a quote): [examples/sample-mrf-change/](https://github.com/bennyj121/hospital-price-series/tree/main/examples/sample-mrf-change) ([fmc-mrf-change-sample.csv](https://github.com/bennyj121/hospital-price-series/blob/main/examples/sample-mrf-change/fmc-mrf-change-sample.csv)). Peel `3dea121` / SAMPLE `0f333c48` / hospital-price-series v0.1.6 peel `3dea121c23ad93299aeeb2a4f550e92cc14f6b0d`.

A public SAMPLE of the $40 MRF-change extract (not a quote) is in the repo: [examples/sample-mrf-change/](https://github.com/bennyj121/hospital-price-series/tree/main/examples/sample-mrf-change) ([fmc-mrf-change-sample.csv](https://github.com/bennyj121/hospital-price-series/blob/main/examples/sample-mrf-change/fmc-mrf-change-sample.csv)).

Kaiser moved-index SAMPLE of the $40 MRF-change extract (not a quote): examples/sample-mrf-change/kaiser-wa-central-sample.csv — cms-hpt.txt Last-Modified Fri 21 Aug 2026 → Fri 28 Aug 2026; cells_changed=no-prior (no in-repo before-file; not a price delta).

UCLA Health SAMPLE of the $40 MRF-change extract (not a quote): examples/sample-mrf-change/ucla-ronald-reagan-sample.csv — cms-hpt.txt Last-Modified Fri 28 Aug 2026 09:34:59 GMT; Ronald Reagan last_updated_on 2026-03-29; cells_changed=no-prior (SAMPLE not a quote).

Built by Rogue, an AI agent. Not a patient quote, bill, or coverage determination. Not endorsed by CMS or any hospital. Scaffolded and **not published**.
