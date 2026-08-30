# Hugging Face dataset upload (morning HITL)

HITL draft only. Benjamin or Atlas morning. Rogue does not self-register or upload.

Status: HITL DRAFT ONLY. Do not upload. Do not self-register. HF account HITL stays with Atlas.

Upload `hf/README.md` plus `examples/paid-pull-sample`.
Do NOT upload `data/fmc_shoppable_sample_2026-08-25.csv` as the product sample.

`hf/README.md` already has `(@v0.1.6)` and the SAMPLE pointer. Peel v0.1.6 stays 3dea121 (3dea121c23ad93299aeeb2a4f550e92cc14f6b0d). Do not retag. SAMPLE SHA 0f333c48d0b20402be2d19800cbd9f1531f0151b (0f333c48; examples/paid-pull-sample/; FMC + Kaiser + UCLA). FUNDING SHA d212fc16ee67e045c592790814c72a0e10d07f04 (d212fc16).

Paid path: $40 hospital MRF-change extract (not a quote) — https://bennyj121.github.io/hospital-price-series/offer.html
Request it on the issue form: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml
In the order note write exactly "monthly MRF-change extract" and the hospital name.
Cash-path: offer.html + extract-request. Do not point buyers at Ko-fi 621b4c7e76 as an MRF SKU (left as-is OpenFEMA custom public-data pull $40 / 2 slots). Do not use ko-fi.com/benjaminjohnston/commissions as a CTA.

Dataset name stays `fmc-shoppable-extract`. Card already in-repo. No HF account. Rogue does not self-register. Do not invent an HF URL as published. Do not invent a Marketplace URL.

An AI drafted this; Benjamin/Atlas reviews before any post.

## Morning commands (Benjamin / Atlas only)

1. Create a human Hugging Face account. Do not let a bot self-register. HF account HITL stays with Atlas.

2. Install the CLI and log in (browser or token that only the human pastes):

```
python3 -m pip install -U huggingface_hub
huggingface-cli login
```

3. Create one public dataset and upload the card plus the paid-pull SAMPLE:

```
huggingface-cli repo create fmc-shoppable-extract --type dataset --yes
huggingface-cli upload fmc-shoppable-extract hf/README.md README.md --repo-type dataset
huggingface-cli upload fmc-shoppable-extract examples/paid-pull-sample paid-pull-sample --repo-type dataset
```

4. Keep the card text: Built by Rogue, an AI agent. Not a patient quote. Not endorsed by CMS or any hospital. License CC0-1.0 for Rogue-authored layout. Charge rows stay the hospital public disclosure. SAMPLE: live FMC + Kaiser WA Central + UCLA Ronald Reagan under examples/paid-pull-sample (SAMPLE SHA 0f333c48, not a quote). Paid path: offer.html + extract-request, not Ko-fi 621b4c7e76.

5. After Atlas HITL upload, dataset name stays `fmc-shoppable-extract` on the human account. Nothing is published yet. Do not invent an HF URL as published. Do not invent a Marketplace URL.

Do not run these commands from a bot session.
