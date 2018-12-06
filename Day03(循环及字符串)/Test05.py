"""
数据类型：
基本类型
    int
    float
    bool

引用类型
    str

    字符串的定义
        str1 = 'HelloWorld'
        str2 = "HelloWorld"

        "\n"

    字符串的输出
        %s

    字符串的输入
       str =  input("从键盘录入任意字符串")

    字符串求长度
        长度 = len(变量/常量)

    字符串的索引值
        范围：
            [0,len(变量)-1]

    字符串的切片操作

    操作字符串常用的方法


"""
# str1 = '\n'
# print(type(str1))
# print(str1+"HelloWorld")
# str2 = "123"
# print("%s"%str2)
# str3 = 'adfjadkjfaldsjfaldsjfladksjfkalsdjfaldsjfadshfaksdjhfajdskfh'
# # 求字符串'str3'的长度
# length = len('str3')
# print(length)
# # 求变量str3中存储的字符串内容的长度
# length = len(str3)
# print(length)
# print("%s的长度为:%d"%(str3,length))

str4 = 'HelloWorld'
# print(str4[0])
# print("hello的长度:%d"%len(str4))
#越界
# print(str4[5])
#取到最后一个
# print(str4[-1])
# print(str4[4])
# print(str4[len(str4)-1])

# 使用循环完成字符串中每个字符的打印，使用\t隔开  (1、while  2、for)
# i = 0
# while i < len(str4):
#     print(str4[i],end="\t")
#     i += 1

# for i in range(len(str4)):
#     print(str4[i], end="\t")

# for i in str4:
#     print(i,end="\t")