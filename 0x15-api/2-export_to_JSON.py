#!/usr/bin/python3

"""
a python script that Export to JSON and ensures
that records all tasks that are owned by this employeee
"""
import json
import requests
import sys


def main():
    USER_ID = sys.argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    response_user = requests.get(url_user)

    if response_user.status_code != 200:
        print("Error fetching user data")
        return
    user = response_user.json()
    USERNAME = user.get("username")

    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': USER_ID}
    response = requests.get(url_todo, params=params)

    if response.status_code != 200:
        print("Error fetching todos")
        return

    todos = response.json()

    to_dict = {USER_ID: []}

    for i in todos:
        COMPLETED = i.get("completed")
        TASK = i.get("title")
        to_dict[USER_ID].append({
            "task": TASK,
            "completed": COMPLETED,
            "username": USERNAME
        })

    filename = f"{USER_ID}.json"
    with open(filename, 'w') as f:
        json.dump(to_dict, f)


if __name__ == "__main__":
    main()
