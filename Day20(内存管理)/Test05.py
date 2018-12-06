"""
内建函数
range(start,end,step)

    不包括终点
    step默认为1

map(function,iterable)

将iterable中的每个元素分别作为function的参数进行处理，得到一个迭代器


"""
# for x in range(10):
# for x in range(0,10,2):
#     print(x)
#倒着取，注意开始以及结束
# for x in range(10,0,-2):
#     print(x)

from collections import Iterator
list1 = [1,2,3,4,5]

# def func_1(x):
#     return  x * 2
#
# result = map(func_1,list1)
# if isinstance(result,Iterator):
#     print("是")
#
# for x in result:
#     print(x)


#使用匿名函数完成将列表中所有元素扩大二倍的操作
result1 = map(lambda x:x*2,list1)
for x in result1:
    print(x)
