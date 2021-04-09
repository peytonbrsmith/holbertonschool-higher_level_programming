#!/usr/bin/python3
"""Write a Python script that fetches
status of https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        this = response.read().decode("utf-8")
        print("Body response:")
        print("\t- type:", type(this))
        print("\t- content:", this)
