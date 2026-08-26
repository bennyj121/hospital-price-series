# Hugging Face dataset upload (morning HITL)

Dry-run 2026-08-25 11:19 PM PT: huggingface-cli is not on PATH (command -v empty). Rogue did not create an account, did not login, and did not upload. In-repo card already exists at hf/README.md (CC0-1.0, AI disclosure, CPT lists, Action + git pip + offer links).

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
huggingface-cli upload fmc-shoppable-extract data/fmc_shoppable_sample_2026-08-25.csv fmc_shoppable_sample_2026-08-25.csv --repo-type dataset
```

4. Keep the card text: Built by Rogue, an AI agent. Not a patient quote. Not endorsed by CMS or any hospital. License CC0-1.0 for Rogue-authored layout. Charge rows stay the hospital public disclosure.

5. Expected URL after upload: https://huggingface.co/datasets/<account>/fmc-shoppable-extract

Do not run these commands from a bot session. Optional second file if wanted: data/fmc_shoppable_fullfile_2026-08-25.csv.
