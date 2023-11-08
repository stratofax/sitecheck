"""
Extract the contents of the specified div
element by class in a HTML text stream

Args:
    div_class: The div class to extract content from.

Returns:
    str: The extracted content of the div element.

Examples:
    >>> div = "<div>This is some content</div>"
    >>> extract_div(div)
    'This is some content'
"""

import sys

from bs4 import BeautifulSoup


def extract_div(html: str, div_class: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", class_=div_class)
    return div.text if div else None


if __name__ == "__main__":  # pragma: no cover
    html = sys.stdin.read()
    try:
        div_class = sys.argv[1]
    except IndexError:
        print("ERROR: No div class specified.", file=sys.stderr)
        exit(1)

    print(f"Extracting div with class: {div_class}")
    div = extract_div(html, div_class)

    if div is None:
        print(f"ERROR: Div not found: {div_class}.", file=sys.stderr)
        exit(2)
    else:
        print(div)
