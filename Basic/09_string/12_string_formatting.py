"""
格式化:
    1. %d   %s  %f
        print("Siegel说:\"%s\"" % string)
    2. format
"""
name = "Siegel"
age = 24
print("%s今年%d岁" % (name, age))
print("{}今年{}岁".format(name, age))
# 使用数字填充,从0开始计数
print("{0}今年{1}岁,{0}在上班时间学习python".format(name, age))
# 使用变量名填充,format的参数必须是关键字参数
print("{name}今年{age}岁,{name}在上班时间学习python".format(name="Siegel", age=24))
