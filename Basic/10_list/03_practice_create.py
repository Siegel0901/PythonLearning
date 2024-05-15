"""
买多件商品:
    输入商品名称,价格,数量
    用列表嵌套输出所买的商品
"""
cart = []
quit_flag = False
count = 0
total_price = 0
while not quit_flag:
    item = []
    name = input("请输入商品名称:")
    price = input("请输入商品价格:")
    num = input("请输入商品数量:")
    item.append(name)
    item.append(price)
    item.append(num)
    cart.append(item)
    cin = input("是否继续购买商品(q或Q退出):")
    if cin.lower() == 'q':
        quit_flag = True
for item in cart:
    print("您购买了{}件单价为{}元的{}".format(int(item[2]), float(item[1]), item[0]))
    total_price += float(item[1])
    count += int(item[2])
print("您总共购买了{}件商品,总价为{}元".format(count, total_price))
