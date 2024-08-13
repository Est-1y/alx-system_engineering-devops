#!/usr/bin/python3
"""Querying subscribers on Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        subscribers = data.get('data', {}).get('subscribers', 0)

        return subscribers
    else:
        return 0
