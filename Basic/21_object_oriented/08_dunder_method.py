# -*- coding = utf-8 -*-
# @Time : 2024/5/25 15:09
# @Author : Siegel
# @File : 08_dunder_method.py
# @Software : PyCharm
"""
魔术方法:
    定义在类中的特殊方法,在特殊时刻触发,形式:__methodName__
    __new__:
        触发时机:实例化对象时触发
        从一个class建立一个object的过程
        __new__是创建object,因此它是有返回值的,必须返回这个object
    __init__:
        触发时机:初始化对象时触发
        有了object之后,给object初始化的过程
        __init__没有返回值,__init__里面的self就是要初始化的对象
    __call__:
        触发时机:实例当做函数使用时触发
        如果想把实例当做函数使用,则需重写__call__方法
        当使用实例被当做函数使用时,默认调用__call方法
    __str__:相当于Java中的toString
        触发时机:打印对象名时自动触发,调用__str__里面的内容
        注意:一定要在__str__方法中添加return,return后面内容就是打印对象看到的内容
    __del__:
        触发时机:没有任何变量引用实例时触发
        参数:self
        返回值:无
        作用:实例使用完回收资源
"""
import sys


class Person:
    def __new__(cls, *args, **kwargs):
        print("this is __new__ method.")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print("this is __init__ method.")


"""
this is __new__ method.
this is __init__ method.
"""
person = Person()
"""
粗略理解为:先调用__new__,再调用__init__
obj = __new__(Person)
__init__(obj)
如果我们在建立object的时候传入了参数,则参数既会传给__new__,也会传给__init__
在我们实际的应用中,__new__函数用到的是相对较少的
如果不需要客制化建立这个object的过程,只需要初始化这个object,则只需要用到__init__
"""

print("".center(60, '-'))

"""
__call__:
    如果想把实例当做函数使用,则需重写__call__方法
    当使用实例被当做函数使用时,默认调用__call方法
"""


class CallClass:
    def __call__(self, info):
        print("this is __call__ method")
        self.info = info
        print(self.info)


c = CallClass()

print(c)
c("siegel")
print("".center(60, '-'))

"""
__str__:相当于Java中的toString
    触发时机:打印对象名时自动触发,调用__str__里面的内容
    注意:一定要在__str__方法中添加return,return后面内容就是打印对象看到的内容
"""


class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


n1 = Name('siegel')
n2 = Name('luis')

print(n1, n2)

print("".center(60, '-'))
"""
    __del__:析构函数
        触发时机:没有任何变量引用实例时触发
        参数:self
        返回值:无
        作用:实例使用完回收资源
"""


class Test:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("this is {}'s __del__ method".format(self.name))


t1 = Test("t1")
t2 = Test("t2")
# 删除t1对地址的引用
del t1  # 调用析构函数,打印this is t1's __del__ method
# 查看对地址的引用次数
print(sys.getrefcount(t2))  # 2
print(t2)  # <__main__.Test object at 0x000001BF8C572870>
# 程序结束后,垃圾回收机制回收t2所指的内存,调用析构函数,打印this is t2's __del__ method
