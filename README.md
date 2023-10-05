# sitecheck

Tools to check a website and create reports on the site's health.

## Install and run this code

We use poetry to manage our dependencies in this project.

After you've cloned this repo onto your local machine, run:

```bash
cd /path/to/sitecheck-repo/
poetry install
cd /src/sitecheck
poetry run python spider.py
```

## spider.py

Extracts a list of unique links from the specified page.

## list_divs.py
