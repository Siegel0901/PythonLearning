# -*- coding = utf-8 -*-
# @Time : 2024/5/24 9:54
# @Author : Siegel
# @File : 06_writable.py
# @Software : PyCharm
file = open('../17_file/file/test1.txt', 'w')
result = file.writable()
print(type(result))
print(result)
file.close()
