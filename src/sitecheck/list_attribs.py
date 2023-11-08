import argparse
import sys

from bs4 import BeautifulSoup


def find_elements(html: str, element: str) -> list:
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all(element)


def find_attribs(elements: list, attrib: str) -> list:
    return [
        element.get(attrib) for element in elements if element.get(attrib) is not None
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find elements and their attributes in HTML."
    )
    parser.add_argument("element", help="The HTML element to find.")
    parser.add_argument(
        "attrib", nargs="?", default="", help="The attribute of the element to find."
    )
    args = parser.parse_args()

    html = sys.stdin.read()
    elements = find_elements(html, args.element)
    if args.attrib:
        elements = find_attribs(elements, args.attrib)
    for element in elements:
        print(element)
