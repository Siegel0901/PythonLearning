# -*- coding = utf-8 -*-
# @Time : 2024/5/25 9:53
# @Author : Siegel
# @File : 04_self.py
# @Software : PyCharm
"""
self代表类的实例,而非类
    类的方法与普通的函数只有一个特别的区别:
        它们必须有一个额外的第一个参数名称，按照惯例它的名称是self
"""


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()
"""
以上实例执行结果为:
    <__main__.Test object at 0x00000160D2220DA0>
    <class '__main__.Test'>
从执行结果可以很明显的看出,self代表的是类的实例,代表当前对象的地址,而self.class则指向类
"""


# self不是Python关键字,可以替换成其他变量名
class Test:
    def prt(siegel):
        print(siegel)
        print(siegel.__class__)


t = Test()
t.prt()

"""
在Python中,self是一个惯用的名称,用于表示类的实例(对象)自身
它是一个指向实例的引用,使得类的方法能够访问和操作实例的属性
当你定义一个类,并在类中定义方法时,第一个参数通常被命名为self
尽管你可以使用其他名称,但强烈建议使用self,以保持代码的一致性和可读性
"""


class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)


# 创建一个类的实例
obj = MyClass(42)

# 调用实例的方法
obj.display_value()  # 输出42
"""
在上面的例子中,self是一个指向类实例的引用
它在__init__构造函数中用于初始化实例的属性,也在display_value方法中用于访问实例的属性
通过使用self,你可以在类的方法中访问和操作实例的属性,从而实现类的行为
"""
