"""
1.批量修改某个文件夹内所有的文件的名字

    1.找到所有文件
    import os
        listdir()
        递归

    2.修改
        rename()


"""
import os
#修改dirPath文件夹中所有的文件名
def rename_files(dirPath):
    allFiles = os.listdir(dirPath)
    for file in allFiles:

        #当前file的完整路径 文件夹路径+'/'+文件名
        filePath = dirPath + '/'+ file
        # print('filePath:%s'%filePath)
        if os.path.isfile(filePath):
            #判断文件是否为.py文件
            if file.endswith('.py'):
                # 新名字
                # newName = dirPath+"/"+'BBB'+ file
                # 将名字修改回去
                newName = dirPath+"/"+ file.replace("BBBAAA","")
                # print(newName)
                #修改名字(一定要写绝对路径)
                os.rename(filePath,newName)
        #如果为文件夹，递归调用自己
        elif os.path.isdir(filePath):
            rename_files(filePath)

rename_files('D:/2018教学/班级/4.18-6-25-212/Day08/代码')
print("修改完毕")


