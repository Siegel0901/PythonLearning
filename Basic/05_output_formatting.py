# -*- coding = utf-8 -*-
# @Time : 2024/5/1 11:58
# @Author : Siegel
# @File : 05_output_formatting.py
# @Software : PyCharm

# 打印:我喜欢听24岁的Siegel唱歌
name = 'Siegel'
age = 24

# python中int类型无法与str类型拼接
# print('我喜欢听' + age)
print('我喜欢听' + str(age) + '岁的' + name + '唱歌')

"""
输出格式化
    符号:
        %s  字符串 string
        %d  整数 digit
        %f  浮点数 float
"""
print('我喜欢听%d岁的%s唱歌' % (age, name))
# 打印:24岁的Siegel一首歌挣999.95元
money = 999.95
print('%d岁的%s一首歌挣%f元' % (age, name, money))
print('%s岁的%s一首歌挣%s元' % (age, name, money))  # 类型转换 str(age) str(money)
print('%d岁的%s一首歌挣%.2f元' % (age, name, money))
print('-' * 50)
"""
练习:
    键盘输入姓名和科目,考试分数,按照如下格式输出:
        xxx本次考试科目是:xxx,得分:xxx
    分数保留一位小数    
"""
name = input("请输入姓名:")
subject = input("请输入科目:")
score = float(input("请输入考试分数:"))
print('%s本次考试科目是:%s,得分:%.1f' % (name, subject, score))
