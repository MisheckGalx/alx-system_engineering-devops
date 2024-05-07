#!/usr/bin/python3
"""0-subs module"""
import requests


def number_of_subscribers(subreddit):
    """
    number_of_subscribers: returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit
    """
    headers = {'User-Agent': 'My User Agent'}

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        if r.text:
            data = r.json()

            subcribers_count = data['data']['subscribers']
            return subcribers_count

    return 0
