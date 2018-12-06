"""
文件:
    重命名：
        rename()
    删除文件：
        remove()
文件夹:
    获取当前所在路径
    getcwd()
    修改所在目录
    chdir()
    创建文件夹
    mkdir()
    删除文件夹
    rmdir()
    获取文件夹中所有的子文件
    listdir()
    判断是否为文件
    os.path.isfile()
    判断是否为文件夹
    os.path.isdir()
"""
import time
import os
# os.chdir('C:/')
print(os.getcwd())
os.listdir()
#文件重命名
# os.rename('123.txt','124.txt')
# os.remove('123-副本.txt')
# os.mkdir('新文件夹1')
# os.rmdir('新文件夹1')
currentPath = os.getcwd()
files = os.listdir(currentPath)
print(type(files))
print(files)
for fileName in files:
    #我是注释
    if os.path.isfile(fileName):
        print("%s是文件"%(currentPath+"\\"+fileName))
    elif os.path.isdir(fileName):
        print("%s是文件夹" %(currentPath+"\\"+fileName))