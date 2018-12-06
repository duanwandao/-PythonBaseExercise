"""
面向对象三大特征：
    封装
    继承
    多态

多态(鸭子类型)：
    不是判断对象本身是什么类型，而是根据对象具备某个能力，就认为是什么类型



"""
class F1(object):
    def show(self):
        print("F1.show")
class S1(F1):
    def show(self):
        print("S1.show")
class S2(S1):
    def show(self):
        print("S2.show")

def func(obj):
    #obj有前提条件， 判断某个对象属于某个类
    # isinstance(对象，类)
    # if isinstance(obj,S2) or isinstance(obj,S1) or isinstance(obj,F1):
    #     obj.show()
    # else:
    #     print("%s 不能响应show方法"%obj)
    # issubclass: 判断某个类是否为另外一个类的子类（包含本身）
    # obj.__class__ ：获取对象obj所属的类
    if issubclass(obj.__class__,F1):
        obj.show()
    else:
        print("%s 不能响应show方法" % obj)
f1 = F1()
s1 = S1()
s2 = S2()

func(f1)
func(s1)
func(s2)

func('123')

