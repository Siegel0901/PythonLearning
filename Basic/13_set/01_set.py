"""
Python3集合
    集合(set)是一个无序的不重复元素序列
    集合中的元素不会重复,并且可以进行交集、并集、差集等常见的集合操作
    可以使用大括号{}创建集合,元素之间用逗号,分隔,或者也可以使用set()函数创建集合
创建格式:
    param = {value01, value02, }
    或者
    set(value)
注意:
    创建一个空集合必须用set()而不是{},因为{}是用来创建一个空字典

更多实例演示：
"""
set1 = {1, 2, 3, 4}  # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])  # 使用set()函数从列表创建集合
print(set1)
print(set2)

print("".center(50, "-"))

# 这里演示的是去重功能
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print("".center(50, "-"))

# 快速判断元素是否在集合内
print('orange' in basket)
print('crabgrass' in basket)

print("".center(50, "-"))

# 下面展示两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
# 集合a
print(a)
# 集合a中包含而集合b中不包含的元素
print(a - b)
# 集合a或b中包含的所有元素
print(a | b)
# 集合a和b中都包含了的元素
print(a & b)
# 不同时包含于a和b的元素
print(a ^ b)
