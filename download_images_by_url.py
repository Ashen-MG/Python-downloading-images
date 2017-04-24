import requests
from html.parser import HTMLParser
from urllib.parse import urlparse
import os
import urllib.request

x = 1
y = 1
z = 1


# Finding links for download
class LinkFinder(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for (attribute, src) in attrs:
                if attribute == "src":
                    print(src)

    def error(self, message):
        pass


#  Naming and downloading images
def naming_downloading_images(path, file_format, source):
    global x

    name = str(x) + file_format
    print(name)
    try:
        urllib.request.urlopen(source)
        try:
            file_name = os.path.join(path + "/", name)
            urllib.request.urlretrieve(source, file_name)
            print("Downloaded! \n\n")
            x += 1
        except:
            print("Some error issue.")
    except:
        print("File doesn't exist anymore or it's invalid. \n\n")


try:
    # URL
    url_input = input("Enter a url that you want to crawl: ").replace(" ", "")
    url = requests.get(url_input).text

    finder = LinkFinder()

    url_parse_check = urlparse(url_input).netloc.split(".")

    # FILE
    file_path = input("Put full path (key sensitive) where you want to save images (directory) Tip: Put / before: ")

    # Check if file exists
    if os.path.exists(file_path) and os.path.isdir(file_path):

        #  Counting how many images are going to be downloaded
        for count_link in soup.findAll("img"):
            count_src = count_link.get("src")
            y += 1

        # Crawling
        for link in soup.findAll("img"):

            src = link.get("src")

            print("Downloading (" + str(z) + "/" + str(y) + ")")

            if str(url_parse_check[0]) not in src:

                final_link = url_input + src
                print(final_link)

                # Saving as png or jpeg/jpg
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

            z += 1

    else:
        print("Path doesn't exist or place where you want to save images is not directory.")

except KeyboardInterrupt:
    print("")
except:
    print("That url doesn't exist or you typed it wrong. Tip: Make sure you're copying it from website and watch "
          "out for protocols (http, https)")
