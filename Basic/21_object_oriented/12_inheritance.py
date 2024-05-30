# -*- coding = utf-8 -*-
# @Time : 2024/5/25 10:24
# @Author : Siegel
# @File : 12_inheritance.py
# @Software : PyCharm
"""
继承
    语法:
        class DerivedClassName(BaseClassName):
            <statement-1>
            .
            .
            .
            <statement-N>
    子类(派生类 DerivedClassName)会继承父类(基类 BaseClassName)的属性和方法
    BaseClassName(实例中的基类名)必须与派生类定义在一个作用域内
    除了类,还可以用表达式,基类定义在另一个模块中时这一点非常有用:
        class DerivedClassName(modname.BaseClassName):
"""


# 类定义:类名首字母大写,使用驼峰命名法
class People:
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __gender = 0

    # 定义构造方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender

    # 定义类的对象方法
    def speak(self):
        print("{} says: I am {} years old.".format(self.name, self.age))
        print("I am a {}.".format("boy" if self.__gender == 1 else "girl"))


# 单继承示例
class Student(People):
    university = ''

    def __init__(self, name, age, gender, school):
        # 调用父类的构造函数
        People.__init__(self, name, age, gender)
        self.university = school

    # 重写父类的方法
    def speak(self):
        print("{} is a student in {} university".format(
            self.name, self.university
        ))


student = Student('siegel', 24, 1, 'nankai')
student.speak()
