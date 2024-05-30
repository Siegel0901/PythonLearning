# -*- coding = utf-8 -*-
# @Time : 2024/5/30 16:47
# @Author : Siegel
# @File : 18_singleton.py
# @Software : PyCharm
"""
单例模式:
    单例模式是指在整个应用程序中,某个类只能有一个实例存在,且该实例可被任何模块访问到.
    这种模式的应用场景包括数据库连接池、日志对象等需要全局唯一性的对象
"""


class Student:
    pass


stu1 = Student()
stu2 = Student()
print(stu1)
print(stu2)
print(stu1 is stu2)

print("".center(50, '-'))


class Singleton:
    # 私有类变量__instance
    __instance = None

    def __new__(cls):
        # 检查_instance是否为None
        if cls.__instance is None:
            # 如果是None,则创建一个新的实例并将其分配给_instance
            cls.__instance = object.__new__(cls)
        # 否则直接返回_instance,保证只有一个Singleton实例
        return cls.__instance


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
# 输出结果为True,说明s1和s2引用的是同一个实例,则单例模式实现成功
print(s1 is s2)  # True
