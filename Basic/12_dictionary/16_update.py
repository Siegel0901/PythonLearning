"""
Python3字典update()方法
描述
    Python字典update()函数把字典参数dict2的key/value(键/值)对更新到字典dict里
语法
    dict.update(dict2)
参数
    dict2   添加到指定字典dict里的字典
返回值
    该方法没有任何返回值
"""

tiny_dict = {'Name': 'Runoob', 'Age': 7}
tiny_dict2 = {'Sex': 'female'}

tiny_dict.update(tiny_dict2)
print("更新字典tiny_dict : ", tiny_dict)