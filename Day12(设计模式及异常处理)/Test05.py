"""
异常处理：
    需求：
        从键盘输入被除数与除数，求商 并打印结果

1.输入的数据类型问题  ValueError:
2.ZeroDivisionError: division by zero

try-except

"""
a = input("请输入被除数")
b = input("请输入除数")
#判断  a必须是全为数字组成才可以转换成int
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    #保证b不能为0才可以求商
    if b != 0:
        c = a / b
        print("商为:%d" % c)
    else:
        print("ZeroDivisionError: division by zero")
        print("除数不能为0")
else:
    print("输入类型有误")





