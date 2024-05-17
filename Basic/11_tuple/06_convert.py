"""
与列表的转换:
    1. list(tuple) ---> 元组转列表
    2. tuple(list) ---> 列表转元组
"""
t2 = ('a', 'b', 'c', 'a', 'b')
# 转换
list1 = list(t2)
list1.append('ace')
print(list1)
t2 = tuple(list1)
print(t2)
