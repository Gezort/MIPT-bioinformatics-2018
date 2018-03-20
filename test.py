#!/usr/bin/env python3
import bs4
import os
import requests
from argparse import ArgumentParser
from contextlib import ContextDecorator
from copy import deepcopy
from functools import wraps

MAIN_PAGE = 'http://rosalind.info'
LOGIN_PAGE = '%s/accounts/login/' % MAIN_PAGE
CLASS_PAGE = '%s/classes/489/' % MAIN_PAGE

def get_credentials():
    login = os.getenv('ROSALIND_LOGIN')
    password = os.getenv('ROSALIND_PASSWORD')
    if not login:
        print('please set $ROSALIND_LOGIN')
        exit(1)
    if not password:
        print('please set $ROSALIND_PASSWORD')
        exit(1)
    return login, password


class client(ContextDecorator):
    def __init__(self):
        self._client = requests.session()
        login, password = get_credentials()
        self._login = login
        self._password = password
        self._client.get(LOGIN_PAGE)
        self._csrftoken = self._client.cookies['csrftoken']

    def _with_cookie(method):
        @wraps(getattr(requests.sessions.Session, method.__name__))
        def wrapped(self, *args, **kwargs):
            if 'data' not in kwargs:
                kwargs['data'] = {}
            else:
                kwargs['data'] = kwargs['data'].copy()
            kwargs['data']['csrfmiddlewaretoken'] = self._csrftoken
            kwargs['data']['username'] = self._login
            kwargs['data']['password'] = self._password
            return method(self, *args, **kwargs)
        return wrapped

    @_with_cookie
    def post(self, *args, **kwargs):
        return self._client.post(*args, **kwargs)

    @_with_cookie
    def get(self, *args, **kwargs):
        return self._client.post(*args, **kwargs)

    def __enter__(self):
        r = self.post(LOGIN_PAGE)
        return self

    def __exit__(self, *exc):
        self._client.close()


def get_task_url(cl, task):
    r = cl.get(CLASS_PAGE)
    page = bs4.BeautifulSoup(r.content, 'lxml')
    tbody = page.find_all('tbody')[0]
    tr = list(tbody.find_all('tr'))[task - 1]
    href = list(tr.find_all('td'))[1]
    href = href.a['href']
    return '%s%s' % (MAIN_PAGE, href)


def get_input_output(cl, url):
    page = bs4.BeautifulSoup(cl.get(url).content, 'lxml')
    data = list(page.find_all('div', {'class': 'codehilite'}))
    input = data[0].pre.text
    output = data[1].pre.text
    return input, output


def main():
    parser = ArgumentParser()
    parser.add_argument(
            'task', type=int, choices=range(1, 31),
            help='rosalind task number')
    args = parser.parse_args()
    with client() as cl:
        url = get_task_url(cl, args.task)
        input, output = get_input_output(cl, url)
        with open('input', 'w') as fin:
            fin.write(input)
        with open('ethalon', 'w') as fout:
            fout.write(output)
        os.system('python3 ./%d.py < input > output && '
                  'diff -w output ethalon && echo "OK"' % args.task)


if __name__ == '__main__':
    main()
