"""
考核点	：函数+文件处理+学生管理系统
考核内容	：
	学生管理系统：
		1、添加学生功能(20)
		2、删除学生功能(20)
		3、查看所有学生功能(15)
		4、退出系统功能(10)
	数据结构：
	students = ['学生名1','学生名2'...]
	实现数据持久化：
	第一次操作完退出系统，下次进来的时候，
上次操作完的数据依旧存在（退出前，先保存数据，
登陆时，先加载上次保存的数据<如果文件存在再加
载>）(20)
（注意不同功能尽量使用函数封装）(15)

"""
import os
#存储所有学生
students = []
#控制循环结束的变量
end = False
#存储数据的文件名字
fileName = 'student.txt'
#展示主菜单
def showMenu():
    print("1.添加学生")
    print("2.删除学生")
    print("3.展示所有")
    print("4.退出系统")
#添加学生
def addStudent(stu):
    students.append(stu)
#判断是否包含学生
def hasStu(stu):
    return stu in students
#删除学生
def delStu(stu):
    if hasStu(stu):
        students.remove(stu)
#展示所有学生
def showAllStudent():
    print(students)
#系统退出
def systemExit():
    print("谢谢使用")
    global end
    end = True
#从文件中加载数据 返回加载得到的列表
def loadData(fileName):
    #如果文件存在
    if os.path.exists(fileName):
        file = open(fileName,'r',encoding='utf-8')
        #读取所有数据
        stus = file.read()
        #使用换行符分割字符串
        stus = stus.split('\n')
        #删除最后一个元素(最后一个元素为换行符)
        stus.pop()
        file.close()
        return stus
    #如果文件不存在，返回空列表
    else:
        return []
#将数据写入到文件中
def saveData(fileName):
    file = open(fileName,'w',encoding='utf-8')
    for i in range(len(students)):
        file.write(students[i]+'\n')
        file.flush()
    file.close()
#程序开始的时候，先从文件中加载之前数据
students = loadData(fileName)
while not end:
    showMenu()
    choice = input("请选择 1-4:")
    if choice == '1':
        stu = input("请输入学生姓名:")
        addStudent(stu)
        print("添加成功")
    elif choice == '2':
        stu = input("请输入学生姓名:")
        delStu(stu)
    elif choice == '3':
        showAllStudent()
    elif choice == '4':
        #退出程序的时候，保存文件
        saveData(fileName)
        systemExit()

