"""
使用继承关系完成Animal、Cat、Dog三个类

"""
class Animal(object):
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
class Cat(Animal):
    pass
class Dog(Animal):
    pass
    def __str__(self):
        return "就不告诉你"

#创建cat对象，验证是否可以继承到父类中的属性以及方法
small_hua_cat = Cat('green',1,'绿巨人','波斯','雌')
print("年龄:%d"%small_hua_cat.age)
small_hua_cat.sleep()
small_hua_cat.eat()
small_hua_dog = Dog('Black',2,'大黄','京巴','雄')
print(small_hua_dog.age)
small_hua_dog.sleep()
small_hua_dog.eat()

print(small_hua_dog)
# print(small_hua_dog.__str__())
# print(small_hua_cat.__str__())
small_hua_cat.showInfo()

