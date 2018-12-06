"""
设计模式：
    单例模式：
        全局对象唯一

    __new__()
        作用： 分配内存空间

    __init__()
        作用： 初始化

    初始化唯一性

"""
class Data():
    #定义一个私有的类属性
    __single = None
    def __new__(cls, *args, **kwargs):
        print("new方法")
        if cls.__single == None:
            cls.__single =  super().__new__(cls)
        return cls.__single
    def __init__(self):
        # self.data = list()
        print("init方法")
        self.students = []

# def saveData(stu):
#     data = Data()
#     data.students.append(stu)
# def showData():
#     data = Data()
#     print("qqq")
#     for stu in data.students:
#         print(stu)

data1 = Data()
data2 = Data()
data3 = Data()
#id(对象)
print(id(data1))
print(id(data2))
print(id(data3))