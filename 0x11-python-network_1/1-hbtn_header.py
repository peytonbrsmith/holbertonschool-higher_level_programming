#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the
value of the X-Request-Id variable found in
the header of the response.
"""
if __name__ == "__main__":
    import sys
    from urllib import request

    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        print(response.getheader("X-Request-Id"))
