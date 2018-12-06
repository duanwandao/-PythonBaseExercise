"""
将以下两个功能，分别添加日志功能

日志功能：  1.记录事件  2.记录时间  3.写入日志文件

"""
import time
def func1():
    #记录当前时间，记录访问方法，写入日志文件
    try:
        file = open('log.txt', 'a', encoding='utf-8')
        time_str = time.ctime()
        func_name = 'func1'
        content = time_str + '\t' + func_name+'\n'
        file.write(content)
    except Exception as e:
        print(e)
    finally:
        file.close()

    print("功能1")
def func2():
    # 记录当前时间，记录访问方法，写入日志文件
    # 记录当前时间，记录访问方法，写入日志文件
    try:
        file = open('log.txt', 'a', encoding='utf-8')
        time_str = time.ctime()
        func_name = 'func2'
        content = time_str + '\t' + func_name+'\n'
        file.write(content)
    except Exception as e:
        print(e)
    finally:
        file.close()
    print("功能2")

func1()
func2()