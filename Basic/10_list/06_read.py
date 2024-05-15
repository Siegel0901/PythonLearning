"""
查找:
    1. 元素 (not) in 列表
        返回bool类型
    2. 列表.index(元素)
        返回元素的下标位置,如果没有此元素则报错
    3. 列表.count(元素)
        存在返回个数,不存在返回0
"""
list1 = ['CPU', '显卡', '主板', '内存', '硬盘', '散热', '机箱']
print('CPU' in list1)
print(list1.index('CPU'))
print(list1.count('显卡'))
print(list1.count('风扇'))
