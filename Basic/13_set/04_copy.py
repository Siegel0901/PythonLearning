"""
Python Set copy()方法
描述
    copy()方法用于拷贝一个集合
语法
    set.copy()
参数
    无
返回值
    返回拷贝的集合
"""
# 打印集合中元素的顺序是随机的
sites = {"Google", "Runoob", "Taobao"}
print(sites)
x = sites.copy()
print(x)
