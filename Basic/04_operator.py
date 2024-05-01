# -*- coding = utf-8 -*-
# @Time : 2024/5/1 10:00
# @Author : Siegel
# @File : 04_operator.py
# @Software : PyCharm
"""
运算符:
    算术运算符: + - * / % // **
"""
a = 1
b = 2
c = a + b
print(a, b, c)  # 1 2 3\n
print(a, b, c, sep=',')  # 1,2,3\n
print(a, b, c, sep=',', end='')  # 1,2,3
# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
#     """
#     Prints the values to a stream, or to sys.stdout by default.
#
#       sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
#       file
#         a file-like object (stream); defaults to the current sys.stdout.
#       flush
#         whether to forcibly flush the stream.
#     """
#     pass
print()  # /n
print(c - a)  # 2
print(c * a)  # 3
print(c / a)  # 3.0
print(c / 2)  # 1.5
print(c // 2)  # 1 //表示整除
print(c ** 2)  # 9 **表示取幂  m ** n -------> 表示m的n次方
print(7 % 4)  # 3  %表示取模

'''
练习:
    键盘输入一个3为数的整数,打印个位数,十位数,百位数
'''
# num = int(input("请输入一个3位数的整数:"))
# print("个位数:", num % 10)
# print("十位数:", num // 10 % 10)
# print("百位数:", num // 100)
print('-' * 20)
"""
运算符:
    赋值运算符: = += -= *= /= %= //= **=
"""
a += b  # a = a + b
print(a, b, c)
"""
运算符:
    关系运算符: > < >= <= == != is
    结果: True False
    字母字符串依照字典序比较(ASCII码)
"""
print(3 > 2)  # True
print(3 < 2)  # False
print(3 >= 2)  # True
print(3 >= 3)  # True
print(3 <= 2)  # False
print(3 == 2)  # False
print(3 != 2)  # True

"""
练习:
    输入考试分数,判断成绩是否在100到80之间?
"""
# score = float(input("请输入考试成绩:"))
# print(80 <= score <= 100)   # python可以用这种数学方式判断范围

"""
练习:
    输入huawei mate40 价格:
    输入iPhone 12 价格:
    比较两者是否相同
"""
# huawei = float(input("输入huawei mate40 价格:"))
# iPhone = float(input("输入iPhone 12 价格:"))
# print(huawei == iPhone)

print('-' * 20)
"""
运算符:
    逻辑运算符: and or not
    结果: True False
    and:与
        A and B 同真为真
        Ture and True   ---> True
        Ture and False  ---> False
        False and True  ---> False
        False and False ---> False
    or:或
        A or B 同假为假
        Ture and True   ---> True
        Ture and False  ---> True
        False and True  ---> True
        False and False ---> False
    not:非
        not A 取反
        not True    ---> False
        not False   ---> True
"""

print(1 and 3)  # 3 and两边都是非零数字,结果为and最后的值
print(0 and 3)  # 0 and两边只要有一侧为0,结果为0
print(1 and 0)  # 0
print(1 == 1 and 1 < 2)  # True
print(1 == 1 and 1 > 2)  # False

print(3 or 1)  # 3 3已经为真,无需判断后面
print(1 or 3)  # 1 1已经为真,无需判断后面
print(0 or 3)  # 3
print(1 == 1 or 1 < 2)  # True
print(1 == 1 or 1 > 2)  # True
print(1 != 1 or 1 > 2)  # False

flag = True
print(not flag)  # False
print(not 1 == 1)  # False
print(not 1 != 1)  # True