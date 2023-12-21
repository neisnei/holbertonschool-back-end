#!/usr/bin/python3
"""
Module Gather data from API
"""
import csv
import requests
from sys import argv


def get_employee_todo_list_progress(employee_id):
    """
    Retrieves employee's TODO list progress and exports it to CSV
    """
    response = requests.get(
        f"https://api.bito.com/v1/employees/{employee_id}/todo_list"
    )
    response.raise_for_status()

    todo_list = response.json()

    completed_tasks = [task for task in todo_list if task["is_done"]]

    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_list)

    print(
        f"Employee {todo_list['name']} is done with tasks
        ({number_of_done_tasks}/{total_number_of_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t{task['title']}")

    # Export data to CSV
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow
        (["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            writer.writerow
            ([employee_id, todo_list["name"], task["is_done"], task["title"]]
            )

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))

    get_employee_todo_list_progress(employee_id)
