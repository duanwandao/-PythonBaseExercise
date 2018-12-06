"""
 1.双分支
    if-else

    if 条件表达式:
        条件成立执行的代码
        ...
    else:
        条件不成立执行的代码
        ....
 2.多分支(多选一，如果前边的条件成立，后续条件不在判断)
    if - elif - else
    if 条件表达式:
        条件成立执行的代码
        ...
    elif 条件表达式1：
        条件表达式1成立执行的代码...

    else:
        以上两个条件都不成立，执行的代码
 3.分支的嵌套
    if 用户名密码都正确:
        if 验证码是否正确:
            登陆成功
        else:
            验证码有误
    else:
        用户名/密码有误
 4. while循环
    while 条件表达式：
        循环体
        循环趋向终止(迭代)
 5. 嵌套循环
    外循环
        内循环
    外循环执行一次，内循环执行一遍

    ****
    ****
    ****

    外循环控制行数，内循环控制每一行的列数

*
**
***
****
*****

*
***
*****
*******

*
****
*******
**********


"""
# if True:
#     print("True1")
# elif True:
#     print("True2")
# else:
#     print("True3")

# i = 10
# while i > 0:
#     print(i,end="\t")
#     i -= 1

# j  = 0
# while j < 3:
#     i = 0
#     while i < 4:
#         print("*", end="")
#         i += 1
#     print()
#     j += 1

# 打印直角三角形
# i  = 0
# line = 100
# while i < line:
#     #内循环负责打印每一行中*的个数
#     j = 0
#     while j <= i:
#         print("*",end="")
#         j += 1
#     print()
#     i += 1


i  = 0
line = 4
while i < line:
    #内循环负责打印每一行中*的个数
    j = 0
    while j < 2*i+1:
        print("*",end="")
        j += 1
    print()
    i += 1


