#!/usr/bin/python3
"""
Script to interact with Reddit's API to fetch hot posts from a subreddit.
"""
import requests

# Variable to store the pagination token for the next set of posts
after_token = None


def recurse(subreddit, hot_posts=None):
    """
    Recursively fetches hot post titles from a subreddit.
    """
    global after_token
    if hot_posts is None:
        hot_posts = []
    # Define custom User-Agent for API request
    headers = {'User-Agent': 'api_advanced_project'}
    # Endpoint to fetch hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # Parameters including pagination token
    params = {'after': after_token}
    response = requests.get(url, params=params,
                            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        # Fetch the 'after' token to get the next set of results
        after_token = response.json().get("data").get("after")
        # Extract titles of the posts
        posts = response.json().get("data").get("children")
        for post in posts:
            # Append each title to the list
            hot_posts.append(post.get("data").get("title"))
        # Continue fetching recursively if there are more posts
        if after_token:
            recurse(subreddit, hot_posts)
        return hot_posts
    else:
        # Return None if the request was unsuccessful
        return None
