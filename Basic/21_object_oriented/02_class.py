# -*- coding = utf-8 -*-
# @Time : 2024/5/25 9:42
# @Author : Siegel
# @File : 02_class.py
# @Software : PyCharm
"""
类定义:
    语法格式如下:
        class ClassName:
            <statement-1>
            ...
            ...
            <statement-n>
    类实例化后,可以使用其属性
    实际上,创建一个类之后,可以通过类名访问其属性
类对象:
    类对象支持两种操作:属性引用和实例化
    属性引用使用和Python中所有属性引用一样的标准语法:obj.name
    类对象创建后,类命名空间中所有命名都是有效属性名
"""


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def foobar(self):
        return "hello world"


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass类的属性i为:{}".format(x.i))
print("MyClass类的方法foobar输出为:{}".format(x.foobar()))
