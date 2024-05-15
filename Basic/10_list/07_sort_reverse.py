# 生成8个1-20之间的随机整数,保存到列表中,遍历打印
import random

list1 = []
for i in range(8):
    ranInt = random.randint(1, 20)
    list1.append(ranInt)
print(list1)
# 翻转数组
list1.reverse()
print(list1)

"""
排序
    sort默认升序,可以通过reverse参数控制升序还是降序
    reverse=True    降序
    reverse=False   升序
"""
# list.sort()
list1.sort(reverse=True)
print(list1)
