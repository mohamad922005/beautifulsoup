# Milestone 2 Report

## Part 2 – API References
# Milestone 2 – Part 2: Exploring BeautifulSoup Source Code


| Function | File | Line Range 
|
| `BeautifulSoup() class` | __init__.py | 133-1152 
| `BeautifulSoup() Constructor 'init()'` | __init__.py | 209-309 
| `find_all()` | element.py | 2715-2748
| `find_parent()` | element.py | 992-1020 
| `select()` | element.py | 2799–2822 
| `prettify()` | element.py | 2601–2617 
| `get_text()` | element.py | 524-550 
| `SoupStrainer` | filter.py | 313-682
| `decompose()` | element.py | 635-655
| `has_attr()` | element.py | 2196-2198 |
| `get()` | element.py | 2160–2171 
| `filter()` | filter.py | 137-156  |


## How I Found These
Opened the extracted `beautifulsoup` folder in VS Code, used global search (`Ctrl + Shift + F`) to locate each function definition, and noted the line numbers shown in the search panel.


## Part 3 – New API: SoupReplacer
- Added `class SoupReplacer(og_tag, alt_tag)` inside `bs4/filter.py`.
- Updated `BeautifulSoup.__init__()` and `handle_starttag()` in `bs4/__init__.py`.
- Wrote tests in `bs4/tests/test_replacer.py`.
- Application: `apps/m2/task6.py` replaces `<b>` → `<blockquote>` during parsing.
