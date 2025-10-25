# test_replacer.py
# Unit tests for the new SoupReplacer API

import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer


def test_replaces_specified_tag_during_parsing():
    """Verify that all <b> tags are replaced with <blockquote> during parsing."""
    html = "<html><body><b>Hello</b><b>World</b></body></html>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tags = [t.name for t in soup.find_all(True)]

    assert tags == ["html", "body", "blockquote", "blockquote"], \
        "SoupReplacer did not replace <b> tags correctly."


def test_does_not_affect_other_tags():
    """Verify that SoupReplacer only changes the specified tag and leaves others intact."""
    html = "<div><b>Bold</b><i>Italic</i><u>Underline</u></div>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.find("blockquote") is not None, "Missing <blockquote> after replacement."
    assert soup.find("i") is not None, "<i> tag was incorrectly modified."
    assert soup.find("u") is not None, "<u> tag was incorrectly modified."
