# test_replacer_v3.py
# Unit tests for the extended SoupReplacer API (Milestone 3)

import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer


def test_name_xformer_replaces_tag_name():
    """Verify that name_xformer renames tags dynamically."""
    html = "<html><body><b>Hello</b><i>World</i></body></html>"
    replacer = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
    )
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tags = [t.name for t in soup.find_all(True)]
    assert "blockquote" in tags
    assert "b" not in tags


def test_attrs_xformer_adds_class_attribute():
    """Ensure attrs_xformer can modify attributes (add class='test')."""
    def add_class(tag):
        if tag.name == "p":
            return {**tag.attrs, "class": "test"}
        return tag.attrs

    html = "<p>para1</p><p>para2</p>"
    replacer = SoupReplacer(attrs_xformer=add_class)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    for p in soup.find_all("p"):
        assert p.get("class") == ["test"] or p.get("class") == "test"


def test_xformer_removes_class_attribute():
    """Ensure xformer can remove a specific attribute by side effect."""
    def remove_class(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    html = '<div class="x"></div><p class="y"></p>'
    replacer = SoupReplacer(xformer=remove_class)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    for tag in soup.find_all(True):
        assert "class" not in tag.attrs


def test_combined_name_and_attrs_transformers():
    """Verify combined name_xformer and attrs_xformer work together."""
    def rename(tag):
        return "section" if tag.name == "div" else tag.name

    def add_id(tag):
        return {**tag.attrs, "id": "test-id"}

    html = "<div></div>"
    replacer = SoupReplacer(name_xformer=rename, attrs_xformer=add_id)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tag = soup.find("section")
    assert tag is not None
    assert tag.get("id") == "test-id"


def test_no_transformations_when_none_specified():
    """Verify that tags remain unchanged when no transformers are provided."""
    html = "<b>hi</b><p>bye</p>"
    replacer = SoupReplacer()  # no args
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("b") is not None
    assert soup.find("p") is not None


def test_m2_backward_compatibility_still_works():
    """Ensure old (og_tag, alt_tag) constructor remains functional."""
    html = "<b>bold</b>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("blockquote") is not None
    assert soup.find("b") is None
