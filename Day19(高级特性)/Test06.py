"""
装饰器装饰固定个数参数的函数

"""
def func_out(func):
    def func_in(arg):
        func(arg)
    return func_in


@func_out
#func_1 = func_out(func_1)
def func_1(a):
    print("a = %s"%a)

# func_1(10)



def func_out2(func):
    def func_in(a,b):
        func(a,b)
    return func_in

@func_out2
#func_2 = func_out2(func_2)
def func_2(a,b):
    print(a,b)
func_2(1,2)
