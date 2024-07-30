#!/usr/bin/python3
"""For a given employee ID, return their todo list progress."""

import requests
import sys


def main():
    # Retrieve the user ID from the command line arguments
    userid = sys.argv[1]

    # Fetch user details using the user ID
    url_usr = f"https://jsonplaceholder.typicode.com/users/{userid}"
    response_usr = requests.get(url_usr)
    users = response_usr.json()
    EMPLOYEE_NAME = users.get("name")

    # Fetch todo list items for the user
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': userid}
    response = requests.get(url_todo, params=params)

    if response.status_code == 200:
        todos = response.json()

    # Initialize counters for tasks
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    # Iterate through the todo list
    for j in todos:
        if isinstance(j, dict):
            TOTAL_NUMBER_OF_TASKS += 1
        if j.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(j.get("title"))

    # Print the todo list progress
    print(f"Employee {EMPLOYEE_NAME} is done with tasks (\
            {NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in TASK_TITLE:
        print('\t ' + title)


if __name__ == '__main__':
    main()
