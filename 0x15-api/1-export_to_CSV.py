#!/usr/bin/python3
"""0-gather_data_from_an_API module."""
import csv
import json
import sys
import urllib.request


def get_info(id):
    """
    get_info: for a given employee ID, returns information
    about his/her TODO list progress in CSV format.
    Args:
        id: the user's id
    """

    # URLs to GET
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{id}'

    # GET User's name
    with urllib.request.urlopen(user_url) as user_response:
        user_data = json.loads(user_response.read().decode('utf-8'))
        employee_name = user_data.get('username')

    # GET todo of the user
    with urllib.request.urlopen(todo_url) as todo_response:
        todo_data = json.loads(todo_response.read().decode('utf-8'))

    with open(f'{sys.argv[1]}.csv', 'w', newline='') as f:
        for data in todo_data:
            f.write(
                    '"{}","{}","{}","{}"\n'.format(
                        id,
                        employee_name,
                        data.get('completed'),
                        data.get('title')
                        )
                    )


if __name__ == '__main__':
    if len(sys.argv) == 2:
        id = sys.argv[1]
        get_info(id)
