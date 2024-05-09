"""
for...else格式:
    for i in range(n):
        循环体
    else:
        如果上面的for循环0~n-1没有出现中断(break),执行else部分
"""
username = 'Siegel'
password = 'root'
for i in range(3):
    username_i = input("请输入用户名:")
    password_i = input("请输入密码:")
    if username_i == username and password_i == password:
        print("登陆成功")
        break
    print("账号或密码错误,请重新登录!")
else:
    print("账号被锁定")
