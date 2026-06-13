# edukuber-geo

Builds `geosite.dat` + `geoip.dat` for the Happ routing profile (blacklist / GlobalProxy=false).

## What's here
- `data/edukuber-proxy`     — domains routed THROUGH the VPN (your proxy.lst). Becomes `geosite:edukuber-proxy`.
- `edukuber-proxy-ip.txt`   — IP/CIDR routed THROUGH the VPN (optional). Becomes `geoip:edukuber-proxy`.
- `config.json`             — v2fly/geoip build config.
- `.github/workflows/build-geo.yml` — daily CI: builds both .dat, publishes to release `geo-latest`.
- `regenerate-profile.py`   — edit host/lists -> prints the Happ deeplink for Remnawave.

## Setup
1. Push to a PUBLIC GitHub repo (release assets must be downloadable without auth).
2. Actions -> run "build-geo" (or just push). Release `geo-latest` gets geoip.dat + geosite.dat.
   Raw URL: https://github.com/<you>/edukuber-geo/releases/download/geo-latest/geosite.dat
3. IMPORTANT: geo files must be reachable from RU WITHOUT a VPN (chicken-and-egg).
   Front them with Cloudflare (geo.edukuber.com -> the release asset / R2). No User-Agent filter.
4. Set GEO_BASE in regenerate-profile.py, run it, paste the deeplink into
   Remnawave: Subscription -> Settings -> Additional Response Headers, key `routing`.
   Also set the required `providerId` header. Wrap in a Response Rule (user-agent CONTAINS happ).

## Notes
- geoip:ru is NOT built by default (avoids DB-IP dependency). RU split stays on the
  domain level via geosite:category-ru. To add geoip:ru, add a dbipCountryMMDB input.
- Refresh edukuber-proxy-ip.txt from current ASN data; CIDRs go stale.
