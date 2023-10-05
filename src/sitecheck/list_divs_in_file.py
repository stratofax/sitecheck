"""
List all the div tags in a HTML file
"""

import sys

from bs4 import BeautifulSoup


def list_divs_in_file(html):
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all("div")
    return [div.get("class") for div in divs]


if __name__ == "__main__":
    # Check for a command line argument
    filename = sys.argv[1] if len(sys.argv) > 1 else "index.html"

    # read the HTML file
    with open(filename, "r") as f:
        html = f.read()

    divs = list_divs_in_file(html)

    if divs is not None:
        print(f"Found {len(divs)} divs on the page {filename}:")
        for div in divs:
            print(div)
    else:
        print(f"Failed to fetch the HTML content from {filename}")
