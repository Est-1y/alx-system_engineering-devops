#!/usr/bin/python3
"""
Querying Reddit API returning a list.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Titles of hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'}
    params = {'limit': 100}  # Limit the number of posts to 100 (maximum)

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for post in data.get('data', {}).get('children', []):
            title = post.get('data', {}).get('title', '')
            hot_list.append(title)

        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None
