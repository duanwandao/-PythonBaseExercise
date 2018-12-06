"""
函数的定义：
    def 函数名(参数列表...)
        代码
        return 对应的值

函数的分类：
    系统函数/自定义函数

    无参无返回值
    有参无返回值
    无参有返回值
    有参有返回值

参数：
    缺省参数
    def test(a = 1):
        pass
    可变参数
        *args
    def test1(*args):
        pass
    test1()
    test1(1)
    test1(1,2,3,4)
    test1([1,2,3])
    test1((1,2,3))

        **kwargs


"""
# def test1(*args):
#     print(type(args))
#     print(args)
#
# test1({"a":1})

# def test2(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# # test2()
# # test2('a':1)
# test2(a=1,b=2,c=[1,2,3],d={'id':1001,'age':18})


def test3(*args,**kwargs):
    print(args)
    print(kwargs)

# test3(1,a=1,b=[1,2,3],[1,2,3])
test3(b=[1,2,3])
