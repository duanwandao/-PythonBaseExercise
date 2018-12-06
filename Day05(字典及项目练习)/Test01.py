"""
练习：
存储学生信息：
    students = [[年龄，分数],[],[]]
硬性要求： 实现1.添加学生功能  2.展示所有学生信息功能   3.退出功能

项目：  学生管理系统v1.0

   欢迎光临学生管理系统v1.0:
    1.添加学生
    2.查找学生
    3.展示所有
    4.删除学生
    5.修改学生
    6.退出系统
"""
# 用来存储所有学生
students = []
print("欢迎光临学生管理系统v1.0:")
while True:
    print("1.添加学生")
    print("2.查找学生")
    print("3.展示所有")
    print("4.删除学生")
    print("5.修改学生")
    print("6.退出系统")
    choice =  input("请选择1-6：")
    if choice == '1':
        # 添加学生逻辑
        name = input("学生姓名")
        score = int(input("学生分数"))
        student = [name,score]
        #将学生添加到学生列表中
        students.append(student)
        print("添加成功")
    elif choice == '2':
        pass
    elif choice == '3':
        print("所有学生信息如下",end=":")
        print(students)
    elif choice == '4':
        pass
    elif choice == '5':
        # 修改逻辑
        name = input("请输入你要修改的学生姓名:\n")
        # 遍历列表中所有的小列表，看小列表中是否包含要查找的名字
        index = -1
        for i in range(len(students)):
            if name in students[i]:
                # 使用index记录名字所在列表的索引值
                index = i
                break
        if index == -1:
            print("对不起，没有你要修改的学生信息")
        else:
            new_name = input("请输入新的名字")
            students[index][0] = new_name
            #新的分数
            new_score = int(input("请输入修改后的分数"))
            students[index][1] = new_score
            print("修改成功")

    elif choice == '6':
        print("谢谢访问，一路走好")
        break
    else:
        print("输入有误,请重新输入")


