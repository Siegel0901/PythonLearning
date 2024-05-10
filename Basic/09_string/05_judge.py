"""
判断:
    startswith
        判断是否以xxx开头
    endswith
        判断是否以xxx结尾
    isalpha
        判断是否全为字母
    isdigit
        判断是否全为数字
    isalnum
        判断是否为字母或数字
    isspace
        判断是否为空格
    isupper
        判断是否全为大写字母
    islower
        判断是否全为小写字母
    返回值都是布尔类型的(True or False)
"""
str1 = 'hello'
print(str1.startswith('he'))
print(str1.endswith('o'))
print('-' * 40)

str2 = '123'
print(str2.isdigit())
print(str2.isalpha())
print(str2.isalnum())
print(str2.isspace())
print('-' * 40)

str3 = 'abc'
print(str3.isdigit())
print(str3.isalpha())
print(str3.isalnum())
print(str3.isspace())
print('-' * 40)

str4 = 'abc123'
print(str4.isdigit())
print(str4.isalpha())
print(str4.isalnum())
print(str4.isspace())
print('-' * 40)

str5 = ' '
print(str5.isdigit())
print(str5.isalpha())
print(str5.isalnum())
print(str5.isspace())
print('-' * 40)

str6 = 'ABC'
print(str6.isupper())
print(str6.islower())
print('-' * 40)
