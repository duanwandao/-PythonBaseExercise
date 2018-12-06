"""
引用类型：
    str
    list
        列表:高级数组
        概念：
            存储多个数据（多个数据可以是任意类型）
        定义形式:
            scores = [89,98,35.5,23,100]
            names = ['童铁锤','王金刚','甄好看']
        访问：

             索引值(like str)


    tuple
    dict

"""

names = ['童铁锤', '王金刚', '甄好看']
#第一个学生名字
print(names[0])
#最后一个学生名字
print(names[-1])
print(names[2])
print(names[len(names)-1])
#IndexError: list index out of range
# print(names[len(names)])


# 如何打印列表所有的数据（遍历）   1.while  2. for i in range()  3. for  i in 变量:
#1.使用while循环
# i = 0
# while i < len(names):
#    print('names[%d] = %s'%(i,names[i]))
#    i += 1

#2. 使用for循环
# for i in range(len(names)):
#     print('names[%d] = %s' % (i, names[i]))

#3. 使用for循环
for name in names:
    # print("names[%d] = %s"%())
    print(name)