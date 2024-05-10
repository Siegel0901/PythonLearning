"""
练习:
    模拟图片文件上传,键盘输入上传图片文件的名称(abc.jpg),判断文件名(abc)是否大于等于6位,扩展名是否是:jpg,gif,png格式
    如果不是则提示上传失败,如果名字不满足条件,而扩展名满足条件则随机生成一个6位字母和数字组成的文件名,打印:成功上传文件名.文件格式
"""
import random

numbers = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

filename = input("请输入上传图片文件的名称:")
# 判断扩展名
if filename.endswith(".jpg") or filename.endswith(".gif") or filename.endswith(".png"):
    i = filename.rfind(".")
    name = filename[:i]  # 截取文件名
    suffix = filename[i:]  # 截取扩展名
    if len(name) < 6:  # 文件名小于6位,构造随机6位字母数字组合作为文件名
        name = ''
        for i in range(6):
            index = random.randint(0, len(numbers) - 1)
            name += numbers[index]
    print("成功上传%s%s" % (name, suffix))
else:
    print("文件格式不对,上传失败!")
