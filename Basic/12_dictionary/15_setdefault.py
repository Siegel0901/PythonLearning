"""
Python3字典setdefault()方法
描述
    Python字典setdefault()方法和get()方法类似,如果键不存在于字典中,将会添加键并将值设为默认值
语法
    dict.setdefault(key, default=None)
参数
    key     查找的键值
    default 键不存在时,设置的默认键值
返回值
    如果key在字典中,返回对应的值
    如果不在字典中,则插入key及设置的默认值default,并返回default,default默认值为None
"""

tiny_dict = {'Name': 'Runoob', 'Age': 7}

print("Age键的值为:%s" % tiny_dict.setdefault('Age', None))
print("Sex键的值为:%s" % tiny_dict.setdefault('Sex', None))
print("新字典为:", tiny_dict)

print("".center(40, '-'))

"""
setdefault和get的区别:
    key不在字典中时,setdefault插入key和设置的默认值default
    get不会插入key,而是返回设置的默认值default
"""
tiny_dict = {'Name': 'Runoob', 'Age': 7}

print("Age键的值为:%s" % tiny_dict.get('Age', None))
print("Sex键的值为:%s" % tiny_dict.get('Sex', None))
print("字典为:", tiny_dict)
