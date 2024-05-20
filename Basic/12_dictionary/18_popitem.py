"""
Python3字典popitem()方法

描述
    Python字典popitem()方法随机返回并删除字典中的最后一对键和值
    如果字典已经为空,却调用了此方法,就报出KeyError异常
语法
    popitem()
参数
    无
返回值
    返回最后插入键值对(key,value形式),按照LIFO(LastInFirstOut后进先出法)顺序规则,即最末尾的键值对
注意
    在Python3.7之前,popitem()方法删除并返回任意插入字典的键值对
"""

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
print(site)

# ('url': 'www.runoob.com') 最后插入会被删除
result = site.popitem()

print('返回值 = ', result)
print('site = ', site)

# 插入新元素
site['nickname'] = 'Runoob'
print('site = ', site)

# 现在 ('nickname', 'Runoob') 是最后插入的元素
result = site.popitem()

print('返回值 = ', result)
print('site = ', site)