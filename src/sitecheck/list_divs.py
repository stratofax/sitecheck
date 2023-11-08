"""
List all the div classes and ids in a page
"""

import sys

from bs4 import BeautifulSoup


def list_div_attribs(html: str, attrib: str) -> list:
    """
    List all the div attributes in an HTML page.

    Args:
        html (str): The HTML content of the page.
        attrib (str): The attribute to find.

    Returns:
        list: A list of div attribs found in the page.
    """
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all("div")
    return [div.get(attrib) for div in divs if div.get(attrib) is not None]


def print_div_attribs(html: str, attrib: str) -> None:
    """
    Print all the div attributes in an HTML page.

    Args:
        html (str): The HTML content of the page.
        attrib (str): The attribute to find.
    """
    div_attribs = list_div_attribs(html, attrib)
    suffix = "es" if attrib == "class" else "s"
    print(f"Found {len(div_attribs)} named div {attrib}{suffix}.")
    for div in div_attribs:
        print(div)


if __name__ == "__main__":  # pragma: no cover
    html = sys.stdin.read()

    print_div_attribs(html, "class")
    print("\n")
    print_div_attribs(html, "id")
