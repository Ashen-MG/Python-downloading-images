import requests
from urllib.parse import urlparse


def getting_url():
    try:
        url = input("Type url that you want to crawl (example - https://blablabla.com): ").replace(" ", "")

        if "https" not in url or "http" not in url:
            print("You need to specify protocol of the page")
            return getting_url()
        else:
            if "://www." in url:
                final_url = url.replace("www.", "")
                if ".com" in url:
                    r = requests.head(final_url)
                    if r.status_code == 200:
                        netloc_url = urlparse(final_url).netloc
                        return final_url, netloc_url
                    else:
                        print("Url doesn't exist")
                else:
                    print("Url is not valid.")
                    return getting_url()
            else:
                if ".com" in url:
                    r = requests.head(url)
                    if r.status_code == 200:
                        netloc_url = urlparse(url).netloc
                        return url, netloc_url
                    else:
                        print("Url doesn't exist")
                else:
                    print("Url is not valid.")
                    return getting_url()

    except:
        print("Url doesn't exist")
        return getting_url()
