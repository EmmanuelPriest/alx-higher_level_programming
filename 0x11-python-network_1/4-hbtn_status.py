#!/usr/bin/python3

'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import requests


if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as req:
        content = req.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
