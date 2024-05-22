"""
    在字典中遍历时,关键字和对应的值可以使用 items() 方法同时解读出来
"""
knights = {'siegel': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
