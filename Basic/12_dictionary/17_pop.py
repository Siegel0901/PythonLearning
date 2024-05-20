"""
Python3字典pop()方法
描述
    Python字典pop()方法删除字典key(键)所对应的值,返回被删除的值
语法
    pop(key[,default])
参数
    key     要删除的键
    default 当键key不存在时返回的值
返回值
    返回被删除的值:
        如果key存在-->删除字典中对应的元素
        如果key不存在-->返回设置指定的默认值default
        如果key不存在且默认值default没有指定-->触发KeyError异常
"""

site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
print(site)

element = site.pop('name')

print('删除的元素为:', element)
print('字典为:', site)

print("".center(40, '-'))

element = site.pop('nickname', '不存在的key的默认值设定')

print('删除的元素为:', element)
print('字典为:', site)
print("".center(40, '-'))

# 如果删除的键不存在,且未指定默认值,会触发异常
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

element = site.pop('nickname')

print('删除的元素为:', element)
print('字典为:', site)