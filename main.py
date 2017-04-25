from file_path import file
from link_finder import final_link
import urllib.request
import os


# Downloading and naming images
def main():
    try:
        path = file()
        x = 1
        for links in final_link():
            if ".jpg" in links or ".jpeg" in links:
                try:
                    file_name = os.path.join(path + "/" + str(x) + ".jpg")
                    urllib.request.urlretrieve(links, file_name)
                    print("Downloading " + str(x) + ".jpg")
                    x += 1

                except:
                    print("Link doesn't exist anymore")
                    continue

            elif ".png" in links:
                try:
                    file_name = os.path.join(path + "/" + str(x) + ".png")
                    urllib.request.urlretrieve(links, file_name)
                    print("Downloading " + str(x) + ".png")
                    x += 1

                except:
                    print("Link doesn't exist anymore")
                    continue
            else:
                print("Not a image. Move in on.")
                continue

    except KeyboardInterrupt:
        print("\nQuiting")

    except:
        print("")


if __name__ == "__main__":
    main()
