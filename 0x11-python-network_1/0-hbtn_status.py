#!/usr/bin/python3

'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        req = res.read()
        print(req, end="")
