"""
Python3字典clear()方法
描述
    Python字典clear()函数用于删除字典内所有元素
语法
    dict.clear()
参数
    NA
返回值
    该函数没有任何返回值。
"""
dict1 = {"name": "Siegel", "age": 24, "city": "TianJin"}
print(dict1)
print("字典长度 : %d" % len(dict1))

dict1.clear()
print(dict1)
print("字典清空后长度 : %d" % len(dict1))
