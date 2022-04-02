#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("{}{}".format("\t- type: ", type(html)))
        print("{}{}".format("\t- content: ", html))
        print("{}{}". format("\t- utf8 content: ", html.decode('utf-8')))
