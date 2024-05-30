# -*- coding = utf-8 -*-
# @Time : 2024/5/30 21:55
# @Author : Siegel
# @File : calculate.py
# @Software : PyCharm
__all__ = ['add', 'minus', 'multiply', 'list1']

# 导入系统模块random
import random


def add(*args):
    if len(args) > 1:
        total = 0
        for i in args:
            total += i
        return total
    else:
        print("at least 2 parameters to calculate.")
        return 0


def minus(*args):
    if len(args) > 1:
        total = args[0]
        for i in args[1:]:
            total -= i
        return total
    else:
        print("at least 2 parameters to calculate.")
        return 0


def multiply(*args):
    if len(args) > 1:
        total = args[0]
        for i in args[1:]:
            total *= i
        return total
    else:
        print("at least 2 parameters to calculate.")
        return 0


def divide(*args):
    if len(args) > 1:
        total = args[0]
        for i in args[1:]:
            total /= i
        return total
    else:
        print("at least 2 parameters to calculate.")
        return 0


list1 = list()
for i in range(random.randint(1, 10)):
    list1.append(random.randint(1, 10))


def test():
    print("this is test method in calculate.")


print('__name__:', __name__)

if __name__ == '__main__':
    print(__name__)
    test()
