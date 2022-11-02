#!/usr/bin/python3
"""
Working with the Reddit API
"""
import requests

BASE = 'https://www.reddit.com'
""" Reddit's base API URL """

def number_of_subscribers(subreddit):
    """Returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0
    """

    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0)',
            'Gecko/20100101',
            'Firefox/106.0'
            ])
        }

    res = requests.get(
        '{}/r/{}/about/.json'.format(BASE, subreddit),
        headers = api_headers,
        allow_redirects = False
        )

    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0
