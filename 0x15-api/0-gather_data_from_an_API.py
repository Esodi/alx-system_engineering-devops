#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID """

import urllib.request
import sys
import json


def req(inpt):
    """ input processor """
    url = f'https://jsonplaceholder.typicode.com/todos/{inpt}'
    try:
        with urllib.request.urlopen(url) as resp:
            read = resp.read()
            data = json.loads(read)
        td = [t for t in data if t['completed']]
        tot = len(data)
        td_count = len(td)
        EMPLOYEE_NAME = data[0].get('name')
        NUMBER_OF_DONE_TASKS = td_count
        TOTAL_NUMBER_OF_TASKS = tot
        print(f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
        for i in td:
            print(f"\t {i['title']}")
    except urllib.error.HTTPError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    l = sys.argv[1]
    req(l)
