#!/usr/bin/python3
"""Titles of the 10 hottest posts on Reddit"""

import requests


def top_ten(subreddit):
    """
    Queries.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced"}
    params = {"limit": 10}
    response = requests.get(
        url=url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(t.get("data").get("title")) for t in results.get("children")]
