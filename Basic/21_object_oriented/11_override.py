# -*- coding = utf-8 -*-
# @Time : 2024/5/25 10:44
# @Author : Siegel
# @File : 11_override.py
# @Software : PyCharm
"""
如果你的父类方法的功能不能满足你的需求,你可以在子类重写你父类的方法
"""


class Parent:  # 定义父类
    def my_method(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def my_method(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.my_method()  # 子类调用重写方法
# super()函数是用于调用父类(超类)的一个方法
super(Child, c).my_method()  # 用子类对象调用父类已被覆盖的方法
print("".center(60, '-'))

"""
构造方法重写:
    情况一:
        子类需要自动调用父类的方法:
            子类不重写__init__()方法,实例化子类后,会自动调用父类的__init__()的方法
    情况二:
        子类不需要自动调用父类的方法:
            子类重写__init__()方法,实例化子类后,将不会自动调用父类的__init__()的方法
    情况三:
        子类重写__init__()方法又需要调用父类的方法:
            使用super关键词：
"""


# 情况一
class Father(object):
    def __init__(self, name):
        self.name = name
        print("name: %s" % self.name)

    def get_name(self):
        return 'Father ' + self.name


class Son1(Father):
    def get_name(self):
        return 'Son ' + self.name


son = Son1('siegel')
print(son.get_name())
print("".center(60, '-'))


# 情况二
class Son2(Father):
    def __init__(self, name):
        print("hi")
        self.name = name

    def get_name(self):
        return 'Son2 ' + self.name


son = Son2('siegel')
print(son.get_name())
print("".center(60, '-'))

"""
情况三:
    如果重写了__init__时,要继承父类的构造方法,可以使用super关键字:
        super(子类, self).__init__(参数1, 参数2, ....)
    还有一种经典写法:
        父类名称.__init__(self, 参数1, 参数2, ...)
"""


class Son3(Father):
    def __init__(self, name):
        super(Son3, self).__init__(name)
        Father.__init__(self, name)
        print("hi")
        self.name = name

    def get_name(self):
        return 'Son ' + self.name


son = Son3('siegel')
print(son.get_name())
