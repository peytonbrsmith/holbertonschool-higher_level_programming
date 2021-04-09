#!/usr/bin/python3
"""get git
"""

if __name__ == "__main__":
    import sys
    import requests

    url = 'https://api.github.com/user'

    username = sys.argv[1]
    token = sys.argv[2]

    req = requests.get(url, auth=(username, token))
    print(req.json().get("id"))
