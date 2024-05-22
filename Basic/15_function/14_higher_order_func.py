"""
高阶函数:
    高阶函数的参数是另一个函数
    系统高阶函数:max min sorted filter map reduce等
"""
"""
def max(*args, key=None): # known special case of max
    '''
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
    '''
    pass
"""
list1 = [('siegel', 24, 2000), ('tom', 22, 2002), ('luis', 18, 2006)]
print(max(list1, key=lambda x: x[1]))
print(max(list1, key=lambda x: x[2]))
print(min(list1, key=lambda x: x[1]))
print(min(list1, key=lambda x: x[2]))
print(sorted(list1, key=lambda x: x[1]))
print(sorted(list1, key=lambda x: x[2]))
print(sorted(list1, key=lambda x: x[1], reverse=True))
print(sorted(list1, key=lambda x: x[2], reverse=True))

# filter
'''
    """
    filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
'''
# filter的匿名函数要求返回值必须是bool类型,只有bool类型结果为True的才是符合过滤条件的
list2 = list(filter(lambda x: x[1] > 20, list1))
print(list2)

# map
'''
    """
    map(func, *iterables) --> map object
    
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """
'''
# map通过匿名函数指明想要提取的内容，并对内容进行加工
list3 = list(map(lambda x: (x[1] + 1, x[2] - 1), list1))
print(list3)
list4 = list(map(lambda x: x[0].title(), list1))
print(list4)

from functools import reduce

# reduce
'''
"""
    reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """
'''
# reduce对一个序列进行压缩运算,得到一个值
print(reduce(lambda x, y: x + y, list(map(lambda x: x[1], list1))))
