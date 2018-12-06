"""
用法：

    求原点到指定点的距离
    sqrt((x-x1)^2  + (y-y1)^2)

    1.函数
    2.闭包

"""

import math
#求两个点之间的距离
def get_dis(x,y,x1,y1):
    return math.sqrt((x-x1)**2 + ((y-y1)**2))

print(get_dis(0,0,10,10))
print(get_dis(0,0,100,100))


def get_dis_out(x,y):
    def get_dis_in(x1,y1):
        return math.sqrt((x - x1) ** 2 + ((y - y1) ** 2))
    return get_dis_in

#使用变量get_dis_in 存储get_dis_out(0,0) 的返回值(返回值为一个函数名)
get_dis_in = get_dis_out(0,0)
#
print(get_dis_in(10,10))
print(get_dis_in(100,100))