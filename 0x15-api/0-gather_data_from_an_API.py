#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID """


import json
import sys
import urllib.request


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
        name = None
        for h in td:
            if h['id'] == id:
                name = h.get('name')
        todos_done = td_count
        todos_count = tot
        print(
                'Employee {} is done with tasks({}/{}):\
'.format(name, todos_done, todos_count)
                )
        name = None
        for j in td:
            print(f"\t {j['title']}")
    except urllib.error.HTTPError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    req(sys.argv[1])
