# shoppable-extract PyPI publish (morning HITL)

Dry-run 2026-08-25 10:59 PM PT: `python -m build` succeeded. Local `dist/` has `shoppable_extract-0.1.0.tar.gz` (3512 B) and `shoppable_extract-0.1.0-py3-none-any.whl` (4561 B). Rogue did not register an account and did not upload.

Name `shoppable-extract` was free on pypi.org (JSON 404) as of 2026-08-25. Human account required.

## Morning commands (Benjamin / Atlas only)

1. Create a PyPI account at https://pypi.org/account/register/ (human, 2FA). Do not let a bot register.

2. From a clone of `bennyj121/hospital-price-series` on main:

```
python3 -m venv .venv
.venv/bin/pip install build twine
.venv/bin/python -m build
ls dist/shoppable_extract-0.1.0.tar.gz dist/shoppable_extract-0.1.0-py3-none-any.whl
.venv/bin/twine upload dist/shoppable_extract-0.1.0.tar.gz dist/shoppable_extract-0.1.0-py3-none-any.whl
```

3. On the PyPI project page, keep the AI disclosure: Built by Rogue, an AI agent. Not a patient quote. Not endorsed by CMS or any hospital.

4. After upload, the install line becomes `pip install shoppable-extract`. Until then use `pip install git+https://github.com/bennyj121/hospital-price-series.git`.

Do not run these commands from a bot session. No publisher fee. CC0-1.0.
