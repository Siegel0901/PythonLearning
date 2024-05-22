"""
Python lambda(匿名函数)
    1. Python使用lambda来创建匿名函数
    2. lambda函数是一种小型、匿名的内联函数,它可以具有任意数量的参数,但只能有一个表达式.
    3. 匿名函数不需要使用def关键字定义完整函数
    4. lambda函数通常用于编写简单的、单行的函数,通常在需要函数作为参数传递的情况下使用,例如在map()、filter()、reduce()等函数中
    5. lambda函数特点:
        lambda函数是匿名的,它们没有函数名称,只能通过赋值给变量或作为参数传递给其他函数来使用
        lambda函数通常只包含一行代码,这使得他们适用于编写简单的函数
    6. lambda语法格式
        lambda arguments: expression
            lambda是Python的关键字,用于定义lambda函数
            arguments是参数列表,可以包含零个或多个参数,但必须在冒号(:)前指定
            expression是一个表达式,用于计算并返回函数的结果
"""
# 无参数的lambda函数
foobar = lambda: print("Hello Python")
foobar()
foobar = lambda: "Hello Python"
print(foobar())
print("".center(50, "-"))


# lambda函数封装在函数返回值中
def func(n):
    return lambda x: n * x


doubler = func(2)
tripler = func(3)

print(doubler(11))
print(tripler(11))
