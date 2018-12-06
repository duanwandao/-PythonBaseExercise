"""
字符串方法：
str

find/rfind
如果有返回索引值，没有返回-1

index/rindex
如果有返回索引值，没有找到的话 raise  ValueError

count
统计某个字符串中要查找内容出现的次数


replace
修改字符串中指定的子串

"""
# result = dir(str)
# print(result)
# str1 ='good good study,day day up'
str2 ='you can \nyou up, \nno can no b b'

# print(str2.find('田'))
# print(str2.rfind('no'))

# print(str2.index('no'))
# print(str2.rindex('no'))
# # print(str2.index('aaaaaaaaa'))


# print(str2.count("no"))
# print(str2.count("Me"))
#
#
# str3 = str2.replace('you','I',1)
# print(str3)

str4 = str2.split(" ")
print(str4)

str5 = str2.splitlines()
print(str5)

# 将首字母大写
str6 = str2.capitalize()
print(str6)