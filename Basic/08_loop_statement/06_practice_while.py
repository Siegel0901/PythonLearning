"""
练习:
    猜拳游戏,3局2胜
"""
import random
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
