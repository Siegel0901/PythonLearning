"""
while...else格式:
    while 循环条件:
        循环体
    else:
        如果上面的循环中没有出现中断(break),执行else部分
"""
n = 1
while n < 11:
    print(n)
    # if n == 5:
    #     break
    n += 1
else:
    print("over")
