# -*- coding = utf-8 -*-
# @Time : 2024/5/2 11:50
# @Author : Siegel
# @File : 07_if.py
# @Software : PyCharm
"""
条件语句:
if
if else
if elif else
"""

"""
if 条件:
    条件成立要执行的语句
"""
# 4有条件打印
print(1)
print(2)
print(3)
result = input("请输入(y/n):")
if result == 'y':
    print(4)
    print('over~~~')

print('-' * 40)

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

"""
if 条件1:
    条件1True,执行的语句
elif 条件2:
    条件2True,执行的语句
elif 条件3:
    条件3True,执行的语句
...
else:
    1,2,3条件都为False的情况下,执行的语句
"""

"""
输入销售金额,符合哪种奖励的范围
1-5:1000元
5-10:奖励笔记本IBM
10-100:奖励iPhone12
超过了100:奖励特斯拉
鼓励奖
"""
money = int(input("请输入销售金额:"))
if 10000 < money <= 50000:
    print("奖励1000元!恭喜!")
elif 50000 < money <= 100000:
    print("奖励笔记本IBM!恭喜!")
elif 100000 < money <= 1000000:
    print("奖励iPhone12!恭喜!")
elif money > 1000000:
    print("奖励特斯拉!恭喜!")
else:
    print("鼓励奖,毛绒玩具")

print('-' * 40)

"""
人员管理系统功能:
    1. 添加员工
    2. 删除员工
    3. 查询员工
    4. 修改员工信息
"""

print("************欢饮进入人员管理系统************")
print("*               1. 添加员工              *")
print("*               2. 删除员工              *")
print("*               3. 查询员工              *")
print("*               4. 修改员工信息           *")
print("*****************************************")
f = int(input("请选择功能:"))
if f == 1:
    print("添加员工")
elif f == 2:
    print("删除员工")
elif f == 3:
    print("查询员工")
elif f == 4:
    print("修改员工信息")
else:
    print("请正确选择功能!")

print('-' * 40)

"""
嵌套if
if 条件1:
    if 条件2:
        条件1为True,条件2为True,执行语句
    else:
        条件1为True,条件2为False,执行语句
else:
    条件1为False,执行语句
"""

"""
阿里巴巴商家节,用户名,消费总金额,账户金额,优惠券
输入消费总金额,
如果金额0-500,则是lv1级别;
如果金额500-2000,则是lv2级别;
2000以上是lv3

lv1:随机赠送3张1-10的优惠券;
lv2:赠送2张50元优惠券,如果充值则送充值金额的10%;
lv3:赠送2张100元优惠券,如果充值则送15%的金额
"""

username = "Siegel"
current_money = 0
coupon_money = 0
total = int(input("请输入消费总金额:"))
# 根据总金额判断级别
if 0 < total < 500:  # lv1
    # 随机赠送3张1-10的优惠券
    lv = 1
    print("当前消费级别lv=%d,随机赠送3张1-10的优惠券" % lv)
    coupon1 = random.randint(1, 10)
    coupon2 = random.randint(1, 10)
    coupon3 = random.randint(1, 10)
    # 将金额数加到coupon_money
    coupon_money = coupon1 + coupon2 + coupon3
    print("当前用户金额为%d,优惠券金额为%d" % (current_money, coupon_money))
elif 500 <= total < 2000:  # lv2
    # 赠送2张50元优惠券,如果充值则送充值金额的10%
    lv = 2
    print("当前消费级别lv=%d,赠送2张50元优惠券,如果充值则送充值金额的10%%" % lv)
    coupon_money += 2 * 50
    # 嵌套if
    recharge = input("亲爱的用户%s,是否要充值(送充值金额的10%%)(y/n):" % username)
    if recharge == 'y':
        charge_money = int(input("请输入要充值的金额:"))
        current_money += charge_money + charge_money * 0.1
        print("充值成功!当前用户金额为%d,优惠券金额为%d" % (current_money, coupon_money))
elif 2000 <= total:  # lv3
    # 赠送2张100元优惠券,如果充值则送15%的金额
    lv = 3
    print("当前消费级别lv=%d,赠送2张100元优惠券,如果充值则送15%%的金额" % lv)
    coupon_money += 2 * 100
    # 嵌套if
    recharge = input("亲爱的用户%s,是否要充值(送充值金额的10%%)(y/n):" % username)
    if recharge == 'y':
        charge_money = int(input("请输入要充值的金额:"))
        current_money += charge_money + charge_money * 0.15
        print("充值成功!当前用户金额为%d,优惠券金额为%d" % (current_money, coupon_money))
else:
    pass

print('-' * 40)
"""
三目运算符:
    结果1 if 条件 else 结果2
    当条件为真时,返回结果1,否则返回结果2
"""

a = 3
b = 5
max_value = a if a > b else b
print(max_value)  # 5

"""
自动类型转换
    if语句需要一个判断条件,这个判断条件的结果需要一个布尔值.
    如果此时输入的判断条件不是一个布尔值,在代码执行的过程中,会将这个值自动转换成一个布尔值.
    在Python中,只有0,"",'',None,(),{},[]会被转换成False,其他都会被转换成True
"""
