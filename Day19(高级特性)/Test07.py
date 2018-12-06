"""
装饰器装饰不定个数参数的函数

"""
def func_out(func):
    def func_in(*args):
        func(*args)
    return func_in

@func_out
def func_1(a):
    print(a)


@func_out
def func_2(a,b):
    print(a,b)


@func_out
def func_3(a,b,c):
    print(a,b,c)
@func_out
def func_0():
    print("我没有参数")

func_1(10)
func_2(10,20)
func_3(10,20,30)
func_0()