#!/usr/bin/python3
"""
sends request and handles http errors
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            this = response.read()
            print(this.decode("utf-8"))
    except error.HTTPError as e:
        error = ''.join((item for item in str(e) if item.isdigit()))
        print("Error code:", error)
