# HITL / NOT PUBLISHED — Stripe Payment Link success + cancel page paste copy (Friday COT Pack)

**Status:** HITL draft. Not published. Not live. **Do not create the live Stripe product, Price, or Payment Link overnight.** Paste-ready success + cancel page copy only. Atlas drops these into Stripe Dashboard later when creating the COT Payment Link from `drafts/notes-first-cot-stripe-clickpath-2026-09-01.md` / checkout `drafts/notes-first-cot-pack-checkout-2026-08-30.md` (commit SHA `54a523828414e3dd5f663dbec4ae64e140029ccb` or live path). No Stripe login. No live SKU. No `buy.stripe.com` URL. No Ko-fi. No Gumroad. No GitHub paid storefront.

**Overnight rule (Atlas, 8:46 PM PT Sep 1, 2026):** Atlas does **not** create the live Stripe product overnight. Success + cancel paste copy only. Other files untouched (fulfillment email, click-path, checkout sheet, morning card, notes-index, publish-order, pack bodies stay as-is).

**SKU:** Candidate #2 only — Friday COT Pack (12 liquid futures, CFTC public). Not candidates 1 or 3. Not the $40 hospital MRF extract. Not Ko-fi. Not GitHub storefront. Not a muonarc.com live path.

**AI disclosure (Rogue):** An AI (Rogue + helper bots) prepared this success + cancel paste copy. Benjamin / Atlas reviews before any Payment Link or Note goes live. Any live Note would state it is AI-built.

**Sources (read-only — do not rewrite):**
- Click-path: `drafts/notes-first-cot-stripe-clickpath-2026-09-01.md` SHA `476066d2ae9843f419783827bb467f8dc1d546d0`
- Checkout paste-fields (live path): `drafts/notes-first-cot-pack-checkout-2026-08-30.md` (commit SHA `54a523828414e3dd5f663dbec4ae64e140029ccb` may 404 as a blob; live path used)
- Fulfillment email (not rewritten): `drafts/notes-first-cot-fulfillment-email-2026-09-01.md` SHA `a8cda7dd03612bc42d506983aa2c910ddeac3e59`

```
CHECKOUT URL: NOT LIVE / PLACEHOLDER
```

Do not invent a live checkout URL.

---

## 1) Success page (buyers see after pay)

**NOT LIVE.** Placeholder title + body for Stripe `after_completion` / **Confirmation page** custom message (`hosted_confirmation`). Do not treat as a published success page. Do not invent a muonarc.com or `buy.stripe.com` success URL.

### Success page title

Stripe field: Confirmation page title / custom confirmation heading (if the Dashboard exposes one). **Confirm in Dashboard.** Do not invent a live URL.

```
Thanks — Friday COT Pack received
```

### Success page body

Stripe field: Confirmation page custom message (`after_completion.hosted_confirmation.custom_message`). Atlas will email the brief + CSV. No live checkout URL.

```
Thanks — this purchase is recorded.

Atlas will email this week's Markdown/HTML brief and CSV (Friday COT Pack: 12 liquid futures, as-of Tuesday 2026-08-25 / released Friday 2026-08-28).

This success page is a placeholder, not a live muonarc.com path. There is no live checkout URL in this draft.

If you do not receive the files, reply to the receipt email.
```

Suggested `after_completion` type: `hosted_confirmation` (or custom URL later). If Atlas later wants `after_completion.type` = `redirect`, the URL stays a placeholder until a real page exists. Docs: https://docs.stripe.com/payment-links/post-payment

---

## 2) Cancel page (buyers who leave checkout)

**NOT LIVE.** Placeholder title + body. Do not treat as a published cancel page. Do not invent a live cancel URL. Try again / return path is copy only — no live URL.

### Cancel page title

Stripe field: cancel / abandoned-checkout page title **if** the Dashboard exposes one. Public Payment Links docs do **not** document a Dashboard **Cancel URL** field (unlike Checkout Session `cancel_url`). **Confirm in Dashboard.** Do not guess a button named "Cancel URL."

```
Checkout canceled — no charge
```

### Cancel page body

Try again / return path without a live URL. No charge. Pack not delivered.

```
Checkout canceled. No charge.

The Friday COT Pack was not delivered. You can close this tab, or try again later from the same Payment Link Atlas shares when it is live.

This cancel page is a placeholder, not a live muonarc.com path. There is no live checkout URL in this draft. Do not bookmark a buy.stripe.com or muonarc.com cancel path from this file — none exists.
```

No live cancel URL. Atlas may paste a cancel URL later **if** the Dashboard exposes one.

---

## 3) Paste-ready Stripe Dashboard fields (later — not overnight)

Copy each labeled block into the matching Stripe Payment Link field **later**, when creating the COT Payment Link from `drafts/notes-first-cot-stripe-clickpath-2026-09-01.md` / checkout SHA `54a52382` (or live checkout path `drafts/notes-first-cot-pack-checkout-2026-08-30.md`). Atlas does **not** paste these overnight. **Do not click Create link. Do not create the live product.**

Price bands stay **UNLOCKED**. Success/cancel stay placeholders — not live URLs.

### Product name

Stripe field: Product name.

```
Friday COT Pack: 12 liquid futures (CFTC public)
```

### Price band (UNLOCKED — do not lock a live amount)

**Band from checkout SHA `54a52382` / live checkout path / `635b5cbb`:** **$12–$25 / Friday pack**, or **$20–$40 / month retain** (4 packs).

Atlas picks a number later. Do **not** invent a live locked price in Stripe. Do **not** paste a single dollar amount from this file as if it were live.

- Per-pack = one Friday pack (Markdown/HTML Note + CSV, 12 rows).
- Monthly retain = four consecutive Friday packs (same 12-contract set, same field set).

**SUGGESTION (not live, in-band only — Atlas may ignore):** $18 / Friday pack, or $32 / month retain. Suggestion only. Not a Stripe price. Not a live SKU.

Stripe field: Price. Leave unset or enter Atlas’s pick later.

### Description / what the buyer gets

Stripe field: Product description / Payment Link description.

```
This week's Friday COT Pack: 12 liquid futures from CFTC public Legacy Futures-Only COT.

Week as-of Tuesday 2026-08-25 / released Friday 2026-08-28: 12 rows (CL, NG, GC, SI, ZC, ZS, ZW, ES, NQ, 6E, 6J, BTC). Markdown/HTML brief + CSV. Not a GitHub issue form.

HITL source (not a storefront):
- drafts/notes-first-cot-pack-2026-08-30.md
- drafts/cot-pack-2026-08-28.csv

Public CFTC data only. AI-built (Rogue); human-reviewed before any live sale.
```

### After the payment (success — paste later)

Docs: https://docs.stripe.com/payment-links/post-payment

Later, when creating the live link:

1. Click **After the payment**.
2. Under **Confirmation page**, prefer the documented custom confirmation message (`hosted_confirmation`).
3. Paste **Success page title** (if a heading field exists — confirm in Dashboard).
4. Paste **Success page body** as the custom message.
5. Do **not** set a live muonarc.com or `buy.stripe.com` success URL.

If **After the payment** / **Confirmation page** is not visible, **confirm in Dashboard**. Do not guess another label.

### Cancel (paste later if Dashboard exposes a field)

Keep **Cancel page title** + **Cancel page body** as copy only. No live cancel URL. Confirm in Dashboard whether a cancel / abandoned-checkout URL exists. Do not guess a button.

### CHECKOUT URL

**NOT LIVE / PLACEHOLDER.** Do not invent a `buy.stripe.com` or muonarc.com checkout URL.

```
CHECKOUT URL: NOT LIVE / PLACEHOLDER
```

---

## HITL close

- File: `drafts/notes-first-cot-success-cancel-2026-09-01.md`
- Success + cancel paste copy only. Not a live Stripe product. **Do not create the live Stripe product overnight.**
- Price band **unlocked** ($12–$25/Friday pack or $20–$40/month retain). Success/cancel stay placeholders. Checkout URL: NOT LIVE / PLACEHOLDER.
- Other files untouched (fulfillment email, click-path, checkout sheet, morning card, notes-index, publish-order, pack bodies).
- STOP holds: no $40 hospital MRF extract, no GitHub paid storefront, no extract-request, no cold email, no r/datasets, DIP, OpenFEMA, NHC. No publish, post, email, chase, or listing UI.

AI-drafted by Rogue. Benjamin / Atlas reviews before any Payment Link or Note goes live.
