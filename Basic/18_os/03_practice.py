# -*- coding = utf-8 -*-
# @Time : 2024/5/24 12:41
# @Author : Siegel
# @File : 03_practice.py
# @Software : PyCharm
"""
将17_file文件夹下的file文件夹复制到18_os文件夹中,并重命名为file_01
"""
import os

# 获取当前路径
cwd = os.getcwd()
# 设置目的路径
target_dir_path = os.path.join(cwd, 'file_01')

# 切换目录
os.chdir(r'../17_file/file')
# 设置原路径
src_dir_path = os.getcwd()


# 文件夹下的文件复制
def copy_file(src_path, target_path):
    print("source is {}".format(src_path))
    print("target is {}".format(target_path))
    # 若file文件夹不存在,创建file文件夹
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    # 获取源文件夹中的文件列表
    src_file_list = os.listdir(src_path)
    for filename in src_file_list:
        # 源文件路径
        src_file_path = os.path.join(src_path, filename)
        # 目的文件路径
        target_file_path = os.path.join(target_path, filename)
        with open(src_file_path, "rb") as src:
            # 读取源文件内容
            content = src.read()
            with open(target_file_path, "wb") as target:
                # 写入目的文件
                target.write(content)
    else:
        print("copy successfully!")


copy_file(src_dir_path, target_dir_path)
