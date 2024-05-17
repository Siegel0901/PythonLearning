"""
Python字典包含了以下内置函数:
    len(dict)
        计算字典元素个数，即键的总数。
    str(dict)
        输出字典，可以打印的字符串表示。
    type(variable)
        返回输入的变量类型，如果变量是字典就返回字典类型。
"""
dict1 = {"name": "Siegel", "age": 24, "city": "TianJin"}
print(len(dict1))

print(dict1)
print(type(dict1))

print(str(dict1).center(100, '-'))
print(type(str(dict1)))
