"""
面向对象:
    核心： 类
创建类的语法：

找代驾开车

class 类名():
    #属性

    # 行为，能力，动态特征，方法
    def 方法名(self,其他参数...):
        pass

    创建对象语法：
        变量名 = 类名()

    调用对象方法的语法：
        对象名.方法名()

"""

class Driver():
    def drive_car(self):
        print("1、踩离合")
        print("2、打火")
        print("3、挂档")
        print("4、松离合给油")
        print("滴滴滴，一起去嗨皮")

# class Girl():
#     pass
# class Car():
#     pass
# class Plane():
#     pass
# 面向过程
# print("1、踩离合")
# print("2、打火")
# print("3、挂档")
# print("4、松离合给油")
# print("滴滴滴，一起去嗨皮")

# 面向对象
# 1.找到一个对象（创建对象）
# list1 = [1,2,3]
#创建一个对象，将对象存储到driver1中
driver1 = Driver()

# 2.让对象开车走  调用对象的方法
driver1.drive_car()

