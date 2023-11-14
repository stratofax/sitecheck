"""
Write HTML meta data to JSON from Cadent web files
"""

import json
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
    tags = [tag.text for tag in soup.find_all("a", attrs={"rel": "tag"})]
    # write post_title to post_title.txt
    # write post_date to post_date.txt
    # write tags to tags.txt
    with open("post_title.txt", "w") as f:
        f.write(post_title)
    with open("post_date.txt", "w") as f:
        f.write(post_date)
    with open("tags.txt", "w") as f:
        for tag in tags:
            f.write(f"{tag},")

    return {"post_title": post_title, "post_date": post_date, "tags": tags}


if __name__ == "__main__":  # pragma: no cover
    with sys.stdin as html:
        metadata = parse_meta(html.read())
    print(json.dumps(metadata, indent=4))
