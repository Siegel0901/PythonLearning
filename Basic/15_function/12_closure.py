"""
闭包
    1. 嵌套函数
    2. 内部函数引用了外部函数的变量
    3. 返回值是内部函数
"""


def outer(n):
    def inner(x):
        x = x * n
        return x

    return inner


doubler = outer(2)
print(doubler)
print(doubler(2))

tripler = outer(3)
print(tripler)
print(tripler(2))

print("".center(50, '-'))


# 用lambda关键字实现
def func(n):
    return lambda x: x * n


my_doubler = func(2)
print(my_doubler)
print(my_doubler(2))

my_tripler = func(3)
print(my_tripler)
print(my_tripler(3))
