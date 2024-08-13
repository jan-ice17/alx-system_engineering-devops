#!/usr/bin/python3
"""
This script utilizes the Reddit API to retrieve
the number of subscribers for a specific subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """This function makes a request to the Reddit API
    and fetches the subscriber count for the given subreddit.
    """
    if subreddit is None:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    custom_user_agent = 'JudyJanice/1.0 (by /u/My-username)'

    try:
        headers = {'User-Agent': 'custom_user_agent'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
