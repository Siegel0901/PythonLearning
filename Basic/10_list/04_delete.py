"""
删除元素
    pop
        pop(index):
            根据下标删除列表中的元素,下标写的时候注意不要超出范围(报错IndexError:index out of range)
        pop():
            从后往前删除
    remove
        remove(value):
            根据元素值删除列表中的元素,如果删除的元素不存在则(报错ValueError:list.remove(x):x not in list)
            如果列表中存在多个值相等的元素,只删除遇到的第一个元素,后面的元素不会被删除
        关键字in:
            元素 in 列表
            表示元素是否在列表中? 返回bool类型
    clear
        清空列表元素
    del list[index]
        根据下标删除元素
    del list
        删除指向列表的指针list
"""
list1 = ['CPU', '显卡', '主板', '内存', '硬盘', '散热', '机箱', '电源']
list1.pop(-1)
print(list1)

print('-' * 60)

list1.append("风扇")
list1.append("风扇")
list1.append("风扇")
print(list1)
list1.remove("风扇")
print(list1)

# 判断是否存在要删除的元素
print('风扇' in list1)

print('-' * 60)
"""
del list[index]
    删除列表中的元素
del list
    删除指向列表的指针list
list1 = [1, 2, 3, 4, 5]
list2 =  list1
此时list2与list1共享列表的地址空间
给list1增加元素会影响list2,因为他们共用地址空间
del list2会删除list2指向列表的指针,但不会影响list1
"""
del list1[0]
print(list1)

print('-' * 60)

list1.clear()
print(list1)
