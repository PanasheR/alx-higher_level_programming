#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
