"""
练习：

项目：  学生管理系统v1.1

   欢迎光临学生管理系统v1.0:
    1.添加学生
    2.查找学生
    3.展示所有
    4.删除学生
    5.修改学生
    6.退出系统

    {name:{},name:{}}

"""
# 用来存储所有学生
students = {}
print("欢迎光临学生管理系统v1.1:")
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
        student = {'name':name,'score':score}
        #将学生添加到学生列表中
        students[name] = student
        print("添加成功")
    elif choice == '2':
        #输入要查找的学生姓名
        search_name = input("请输入你要查找的学生姓名")
        #获取所有的keys
        all_keys = students.keys()
        #看keys中是否有你要查找的
        if search_name not in all_keys:
            print("没有你要查找的学生")
        else:
            student_dic = students[search_name]
            print("学生信息如下:")
            print("【name:%s socre:%d】"%(student_dic['name'],student_dic['score']))
    elif choice == '3':
        print("所有学生信息如下",end="\n")
        #遍历所有的key
        # 获取所有的key
        # all_keys = students.keys()
        # for key in all_keys:
        #     # 找到key对应的value值
        #     stu_dic = students[key]
        #     print("【name:%s socre:%d】" % (stu_dic['name'], stu_dic['score']))
        #遍历所有的value
        # all_value = students.values()
        # for stu_dic in all_value:
        #     print("【name:%s socre:%d】" % (stu_dic['name'], stu_dic['score']))

        # 遍历所有的key，以及value  items()
        all_key_value = students.items()
        for key,stu_dic in all_key_value:
            print('key:%s'%key)
            print("【name:%s socre:%d】" % (stu_dic['name'], stu_dic['score']))

    elif choice == '4':
        del_name = input("请输入要删除的学生名字")
        all_keys = students.keys()
        if del_name in all_keys:
            del students[del_name]
            print("删除成功")
        else:
            print("没有该学生或者已经删除")
    elif choice == '5':
        # 修改逻辑
        update_name = input("请输入你要修改的学生姓名:\n")
        all_keys = students.keys()
        if update_name not in all_keys:
            print("没有该学生")
        else:
            new_name = input("请输入新名字")
            new_score = int(input("请输入新分数"))
            new_stu = {'name':new_name,'score':new_score}
            #将旧学生删除
            del students[update_name]
            #将新的加入
            students[new_name] = new_stu
            print("修改成功")
    elif choice == '6':
        print("谢谢访问，一路走好")
        break
    else:
        print("输入有误,请重新输入")


