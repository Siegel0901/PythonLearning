"""
修改字典
    向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
"""
tiny_dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

tiny_dict['Age'] = 8  # 更新 Age
tiny_dict['School'] = "菜鸟教程"  # 添加信息

print("tiny_dict['Age']: ", tiny_dict['Age'])
print("tiny_dict['School']: ", tiny_dict['School'])