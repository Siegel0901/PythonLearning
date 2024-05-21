# -*- coding = utf-8 -*-
# @Time : 2024/5/21 21:01
# @Author : Siegel
# @File : 03_call.py
# @Software : PyCharm
"""
函数调用
    定义一个函数:给了函数一个名臣,指定了函数里包含的参数,和代码块结构
    这个函数的基本结构完成以后,可以通过另一个函数调用执行,也可以直接调用执行
"""


# 定义函数
def print_me(string):
    # 自定义函数调用print函数打印任何传入的字符串
    print(string)
    return


# 调用函数
print_me("我要调用用户自定义函数!")
print_me("再次调用同一函数")
