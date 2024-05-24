# -*- coding = utf-8 -*-
# @Time : 2024/5/24 10:27
# @Author : Siegel
# @File : 01_path.py
# @Software : PyCharm

import os

"""
os.path:
    __file__表示当前文件
    os.path.dirname(__file__)   os.getcwd()
        获取当前文件所在的文件目录(绝对路径)
    os.path.join(path1, path2)
        拼接路径    
    os.path.isabs(path)
        判断是否为绝对路径    
    os.path.abspath(path)
        获取绝对路径
"""

# 获取当前文件所在的文件目录(绝对路径)
path = os.path.dirname(__file__)
print(type(path))
print(path)
path = os.getcwd()
print(path)
print("".center(50, '-'))

# 拼接路径
new_path = os.path.join(path, 'test', 'file', 'test1.txt')
print(new_path)
print("".center(50, '-'))

# 判断是否为绝对路径
result = os.path.isabs("../17_file/file/test1.txt")
print(type(result))
print(result)
print("".center(50, '-'))

# 获取绝对路径
relative_path = "../17_file/file/test1.txt"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)
print("".center(50, '-'))

"""
os.path.split(path)
    分割路径中的目录和文件名,以元组形式返回
os.path.splitext(path)
    分割路径中的文件与扩展名,以元组形式返回
"""
now_path = os.path.abspath(__file__)
print(now_path)
print("".center(50, '-'))

tuple1 = os.path.split(now_path)
print(tuple1)
print("now filename is {}".format(tuple1[1]))
print("".center(50, '-'))

tuple2 = os.path.splitext(now_path)
print(tuple2)
print("".center(50, '-'))

"""
os.path.getsize(path)
    获取path路径中文件的大小 单位字节
"""
size = os.path.getsize(__file__)
print(size)
print("".center(50, '-'))
