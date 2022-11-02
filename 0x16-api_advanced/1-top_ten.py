#!/usr/bin/python3
"""
Working with the Reddit API
"""
import requests

BASE = 'https://www.reddit.com'
""" Reddit's base API URL """

def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit
    """

    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0)',
            'Gecko/20100101',
            'Firefox/106.0'
            ])
        }

    sort = 'top'
    limit = 10
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            BASE,
            subreddit,
            sort,
            limit
            ),
        headers = api_headers,
        allow_redirects = False
        )

    if res.status_code == 200:
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
        else:
            print(None)

