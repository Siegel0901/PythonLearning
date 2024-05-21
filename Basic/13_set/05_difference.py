"""
Python Set difference()方法
描述
    difference()方法用于返回集合的差集,即返回的集合元素包含在第一个集合中,但不包含在第二个集合(方法的参数)中
语法
    set.difference(set)
参数
    set 必需,用于计算差集的集合
返回值
    返回一个新的集合
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# z = x - y = x - x ∩ y
z = x.difference(y)

print(x)
print(y)
print(z)