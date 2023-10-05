from bs4 import BeautifulSoup


def html_link_spider(html: str, links: set) -> int:
    """
    Extract all links from an HTML page,
    returning a set of unique links.
    """

    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        links.add(href)
    return links


if __name__ == "__main__":
    # Test the spider

    # Check for a command line argument
    import sys

    # use default URL if no argument is given

    filename = sys.argv[1] if len(sys.argv) > 1 else "index.html"

    # read the HTML file
    with open(filename, "r") as f:
        html = f.read()

    links = set()
    status = html_link_spider(html, links)
    print(
        f"Found {len(links)} unique links on page {filename}:"
    )
    for link in links:
        print(link)
