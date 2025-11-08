# SWE262 – BeautifulSoup Project (Milestone 2)

This repository contains the work for **Milestone 2** of the SWE262 course project, where we extend the BeautifulSoup library with optimized parsing features and a new API (`SoupReplacer`).

---

## Repository Structure

```
beautifulsoup/
│
├── bs4/                            # Library source code (edited)
│   ├── __init__.py                 # Modified to integrate SoupReplacer
│   ├── filter.py                   # Added SoupReplacer class
│   ├── element.py
│   ├── tests/                      # New tests for milestone 2
│   │   └── test_replacer.py
│
├── apps/
│   └── Milestone-2/                # Application scripts
│       ├── task2.py                # Prints all <a> tags (hyperlinks)
│       ├── task3.py                # Prints all tags
│       ├── task4.py                # Prints all tags with id attributes
│       ├── task6.py                # Uses new SoupReplacer API
│       ├── large.html              # Sample test file
│       └── large_with_id.html      # Sample test file with id attributes
│
└── README.md                       # This file
```

---

##  Milestone-2 Overview

This milestone explores **BeautifulSoup API optimization** using `SoupStrainer` and introduces a new in-library API — `SoupReplacer`.

###  Implemented Features

- **`SoupStrainer` optimization**
  - Used in `task2.py`, `task3.py`, and `task4.py` to parse only parts of HTML files.
  - Improves performance by avoiding full-tree parsing.

- **`SoupReplacer(og_tag, alt_tag)`**
  - Implemented inside `bs4/filter.py`
  - Replaces tags *during parsing* (e.g., `<b>` → `<blockquote>`).
  - Integrated via `handle_starttag()` in `bs4/__init__.py`.

- **Unit Tests**
  - Created in `bs4/tests/test_replacer.py`
  - Verify that:
    - All specified tags are replaced during parsing.
    - Unrelated tags remain unchanged.

---

## Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/mohamad922005/beautifulsoup.git
   cd beautifulsoup
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install beautifulsoup4 lxml pytest
   ```

---

## Running the Application Scripts

Each script is inside `apps/Milestone-2`.

### 🔹 Task 2 — Print all hyperlinks (`<a>` tags)
```bash
python apps/Milestone-2/task2.py apps/Milestone-2/large.html
```

### 🔹 Task 3 — Print all tags in the document
```bash
python apps/Milestone-2/task3.py apps/Milestone-2/large.html
```

### 🔹 Task 4 — Print all tags that have an id attribute
```bash
python apps/Milestone-2/task4.py apps/Milestone-2/large_with_id.html
```

### 🔹 Task 6 — Replace `<b>` tags with `<blockquote>` using SoupReplacer
```bash
python apps/Milestone-2/task6.py apps/Milestone-2/large.html
```

Expected output:
```
 Using BeautifulSoup from: ...\bs4\__init__.py
Replacement done during parsing → task6_replacer_output.html
```

---

##  Running Tests

Run from the project root:
```bash
pytest bs4/tests/test_replacer.py -v
```

You should see:
```
============================= test session starts =============================
collected 2 items

bs4/tests/test_replacer.py::test_replaces_specified_tag_during_parsing PASSED
bs4/tests/test_replacer.py::test_does_not_affect_other_tags PASSED
============================== 2 passed in 0.03s ==============================
```

---

##  Tag & Release Info

**Git tag:** `milestone-2`  
**Release includes:**
- `SoupReplacer` API (in `bs4/filter.py`)
- Integrated `handle_starttag()` logic
- Application tasks 2, 3, 4, 6
- Unit tests in `bs4/tests/test_replacer.py`
- Project documentation (`README.md`)

---

*Milestone 2 completed successfully and tagged as `milestone-2`.*
