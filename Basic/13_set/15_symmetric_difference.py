"""
Python Set symmetric_difference()方法
描述
    symmetric_difference()方法返回两个集合中不重复的元素集合,即会移除两个集合中都存在的元素
    A∪B - A∩B
语法
    set.symmetric_difference(set)
参数
    set 集合
返回值
    返回一个新的集合
"""
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
# z = x∪y - x∩y
z = x.symmetric_difference(y)

print(x)
print(y)
print(z)
