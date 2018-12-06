"""
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
        字符串变量名[start:end:step]
        不包含end


    操作字符串常用的方法


"""

str_num = '0123456789'
# 从开始位置截取两个字符出来
result = str_num[0:2]
print(result)
# 切 从0到2的位置，不包括2
result1 = str_num[:2:1]
print(result1)
# 取从[0,2) 步长为2
result1 = str_num[:2:2]
# 默认取所有
result2 = str_num[:]
print(result2)

# 从索引值位置2的位置开始切片，切到哪？
result3 = str_num[2:]
print("result3 = %s"%result3)

#手动切片，从2到末尾
result4 = str_num[2:len(str_num)]
print("result4 = %s"%result4)
# 切片不会报越界异常  IndexError
result5 = str_num[2:1000]
print("result5 = %s"%result5)


result6 = str_num[1::2]
print(result6)

result7 = str_num[::-1]
print(result7)

# step为负值，表示从右往左取，如果要指定开头跟结尾，开头的值要大，结束的值要小
result8 = str_num[5:0:-1]
print("result8 = %s"%result8)




