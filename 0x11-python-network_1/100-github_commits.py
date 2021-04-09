#!/usr/bin/python3
"""get gitted
"""

if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    payload = {
        'per_page': 10,
    }
    req = requests.get(url, params=payload)
    for commit in req.json():
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))
