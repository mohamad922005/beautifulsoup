from bs4 import BeautifulSoup, SoupReplacer

def add_class_to_p(tag):
    """Adds class='test' to every <p> tag."""
    if tag.name == "p":
        tag.attrs["class"] = "test"

# Create the replacer
p_class_adder = SoupReplacer(xformer=add_class_to_p)

# Read test input HTML
input_path = "apps/M3/test_file.html"
output_path = "apps/M3/output_task7.html"

with open(input_path, "r", encoding="utf-8") as f:
    html_doc = f.read()

# Parse and transform during parsing
soup = BeautifulSoup(html_doc, "html.parser", replacer=p_class_adder)

# Write modified HTML to output
with open(output_path, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print(f"Transformed tree written to {output_path}")
