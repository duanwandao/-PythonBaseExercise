"""
方法重写：
    1.什么叫方法重写？如何重写？
    前提： 继承关系，父类中存在某个方法，子类中将该方法重写实现一遍
    overrides
    2.重写有什么好处？
        可以为父类中方法补充新的东西
    3.什么情况下需要重写？
        父类中的方法，不能满足需求的时候，可以使用重写

    4.重写的时候注意事项：
        1.方法名
            方法名必须一致
        2.参数
            参数可以不同
        3.返回值
            与返回值无关

"""
class Animal(object):
    def __init__(self,color):
        self.color = color
    def eat(self):
        print("吃")
    def shout(self):
        print("动物都会叫")
class Dog(Animal):
    def __init__(self,name,age,color):
        # 如果使用super的话，子类中只能使用父类继承的color
        super().__init__(color)
        #父类中有一个color，子类中重写写了一个color
        # self.color = color
        self.name = name
        self.age = age
    def eat(self):
        print("吃除了吃肉还吃骨头")
    def shout(self,a,c):
        #调用父类的方法
        super().shout()
        # super(Dog, self).shout()s
        print("汪汪汪~")
        return 123

dog = Dog('Big Yellow',3,'Yellow')
dog.eat()
dog.shout(1,2)
print(dog.color)
an = Animal('Black')
print(an.color)
print(dog.color)
