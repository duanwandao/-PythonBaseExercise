"""
def 函数名(参数...):
    代码...

    形参：
        出现在函数的定义中，定义时没有具体值
    实参：
        出现在函数的调用中

    调用的时候，实际参数的值赋值给形式参数


"""
# def print99():
#     # print(a)
#     for i in range(1, 6):
#         for j in range(1, i + 1):
#             print('%d * %d = %d\t' % (j, i, j * i), end='')
#         print()
# def print98():
#     # print(a)
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print('%d * %d = %d\t' % (j, i, j * i), end='')
#         print()

#定义的时候，line 叫做形式参数
def print99(line):
    for i in range(1, line):
        for j in range(1, i + 1):
            print('%d * %d = %d\t' % (j, i, j * i), end='')
        print()

#调用的时候，给出实际参数
print99(10)
print99(6)
print99(13)