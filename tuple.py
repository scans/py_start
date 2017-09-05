#encoding=utf-8


# tuple 不可变的list

# define 
tuple=(1,2,3,4)

# 陷阱：定义单元素的tuple
a=(1) # 这样定义会被认为是一个数字
print a
b=(1,) #单元素tuple必须这样定义
print b 

