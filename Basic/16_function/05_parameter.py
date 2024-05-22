# -*- coding = utf-8 -*-
# @Time : 2024/5/21 21:37
# @Author : Siegel
# @File : 05_parameter.py
# @Software : PyCharm
"""
以下是调用函数时可使用的正式参数类型:
    必需参数
    关键字参数
    默认参数
    不定长参数
"""
"""
必需参数:
    必需参数须以正确的顺序传入参数
    调用时的数量必须和声明时的一样
"""


# 可写函数说明
def print_me(string):
    # "打印任何传入的字符串"
    print(string)
    return


# 调用 print_me 函数，不加参数会报错
# print_me()
print("".center(50, '-'))

"""
关键字参数
    关键字参数和函数调用关系密切,函数调用使用关键字参数来确定传入的参数值
    使用关键字参数允许函数调用时参数的顺序与声明时不一致,因为Python解释器能够用参数名匹配参数值
"""


def print_info(name, age):
    print("name={},age={}".format(name, age))
    return


print_info(age=24, name='Siegel')
print("".center(50, '-'))

"""
默认参数
    调用函数时,如果没有传递参数,则会使用默认参数
"""


def print_info(name, age=24):
    print("name={},age={}".format(name, age))
    return


print_info(name='Siegel')
print("".center(50, '-'))

"""
不定长参数
    不定长参数使函数能处理比当初声明时更多的参数
    不定长参数在声明时不会命名
基本语法如下:
    def function_name([formal_args,] *var_args_tuple):
        function_suite
        return [expression]
加了星号*的参数会以元组(tuple)的形式导入,存放所有未命名的变量参数
"""


def print_info(arg1, *var_tuple):
    print(arg1, var_tuple)
    for var in var_tuple:
        print(var)


print_info('Siegel', 24, 2000, '0901')
# 未指定参数时,是一个空元组
print_info('Siegel')
print("".center(50, '-'))

"""
不定长参数带两个星号**的语法:
    def function_name([formal_args,] **var_args_dict):
        function_suite
        return [expression]
"""


def print_info(arg1, **var_dict):
    print(arg1, var_dict)
    for var in var_dict:
        print(var)


print_info('Siegel', age=24, year=2000, month_and_day='0901')
# 未指定参数时,是一个空字典
print_info('Siegel')
print("".center(50, '-'))

"""
声明函数时,单独出现星号*
    如果单独出现星号*，则星号*后的参数必须用关键字传入
"""


def func(a, b, *, c):
    return a + b + c


# 报错
# print(f(1, 2, 3))
print(func(1, 2, c=3))
print("".center(50, '-'))

"""
强制位置参数
    用/来指明函数形参必须使用指定位置参数,不能使用关键字参数
"""


# 形参a和b必须使用指定位置参数
# c或d可以是位置参数或关键字形参
# 而e和f要求为关键字形参
def func(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


# 以下使用方法是正确的
func(1, 2, 3, d=3, e=4, f=5)
func(10, b=20, c=30, d=40, e=50, f=60)  # b 不能使用关键字参数的形式
func(10, 20, 30, 40, 50, f=60)  # e 必须使用关键字参数的形式
