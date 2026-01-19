# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Sitecheck is a Python-based HTML analysis tool for extracting and processing information from HTML files. It provides modular utilities that can be piped together Unix-style.

## Commands

```bash
# Install dependencies
poetry install

# Run scripts (from project root, using stdin)
poetry run python src/sitecheck/read_file.py <file>                      # Read file to stdout
poetry run python src/sitecheck/list_divs.py < file.html                 # List div classes/ids
poetry run python src/sitecheck/list_attribs.py <element> [attrib] < file.html  # List element attributes
poetry run python src/sitecheck/extract_div.py <div_class> < file.html   # Extract div content
poetry run python src/sitecheck/remove_element.py <elem>... < file.html  # Remove elements

# Piping example
poetry run python src/sitecheck/read_file.py page.html | \
  poetry run python src/sitecheck/extract_div.py content | \
  poetry run python src/sitecheck/remove_element.py script noscript

# Code quality
poetry run black src/sitecheck tests      # Format code
poetry run isort src/sitecheck tests      # Sort imports
poetry run flake8 src/sitecheck tests     # Lint
poetry run mypy src/sitecheck             # Type check

# Testing
poetry run pytest tests/
poetry run pytest --cov=src/sitecheck tests/  # With coverage
```

## Architecture

The project consists of modular Python scripts in `src/sitecheck/` that read HTML from stdin and write to stdout:

| Script | Purpose | Input |
|--------|---------|-------|
| `read_file.py` | Read file contents to stdout | File path argument |
| `list_divs.py` | List all div class and id attributes | stdin |
| `list_attribs.py` | Find elements and their attributes | stdin + element/attrib args |
| `extract_div.py` | Extract content of a div by class | stdin + class arg |
| `remove_element.py` | Remove specified HTML elements | stdin + element args |

**Design pattern:** Unix-style pipeline - modules read HTML from stdin and write to stdout, allowing them to be chained together.

**Entry points:** Each script supports CLI execution with `if __name__ == "__main__"` blocks.

## Dependencies

- **Runtime:** `requests` (HTTP), `beautifulsoup4` (HTML parsing)
- **Dev:** `black`, `flake8`, `isort`, `mypy`, `pytest`, `pytest-cov`
- **Python:** ^3.9
