import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    print("Usage: python task2.py <html_file>")
    sys.exit(1)

filename = sys.argv[1]

# Parse only <a> tags
only_a_tags = SoupStrainer("a")

with open(filename, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", parse_only=only_a_tags)

# Print all hyperlinks
for link in soup.find_all("a", href=True):
    print(link["href"])
