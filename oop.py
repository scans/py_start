#!/usr/bin/env python
# encoding=utf-8


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def toString(self):
        print 'name:%s ; score: %s' % (self.name, self.score)


class Animal(object):
    def run():
        pass


class Dog(Animal):
    def run(self):
        print 'dog run...'


class Cat(Animal):
    def run(self):
        print 'cat run...'
