"""

1.包是什么？
    包：（文件夹）
    package
    python3中可以不使用__init__.py模块
        __init__.py 初始化

    python2中一定要有

2.如何创建一个包
    new->package
    直接创建一个文件夹

3.包的作用
    1.方便管理
    2.不同的包中，允许存在同名类

4.如何引入指定包中的指定模块
    import package1.Test00
    from package1.Test00 import *

    引入某个包中的任何一个模块，该包中的__init__.py会先执行
        在init中一般执行导入当前包里的其他模块


"""
# import package1.Test00
# print(package1.Test00.PI)
# from package1.Test00 import *
# import package1
# print(package1.Test00.PI)

# from package2 import Test00
# from package1 import Test00
# print(Test00.PI)

#使用以下两种方式：
# from package1 import *
# print(PI)

import package1
print(package1.PI)


