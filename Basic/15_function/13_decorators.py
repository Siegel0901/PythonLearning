"""
Python 装饰器
    装饰器(decorators)是Python中的一种高级功能,它允许你动态地修改函数或类的行为
    装饰器是一种函数,它接受一个函数作为参数,并返回一个新的函数或修改原来的函数
    装饰器的语法使用@decorator_name来应用在函数或方法上
    Python还提供了一些内置的装饰器,比如@staticmethod和@classmethod,用于定义静态方法和类方法
装饰器的应用场景:
    1. 日志记录
        装饰器可用于记录函数的调用信息、参数和返回值
    2. 性能分析
        可以使用装饰器来测量函数的执行时间
    3. 权限控制
        装饰器可用于限制对某些函数的访问权限
    4. 缓存
        装饰器可用于实现函数结果的缓存,以提高性能
"""
"""
基本语法
    Python装饰允许在不修改原有函数代码的基础上,动态地增加或修改函数的功能
    装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象
        def decorator_function(original_function):
            def wrapper(*args, **kwargs):
                # 这里是在调用原始函数前添加的新功能
                before_call_code()
                result = original_function(*args, **kwargs)
        
                # 这里是在调用原始函数后添加的新功能
                after_call_code()
        
                return result
        
            return wrapper
        
        
        # 使用装饰器
        @decorator_function
        def target_function(arg1, arg2):
            pass  # 原始函数实现
    上述代码将target_function函数传递给decorator_function装饰器,并将返回的函数重新赋值给target_function
    从而,每次调用target_function时,实际上调用了经过装饰器处理后的函数
"""


# 使用装饰器
def decorator(func):
    def wrapper(*args, **kwargs):
        print("原函数执行前装饰")
        func(*args, **kwargs)
        print("原函数执行后装饰")
        print("在装饰器中打印原函数的参数:")
        for arg in args:
            print(arg)
        for key in kwargs:
            print({key: kwargs[key]})

    return wrapper


@decorator  # target = decorator(target)
def target(*args, **kwargs):
    print("原函数执行中..")


target('Siegel', 'Siegel', 'Siegel')
target(name='Siegel', age=24)
print("".center(50, '-'))


# 带参数的装饰器
def repeat(n):
    def decorator1(func):
        def wrapper(name):
            for _ in range(n):
                func(name)

        return wrapper

    return decorator1


@repeat(3)
def greet(name):
    print("Hello " + name)


greet("Siegel")
print("".center(50, '-'))
"""
以上代码中repeat函数是一个带参数的装饰器
    它接受一个整数参数n,然后返回一个装饰器函数
    该装饰器函数内部定义了wrapper函数,在调用原始函数之前重复执行n次
    因此,greet函数在被@repeat(3)装饰后,会打印三次问候语
"""

"""
装饰器修饰有返回值的函数
    原函数有返回值,装饰器的内部可以接受返回值,并更改返回值继续返回
"""


def decorator2(func):
    def wrapper(*args, **kwargs):
        string = func(*args, **kwargs)
        string += " decorated"
        return string

    return wrapper


@decorator2
def output(string):
    return string


result = output("Hello world")
print(result)
