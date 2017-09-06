#!/usr/bin/env python
# encoding=utf-8

'关于os模块相关操作'


import os

print os.name

print os.uname()

print os.environ

print os.getenv('PATH')


def search(condition, file='.'):
    if os.path.isdir(file):
        for f in os.listdir(file):
            search(condition, f)
    else:
        if condition in file:
            print os.path.abspath(file)


if __name__ == '__main__':
    search('options')
