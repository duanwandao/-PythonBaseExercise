"""
匿名函数
    关键字
    lambda
    lambda 参数...: 表达式


    注意：
        1.匿名函数中可以存在0，1，多个参数
        2.匿名函数中不能存在return语句
        3.匿名函数运算完之后，只能得到一个值(返回值)
    思考：
        一般函数可以存在几个返回值？
            一个还是多个？

    返回值可以存在1个或者多个
        如果函数返回多个值，接受的方式有两种：1. 只有一个接受  2.个数匹配


"""


def get_sum(a,b):
    return a + b

# test = lambda :print("哈哈哈")
#匿名函数中不能存在return关键字
# test = lambda :return 1
#
# get_sum1 = lambda a,b:a + b
# print(type(get_sum1))
# print(get_sum1)
#
# print(get_sum(10,20))
# print(get_sum1(10,20))
# # test()

#测试多个返回值的问题
# def testReturnValue():
#     return 1,2
#
# result =  testReturnValue()
# print(type(result))
# print(result)


# v1,v2 = testReturnValue()
# print(type(v1))
# print(type(v2))
# print(v1,v2)

def testReturnValue1():
    return 1,2,3
a,b,c = testReturnValue1()
print(type(a))
print(type(b))
print(a)
print(b)

print(lambda x,y:x**y)
print(get_sum)
str