"""
练习:
    模拟登录:输入用户名和密码,如果三次没有登陆成功,提示账号被锁定
"""
username = 'Siegel'
password = 'root'
flag = False
for i in range(3):
    username_i = input("请输入用户名:")
    password_i = input("请输入密码:")
    if username_i == username and password_i == password:
        flag = True
        print("登陆成功")
        break
    print("账号或密码错误,请重新登录!")
if not flag:
    print("账号被锁定")
