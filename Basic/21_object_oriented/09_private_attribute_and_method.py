# -*- coding = utf-8 -*-
# @Time : 2024/5/25 11:04
# @Author : Siegel
# @File : 09_private_attribute_and_method.py
# @Software : PyCharm
"""
类属性与方法
    类的私有属性
        __private_attrs:
            两个下划线开头,声明该属性为私有,不能在类的外部被使用或直接访问
            在类内部的方法中使用时self.__private_attrs
    类的私有方法
        __private_method:
            两个下划线开头,声明该方法为私有方法,只能在类的内部调用,不能在类的外部调用
            self.__private_methods
"""


# 类的私有属性
class JustCounter:
    __secretCount = 0  # 私有属性
    publicCount = 0  # 公共属性

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


try:
    counter = JustCounter()
    counter.count()
    counter.count()
    print(counter.publicCount)
    print(counter.__secretCount)  # 报错，实例不能访问私有变量
except Exception as err:
    print(err)  # 'JustCounter' object has no attribute '__secretCount'
print("".center(60, '-'))


# 类的私有方法
class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()  # 私有方法可以在类内部使用


try:
    x = Site('Siegel个人博客', 'www.siegel.top')
    x.who()  # 正常输出
    x.foo()  # 正常输出
    x.__foo()  # 报错
except Exception as err:
    print(err)

"""
dunder methods:     格式:__方法名__
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __truediv__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
"""
print("".center(60, '-'))

"""
私有化好处:
    1. 隐藏属性不被外界随意修改
    2. 通过声明get和set方法修改
        def setXX(self, XX):
            # 筛选赋值内容
            if xxx符合条件:
                self.__XX = XX
            else:
                不赋值
        def getXX(self)
            return self.__XX
"""


class Student:
    __name = str()
    __age = int()
    __college = str()

    # 定义get和set方法
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("age error")

    def set_college(self, college):
        self.__college = college

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_college(self):
        return self.__college

    def __str__(self):
        return "name={}, age={}, college={}".format(self.__name, self.__age, self.__college)


student = Student()
student.set_name('siegel')
student.set_age(24)
student.set_college('nankai')
print(student)

student.set_age(150)
print(student.get_name(), student.get_age(), student.get_college())
