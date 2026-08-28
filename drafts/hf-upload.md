# Hugging Face dataset upload (morning HITL)

HITL draft only. Benjamin or Atlas morning. Rogue does not self-register or upload.

Upload `hf/README.md` plus `examples/sample-mrf-change/fmc-mrf-change-sample.csv`.
Do NOT upload `data/fmc_shoppable_sample_2026-08-25.csv` as the product sample.

`hf/README.md` already has `(@v0.1.6)` and the SAMPLE pointer.

Dataset name stays `fmc-shoppable-extract`. Card already in-repo. No HF account. Rogue does not self-register.

## Morning commands (Benjamin / Atlas only)

1. Create a human Hugging Face account. Do not let a bot self-register.

2. Install the CLI and log in (browser or token that only the human pastes):

```
python3 -m pip install -U huggingface_hub
huggingface-cli login
```

3. Create one public dataset and upload the card plus the sample extract CSV:

```
huggingface-cli repo create fmc-shoppable-extract --type dataset --yes
huggingface-cli upload fmc-shoppable-extract hf/README.md README.md --repo-type dataset
huggingface-cli upload fmc-shoppable-extract examples/sample-mrf-change/fmc-mrf-change-sample.csv fmc-mrf-change-sample.csv --repo-type dataset
```

4. Keep the card text: Built by Rogue, an AI agent. Not a patient quote. Not endorsed by CMS or any hospital. License CC0-1.0 for Rogue-authored layout. Charge rows stay the hospital public disclosure.

5. Expected URL after upload: https://huggingface.co/datasets/<account>/fmc-shoppable-extract

Do not run these commands from a bot session.
