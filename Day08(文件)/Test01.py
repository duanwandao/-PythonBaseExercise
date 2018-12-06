"""
多参数
    **kwargs
    a=1,b=2


多返回值
    一个函数可以有多个返回值

    如果接受者为一个值，接收到的是元组
    否则就按指定个数去接收

递归函数
    直接或者间接调用自己
    压栈（栈：先进后出）

匿名函数
    lambda 参数...:表达式

    可以有一个或者多个参数
    不能有return
    可以将匿名函数存储到一个变量中，这个变量是function类型

    匿名函数的调用方式：
    变量(参数,...)

文件：
    打开文件
        file = open()
        r:只读
        w:写入
        a:追加
        b: 二进制的读取

        encoding = 'utf-8'

    写入文件
        write(“写入内容”)
        flush()
    读取文件
        read(n)
        readline()
            读取一行
        readlines()
    关闭文件：
        close()

    需求：
        完成123.txt的复制
        1.打开目标文件
        2.读取文件内容
        3.写入新文件
            新文件的名字处理?
        4.关闭文件(a、读取的文件  b、新创建的文件)

"""
file_name = '123.txt'
file_path = 'C:/Users/Administrator/Desktop/'+file_name
#打开目标文件
file = open(file_path,'r')
#读取目标文件的内容
content = file.read()

#新文件名格式：  原文件名-副本.txt，
#新文件名待处理(用到字符串的切片操作)
#1.在文件名中找到.的位置
index = file_name.index('.')
# 123
name = file_name[0:index]

#文件后缀  .txt
suffix = file_name[index:]

#新名字等于   name + '-副本'+suffix
new_file_name = name + '-副本' + suffix
#C:/Users/Administrator/Desktop/123-副本.txt
new_file_path = 'C:/Users/Administrator/Desktop/'+new_file_name

#打开新文件
new_file = open(new_file_path,'w',encoding='utf-8')
#将读取到的内容写入到新文件中
new_file.write(content)

#关闭文件
file.close()
new_file.close()


