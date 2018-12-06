"""
多分支语句：
    多分支：
        if 表达式1：
            表达式1成立执行的代码
        elif 表达式2:
            表达式2成立执行的代码
        elif 表达式3:
            表达式3成立执行的代码
        else:
            三个条件都不满足执行的代码

        A[90,100]
        B[80,90)
        C[70,80)
        D[60,69]
        E < 60


跟电脑猜石头剪子布，打印输赢

1.计算机随机生成：0.石头 1.剪刀 2.布
    random.randint
2.该你出了：0.石头 1.剪刀 2.布
    input()
3.比较输赢
    if - elif - else
    1.赢了
    2.平局
    3.输了

"""
import random
# score = int(input("请输入你要查询的分数"))
# if score >= 90 and score <= 100:
#     print("A")
# elif score >= 80 and score < 90:
#     print("B")
# elif score >= 70 and score < 80:
#     print("C")
# elif score >= 60 and score < 70:
#     print("D")
# else:
#     print("E")
# num = 生成一个随机数区间位于[0,2]
# your_num = input("")
# if 你出了石头电脑出了剪刀 or  你出了剪刀电脑出了布 or 你出了布电脑出了石头:
#     print("你赢了")
# elif 你出的跟电脑出的一样：
#     print("平局")
# else:
#     print("你输了")
#计算机随机生成的.
cmp_num = random.randint(0,2)
print("计算机准备完毕")
your_num = int(input("该你了 0:石头 1：剪刀 2：布\n"))
if (your_num == 0 and cmp_num == 1) or (your_num == 1 and cmp_num == 2) or (your_num == 2 and cmp_num == 0):
    print("你赢了")
elif your_num == cmp_num:
    print("平局")
else:
    print("你输了")

