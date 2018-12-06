"""
封装动物类、猫类、狗类

面向对象：

    1、封装(类的封装)

    2、继承(父类 子类)
        父类(超类，根类，基类)
        子类(派生类)

        继承的特性：
            子类可以继承父类中所有的非私有的属性及方法
         继承的语法：
            class 类(父类):
                pass


    3、多态（鸭子类型）


"""
class Animal():
    def __init__(self,color,age,name,breed,gender):
        self.color = color
        self.age = age
        self.name = name
        self.breed = breed
        self.gender = gender
    def eat(self):
        print("吃")
    def sleep(self):
        print("睡")
class Cat():
    def __init__(self,color,age,name,breed,gender):
        self.color = color
        self.age = age
        self.name = name
        self.breed = breed
        self.gender = gender
    def eat(self):
        print("吃")
    def sleep(self):
        print("睡")
class Dog():
    def __init__(self,color,age,name,breed,gender):
        self.color = color
        self.age = age
        self.name = name
        self.breed = breed
        self.gender = gender
    def eat(self):
        print("吃")
    def sleep(self):
        print("睡")
