#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to fetch
data about a specific employee
and prints a summary of their TODO list progress.
"""

import json
import requests
import sys


        def get_employee_todo_list_progress(employee_id):
  """Gets the employee TODO list progress from the REST API.

  Args:
    employee_id: The employee ID.

  Returns:
    A dictionary containing the employee TODO list progress.
  """

        url = 'https://api.bito.com/v1/employees/{}/todo_list_progress'.format(
      employee_id)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


def main():
  """Gets employee TODO list progress and prints to standard output."""

        employee_id = int(input('Enter the employee ID: '))
        progress = get_employee_todo_list_progress(employee_id)
        print('Employee {} is done with tasks({}/{}):'.format(
        progress['name'], progress['number_of_done_tasks'],
        progress['total_number_of_tasks']))
  for task in progress['completed_tasks']:
        print('\t{}'.format(task['title']))

if __name__ == '__main__':
  main()
