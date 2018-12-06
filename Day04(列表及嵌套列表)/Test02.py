"""
方法：
    拆分方法：
    partition

    rpartition

    isalpha
        所有字符都是字母
    isdigit
        是否所有的字符都是数字
    isalnum
        是否所有字符都是数字或者字母
    isspace
        是否所有字符都是space
    join


"""
str1 = 'ni hao ma hao de hen'
print(str1.partition('hao'))
print(str1.rpartition('hao'))
print(str1.split('hao'))

str2 = 'abc_*&123'
print(str2.isalpha())
print(str2.isdigit())
print(str2.isalnum())
print("     ".isspace())

str3 = '_'

print(str3.join(str1))

