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
    __firstInit = False
    def __new__(cls, *args, **kwargs):
        print("new方法")
        if cls.__single == None:
            cls.__single =  super().__new__(cls)
        return cls.__single
    def __init__(self):
        if Data.__firstInit == False:
            # self.data = list()
            print("init方法")
            self.students = []
            Data.__firstInit = True

def saveData(stu):
    #创建一个对象(对象的唯一性能够保证该对象多次创建都是同一个对象)
    data = Data()
    data.students.append(stu)
def showData():
    #创建一个对象
    data = Data()
    print("qqq")
    for stu in data.students:
        print(stu)

saveData('学生1')
saveData('学生2')
saveData('学生3')
showData()