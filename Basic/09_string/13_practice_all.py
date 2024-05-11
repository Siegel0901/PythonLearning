"""
模拟论坛回复:
    回复验证:
        1. 回复的内容不能为空
        2. 里面不能存在敏感词汇
        3. 最多评论20个字,剩余多少个字
        4. 回复的内容前后不能有空格
框架:
    msg = input("发表一句话:")
    print('-' * 40)
    print("以下为回复内容:")
    while True:
        # 输入用户名:
        # 输入回复内容:
        # 验证内容:
        # 成功则发出评论,否则重新输入
        pass
"""
msg = input("发表一句话:")
print('-' * 40)
print("以下为回复内容:")
while True:
    # 输入用户名:
    username = input("请输入用户名:")
    while True:
        # 输入回复内容:
        comment = input("请输入回复内容:")
        comment = comment.strip()
        # 验证内容:
        if len(comment) != 0:
            # 验证长度是否超过20个字
            if len(comment) <= 20:
                # 去除敏感词汇
                comment = comment.replace('---', "****")
                print("{}:".format(username))
                print(comment.center(30))
                break
            else:
                print("长度不能超过20个字!")
        else:
            print("回复不能为空!")
