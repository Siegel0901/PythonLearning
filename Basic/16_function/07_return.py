"""
return语句
    return[表达式]用于退出函数,选择性地向调用方返回一个表达式
    不带参数的return语句返回None
"""


def my_sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
result = my_sum(10, 20)
print("函数外 : ", result)
