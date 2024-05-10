"""
条件嵌套:
    if 条件:
        pass
    else:
        if 条件:
            pass
循环嵌套:
    1. while嵌套
        while 循环条件:
            while 循环条件:
                执行语句
    2. for嵌套
        for i in range(n):
            for j in range(n):
                执行语句
"""
"""
打印一下内容:
*
**
***
****
*****
"""
n = 0
while n < 5:
    i = 0
    while i <= n:
        print('*', end='')
        i = i + 1
    print()
    n = n + 1

print("-" * 40)
for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()
