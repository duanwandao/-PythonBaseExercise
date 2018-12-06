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
import gc,sys,time

class AAA(object):
    def __init__(self):
        print("object: born at:%s" % hex(id(self)))

    def __new__(cls, *args, **kwargs):
        print("new")
        return super(AAA, cls).__new__(cls)
    def __del__(self):
        print("bye bye")
def start():
    while True:
        a = AAA()
        b = AAA()
        #给a添加成员变量
        a.v = b
        #给b添加成员变量
        b.v = a
        #无法删除  只是减少引用计数
        del a
        del b
        print(gc.get_count())
        print(gc.get_threshold())
        time.sleep(0.01)


# 手动调用垃圾回收器回收一次
# gc.collect()
# 设置隔代回收阈值
# gc.set_threshold(100,5,5)
#手动关闭垃圾回收机制(开发过程禁用)  python3 默认开启
# gc.disable()
start()