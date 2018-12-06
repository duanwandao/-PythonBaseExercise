"""
闭包：

    什么是闭包？
        嵌套定义的函数，内部函数使用外部变量，内部函数就称为闭包。

    如何定义一个闭包？
        1.函数嵌套定义
        2.内部函数使用外部函数作用域内的变量
        3.外部函数必须有返回值，返回内部函数名

    闭包的使用！
        好处：
            将外部函数中，局部变量的生命周期延长，程序周期
"""

def test(num1,num2):
    print(num1+num2)
test(10,20)

#外部函数
def func_out(num1):
    #内部函数 闭包
    def func_in(num2):
        return num1 + num2
    return func_in

func_in123 = func_out(10)
print(type(func_in123))
result = func_in123(20)
print(result)

result1 = func_in123(100)
print(result1)

result2 = func_in123(30)
print(result2)

func_in = func_out(20)
result3 = func_in(30)
print(result3)



