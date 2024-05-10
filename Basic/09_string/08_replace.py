"""
替换内容:
    replace(old, new, count)
        old:被替换词
        new:替换词
        count:替换个数(默认全部替换)
"""

s = "php is the best programming language, php is the best programming language in the world!"
result = s.replace("php", "python")
print(result)
result = s.replace("php", "python",1)
print(result)