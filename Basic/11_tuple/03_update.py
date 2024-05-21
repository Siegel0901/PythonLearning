"""
修改元组
    元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
"""
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

"""
关于元组是不可变的
    所谓元组的不可变指的是元组所指向的内存中的内容不可变。
    重新赋值的元组tup1，绑定到新的对象了，不是修改了原来的对象。
"""
print(id(tup1))  # 查看内存地址
tup1 = tup1 + tup2
print(id(tup1))  # 内存地址不一样了