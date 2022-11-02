#!/usr/bin/python3
""" a program that prints the 1st 10 hot posts
on a subreddit"""


import requests

Base_url = 'https://www.reddit.com'


def top_ten(subreddit):
    """a function that prints the 1st 10 hot posts
    """

    api_headers = {
         'Accept': 'application/json',
         'user-agent': ' '.join([
             'Mozilla/5.0 (Linux; Android 6.0;Nexus 5 Build/MRA58N)'
             'AppleWebKit/537.36 (KHTML, like Gecko)'
             'Chrome/106.0.0.0 Mobile Safari/537.36'
         ])
        }
    sort = 'top'
    limit = 10
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            Base_url,
            subreddit,
            sort,
            limit
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
