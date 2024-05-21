"""
字典推导基本格式
    { key_expr: value_expr for value in collection }
    或
    { key_expr: value_expr for value in collection if condition }
"""
# 使用字符串及其长度创建字典:
list_demo = ['Google', 'Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
new_dict = {key: len(key) for key in list_demo}
print(new_dict)

# 提供三个数字,以三个数字为键,三个数字的平方为值来创建字典:
num_dict = {x: x ** 2 for x in (1, 2, 3)}
print(num_dict)
