import unittest

from bs4 import BeautifulSoup, Tag, NavigableString


class TestIterableSoup(unittest.TestCase):
    def test_iter_equals_descendants(self):
        """Iterating over soup yields exactly the same sequence as soup.descendants."""
        html = "<div><p>One</p><p>Two<b>Bold</b></p></div>"
        soup = BeautifulSoup(html, "html.parser")

        iter_nodes = list(soup)
        desc_nodes = list(soup.descendants)

        self.assertEqual(iter_nodes, desc_nodes)

    def test_empty_document_yields_no_nodes(self):
        """Empty markup should give an empty iteration."""
        soup = BeautifulSoup("", "html.parser")
        self.assertEqual(list(soup), [])

    def test_iteration_yields_tags_and_strings(self):
        """Iteration should include both Tag and NavigableString nodes."""
        html = "<div><p>One</p><p>Two<b>Bold</b></p></div>"
        soup = BeautifulSoup(html, "html.parser")

        nodes = list(soup)
        self.assertTrue(any(isinstance(n, Tag) for n in nodes))
        self.assertTrue(any(isinstance(n, NavigableString) for n in nodes))

    def test_iteration_reflects_tree_modifications(self):
        """If the tree is modified after parsing, iteration sees the new nodes."""
        html = "<div><p>One</p></div>"
        soup = BeautifulSoup(html, "html.parser")

        div = soup.find("div")
        span = soup.new_tag("span")
        span.string = "New"
        div.append(span)

        tag_names = [n.name for n in list(soup) if isinstance(n, Tag)]
        self.assertIn("span", tag_names)

    def test_iter_returns_iterator(self):
        """Calling iter(soup) returns an iterator object that can be consumed."""
        html = "<p>Hello</p>"
        soup = BeautifulSoup(html, "html.parser")

        it = iter(soup)
        self.assertIsNotNone(next(it, None))  # can get at least one node
        # After consuming all nodes, further next() calls should yield None
        while next(it, None) is not None:
            pass
        self.assertIsNone(next(it, None))


if __name__ == "__main__":
    unittest.main()
