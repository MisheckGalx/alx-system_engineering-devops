#!/usr/bin/python3
"""2-export_to_JSON module"""
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

    # all tasks that are owned by this employee
    task_obj = []
    for data in todo_data:
        task_obj.append(
                {
                    "task": data.get('title'),
                    "completed": data.get('completed'),
                    "username": employee_name,
                    }
                    )

        if not task_obj[-1]:
            task_obj.append(', ')

    # dictionary
    dictionary = {
            id: task_obj
            }

    json_object = json.dumps(dictionary)

    with open(f'{sys.argv[1]}.json', 'w') as f:
        f.write(json_object)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        id = sys.argv[1]
        get_info(id)
