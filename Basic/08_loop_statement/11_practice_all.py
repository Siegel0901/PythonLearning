"""
注意事项:
    什么时候用while什么时候用for?
    while:
        1. 固定次数的循环
        2. 不确定次数的循环
        格式:
            while 条件:
                pass
    for:
        肯定是固定次数的循环
        格式:
            for i in range(n):
                pass
"""
"""
综合练习:
    掷骰子游戏
    规则:
        1. 掷两个骰子,每个骰子的点数为1-6
        2. 关于金币:
            2.1 玩游戏需要消耗金币,没有金币不能玩游戏
            2.2 玩游戏赠金币1枚,充值获取金币
            2.3 充值金额必须为10的倍数
            2.4 一个金币0.5元,10块钱20个金币
            2.5 玩游戏消耗5个金币
        3. 游戏内容:
            3.1 猜大小,两个骰子点数之和超出6点为大,否则为小
            3.2 猜对,赠金币2枚
            3.3 猜错,没有奖励
        4. 游戏结束:
            4.1 主动退出
            4.2 没有金币退出
            4.3 只要退出则打印金币数以及共玩了多少局
"""
import random

# 金币数
coins = 0
# 总局数
total = 0
# 是否结束游戏
quit_flag = False
while not quit_flag:  # 控制用户开始游戏的正确输入
    cin = input("开始游戏(y/n):")
    if cin == 'y':
        while not quit_flag:  # 控制游戏是否结束
            # 金币不够一局游戏时,提示用户充值
            if coins < 5:
                recharge_flag = False  # 是否充值成功
                while not recharge_flag and not quit_flag:  # 控制用户是否充值的正确输入
                    cin = input("当前金币为%d,无法继续游戏,金币一个0.5元,是否充值(y/n):" % coins)
                    if cin == 'y':
                        while not recharge_flag:  # 控制用户充值金额的正确输入
                            recharge_money = input("请输入充值金额(必须是10的倍数,单位:元):")
                            if recharge_money.isdigit():
                                recharge_money = int(recharge_money)
                                if recharge_money % 10 == 0:
                                    value_coins = recharge_money // 0.5  # 转化为金币
                                    coins += value_coins  # 金币累加
                                    recharge_flag = True  # 充值成功
                                    print("充值成功,您充值了%d元,价值%d金币,当前金币为:%d" % (
                                        recharge_money, value_coins, coins))
                                else:
                                    print("充值金额必须为10的整数倍!")
                            else:
                                print("输入有误,请重新输入!")
                    elif cin == 'n':
                        print("金币为0,无法继续游戏,游戏局数:%d,金币数:%d" % (total, coins))
                        quit_flag = True
                    else:
                        print("输入有误,请重新输入!")
            if coins < 5 and quit_flag:  # 金币不足且未充值
                break
            # 游戏开始
            total += 1  # 累计局数
            coins -= 5  # 玩游戏消耗5个金币
            print("游戏开始!这是第%d局游戏,本局游戏消耗5枚金币!当前金币数为:%d" % (total, coins))
            coins += 1  # 系统赠金币1枚
            print("恭喜!系统赠金币1枚!当前金币数为:%d" % coins)
            print("开始投掷骰子！")
            dice1 = random.randint(1, 6)
            print("第一个骰子投掷完毕")
            dice2 = random.randint(1, 6)
            print("第二个骰子投掷完毕")
            dice_sum = dice1 + dice2
            guess_flag = False
            while not guess_flag:  # 控制用户猜大猜小的正确输入
                guess = input("点数之和为6以上是大,否则是小,请问您猜大猜小(大/小):")
                # 猜大
                if guess == '大':
                    guess_flag = True
                    # 猜对
                    if dice_sum > 6:
                        coins += 2
                        print("恭喜你猜对了!系统赠金币2枚!当前金币数为:%d" % coins)
                    # 猜错
                    else:
                        print("很遗憾你猜错了,当前金币数为:%d" % coins)
                # 猜小
                elif guess == '小':
                    guess_flag = True
                    # 猜对
                    if dice_sum <= 6:
                        coins += 2
                        print("恭喜你猜对了!系统赠金币2枚!当前金币数为:%d" % coins)
                    # 猜错
                    else:
                        print("很遗憾你猜错了,当前金币数为:%d" % coins)
                else:
                    print("输入有误,请重新输入!")

            while not quit_flag:  # 控制用户是否继续游戏的正确输入
                cin = input("是否继续游戏(y/n):")
                if cin == 'y':
                    print("-" * 50)  # 分割线
                    break
                elif cin == 'n':
                    print("游戏局数:%d,金币数:%d" % (total, coins))
                    quit_flag = True
                else:
                    print("输入有误,请重新输入!")
    elif cin == 'n':
        print("游戏局数:%d,金币数:%d" % (total, coins))
        quit_flag = True
    else:
        print("输入有误,请重新输入!")
