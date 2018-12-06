"""
从键盘录入两个整型数，分别打印两个值，
input()
int()
将两个数值完成交换，打印交换之后的值
=
print
"""
a = int(input("请输入第一个整型数"))
b = int(input("请输入第二个整型数"))
print("交换前:a = %d b = %d"%(a,b))
# 交换运算
# temp = a
# a = b
# b = temp

# a = a + b
# b = a - b
# a = a - b

a,b = b,a

print("交换后:a = %d b = %d"%(a,b))


