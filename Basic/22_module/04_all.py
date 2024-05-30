# -*- coding = utf-8 -*-
# @Time : 2024/5/30 22:32
# @Author : Siegel
# @File : 04_all.py
# @Software : PyCharm
"""
from 模块名 import *
    星号*代表该模块中所有可以访问的内容
    在模块中使用__all__可以设置对外开放的变量,函数,类
"""
from calculate import *

print(list1)

# 使用星号*运算法展开list1列表中的所有元素传给calculate模块中的函数
add_result = add(*list1)
print(add_result)
minus_result = minus(*list1)
print(minus_result)
multiply_result = multiply(*list1)
print(multiply_result)
