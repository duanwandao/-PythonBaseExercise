"""
数据类型
        num = 10
    int
        PI = 3.14
    float

    True/False

    bool

    type(要查看的变量或者常量)，得到该变量或者常量所属的类型





    list
        列表
    tuple
        元组
    dict
        字典
    set
        集合


输出
    格式化输出
    %g:输出小数或者整数
    %d:输出整数
    %f:输出小数

    %s:输出字符串

    print("身高:%g"%height)
    print("身高:%d"%height)
    print("身高:%f"%height)


输入


"""
# num = 10
# num = 20
# # 打印num的类型
# print(type(num))
# print(num)
# PI = 3.14
# print(type(PI))
# #3.14
# print("PI = %g"%PI)
# #3
# print("PI = %d"%PI)
# #3.14
# print("PI = %f"%PI)
# #保留小数点后2位打印
# print("PI = %.2f"%PI)
# 从键盘录入指定瓶数的可乐，计算总钱数
price = 2.8
count = input("请输入你想买多少瓶\n")
# print(type(count))
#从键盘录入的count，是str类型，不能进行数学运算，需要将count转换为int类型
count = int(count)
money = price * count
print("购买%d瓶可乐，需要花费:%g元"%(count,money))
