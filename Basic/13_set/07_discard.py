"""
Python Set discard()方法
描述
    discard()方法用于移除指定的集合元素
    该方法不同于remove()方法,因为remove()方法在移除一个不存在的元素时会发生错误,而discard()方法不会
语法
    set.discard(value)
参数
    value   必需,要移除的元素
返回值
    无
"""
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
fruits.discard("banana")
print(fruits)
