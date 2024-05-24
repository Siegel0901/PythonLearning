# -*- coding = utf-8 -*-
# @Time : 2024/5/24 10:04
# @Author : Siegel
# @File : 08_writelines.py
# @Software : PyCharm

# mode=a,表示追加
file = open("../17_file/file/test2.txt", 'a')
file.writelines(['this is the third line in test2.txt\n', 'this is the fourth line in test2.txt\n'])
file.close()