#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries module"""
import json
import urllib.request


def get_info():
    """
    get_info: for a given employee ID, returns information
    about his/her TODO list progress in CSV format.
    """

    # URLs to GET
    todo_url = f'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users'

    # GET User's name
    with urllib.request.urlopen(user_url) as user_response:
        user_data = json.loads(user_response.read().decode('utf-8'))

        employee_name_dict = {}

        for info in user_data:
            employee_id = info['id']
            employee_name = info['username']
            employee_name_dict[employee_id] = employee_name

    # GET todo of the user
    with urllib.request.urlopen(todo_url) as todo_response:
        todo_data = json.loads(todo_response.read().decode('utf-8'))

    # all tasks that are owned by this employee
    task_dict = {}
    for data in todo_data:
        user_id = data['userId']
        task_obj = {
                "username": employee_name_dict.get(user_id),
                "task": data['title'],
                "completed": data['completed'],
                }

        if user_id not in task_dict:
            task_dict[user_id] = []
        task_dict[user_id].append(task_obj)

    # dictionary
    json_object = json.dumps(task_dict)

    with open('todo_all_employees.json', 'w') as f:
        f.write(json_object)


if __name__ == '__main__':
    get_info()
