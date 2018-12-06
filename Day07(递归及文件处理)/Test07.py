"""
文件的写：

D:/2018教学/班级/4.18-6-25-212/Day07/视频
D:\\2018教学\\班级\\4.18-6-25-212\\Day07\\视频

文件的读取：
    1、read
    2、readline
    3、readlines

"""
def write_ancient_poetry(fileName):
    file =open(fileName,'a',encoding='utf-8')
    for i in range(1,5):
        content = input("请输入第%d句"%i)
        file.write('\n')
        file.write(content)
        #刷新
        file.flush()
    #文件关闭，默认刷新
    file.close()

def read_content(fileName):
    #1.打开文件
    file = open(fileName, 'r', encoding='utf-8')
    #2.读取文件
    content = file.read()
    print(type(content))
    print(content)
    #3.关闭文件
    file.close()

def read_content1(fileName):
    #1.打开文件
    file = open(fileName, 'r', encoding='utf-8')
    #2.读取文件
    for i in range(6):
        content = file.readline()
        while content != "":
            print(type(content))
            print(content)
            content = file.readline()
    #3.关闭文件
    file.close()


def read_content2(fileName):
    #1.打开文件
    file = open(fileName, 'r', encoding='utf-8')
    #2.读取文件
    content = file.readlines()
    print(type(content))
    print(content)
    #3.关闭文件
    file.close()


# write_ancient_poetry('123.txt')
# read_content('123.txt')
# read_content1('123.txt')
read_content2('123.txt')