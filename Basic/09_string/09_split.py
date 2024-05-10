"""
切割字符串
    split
        split(sep,maxsplit)
            sep:分隔符
            maxsplit:最多分割次数
            返回的结果是一个列表
    rsplit
        right split
    splitlines
        按照行分割
        返回结果是一个列表
    partition
        按照分隔符分为三部分
    rpartition
        right partition
"""

s = 'php java python go c c++ c# lisp'
print(s.split(" "))
print(s.split(" ", 1))
print(s.rsplit(" ", 1))
print('-' * 40)

s = """    php java python go c c++ c# lisp
    php is the best programming language
    lisp is the best programming language in the world
"""
print(s)
print(s.splitlines())
print('-' * 40)

s = 'php java python go c c++ c# lisp'
print(s.partition(" "))
print(s.rpartition(" "))