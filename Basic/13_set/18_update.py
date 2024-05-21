"""
Python Set update()方法
描述
    update()方法用于修改当前集合,可以添加新的元素或集合到当前集合中,如果添加的元素在集合中已存在,则该元素只会出现一次,重复的会忽略
    与union的区别:
        update更新到自身,并不返回新集合
        union不更新自身,返回新集合
语法
    set.update(set)
参数
    set 必需,可以是元素或集合
返回值
    无
"""
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = {"Python", "Java", "C++", "JavaScript"}

x.update(y)

print(x)