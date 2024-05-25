# -*- coding = utf-8 -*-
# @Time : 2024/5/25 10:11
# @Author : Siegel
# @File : 05_object_method.py
# @Software : PyCharm
"""
类的对象方法:
    在类的内部,使用def关键字来定义一个对象方法
    与一般函数定义不同,对象方法必须包含参数self,且为第一个参数
    self代表的是类的实例(对象)
        def method_name(self)
            pass
    类的对象方法需要依赖对象调用
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


# 实例化类
p = People("siegel", 24, 1)
p.speak()

# 访问实例的私有属性
try:
    print(p.__gender)
except Exception as err:
    print(err)  # 'People' object has no attribute '__gender'
