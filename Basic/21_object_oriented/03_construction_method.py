# -*- coding = utf-8 -*-
# @Time : 2024/5/25 9:48
# @Author : Siegel
# @File : 03_construction_method.py
# @Software : PyCharm
"""
构造方法:
    类有一个名为__init__()的特殊方法(构造方法)
    该方法在类实例化时会自动调用,像下面这样:
        def __init__(self):
            self.data = []
    类定义了__init__()方法,类的实例化操作会自动调用__init__()方法
    __init__()方法可以有参数,参数通过__init__()传递到类的实例化操作上
"""


class Complex:
    def __init__(self, real_part, image_part):
        self.r = real_part
        self.i = image_part


x = Complex(3.0, -4.5)
print(x.r, x.i)
