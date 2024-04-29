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
num1 = input('输入第一个数:')
num2 = input('输入第二个数:')
print("两数之和:"+'{:,}'.format(int(num1) + int(num2)))
print("两数之差:"+'{:,}'.format(int(num1) - int(num2)))
