from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <p>First</p>
    <div><span>Second</span></div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print("Iterating over all nodes:\n")
for node in soup:
    print(repr(node))
