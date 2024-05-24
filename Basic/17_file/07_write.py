# -*- coding = utf-8 -*-
# @Time : 2024/5/24 9:56
# @Author : Siegel
# @File : 07_write.py
# @Software : PyCharm

file = open("../17_file/file/test2.txt", 'w')
file.write("this is the first line in test2.txt\n")
file.write("this is the second line in test2.txt\n")

file.close()
