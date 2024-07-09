"""
Remove the specified element from HTML
"""

import sys

from bs4 import BeautifulSoup


def remove_element(html: str, elements) -> str:
    """
    Remove the specified element from HTML.

    Args:
        html (str): The HTML content.
        elements: The elements to be removed from the HTML.

    Returns:
        str: The modified HTML content with the specified elements removed.
    """
    soup = BeautifulSoup(html, "html.parser")
    for element in elements:
        for tag in soup.find_all(element):
            tag.decompose()

    return soup.decode_contents()


if __name__ == "__main__":  # pragma: no cover
    html = sys.stdin.read()
    remove_elements = sys.argv[1:]
    clean_html = remove_element(html, remove_elements)
    print(clean_html)
