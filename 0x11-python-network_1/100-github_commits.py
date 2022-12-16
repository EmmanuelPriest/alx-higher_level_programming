#!/usr/bin/python3

'''
Listing of 10 commits(from the most recent to oldest) using this Github API:
https://developer.github.com/v3/repos/commits/
'''
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for n in range(10):
            print("{}: {}".format(commits[n].get("sha"),
                  commits[n].get("commit").get("author").get("name")))
    except IndexError:
        pass
