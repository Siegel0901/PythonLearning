"""
Python3字典copy()方法
描述
    Python字典copy()函数返回一个字典的浅复制
语法
    dict.copy()
参数
    NA
返回值
    返回一个字典的浅复制
"""
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

dict2 = dict1  # 直接赋值:引用对象
dict3 = dict1.copy()  # 浅拷贝:父对象（一级目录）不同,子对象（二级目录）相同,子对象是引用

# 修改data数据
dict1['user'] = 'root'
dict1['num'].remove(1)

# 输出结果
print(dict1)
print(dict2)
print(dict3)
"""
dict2其实是dict1的引用(别名),所以输出结果都是一致的
dict3父对象进行了深拷贝,不会随dict1修改而修改,子对象是浅拷贝所以随dict1的修改而修改。
Python 直接赋值、浅拷贝和深度拷贝解析:
https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
"""

