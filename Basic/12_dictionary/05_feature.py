"""
字典的特性
    字典值可以是任何的python对象,既可以是标准的对象,也可以是用户定义的,但键不行
两个重要的点需要记住：
    1. 不允许同一个键出现两次,创建时如果同一个键被赋值两次,后一个值会被记住
    2. 键必须不可变,所以可以用数字,字符串或元组充当,而用列表就不行
"""

# 不允许同一个键出现两次,创建时如果同一个键被赋值两次,后一个值会被记住
tiny_dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print("tiny_dict['Name']: ", tiny_dict['Name'])

# 用元组当键
tiny_dict = {('Name',): 'Runoob', 'Age': 7}
print("tiny_dict[('Name',)]: ", tiny_dict[('Name',)])

# 用列表当键会报错
tiny_dict = {['Name']: 'Runoob', 'Age': 7}
print("tiny_dict['Name']: ", tiny_dict['Name'])