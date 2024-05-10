"""
用户名或手机号登录
用户名:siegel0901
手机号:12345678901
密码:123456
规则:
    用户名:全部小写,不能以数字开头,长度必须6位及以上
    手机号:11位纯数字
    密码:必须是6位数字
以上条件符合则验证用户名或手机号是否与密码匹配
"""

username = 'siegel0901'
phone_number = '1234567890'
password = '123456'
account_in = ''
password_in = ''
while True:
    while True:
        cin = input("请输入用户名或手机号:")
        if cin.isdigit():
            if len(cin) != 11:
                print("手机号码必须为11位!")
            else:
                account_in = cin
                break
        else:
            if len(cin) < 6:
                print("用户名长度必须为6位及以上!")
            elif cin[0].isdigit():
                print("用户名不能以数字开头!")
            elif not cin[0].islower():
                print("用户名必须全部小写!")
            else:
                account_in = cin
                break
    while True:
        cin = input("请输入密码:")
        if len(cin) != 6:
            print("密码必须为6位数字!")
        elif not cin.isdigit():
            print("密码必须为6位数字!")
        else:
            password_in = cin
            break

    if (account_in == username or account_in == phone_number) and password_in == password:
        print("登录成功!")
        break
    else:
        print("用户名或手机号或密码错误,登陆失败!")
