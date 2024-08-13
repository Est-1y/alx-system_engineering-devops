#!/usr/bin/python3
"""
function querying the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    """querying Reddit API and returning no. of subs."""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
    
    try:
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            return 0
        r_json = r.json()
        subs = r_json.get("data", {}).get("subscribers", 0)
        return subs
    except requests.exceptions.RequestException as e:
        return 0
    except ValueError:
        return 0
