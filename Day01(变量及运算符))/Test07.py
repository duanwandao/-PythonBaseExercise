"""
if 语句

if 表达式:
    表达式成立执行的代码

1-6

    模拟实现骰子大小
    1.随机数

    2.if 判断
    1-3  输出小

    4-6  输出大

"""
import random
#得到[1,6]范围内的随机数，包括1，6
rand_num = random.randint(1,6)
print(rand_num)
if rand_num <= 3:
    print("小")
if rand_num >= 4:
    print("大")