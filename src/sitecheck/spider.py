import requests
from bs4 import BeautifulSoup

OK = 200


def link_spider(url: str, links: set) -> int:
    page = requests.get(url)
    status = page.status_code
    if status == OK:
        soup = BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            # This doesn't work for site root links, like '/about.html'
            # if href and url in href:
            links.add(href)
    return status


if __name__ == "__main__":
    url = "https://example.com/"
    links = set()
    status = link_spider(url, links)
    if status == OK:
        print(f"Links found (response {status}):")
        for link in links:
            print(link)
    else:
        print(f"Could not fetch the page - response {status}")
