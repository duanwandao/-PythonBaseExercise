"""
比较运算符：
    >
    <
    >=
    <=
    ==
    !=
    比较结果：
        bool值
            True        /Yes            非0
            False       /No             0



逻辑运算符
    and
    or
    not

输入用户名跟密码，输入都正确之后，给出登陆成功提示


"""
# result = 10 > 9
# print(result)
# print(type(result))
#
# import random
# #得到[1,6]范围内的随机数，包括1，6
# rand_num = random.randint(1,6)
# print(rand_num)
# if 1 <= rand_num <= 3:
#     print("小")
# if 6 >= rand_num >= 4:
#     print("大")


acc = '15888888888'
pwd = 'Abc1234569'

account = input("请输入用户名\n")
password = input("请输入密码")

if(account == acc and password == pwd):
    print("登陆成功")

if(account != acc or password != pwd):
    print("用户名或者密码错误")
