#!/usr/bin/python3
"""Script to return info about todo list progress"""
import requests
from requests import get
from sys import argv


def information_employee():
    """Returns information about employees"""
    id_employee = int(argv[1])
    employee_name = ""
    number_of_done_task = 0
    total_number_of_task = 0
    task_title = []

    url_users = 'https://jsonplaceholder.typicode.com/users'

    # Get user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{id_employee}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_one = get(url_users)
    response_two = get(url_todos)

    if response_one.status_code == 200:
        response_usr = response_one.json()
        response_tod = response_two.json()

        for user in response_usr:
            if (user['id'] == id_employee):
                employee_name = user['name']

                for tod in response_tod:
                    if tod['userId'] == id_employee:
                        total_number_of_task += 1
                        if tod['completed'] is True:
                            number_of_done_task += 1
                            task_title.append(tod['title'])

        print('Employee {} is done with tasks({}/{}):'
              .format(employee_name, number_of_done_task,
                      total_number_of_task))
        for title in task_title:
            print('\t {}'.format(title))


if __name__ == "__main__":
    information_employee()
