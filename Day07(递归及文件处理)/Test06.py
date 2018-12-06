"""
文件:
    .avi
    .mp4
    .mp3
    .txt
    .doc
    .gif
    .jpg
    .py
作用：
    数据持久化：
操作：
    1.打开文件
    file = open()


    2.写/读/修改（文件内容的操作）
    write('内容')

    3.关闭文件（自动保存）
    close()


    将“HelloWorld写入到指定的文件中123.txt”

    将你最喜欢一首古诗写入指定的文件，注意换行

"""
import locale
#获取当前默认的编码方式
print(locale.getpreferredencoding())
# print("%c"%20010)

#编码方式默认为cp936（GBK），不知道当前的默认编码可以使用locale.getpreferredencoding()查看 ，最好 手动指定为utf-8
# file = open('123.txt','w',encoding='utf-8')
file = open('C:/Users/Administrator/Desktop/123.txt','w',encoding='utf-8')
#‘w’:写，如果没有文件，会创建新的
file.write('HelloWorld')
file.close()