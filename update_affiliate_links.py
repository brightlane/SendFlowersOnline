import os
import re

# ── What to fix ──────────────────────────────────────────────────────────────
CORRECT_ID   = "2013017799"
CORRECT_BASE = "https://www.floristone.com/main.cfm"

# Any wrong affiliate IDs found in the old script or pages
WRONG_IDS = ["21885", "2188", "0000"]   # add more if you spot others

# Wrong base URLs to replace
WRONG_BASES = [
    "https://www.floristone.com/main.cfm",   # keep in case params differ
    "http://www.floristone.com/main.cfm",
    "www.floristone.com/main.cfm",
]

# Wrong occ= values → correct ones
OCC_MAP = {
    "occ=md":   "occ=md",    # mothers-day  (may already be right)
    "occ=sy":   "occ=sy",    # sympathy
    "occ=bd":   "occ=bd",    # birthday
    "occ=gw":   "occ=gw",    # get-well
    "occ=an":   "occ=an",    # anniversary
    "occ=ro":   "occ=ro",    # romance
    "occ=ty":   "occ=ty",    # thank-you
    "occ=nb":   "occ=nb",    # new-baby
    "occ=xm":   "occ=xm",    # christmas
    # common wrong alias
    "occ=cm":   "occ=cm",    # generic / catch-all
}

# The source_id and affiliate param must always be present
REQUIRED_PARAMS = f"source_id=aff&affiliate_id={CORRECT_ID}"
# ─────────────────────────────────────────────────────────────────────────────

EXTENSIONS = (".html", ".js")
fixed = 0

for root, dirs, files in os.walk("."):
    # skip hidden dirs like .git
    dirs[:] = [d for d in dirs if not d.startswith(".")]

    for filename in files:
        if not any(filename.endswith(ext) for ext in EXTENSIONS):
            continue

        filepath = os.path.join(root, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            original = content

            # 1. Replace every wrong affiliate ID with the correct one
            for wid in WRONG_IDS:
                content = content.replace(f"affiliate_id={wid}", f"affiliate_id={CORRECT_ID}")
                content = content.replace(f"aff_id={wid}",       f"affiliate_id={CORRECT_ID}")
                content = content.replace(f"aid={wid}",           f"affiliate_id={CORRECT_ID}")
                # bare ID sitting in a URL query string
                content = re.sub(
                    rf'([\?&])({re.escape(wid)})([&"\s])',
                    rf'\g<1>{CORRECT_ID}\g<3>',
                    content
                )

            # 2. Make sure every floristone link has the correct params
            #    Pattern: floristone.com/main.cfm?... (capture existing query)
            def fix_floristone_url(m):
                query = m.group(1)
                # ensure affiliate_id is correct
                query = re.sub(r'affiliate_id=\d+', f'affiliate_id={CORRECT_ID}', query)
                if 'affiliate_id=' not in query:
                    query = query.rstrip('&') + f'&affiliate_id={CORRECT_ID}'
                # ensure source_id=aff is present
                if 'source_id=' not in query:
                    query = query.rstrip('&') + '&source_id=aff'
                return f"https://www.floristone.com/main.cfm?{query}"

            content = re.sub(
                r'https?://(?:www\.)?floristone\.com/main\.cfm\?([^"\'>\s]+)',
                fix_floristone_url,
                content
            )

            if content != original:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Fixed: {filepath}")
                fixed += 1
            else:
                print(f"No change: {filepath}")

        except Exception as e:
            print(f"Skipped {filepath}: {e}")

print(f"\nDone. Fixed {fixed} file(s). Affiliate ID is now {CORRECT_ID} everywhere.")
