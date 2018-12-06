"""
属性私有化的问题：

xx
    普通的变量
_x
    使用from 模块 import *  无法导入

__x
    私有属性，方法
    名字重整：
        __age
        _类名__age

__xx__:
    魔法方法
    自定义的方法避免使用这种形式

x_:
    避免变量名字冲突



"""
# import Test01
from Test01 import *


class Student():
    def __init__(self,name,age):
        self.name = name
        #私有属性：外部不能访问
        self.__age = age


# print(Test01.PI)
# print(Test01._num)

print(PI)
# print(_num)
# _test()

stu =Student('学生1',18)
# print(stu.__age)
print(dir(stu))
#名字重整
# stu._Student__age = 100
# print(stu._Student__age)


