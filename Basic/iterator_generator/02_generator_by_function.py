# -*- coding = utf-8 -*-
# @Time : 2024/5/24 19:04
# @Author : Siegel
# @File : 02_generator_by_function.py
# @Software : PyCharm

"""
定义生成器的方式
    1. 通过列表推导式定义生成器
    2. 借助函数定义生成器
"""
"""
借助函数定义生成器
    函数中出现了关键字yield,则表明当前函数是一个生成器
    步骤:
        1. 定义一个函数,函数中使用yield关键字
        2. 调用函数,接受调用结果得到生成器
        3. 借助于next()或者__next__()得到元素
        4. 函数中return语句的返回值在生成器遍历结束后通过StopIteration异常返回
"""


def foobar():
    n = 0
    while True:
        n += 1
        yield n  # 相当于return n ＋ 暂停
        if n == 10:
            break


print(type(foobar()))
g = foobar()
while True:
    try:
        print(next(g))
    except Exception as err:
        print(err)
        break


# 用生成器实现斐波那契数列
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield a
        a, b = b, a + b
        n += 1

    return "out of length"


g = fib(8)
while True:
    try:
        print(next(g), end=' ')
    except Exception as err:
        print()
        print(err)
        break
