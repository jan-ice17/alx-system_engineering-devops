#!/usr/bin/python3
"""
This script retrieves a user's todo list from a given API and formats it into a CSV file.
The CSV file is named using the user's ID and contains the following fields:
USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE.
"""
import csv
import requests
import sys


def main():
    # Retrieve the USER_ID from command line arguments
    USER_ID = sys.argv[1]

    # Fetch user details from the API
    url_user = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    response_user = requests.get(url_user)
    users = response_user.json()
    USERNAME = users.get("username")

    # Fetch user's todos from the API
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': USER_ID}
    response = requests.get(url_todo, params=params)

    if response.status_code == 200:
        todos = response.json()

    # Filename will be represented with the user id
    filename = f"{USER_ID}.csv"
    with open(filename, 'w', newline='') as f:
        # Define the CSV writer with specific fieldnames and quoting settings
        write_csv = csv.DictWriter(f, fieldnames=["USER_ID", "USERNAME",
                                                  "TASK_COMPLETED_STATUS", "TASK_TITLE"],
                                   quotechar='"', quoting=csv.QUOTE_ALL)
        
        # Write the header to the CSV file
        write_csv.writeheader()

        # Write each todo item to the CSV file
        for j in todos:
            TASK_COMPLETED_STATUS = j.get("completed")
            TASK_TITLE = j.get("title")
            row = {
                "USER_ID": USER_ID,
                "USERNAME": USERNAME,
                "TASK_COMPLETED_STATUS": TASK_COMPLETED_STATUS,
                "TASK_TITLE": TASK_TITLE
            }
            write_csv.writerow(row)


if __name__ == '__main__':
    main()
