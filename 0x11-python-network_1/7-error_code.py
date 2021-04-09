#!/usr/bin/python3
"""send request,
display body,
handle errors
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
