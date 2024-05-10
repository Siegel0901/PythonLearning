"""
转义字符:
    \n  \t  \\  \'  \"
"""
print("Hello \nWorld!")
print("Hello \tWorld!")
print("Hello \\World!")
print("Hello \'World!")
print("Hello \"World!")

print('-' * 40)

# 字符串常量池
s1 = "Hello World!"
s2 = s1
s3 = 'Hello World!'
s4 = s1 + s2 + s3

# id()取当前变量的内存地址
print(id(s1), id(s2), id(s3), id(s4))

# is:比较变量的内存地址
print(s1 is s2)
print(s1 is s4)

s1 = "Hello World?"
print(s1, s2, s3, s4)

print('-' * 40)