#!/usr/bin/python3
""" top ten posts """


import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    h = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=h)
        data = resp.json()
        lst = data['data']['children']
        for i, post in enumerate(lst[:10], 1):
            title = post['data']['title']
            print(title)
    except:
        print(None)
