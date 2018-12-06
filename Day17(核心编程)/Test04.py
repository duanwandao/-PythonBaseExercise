"""
深复制与浅复制
list.copy()方法： 浅复制

deepcopy()
copy()


浅复制：
    对于单独的一个对象(对象中的成员变量为基本数据)，复制一份新的出来，跟深复制一样

深复制：
    deepcopy()
    返回一个新的对象(内容跟被复制对象一致)


二者区别：
浅拷贝和深拷贝之间的区别只适用于复合对象(包含其他对象的对象，如列表或类实例):
浅拷贝构造一个新的复合对象，然后(尽可能地)将引用插入到原始对象中。
深度复制构造一个新的复合对象，然后递归地将原始对象的副本插入其中。

"""
import copy
# list1 = [1,2,3]
# # print(list1)
# # print(id(list1))
# # list2 = list1.copy()
# # print(list2)
# # print(id(list2))
# list3 = copy.copy(list1)
# print(list3)
# print(id(list3))
#
# list4 = copy.deepcopy(list1)
# print(list4)
# print(id(list4))
list1 = [[1,2],[3,4]]
#浅复制
list2 = copy.copy(list1)
#深复制
list3 = copy.deepcopy(list1)
#True
print(list1[0] is list2[0])
#False
print(list1[0] is list3[0])





