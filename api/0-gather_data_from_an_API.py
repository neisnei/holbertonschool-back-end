#!/usr/bin/python3
"""
Module script returns information about list progress
"""
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    response = requests.get(
        "https://api.bito.com/v1/employees/{}/todo_list".format(employee_id)
    )
    response.raise_for_status()

    todo_list = response.json()

    completed_tasks = [task for task in todo_list if task["is_done"]]

    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_list)

    print("Employee {} is done with tasks({}/{}):".format(
        todo_list["name"], number_of_done_tasks, total_number_of_tasks
    ))

    for task in completed_tasks:
        print("\t{}".format(task["title"]))


if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))

    get_employee_todo_list_progress(employee_id)
