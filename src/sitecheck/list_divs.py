"""
List all the div tags in a page
"""

import sys

import requests
from bs4 import BeautifulSoup


def list_divs(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div")
    return [div.get("class") for div in divs]


if __name__ == "__main__":
    # Check for a command line argument
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com/"
    divs = list_divs(url)

    if divs is not None:
        print(f"Found {len(divs)} divs on the page {url}:")
        for div in divs:
            print(div)
    else:
        print(f"Failed to fetch the HTML content from {url}")
