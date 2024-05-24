# -*- coding = utf-8 -*-
# @Time : 2024/5/24 14:47
# @Author : Siegel
# @File : 05_practice.py
# @Software : PyCharm

"""
将文件夹file_02复制到同目录的file_03中
"""
import os

path = os.getcwd()
# 源文件夹路径
src_path = os.path.join(path, 'file_02')
# 目的文件夹路径
target_path = os.path.join(path, 'file_03')


def copy(src, target):
    print("source is {}".format(src))
    print("target is {}".format(target))
    # 若目的文件夹不存在,则新建
    if not os.path.exists(target):
        os.mkdir(target)
    # 获取源文件夹中的文件列表
    file_list = os.listdir(src)
    for file_or_dir in file_list:
        # 源文件夹中的文件或文件夹路径
        src_fod_path = os.path.join(src, file_or_dir)
        # 目的文件夹中的文件或文件夹路径
        target_fod_path = os.path.join(target, file_or_dir)
        # 若该路径是文件
        if os.path.isfile(src_fod_path):
            with open(src_fod_path, "rb") as src_file:
                # 读取源文件内容
                binary = src_file.read()
                with open(target_fod_path, "wb") as target_file:
                    # 写入目的文件
                    target_file.write(binary)
        # 若该路径是文件夹
        if os.path.isdir(src_fod_path):
            # 若不存在目的文件夹路径,则新建
            if not os.path.exists(target_fod_path):
                os.mkdir(target_fod_path)
            # 递归调用copy函数,传入源文件夹中的文件夹路径和目的文件夹中的文件夹路径
            copy(src_fod_path, target_fod_path)
    else:
        print("copy successfully!")


copy(src_path, target_path)
