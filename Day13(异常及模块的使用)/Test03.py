"""
自定义异常：
    自己创建异常类,继承Exception
    抛出异常 raise  异常对象
"""
PI = 3.14
class GenderError(Exception):
    class_id = 210
    def __init__(self):
        self.errMsg = '性别异常，只能设置为男或者女'

class Student():
    def __init__(self,name,gender):
        self.name = name
        # self.__gender = gender
        self.setGender(gender)

    def setGender(self,gender):
        if gender == '男' or gender  == '女':
            self.__gender = gender
        else:
            #抛出异常
            raise GenderError()
    def getGender(self):
        return self.__gender

def showInfo(stu):
    print(stu)

stu1 = Student('刘忙','男')
try:
    stu1.setGender('未知')
except Exception as e:
    print(type(e))
    print(e.args)
    print(e.errMsg)
