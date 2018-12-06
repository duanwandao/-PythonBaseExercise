"""
求1-100中所有偶数的和
    1 2 3 4...100

    判断某个数字是否为偶数(能被2整除，i%2 == 0)

    猜数字的游戏：
        1.随机生成一个数字[1,100]
            random
        while
        2.输入猜测
            input
            if - elif - else
            猜大了，再小点
            猜小了，再大点
            猜中了

            统计猜的次数：
                根据次数评级：
                    if - elif - else
                    1-3  超神
                    4-6  菜鸟
                    7+   脑子是个好东西



"""
# i = 1
# #记录所有偶数的和
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print("1-100中所有偶数的和为:%d"%sum)
#
# j = 0
# sum1 = 0
# while j <= 100:
#     sum1 += j
#     j += 2
# print("1-100中所有偶数的和为:%d"%sum1)

import random
rand_num = random.randint(1,100)
# 用来控制循环是否结束
End = True
# 用来记录猜测的次数
count = 0
while End:
    num = int(input("请猜测:"))
    #猜测次数+1
    count += 1
    if num > rand_num:
        print("猜大了，再小点")
    elif num == rand_num:
        print("猜中了")
        #1.结束循环
        End = False
        #2.根据猜测次数，进行评级
        if 1 <= count <= 3:
            print("超神，你很牛啊兄弟")
        elif 4 <= count <= 6:
            print("菜菜菜~")
        else:
            print("脑子是个好东西~")
    else:
        print("猜小了，再大点")

