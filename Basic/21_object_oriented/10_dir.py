# -*- coding = utf-8 -*-
# @Time : 2024/5/26 10:33
# @Author : Siegel
# @File : 10_dir.py
# @Software : PyCharm
"""
dir()函数:
    用于查找对象的所有属性和方法
语法:
    dir([object])
    object是要查找属性和方法的对象
    如果省略,则返回当前作用域中的所有变量、方法和定义的类型
返回值
    dir()函数返回一个包含对象的所有属性和方法名称的字符串列表.
    这些名称按照字母顺序排序,并包括以下几种类型的信息:
        对象的属性(变量)
        对象的方法(函数)
        内置函数和变量
        类型信息
"""


class Student:
    __name = str()
    __age = int()

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("age error")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


student = Student()
print(dir(student))
# 私有化只不过是系统自动将私有属性改名导致无法用原来的属性名访问
print(student._Student__age)  # 虽然可以通过这种方式访问,但是失去了私有化的意义,并不推荐
print(student.get_age())
print(student.__dir__())
