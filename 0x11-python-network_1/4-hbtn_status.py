#!/usr/bin/python3
"""Write a Python script that fetches
status of https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests

    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", req.text.__class__)
    print("\t- content:", req.text)
