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
               6 循环嵌套:
                  1. while嵌套
                     while 循环条件:
                        while 循环条件:
                           执行语句
                  2. for嵌套
                     for i in range(n):
                        for j in range(n):
                           执行语句
### 字符串
      1. 转义字符:
         \n  \t  \\  \'  \"
      2. 字符串常量池
         id()取当前变量的内存地址
         is:比较变量的内存地址
      3. 字符串索引机制:
         1. 从前往后
             0～len(s)-1
         2. 从后往前
            -len(s)～-1
      4. 切片:
         适用于字符串和列表
         格式:
            1. 字符串变量[start:end]
                切片范围为[start,end)
                如果省略start,默认从字符串的首部开始
                如果省略end,则默认取到字符串的末尾
            2. 字符串变量[start:end:step]
                step的作用:
                    1. 步长
                    2. 更改获取元素的方向
                        1. 正数:从左到右(默认)
                        2. 负数:从右到左
      5. 查找
         find
            从左向右查找,只要遇到一个符合要求的则返回位置
            如果没有找到任何符合要求的则返回-1
         rfind
            right find
            从右向左查找
         index
         rindex
         index与find的区别:找不到符合要求的会报错,不会返回-1
      6. 计数
         count
      7. 判断
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
      8. 替换内容:
         replace(old, new, count)
            old:被替换词
            new:替换词
            count:替换个数(默认全部替换)
      9. 切割字符串
          split
              split(sep,maxsplit)
                  sep:分隔符
                  maxsplit:最多分割次数
                  返回的结果是一个列表
          rsplit
              right split
          splitlines
              按照行分割
              返回结果是一个列表
          partition
              按照分隔符分为三部分
          rpartition
              right partition
      10. 大小写转换:
          upper
              全部转换为大写
          lower
              全部转换为小写
          title
              单词首字母大写
          capitalize
              字符串首字母大写
      11. 空格处理:
          添加空格控制字符串的对齐方式
              ljust
                  左对齐
              rjust
                  右对齐
              center
                  居中对齐
          删除字符串左侧或右侧的空格
              strip
                  去除字符串两侧的空格
              lstrip
                  去除字符串左侧的空格
              rstrip
                  去除字符串右侧的空格
      12. format格式化:
         使用数字填充,从0开始计数
         使用变量名填充,format的参数必须是关键字参数
### 列表
      如何定义一个列表:
          1. 空列表: []
          2. 有内容的列表
              ['A', 'B', 'C']
              [1, 2, 3]
              [3.5, 4.5, 5.5]
              [['A', 'B', 'C'], [1, 2, 3], []]
      添加元素:
          append(value):追加,类似排队
          extend(list):合并延长列表
          insert(index,value):插入
          index(value):根据元素值返回找到的第一个符合要求的元素位置
      删除元素
          pop
              pop(index):
                  根据下标删除列表中的元素,下标写的时候注意不要超出范围(报错IndexError:index out of range)
              pop():
                  从后往前删除
          remove
              remove(value):
                  根据元素值删除列表中的元素,如果删除的元素不存在则(报错ValueError:list.remove(x):x not in list)
                  如果列表中存在多个值相等的元素,只删除遇到的第一个元素,后面的元素不会被删除
              关键字in:
                  元素 in 列表
                  表示元素是否在列表中? 返回bool类型
          clear
              清空列表元素
          del list[index]
              根据下标删除元素
          del list
              删除指向列表的指针list
      查找:
          1. 元素 (not) in 列表
              返回bool类型
          2. 列表.index(元素)
              返回元素的下标位置,如果没有此元素则报错
          3. 列表.count(元素)
              存在返回个数,不存在返回0
      排序
          sort默认升序,可以通过reverse参数控制升序还是降序
          reverse=True    降序
          reverse=False   升序
### 元组
      Python的元组与列表类似，不同之处在于元组的元素不能修改(增删改)
      元组使用小括号(),列表使用中括号[]
      关键字:
          list 列表
          tuple 元组
      定义:
          变量名 = ()
      注意:
          1. 如果元组中只有一个元素,必须添加逗号
          2. 元组支持下标和切片
          3. index(value, start, stop)
              [start, stop)范围中,找到第一个值等于value的元素位置,找不到报错
          4. 元组支持count
          5. 元组支持(not) in关键字
          6. 元组支持循环
      与列表的转换:
          1. list(tuple) ---> 元组转列表
          2. tuple(list) ---> 列表转元组