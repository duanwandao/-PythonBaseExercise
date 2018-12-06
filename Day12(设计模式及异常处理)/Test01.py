"""
类的组成部分：
    属性
        类属性：
            类变量

        对象属性：
            成员变量

    行为:
        成员方法

        类方法

        静态方法

    1.什么叫类变量：
        变量定义在类中，方法外，属于类所有，所有对象共享一份

    2.与成员变量有什么区别？
        定义位置不同
        属于者不同
            成员变量属于对象
            类变量属于类
        存储份数不同：
            成员变量：
                每个对象中都有一份
            类变量：
                只有一份，供所有对象共享

    为什么要使用类变量？
        存储份数唯一

    什么情况下使用类变量？


    如何使用类变量？
    类变量的访问：
        1.获取值
            a.类名.类属性名
            b.对象名.类属性名
        2.设置值
            类名.类属性名 = 对应值
            对象名.类属性名 = 对应值

        如果存在与类属性名相同的对象属性，
        用对象名.属性名 优先访问 对象的

"""
class Student():
    #类变量定义类内，方法外
    class_id = 210
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.class_id = 100
stu1 = Student('马哥',38)
stu2 = Student('大龙哥',66)

print("%s所在教室:%d"%(stu1.name,stu1.class_id))
print("%s所在教室:%d"%(stu1.name,Student.class_id))
#将教室id更改为211
Student.class_id = 211
#这种方式等于是给对象stu1中增加一个成员变量class_id
# stu1.class_id = 211
print("更改教室后:")
print("%s所在教室:%d"%(stu1.name,Student.class_id))
print("%s所在教室:%d"%(stu1.name,stu2.class_id))


