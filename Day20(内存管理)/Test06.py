"""
filter(func,iterable)
    使用func对iterable进行过滤，得到一个迭代器（可以迭代满足条件的数据）
reduce
需要先导入
from functool import reduce

    需求：求一个列表中所有元素的和

sorted()
    返回一个排序后的对象,默认按自然顺序排序(从小到大)，reverse = True ，则按从大到小
sort()

"""
# list1 = [x for x in range(1,101)]
# #过滤
# it = filter(lambda x:x%2==0,list1)
# for i in it:
#     print(i)

#--------------------------------

#【1，2，3，4，5，6...】
#['1','2','3','4']

# from functools import reduce
# list2 = [x for x in range(1,101)]
# result = reduce(lambda x,y:x+y,list2)
# print(result)
#
# list3 = ['1','2','3','4']
# result2 = reduce(lambda x,y:x+y,list3)
# print(type(result2))
# print(result2)
# print(int(result2))

# list3 = [1,9,3,20,100,8]
# print(list3.sort())
# result3 = sorted(list3,reverse=True)
# print(result3)

class Student():
    """
    文档注释：Student(name,age) -> new Student with name,age
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '【'+self.name+' '+str(self.age)+'】 '

stu1 = Student('bbc',18)
stu2 = Student('bac',20)
stu3 = Student('cab',17)

list4 = [stu1,stu2,stu3]
# list5 = sorted(list4,key=lambda x:x.age,reverse=True)
list5 = sorted(list4,key=lambda x:x.name,reverse=True)
# print(list5)
for stu in list5:
    print(stu)