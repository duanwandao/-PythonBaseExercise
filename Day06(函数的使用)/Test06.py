"""
    1.封装函数，完成由"*"组成的自定义*个数的直线

    2.封装函数，完成 自定义行数的 类似1中完成的直线

    3.封装一个函数：功能是求任意三个整数的平均数


    局部变量：
        定义在函数内，函数内部有效
        形式参数也是局部变量

    全局变量
        定义在函数外，所有函数中有效

        变量一定先定义，后使用

    如果在函数中，修改全局变量的值：
        1.如果全局变量是基本类型(int,float,bool),修改之前需要使用global声明
        2.如果全局变量是引用类型，可以直接修改，不用声明
        3.如果在函数中有与全局变量同名的局部变量时，优先访问的为局部变量

"""

# 打印n个*组成的直线
def print_line(n):
    print("*" * n)
    # for i in range(n):
    #     print("*",end='')
# print(print_line(10))
#调用打印直线的函数
# print_line(10)

# line表示打印的行数  count 每一行中*的个数
def print_more_line(line, count):
    for i in range(line):
        # 调用打印直线的函数
        print_line(count)

#调用打印多行的函数
# print_more_line(3,5)

def get_avg(a,b,c):
    return (a+b+c)/3

# print(get_avg(10,20,30))

#全局变量
c = 100

list1 = [1,2,3]

def test1():
    a = 10
    print('a = %d'%a)
    #声明以下，我要修改的c，就是全局变量
    global c
    #修改全局变量的值
    c += 100
    print('c = %d'%c)


def test2():
    # print('a = %d'%a)
    c = 1000
    print('c = %d'%c)
    # print(b)
    list1[0] = 100

test1()
test2()
