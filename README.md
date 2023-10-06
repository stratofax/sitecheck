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

Extracts a list of unique links from the URL provided.

## spider_file.py

Extracts a list of unique links from an HTML file.

## list_divs.py

Display a list of div classes found in the URL provided. Divs with multiple classes are displayed in a list.

## scrape_div.py

Extracts the contents of the specified `div` class from the file provided. Additional `div` classes will be removed.

Returns: A new HTML file with the extracted content as the `body` of the file.

Usage

```bash
cd /path/to/sitecheck-repo/
poetry run python list_divs.py <file> <div_class_to_extract> [div_class_to_remove1 div_class_to_remove2 ...]
```

Sample

```bash
cd /path/to/sitecheck/tests
poetry run python ../src/sitecheck/scrape_div.py index.html entry-content sharedaddy > output.html
```

This sample command, when executed in this repo's `tests` directory:

- runs `scrape_div.py` on the `index.html` file
- extracts the `entry-content` class from the `index.html` file
- removes the `sharedaddy` class from the extracted content
- writes the extracted content to `output.html`
