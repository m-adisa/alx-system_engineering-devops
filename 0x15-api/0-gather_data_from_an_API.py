#!/usr/bin/python3
"""a script that returns the todo list of an employee
with a given ID """


import requests
import sys

if __name__ == "__main__":

    """get the id from the user input"""
    userId = sys.argv[1]
    """ the response to the client is served by this request"""
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
            )

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print(
            'Employee {} is done with tasks({}/{}):'
            .format(name, completed, totalTasks)
    )

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
