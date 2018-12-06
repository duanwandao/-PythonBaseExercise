"""
内存管理机制：
    1、小整数池
        [-5,256]

    2、大整数池

    3、字符串
        intern
        相同的字符串（不包含空格，或者特殊字符），默认只保留一份
        id() 查地址
        is   判断两个对象是否为同一个

Python中的内部管理机制：
    gc机制：
        garbage collection（垃圾回收）
        1.引用计数机制
            获取引用计数
                sys.getrefcount()

            增加引用计数
                将对象计入到列表
                将对象赋值给新的对象
                将对象作为形参

            减少引用计数
                从列表中移除
                del 对象



        2.隔代回收机制

"""
import gc,sys

class AAA(object):
    """
    我是介绍
    """
    def __init__(self):
        print("object: born at:%s" % hex(id(self)))
        self.aaa = 1

    def __new__(cls, *args, **kwargs):
        print("new")
        return super(AAA, cls).__new__(cls)
    def __del__(self):
        print("bye bye")

a = AAA()
print(sys.getrefcount(a))
list1 = []
list1.append(a)
print(sys.getrefcount(a))
list1.remove(a)
print(sys.getrefcount(a))
# del a
print("-"*50)
print(gc.get_threshold())
gc.collect()
print(gc.get_count())

from functools import reduce
v = reduce(lambda x,y:x+y,[1,2,3,4])
print(v)
v = reduce(lambda x,y:x+y,['1','2','3','4'],'5')
print(v)