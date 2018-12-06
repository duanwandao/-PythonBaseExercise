"""
函数：
    单独的一个功能，经常使用，将实现该功能的代码放在一起，起个别名

语法：
    函数的定义：
        def 自定义的函数名():
            实现功能的代码...

    函数的调用：
        函数名()
        #调用print函数
        print()

    函数一定是先定义，后调用

    系统函数/自定义函数



好处：
    更好管理，提高代码复用率，封装性更好
"""

# 封装一个实现打印99乘法表的函数
def print99():
    # print(a)
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d * %d = %d\t' % (j, i, j * i), end='')

        print()

#实现打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d * %d = %d\t'%(j,i,j*i),end='')
#
#     print()

#调用函数
print(10)
print99()
print("HellWorld")
print99()


