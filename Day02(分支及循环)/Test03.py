"""
分支语句的嵌套使用：
    if 表达式：
        表达式成立执行的代码
        if 表达式1
            ...
        else:
            ...
    else:
        表达式不成立执行
"""
import random
print("先注册：")
account = input("请输入要注册用户名")
password = input("请输入要注册密码")
print("接下来登陆:")
acc = input("请输入用户名")
pwd = input("请输入密码")
if account == acc and password == pwd:
    # 生成一个四位的随机数验证码
    security_code = str(random.randint(1000,9999))
    print("你收到的验证码为:%s"%security_code)
    input_code = input("请输入验证码")
    if security_code == input_code:
        print("登陆成功")
    else:
        print("验证码有误，请等待一分钟之后重新获取")

else:
    print("用户名或者密码有误")



cmp_num = random.randint(0,2)
print("计算机准备完毕")
your_num = int(input("该你了 0:石头 1：剪刀 2：布\n"))

#练习： 使用 嵌套分支解决石头剪子布游戏
if cmp_num == 0:
    if your_num == 0:
        print("计算机出的石头，你也石头，平局")
    elif your_num == 1:
        pass
    elif your_num == 2:
        pass

elif cmp_num == 1:
    pass
elif cmp_num == 2:
    pass


