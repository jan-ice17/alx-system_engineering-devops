#!/usr/bin/python3
"""Reddit API interaction script to count
word occurrences in hot post titles."""

import requests


def count_words(subreddit, word_list, after="", word_count=None):
    """ Recursively counts occurrences of words in the titles of hot posts
    from a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of words to count in the titles.
        after (str): Pagination token for Reddit API (default: empty string).
        word_count (list): List to store counts of each word (default: None).
    """
    if word_count is None:
        word_count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            params={'after': after},
                            allow_redirects=False,
                            headers={'User-Agent': 'api_word_counter'})

    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            for word in post['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        word_count[i] += 1

        after = data['data']['after']
        if after is None:
            merged_indices = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        merged_indices.append(j)
                        word_count[i] += word_count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (word_count[j] > word_count[i] or
                            (word_list[i] > word_list[j] and
                             word_count[j] == word_count[i])):
                        word_count[i], word_count[j] = word_count[j], word_count[i]
                        word_list[i], word_list[j] = word_list[j], word_list[i]

            for i in range(len(word_list)):
                if word_count[i] > 0 and i not in merged_indices:
                    print("{}: {}".format(word_list[i].lower(), word_count[i]))
        else:
            count_words(subreddit, word_list, after, word_count)
