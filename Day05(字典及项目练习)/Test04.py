"""
字典的常用方法：

students = {'胡来':{},'大娃':{}}

students['胡来']

增
    student[key] = value（可以为任意类型）

删
    pop(’key‘)
    del
    keyError： 没有要删除元素的时候报错

改
   key唯一，二次赋值的时候，新值覆盖旧值

查
    keys
    values
    items

"""
# studnets = {}
# name = input("请输入学生姓名")
# score = input("请输入学生分数")
# # {'胡来': ['胡来', '89']}
# # student = [name,score]
# #{'胡来': {'name': '胡来', 'score': '89'}}
# student = {'name':name,'score':score}
# studnets[name] = student
# print(studnets)
# # del_name = input("请输入要删除的学生姓名")
# # 可以
# # studnets.pop(del_name)
# # del studnets[del_name]
# # print(studnets)
#
# update_name = input("请输入要修改的学生姓名")
# update_new_name = input("请输入新的名字")
# update_new_score = input("请输入新的分数")
# new_student_list = [update_new_name,update_new_score]
# studnets[update_name] = new_student_list
#
# # new_studnet_dict = {'name':update_new_name,'score':update_new_score}
# # studnets[update_name] = new_studnet_dict
# print("修改之后的数据:",studnets)
#

countries =  {'CN':'China','JP':'Japan','CA':'Canada'}
all_keys = countries.keys()
print(all_keys)

for key in all_keys:
    print(key)
    print(countries[key])


# 判断是否包含某个值
print('CN' in all_keys)

del countries['CA']
countries.pop('JP')
print(countries)

del countries
