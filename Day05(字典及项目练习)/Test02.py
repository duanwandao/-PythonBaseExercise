"""

元组：
    tuple
    表示形式:   (元素1，元素2....)
    不可变： 存储的的元素的值，不可修改，不可删除
    元素的访问：
        通过索引值访问
        tuple1[0]

    增
        append  insert
    删
    pop remove del
    clear
    改

    查
        index()
        count()
        in
        not in

    转换
        list <==> tuple


字典:


"""

tuple1 = ('学生1',99)
print(type(tuple1))
# AttributeError: 'tuple' object has no attribute 'append'
# tuple1.append(1001)
# AttributeError: 'tuple' object has no attribute 'remove'
# tuple1.remove(99)
# 访问指定索引值的元素
print(tuple1[0])
print(tuple1[-1])
print(tuple1[len(tuple1)-1])
#使用del删除索引值为0的元素 TypeError: 'tuple' object doesn't support item deletion
# del tuple1[0]
#TypeError: 'tuple' object does not support item assignment
# tuple1[1] = 100

# 查找
print(tuple1.index(99))
print(tuple1.count(99))
print(99 in tuple1)
print(99 not in tuple1)


#将元组转换为列表(tuple - > list)
list1 = list(tuple1)
print(list1)
list1[1] = 100
tuple1 = tuple(list1)
print(tuple1)


