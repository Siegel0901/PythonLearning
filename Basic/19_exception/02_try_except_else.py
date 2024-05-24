# -*- coding = utf-8 -*-
# @Time : 2024/5/24 15:52
# @Author : Siegel
# @File : 02_try_except_else.py
# @Software : PyCharm
"""
try:
    有可能有异常的代码
except 类型1:
    pass
...
else:
    如果try中没有发生异常则进入的代码

注意:
    如果使用else则在try代码中不能出现return
"""


def foobar():
    try:
        num = int(input("please input a number:"))
        print(num)
        # return num
    except ValueError as error:
        print(error)
    else:
        print("number input successfully")


foobar()
