import requests
from bs4 import BeautifulSoup
import pprint


def request_page(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


def sort_stories_by_votes(hn):
    hn.sort(key=lambda x: x["points"], reverse=True)
    return hn


def custom_hn(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtexts[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "href": href, "points": points})
    return sort_stories_by_votes(hn)


URL_main = "https://news.ycombinator.com/"
URL_pages = []
how_many_pages = 3
links = []
subtexts = []

for page in range(1, how_many_pages + 1, 1):
    page_num = "news?p=" + str(page)
    URL_for_page = URL_main + page_num
    soup = request_page(URL_for_page)
    links_on_page = soup.select(".titlelink")
    links = links + links_on_page
    subtexts_on_page = soup.select(".subtext")
    subtexts = subtexts + subtexts_on_page
    print("parsed page #", page, "its URLS is ", URL_for_page)

pprint.pprint(custom_hn(links, subtexts))
