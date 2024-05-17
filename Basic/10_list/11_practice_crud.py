"""
英雄联盟角色管理系统

角色属性:姓名,性别,定位

添加角色
删除角色
修改角色
查询角色 --> 单个角色信息
显示所有角色
退出系统
"""
import time

print("欢迎进入英雄联盟角色管理系统".center(30, "-"))
roles = []
while True:
    print("功能列表".center(36, "*"))
    print("1. 添加角色".center(34))
    print("2. 删除角色".center(34))
    print("3. 修改角色".center(34))
    print("4. 查询角色".center(34))
    print("5. 查询全部".center(34))
    print("6. 退出系统".center(34))
    print("".center(39, "*"))
    choice = input("请选择功能:")
    if choice == "1":
        role = []
        name = input("请输入角色姓名:")
        gender = input("请输入角色性别:")
        position = input("请输入角色定位:")
        role.append(name)
        role.append(gender)
        role.append(position)
        print("正在查询该角色~~~")
        time.sleep(2)
        if role not in roles:
            print("正在添加该角色~~~")
            time.sleep(1)
            roles.append(role)
            print("添加角色成功!")
        else:
            print("系统中已存在该角色,添加角色失败!")
        input("按任意键继续...")
    elif choice == "2":
        role = []
        name = input("请输入所要删除的角色姓名:")
        gender = input("请输入所要删除的角色性别:")
        position = input("请输入所要删除的角色定位:")
        role.append(name)
        role.append(gender)
        role.append(position)
        print("正在查询该角色~~~")
        time.sleep(2)
        if role in roles:
            print("查询成功!")
            print("正在删除该角色~~~")
            time.sleep(1)
            roles.remove(role)
            print("删除成功!")
        else:
            print("系统中不存在该角色!删除失败!")
        input("按任意键继续...")
    elif choice == "3":
        role = []
        name = input("请输入所要修改的角色姓名:")
        gender = input("请输入所要修改的角色性别:")
        position = input("请输入所要修改的角色定位:")
        role.append(name)
        role.append(gender)
        role.append(position)
        print("正在查询该角色~~~")
        time.sleep(2)
        if role in roles:
            print("查询成功!")
            index = roles.index(role)
            name = input("请输入修改后的角色姓名:")
            gender = input("请输入修改后的角色性别:")
            position = input("请输入修改后的角色定位:")
            print("正在修改该角色~~~")
            time.sleep(1)
            roles[index][0] = name
            roles[index][1] = gender
            roles[index][2] = position
            print("修改成功!")
        else:
            print("系统中不存在该角色!修改失败!")
        input("按任意键继续...")
    elif choice == "4":
        role = []
        length = len(roles)
        index = int(input("请输入所要查询的角色编号:"))
        print("正在查询该角色~~~")
        time.sleep(2)
        if -length <= index < length:
            print("查询成功!")
            print("该角色的姓名为{},性别为{},定位为{}".format(roles[index][0], roles[index][1], roles[index][2]))
        else:
            print("系统中不存在该角色!查询失败!")
        input("按任意键继续...")
    elif choice == "5":
        role = []
        print("正在查询所有角色~~~")
        time.sleep(2)
        if len(roles) == 0:
            print("当前系统中无角色信息!")
        else:
            for role in roles:
                for info in role:
                    print(info, end="\t")
                print()
            print("查询成功!")
        input("按任意键继续...")
    elif choice == "6":
        print("正在退出系统~~~")
        time.sleep(2)
        print("退出成功!")
        break
    else:
        print("输入有误!请重新输入!")
        input("按任意键继续...")
