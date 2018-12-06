"""
集合

"""

var = {1,2,3,4,2}
# print(type(var))
# print(var)

var1 = {3,4,5,6}
#set不能使用+连接
# print(var+var1)

#&  取交集
print(var & var1)

#| 取并集
print(var | var1)

#^ 从并集中排除交集
print(var ^ var1)

#- {1,2,3,4} - {3,4,5,6}   从集合1中 刨除集合中与集合2的交集
print(var - var1)

#append.extend.insert
var.add(40)
print(var)
var.remove(4)
print(var)

#set没有索引值
# print(var[0])






