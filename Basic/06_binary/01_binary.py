# -*- coding = utf-8 -*-
# @Time : 2024/5/2 10:39
# @Author : Siegel
# @File : 01_binary.py
# @Software : PyCharm
"""
二进制:
    0,1
八进制:
    0,1,2,3,4,5,6,7
十进制:
    0,1,2,3,4,5,6,7,8,9
十六进制:
    0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
"""

# 十进制转二进制
n = 149
result = bin(n)  # binary
print(result)

# 十进制转八进制
result = oct(n)
print(result)

# 十进制转十六进制
n = 985
result = hex(n)
print(result)

"""
前缀:
    0b  二进制
    0o  八进制
    0x  十六进制
    默认十进制
函数:
    bin()   0b
    int()
    oct()   0o
    hex()   0x
"""

n = 0x558

"""
思考:
    1. n = 0x558,如何转成十进制输出?
    2. 已知n = 0x558,如何转成二进制输出?如何转成八进制输出?
"""

# 转成十进制
result = int(n)
print(result)
# def __init__(self, x, base=10):  # known special case of int.__init__
#     """
#     int([x]) -> integer
#     int(x, base=10) -> integer
#
#     Convert a number or string to an integer, or return 0 if no arguments
#     are given.  If x is a number, return x.__int__().  For floating point
#     numbers, this truncates towards zero.
#
#     If x is not a number or if base is given, then x must be a string,
#     bytes, or bytearray instance representing an integer literal in the
#     given base.  The literal can be preceded by '+' or '-' and be surrounded
#     by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
#     Base 0 means to interpret the base from the string as an integer literal.
#     >>> int('0b100', base=0)
#     4
#     # (copied from class doc)
#     """
#     pass

# 转成二进制
result = bin(n)  # 无论当前的参数是几进制,都会转成二进制
print(result)

# 转成八进制
result = oct(n)  # 无论当前的参数是几进制,都会转成八进制
print(result)

"""
二进制与十六进制之间的转换:
    从低位到高位,二进制四位一组对应十六进制的一位,高位不足补0
二进制与八进制之间的转换:
    从低位到高位,二进制三位一组对应八进制的一位,高位不足补0
"""

print('-' * 40)

"""
位运算:针对二进制进行的运算
    &与
    |或
    ^异或
    ~非
    <<左移
    >>右移
"""

n1 = 0b0110  # 6
n2 = 0b1010  # 10
print(n1 & n2)  # 0b0010 ---> 2
print(n1 | n2)  # 0b1110 ---> 14
print(n1 ^ n2)  # 0b1100 ---> 12
print(~n1)  # 0b1001 ---> -7
"""
n1为int类型,占4字节,共32bit
n1的原码:0000 0000 0000 0110
n1的补码:0000 0000 0000 0110(计算机中用补码表示)
对n1的补码取反得到result:1111 1111 1111 1001(当做补码处理)
result转为原码:1000 0000 0000 0111(-7)
"""
print(n1 << 1)  # 0b1100 ---> 12
print(n1 >> 1)  # 0b0011 ---> 3

n3 = -4
print(n3 >> 1)  # -2
print(n3 << 1)  # -8

"""
n3 = -4
原码a:
    1000 0000 0000 0100
补码b:
    1111 1111 1111 1100
b右移一位得到result:
    1111 1111 1111 1110
result转成原码:
    1000 0000 0000 0010(-2)
b左移一位得到result:
    1111 1111 1111 1000
result转成原码:
    1000 0000 0000 1000(-8)
负数补码移位运算:
    左移同原码添0,右移同反码添1
Python的移位运算符是逻辑移位,不考虑符号位(星火大模型)
"""

"""
运算符的优先级:可用()提高优先级
    **
    ~   +   -
    *   /   %   //
    +   -
    >>  <<
    &
    ^   |
    <=  <   >   >=
    <>  ==  !=
    =   %=  /=  //= -=  +=  *=  **=
    is  is not
    in  not in
    not > and > or
"""