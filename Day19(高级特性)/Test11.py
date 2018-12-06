"""
type

    类也是对象，元类type的对象

1.判断一个变量所属的类
2.元类
    动态创建类
    类 = type('名字',(父类...),{属性，方法})

"""
class Person():
    def __init__(self,name):
        self.name = name
    def showName(self):
        print(self.name)
# print(1)
# print('Hello')
# print([1,2,3])
# print(type(Person))

def study(self):
    print("学习使我快乐")
    print(self.age)
age = 10
Student = type('Student',(Person,),{'age':age,'study':study})
stu = Student("学生2")
print(stu.age)
#查看对象中所有的方法跟属性
print(dir(stu))
stu.study()

#是否可以访问父类的属性
# stu.name = '学生1'

#是否可以访问父类的方法
stu.showName()

print(Student.__name__)
