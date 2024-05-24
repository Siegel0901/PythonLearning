# -*- coding = utf-8 -*-
# @Time : 2024/5/24 15:57
# @Author : Siegel
# @File : 03_try_except_finally.py
# @Software : PyCharm
"""
    try:
        可能出现异常的代码
    except:
        如果有异常执行的代码
    [finally:
        无论是否存在异常都会被执行的代码]
当函数中有finally时,其余部分的return不会立即返回
    若finally中存在return语句,则其余部分的return结果会被覆盖
    若finally中不存在return语句,则按照其余部分的return结果返回
"""


def foobar():
    file = None
    try:
        file = open("../17_file/file/test1.txt")
        file.write("testWriteError")
        return "return in try"
    except Exception as error:
        print(error)
        return "return in except"
    finally:
        print("finally".center(40, '-'))
        if file:
            file.close()
        # return "return in finally"


print(foobar())
