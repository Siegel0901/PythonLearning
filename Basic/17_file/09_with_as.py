# -*- coding = utf-8 -*-
# @Time : 2024/5/24 10:08
# @Author : Siegel
# @File : 09_with_as.py
# @Software : PyCharm

"""
使用with open() as file_name格式
    系统将自动帮助我们释放资源
"""
with open('../17_file/file/avatar.jpg') as file:
    pass
# ValueError: I/O operation on closed file
file.readable()
