# -*- coding = utf-8 -*-
# @Time : 2024/5/24 23:05
# @Author : Siegel
# @File : 03_send.py
# @Software : PyCharm
"""
生成器方法:
    __next__()
        获取下一个元素
    send(value)
        向每次生成器调用中传值
        第一次调用send()时,必须向其中传None
"""


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print("temp={}".format(temp))
        for x in range(temp):
            print(x, end=' ')
        print()
        i += 1


g = gen()
n0 = g.send(None)
print("n0={}".format(n0))

n1 = g.send(3)
print("n1={}".format(n1))

n2 = g.send(5)
print("n2={}".format(n2))
