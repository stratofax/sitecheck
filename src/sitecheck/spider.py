import requests
from bs4 import BeautifulSoup

OK = 200


def link_spider(url: str, links: set) -> int:
    """
    Fetch a page and extract all links from it,
    returning the status code.
    """
    page = requests.get(url)
    status = page.status_code
    if status == OK:
        soup = BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            links.add(href)
    return status


if __name__ == "__main__":
    # Test the spider

    # Check for a command line argument
    import sys

    # use default URL if no argument is given
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com/"

    links = set()
    status = link_spider(url, links)
    print(f"Status code: {status}")
    if status == OK:
        print(
            f"Found {len(links)} unique links on page {url}:"
        )
        for link in links:
            print(link)
    else:
        print("Could not fetch the page")
