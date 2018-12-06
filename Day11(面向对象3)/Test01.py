"""
使用面向对象（学生管理系统v3.0）
    学生类
    管理系统类


魔法方法：
    不手动调用，会自动执行的方法magic method

    特点：双下划线开头，双下划线结尾

"""
students_list = []

class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    #手动实现__str__()方法
    def __str__(self):
        return 'name:%s score:%d' % (self.name, self.score)


class SystemManger():
    def __init__(self,version,name,author):
        self.version = version
        self.name = name
        self.author = author
    def showMenu(self):
        print("欢迎光临%s %s"%(self.name,self.version))
        print("1.添加学生")
        print("2.展示学生")
        print("3.退出系统")

    def addStudent(self,stu):
        students_list.append(stu)
    def showAllStudents(self):
        #<__main__.Student object at 0x0000000002258EF0>
        #<__main__.Student object at 0x0000000002258F28>
        for stu in students_list:
            print(stu)
            # name: xxx score: xxx
            # print(stu.__str__())
    def systemExit(self):
        print("谢谢使用")
        exit()
manger = SystemManger('v3.0','学生管理系统','大卫')
while True:
    manger.showMenu()
    choice = input("请选择1-3:")
    if choice == '1':
        name = input("请输入姓名")
        score = int(input("请输入分数"))
        #创建学生对象
        stu = Student(name,score)
        #调用添加学生的方法
        manger.addStudent(stu)
    elif choice == '2':
        manger.showAllStudents()
    elif choice == '3':
        manger.systemExit()
    else:
        print("选项有误，重新输入")