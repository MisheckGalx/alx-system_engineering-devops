#!/usr/bin/python3
"""Script gather and display TODO list progress of an employee from an API"""

import json
import sys
import urllib.request


def get_employee_info(employee_id):
    """
    Retrieves and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): ID of the employee whose progress is to be checked.
    """

    # Construct URLs for fetching user and TODO list data based on employee_id
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

	with urllib.request.urlopen(user_url) as user_response:
        user_data = json.loads(user_response.read().decode('utf-8'))
        employee_name = user_data.get('name')


		with urllib.request.urlopen(todo_url) as todo_response:
            todo_data = json.loads(todo_response.read().decode('utf-8'))

            total_tasks = len(todo_data)
            completed_tasks = []


            for task in todo_data:
                if task['completed']:
                    completed_tasks.append(task)


            print(f'Employee {empolyee_name} is done with ', end='')
            for task in completed_tasks:
                print(f'\t {task["title"]}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        get_employee_info(employee_id)
    else:
        print("Usage: python script_name.py <employee_id>")
