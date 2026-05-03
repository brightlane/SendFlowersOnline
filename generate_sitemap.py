import os
import glob
from datetime import date

BASE_URL = "https://brightlane.github.io/SendFlowersOnline"
TODAY = date.today().isoformat()

# Priority rules by path/filename
def get_priority(filepath):
    if filepath == "index.html":
        return "1.0"
    if filepath in ("blog.html", "floristone_same_day_delivery.html"):
        return "0.9"
    if filepath == "404.html":
        return "0.3"
    if filepath.startswith("blog-"):
        return "0.7"
    return "0.8"  # bing/* pages

# Changefreq rules
def get_changefreq(filepath):
    if filepath == "index.html":
        return "daily"
    if filepath in ("blog.html", "floristone_same_day_delivery.html"):
        return "daily"
    if filepath == "404.html":
        return "monthly"
    if filepath.startswith("blog-"):
        return "never"
    return "weekly"

# Collect all HTML files
urls = []
for html_file in sorted(glob.glob("**/*.html", recursive=True)):
    # Skip any files in hidden dirs
    if any(part.startswith(".") for part in html_file.split(os.sep)):
        continue
    
    # Normalize path separators
    clean_path = html_file.replace("\\", "/")
    url = f"{BASE_URL}/{clean_path}"
    priority = get_priority(clean_path)
    changefreq = get_changefreq(clean_path)
    
    urls.append(f'  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>')

# Build sitemap
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += "\n".join(urls)
sitemap += "\n</urlset>"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print(f"✅ sitemap.xml generated with {len(urls)} URLs — dated {TODAY}")
