"""
空格处理:
    添加空格控制字符串的对齐方式
        ljust
            左对齐
        rjust
            右对齐
        center
            居中对齐
    删除字符串左侧或右侧的空格
        strip
            去除字符串两侧的空格
        lstrip
            去除字符串左侧的空格
        rstrip
            去除字符串右侧的空格
"""

username = "   Siegel     "
print(len(username))
print(username)
print(len(username.strip()))
print(username.strip())
print(len(username.lstrip()))
print(username.lstrip())
print(len(username.rstrip()))
print(username.rstrip())

username = "Siegel"
print(username.center(40))
print(username.center(40, "-"))
print(username.ljust(40))
print(username.ljust(40, "-"))
print(username.rjust(40))
print(username.rjust(40, "-"))
