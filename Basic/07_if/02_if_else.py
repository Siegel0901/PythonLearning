"""
if 条件:
    条件成立要执行的语句
else:
    条件不成立要执行的语句
"""

# 猜数字
import random

ran = random.randint(1, 10)
print(ran)
guess = input('请输入你猜的数:')
guess = int(guess)  # 键盘输入的guess类型为字符串,不用int转的话,会用ASCII码比较
if ran == guess:
    print('恭喜你猜对了!')
else:
    print('猜错咯~~')

print('-' * 40)
"""
练习:
    1. 输入账号和密码(名:admin,密码:1234),判断是否正确,正确显示登录成功,否则登录失败.
    2. 键盘输入一个4位数整数,判断百位数和十位数相加的和是否大于10,如果大于10,则显示:success   否则显示:fail
    3. 产生两个1-10内的随机整数,判断两个数字之间的和是否大于8并且差小于等于3,如果是则显示:success    否则显示fail
"""
# 1. 账号密码
username = input("请输入账号:")
password = input("请输入密码:")
if username == "admin" and password == "1234":
    print("登录成功")
else:
    print("登录失败")

print('-' * 40)

# 2. 整数判断
num = int(input("请输入一个4位数整数:"))
a = num // 100 % 10
b = num // 10 % 10
print(a, b)
if a + b > 10:
    print("success")
else:
    print("fail")

print('-' * 40)

# 3. 随机数
ran1 = random.randint(1, 10)
ran2 = random.randint(1, 10)
print(ran1, ran2)
if ran1 + ran2 > 8 and abs(ran1 - ran2) <= 3:
    print("success")
else:
    print("fail")

print('-' * 40)
