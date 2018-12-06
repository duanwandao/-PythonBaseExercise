"""
property：简化私有属性的访问方式

"""
class Student():
    def __init__(self,name,age):
        self.name = name
        self.setAge(age)
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            raise TypeError('年龄必须是int类型')

    age = property(getAge,setAge)

stu = Student('aaa',10)
# stu.setAge(20)
stu.age = 20
# print(stu.getAge())
print(stu.age)
