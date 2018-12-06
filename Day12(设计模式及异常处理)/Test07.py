"""
异常处理：
    需求：
        从键盘输入被除数与除数，求商 并打印结果

1.输入的数据类型问题  ValueError:
2.ZeroDivisionError: division by zero

try:
except Exception as e:

try:
except A异常:

except B异常

如果A异常类型匹配，B异常不会执行

可以存在多个except分支，多个异常之间，要求，子类在前，父类在后


"""
a = input("请输入被除数")
b = input("请输入除数")
# try:
#     a = int(a)
#     b = int(b)
#     c = a / b
#     print("商为:%d" % c)
# except ValueError as e:
#     print(type(e))
#     print(e)
# except ZeroDivisionError:
#     print("数学异常")
# except Exception:
#     print("遇到异常")

# try:
#     print("转换a")
#     a = int(a)
#     print("转换b")
#     b = int(b)
#     print("计算")
#     c = a / b
#     print("商为:%d" % c)
# except ValueError as e:
#    print("输入类型有误")
# except ZeroDivisionError:
#     print("除数为0")

try:
    print("转换a")
    a = int(a)
    print("转换b")
    b = int(b)
    print("计算")
    c = a / b
    print("商为:%d" % c)
except (Exception,ValueError,ZeroDivisionError) as e:
    print(type(e))
    print("输入类型有误/或者除数为0")
    #args为BaseException中的一个成员变量，存储错误原因
    print(e.args)







