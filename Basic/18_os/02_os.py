# -*- coding = utf-8 -*-
# @Time : 2024/5/24 12:06
# @Author : Siegel
# @File : 02_os.py
# @Software : PyCharm
import os
import random

"""
os中的函数
    os.getcwd()
        获取当前文件目录
    os.listdir(path)
        获取指定路径下所有的文件和文件夹,保存至列表中
    os.mkdir(path)
        创建文件夹,path可以是绝对路径也可以是相对路径
    os.exists(path)
        查看path是否存在,返回布尔类型
    os.rmdir(path)
        删除文件夹,文件夹必须为空
    os.remove(path)
        删除文件
    os.chdir(path)
        切换目录
"""
# 获取当前文件目录
now_dir = os.getcwd()
print(now_dir)
print("".center(50, '-'))

# 获取指定路径下所有的文件和文件夹,保存至列表中
listdir_result = os.listdir(now_dir)
print(listdir_result)
print("".center(50, '-'))

# 创建文件夹
dirname = 'test_mkdir'
test_dir_path = os.path.join(now_dir, dirname)
if not os.path.exists(test_dir_path):
    os.mkdir(test_dir_path)

# 删除文件夹
if not os.listdir(test_dir_path):
    os.rmdir(test_dir_path)

# 删除文件
filename = 'remove_file.txt'
remove_path = os.path.join(now_dir, filename)
open(remove_path, 'w').close()
os.remove(remove_path)

# 删除有内容的文件夹
if not os.path.exists(test_dir_path):
    os.mkdir(test_dir_path)
    for i in range(3):
        path = os.path.join(test_dir_path, 'test_remove_{}.txt'.format(i))
        open(path, 'w').close()
file_list = os.listdir(test_dir_path)
for file in file_list:
    os.remove(os.path.join(test_dir_path, file))
else:
    os.rmdir(test_dir_path)

# 切换目录
path = os.getcwd()
print(path)
os.chdir('../')
path = os.getcwd()
print(path)
os.chdir(os.listdir(path)[random.randint(0, 17)])
path = os.getcwd()
print(path)
