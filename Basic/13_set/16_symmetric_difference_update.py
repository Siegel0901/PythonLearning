"""
Python Set symmetric_difference_update()方法
描述
    symmetric_difference_update()方法移除当前集合中在另外一个指定集合相同的元素
    并将另外一个指定集合中不同的元素插入到当前集合中
语法
    set.symmetric_difference_update(set)
参数
    set 要检测的集合
返回值
    无
"""
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

# x = x∪y - x∩y
result = x.symmetric_difference_update(y)
print(result)
print(x)