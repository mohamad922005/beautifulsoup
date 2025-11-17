# Technical Brief: Iterable BeautifulSoup API

1. Goal of Milestone 4

Milestone 4 extends the BeautifulSoup API by making the main BeautifulSoup object directly iterable.
This allows client code to traverse the entire parse tree in a streaming style:

soup = BeautifulSoup(html_doc, "html.parser")

for node in soup:
    print(node)


Iteration should:

yield every node in document order (Tags and NavigableStrings),

avoid constructing any intermediate list,

be lazy (nodes produced one-at-a-time rather than all upfront),

work seamlessly with the existing library design.

This milestone teaches stream-based APIs, efficient iteration, and extension of a pre-existing codebase.

2. Design Motivation

BeautifulSoup already provides a generator-based tree traversal through:

tag.descendants


descendants walks the tree using BeautifulSoup’s internal next_element linked structure.
This traversal is:

lazy

memory-efficient

already implemented and tested

guarantees document order

Instead of writing a new traversal algorithm, the most natural and consistent solution is to use the existing generator.

3. Implementation

The only required change is to override __iter__ inside the BeautifulSoup class in:

beautifulsoup/bs4/__init__.py


Implementation:

def __iter__(self):
    """
    Iterate over all nodes in document order using the existing
    descendants generator. This provides a streaming traversal of the
    tree without materializing intermediate lists.
    """
    return self.descendants


This makes the BeautifulSoup object itself iterable while preserving the original iteration behavior of Tag (which only iterates over direct children).

4. Why This Approach Is Correct
4.1 Streaming (Lazy) Traversal

The requirement explicitly says:

“Very important: you should not collect the nodes of the tree onto a list.”

self.descendants satisfies this by yielding nodes one at a time.

4.2 Efficient

There is no recursion and no list construction.
Traversal follows BeautifulSoup’s optimized next_element pointers.

4.3 Minimal and Consistent

The update integrates cleanly with the existing architecture:

No changes to the parser

No changes to tree nodes

No duplication of traversal logic

We simply expose an iterable interface that delegates to the built-in mechanism.

5. Unit Tests

A new file was added:

beautifulsoup/bs4/tests/test_iterable_soup.py


The 5 tests validate:

for node in soup matches list(soup.descendants)

Empty soup yields no nodes

Iteration includes both Tag and NavigableString

Modifying the tree after parsing updates the iteration results

iter(soup) returns a valid Python iterator

This confirms correct behavior across typical and edge cases.

6. Application Example

Placed in:

beautifulsoup/apps/m4/iterate_nodes.py


The script demonstrates that:

for node in soup:
    print(repr(node))


yields all nodes in document order, including whitespace and text nodes.
This verifies the streaming iteration in real usage.

7. Conclusion

Milestone 4 introduces a lightweight but powerful extension to BeautifulSoup:

It makes BeautifulSoup iterable.

It integrates with BeautifulSoup’s traversal infrastructure.

It exposes a natural Python interface (for node in soup).

It meets the project goals of learning stream-based API design.