"""
动态添加方法：
    types.MethodType(函数,对象)
    成员方法
    类方法
    静态方法

"""
class Student():
    def __init__(self,name):
        self.name = name
stu1 = Student('学生1')
stu1.age = 18
Student.cls_id = 210

def study(self):
    print("学习使我快乐")

#如何让一个函数跟类建立关系
# stu1.study = study
#
# stu1.study()
import types
# 将函数study与对象stu1绑定，手动告诉函数参数self指的是stu1
stu1.study = types.MethodType(study,stu1)
stu1.study()


@classmethod
def testClsMethod(cls):
    print("我是类方法")
    #访问类属性
    print(cls.cls_id)

#动态添加类方法
Student.testClsMethod = testClsMethod
Student.testClsMethod()

@staticmethod
def testStaticMethod():
    print("我是静态方法")


#动态添加静态方法：
Student.testStaticMethod = testStaticMethod
Student.testStaticMethod()




