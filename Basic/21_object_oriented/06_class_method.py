# -*- coding = utf-8 -*-
# @Time : 2024/5/25 11:33
# @Author : Siegel
# @File : 06_class_method.py
# @Software : PyCharm
"""
类方法
    1. 类方法不需要依赖对象调用,需要加装饰器@classmethod
    2. 类方法中的参数不是一个对象,而是一个类
    3. 类方法中只可以使用类属性
    4. 类方法中不能使用对象方法
类方法的作用:
    因为只能访问类属性和类方法,所以在对象创建之前,可完成所需功能
"""


class Dog:
    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):  # self 对象
        print("Dog {} is running!".format(self.nickname))

    def eat_and_run(self):
        print("Dog {} is eating".format(self.nickname))
        self.run()  # 类中的普通兄弟方法,通过self.method_name()调用

    @classmethod
    def test(cls):  # cls class
        print(cls)  # <class '__main__.Dog'>
        print(cls.nickname)  # type object 'Dog' has no attribute 'nickname'


dog = Dog("curl")
dog.run()

try:
    # dog.test()
    Dog.test()
except Exception as err:
    print(err)
print("".center(60, '-'))


# 不依赖对象获取类属性,通过类方法修改属性实例
class Person:
    # 私有属性age
    __age = 20

    def show_age(self):
        print("this person is {} years old.".format(Person.__age))

    @classmethod
    def update_age_without_object(cls):
        cls.__age += 1

    @classmethod
    def get_age(cls):
        return cls.__age


print(Person.get_age())
Person.update_age_without_object()
print(Person.get_age())
