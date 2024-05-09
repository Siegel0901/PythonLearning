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