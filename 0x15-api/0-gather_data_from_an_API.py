#!/usr/bin/python3
"""For a given employee ID, return their todo list progress."""

import requests
import sys

def main():
    # Retrieve the user ID from the command line arguments
    user_id = sys.argv[1]

    # Fetch user details using the user ID
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response_user = requests.get(user_url)
    user_data = response_user.json()
    employee_name = user_data.get("name")

    # Fetch todo list items for the user
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': user_id}
    response_todos = requests.get(todos_url, params=params)

    if response_todos.status_code == 200:
        todos = response_todos.json()

    # Initialize counters for tasks
    completed_tasks_count = 0
    total_tasks_count = 0
    completed_task_titles = []

    # Iterate through the todo list
    for task in todos:
        if isinstance(task, dict):
            total_tasks_count += 1
            if task.get("completed") is True:
                completed_tasks_count += 1
                completed_task_titles.append(task.get("title"))

    # Print the todo list progress
    print(f"Employee {employee_name} is done with tasks (/
            {completed_tasks_count}/{total_tasks_count}):")
    for title in completed_task_titles:
        print('\t ' + title)

if __name__ == '__main__':
    main()
