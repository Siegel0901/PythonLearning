"""
Python Set issubset()方法
描述
    issubset()方法用于判断集合的所有元素是否都包含在指定集合中,如果是则返回True,否则返回False
语法
    set.issubset(set)
参数
    set 必需,要比查找的集合
返回值
    返回布尔值,如果都包含返回True,否则返回False
"""
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

z = x.issubset(y)

print(z)
