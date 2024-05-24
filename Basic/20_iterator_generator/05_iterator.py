"""
迭代器
    迭代是Python最强大的功能之一,是访问集合元素的一种方式
    迭代器是一个可以记住遍历的位置的对象
    迭代器对象从集合的第一个元素开始访问,直到所有的元素被访问完结束
    迭代器只能往前不会后退
    迭代器有两个基本的方法:iter()和next()
"""
try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

"""
可迭代对象:
    1. 生成器
    2. 元组 列表 集合 字典 字符串
如何判断一个对象是否可迭代?
    isinstance(对象, Iterable)
可迭代对象一定是迭代器吗?
    可以被next()函数调用,并不断返回下一个值的对象称为迭代器:Iterable
    生成器是可迭代的,也是迭代器
    list是可迭代的,但不是迭代器
    通过iter()函数,将可迭代对象变成一个迭代器
生成器和迭代器的关系:
    生成器是迭代器的一种,元组 列表 集合 字典 字符串等可由iter()函数转为迭代器
"""

# 判断一个对象是否可迭代
list1 = list()
print(isinstance(list1, Iterable))  # True
print(isinstance('abd', Iterable))  # True
print(isinstance(100, Iterable))  # False
print(type((i + 1 for i in range(10))))  # <class 'generator'>
print(isinstance((i + 1 for i in range(10)), Iterable))  # True
print("".center(60, '-'))

# 测试list是否为迭代器
try:
    list1 = [i for i in range(10)]
    print(next(list1))
except Exception as err:
    print(err)  # 'list' object is not an iterator
print("".center(60, '-'))
"""
    字符串,列表或元组对象都可用于创建迭代器
    通过iter()函数将可迭代对象变成一个迭代器
"""
list1 = [1, 2, 3, 4]
it = iter(list1)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))
print("".center(60, '-'))

# 迭代器对象可以使用常规for语句进行遍历
it = iter(list1)  # 创建迭代器对象
for x in it:
    print(x, end=" ")
print()

print("".center(60, '-'))

# 用while循环和迭代器迭代列表
it = iter(list1)  # 创建迭代器对象

while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
