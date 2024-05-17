"""
Python3字典get()方法
描述
    Python字典get()函数返回指定键的值
语法
    dict.get(key[,value])
参数
    key     字典中要查找的键
    value   可选,如果指定键的值不存在时,返回该默认值
返回值
    返回指定键的值,如果键不在字典中返回默认值,如果不指定默认值,则返回None
"""

tiny_dict = {'Name': 'Runoob', 'Age': 27}

print("Age:", tiny_dict.get('Age'))

# 没有设置Sex,也没有设置默认的值,输出None
print("Sex:", tiny_dict.get('Sex'))

# 没有设置Salary,输出默认的值0.0
print('Salary:', tiny_dict.get('Salary', 0.0))

# 嵌套字典使用
# get()方法对嵌套字典的使用方法如下:
tiny_dict = {'RUNOOB': {'url': 'www.runoob.com'}}
res = tiny_dict.get('RUNOOB', {}).get('url')
print("RUNOOB url 为:", str(res))

"""
get()方法 Vs dict[key]访问元素区别
    get(key)方法在key(键)不在字典中时,可以返回默认值None或者设置的默认值
    dict[key]在key(键)不在字典中时,会触发KeyError异常
"""
runoob = {}
print('URL:', runoob.get('url'))  # 返回None
print(runoob['url'])  # 触发KeyError
