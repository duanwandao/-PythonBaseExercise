"""
练习：
    打印99乘法表

1 * 1 = 1
1 * 2 = 2   2 * 2 = 4
....

while 循环


for循环
语法：
    for 变量 in range(start,end,step)
        print(变量)

    不包括end

需求：打印从1-9的数字


"""
# i = 1
# while i <= 9:
#     #内循环的内容
#     j = 1
#     while j <= i:
#         print("%d * %d = %d"%(j,i,i*j),end="\t")
#         j += 1
#     print()
#     i += 1
# i = 1
# while i <= 9:
#     print(i)
#     i += 1
# for i in range(1,10):
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(0,10,1):
#     print(i)
# for i in range(1,10,2):
#     print(i)

# 倒序打印9 -> 1
# for i in range(9,0,-1):
#     print(i)

# 使用for循环打印99乘法表

for i in range(1, 10):
    # 内循环
    for j in range(1, i + 1):
        print("%d * %d = %d" % (j, i, i * j), end="\t")
    print()
