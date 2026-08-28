# shoppable-extract PyPI publish (morning HITL)

HITL draft only. Benjamin or Atlas morning. Rogue does not register or twine upload.

`pyproject.toml` is already version `0.1.6`. Description leads with `$40 hospital MRF-change extract`. Readme is `pypi/README.md`. Documentation is `offer.html`.

Build artifacts will be `shoppable_extract-0.1.6.tar.gz` and `shoppable_extract-0.1.6-py3-none-any.whl` (NOT `0.1.0`).

`shoppable-extract` is still unpublished on pypi.org (404). Human account + 2FA required. Rogue does not register or twine upload.

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

3. On the PyPI project page, keep the AI disclosure: Built by Rogue, an AI agent. Not a patient quote. Not endorsed by CMS or any hospital.

4. After upload, the install line becomes `pip install shoppable-extract`. Until then use `pip install git+https://github.com/bennyj121/hospital-price-series.git`.

Do not run these commands from a bot session. No publisher fee. CC0-1.0.
