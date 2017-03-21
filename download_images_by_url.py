import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import urllib.request

x = 1

# Naming and downloading images


def naming_downloading_images(path, file_format, source):
    global x

    name = str(x) + file_format
    print(name)
    try:
        urllib.request.urlopen(source)
        try:
            file_name = os.path.join(path + "/", name)
            urllib.request.urlretrieve(source, file_name)
            print("Downloaded!")
            x += 1
        except:
            print("Some error issue.")
    except:
        print("File doesn't exist anymore or it's invalid.")


try:
    # URL
    url_input = input("Enter a url that you want to crawl: ").replace(" ", "")
    url = requests.get(url_input).text
    soup = BeautifulSoup(url, "lxml")

    url_parse_check = urlparse(url_input).netloc.split(".")

    # FILE
    file_path = input("Put full path (key sensitive) where you want to save images (directory) Tip: Put / before: ")

    if os.path.exists(file_path) and os.path.isdir(file_path):

        for link in soup.findAll("img"):

            src = link.get("src")

            if str(url_parse_check[0]) not in src:

                final_link = url_input + src
                print(final_link)

                if ".png" in src:
                    try:
                        naming_downloading_images(file_path, ".png", final_link)
                    except:
                        continue
                elif ".jpg" or ".jpeg" in src:
                    try:
                        naming_downloading_images(file_path, ".jpg", final_link)
                    except:
                        continue
            else:
                if ".png" in src:
                    try:
                        naming_downloading_images(file_path, ".png", final_link)
                    except:
                        continue
                elif ".jpg" or ".jpeg" in src:
                    try:
                        naming_downloading_images(file_path, ".jpg", final_link)
                    except:
                        continue

    else:
        print("Path doesn't exist or place where you want to save images is not directory.")

except KeyboardInterrupt:
    print("")
except:
    print("That url doesn't exist or you typed it wrong. Tip: Make sure you're copying it from website and watch "
        "out for protocols (http, https)")
