import os


def file():
    global path
    try:
        file_path = input("Type full path where you want to save images: ")

        if os.path.exists(file_path) and os.path.isdir(file_path):
            for path in file_path:
                pass
            if path == "/":
                file_path = file_path[:-1]
                return file_path
            else:
                return file_path
        else:
            print("Path doesn't exist or it is not a directory.")
            file()

    except os.error as msg:
        print("Some error issue")
        print(str(msg) + "\n")
        file()
