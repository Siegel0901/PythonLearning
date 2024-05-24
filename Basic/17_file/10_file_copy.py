# -*- coding = utf-8 -*-
# @Time : 2024/5/24 10:10
# @Author : Siegel
# @File : 10_file_copy.py
# @Software : PyCharm

with open("../17_file/file/avatar.jpg", 'rb') as origin_file:
    binary = origin_file.read()
    with open("../17_file/file/avatar_copy.jpg", 'wb') as copy_file:
        copy_file.write(binary)

print("copy file successfully!")
