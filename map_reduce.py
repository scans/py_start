#!/usr/bin/env python
# encoding=utf-8

print map(str, [1, 2, 3, 4, 7, 5, 6])

print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6])


# map处理数据，数据规范
user_names = ['chen', 'tOM', 'JERRy']


def format_name(name):
    name_str = ''
    for i, c in enumerate(name):
        if i == 0:
            name_str += c.upper()
        else:
            name_str += c.lower()
    return name_str


print map(format_name, user_names)
print map(str.capitalize, user_names)


def prod(numbers):
    print numbers
    return reduce(lambda x, y: x * y, numbers)

print prod(range(1,4))
