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

"""
练习:
    超市购物,输入价格和数量,允许购买多件商品
    计算所有商品的数量和总额
"""
total = 0
numbers = 0
while True:
    # 输入购买的商品价格和数量
    price = float(input("请输入购买的商品价格:"))
    guess = int(input("请输入购买的商品数量:"))
    # 统计总价和总数
    total += guess * price
    numbers += guess
    # 判断是否购物结束
    finish = input("是否完成购物(y/n):")
    if finish == 'y':
        break
print("购买商品数量为%d,商品总价为%.2f" % (numbers, total))

print('-' * 40)

"""
练习:
    猜数字
    1. 产生随机数 random.randint(start, end)
        可以猜多次,直到猜对为止,如果猜错了适当给提示,猜大了还是猜小了
    2. 统计猜的次数
        1次猜中,赶快去买彩票吧,运气爆了
        2-5次猜中,运气还可以哦
        6及以上,猜对了,运气一般啊
"""
import random

ran = random.randint(1, 50)
numbers = 0
while True:
    guess = int(input("请输入1-50之间的数字:"))
    numbers += 1
    if guess == ran:
        if numbers == 1:
            print("恭喜你猜对了!赶快去买彩票吧,运气爆了!")
        elif 2 <= numbers <= 5:
            print("恭喜你猜对了!运气还可以哦!")
        else:
            print("恭喜你猜对了!运气一般啊!")
        break
    elif guess > ran:
        print("猜大了")
    elif guess < ran:
        print("猜小了")

print('-' * 40)
"""
练习:
    猜拳游戏,3局2胜
"""
win = 0
lose = 0
while win != 2 and lose != 2:
    person_gesture = int(input("请输入手势:(0)石头、(1)剪刀、(2)布:"))
    computer_gesture = random.randint(0, 2)
    if person_gesture == 0 and computer_gesture == 1:
        print("计算机出的是剪刀,这局你赢了!")
        win += 1
    elif person_gesture == 0 and computer_gesture == 2:
        print("计算机出的是布,这局你输了!")
        lose += 1
    elif person_gesture == 1 and computer_gesture == 0:
        print("计算机出的是石头,这局你输了!")
        lose += 1
    elif person_gesture == 1 and computer_gesture == 2:
        print("计算机出的是布,这局你赢了!")
        win += 1
    elif person_gesture == 2 and computer_gesture == 0:
        print("计算机出的是石头,这局你赢了!")
        win += 1
    elif person_gesture == 2 and computer_gesture == 1:
        print("计算机出的是剪刀,这局你输了!")
        lose += 1
    else:
        print("平局...")
if win == 2:
    print("恭喜你赢了!")
if lose == 2:
    print("很遗憾你输了!")


print('-' * 40)
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
for i in range(1,11):
    print(i)

print('-' * 40)

# 1-50累加和
total = 0
for i in range(1,51):
    total += i
print(total)

print('-' * 40)

"""
练习:
    模拟登录:输入用户名和密码,如果三次没有登陆成功,提示账号被锁定
"""
username = 'Siegel'
password = 'root'
flag = False
for i in range(3):
    username_i = input("请输入用户名:")
    password_i = input("请输入密码:")
    if username_i == username and password_i == password:
        flag = True
        print("登陆成功")
        break
    else:
        print("账号或密码错误,请重新登录!")
if not flag:
    print("账号被锁定")

