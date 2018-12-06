"""
列表中元素的排序
sort()
 按自然顺序(从小到大)进行排序

 对源数据直接进行排序操作，不会生成新的备份


列表的嵌套使用

num =  random.randint(1,6)
嵌套列表中所有元素的遍历

"""
# list1 = [98,20,100,66,88,10,90]
# # 从小到大
# # list1.sort()
# # 从大到小
# list1.sort(reverse=True)
# print(list1)

# list2 = [[1,2,3],[4,5],[6,7,8,9]]
list2 = [[1,2,3],4,5,[6,7,8,9]]

for v in list2:
    # print(sub_list)
    # 判断sub_list是列表的时候，在进行二级遍历
    if type(v) == list:
        for i in v:
            print(i)
    else:
        print(v)
students = [['name1',1001],['name2',1002],['name3',1003]]
# print('name1' in students)
for i in range(len(students)):
    if 'name1' in students[i]:
        print("包含")