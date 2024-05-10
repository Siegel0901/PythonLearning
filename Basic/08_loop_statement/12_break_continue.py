"""
break
    跳出当前的循环结构
continue
    跳过本次循环,继续下一次循环
"""
# 打印1-10内的整数,遇到7停止
for num in range(1, 11):
    if num == 7:
        break
    print(num)

print('-' * 40)
# 打印1-10中不能被3整除的数
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
