#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request


    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        this = response.read()
        print("Body response:")
        print("\t- type: ", this.__class__)
        print("\t- content: ", this)
        print("\t- utf8 content: ", this.decode("utf-8"))
