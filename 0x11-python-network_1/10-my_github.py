#!/usr/bin/python3
"""GitHub credentials (username and password) and
uses the GitHub API to display your id"""
from sys import argv
import requests

if __name__ == "__main__":
    auth = (argv[1], argv[2])
    r = requests.get("https://api.githum.com/user", auth)
    print(r.json().get("id"))
