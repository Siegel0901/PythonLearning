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