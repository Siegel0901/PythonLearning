# -*- coding = utf-8 -*-
# @Time : 2024/5/24 9:46
# @Author : Siegel
# @File : 05_readlines.py
# @Software : PyCharm

file = open("../17_file/file/test1.txt")
# readlines读取所有行,并以列表形式返回
lines = file.readlines()
print(type(lines))
for i in lines:
    print(i)
file.close()
