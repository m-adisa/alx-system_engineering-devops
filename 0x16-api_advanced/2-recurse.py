#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def recurse(subreddit, hot_list=[], n=0, after=None):
    '''
    returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should return None.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0)',
            'Gecko/20100101',
            'Firefox/106.0'
            ])
        }
    
    sort = 'hot'
    limit = 30
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
