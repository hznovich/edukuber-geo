#!/usr/bin/env python3
# Edit GEO_BASE / lists below, run:  python3 regenerate-profile.py
import json, base64

GEO_BASE = "https://geo.edukuber.com"   # <-- RU-reachable host (Cloudflare-fronted)

cfg = {
  "Name": "edukuber",
  "GlobalProxy": "false",
  "RouteOrder": "block-proxy-direct",
  "RemoteDNSType": "DoH",
  "RemoteDNSDomain": "https://cloudflare-dns.com/dns-query",
  "RemoteDNSIP": "1.1.1.1",
  "DomesticDNSType": "DoU",
  "DomesticDNSDomain": "",
  "DomesticDNSIP": "77.88.8.8",
  "Geoipurl":   f"{GEO_BASE}/geoip.dat",
  "Geositeurl": f"{GEO_BASE}/geosite.dat",
  "DnsHosts": {},
  "DirectSites": ["geosite:category-ru", "geosite:private"],
  "DirectIp":    ["geoip:private", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"],
  "ProxySites":  ["geosite:edukuber-proxy"],
  "ProxyIp":     ["geoip:edukuber-proxy"],
  "BlockSites":  ["geosite:category-ads-all"],
  "BlockIp": [],
  "DomainStrategy": "IPIfNonMatch",
  "FakeDNS": "false",
  "UseChunkFiles": "true"
}

compact = json.dumps(cfg, separators=(",", ":"), ensure_ascii=False)
b64 = base64.b64encode(compact.encode()).decode()
print("JSON:\n" + compact + "\n")
print("DEEPLINK (put in Remnawave 'routing' header):\n" + "happ://routing/onadd/" + b64)
