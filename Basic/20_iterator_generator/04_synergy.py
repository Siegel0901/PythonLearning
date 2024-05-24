# -*- coding = utf-8 -*-
# @Time : 2024/5/24 23:26
# @Author : Siegel
# @File : 04_synergy.py
# @Software : PyCharm

"""
利用生成器实现协程功能
"""


def task1(n):
    for i in range(n):
        print("moving the no.{} brick".format(i))
        yield None


def task2(n):
    for i in range(n):
        print("listening the no.{} song".format(i))
        yield None


g1 = task1(5)
g2 = task2(5)

while True:
    try:
        next(g1)
        next(g2)
    except Exception as err:
        print(err)
        break
