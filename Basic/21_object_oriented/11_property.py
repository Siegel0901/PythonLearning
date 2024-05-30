# -*- coding = utf-8 -*-
# @Time : 2024/5/26 10:48
# @Author : Siegel
# @File : 11_property.py
# @Software : PyCharm
"""
@property装饰器
    先设置get方法再设置set方法:set方法依赖于get方法
    get方法的设置:
        取私有属性名作为方法名,参数为self,在方法前加上装饰器@property
    set方法的设置:
        取私有属性名作为方法名,参数为self和value,在方法前加上装饰器@私有属性名.setter
"""


class Student:
    name = str()
    __age = int()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("age error")


student = Student()
print(student.name)
print(student.age)
student.name = "siegel"
student.age = 24
print(student.name)
print(student.age)
