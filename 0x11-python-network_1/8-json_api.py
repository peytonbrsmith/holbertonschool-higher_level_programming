#!/usr/bin/python3
"""post with json
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "http://761cd13fb8de.3b3b042d.hbtn-cod.io:5000/search_user"

    qval = ""
    try:
        qval = sys.argv[1]
    except:
        pass

    data = {"q": qval}
    req = requests.post(url, data)
    json = req.json()
    if (type(json)):
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    else:
        print("Not valid JSON")
