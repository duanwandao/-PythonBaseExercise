"""
初始化方法中设置属性的其他方法：

def __init__(self,name,age,gender,id,score)
    self.name = name
    ...

"""
class Student(object):
    def __init__(self,name,age,gender,id,score,address,tel,height,weight):
        # self.name = name
        # pass
        dic = locals()
        # print(type(dic))
        # print(dic)
        # dic.pop('self')
        # print(dic)
        for k,v in dic.items():
            #设置属性的函数
            setattr(self,k,v)

    def showInfo(self):
        print("name:%s age:%d 性别:%s"%(self.name,self.age,self.gender))

stu = Student('学生1',18,'男','1001',89,'北京天安门','15888888888',130,130)

stu.showInfo()

