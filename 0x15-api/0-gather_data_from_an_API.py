#!/usr/bin/python3

"""display TODO list progress"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Using REST API for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # User info.
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # TODO list.
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Progress check
    total_tasks = len(todos_data)
    completed_tasks = sum(task.get("completed", False) for task in todos_data)

    # Progress info
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, completed_tasks, total_tasks))

    # Titles of tasks done
    for task in todos_data:
        if task.get('completed', False):
            print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    # Verify command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Employee ID
    employee_id = int(sys.argv[1])

    # Get TODO list progress
    get_employee_todo_progress(employee_id)
