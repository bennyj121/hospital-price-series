# shoppable-extract PyPI publish (morning HITL)

HITL draft only. Benjamin or Atlas morning. Rogue does not register or twine upload.

Status: HITL DRAFT ONLY. Do not register. Do not twine upload. Do not publish.

`pyproject.toml` is already version `0.1.6`. Package name stays `shoppable-extract`. Readme is `pypi/README.md`. Documentation is `offer.html`. Peel v0.1.6 stays 3dea121 (3dea121c23ad93299aeeb2a4f550e92cc14f6b0d). Do not retag. SAMPLE SHA 0f333c48d0b20402be2d19800cbd9f1531f0151b (0f333c48; examples/paid-pull-sample/; FMC + Kaiser + UCLA). FUNDING SHA d212fc16ee67e045c592790814c72a0e10d07f04 (d212fc16).

Paid: live $40 Custom public-data pull (alias 621b4c7e76) — https://ko-fi.com/benjaminjohnston/commissions — monthly MRF-change extract (not a quote).

Build artifacts will be `shoppable_extract-0.1.6.tar.gz` and `shoppable_extract-0.1.6-py3-none-any.whl` (NOT `0.1.0`).

`shoppable-extract` is still unpublished on pypi.org (404). Human account + 2FA required. Rogue does not register or twine upload. Do not invent a PyPI URL as published. Do not invent a Marketplace URL.

An AI drafted this; Benjamin/Atlas reviews before any post.

## Morning commands (Benjamin / Atlas only)

1. Create a PyPI account at https://pypi.org/account/register/ (human, 2FA). Do not let a bot register.

2. From a clone of `bennyj121/hospital-price-series` on main:

```
python3 -m venv .venv
.venv/bin/pip install build twine
.venv/bin/python -m build
ls dist/shoppable_extract-0.1.6.tar.gz dist/shoppable_extract-0.1.6-py3-none-any.whl
.venv/bin/twine upload dist/shoppable_extract-0.1.6.tar.gz dist/shoppable_extract-0.1.6-py3-none-any.whl
```

3. On the PyPI project page, keep the AI disclosure: Built by Rogue, an AI agent. Not a patient quote. Not endorsed by CMS or any hospital. SAMPLE: live FMC + Kaiser WA Central + UCLA Ronald Reagan under examples/paid-pull-sample (SAMPLE SHA 0f333c48, not a quote).

4. After upload, the install line becomes `pip install shoppable-extract`. Until then use `pip install git+https://github.com/bennyj121/hospital-price-series.git`. Nothing is published yet. Do not invent a PyPI URL as published.

Do not run these commands from a bot session. No publisher fee. CC0-1.0.
