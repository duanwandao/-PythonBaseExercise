"""
迭代器：
    迭代：
        遍历的一种方式

    可迭代性：iterable
        如何判断一个对象是否具备可迭代性？
            1.判断目标对象是否属于Iterable类   instance


            2.for 循环

        练习：
            测试列表,字符串，元组，字典，是否具备可迭代性,生成器


    迭代器： Iterator
        能够使用next()函数调用，并不断返回下一个值的对象，称为迭代器
        生成器是否是迭代器？
        列表、元组、字符串、字典是否是迭代器？
        具备可迭代性的不一定是迭代器


    将具备可迭代性的对象转换为迭代器
    iter(具备可迭代性的对象)


"""
from collections import Iterable,Iterator

list1 = [x for x in range(10)]

#测试列表是否具备可迭代性
if isinstance(list1,Iterable):
    for x in list1:
        print(x,end=' ')

print()
#字符串是否具备可迭代性

str1 = 'HelloWorld'
if isinstance(str1,Iterable):
    for ch in str1:
        print(ch,end=" ")

print()
tuple1 = tuple(list1)
#元组是否具备可迭代性
if isinstance(tuple1,Iterable):
    for x in tuple1:
        print(x,end=' ')

print()

#测试字典是否具备可迭代性
dict1 = {'one':1,'two':2,'three':3,'four':4,'five':5}
if isinstance(dict1.values(),Iterable):
    for v in dict1.values():
        print(v,end=" ")

print()
#测试生成器是否具备可迭代性
g = (x for x in range(10))
if isinstance(g,Iterable):
    for x in g:
        print(x,end=' ')

print()
#判断生成器是否为迭代器
if isinstance(g,Iterator):
    print("生成器就是迭代器")
    # next(g)

if isinstance(list1,Iterator):
    print("列表是迭代器")
else:
    print("列表不是迭代器")

list1 = iter(list1)
if isinstance(list1, Iterator):
    print("转换后的列表是迭代器")
else:
    print("列表不是迭代器")

print(next(list1))

all_items = dict1.items()
print(type(all_items))
if isinstance(all_items,Iterable):
    for k,v in all_items:
        print(k,v)

all_items = iter(all_items)
print(type(all_items))
if isinstance(all_items,Iterator):
    print("是迭代器")
else:
    print('No')

