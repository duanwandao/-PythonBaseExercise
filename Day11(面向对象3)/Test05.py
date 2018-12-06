"""
继承：
class Dog(Animal):
    pass


继承语法：
    class  子类(父类1，父类2....):
        pass
多继承：
    一个子类可以同时存在多个父类

    狼狗    狗 狼

    骡子    马 驴

    多继承的前提：方法有什么变化

    如果C（A，B）
        意味C类可以共享A类以及B类中所有的非私有方法
        如果A类与B类中存在同名方法，子类继承的方法取决于父类的顺序(取前边的)

"""

class B():
    def testA(self):
        print("我是B类中的testA方法")
    def testB(self):
        print("我是B中的testB方法")
class A():
    def testA(self):
        print("我是A中的testA方法")
class C(B,A):
    def testA(self):
        print("我是C中testA方法")
    def __testC(self):
        print("我是C中私有的testC方法")
class D(C):
    pass

# c = C()
# c.testA()
# c.testB()
d = D()
d.testA()
#打印方法调用时的查找顺序
print(D.mro())
#子类对象无法调用父类中的私有方法
# d.__testC()

