"""

多继承中属性的处理：



"""
class A():
    def __init__(self,a,aa):
        self.a = a
        self.aa = aa
class B():
    def __init__(self,b):
        self.b = b
class C(A,B):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
#
# c = C(1,2)
# print(c.a)
# print(c.aa)
# print(c.b)
c = C(1,2,3)
# print(c.a)
print(c.a)
print(c.aa)
print(c.c)

print(C.mro())
print(C.__mro__)