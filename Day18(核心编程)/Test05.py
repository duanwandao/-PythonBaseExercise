"""
生成器：
    在Python中， 一边循环一边计算的机制， 称为生成器： generator
创建生成器: G = ( x*2 for x in range(5))
可以通过 next(生成器) 函数获得生成器的下一个返回值
没有更多的元素时， 抛出 StopIteration 的异常
生成器也可以使for 循环，因为生成器也是可迭代对象

创建生成器的方式：
    1.
        列表推导式
        g = (列表推导式)
    2.
        yield


迭代器
闭包
装饰器
"""
# list1 = [2,4,6,8...10]
list1 = []
#循环操作
for i in range(2,101,2):
    list1.append(i)
print(list1)
#列表推导式
list2 = [x for x in range(2,101,2)]
list3 = [x for x in range(101) if x % 2 == 0 if x != 0 if x >=50]
print(list2)
print(list3)
g = (x for x in range(101) if x % 2 == 0 if x != 0 if x >=50)
print(type(g))
# print(g)
print(next(g))
print(next(g))
print('-'*50)
#使用for循环遍历生成器能生成的所有的数据
for v in g:
    print(v)
print('-'*50)
#超出生成器生成的范围“StopIteration”异常
# print(next(g))
# print(g.__next__())
