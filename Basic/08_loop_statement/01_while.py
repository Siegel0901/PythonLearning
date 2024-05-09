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
            for i in range(n):
                循环体中的内容
    range():
        range(stop):[0,stop)
        range(start,stop):[start,stop)
        range(start,stop,step):
            [start,stop),
            step为步长(增量),默认为1
"""

# 打印1-10之间的数字
n = 1  # 初始值
while n <= 10:  # 结束条件
    print(n, end=" ")
    n += 1  # 变量自增
print()
print('-' * 40)







