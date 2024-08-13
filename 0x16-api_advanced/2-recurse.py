#!/usr/bin/python3
"""Titles of all hot posts on subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Queries Reddit API and returns a list.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(
        url=url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
