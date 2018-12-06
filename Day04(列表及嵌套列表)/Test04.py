"""
list:
    加入购物车
    从购物车删除
    查询
    修改

    1.增
       append()
       insert()
       extend()

    2.删
        remove()
        del()
        pop()
        clear()
    3.查
        index()
        count()
        in
        not in

    4.改


"""
#创建空列表
names = []
# 实现条件数据
names.append("甄的热")
names.append('甄凉快')
print(names)
#往索引值为0的位置放入新的元素
names.insert(0,'范学良')
# 将范学良插入到-1(表示最后一个元素)，之前的最后一个元素向后移动
# names.insert(-1,'范学良')
print(names)

names2 = ['陆仁甲','王富贵']
#可以将name2中所有的元素，逐个加入到names中
names.extend(names2)

print(names)
#['范学良', '甄的热', '甄凉快', '陆仁甲', '王富贵']

# 查询操作
# 打印王富贵在列表中的索引值
print(names.index('王富贵'))
# list中没有的元素，报错ValueError:
# print(names.index('王富贵他大爷'))
print(names.count("王富贵"))
# 没有的元素，返回0，不报错
# print(names.count("王富贵他二大爷"))
print('王富贵' in names)
print('王富贵' not in names)

#给王富贵改的名字
#1.先判断有没有这个人
if '王富贵' in names:
    #2.找出位置index
    index = names.index('王富贵')
    #3.修改
    names[index] = '宋仁义'
else:
    print("Wang sir is not in")

# 删除操作
names.remove("陆仁甲")
print(names)
names.pop(0)
print(names)
#clear
names.clear()
print(names)

# del names[0]
# print(names)
# 删除购物车
# del names
# 不能使用
# print(names)




