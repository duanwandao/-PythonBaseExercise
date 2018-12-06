"""
builtins

内建属性

__name__:
__doc__:


内建函数

"""
class Student():
    """
    文档注释：Student(name,age) -> new Student with name,age
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        if item == 'age':
            return '100'
        if item == 'name':
            return '***'
#
# list1 = []
# print(list1.__doc__)
# stu = Student('学生1',18)
# print(stu.__doc__)

stu = Student('李闹',19)
print(stu.name)
print(stu.age)