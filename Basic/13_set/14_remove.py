"""
Python Set remove()方法
描述
    remove()方法用于移除集合中的指定元素
    该方法不同于discard()方法,因为remove()方法在移除一个不存在的元素时会发生错误,而discard()方法不会
语法
    set.remove(item)
参数
    item    要移除的元素
返回值
    没有返回值
"""
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)
fruits.discard("banana")
print("".center(50, "-"))
fruits.remove("banana")
