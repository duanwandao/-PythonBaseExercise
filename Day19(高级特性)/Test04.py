"""
开发中的开闭原则：
    开放：
        添加功能开放

    关闭：
        修改源码

"""
import time
def write_log(file_name,func_name):
    # 记录当前时间，记录访问方法，写入日志文件
    try:
        file = open(file_name, 'a', encoding='utf-8')
        time_str = time.ctime()
        func_name = func_name
        content = time_str + '\t' + func_name + '\n'
        file.write(content)
    except Exception as e:
        print(e)
    finally:
        file.close()
#使用闭包完成功能的添加
#1.函数嵌套定义  2.内部函数访问外部函数作用域中的变量  3.外部函数必须有返回值，返回内部函数

def func_out(func):
    def func_in():
        #新增功能(写入日志文件)
        write_log('log.txt',func.__name__)
        #func是传进来的一个函数,调用函数
        func()
    return func_in
@func_out
#func1 = func_out(func1)
def func1():
    print("功能1")
@func_out
#func2 = func_out(func2)
def func2():
    print("功能2")

# func1 = func_out(func1,'log.txt')
# func1()
# func2 = func_out(func2,'log.txt')
# func2()
func1()
func2()
