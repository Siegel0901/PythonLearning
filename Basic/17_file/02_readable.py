# -*- coding = utf-8 -*-
# @Time : 2024/5/24 9:44
# @Author : Siegel
# @File : 02_readable.py
# @Software : PyCharm

file = open("../17_file/file/test1.txt")
# readable()表示是否可读,返回布尔类型
result = file.readable()
print(type(result))
print(result)
file.close()
