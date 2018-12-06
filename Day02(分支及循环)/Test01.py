"""
1、变量的定义
    num  = 10
2、变量的类型
    int
    float
    bool

    str

    list
    tuple
    dict
    set

    查看类型
        type(要查看的变量或者常量)
3、数学运算符(算术运算符)
    +
    -
    *
    /
    //
    **
    %
4、赋值运算符
    4.1 单独的赋值
        =
    4.2 结合使用的赋值
        +=
        -=
        *=
        /=
        //=
        **=
        %=
5、比较运算符
    ==
    !=
    >
    <
    >=
    <=

    比较结果： bool
6、逻辑运算符
    and
    or
    not
7、输入与输出
    result =  input("提示语句")
    result = int(result)

    print("%d %f %g %s")
    %d 输出int类型
    %f 输出float类型
    %g 自动识别整数还是小数
    %s 输出字符串

8、分支语句
    语法：
        if 表达式：
            表达式成立执行的代码


    逻辑操作之后的结果为bool


语句：
    分支语句：
        1.单分支
            if 表达式：
                表达式成立执行的代码
        2.双分支（二选一）
            if 表达式：
                表达式成立执行的代码
            else:
                表达式不成立执行的代码

        3.多分支：
            if 表达式1：
                表达式1成立执行的代码
            elif 表达式2:
                表达式2成立执行的代码
            elif 表达式3:
                表达式3成立执行的代码
            else:
                三个条件都不满足执行的代码


    循环语句：
"""
# print('abd' > 'abc')
# print(True and 'abd' > 'abc')

import random
num = random.randint(1,6)
print("num = %d"%num)
# if 1 <= num <= 3:
#     print("小")
#
# if 4 <= num <= 6:
#     print("大")

# if num >= 1 and num <= 3:
#     print("小")

if 1 <= num <= 3:
    print("小")
else:
    print("大")