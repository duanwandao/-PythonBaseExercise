"""
函数的返回值：

def  maifan(money):
    return fan

函数 ： 求1+2+3...+n的和


定义函数练习：
    封装一个函数，函数的作用是判断一个整数是否为偶数


练习：
    1.封装函数，完成由"*"组成的自定义*个数的直线
    2.封装函数，完成 自定义行数的 类似1中完成的直线
    3.封装一个函数：功能是求任意三个整数的平均数

"""
# 求1+2..+n的和
def get_sum(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result
    # print(result)

sum1 = get_sum(1000)
print(sum1)
#
# import random
# num =  random.randint(1,6)

def is_even_number(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # result = False
    # if n % 2 == 0:
    #     result = True
    # return result

    return n % 2 == 0

print(is_even_number(3))
print(is_even_number(4))