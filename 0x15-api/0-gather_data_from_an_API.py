#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID """

import urllib.request
import sys
import json


def req(inpt):
    """ input processor """
    url = f'https://jsonplaceholder.typicode.com/todos/'
    try:
        with urllib.request.urlopen(url) as resp:
            read = resp.read()
            data = json.loads(read)
        lst = []
        for n in range(len(data)):
            if data[n]['userId'] == int(inpt):
                lst.append(data[n])
        td = [i for i in lst if i['completed'] is True]
        tot = len(lst)
        td_count = len(td)
        EMPLOYEE_NAME = int(inpt)
        NUMBER_OF_DONE_TASKS = td_count
        TOTAL_NUMBER_OF_TASKS = tot
        print(
                f'Employee {EMPLOYEE_NAME} is done with ' +
                f'tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):'
                )
        for j in td:
            print(f"\t {j['title']}")
    except urllib.error.HTTPError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    req(sys.argv[1])
