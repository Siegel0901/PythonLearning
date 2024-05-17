"""
    元组支持count,index,(not) in,循环等操作
"""

t2 = ('a', 'b', 'c', 'a', 'b')

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
