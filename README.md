# sitecheck

Tools to check a website and its pages by analyzing HTML code.

For more information about sitecheck, see the [FAQ](docs/FAQ.md).

## Install and run this code

This project uses `poetry` to manage its dependencies. To get started, install `poetry` for your system, as described in [the Introduction of the Poetry Documentation](https://python-poetry.org/docs/). Then clone this repo.

After you've cloned this repo onto your local machine:

```bash
cd /path/to/sitecheck-repo/
poetry install
```

## Usage

The modules read HTML from stdin and write to stdout, allowing them to be piped together:

```bash
# Read a file and list its div classes and ids
poetry run python src/sitecheck/read_file.py page.html | \
  poetry run python src/sitecheck/list_divs.py

# Extract a specific div and remove unwanted elements
poetry run python src/sitecheck/read_file.py page.html | \
  poetry run python src/sitecheck/extract_div.py main-content | \
  poetry run python src/sitecheck/remove_element.py script noscript > clean.html

# List all anchor href attributes
poetry run python src/sitecheck/read_file.py page.html | \
  poetry run python src/sitecheck/list_attribs.py a href
```

## Modules

| Module | Purpose |
|--------|---------|
| `read_file.py` | Read file contents to stdout |
| `list_divs.py` | List all div class and id attributes |
| `list_attribs.py` | Find elements and their attributes |
| `extract_div.py` | Extract content of a div by class |
| `remove_element.py` | Remove specified HTML elements |
