# -*- coding = utf-8 -*-
# @Time : 2024/5/30 22:19
# @Author : Siegel
# @File : 03_from_import.py
# @Software : PyCharm
"""
    2. 导入模块的方式
        1. import 模块名
            模块名.变量
            模块名.函数
            模块名.类
        2. from 模块名 import 变量 | 函数 | 类
            在代码中可以直接使用导入模块的变量,函数,类
            不用加模块名
        3. from 模块名 import *
            星号*代表该模块的所有内容
"""
from calculate import add, minus, list1

print(list1)

# 使用星号*运算法展开list1列表中的所有元素传给calculate模块中的函数
add_result = add(*list1)
print(add_result)
minus_result = minus(*list1)
print(minus_result)
