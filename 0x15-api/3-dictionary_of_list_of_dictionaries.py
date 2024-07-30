#!/usr/bin/python3
"""
A python script that prints out Dictionary of list of dictionaries
as.
"""
import json
import requests
import sys


def main():
    url_user = "https://jsonplaceholder.typicode.com/users"
    response_user = requests.get(url_user)
    users = response_user.json()

    if response_user.status_code == 200:
        dictionary = {}
        for user in users:
            USER_ID = user.get('id')
            USERNAME = user.get('username')
            url_todo = 'https://jsonplaceholder.typicode.com/todos'
            params = {'userId': USER_ID}
            response_todo = requests.get(url_todo, params=params)
            if response_todo.status_code == 200:
                todos = response_todo.json()
                to_list = []
                for i in todos:
                    COMPLETED = i.get("completed")
                    TASK = i.get("title")
                    usr_dict = {
                            "username": USERNAME,
                            "task": TASK,
                            "completed": COMPLETED}
                    to_list.append(usr_dict)
                dictionary[USER_ID] = to_list

        with open('todo_all_employees.json', 'w', newline='') as f:
            json.dump(dictionary, f)


if __name__ == '__main__':
    main()
