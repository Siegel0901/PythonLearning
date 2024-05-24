# -*- coding = utf-8 -*-
# @Time : 2024/5/24 9:45
# @Author : Siegel
# @File : 04_readline.py
# @Software : PyCharm

file = open("../17_file/file/test1.txt")
# readline()读取文件中的一行,包括‘\n’字符
while True:
    line = file.readline()
    print(line)
    if not line:
        break
file.close()
