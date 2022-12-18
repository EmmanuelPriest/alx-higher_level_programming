#!/usr/bin/python3

'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        req = resp.read()
