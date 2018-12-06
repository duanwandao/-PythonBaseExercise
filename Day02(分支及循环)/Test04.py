"""
分支：
    单分支
    if 表达式：
        表达式成立执行的代码...

    双分支
    多分支
    分支的嵌套

循环：
    while

    语法：
    while 表达式：
        表达式成立执行的代码...
        迭代(趋向终止)

    for

"""
# 将HelloWorld输出10遍
# print('HelloWorld\n'*10)
# i = 0
# while i < 10:
#     print("HelloWorld i = %d"%i)
#     i = i + 1

# i = 1
# while i <= 100:
#     print('i = %d'%i)
#     # i = i+1
#     i += 1

# 求 1 + 2 + 3 + .....+ 100的和
# sum = 0  sum += 1  sum += 2 sum += 3...sum += 100


# j = 1
# # 用来记录总和
# sum = 0
# while j <= 101:
#     sum += j
#     j += 1
# print("和为：%d"%sum)
import random
i = 0
while i < 10:
    cmp_num = random.randint(0, 2)
    print("计算机准备完毕")
    your_num = int(input("该你了 0:石头 1：剪刀 2：布\n"))
    if (your_num == 0 and cmp_num == 1) or (your_num == 1 and cmp_num == 2) or (your_num == 2 and cmp_num == 0):
        print("你赢了")
    elif your_num == cmp_num:
        print("平局")
    else:
        print("你输了")

    i += 1



