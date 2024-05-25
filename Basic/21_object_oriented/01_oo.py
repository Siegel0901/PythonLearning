# -*- coding = utf-8 -*-
# @Time : 2024/5/25 7:52
# @Author : Siegel
# @File : 01_oo.py.py
# @Software : PyCharm
"""
Python3 面向对象
面向对象技术简介:
    类(Class):
        用来描述具有相同的属性和方法的对象的集合
        它定义了该集合中每个对象所共有的属性和方法
        对象是类的实例
    方法:
        类中定义的函数
    类变量:
        类变量在整个实例化的对象中是公用的
        类变量定义在类中且在函数体之外
        类变量通常不作为实例变量使用
    数据成员:
        类变量或实例变量用于处理类及其实例对象的相关的数据
    方法重写:
        如果从父类继承的方法不能满足子类的需求,可以对其进行改写,这个过程叫方法的覆盖(override),也称为方法的重写
    局部变量:
        定义在方法中的变量,只作用于当前实例的类
    实例变量:
        在类的声明中,属性是变量来表示的,这种变量就称为实例变量,实例变量就是一个用self修饰的变量
    继承:
        即一个派生类(derived class)继承基类(base class)的字段和方法
        继承允许把一个派生类的对象作为一个基类对象对待
    实例化:
        创建一个类的实例,类的具体对象
    对象:
        通过类定义的数据结构实例
        对象包括两个数据成员(类变量和实例变量)和方法
    和其他编程语言相比,Python在尽可能不增加新的语法和语义的情况下加入了类机制
    Python中的类提供了面向对象编程的所有基本功能:
        类的继承机制允许多个基类,派生类可以覆盖基类中的任何方法,方法中可以调用基类中的同名方法
    对象可以包含任意数量和类型的数据
"""
