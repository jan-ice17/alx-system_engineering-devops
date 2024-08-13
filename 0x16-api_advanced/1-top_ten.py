#!/usr/bin/python3
"""
A function queries the Reddit API and
prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit_name):
    """Fetches and prints the titles of the first 10
    hot posts for the specified subreddit.
    """
    api_url = f"https://www.reddit.com/r/{subreddit_name}/hot.json?limit=10"
    user_agent_str = 'JudyJanic/1.0 (by /u/My-Username)'
    headers = {'User-Agent': user_agent_str}
    try:
        response = requests.get(
            api_url,
            headers=headers,
            allow_redirects=False
        )
        if response.status_code == 200:
            json_data = response.json()
            posts = json_data['data']['children']
            post_titles = []
            for post in posts:
                post_titles.append(post['data']['title'])
            for title in post_titles:
                print(title)
        else:
            print(None)
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
