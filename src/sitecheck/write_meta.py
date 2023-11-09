"""
Write HTML meta data to JSON
"""

import sys

from bs4 import BeautifulSoup


def clean_title(title: str) -> str:
    # remove ' – Cadent' from the end of the title
    # note that the '–' character is not a dash!
    return title.replace(" – Cadent", "")


def parse_meta(html: str):
    soup = BeautifulSoup(html, "html.parser")
    post_title = clean_title(soup.title.string)
    post_date = soup.time["datetime"]

    return {"post_title": post_title, "post_date": post_date}


if __name__ == "__main__":  # pragma: no cover
    with sys.stdin as html:
        print(parse_meta(html.read()))
