"""
Python的元组与列表类似，不同之处在于元组的元素不能修改(增删改)
元组使用小括号(),列表使用中括号[]
关键字:
    list 列表
    tuple 元组
定义:
    变量名 = ()
注意:
    1. 如果元组中只有一个元素,必须添加逗号
    2. 元组支持下标和切片
    3. index(value, start, stop)
        [start, stop)范围中,找到第一个值等于value的元素位置,找不到报错
    4. 元组支持count
    5. 元组支持(not) in关键字
    6. 元组支持循环
与列表的转换:
    1. list(tuple) ---> 元组转列表
    2. tuple(list) ---> 列表转元组
"""

t1 = ()
print(type(t1))  # <class 'tuple'>

t1 = ('aa')
print(type(t1))  # <class 'str'>

t1 = ('aa',)
print(type(t1))  # <class 'tuple'>

t2 = ('a', 'b', 'c', 'a', 'b')
print(type(t2))  # <class 'tuple'>

print('-' * 40)

# 下标和切片
print(t2[0])
print(t2[0::2])
print(t2[::-1])

print('-' * 40)

# count计数
n = t2.count('c')
print(n)

print('-' * 40)

# index索引
print(t2.index('a'))
print(t2.index('a', 1, 4))

print('-' * 40)

# (not) in
if 'a' in t2:
    print(t2.count('a'))

print('-' * 40)

# for...in循环
for i in t2:
    print(i, end=' ')

print()
print('-' * 40)

# 转换
list1 = list(t2)
list1.append('ace')
print(list1)
t2 = tuple(list1)
print(t2)