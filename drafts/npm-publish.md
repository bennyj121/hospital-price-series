# @bennyj121/hospital-mrf-index GitHub Packages (morning HITL)

HITL draft only. Benjamin or Atlas morning. Rogue does not upload, register, or retry Packages.

Package is `@bennyj121/hospital-mrf-index` version `0.1.6`.
Target is GitHub Packages (`https://npm.pkg.github.com`), NOT public npmjs.com `0.1.0`.

`npm/package.json` is already `0.1.6`. Description leads with `$40 hospital MRF-change extract`. Homepage is `offer.html`. `publishConfig.registry` is `https://npm.pkg.github.com`.

Packages E403 parked (token is repo+workflow only). Morning HITL: `gh auth refresh` for read:packages + write:packages. Do not retry overnight.

Pack artifact name if packed: `@bennyj121-hospital-mrf-index-0.1.6.tgz` (scoped).

## Morning commands (Benjamin / Atlas only)

```
cd npm
npm pack --ignore-scripts
ls @bennyj121-hospital-mrf-index-0.1.6.tgz
npm publish --access public   # registry from publishConfig = GitHub Packages
```

Keep AI disclosure: Built by Rogue, an AI agent. Not a quote. Not endorsed by CMS.

Until then use: `pip install git+https://github.com/bennyj121/hospital-price-series.git`

Do not run upload from a bot session.
