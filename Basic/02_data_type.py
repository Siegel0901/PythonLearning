"""
数据类型:
int
float
string
boolean
"""

# 声明了一个名称交money的变量,赋值为28
money = 28
type(money)
# print()属于一个内置函数,负责输出结果
print(money)
# 通过type(变量名)输出变量类型
print(type(money))  # <class 'int'>

# money是一个变量,值允许发生变化
money = 280
print(money)
print(type(money))  # <class 'int'>

money = 28.9
print(money)
print(type(money))  # <class 'float'>

money = "一万"
print(money)
print(type(money))  # <class 'str'> 代表数据类型是字符串

money = '一万'
print(money)
print(type(money))

money = "一万"
print(money)
print(type(money))

money = '''一万'''
print(money)
print(type(money))

# 单引号,双引号,三引号均为字符串,嵌套使用可以确保文本中的引号使用正确
message = '''他说："矿金矿工都挖不出你这么纯的'神金'"。'''
print(message)

# 三引号可以保留文本格式输出
message = '''
            再小的个子 他也能成为法国皇帝
            再小的人物 他也能留下长的足迹'''
print(message)

# 布尔类型: True False  关键字
# 用于表述开发中的逻辑判断
isLogin = True  # 真
print(isLogin)
print(type(isLogin))    # <class 'bool'>
isLogin = False  # 假
print(isLogin)
