#!/usr/bin/python3
"""post with json
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "http://761cd13fb8de.3b3b042d.hbtn-cod.io:5000/search_user"

    try:
        qval = sys.argv[1]
    except IndexError:
        qval = ""

    data = {"q": qval}
    req = requests.post(url, data)
    try:
        json = req.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except (ValueError, simplejson.JSONDecodeError):
        print("Not a valid JSON")
