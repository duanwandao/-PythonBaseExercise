lines = 0
import  os
def irisCodeCounter(filePath):
    for i in os.listdir(filePath):
        newPath = filePath + "/" + i
        # if ".py" in i:
        if os.path.isfile(newPath):
            a = 0
            file = open(newPath, 'r', encoding='utf-8')
            # 读取内容
            content = file.readline()
            while content != "":
                a += 1
                content = file.readline()
            # 关闭文件
            global lines
            lines += a
            file.close()
        elif os.path.isdir(newPath):
            # if i != ".idea":
            irisCodeCounter(newPath)

irisCodeCounter('D:/2018教学/班级/4.18-6-25-212')
print(lines)
