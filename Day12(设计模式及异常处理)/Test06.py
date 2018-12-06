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
try:
    a = int(a)
    b = int(b)
    c = a / b
    print("商为:%d" % c)
except:
    print("输入类型有误或者除数为0")





