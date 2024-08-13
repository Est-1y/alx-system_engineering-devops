#!/usr/bin/python3
""" Querying Reddit API and printing titles"""
import requests


def top_ten(subreddit):
    """Titles of 10 hottest posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for post in data.get('data').get('children'):
            title = post.get('data').get('title')
            print(title)
    else:
        print(None)
