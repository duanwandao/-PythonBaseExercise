"""
模块：
    1.什么叫模块
        一个以.py后缀结束的文件
        random/time/os/io/

    2.模块中可以存什么东西
        全局变量
        类
        函数
        可执行的代码

    3.如何使用模块
        import random
        会将模块中所有的代码执行一遍
        random.randint(1,6)

        手动引入模块
        import 模块
        导入之后的使用方式
            模块名.方法名()

"""
import Test00
print("--"*20)
print("PI = %g"%Test00.PI)
Test00.showPI()
#调用自定义模块类AAA中的成语方法
# a = Test00.AAA()
# a.test1()
#使用匿名对象直接调用模块Test00中类AAA中的成语方法
Test00.AAA().test1()
#调用Test00模块中类AAA中的静态方法，类方法
Test00.AAA.testStaticMethod()
Test00.AAA.testClassMethod()
import random

