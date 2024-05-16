# 冒泡排序
import random

random_length = random.randint(1, 10)
random_list = [random.randint(0, 100) for i in range(random_length)]

print(random_list)

for i in range(random_length - 1):
    for j in range(random_length - i - 1):
        if random_list[j] >= random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
print(random_list)
