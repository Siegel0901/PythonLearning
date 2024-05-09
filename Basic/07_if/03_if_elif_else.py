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