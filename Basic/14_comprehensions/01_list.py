"""
Python推导式是一种独特的数据处理方式,可以从一个数据序列构建另一个新的数据序列的结构体
Python支持各种数据结构的推导式:
    列表(list)推导式
    字典(dict)推导式
    集合(set)推导式
    元组(tuple)推导式
列表推导式格式为:
    [表达式 for 变量 in 列表]
    [out_exp_res for out_exp in input_list]
    或者
    [表达式 for 变量 in 列表 if 条件]
    [out_exp_res for out_exp in input_list if condition]
    out_exp_res:
        列表生成元素表达式,可以是有返回值的函数
    for out_exp in input_list:
        迭代input_list将out_exp传入到out_exp_res表达式中
    if condition:
        条件语句,可以过滤列表中不符合条件的值
"""
# 过滤掉长度小于或等于3的字符串列表,并将剩下的转换成大写字母:
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# 计算30以内可以被3整除的整数:
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
