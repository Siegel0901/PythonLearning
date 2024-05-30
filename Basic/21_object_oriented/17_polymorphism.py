# -*- coding = utf-8 -*-
# @Time : 2024/5/30 15:57
# @Author : Siegel
# @File : 17_polymorphism.py
# @Software : PyCharm
"""
多态:
    参数为父类对象,可以接受继承父类的子类对象
"""


class Pet:
    role = None

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show_info(self):
        print("{} is {} years old.".format(self.nickname, self.age))


class Cat(Pet):
    role = 'cat'


class Dog(Pet):
    role = 'dog'


class Tiger:
    role = 'tiger'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age


class Person:
    def __init__(self, name):
        self.name = name

    def show_pet(self, pet):
        if isinstance(pet, Pet):
            """
                pet既可以接收cat,也可以接收dog,还可以接收tiger
                isinstance(obj, 类) --> 判断obj是不是类的对象或者判断obj是不是该类子类的对象
            """
            print("{} has a {}. it's nickname is {}.".format(self.name, pet.role, pet.nickname))
        else:
            print("not Pet class")


person = Person('siegel')
cat = Cat('kitty', 2)
dog = Dog('puppy', 3)
tiger = Tiger('kate', 4)
person.show_pet(cat)
person.show_pet(dog)
person.show_pet(tiger)
