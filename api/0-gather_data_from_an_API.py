#!/usr/bin/python3
"""Module data from an API"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Make a GET request to the API endpoint
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    # Check if the request was successful
    if response.status_code == 200:
        todos = response.json()

        # Filter completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]

        # Get the employee name
        employee_name = todos[0]['name']

        # Get the number of completed tasks
        num_completed_tasks = len(completed_tasks)

        # Get the total number of tasks
        total_tasks = len(todos)

        # Print the progress information
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    else:
        print(f"Error: Failed to retrieve TODO list for employee ID {employee_id}")
