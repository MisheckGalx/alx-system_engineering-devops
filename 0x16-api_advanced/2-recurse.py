#!/usr/bin/python3
"""2-recurse module"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    recurse: returns a list containing the titles of all
    hot articles for a given subreddit
    Args:
        subreddit: passed to the url
    """

    if hot_list is None:
        hot_list = []

    params = {"after": after} if after else {}
    headers = {'User-Agent': 'My User Agent 1.0'}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    r = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    if r.status_code == 200:
        data = r.json()
        results = data.get("data")

        for i in results.get("children"):
            hot_titles = i.get('data').get('title')

            hot_list.append(hot_titles)

        after = results.get('after')

        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
