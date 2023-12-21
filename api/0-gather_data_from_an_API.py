#!/usr/bin/python3
"""Using employee ID returns information about his/her TODO list progress"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response = requests.get(url)  # Get the response from the API
    name = response.json().get("name")  # Get the name of the user
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    # Get the response from the API for the user_id from the argv
    response = requests.get(url)
    tasks = response.json()  # Get the tasks of the user
    completed = [task for task in tasks if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(name, len(completed),
                                                          len(tasks)))
    for task in completed:
        print("\t {}".format(task.get("title")))
