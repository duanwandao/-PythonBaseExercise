"""
面向对象的知识：
    类的封装：
        属性(成员变量)
        行为(成员方法)

    语法：
        class 类名():
            def __init__(self,属性...):
                self.属性1 = 属性1

    创建对象：
        a = 类名(参数个数取决于init方法中参数的个数)

    访问属性：
        print(a.属性名)
        a.属性名 = 值

    访问方法：
        a.方法名(参数)

    完成学生类的封装：
        属性有，姓名，年龄，性别
        方法有，学习，游戏，睡觉，吃饭，自我介绍


    私有属性：
        只能内部访问，外部无法访问的属性

    语法：  __属性名

    如果某个属性定义成了私有的：
        为属性提供对应的两个方法：
            getAge(self)：
                return self.__age
            setAge(self,age)：
                if ：
                    self.__age = age

"""
class Student():
    def __init__(self,name,age,gender):
        self.name = name
        self.setAge(age)
        # self.__age = age
        self.gender = gender

    #对私有属性提供设置值以及获取值的方法
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("年龄设置范围不合理，默认为0")
            self.__age = 0
    def study(self):
        print("学习使我快乐，一天不写代码会死")
    def playGame(self):
        print("玩把游戏，嗨皮一下")
    def sleep(self):
        print("闭上眼睛就睡觉,感觉在打雷")
    def eat(self):
        print("吃饭使我快乐")
    def introduce(self):
        print("我叫:%s 性别：%s 年龄:%d"%(self.name,self.gender,self.__age))
#创建对象
stu1 = Student("胡了",1800,'男')
#获取属性值
# print(stu1.name)
# #设置值
# stu1.name = '宋行'
# print(stu1.name)
# stu1.introduce()
# stu1.age = 1000
# # stu1.age = -10
# stu1.introduce()
#私有属性无法在外部访问
# print(stu1.__age)
# stu1.setAge(30)
# print(stu1.getAge())
stu1.introduce()
