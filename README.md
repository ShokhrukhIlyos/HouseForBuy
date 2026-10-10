# HouseForBuy

Home-search knowledge base for Mirzo Ulug‘bek district, Tashkent (Qorasuv first): 2–3 rooms, up to US$75,000.

The site is one static page, `site/index.html`, built from the research data.

## Layout

- `qorasuv-knowledge-base/` – research data and notes
  - `listings.json` – Qorasuv leads (Q001–Q013)
  - `mirzo-ulugbek-additional-listings.json` – rest of district (M001–M014)
  - `karasu-realtor-channel.json` – karasu_realtor Telegram leads (T001–T006)
- `tashkent-house-buying-sources.md` – 26 listing sites, agencies and Telegram channels
- `src/template.html` – page template (data is injected at build time)
- `build.py` – builds `site/index.html`
- `netlify.toml` – Netlify config

## Update the data

Edit the JSON files, then run:

```
python build.py
```

Netlify runs the same command on every push, so editing a JSON file on GitHub is enough to update the live site.

## Deploy to Netlify

1. Netlify → **Add new site → Import an existing project → GitHub** → pick `HouseForBuy`.
2. Settings are read from `netlify.toml` (build command `python3 build.py`, publish directory `site`). Leave the form fields as they are.
3. Deploy.

The site sends `X-Robots-Tag: noindex` so search engines don't index it. Anyone with the link can still open it.

Progress and notes typed into the page are saved in the browser only (localStorage), not on the server.
