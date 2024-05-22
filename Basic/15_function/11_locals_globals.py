"""
locals()和globals()
    locals()函数可以查看本地变量有哪些,以字典形式输出
    globals()函数可以查看全局变量有哪些,以字典形式输出(注意里面会有一些系统的键值对)
"""
x = 1000


def func():
    n = 100
    list1 = [1, 2, 3]

    def func2():
        list2 = [4, 5, 6]
        print(locals())

    func2()
    print(locals())


func()

print(globals())
