#!/usr/bin/env python
# encoding=utf-8

'对于python来说变量作用域只是约定俗称的东西，不管怎么声明都可以在外部调用。
private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。'

def _private1():
    print 'private function 1'


def _private2():
    print 'private function 2'



def publicFunction():
    _private1()
    _private2()
