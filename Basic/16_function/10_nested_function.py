"""
函数嵌套
    可以在函数内部继续声明函数
    内部函数可以使用外部函数声明的局部变量
        若是不可变类型,修改时需要加nonlocal关键字
        若是可变类型,修改时无需加nonlocal关键字
    内部函数修改全局的不可变变量时,需要在内部函数中用关键字global声明
"""

x = 1000


def func():
    n = 100
    list1 = [1, 2, 3]

    # 内部函数对func中的变量进行修改
    def func2():
        global x  # x为全局变量,修改时需要在内部函数中增加关键字global
        nonlocal n  # n为不可变类型,修改时需要增加关键字nonlocal
        n *= 2
        x += 1
        # list1为可变类型,修改是无需加关键字nonlocal
        for index, item in enumerate(list1):
            list1[index] = item + n
        print('n=%d, list1=%s, x=%d' % (n, list1, x))

    # 调用内部函数
    func2()


# 调用主函数
func()
