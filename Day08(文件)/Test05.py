"""
统计所有的代码
    1.统计单个文件中的代码
        a.单行注释的排除
        b.多行注释的排除

    2.找出某文件夹中所有的文件(.py文件)
"""
#统计指定文件中代码的行数
def irisCodeCounter(filePath):
    #记录代码的总行数
    lines = 0
    #打开文件
    file = open(filePath,'r',encoding='utf-8')
    #读取内容
    content = file.readline()
    #用来记录多行注释的开关
    add = True
    while content != "":
        str = '"""'
        # if str in content:
        #     add = not add
        if add:
            # 判断读取到的内容是否应该记录行数
            # 处理单行注释
            # if "#" not in content:
            lines += 1
        content = file.readline()
    #关闭文件
    file.close()
    return  lines
# print(irisCodeCounter('Test01.py'))