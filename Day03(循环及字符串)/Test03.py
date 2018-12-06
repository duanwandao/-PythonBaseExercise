"""
打印倒的99乘法表

1*9 = 9 2*9 = 18


循环控制：
    break:
        结束当前循环
    continue
        跳过本次循环中的后续代码

"""
# for i in range(1, 10).__reversed__():
#     # 内循环
#     for j in range(1, i + 1):
#         print("%d * %d = %d" % (j, i, i * j), end="\t")
#     print()

# for i in range(9,0,-1):
#     #内循环打印每一行中的数据
#     for j in range(1,i+1):
#         print("%d * %d = %d"%(j,i,i*j),end="\t")
#     print()

# for j in range(3):
#     print("我是外循环%d"%j)
#     for i in range(10):
#         print(i)
#         if i == 5:
#             # 结束（当前）循环
#             break

for i in range(10):
    if i == 5:
        # 跳过后续代码
        continue
    print(i)
    print(i)
