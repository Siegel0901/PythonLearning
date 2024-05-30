# -*- coding = utf-8 -*-
# @Time : 2024/5/30 22:19
# @Author : Siegel
# @File : 02_import.py
# @Software : PyCharm
"""
    1. 系统模块和自定义模块
"""

# 导入自定义模块calculate
import calculate

add_result = calculate.add(*calculate.list1)
minus_result = calculate.minus(*calculate.list1)
multiply_result = calculate.multiply(*calculate.list1)
divide_result = calculate.divide(*calculate.list1)

print(add_result, minus_result, multiply_result, divide_result)

"""
可以使用模块中的变量、函数和类
    模块名.变量
    模块名.函数()
    模块名.类()
"""
