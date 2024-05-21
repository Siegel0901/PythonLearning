"""
Python Set issuperset()方法
描述
    issuperset()方法用于判断指定集合的所有元素是否都包含在原始的集合中(超集)
    如果是则返回True,否则返回False
语法
    set.issuperset(set)
参数
    set 必需,要比查找的集合
返回值
    返回布尔值,如果都包含返回True,否则返回False
"""
# 判断集合y的所有元素是否都包含在集合x中
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

# 如果没有全部包含返回False
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)