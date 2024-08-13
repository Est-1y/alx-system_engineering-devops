#!/usr/bin/python3
"""Returning the number of subscribers on a given subreddit
And 0 if invalid
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced"}
    response = requests.get(url=url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
