import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    print("Usage: python task4.py <html_file>")
    sys.exit(1)

filename = sys.argv[1]

# Use a SoupStrainer that simply allows all tags, then filter by id in one call
only_tags = SoupStrainer(True)

with open(filename, "r", encoding="utf-8") as f:
    # 'html.parser' is stable for this task
    soup = BeautifulSoup(f, "html.parser", parse_only=only_tags)

# ✅ Single API call: find all tags that have id attributes
for tag in soup.find_all(True, id=True):
    print(f"{tag.name} → id={tag['id']}")
