# -*- coding = utf-8 -*-
# @Time : 2024/5/21 20:30
# @Author : Siegel
# @File : 01_mutable_immutable.py
# @Software : PyCharm
"""
可变对象和不可变对象
    不可变对象:对象所指向的内存中的值不可以改变
    不可变数据类型:
        int str float tuple
    可变对象:对象所指向的内存中的值可以改变
    可变数据类型:
        list dict
"""
# 不可变类型
a = 1
print(id(a))
a = 2
print(id(a))
print("".center(50, '-'))

str1 = 'siegel'
print(id(str1))
str1 = 'Siegel'
print(id(str1))
print("".center(50, '-'))

f = 0.1
print(id(f))
f = 0.901
print(id(f))
print("".center(50, '-'))

t = (1, 2, 3, 4)
print(id(t))
t = (1, 2, 3)
print(id(t))
print("".center(50, '-'))

# 可变类型
list1 = [1, 2, 3, 4]
print(id(list1), list1)
list1.pop()
print(id(list1), list1)
print("".center(50, '-'))

dict1 = dict()
print(id(dict1), dict1)
dict1.update({"key": "value"})
print(id(dict1), dict1)
