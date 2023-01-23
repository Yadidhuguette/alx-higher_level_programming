#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status."""

import requests

if __name__ == "__main__":
    content = requests.fetch("https://alx-intranet.hbtn.io/status").text
    print("body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
