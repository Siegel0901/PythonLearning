"""
用户登录
    1. 用户输入用户名、密码和验证码进行登录
    2. 登录需要单独一个函数实现
    3. 验证码需要单独一个函数实现
"""
import random


def check_account(username, password):
    if username == 'Siegel' and password == 'root':
        return True
    else:
        return False


def generate_code():
    sample = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    code = ""
    for i in range(5):
        code += random.choice(sample)
    return code


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    code = generate_code()
    print("check code is:{}".format(code))
    my_code = input("Enter your code: ").lower()
    if my_code == code.lower():
        if check_account(username, password):
            print("Welcome {}".format(username))
        else:
            print("Wrong account or password")
    else:
        print("Wrong code")


login()
