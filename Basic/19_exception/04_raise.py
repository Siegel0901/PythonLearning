# -*- coding = utf-8 -*-
# @Time : 2024/5/24 16:10
# @Author : Siegel
# @File : 04_raise.py
# @Software : PyCharm

"""
    抛出异常 raise
"""


def register():
    username = input("please input username:")
    if len(username) < 6:
        # 用raise关键字手动抛出异常
        raise Exception("the length of username should greater than or equal to 6")
    else:
        print("your username is {}".format(username))


try:
    register()
except Exception as error:
    print(error)
    print("register failed")
else:
    print("register successfully")
