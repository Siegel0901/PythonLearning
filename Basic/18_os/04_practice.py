# -*- coding = utf-8 -*-
# @Time : 2024/5/24 14:14
# @Author : Siegel
# @File : 04_practice.py
# @Software : PyCharm

"""
新建file_02文件夹
将file_01中的文件按照文件后缀名分类到不同的文件夹中
"""
import os

cwd = os.getcwd()
# 源文件夹路径
src_path = os.path.join(cwd, 'file_01')
# 目的文件夹路径
target_path = os.path.join(cwd, 'file_02')


def copy(src, target):
    print("source is {}".format(src))
    print("target is {}".format(target))
    # 若目的文件夹不存在,则新建
    if not os.path.exists(target):
        os.mkdir(target)
    # 获取源文件夹中文件列表
    file_list = os.listdir(src)
    for file in file_list:
        # 获取文件后缀
        suffix = os.path.splitext(file)[1][1:]
        # print(suffix)
        # 拼接后缀分类文件夹名
        suffix_dir_path = os.path.join(target, suffix)
        # 新建后缀分类文件夹名
        if not os.path.exists(suffix_dir_path):
            os.mkdir(suffix_dir_path)
        # 源文件路径
        src_file_path = os.path.join(src, file)
        # 目的文件路径
        target_file_path = os.path.join(suffix_dir_path, file)
        with open(src_file_path, "rb") as src_file:
            # 读取源文件内容
            binary = src_file.read()
            with open(target_file_path, "wb") as target_file:
                # 写入目的文件
                target_file.write(binary)
    else:
        print("copy successfully!")


copy(src_path, target_path)
