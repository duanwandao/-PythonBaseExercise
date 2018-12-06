"""
类的封装：


"""
class Driver():
    def drive_car(self):
        print("工号：%d 为您服务"%self.id)
        print("1、踩离合")
        print("2、打火")
        print("3、挂档")
        print("4、松离合给油")
        print("滴滴滴，一起去嗨皮")
# 创建对象
driver1 = Driver()
#手动添加属性
driver1.id = 1001
#修改属性值
# driver1.id = 1002

# 2.让对象开车走  调用对象的方法
driver1.drive_car()

