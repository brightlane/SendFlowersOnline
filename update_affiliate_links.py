import os
import re

# Correct affiliate ID and URL
OLD_IDS = ["2013017799", "YOUR_AFFILIATE_ID_PLACEHOLDER"]
CORRECT_ID = "21885"
OLD_URL = "index.cfm"
CORRECT_URL = "main.cfm"
OLD_OCC = "occ=sd"
CORRECT_OCC = "occ=md"

fixed = 0
for filename in os.listdir("."):
    if not filename.endswith(".html") and not filename.endswith(".py") and not filename.endswith(".js"):
        continue
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        original = content
        for old_id in OLD_IDS:
            content = content.replace(old_id, CORRECT_ID)
        content = content.replace(OLD_URL, CORRECT_URL)
        content = content.replace(OLD_OCC, CORRECT_OCC)
        if content != original:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed: {filename}")
            fixed += 1
    except Exception as e:
        print(f"Skipped {filename}: {e}")

print(f"\nDone. Fixed {fixed} files. Affiliate ID is now 21885 everywhere.")
