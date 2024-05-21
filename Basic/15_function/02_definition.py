# -*- coding = utf-8 -*-
# @Time : 2024/5/21 20:47
# @Author : Siegel
# @File : 02_definition.py
# @Software : PyCharm
"""
函数定义:
    1. 函数代码块以def关键词开头,后接函数标识符名称和圆括号()
    2. 任何传入参数和自变量必须放在圆括号中间,圆括号之间可以用于定义参数
    3. 函数的第一行语句可以选择性地使用文档字符串——用于存放函数说明
    4. 函数内容以冒号:起始,并且缩进
    5. return [表达式]结束函数,选择性地返回一个值给调用方,不带表达式的return相当于返回None
语法:
    def 函数名 (参数列表):
        函数体
    默认情况下,参数值和参数名称是按函数声明中定义的顺序匹配起来的
"""


# 函数输出"Hello World"
def hello_world():
    print("Hello World")


hello_world()


# 比较两个数,返回较大的数
def max_num(a, b):
    if a > b:
        return a
    else:
        return b


bigger = max_num(1, 2)
print(bigger)

