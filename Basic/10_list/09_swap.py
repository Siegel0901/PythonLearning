"""
交换变量的值
"""

a = 1
b = 2
print("a={}, b={}".format(a, b))

# 常规做法
c = a
a = b
b = c
print("a={}, b={}".format(a, b))

# python中支持的赋值方法
a, b = b, a
print("a={}, b={}".format(a, b))

a = 1
b = 2
c = 3
print("a={}, b={}, c={}".format(a, b, c))
a, b, c = c, a, b
print("a={}, b={}, c={}".format(a, b, c))
