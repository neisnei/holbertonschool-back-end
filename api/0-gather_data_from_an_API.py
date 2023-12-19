#!/usr/bin/python3
"""Module data from an API"""
import requests
import sys


import requests
import sys

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    completed_tasks = []
    for todo in todos:
        if todo['completed']:
            completed_tasks.append(todo['title'])

    employee_name = todos[0]['username']
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
