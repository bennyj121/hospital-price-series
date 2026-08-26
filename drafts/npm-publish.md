# hospital-mrf-index morning HITL
Dry-run pack succeeded. Tarball /tmp/nmpsk/hospital-mrf-index-0.1.0.tgz 484 B. Registry 404 for hospital-mrf-index and shoppable-extract. No account created.

Morning (human only):
1. Register at the public JS registry (2FA).
2. In the repo helper folder: pack --ignore-scripts, then upload with access public.
3. Keep AI disclosure on the project page: Built by Rogue, an AI agent. Not a quote. Not endorsed by CMS.
4. Until then use: pip install git+https://github.com/bennyj121/hospital-price-series.git
Do not run upload from a bot session.

Exact commands:
```
cd npm
npm pack --ignore-scripts
ls hospital-mrf-index-0.1.0.tgz
npm publish --access public
```
