#!/usr/bin/python3
"""use requests to display header from url
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
