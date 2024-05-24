# -*- coding = utf-8 -*-
# @Time : 2024/5/24 18:44
# @Author : Siegel
# @File : 01_generator_by_comprehensions.py
# @Software : PyCharm
"""
通过列表推导式,我们可以直接创建一个列表
但是,受到内存的限制,列表容量肯定是有限的
创建一个包含100万个元素的列表,会占用很大的存储空间
如果我们仅仅需要访问前面几个元素,那后面绝大多数元素占用的空间就白白浪费了
所以,如果列表元素可以按照某种算法推算出来,那我们是否可以在循环的过程中不断推算出后续的元素呢?
这样就不必创建完整的list,从而节省大量的空间
在Python中,这种一边循环一边计算的机制,称为生成器:generator
"""

"""
定义生成器的方式
    1. 通过列表推导式定义生成器
    2. 借助函数定义生成器
"""
# 列表推导式声明列表
numbers = [x * 3 for x in range(3)]
print(type(numbers))
print(numbers)
print("".center(50, '-'))

# 通过列表推导式得到生成器
g = (x * 3 for x in range(3))
print(type(g))
print(g)
print("".center(50, '-'))

"""
如何得到生成器中的元素:
    方式1:通过调用__next__()得到元素
    方式2:通过next(),每调用一次next生产一个元素
"""
# 方式1:通过调用__next__()得到元素
print(g.__next__())  # 0
# 方式2:通过next(),每调用一次next生产一个元素
print(next(g))  # 3

"""
StopIteration异常:
    当生成器遍历到最后一个元素还继续取下一个元素时,会抛出StopIteration异常
"""
while True:
    try:
        print(next(g))
    except Exception as error:
        print(error)
        print("at the end")
        break
