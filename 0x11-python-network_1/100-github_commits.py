#!/usr/bin/python3
"""list 10 commits of repository "rails" by user "rails"."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    request = requests.get9url)
    commits = request.json()
    try:
        for a in range(10):
            print("{}: {}".format(
                commits[a].get("sha"),
                commits[a].get("commit").get("author").get("name")))
    except IndexError:
        pass
