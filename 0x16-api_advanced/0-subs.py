#!/usr/bin/python3
""" a program that queries Reddit Api and returns
the number of subscribers """

import requests

Base_url = 'https://www.reddit.com'


def number_of_subscribers(subreddit):
    """ a function that queries reddit's api"""

    api_headers = {
         'Accept': 'application/json',
         'user-agent': ' '.join([
             'Mozilla/5.0 (Linux; Android 6.0;Nexus 5 Build/MRA58N)'
             'AppleWebKit/537.36 (KHTML, like Gecko)'
             'Chrome/106.0.0.0 Mobile Safari/537.36'
         ])
        }

    res = requests.get(
        '{}/r/{}/about/.json'.format(Base_url, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0
