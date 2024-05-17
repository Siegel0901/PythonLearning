"""
删除元组
    元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
"""
tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
del tup
print("删除后的元组 tup : ")
print(tup)
"""
Traceback (most recent call last):
  File "D:\Program Files\ProjectSpace\PyCharmProject\PythonLearning\Basic\11_tuple\04_delete.py", line 10, in <module>
    print(tup)
          ^^^
NameError: name 'tup' is not defined
"""