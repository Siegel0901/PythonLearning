"""
    for格式:
        for i in range(n):
            循环体中的内容
    range():
        range(stop):[0,stop)
        range(start,stop):[start,stop)
        range(start,stop,step):
            [start,stop),
            step为步长(增量),默认为1
"""
# 1-10数字打印
for i in range(1, 11):
    print(i)

print('-' * 40)

# 1-50累加和
total = 0
for i in range(1, 51):
    total += i
print(total)

print('-' * 40)

