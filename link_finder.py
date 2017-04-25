from html.parser import HTMLParser
from url import getting_url
import requests
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for (attribute, src) in attrs:
                if attribute == "src":
                    self.links.add(src)

    def links(self):
        return self.links

    def error(self, message):
        pass


def final_link():
    try:
        finder = LinkFinder()
        links = set()
        url, netloc_url = getting_url()
        r = requests.get(url).text
        finder.feed(r)
        for link in finder.links:
            final_link = parse.urljoin(url, link)
            links.add(str(final_link))
        length_links = len(links)
        if length_links == 0:
            print("No images found.")
        elif length_links == 1:
            print("1 image is going to be downloaded.")
            return links
        else:
            print(str(length_links) + " images are going to be downloaded.")
            return links

    except:
        print("")
