#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a
   parameter."""


if __name__ == "__main__":
    import requests
    from sys import argv

    par = ""
    if len(argv) > 1:
        par = argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': par})
    try:
        result = res.json()
        if result == {}:
            print('No result')
        else:
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except ValueError:
        print('Not a valid JSON')
