"""
字符串索引机制:
    1. 从前往后
        0～len(s)-1
    2. 从后往前
        -len(s)～-1
"""
s = "Hello World"
print(len(s))
print(s[0], s[1])
print(s[-1], s[len(s) - 1])

print('-' * 40)

"""
切片:
    适用于字符串和列表
格式:
    1. 字符串变量[start:end]
        切片范围为[start,end)
        如果省略start,默认从字符串的首部开始
        如果省略end,则默认取到字符串的末尾
    2. 字符串变量[start:end:step]
        step的作用:
            1. 步长
            2. 更改获取元素的方向
                1. 正数:从左到右(默认)
                2. 负数:从右到左
"""
s = "ABCDEFG"
# 取ABC
print(s[:3])
# 取BCD
print(s[1:4])
# 取BCDEF
print(s[1:-1])
# 取EFG
print(s[-3:])
# 取ABCDEFG
print(s[:])

# 再次验证字符串常量值
print(s is s[:])  # True

print('-' * 40)

# step为步长
print(s[:-1:2])  # ACE
print(s[1::2])  # BDF
print(s[::-1])  # GFEDCBA
print(s[::-2])  # GECA
print(s[0:6:-1])  # 空
