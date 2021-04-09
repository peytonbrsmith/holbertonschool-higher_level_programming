#!/usr/bin/python3
"""
post request with email
"""

if __name__ == "__main__":
    import sys
    from urllib import request, parse

    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}
    data = parse.urlencode(values)
    data = data.encode('ascii')

    req = request.Request(url, data=data, method="POST")
    with request.urlopen(req) as response:
        this = response.read()
        print(this.decode("utf-8"))
