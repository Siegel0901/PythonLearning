"""
Python3字典fromkeys()方法
描述
    Python字典fromkeys()函数用于创建一个新字典,以序列seq中元素做字典的键,value为字典所有键对应的初始值
语法
    dict.fromkeys(seq[, value])
参数
    seq     字典键值列表。
    value   可选参数,设置键序列(seq)对应的值,默认为None
返回值
    该方法返回一个新字典
"""
seq = ('key1', 'key2', 'key3')

tiny_dict = dict.fromkeys(seq)
print("新的字典为 : %s" % str(tiny_dict))

tiny_dict = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(tiny_dict))