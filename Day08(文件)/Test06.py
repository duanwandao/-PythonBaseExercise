"""
找出某个文件夹中所有的子文件
    递归

"""
totalLines = 0
import os
#使用Test05中的函数，首先要import Test05
import Test05
#展示某个文件夹所有的子文件
def showAllFiles(dirPath):
    #展示文件夹中所有的子文件
    listFileNames = os.listdir(dirPath)
    # 遍历所有子文件中的每个文件
    for fileName in listFileNames:
        #文件的绝对路径
        newPath = dirPath + "/" +fileName
        #如果newPath为文件(判断是否为.py文件，统计文件代码行数)
        if os.path.isfile(newPath):
            #判断文件后缀
            if newPath.endswith('.py'):
                #统计文件代码
                # print(newPath)
                global totalLines
                #调用Test05实现的递归函数
                totalLines += Test05.irisCodeCounter(newPath)
        #如果为文件夹
        elif os.path.isdir(newPath):
            #递归调用自己
            showAllFiles(newPath)

showAllFiles('D:/2018教学/班级/4.18-6-25-212')
print("从开学到现在，代码总行数为:%d:"%totalLines)