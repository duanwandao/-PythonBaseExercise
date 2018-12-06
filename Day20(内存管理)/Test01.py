"""
闭包：
    1.函数嵌套定义
        外部函数
            内部函数
                内部函数
                    ...
    2.内部函数使用外部函数作用域内的变量
    3.外部函数要有返回值，返回内部函数名

"""
# def func_out(func):
#     def func_in(*args,**kwargs):
#         print("我是新增功能")
#         return func(*args,**kwargs)
#     return func_in
#
# @func_out
# #test = func_out(test)
# def test():
#     print("我是测试函数")
#
# test()


class Test():
    def __init__(self,func):
        self.func = func
        print("我是新增功能")
        self.func()
    #解决'Test' object is not callable
    def __call__(self, *args, **kwargs):
        pass
@Test
#test = Test(test)
def test():
    print("我是测试函数")
# TypeError: 'Test' object is not callable
# test()


