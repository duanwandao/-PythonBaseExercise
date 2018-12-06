"""
切片

字符串[start:end:step]

切片操作：包括start，不包括end

"""
#复制目标文件：  文件为srcFile:表示的完整路径(绝对路径)
#C:/Users/Administrator/Desktop/123.txt
def copyFile(scrFile):
    file = open(scrFile, 'r')
    content = file.read()

    file_name = scrFile[scrFile.rindex('/')+1:]
    # print(file_name)
    index = file_name.rindex('.')
    name = file_name[0:index]
    #文件后缀  .txt
    suffix = file_name[index:]
    #新名字等于   name + '-副本'+suffix
    new_file_name = name + '-副本' + suffix

    new_file_path =scrFile[:scrFile.rindex('/')+1] + new_file_name
    new_file = open(new_file_path,'w',encoding='utf-8')
    # #将读取到的内容写入到新文件中
    new_file.write(content)

    #关闭文件
    file.close()
    new_file.close()


copyFile('D:/2018教学/班级/4.18-6-25-212/Day08/代码/123.txt')