import datetime
import hashlib
import os

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
AFF_BASE = "https://www.floristone.com/main.cfm?source_id=aff&AffiliateID=21885"
BASE_URL = "https://brightlane.github.io/SendFlowersOnline"
today = datetime.date.today()
date_str = str(today)
year = today.year
seed = int(hashlib.md5(date_str.encode()).hexdigest()[:8], 16)

# ─────────────────────────────────────────────
# CONTENT POOLS
# ─────────────────────────────────────────────
cities = [
    "New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia",
    "San Antonio","San Diego","Dallas","San Jose","Austin","Seattle",
    "Denver","Nashville","Miami","Atlanta","Tampa","Minneapolis",
    "Toronto","Montreal","Vancouver","Calgary","Edmonton","Ottawa",
    "Winnipeg","Quebec City","Hamilton","Kelowna","Halifax","Saskatoon"
]

occasions = [
    {"name":"Mother's Day","slug":"mothers-day","tag":"md"},
    {"name":"Birthday",    "slug":"birthday",   "tag":"bd"},
    {"name":"Anniversary", "slug":"anniversary","tag":"an"},
    {"name":"Sympathy",    "slug":"sympathy",   "tag":"sy"},
    {"name":"Get Well",    "slug":"get-well",   "tag":"gw"},
    {"name":"Romance",     "slug":"romance",    "tag":"ro"},
    {"name":"Thank You",   "slug":"thank-you",  "tag":"ty"},
    {"name":"New Baby",    "slug":"new-baby",   "tag":"nb"},
]

titles = [
    "Send {occ} Flowers Online to {city} — Same-Day Delivery {year}",
    "Best {occ} Flowers Delivered Online to {city} — Free Same Day",
    "Order {occ} Flowers Online in {city} — No Hidden Fees",
    "Last Minute {occ} Flowers Online — Still Delivered Today in {city}",
]

intros = [
    "Looking to send {occ} flowers online to {city} today? Floristone delivers farm-fresh flowers same-day to every neighbourhood in {city} — free delivery, $0 service fees, freshness guaranteed.",
    "Send {occ} flowers online to {city} in minutes. Floristone's local florist network delivers same-day across {city} with free delivery and zero hidden fees — starting at $29.99.",
    "Need to send {occ} flowers online today in {city}? Floristone makes it simple — order in 2 minutes, same-day delivery, free, no service fees, 4.8 stars from 18,742 customers.",
    "The easiest way to send {occ} flowers online to {city} — Floristone delivers same-day with free delivery and $0 fees. Farm-fresh, local florists, live tracking included.",
]

# Pick today's content deterministically
city     = cities[seed % len(cities)]
occasion = occasions[(seed // 7) % len(occasions)]
title_t  = titles[(seed // 13) % len(titles)]
intro_t  = intros[(seed // 17) % len(intros)]

title = title_t.format(occ=occasion["name"], city=city, year=year)
intro = intro_t.format(occ=occasion["name"].lower(), city=city)
aff_link = f"{AFF_BASE}&occ={occasion['tag']}"
city_slug = city.lower().replace(" ", "-")
filename = f"blog-{city_slug}-{occasion['slug']}-{date_str}.html"

# ─────────────────────────────────────────────
# HTML
# ─────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SendFlowersOnline</title>
    <meta name="description" content="Send {occasion['name'].lower()} flowers online to {city}. Free same-day delivery, $0 service fees, from $29.99. 4.8 stars from 18,742 customers.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{BASE_URL}/{filename}">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@graph":[
      {{"@type":"Article","headline":"{title}","datePublished":"{date_str}","dateModified":"{date_str}","author":{{"@type":"Organization","name":"SendFlowersOnline"}}}},
      {{"@type":"Product","name":"Floristone {occasion['name']} Flowers — {city}","offers":{{"@type":"Offer","priceCurrency":"USD","price":"29.99","availability":"https://schema.org/InStock","url":"{aff_link}","deliveryLeadTime":{{"@type":"QuantitativeValue","value":"0","unitCode":"DAY"}}}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"18742"}}}}
    ]}}
    </script>
    <style>
        :root{{--brand:#FF2E63;--bg:#f9f9ff;--border:#e6e6f0;--mid:#666;}}
        *{{box-sizing:border-box;margin:0;padding:0;}}
        body{{font-family:system-ui,sans-serif;background:var(--bg);color:#333;line-height:1.7;}}
        .nav{{background:#fff;padding:14px 5%;border-bottom:1px solid var(--border);font-weight:700;color:var(--brand);display:flex;justify-content:space-between;align-items:center;}}
        .nav a{{font-size:0.85rem;color:var(--brand);text-decoration:none;}}
        .article{{max-width:760px;margin:0 auto;padding:50px 24px 80px;}}
        .eyebrow{{font-size:0.75rem;font-weight:700;color:var(--brand);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:12px;display:block;}}
        h1{{font-size:clamp(1.8rem,4vw,2.5rem);color:#1a1a1a;margin-bottom:16px;line-height:1.2;}}
        .byline{{font-size:0.85rem;color:#999;margin-bottom:32px;border-bottom:1px solid var(--border);padding-bottom:16px;}}
        h2{{font-size:1.3rem;color:#1a1a1a;margin:32px 0 10px;}}
        p{{margin-bottom:16px;font-size:1rem;color:#444;}}
        .cta-box{{background:linear-gradient(135deg,#003366 0%,#FF2E63 100%);color:#fff;text-align:center;padding:40px 24px;border-radius:16px;margin:40px 0;}}
        .cta-box h2{{color:#fff;margin:0 0 10px;font-size:1.5rem;}}
        .cta-box p{{color:rgba(255,255,255,0.88);margin-bottom:20px;}}
        .cta-btn{{background:#fff;color:var(--brand);padding:14px 32px;border-radius:99px;font-weight:900;text-decoration:none;display:inline-block;font-size:1rem;}}
        .trust-row{{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-top:12px;}}
        .trust-row span{{font-size:0.75rem;color:rgba(255,255,255,0.8);font-weight:700;}}
        .faq-box{{background:#fff;border:1px solid var(--border);border-radius:12px;padding:24px;margin:32px 0;}}
        .faq-box strong{{display:block;color:#1a1a1a;margin-bottom:8px;}}
        .faq-box p{{margin:0;font-size:0.92rem;}}
        .back{{display:block;text-align:center;margin-top:32px;font-size:0.85rem;color:var(--brand);text-decoration:none;}}
        footer{{background:#111;color:#888;text-align:center;padding:24px;font-size:0.78rem;}}
    </style>
</head>
<body>
<nav class="nav">SendFlowersOnline <a href="{BASE_URL}/">← Back to home</a></nav>
<article class="article">
    <span class="eyebrow">{occasion['name']} · {city} · {date_str}</span>
    <h1>{title}</h1>
    <p class="byline">SendFlowersOnline · Same-day delivery in {city} · {date_str}</p>
    <p>{intro}</p>
    <h2>How to send {occasion['name'].lower()} flowers online to {city}</h2>
    <p>It takes less than 2 minutes. Click the button below, choose your arrangement, add a personal card message, enter the delivery address in {city}, and checkout. The price shown is the final price — free delivery included, $0 service fees. Flowers arrive the same day.</p>
    <h2>Why Floristone is the best way to send flowers online to {city}</h2>
    <p>4.8/5 stars from 18,742 verified customers. Free same-day delivery. $0 service fees. Local florists in {city} cut flowers fresh on the day of delivery — no warehouse transit, no wilted stems. Live tracking on every order so you know exactly when they arrive.</p>
    <div class="cta-box">
        <h2>Send {occasion['name']} Flowers to {city} Now</h2>
        <p>From $29.99 · Free delivery · $0 fees · 4.8★ from 18,742 customers</p>
        <a href="{aff_link}" class="cta-btn">Send Flowers Online Now 🌷</a>
        <div class="trust-row">
            <span>✓ FREE DELIVERY</span><span>✓ $0 FEES</span><span>✓ FRESHNESS GUARANTEED</span><span>✓ LIVE TRACKING</span>
        </div>
    </div>
    <div class="faq-box">
        <strong>Q: Can I send {occasion['name'].lower()} flowers online to {city} today?</strong>
        <p>Yes. Floristone guarantees same-day delivery across {city} with free delivery and $0 service fees. Order before the daily cutoff for guaranteed same-day arrival. The price shown at checkout is the final price — no hidden fees.</p>
    </div>
    <a href="{BASE_URL}/" class="back">← Browse all flower delivery options</a>
</article>
<footer>This page contains affiliate links. We may earn a commission at no cost to you. © {year} SendFlowersOnline</footer>
</body>
</html>"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

# Update sitemap
sitemap_entry = f'  <url><loc>{BASE_URL}/{filename}</loc><lastmod>{date_str}</lastmod><changefreq>never</changefreq><priority>0.7</priority></url>'
if os.path.exists("sitemap.xml"):
    with open("sitemap.xml", "r") as f:
        sm = f.read()
    if filename not in sm:
        sm = sm.replace("</urlset>", f"{sitemap_entry}\n</urlset>")
        with open("sitemap.xml", "w") as f:
            f.write(sm)

print(f"Generated: {filename}")
print(f"City: {city} | Occasion: {occasion['name']}")
print(f"Affiliate ID: 21885 ✓")
