#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the
body of the response."""
import requests
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    request = requests.get(URL)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
