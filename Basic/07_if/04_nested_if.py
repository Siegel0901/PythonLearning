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
import random

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