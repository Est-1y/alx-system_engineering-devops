#!/usr/bin/python3
"""
 exporting data in the JSON format.
"""

import json
import requests
import sys


def get_employee_info_and_tasks(employee_id):
    """
    Info about employees and their tasks
    """
    # API base URL
    api_url = 'https://jsonplaceholder.typicode.com/'

    # URLs for user and tasks.
    user_url = '{}users/{}'.format(api_url, employee_id)
    todos_url = '{}todos?userId={}'.format(api_url, employee_id)

    # user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # username
    username = user_data.get('username')

    # tasks
    todos_response = requests.get(todos_url)
    tasks_data = todos_response.json()

    # Creating a list of tasks.
    tasks_list = []
    for task in tasks_data:
        dict_task = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks_list.append(dict_task)

    # Creating a dictionary
    employee_tasks = {str(employee_id): tasks_list}

    # Creating a JSON file.
    filename = '{}.json'.format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump(employee_tasks, json_file)


if __name__ == "__main__":
    # Check command-line arguments provision
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    # employee I
    employee_id = sys.argv[1]

    # geting employee information and task
    get_employee_info_and_tasks(employee_id)
