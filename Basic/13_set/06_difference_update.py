"""
Python Set difference_update()方法
描述
    difference_update()方法用于移除两个集合中都存在的元素(去重留下差集)
    difference_update()方法与difference()方法的区别在于
        difference()方法返回一个移除相同元素的新集合
        而difference_update()方法是直接在原来的集合中移除元素,没有返回值
语法
    set.difference_update(set)
参数
    set 必需,用于计算差集的集合
返回值
    无
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

result = x.difference_update(y)
print(result)
print(x)
print(y)