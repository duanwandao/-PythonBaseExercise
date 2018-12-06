"""
python的动态特性：
    动态添加属性：成员属性，类属性

    动态添加方法：成员方法，类方法，静态方法

"""
class Student():
    def __init__(self,name):
        self.name = name

stu1 = Student('学生1')
#动态添加属性
stu1.age = 18
#添加类属性
Student.cls_id = 210
#类属性的访问方式：1.类名.属性名  2.对象.属性名
stu2 = Student('学生2')
print(Student.cls_id)
print(stu2.cls_id)






