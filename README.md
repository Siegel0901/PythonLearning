# Basic:python基础知识学习

## python安装

python安装csdn教程： http://t.csdnimg.cn/8Zbd3

## pycharm使用与安装

pycharm安装csdn教程： http://t.csdnimg.cn/FyEMb

## 基础语法学习

### 变量

1. 注释:单行、多行
2. 格式：变量名=值
3. 起名：驼峰or下划线

### 数据类型

int float str bool

### 类型转换

1. a = 10 str(a)
2. str = input('提示语句')
3. 所有键盘输入的内容都是字符串类型

### 运算符

1. 算术 + - * / % // **
2. 赋值 = += -= *= /= %= //= **=
3. 比较 > < >= <= == != 结果：True False
4. 逻辑 and or not 结果：True False

### 输出格式化
1. %s字符串string
2. %d整数digit
3. %f浮点数float

### 进制转换
1. 进制
   1. 二进制:0,1
   2. 八进制:0,1,2,3,4,5,6,7
   3. 十进制:0,1,2,3,4,5,6,7,8,9
   4. 十六进制:0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
2. 前缀:
   1. 0b  二进制
   2. 0o  八进制
   3. 0x  十六进制
   4. 默认十进制
3. 函数:
   1. bin()   0b
   2. int()
   3. oct()   0o
   4. hex()   0x
4. 进制转换
   1. 二进制与十六进制之间的转换:
    从低位到高位,二进制四位一组对应十六进制的一位,高位不足补0
   2. 二进制与八进制之间的转换:
    从低位到高位,二进制三位一组对应八进制的一位,高位不足补0

### 位运算
针对二进制进行的运算
1. "&"与
2. "|"或
3. "^"异或
4. "~"非
5. "<<"左移
6. ">>"右移
   1. 负数补码移位运算:
    左移同原码添0,右移同反码添1
   2. Python的移位运算符是逻辑移位,不考虑符号位(星火大模型)

### 运算符的优先级
可用()提高优先级

### 条件语句
      格式1:
         if 条件:
            条件成立要执行的语句
      格式2:
         if 条件:
            条件成立要执行的语句
         else:
            条件不成立要执行的语句
      格式3:
         if 条件1:
             条件1True,执行的语句
         elif 条件2:
             条件2True,执行的语句
         elif 条件3:
             条件3True,执行的语句
         ...
         else:
             1,2,3条件都为False的情况下,执行的语句
      嵌套if:
         if 条件1:
             if 条件2:
                 条件1为True,条件2为True,执行语句
             else:
                 条件1为True,条件2为False,执行语句
         else:
             条件1为False,执行语句
      三目运算符:
          结果1 if 条件 else 结果2
          当条件为真时,返回结果1,否则返回结果2
      自动类型转换:
          if语句需要一个判断条件,这个判断条件的结果需要一个布尔值.
          如果此时输入的判断条件不是一个布尔值,在代码执行的过程中,会将这个值自动转换成一个布尔值.
          在Python中,只有0,"",'',None,(),{},[]会被转换成False,其他都会被转换成True

### 循环
      循环:
         场景:
            1. 用户名和密码,反复输入
            2. 计算1-100
            3.游戏,死了重生
            ...
            方式:
               1. while
                  2. for
            格式:
               1. while格式
                  while 条件:
                     要循环执行的代码
               2. for格式
                  for i in range(n):
                     循环体中的内容
               3. range():
                     range(stop):[0,stop)
                     range(start,stop):[start,stop)
                     range(start,stop,step):
                     [start,stop),
                     step为步长(增量),默认为1
               4. for...else格式:
                  for i in range(n):
                     循环体
                  else:
                     如果上面的for循环0~n-1没有出现中断(break),执行else部分
               5. while...else格式:
                  while 循环条件:
                     循环体
                  else:
                     如果上面的循环中没有出现中断(break),执行else部分
               6.1 循环嵌套:
                  1. while嵌套
                     while 循环条件:
                        while 循环条件:
                           执行语句
                  2. for嵌套
                     for i in range(n):
                        for j in range(n):
                           执行语句