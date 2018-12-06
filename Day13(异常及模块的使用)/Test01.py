"""
类属性
    定义位置
        类内，方法外

    存储份数
        唯一
        所有对象共享一份

    类属性的访问方式：
        1.类名.类属性
        2.对象名.类属性
            仅限于获取值
            设置值的意味着添加一个新的成员变量，变量名与类属性名一致

类方法静态方法

单例模式：
    业务核心：
        1.保证全局对象唯一
            __new__()
            分配内存
        2.保证初始化唯一
            __init__()
            将内存中存储的成员变量进行初始化

异常处理：
    try:
        可能出现问题的代码
    except:
        捕获到异常后执行的代码
     try:
        可能出现问题的代码
     except Exception as e:
        print(e.args)

    try:
        可能出现问题的代码
    except 异常1:
        捕获到异常1后执行的代码
    except 异常2:
        捕获到异常2后执行的代码
    except 异常3:
        捕获到异常3后执行的代码

    多个异常之间，子类在前，父类在后

    try:
        可能出现问题的代码
    except(异常1，异常2...)
        捕获到异常元组中任何一个异常执行的代码
        注意:元组中的异常，没有顺序要求

异常：try except  else  finally

else:
    没有异常的时候执行

finally：
    不管是否有异常，都会在程序结束前执行


"""
# class Data():
#     __single = None
#     __firstInit = False
#     def __new__(cls, *args, **kwargs):
#         # if cls.__single == None
#         if not cls.__single:
#             cls.__single = super().__new__(cls)
#             # return cls.__single
#         return cls.__single
#     def __init__(self,name):
#         if not Data.__firstInit:
#             self.name = name
#             Data.__firstInit = True
# data1 = Data('123')
# data2 = Data('456')
# print(id(data1))
# print(id(data2))
# print(data1.name)
# print(data2.name)

# try:
#     file = open('123.txt', 'r', encoding='utf-8')
#     content = file.read()
#     print(content)
#     file.close()
# except:
#     print("io异常")
# else:
#     print("没有异常")
# for i in range(5):
#     print(i)
# else:
#     print("循环结束")

try:
    file = open('123.txt', 'w', encoding='utf-8')
    file.write('HelloWorld1\n')
    file.write('HelloWorld2\n')
    file.write('HelloWorld3\n')
    file.write([1,2,3,4])
except ValueError as e:
    print(e.args)
else:
    print("没有异常")
finally:
    file.close()
    #数据库关闭，socket关闭，io流关闭
    print("谢谢使用")

try:
    print("试一试")
finally:
    print("最后执行的代码")
