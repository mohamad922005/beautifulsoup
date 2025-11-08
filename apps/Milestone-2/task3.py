import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    print("Usage: python task3.py <html_file>")
    sys.exit(1)

filename = sys.argv[1]

# Safe filter function — accepts variable arguments
def all_tags(name=None, attrs=None):
    return name is not None

# Create the SoupStrainer
only_tags = SoupStrainer(all_tags)

with open(filename, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml", parse_only=only_tags)

# Print all tag names
for tag in soup.find_all(True):
    print(tag.name)
