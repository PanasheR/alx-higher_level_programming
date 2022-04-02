#!/usr/bin/python3
"""script that takes in a URL, sends a request
   to the URL and displays the body of the
   response (decoded in utf-8)"""


if __name__ == "__main__":
    from sys import argv
    from urllib.error import HTTPError
    import urllib.request

    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
