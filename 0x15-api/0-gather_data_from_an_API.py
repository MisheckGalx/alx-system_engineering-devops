#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import json
import sys
import urllib.request


def get_info(id):
    """
    get_info: for a given employee ID, returns information
    about his/her TODO list progress.
    Args:
        id: the user's id
    """

    # URLs to GET
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{id}'

    # GET User's name
    with urllib.request.urlopen(user_url) as user_response:
        user_data = json.loads(user_response.read().decode('utf-8'))
        empolyee_name = user_data.get('name')

        # GET todo of the user
        with urllib.request.urlopen(todo_url) as todo_response:
            todo_data = json.loads(todo_response.read().decode('utf-8'))

            total_tasks = len(todo_data)

            completed_tasks = []

            for task in todo_data:
                if task['completed']:
                    completed_tasks.append(task)

            print(f'Employee {empolyee_name} is done with ', end='')
            print(f'tasks({len(completed_tasks)}/{total_tasks}):')

            for task in completed_tasks:
                print(f'\t {task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        id = sys.argv[1]
        get_info(id)
