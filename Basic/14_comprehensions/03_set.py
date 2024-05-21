"""
集合推导式基本格式:
    { expression for item in Sequence }
    或
    { expression for item in Sequence if conditional }
"""
# 计算数字1,2,3的平方数:
set1 = {i ** 2 for i in (1, 2, 3)}
print(set1)
# 判断不是abc的字母并输出:
set2 = {word for word in 'fdjakafkdlabfkldajc' if word not in 'abc'}
print(set2)
