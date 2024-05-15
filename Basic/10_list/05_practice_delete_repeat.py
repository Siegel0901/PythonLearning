
list1 = ['CPU', '显卡', '主板', '内存', '硬盘', '散热', '机箱', '风扇', '风扇', '风扇']

# 用下面这种方法remove循环删除多个值相等的元素,会有漏删的情况
# 原因是立即删除后,后面的元素前移,下标后移,如果此时前移的元素需要删除,则会被漏掉
for item in list1:
    if item == '风扇':
        list1.remove(item)
# ['CPU', '显卡', '主板', '内存', '硬盘', '散热', '机箱', '风扇']
print(list1)

print('-' * 60)

# 用while循环控制下标解决漏删问题
list1.append("风扇")
list1.append("风扇")
list1.append("风扇")
n = 0
while n < len(list1):
    if list1[n] == '风扇':
        list1.remove(list1[n])
    else:
        n += 1
print(list1)  # ['CPU', '显卡', '主板', '内存', '硬盘', '散热', '机箱']

print('-' * 60)

# 用for循环控制下标解决漏标问题
list1.append("风扇")
list1.append("风扇")
list1.append("风扇")
for i in list1[::-1]:  # 从后往前遍历,这样下标移动的方向和元素移动的方向一致
    if i == '风扇':
        list1.remove(i)
print(list1)  # ['CPU', '显卡', '主板', '内存', '硬盘', '散热', '机箱']

print('-' * 60)

# 用关键字in删除元素
list1.append("风扇")
list1.append("风扇")
list1.append("风扇")
while "风扇" in list1:
    list1.remove("风扇")
print(list1)  # ['CPU', '显卡', '主板', '内存', '硬盘', '散热', '机箱']
