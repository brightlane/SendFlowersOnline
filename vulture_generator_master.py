"""
vulture_generator_master.py
SendFlowersOnline — Daily Content Engine
Generates:
  1. 3 blog posts (city x occasion combos)
  2. 5 city landing pages
  3. Updated blog index
  4. Updated sitemap
Affiliate URL is locked — do not change.
"""
import datetime
import hashlib
import os
import json

# ─────────────────────────────────────────────
# CONFIG — DO NOT CHANGE AFFILIATE URL
# ─────────────────────────────────────────────
AFF_URL  = "https://www.floristone.com/main.cfm?cat=r&source_id=aff&AffiliateID=2013017799&affiliate_id=2013017799"
BASE_URL = "https://brightlane.github.io/SendFlowersOnline"
today    = datetime.date.today()
date_str = str(today)
year     = today.year
seed     = int(hashlib.md5(date_str.encode()).hexdigest()[:8], 16)

RELATED_SITES = [
    ("Send Flowers Online",     "https://brightlane.github.io/SendFlowersOnline/"),
    ("Mother's Day Flowers",    "https://brightlane.github.io/MothersDayFlowers/"),
    ("Bouquet Flowers",         "https://brightlane.github.io/BouquetFlowers/"),
    ("Valentine's Day Flowers", "https://brightlane.github.io/ValentinesDayFlowers/"),
    ("FTD Flowers",             "https://brightlane.github.io/FtdFlowers/"),
    ("Same Day Flowers",        "https://brightlane.github.io/SameDayFlowers/"),
    ("Christmas Flowers",       "https://brightlane.github.io/ChristmasFlowers/"),
    ("Flower Delivery",         "https://brightlane.github.io/FlowerDelivery/"),
    ("Same Day Florist",        "https://brightlane.github.io/SameDayFlorist/"),
]
related_links = " &nbsp;|&nbsp; ".join(
    f'<a href="{url}">{name}</a>' for name, url in RELATED_SITES
)

# ─────────────────────────────────────────────
# CONTENT POOLS
# ─────────────────────────────────────────────
CITIES = [
    # USA
    "New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia",
    "San Antonio","San Diego","Dallas","San Jose","Austin","Seattle",
    "Denver","Nashville","Miami","Atlanta","Tampa","Minneapolis",
    "Portland","Las Vegas","Sacramento","Baltimore","Kansas City",
    "Columbus","Indianapolis","Charlotte","Memphis","Louisville",
    "Boston","Detroit","El Paso","Fort Worth","Oklahoma City",
    # Canada
    "Toronto","Montreal","Vancouver","Calgary","Edmonton","Ottawa",
    "Winnipeg","Quebec City","Hamilton","Kelowna","Halifax","Saskatoon",
    "Victoria","Mississauga","Brampton","Surrey","London","Windsor",
]

OCCASIONS = [
    {"name": "Mother's Day",  "slug": "mothers-day",  "emoji": "🌷"},
    {"name": "Birthday",      "slug": "birthday",     "emoji": "🎂"},
    {"name": "Anniversary",   "slug": "anniversary",  "emoji": "💍"},
    {"name": "Sympathy",      "slug": "sympathy",     "emoji": "🕊️"},
    {"name": "Get Well",      "slug": "get-well",     "emoji": "💐"},
    {"name": "Romance",       "slug": "romance",      "emoji": "🌹"},
    {"name": "Thank You",     "slug": "thank-you",    "emoji": "💝"},
    {"name": "New Baby",      "slug": "new-baby",     "emoji": "👶"},
    {"name": "Graduation",    "slug": "graduation",   "emoji": "🎓"},
    {"name": "Just Because",  "slug": "just-because", "emoji": "🌸"},
]

TITLES = [
    "Send {occ} Flowers Online to {city} — Free Same-Day Delivery {year}",
    "Best {occ} Flowers Delivered to {city} Today — $0 Service Fees",
    "Order {occ} Flowers Online in {city} — No Hidden Fees",
    "Last-Minute {occ} Flowers in {city} — Still Delivered Today",
    "{occ} Flower Delivery {city} — Fresh Bouquets From $29.99",
]

INTROS = [
    "Looking to send {occ} flowers online to {city} today? Floristone delivers farm-fresh flowers same-day to every neighbourhood in {city} — free delivery, $0 service fees, freshness guaranteed.",
    "Send {occ} flowers online to {city} in minutes. Floristone's local florist network delivers same-day across {city} with free delivery and zero hidden fees — starting at $29.99.",
    "Need to send {occ} flowers online today in {city}? Floristone makes it simple — order in 2 minutes, same-day delivery, free, no service fees, 4.8 stars from 18,742 customers.",
    "The easiest way to send {occ} flowers online to {city} — Floristone delivers same-day with free delivery and $0 fees. Farm-fresh, hand-arranged by local florists, live tracking included.",
    "Sending {occ} flowers to {city} has never been easier. Choose your arrangement, add a personal message, and Floristone's local {city} florists deliver same-day — free, no fees, freshness guaranteed.",
]

CITY_INTROS = [
    "Floristone delivers fresh flowers same-day to every neighbourhood in {city}. Free delivery, zero service fees, 4.8 stars. Order by 2 PM for guaranteed same-day arrival.",
    "Same-day flower delivery across {city} — powered by Floristone's local florist network. No service fees, no hidden charges. Farm-fresh bouquets from $29.99.",
    "Send flowers to anyone in {city} today. Floristone partners with local {city} florists to deliver same-day, free, with $0 fees and live order tracking.",
]

SHARED_CSS = """
    :root{--brand:#FF2E63;--bg:#f9f9ff;--border:#e6e6f0;}
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:var(--bg);color:#333;line-height:1.7;}
    .nav{background:#fff;padding:14px 5%;border-bottom:1px solid var(--border);font-weight:700;color:var(--brand);display:flex;justify-content:space-between;align-items:center;}
    .nav a{font-size:.85rem;color:var(--brand);text-decoration:none;}
    .cta-box{background:linear-gradient(135deg,#003366,#FF2E63);color:#fff;text-align:center;padding:40px 24px;border-radius:16px;margin:40px 0;}
    .cta-box h2{color:#fff;margin:0 0 10px;font-size:1.5rem;}
    .cta-box p{color:rgba(255,255,255,.88);margin-bottom:20px;}
    .cta-btn{background:#fff;color:var(--brand);padding:14px 32px;border-radius:99px;font-weight:900;text-decoration:none;display:inline-block;font-size:1rem;}
    .trust-row{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-top:12px;}
    .trust-row span{font-size:.75rem;color:rgba(255,255,255,.8);font-weight:700;}
    .related{background:#fff;border-top:1px solid var(--border);padding:20px 24px;text-align:center;font-size:.82rem;}
    .related a{color:var(--brand);text-decoration:none;font-weight:600;}
    footer{background:#111;color:#888;text-align:center;padding:24px;font-size:.78rem;}
"""

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def pick(pool, offset=1):
    return pool[(seed * offset) % len(pool)]

def city_slug(city):
    return city.lower().replace(" ", "-")

def already_exists(filename):
    return os.path.isfile(filename)

generated_files = []

# ─────────────────────────────────────────────
# 1. BLOG POSTS — 3 per day
# ─────────────────────────────────────────────
def make_blog_post(city, occasion, idx):
    slug = city_slug(city)
    filename = f"blog-{slug}-{occasion['slug']}-{date_str}.html"

    if already_exists(filename):
        print(f"  ↩ Skipping (exists): {filename}")
        return None

    title   = pick(TITLES, idx + 1).format(occ=occasion["name"], city=city, year=year)
    intro   = pick(INTROS, idx + 3).format(occ=occasion["name"].lower(), city=city)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | SendFlowersOnline</title>
<meta name="description" content="Send {occasion['name'].lower()} flowers online to {city}. Free same-day delivery, $0 service fees, from $29.99. 4.8 stars.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{BASE_URL}/{filename}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[
  {{"@type":"Article","headline":"{title}","datePublished":"{date_str}","dateModified":"{date_str}","author":{{"@type":"Organization","name":"SendFlowersOnline"}}}},
  {{"@type":"Product","name":"Floristone {occasion['name']} Flowers — {city}",
    "offers":{{"@type":"Offer","priceCurrency":"USD","price":"29.99","availability":"https://schema.org/InStock","url":"{AFF_URL}"}},
    "aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"18742"}}}}
]}}
</script>
<style>{SHARED_CSS}
.article{{max-width:760px;margin:0 auto;padding:50px 24px 80px;}}
.eyebrow{{font-size:.75rem;font-weight:700;color:var(--brand);letter-spacing:.1em;text-transform:uppercase;margin-bottom:12px;display:block;}}
h1{{font-size:clamp(1.8rem,4vw,2.5rem);color:#1a1a1a;margin-bottom:16px;line-height:1.2;}}
.byline{{font-size:.85rem;color:#999;margin-bottom:32px;border-bottom:1px solid var(--border);padding-bottom:16px;}}
h2{{font-size:1.3rem;color:#1a1a1a;margin:32px 0 10px;}}
p{{margin-bottom:16px;font-size:1rem;color:#444;}}
.faq-box{{background:#fff;border:1px solid var(--border);border-radius:12px;padding:24px;margin:32px 0;}}
.faq-box strong{{display:block;color:#1a1a1a;margin-bottom:8px;}}
.back{{display:block;text-align:center;margin-top:20px;font-size:.85rem;color:var(--brand);text-decoration:none;}}
</style>
</head>
<body>
<nav class="nav">SendFlowersOnline <a href="{BASE_URL}/">← Home</a></nav>
<article class="article">
  <span class="eyebrow">{occasion['emoji']} {occasion['name']} · {city} · {date_str}</span>
  <h1>{title}</h1>
  <p class="byline">SendFlowersOnline · Same-day delivery in {city} · {date_str}</p>
  <p>{intro}</p>
  <h2>How to send {occasion['name'].lower()} flowers online to {city}</h2>
  <p>It takes less than 2 minutes. Click the button below, choose your arrangement, add a personal card message, enter the delivery address in {city}, and checkout. The price shown is the final price — free delivery included, $0 service fees. Flowers arrive the same day.</p>
  <h2>Why Floristone for {city} flower delivery</h2>
  <p>4.8 stars from 18,742 verified customers. Free same-day delivery. $0 service fees. Local florists in {city} cut flowers fresh on the day of delivery — no warehouse transit, no wilted stems. Live tracking on every order.</p>
  <div class="cta-box">
    <h2>Send {occasion['name']} Flowers to {city} Now {occasion['emoji']}</h2>
    <p>From $29.99 · Free delivery · $0 fees · 4.8★ from 18,742 customers</p>
    <a href="{AFF_URL}" class="cta-btn" target="_blank" rel="nofollow sponsored noopener">Send Flowers Online Now 🌷</a>
    <div class="trust-row">
      <span>✓ FREE DELIVERY</span><span>✓ $0 FEES</span><span>✓ FRESHNESS GUARANTEED</span><span>✓ LIVE TRACKING</span>
    </div>
  </div>
  <div class="faq-box">
    <strong>Q: Can I send {occasion['name'].lower()} flowers online to {city} today?</strong>
    <p>Yes. Floristone guarantees same-day delivery across {city} with free delivery and $0 service fees. Order before 2 PM local time for guaranteed same-day arrival.</p>
  </div>
  <a href="{AFF_URL}" class="back" target="_blank" rel="nofollow sponsored noopener">→ Browse all {occasion['name'].lower()} arrangements on Floristone</a>
  <a href="{BASE_URL}/" class="back">← All flower delivery options</a>
</article>
<div class="related"><strong>More Flower Delivery Sites:</strong><br><br>{related_links}</div>
<footer>Affiliate links present. Commission may be earned at no cost to you. © {year} SendFlowersOnline</footer>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✅ Blog: {filename}")
    generated_files.append(filename)
    return filename

# ─────────────────────────────────────────────
# 2. CITY LANDING PAGES — 5 per day
# ─────────────────────────────────────────────
def make_city_page(city, idx):
    slug = city_slug(city)
    filename = f"flowers-{slug}.html"

    # Always refresh city pages (they benefit from updated dates)
    intro = pick(CITY_INTROS, idx + 7).format(city=city)

    occ_cards = "\n".join([
        f'<a href="{AFF_URL}" class="occ-card" target="_blank" rel="nofollow sponsored noopener">'
        f'<span>{o["emoji"]}</span><strong>{o["name"]}</strong></a>'
        for o in OCCASIONS
    ])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Flower Delivery {city} — Free Same-Day | SendFlowersOnline</title>
<meta name="description" content="Send flowers to {city} with free same-day delivery. $0 service fees. From $29.99. 4.8 stars. Order by 2 PM for delivery today.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{BASE_URL}/{filename}">
<meta name="geo.placename" content="{city}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"LocalBusiness",
  "name":"SendFlowersOnline — {city}",
  "description":"Free same-day flower delivery in {city}. $0 fees. From $29.99.",
  "url":"{BASE_URL}/{filename}",
  "areaServed":{{"@type":"City","name":"{city}"}},
  "aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"18742"}}
}}
</script>
<style>{SHARED_CSS}
.hero{{background:linear-gradient(135deg,#1a1a2e,#4a1535);color:#fff;text-align:center;padding:64px 5%;}}
.hero h1{{font-size:clamp(2rem,5vw,3.5rem);font-weight:800;margin-bottom:14px;line-height:1.1;}}
.hero p{{font-size:1.1rem;color:rgba(255,255,255,.72);max-width:500px;margin:0 auto 30px;}}
.hero-btn{{background:#FF2E63;color:#fff;padding:18px 42px;border-radius:99px;font-size:1.1rem;font-weight:700;text-decoration:none;display:inline-block;transition:all .2s;}}
.hero-btn:hover{{background:#c8365a;transform:translateY(-2px);}}
.trust{{display:flex;justify-content:center;gap:24px;flex-wrap:wrap;padding:20px 5%;background:#fff;border-bottom:1px solid var(--border);font-size:.85rem;font-weight:600;color:#555;}}
.occ-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;max-width:900px;margin:0 auto;}}
.occ-card{{background:#fff;border:1px solid var(--border);border-radius:14px;padding:20px 16px;text-align:center;text-decoration:none;color:#333;transition:all .2s;display:block;}}
.occ-card:hover{{border-color:#FF2E63;transform:translateY(-2px);}}
.occ-card span{{font-size:1.8rem;display:block;margin-bottom:6px;}}
.occ-card strong{{font-size:.9rem;}}
.sec{{max-width:900px;margin:0 auto;padding:56px 5%;}}
h2{{font-size:1.8rem;color:#1a1a1a;margin-bottom:28px;font-weight:800;}}
.back{{display:block;text-align:center;margin-top:24px;font-size:.85rem;color:var(--brand);text-decoration:none;}}
</style>
</head>
<body>
<nav class="nav">SendFlowersOnline <a href="{BASE_URL}/">← Home</a></nav>
<div class="hero">
  <h1>Flower Delivery {city} 🌷</h1>
  <p>{intro}</p>
  <a href="{AFF_URL}" class="hero-btn" target="_blank" rel="nofollow sponsored noopener">Send Flowers to {city} Today →</a>
</div>
<div class="trust">
  <span>🚚 Free Same-Day Delivery</span>
  <span>💳 $0 Service Fees</span>
  <span>⭐ 4.8/5 Stars</span>
  <span>🌸 Farm-Fresh Flowers</span>
</div>
<div class="sec">
  <h2>Shop by Occasion — Delivered to {city}</h2>
  <div class="occ-grid">{occ_cards}</div>
</div>
<div class="sec" style="padding-top:0">
  <div class="cta-box">
    <h2>Send Flowers to {city} Today 🌷</h2>
    <p>Free same-day delivery · From $29.99 · $0 fees · 4.8★</p>
    <a href="{AFF_URL}" class="cta-btn" target="_blank" rel="nofollow sponsored noopener">Order Now — Free Delivery</a>
    <div class="trust-row">
      <span>✓ FREE DELIVERY</span><span>✓ $0 FEES</span><span>✓ SAME DAY</span><span>✓ LIVE TRACKING</span>
    </div>
  </div>
  <a href="{BASE_URL}/" class="back">← All flower delivery options</a>
</div>
<div class="related"><strong>More Flower Delivery Sites:</strong><br><br>{related_links}</div>
<footer>Affiliate links present. Commission may be earned at no cost to you. © {year} SendFlowersOnline</footer>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✅ City: {filename}")
    generated_files.append(filename)
    return filename

# ─────────────────────────────────────────────
# 3. BLOG INDEX PAGE
# ─────────────────────────────────────────────
def make_blog_index():
    blog_files = sorted(
        [f for f in os.listdir(".") if f.startswith("blog-") and f.endswith(".html")],
        reverse=True
    )[:60]  # show last 60 posts

    items = ""
    for bf in blog_files:
        parts = bf.replace(".html", "").split("-")
        label = bf.replace(".html", "").replace("-", " ").title()
        items += f'<li><a href="{BASE_URL}/{bf}">{label}</a></li>\n'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Flower Delivery Blog — City Guides & Occasion Tips | SendFlowersOnline</title>
<meta name="description" content="Flower delivery guides for every city and occasion. Same-day delivery tips, local florist info, and more. Updated daily.">
<link rel="canonical" href="{BASE_URL}/blog.html">
<style>{SHARED_CSS}
.wrap{{max-width:800px;margin:0 auto;padding:48px 24px;}}
h1{{font-size:2.2rem;color:#1a1a1a;margin-bottom:8px;}}
.sub{{color:#888;margin-bottom:32px;font-size:.95rem;}}
ul{{list-style:none;display:grid;gap:8px;}}
li a{{display:block;padding:12px 16px;background:#fff;border:1px solid var(--border);border-radius:10px;color:#333;text-decoration:none;font-size:.92rem;transition:all .2s;}}
li a:hover{{border-color:#FF2E63;color:#FF2E63;}}
</style>
</head>
<body>
<nav class="nav">SendFlowersOnline <a href="{BASE_URL}/">← Home</a></nav>
<div class="wrap">
  <h1>🌷 Flower Delivery Blog</h1>
  <p class="sub">City guides, occasion tips, and same-day delivery advice. Updated daily.</p>
  <ul>{items}</ul>
</div>
<div class="related"><strong>More Flower Delivery Sites:</strong><br><br>{related_links}</div>
<footer>Affiliate links present. © {year} SendFlowersOnline</footer>
</body>
</html>"""

    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✅ Blog index: blog.html")

# ─────────────────────────────────────────────
# 4. SITEMAP
# ─────────────────────────────────────────────
def make_sitemap():
    all_html = sorted([f for f in os.listdir(".") if f.endswith(".html")])
    urls = "\n".join([
        f"  <url><loc>{BASE_URL}/{f}</loc><lastmod>{date_str}</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>"
        for f in all_html
    ])
    # Homepage gets higher priority
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{BASE_URL}/</loc><lastmod>{date_str}</lastmod><changefreq>daily</changefreq><priority>1.0</priority></url>
  <url><loc>{BASE_URL}/blog.html</loc><lastmod>{date_str}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>
{urls}
</urlset>"""
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("  ✅ Sitemap: sitemap.xml")

# ─────────────────────────────────────────────
# MAIN — RUN EVERYTHING
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\n🌷 Vulture Master Engine — {date_str}")
    print("=" * 48)

    # 3 blog posts — different city/occasion combos each day
    print("\n📝 Generating blog posts...")
    for i in range(3):
        city     = CITIES[(seed + i * 7) % len(CITIES)]
        occasion = OCCASIONS[(seed + i * 3) % len(OCCASIONS)]
        make_blog_post(city, occasion, i)

    # 5 city landing pages
    print("\n🏙️ Generating city pages...")
    for i in range(5):
        city = CITIES[(seed + i * 11 + 100) % len(CITIES)]
        make_city_page(city, i)

    # Blog index + sitemap
    print("\n📋 Updating index and sitemap...")
    make_blog_index()
    make_sitemap()

    print(f"\n✅ Done — {len(generated_files)} new files generated")
    print(f"🔗 Affiliate URL active: {AFF_URL}")
