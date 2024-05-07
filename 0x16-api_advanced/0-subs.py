#!/usr/bin/python3
""" return total number of subscribe in subreddit """


import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    h = {'User-Agent': 'Mozilla/5.0'}

    try:
        resp = requests.get(url, headers=h)
        data = resp.json()
        subs = data['data']['subscribers']
        return subs
    except Exception:
        return 0
