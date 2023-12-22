#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to fetch
data about a specific employee
and prints a summary of their TODO list progress.
"""

import requests
import sys


def print_todo_progress(employee_id):
    user_url = ('https://jsonplaceholder.typicode.com/users/{}'
                .format(employee_id))
    user_response = requests.get(user_url)
    employee_name = user_response.json()['name']

    todos_url = ('https://jsonplaceholder.typicode.com/todos?userId={}'
                 .format(employee_id))
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task['completed'])

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, done_tasks, total_tasks))
    for task in todos_data:
        if task['completed']:
            print('\t {}'.format(task['title']))


if __name__ == "__main__":
    employee_id = sys.argv[1]
    print_todo_progress(employee_id)
