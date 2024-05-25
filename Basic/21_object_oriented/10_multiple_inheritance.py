# -*- coding = utf-8 -*-
# @Time : 2024/5/25 10:33
# @Author : Siegel
# @File : 10_multiple_inheritance.py
# @Software : PyCharm
"""
多继承语法:
    class DerivedClassName(Base1, Base2, Base3):
        <statement-1>
        .
        .
        .
        <statement-N>
    需要注意圆括号中父类的顺序
        若是父类中有相同的方法名,而在子类使用时未指定,python从左至右搜索
        即方法在子类中未找到时,从左到右查找父类中是否包含方法
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

    def __init__(self, name, age, gender, university):
        # 调用父类的构造函数
        People.__init__(self, name, age, gender)
        self.university = university

    # 重写父类的方法
    def speak(self):
        print("{} is a student in {} university".format(
            self.name, self.university
        ))


# 另一个类,多继承之前的准备
class Programmer:
    name = ''
    language = ''

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def speak(self):
        print("My name is %s." % self.name)
        print("I am a programmer.")
        print("I am good at coding with {}.".format(self.language))


class Sample(Programmer, Student):
    def __init__(self, name, age, gender, university, language):
        Student.__init__(self, name, age, gender, university)
        Programmer.__init__(self, name, language)


test = Sample("siegel", 24, 1, "nankai", "Python")
# 方法名相同,默认调用的是在括号中参数位置排前父类的方法
test.speak()
