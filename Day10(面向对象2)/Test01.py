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
#用来存储所有学生信息
students = []
fileName = 'students.txt'
#展示主菜单功能
def showMenu():
    print("欢迎光临学生管理系统v2.0")
    print("1.添加学生")
    print("2.展示学生")
    print("3.退出系统")

#添加学生方法
def addStudent(stu):
    students.append(stu)
#展示所有学生
def showAllStudents():
    print(students)
def exitSystem():
    print("谢谢使用！")
    #系统的退出方法
    exit()
#从文件中加载数据
def loadStudents(fileName):
    #判断文件是否存在
    if os.path.exists(fileName):
        file = open(fileName,'r',encoding='utf-8')
        stus_str = file.read()
        stus = stus_str.splitlines()
        file.close()
        print("加载数据完毕")
        return stus
    else:
        return []
#将列表中的数据写入文件
def saveStudents(fileName):
    file = open(fileName,'a',encoding='utf-8')
    for stu in students:
        file.write(stu+"\n")
    file.close()
    print("写入数据完毕")

#程序最开始的时候，从数据将文件中加载出来
students = loadStudents(fileName)
while True:
    showMenu()
    choice = input("请选择:1-3")
    if choice == '1':
        #输入学生信息
        stu = input("请输入学生姓名")
        #调用添加方法
        addStudent(stu)
    elif choice == '2':
        showAllStudents()
    elif choice == '3':
        #程序结束之前，将数据写入到文件
        saveStudents(fileName)
        exitSystem()
