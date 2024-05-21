"""
Python Set intersection()方法
描述
    intersection()方法用于返回两个或更多集合中都包含的元素,即交集
语法
    set.intersection(set1,set2...etc)
参数
    set1    必需,要查找相同元素的集合
    set2    可选,其他要查找相同元素的集合,可以多个,多个使用逗号,隔开
返回值
    返回一个新的集合
"""
# 返回一个新集合,该集合的元素既包含在集合x又包含在集合y中
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

# z = x ∩ y
z = x.intersection(y)

print(z)

# 计算多个集合的交集
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
