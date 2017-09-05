# encoding=utf-8
# 列表生成表达式


a = [x * x for x in range(1, 11)]
print a


# 尾部跟if
b = [x * x for x in range(1, 11) if x % 2 == 0]
print b


# 全排列
c = [m + n for m in 'ABCDE' for n in 'XYZ']
print c

# 遍历目录
import os
print [d for d in os.listdir('.')]

# 遍历dict
map = {'a': '1', 'b': '2', 'c': '3'}
print [x + '=' + y for x, y in map.iteritems()]

# 小写

print [x.lower() for x in ['cHen', 'Gogole', 'Baidu', 18, 'duckGO'] if isinstance(x, str)]
