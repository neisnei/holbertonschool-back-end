#!/usr/bin/python3
"""Module Gather data from API"""

import csv
import requests
from sys import argv


employee_id = sys.argv[1]
"""Get the employee ID"""

u_response = requests.get(
    'https://jsonplaceholder.typicode.com/users/' + employee_id)
"""Get the user response"""

data = u_response.json()
"""Get the user response in json format"""

employee_name = data.get('name')
"""Get the employee name"""

to_do_response = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
"""Get the to do response"""

to_do_data = to_do_response.json()
"""Get the to do response in json format"""

to_do_total = len(to_do_data)
"""Get the total number of to do"""

comp_to_do = sum([1 for task in to_do_data if task.get('completed')])
"""Get the number of completed to do"""

print("Employee " + employee_name + " is done with tasks(" +
      comp_to_do + "/" + to_do_total + "):")

for task in to_do_data:
    if task['completed']:
        print('\t ' + task['title'])

if __name__ == '__main__':
    pass
