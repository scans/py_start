# encoding=utf-8

# define
names = ['chen','li','ouyang','sweet']

# index
print names[1]

print names[-1]

# insert
names.insert(1,'Tom')

# remove 出栈 pop([index]) -> item -- remove and return item at index (default last)
print names.pop()
print names.pop(1)

# replace
names[1]='Jerry'
print names[1]

# len
print len(names)

# Multi maintenance
p = ['asp','php']
s = ['c','java',p,'py']
print len(s)

