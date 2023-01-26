#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge like
list 10 commits of repository "rails" by user "rails"."""

from sys import argv
import requests

if __name__ == "__main__":
    URL = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
            .format(argv[2], argv[1])

            r = requests.get(URL)
            commits = r.json()
            for commit in commits:
                print("{}: {}".format(commit.get("sha"),
                                      commit.get("commit").get("author").get("name")))
