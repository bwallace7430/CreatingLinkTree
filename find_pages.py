import requests
from bs4 import BeautifulSoup


def get_subpages(url, all_links):
    response = requests.get(url)
    try:
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        print(f"Unable to parse HTML for URL: {url}")
        return []
    local_links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if (
            href
            and (
                href.startswith("https://nursing.byu.edu/")
                or href.startswith("https://communications.nursing.byu.edu/")
                or href.startswith("https://advisement.nursing.byu.edu/")
            )
            and href not in all_links
        ):
            all_links.append(href)
            local_links.append(href)

    return local_links


def get_pages(url, all_links):
    local_links = get_subpages(url, all_links)
    if local_links:
        print(url.upper() + ": \n")
    for i in local_links:
        print(i + "\n")
    while local_links:
        get_pages(local_links[0], all_links)
        local_links.pop(0)

main_url = "https://nursing.byu.edu/"
all_links = []

get_pages(main_url, all_links)
