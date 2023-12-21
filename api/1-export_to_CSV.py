#!/usr/bin/python3
"""Module Gather data from API"""

import csv
import requests
from sys import argv


def get_employee_todo_list_progress(employee_id):
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    )
    response.raise_for_status()
    todo_list = response.json()

    # Get user info
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user_response.raise_for_status()
    user_info = user_response.json()

    # Extract relevant information
    user_id = user_info["id"]
    username = user_info["username"]

    # Export data to CSV
    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            writer.writerow([user_id, username, task["completed"], task["title"]])

    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID.")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
