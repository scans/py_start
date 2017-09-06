#!/usr/bin/env python
# encoding=utf-8


# 读取文件默认按照字符串读取
with open('./decorator.py') as f:
    for line in f.readlines():
        print line.strip()


# 按照二进制读取
with open('./file_io.py', 'rb') as f:
    pass

import chardet
import codecs
# 指定编码
with open('./gbk.txt') as f:
    data = f.read()
    fencoding = chardet.detect(data)
    print fencoding
    if fencoding['encoding'] and fencoding['encoding'].lower() == 'gbk':
        print data.decode('gbk')

# 使用codecs模块读取时指定编码
# with codecs.open('./gbk.txt', 'r', 'gbk') as f1:
#    print f1.read()

# 写文件
with open('./gbk.txt', 'w') as f:
    f.write('hello china\n')
    f.write('hello chen\n')
    f.write('你好，中国\n')

# 指定编码写文件
with codecs.open('./gbk.txt', 'w', 'gbk') as f:
    f.write(u'你好中国\n')
