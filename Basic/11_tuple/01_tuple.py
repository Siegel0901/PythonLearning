"""
Python的元组与列表类似，不同之处在于元组的元素不能修改(增删改)
元组使用小括号(),列表使用中括号[]
关键字:
    list 列表
    tuple 元组
定义:
    变量名 = ()
注意:
    如果元组中只有一个元素,必须添加逗号
    元组支持下标和切片
"""

t1 = ()
print(type(t1))  # <class 'tuple'>

t1 = ('aa')
print(type(t1))  # <class 'str'>

t1 = ('aa',)
print(type(t1))  # <class 'tuple'>

t2 = ('a','b','c')
print(type(t2))  # <class 'tuple'>

# 下标和切片
print(t2[0])
print(t2[0::2])
print(t2[::-1])

# count计数
n = t2.count('c')
print(n)

# index索引
print(t2.index('c'))