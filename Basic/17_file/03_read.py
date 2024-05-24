# -*- coding = utf-8 -*-
# @Time : 2024/5/24 9:45
# @Author : Siegel
# @File : 03_read.py
# @Software : PyCharm

file = open("../17_file/file/test1.txt")
# read()读取文件所有内容
container = file.read()
print(type(container))
print(container)
file.close()
