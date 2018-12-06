"""

通用装饰器
    修饰什么函数都好用

"""
def func_out(func):
    def func_in(*args,**kwargs):
        print("日志记录")
        return func(*args,**kwargs)
    return func_in
@func_out
def func1(a):
    print(a)
@func_out
def func2(a,b):
    return a + b
# print(func1(10))
@func_out
#b,c为缺省参数
def func3(a,b=2,c=3):
    print(a,b,c)

# result = func2(10,20)
# print(result)

# func3(1,2,3)




