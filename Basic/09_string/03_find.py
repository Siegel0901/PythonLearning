"""
查找
    find
        从左向右查找,只要遇到一个符合要求的则返回位置
        如果没有找到任何符合要求的则返回-1
    rfind
        right find
        从右向左查找
    index
    rindex

    index与find的区别:找不到符合要求的会报错,不会返回-1
"""

path = "https://pss.bdstatic.com/static/superman/img/logo/logo_white-d0c9fe2af5.png"
i = path.find("/logo_")
print(path[i + 1:])

i = path.rfind(".")
print(path[i:])

i = path.find("Siegel")
print(i)
print(path[:i])

i = path.index("Siegel")