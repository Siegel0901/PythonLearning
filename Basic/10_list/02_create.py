"""
添加元素:
    append(value):追加,类似排队
    extend(list):合并延长列表
    insert(index,value):插入
    index(value):根据元素值返回找到的第一个符合要求的元素位置
"""
list1 = []
list2 = ['内存']

print(list1)
list1.append('CPU')
print(list1)
list1.append('显卡')
list1.append('主板')
print(list1)

list2.append('硬盘')
print(list2)

"""
加号
    数字: n = 1 + 3 + 5 + 7 + 11 + 13 ---> n = 4
    字符串: s = 'a' + 'b' + 'c' + 'd' + 'e' ---> s = 'abcde'
    列表: list0 = ['a', 'b'] + [1, 2]  ---> list0 = ['a', 'b', 1, 2] 
"""
list1 = list1 + list2
print(list1)

list3 = ['散热', '机箱', '电源']
list1.extend(list3)
# ['CPU', '显卡', '主板', '内存', '硬盘', '散热', '机箱', '电源']
print(list1)

pos = list1.index('散热')
list1.insert(pos, '风扇')
print(list1)