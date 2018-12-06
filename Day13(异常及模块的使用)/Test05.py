"""
模块的使用：
import Test00
import Test00
import Test00

无论import多少次，都执行一遍

1.import 模块
    访问方式
    模块.方法()
2.from 模块 import 变量,函数，类
    访问方式
        直接访问
        PI
        showPI
        AAA
    from 模块 import *

3. __all__ = ['变量名','类名','函数名']
    from 模块 import *
        只导入__all__列表中包含的

"""
# import Test00
# print(Test00.PI)
# from Test00 import PI,showPI as _showPI,AAA
# import Test00
# print(PI)
# # showPI()
# _showPI()
# a = AAA()
# a.test1()

# from Test00 import *
# print(PI)
# showPI()
# a = AAA()
# a.test1()
# AAA.testClassMethod()
# AAA.testStaticMethod()

#在Test00模块中，不指明__all__的时候，默认导入所有的

#如果手动指明了列表，这时候导入的是列表中包含的
from Test00 import *
print(PI)
# showPI()
AAA.testClassMethod()

