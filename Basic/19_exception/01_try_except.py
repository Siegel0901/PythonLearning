# -*- coding = utf-8 -*-
# @Time : 2024/5/24 15:16
# @Author : Siegel
# @File : 01_try_except.py
# @Software : PyCharm
"""
异常:
    代码运行过程中出现的错误:xxxError
    出现异常后的代码不会被执行
异常处理:
    try:
        可能出现异常的代码
    except:
        如果有异常执行的代码
多种异常类型的情况
    try:
        有可能会产生多种异常
    except 异常类型1:
        print()
    except 异常类型2:
        print()
    ...
    except Exception as error:
        print(error)
    按照异常类型1,异常类型2,..从上至下的顺序进行异常匹配
    如果是有多个except,异常类型的顺序需要注意,父类Exception要放到最后
"""


def foobar():
    try:
        num1 = int(input("please input the first number:"))
        num2 = int(input("please input the second number:"))
        """
            ValueError: invalid literal for int() with base 10: 'a'
        """
        operator = input("please input operator(+-*/):")
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            """
                ZeroDivisionError: division by zero
            """
            result = num1 / num2
        else:
            print("operator input error")
            return
        print("{} + {} = {}".format(num1, num2, result))
    except ValueError:
        print("please input the type of number")
    # except ZeroDivisionError:
    #     print("divisor is zero")
    except Exception as error:
        print(error)


foobar()

print("after foobar")
