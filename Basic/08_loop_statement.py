"""
循环:
    场景:
        1. 用户名和密码,反复输入
        2. 计算1-100
        3.游戏,死了重生
        ...
    方式:
        1. while
        2. for
    格式:
        1. while格式
            while 条件:
                要循环执行的代码
        2. for格式


"""

# 打印1-10之间的数字
n = 1  # 初始值
while n <= 10:  # 结束条件
    print(n, end=" ")
    n += 1  # 变量自增
print()
print('-' * 40)

"""
练习:
    打印1-50之间能被3整除的数字
"""
n = 1
while n <= 50:
    if n % 3 == 0:
        print(n, end=" ")
    n += 1
print()
print('-' * 40)
"""
练习:
    打印1-10之间数字的累加和
"""
n = 1
total = 0
while n <= 10:
    total += n
    n += 1
print(total)
print('-' * 40)
