"""
类的组成部分：
    属性
        类变量
        成员变量

    行为
        成员方法
            对象方法、实例方法、动态方法

        类方法
            1.装饰器
                @classmethod
            2.有一个必要参数：
                cls

        访问方式：
            1.类名.类方法名()
            2.对象名.类方法名()

        类方法中：
            在类方法中可不可以访问当前类中的属性
            在类方法中，不能使用self关键字

        好处:
            直接类名调用，不用创建对象


        静态方法
            @staticmethod
            没有参数
            类名调用


"""
class Student():
    #类变量定义类内，方法外
    class_id = 210
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #在成员方法中能否访问类方法
    def test(self):
        Student.test1()
        self.test1()
        self.__class__.test1()
        # cls.test1()

    @classmethod
    def test1(cls):
        print("我是类方法")
        print("class_id:%d"%Student.class_id)
        print("class_id:%d"%cls.class_id)
        # print("name:%s"%self.name)
        # print("age:%s"%self.name)
        Student('学生1',19).test()
    @staticmethod
    def test2():
        print("我是静态方法")


# Student.test1()
#使用对象访问类方法
stu1 = Student('学生1',18)
# stu1.__class__.test1()
stu1.test()
# Student.test2()
# stu1.test2()