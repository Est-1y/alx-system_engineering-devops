#!/usr/bin/python3
"""Querying subscribers on a Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0\
            (by /u/Large_Alternative_30)"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")
    except (Exception):
        print('Not Found')
        return (0)
