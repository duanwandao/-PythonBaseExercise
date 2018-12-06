"""
循环：
    分支：
        分支:


嵌套循环：
外循环：
    内循环：

while 条件：
    while 条件：
        内循环的代码

外循环执行一次，内循环要执行一遍
"""
# i = 0
# while i < 3:
#     print("我是外循环%d"%i)
#     j = 0
#     while j < 2:
#         print("我是内循环%d"%j)
#         j += 1
#     i += 1

#  打印 *****
# print("*****")
# print("*"*5)
"""
*****
*****
*****
"""

j = 0
while j < 3:
    i = 0
    while i < 5:
        print("*", end="")
        i += 1
    print()
    j += 1