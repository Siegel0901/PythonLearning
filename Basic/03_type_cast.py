# message = "Hello Python"
# print(message)
# message = input("input message:")
# print(message)
# print(type(message))

money = input("input money:")
print(money)
print(type(money))  # <class 'str'>

# print(money +1000) # TypeError: can only concatenate str (not "int") to str

# 类型转换
# str------->int
print(int(money) + 1000)
print(type(int(money) + 1000))
# int------->str
print(money + "1000")
print(type(money + "1000"))

"""
练习：
键盘输入两个整数,输出两个整数的和,输出差
input('输入第一个数:')
input('输入第二个数:')
"""
# 输入
num1 = input('输入第一个数:')
num2 = input('输入第二个数:')
# 计算
print(num1 + num2)
# 类型转换
print(int(num1) + int(num2))
print(float(num1) + float(num2))

'''
以变量名a为例
    str --------> int   int(a)      但是如果'9.9'而且是字符串类型转成int的时候报错了
    str --------> float float(a)
    
    int --------> str   str(a)
    float ------> str   str(a)
    
    int --------> float float(a)
    float ------> int   int(a)      只不过float类型中小数点后面的数字被抹掉了
'''

# 布尔类型转换
flag = True
print(int(flag))  # 1
print(float(flag))  # 1.0
print(str(flag))  # 'True'

'''
思考:
a = 5
能否将a转成bool类型
'''

a = 5
print(bool(a))  # True
a = 0
print(bool(a))  # False
a = -1
print(bool(a))  # True
a = ''
print(bool(a))  # False
# 变量的值是:0,''(空字符串),转换结果是False,其他只要变量有值则为True
