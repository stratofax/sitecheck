"""
Extract the contens of the specified div tag in a HTML file
"""

import sys

from bs4 import BeautifulSoup


def scrape_div(html: str, div_class: str, remove_divs: str = None) -> str:
    soup = BeautifulSoup(html, "html.parser")
    # Find the div
    div = soup.find("div", class_=div_class)
    title = soup.title.string

    # Remove the specified div tag if it exists
    if remove_divs is not None:
        for div_to_remove in remove_divs:
            remove_this = div.find("div", class_=div_to_remove)
            while remove_this is not None:
                remove_this.extract()
                remove_this = div.find("div", class_=div_to_remove)

    new_body = div.decode_contents()

    return (
        f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
        f"<title>{title}</title></head>"
        f"<body>{new_body}</body></html>"
    )


if __name__ == "__main__":
    # Check for a command line argument
    filename = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    div_class = sys.argv[2] if len(sys.argv) > 2 else None
    remove_divs = sys.argv[3:] if len(sys.argv) > 3 else None

    # If div_class is None, exit with message
    if div_class is None:
        print("Please provide a div class name.")
        exit(1)

    # read the HTML file
    with open(filename, "r") as f:
        html = f.read()

    div = scrape_div(html, div_class, remove_divs)

    if div is not None:
        print(div)
    else:
        print(f"Failed to fetch the HTML content from {filename}")
