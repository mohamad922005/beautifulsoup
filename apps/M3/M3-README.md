# Technical Brief: SoupReplacer API (Milestone 2 vs. Milestone 3)
1. Purpose of This Brief

This brief advises our team on whether to continue using the Milestone 2 SoupReplacer API or adopt the redesigned Milestone 3 API for future extensions to BeautifulSoup. It summarizes the differences, evaluates strengths and weaknesses, and presents a recommendation.

2. Comparison: Milestone 2 vs. Milestone 3
Milestone 2 – Static Tag Renaming

API:

SoupReplacer(og_tag, alt_tag)


Capabilities:

Replaces one specific tag name with another during parsing.

Limitations:

Only renames tags — cannot modify attributes.

Only supports one fixed replacement rule.

No access to tag context or content.

Not scalable for real document transformations (sanitizers, normalizers, converters).

Milestone 3 – General Transformation API

API:

SoupReplacer(
    name_xformer=lambda tag: ...,
    attrs_xformer=lambda tag: ...
)


Capabilities:

Modify tag names dynamically.

Modify attributes dynamically.

Can apply conditional rules based on tag content, attributes, or position.

Enables expressive transformations like:

attribute normalization

HTML sanitization

style migration

accessibility overlays

XML to HTML conversions

Tradeoffs:

Slight performance overhead due to two function calls per tag creation.

More complexity requires disciplined design.

3. Why Milestone 3 Is Stronger

Milestone 3 fits real-world use cases where HTML must be rewritten or sanitized.
It separates parsing from transformation, which is a clean and extensible architectural boundary.

Key improvements:

Full control over tag mutation.

More reusable and future-proof.

Integrates well with existing BeautifulSoup internals.

Eliminates the need to modify the library again for future extensions.

This generalizes the transformation step and prevents “API sprawl” where many special-case functions accumulate.

4. Recommendation to the Team

I recommend that our team adopts the Milestone 3 SoupReplacer API as the standard going forward.

Reasons:

Flexibility: It handles all use cases that Milestone 2 supported and many more.

Scalability: Supports complex rule sets without API redesign.

Maintainability: Clean separation of concerns; transformations remain outside core parsing code.

Performance: Additional cost is minimal compared to the cost of parsing itself.

Future-proof: Suitable for advanced applications such as HTML sanitization, automated cleanup, accessibility processing, and document conversion tasks.

5. Conclusion

Milestone 3 represents a meaningful evolution toward a modern, extensible HTML transformation mechanism. Its flexibility and alignment with BeautifulSoup’s architecture make it the better long-term choice. For these reasons, I advise adopting the Milestone 3 API as our recommended transformation mechanism in future extensions.