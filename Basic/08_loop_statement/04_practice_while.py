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