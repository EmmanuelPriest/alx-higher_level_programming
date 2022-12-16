#!/usr/bin/python3

'''
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
'''
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) != 2:
        print("No result")
    else:
        let = sys.argv[1]
        if let:
            reqd_data = {"q": sys.argv[1]}
        else:
            reqd_data = {"q": ""}
        req = requests.post(url, reqd_data)
        try:
            json_req = req.json()
            if not json_req.get("id"):
                print("No result")
            else:
                print("[{}] {}".format(json_req.get("id"),
                                       json_req.get("name")))
    except ValueError:
        print("Not a valid JSON")
