"""
装饰器
"""
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            raise TypeError('年龄必须是int类型')

stu = Student('学生1',10)
#设置年龄
stu.age = 20
print(stu.age)

list1 = [x for x in range(100) if x % 2 == 0]
print(list1)


