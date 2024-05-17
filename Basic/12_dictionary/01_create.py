"""
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值key=>value对用冒号:分割,每个对之间用逗号(,)分割,整个字典包括在花括号{}中
格式如下所示：
    d = {key1: value1, key2: value2, key3: value3}
注意:
    1. dict作为Python的关键字和内置函数,变量名不建议命名为dict
    2. 键必须是唯一的,但值则不必
    3. 值可以取任何数据类型,但键必须是不可变的,如字符串,数字
"""
# 创建字典
tiny_dict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
# 使用大括号{}创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

print('-' * 40)

# 使用内建函数dict()创建字典
emptyDict = dict()

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))