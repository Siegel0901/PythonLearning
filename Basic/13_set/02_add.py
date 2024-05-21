"""
Python Set add()方法
描述
    add()方法用于给集合添加元素,如果添加的元素在集合中已存在,则不执行任何操作
语法
    set.add(element)
参数
    element 必需,要添加的元素
返回值
    无
"""
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# 已存在的元素，则不执行添加操作
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)
