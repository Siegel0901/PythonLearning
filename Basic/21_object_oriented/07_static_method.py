# -*- coding = utf-8 -*-
# @Time : 2024/5/25 14:30
# @Author : Siegel
# @File : 07_static_method.py
# @Software : PyCharm
"""
静态方法:类似于类方法
    1. 需要装饰器@staticmethod
    2. 静态方法无需传递参数(cls、self等)
    3. 也只能访问类的属性和方法,无法访问对象(self)的属性和方法
    4. 不同于类方法的地方:
        1. 装饰器不同
        2. 无需参数
    5. 相同于类方法的地方:
        1. 只能访问类的属性和方法,对象的属性和方法无法访问
        2. 都可以通过类名调用访问
        3. 由于不依赖于对象,都可以在创建对象之前使用
对象方法与二者的不同之处:
    1. 对象方法没有装饰器
    2. 依赖于对象,每个对象方法都有self
    3. 只有创建了对象才可以调用对象方法,否则无法调用
"""


class MyClass:
    __attr1 = 'default_value'

    def __init__(self, attr):
        self.__attr1 = attr

    @staticmethod
    def my_static():
        print("this is a static method")
        print("class attr:{}".format(MyClass.__attr1))


MyClass.my_static()
