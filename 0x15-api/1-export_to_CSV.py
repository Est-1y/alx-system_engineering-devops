#!/usr/bin/python3

"""
exporting data in the CSV format
"""

import csv
import requests
import sys


def get_employee_info_and_tasks(employee_id):
    """
    getting employee info
    """
    # API base URL
    api_url = 'https://jsonplaceholder.typicode.com/'

    # URLs
    user_url = '{}users/{}'.format(api_url, employee_id)
    todos_url = '{}todos?userId={}'.format(api_url, employee_id)
    # user info
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # username
    username = user_data.get('username')

    # Fetching tasks
    todos_response = requests.get(todos_url)
    tasks_data = todos_response.json()

    # Creating a list of tasks
    tasks_list = []
    for task in tasks_data:
        tasks_list.append(
            [employee_id, username, task.get('completed'), task.get('title')])

    # Creating a CSV file
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        # task write
        for task in tasks_list:
            employee_writer.writerow(task)


if __name__ == "__main__":
    # command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Check command-line arguments
    employee_id = sys.argv[1]

    # getting employee info
    get_employee_info_and_tasks(employee_id)
