#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to fetch
data about a specific employee
and prints a summary of their TODO list progress.
"""
import json
import requests
import sys

def get_employee_todo_progress(employee_id):
    # URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Get user's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task["completed"]]

    # Display progress information
    print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to get and display employee TODO list progress
    get_employee_todo_progress(employee_id)

