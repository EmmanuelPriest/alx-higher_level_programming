#!/usr/bin/python3

'''
Python script that takes my GitHub credentials(username and password)
and uses the GitHub API to display my id
'''
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print("{}".format(req.json().get("id")))
