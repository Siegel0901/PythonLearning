"""
生成8个1-100之间的随机整数,保存到列表中
键盘输入一个1-100之间的整数,将整数插入到排序后的列表中(升降没有要求)
[3,4,7,8,7,5,9,3]
[3,3,4,5,7,7,8,9]
6
[3,3,4,5,6,7,7,8,9]
"""
import random

list1 = []
for i in range(8):
    ranInt = random.randint(1, 100)
    list1.append(ranInt)
while True:
    num = input("请输入一个1-100之间的整数:")
    if num.isdigit() and 1 <= int(num) <= 100:
        num = int(num)
        list1.append(num)
        list1.sort()
        print(list1)
        break
    else:
        print("输入有误,请重新输入!")
