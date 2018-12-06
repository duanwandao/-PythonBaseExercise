"""
创建对象，拥有默认属性：
__init__()方法的使用

"""
class Driver():
    #增加一个方法
    def __init__(self,id,name):
        print("我是init方法")
        # 给自己加属性
        self.id = id
        self.name = name

    def drive_car(self):
        print("工号：%d %s为您服务"%(self.id,self.name))
        print("1、踩离合")
        print("2、打火")
        print("3、挂档")
        print("4、松离合给油")
        print("滴滴滴，一起去嗨皮")
# 创建对象
driver1 = Driver(1001,'黄师傅')
# 2.让对象开车走  调用对象的方法
driver1.drive_car()

driver2 = Driver(1002,'于师傅')
driver2.drive_car()

