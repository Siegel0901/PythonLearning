"""
删除字典
    能删单一的元素也能清空字典
    显式删除一个字典用del命令
"""

tiny_dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(tiny_dict)

del tiny_dict['Name']  # 删除键 'Name'
print(tiny_dict)

tiny_dict.clear()  # 清空字典
print(tiny_dict)

del tiny_dict  # 删除字典
print("tiny_dict['Age']: ", tiny_dict['Age'])
print("tiny_dict['School']: ", tiny_dict['School'])