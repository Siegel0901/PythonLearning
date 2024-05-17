"""
Python3字典items()方法
描述
    Python字典items()方法以列表返回视图对象,是一个可遍历的key/value对
    dict.keys()、dict.values()和dict.items()返回的都是视图对象(view objects)
        提供了字典实体的动态视图,这就意味着字典改变,视图也会跟着变化
    视图对象不是列表,不支持索引,可以使用list()来转换为列表
    我们不能对视图对象进行任何的修改,因为字典的视图对象都是只读的
语法
    dict.items()
参数
    NA
返回值
    返回可视图对象
"""
tiny_dict = {'Name': 'Runoob', 'Age': 7}
print(tiny_dict.items())

# 遍历
for i, j in tiny_dict.items():
    print(i, j)

# 转换为列表
list1 = list(tiny_dict.items())
print(list1)
