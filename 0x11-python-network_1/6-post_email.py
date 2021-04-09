#!/usr/bin/python3
"""use requests to display post an email
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    req = requests.post(url, data=data)
    print(req.text)
