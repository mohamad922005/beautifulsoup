import sys, os

# Force Python to load the local BeautifulSoup implementation (not the global one)
sys.path.insert(0, os.path.abspath("C:/Users/user/OneDrive/Desktop/SWE262/Project/beautifulsoup"))

import bs4
print("Using BeautifulSoup from:", bs4.__file__)

from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer


# Part 1: Application Program (replaces <b> → <blockquote>)

def replace_during_parsing(input_file: str):
    """Reads an HTML file and replaces all <b> with <blockquote> DURING parsing."""
    output_file = "task6_replacer_output.html"

    with open(input_file, "r", encoding="utf-8") as f:
        html_doc = f.read()

    # Create replacer object
    b_to_blockquote = SoupReplacer("b", "blockquote")

    #  Use built-in parser instead of lxml
    soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f" Replacement done during parsing → {output_file}")


# Part 2: Simple test cases for SoupReplacer

def test_simple_replacement():
    """Test that <b> becomes <blockquote>."""
    html = "<b>Hello</b><b>World</b>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tags = [t.name for t in soup.find_all(True)]
    assert tags == ["blockquote", "blockquote"], " Replacement failed"
    print(" test_simple_replacement passed")


def test_mixed_tags():
    """Test that only the specified tag (<b>) is replaced."""
    html = "<div><b>Test</b><i>Keep</i></div>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("blockquote") is not None, " <b> not replaced"
    assert soup.find("i") is not None, " other tags missing"
    print(" test_mixed_tags passed")


# Main runner
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        replace_during_parsing(sys.argv[1])
    else:
        print("Running SoupReplacer tests...\n")
        test_simple_replacement()
        test_mixed_tags()
        print("\nAll tests passed.")
