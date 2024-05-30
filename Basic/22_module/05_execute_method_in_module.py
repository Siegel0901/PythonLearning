# -*- coding = utf-8 -*-
# @Time : 2024/5/30 22:43
# @Author : Siegel
# @File : 05_execute_method_in_module.py
# @Software : PyCharm
"""
无论是哪种导入方式,都会将模块中的内容加载到内存
如果不希望模块中的函数调用部分被执行,可以使用__name__过滤
    在自己的模块中,__name__ == __main__
    在其他模块中通过导入的方式调用,__name__ == 模块名
"""
