# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Sitecheck is a Python-based web scraping and HTML analysis tool for extracting information from websites and HTML files. It creates reports on a site's structural and link health.

## Commands

```bash
# Install dependencies
poetry install

# Run scripts (from project root)
poetry run python src/sitecheck/spider.py [URL]           # Web crawler - extracts links from URL
poetry run python src/sitecheck/spider_file.py [file]     # Extract links from local HTML file
poetry run python src/sitecheck/list_divs.py [URL]        # List div classes from URL
poetry run python src/sitecheck/list_divs_in_file.py [file]  # List div classes from file
poetry run python src/sitecheck/scrape_div.py <file> <div_class> [divs_to_remove...]  # Extract div content

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

The project consists of standalone Python scripts in `src/sitecheck/`, each with a specific purpose:

| Script | Purpose | Input |
|--------|---------|-------|
| `spider.py` | Crawl web page, extract all links | URL |
| `spider_file.py` | Extract links from HTML file | File path |
| `list_divs.py` | List all div class attributes | URL |
| `list_divs_in_file.py` | List div classes from file | File path |
| `scrape_div.py` | Extract specific div content, optionally removing nested divs | File + class names |

**Design pattern:** Dual input methods - most functions have URL-based and file-based variants. All HTML parsing uses BeautifulSoup.

**Entry points:** Each script supports CLI execution with `if __name__ == "__main__"` blocks and sensible defaults.

## Dependencies

- **Runtime:** `requests` (HTTP), `beautifulsoup4` (HTML parsing)
- **Dev:** `black`, `flake8`, `isort`, `mypy`, `pytest`, `pytest-cov`
- **Python:** ^3.9
