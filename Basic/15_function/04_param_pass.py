# -*- coding = utf-8 -*-
# @Time : 2024/5/21 21:06
# @Author : Siegel
# @File : 04_param_pass.py
# @Software : PyCharm
"""
Python函数的参数传递:
    不可变类型:
        类似C++的值传递,如整数、字符串、元组
        如fun(a),传递的只是a的值,没有影响a对象本身
        如果在fun(a)内部修改a的值,则是新生成一个a的对象
    可变类型:
        类似C++的引用传递,如列表,字典
        如fun(la),则是将la真正的传过去,修改后fun外部的la也会影响
python中一切都是对象,严格意义我们不能说值传递还是引用传递
我们应该说传不可变对象和传可变对象
"""


# 传不可变对象案例
def change(a):
    print("函数内部a重新赋值前的内存地址:{}".format(id(a)))  # 指向同一个对象
    a = 10
    print("函数内部a重新赋值后的内存地址:{}".format(id(a)))  # 指向新对象


a = 1
print("调用函数前a的内存地址:{}".format(id(a)))
change(a)


# 传可变对象案例
def change_me(list1):
    print("函数内部list1.pop()前的内存地址:{}".format(id(list1)))  # 指向同一个对象
    list1.pop()
    print("函数内部list1.pop()重新赋值后的内存地址:{}".format(id(list1)))  # 指向新对象


list1 = [1, 2]
print("调用函数前list1的内存地址:{}".format(id(list1)))
change_me(list1)
