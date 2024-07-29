#!/usr/bin/python3
"""
extending Python script to export data in the JSON format
"""

import json
import requests
import sys


def get_all_employees_and_tasks():
    """
    Info about all employees and their tasks from API
    """
    # API base URL
    api_url = 'https://jsonplaceholder.typicode.com/'

    # information.
    users_url = '{}users'.format(api_url)
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Task Dictionary.
    all_employees_tasks = {}

    # Iteration.
    for user in users_data:
        name = user.get('username')
        userid = user.get('id')

        # tasks.
        todos_url = '{}todos?userId={}'.format(api_url, userid)
        todos_response = requests.get(todos_url)
        tasks_data = todos_response.json()

        # storing tasks
        tasks_list = []

        # Iterating through tasks.
        for task in tasks_data:
            dict_task = {
                "username": name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            tasks_list.append(dict_task)

        # Adding tasks to the dictionary
        all_employees_tasks[str(userid)] = tasks_list

    # Creating a JSON file
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_tasks, json_file)


if __name__ == "__main__":
    # getting info about all employees and their tasks
    get_all_employees_and_tasks()
