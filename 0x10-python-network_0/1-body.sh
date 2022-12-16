#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -X GET -w "%{stderr}{\"status\": \"%{http_code}\", \"body\":\"%{stdout}\"}" -s -o - "$1"
