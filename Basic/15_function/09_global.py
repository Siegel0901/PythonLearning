"""
global关键字
    全局变量:
        声明在函数的外层,所有函数都可以访问
        全局变量如果是不可变类型,在函数中修改需要添加global关键字,如str,int,float
        全局变量如果是可变类型,在函数中修改不需要添加global关键字,如list,dict
    局部变量:
        声明在函数的内层,仅限于在函数内部使用
"""
name = 'Siegel'
birthday = '2000-09-01'


def func():
    name = 'siegel'  # 函数内部的局部变量和全局变量同名时,函数内部优先使用局部变量
    print(name)
    name += ' is handsome'  # 函数内部可对局部变量随意进行修改
    print(name)


func()


def print_birthday():
    print('{}\'s birthday is {}'.format(name, birthday))


def change_birthday():
    global birthday  # 用global关键字声明的全局不可变类型的变量,可在函数内部更改
    birthday = '2024-09-01'


print_birthday()
change_birthday()
print_birthday()

list1 = [1, 2, 3]


def foobar():
    list1.append(4) # 对于可变类型的全局变量,在函数内部修改时不需要使用global
    print(list1)


foobar()
