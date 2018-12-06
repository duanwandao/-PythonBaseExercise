"""
文件指针的偏移
    查看光标的位置
        tell()
        查看光标位置

    光标位置手动偏移
        seek(offset,position)

"""
# file = open('123.txt')
# print(file.tell())
# file.read(2)
# print(file.tell())
# file.close()

# file = open('123.txt')
#往后偏移两个位置
import io
# io.SEEK_SET       0
# io.SEEK_CUR       1
# io.SEEK_END       2
# file.seek(2,0)
# content = file.read()
# #3456
# print(content)
# file.close()

# 从文件末尾读取2个单位，‘-’符号是方向
#如果从文件末尾往前偏移，需要使用'rb'的形式打开文件
# file = open('123.txt','rb')
# # file.seek(-2,2)
# file.seek(-2,io.SEEK_END)
# content = file.read()
# print(content)

#统计指定文件中代码的行数
def getNumberOfCodeInFile(filePath):
    file = open(filePath,encoding='utf-8')
    if file:
        count = 0
        content = file.readline()
        add = True
        while content != "":
            str = '"""'
            if str in content:
                add = not add
            if add:
                if "#" not in content:
                    count += 1
                    print(content)
            content = file.readline()
    file.close()
    return count


print(getNumberOfCodeInFile('Test04.py'))