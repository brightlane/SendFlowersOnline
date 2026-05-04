import math
import os
import json
import shutil
from datetime import datetime
from urllib.parse import quote

def generate_vulture_system():
    CHUNK_SIZE = 45000
    BASE_URL = "https://brightlane.github.io/SameDayFlowers"
    SITEMAP_DIR = "sitemaps"
    PAGE_DIR = "blog"
    TODAY = datetime.now().strftime("%Y-%m-%d")

    # 🔗 YOUR LINKS (intact)
    MANYCHAT = "https://m.me/brightlane?ref=nwkkk7vkps17"
    AFFILIATE = "http://www.floristone.com/main.cfm?source_id=aff&AffiliateID=2013017799&occ=mothersday"

    # Reset dirs
    for d in [SITEMAP_DIR, PAGE_DIR]:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)

    # Load data
    with open('cities.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Deduplicate
    seen = set()
    clean = []
    for item in data:
        city = item.get('city', '').strip()
        state = item.get('state', '').strip()
        key = f"{city.lower()}-{state.lower()}"
        if city and state and key not in seen:
            seen.add(key)
            clean.append({"city": city, "state": state})

    total = len(clean)
    parts = math.ceil(total / CHUNK_SIZE)
    child_files = []

    # --- PAGE TEMPLATE (includes routing logic) ---
    def build_page(city, state, slug):
        return f"""<!DOCTYPE html>
<html>
<head>
  <title>Same Day Flowers in {city}, {state}</title>
  <meta name="description" content="Order same day flower delivery in {city}, {state}. Mother's Day specials available.">
</head>
<body>
  <h1>Same Day Flowers in {city}, {state}</h1>
  <button onclick="routeUser()">Order Flowers 🌸</button>

<script>
const MANYCHAT = "{MANYCHAT}";
const AFFILIATE = "{AFFILIATE}";

function routeUser() {{
  const now = new Date();
  const panicStart = new Date("2026-05-07");
  const panicEnd = new Date("2026-05-10");

  let url = AFFILIATE;

  // Panic window → send to ManyChat first
  if (now >= panicStart && now <= panicEnd) {{
    url = MANYCHAT;
  }}

  // 40% traffic → ManyChat
  if (Math.random() < 0.4) {{
    url = MANYCHAT;
  }}

  window.location.href = url;
}}
</script>

</body>
</html>"""

    # --- GENERATE SITEMAPS ---
    for i in range(parts):
        filename = f"part-{i+1}.xml"
        child_files.append(filename)

        start = i * CHUNK_SIZE
        end = (i + 1) * CHUNK_SIZE
        chunk = clean[start:end]

        with open(os.path.join(SITEMAP_DIR, filename), "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

            for item in chunk:
                city_slug = quote(item['city'].lower().replace(' ', '-'))
                state_slug = quote(item['state'].lower())
                slug = f"flowers-{city_slug}-{state_slug}.html"

                loc = f"{BASE_URL}/{PAGE_DIR}/{slug}"

                # Write sitemap entry
                f.write(f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>\n")

                # --- GENERATE PAGE ---
                page_html = build_page(item['city'], item['state'], slug)
                with open(os.path.join(PAGE_DIR, slug), "w", encoding="utf-8") as p:
                    p.write(page_html)

            f.write('</urlset>')

        print(f"Created {filename}")

    # --- INDEX FILE ---
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for child in child_files:
            f.write(f"<sitemap><loc>{BASE_URL}/{SITEMAP_DIR}/{child}</loc></sitemap>\n")

        f.write('</sitemapindex>')

    print("\n--- SYSTEM COMPLETE ---")
    print(f"Pages: {total}")
    print(f"Sitemaps: {parts}")
    print("Affiliate + ManyChat routing: ACTIVE")
    print("-------------------------")


if __name__ == "__main__":
    generate_vulture_system()
