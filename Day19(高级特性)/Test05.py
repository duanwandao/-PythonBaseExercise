"""
一个函数拥有多个装饰器的问题：
    装饰器用来装饰函数
    如果一个函数有多个装饰器，那么，装饰顺序取决于离函数的远近距离（近的先装）


《》

"""

def add_out1(func):
    print("装饰器开始装饰1")
    def add_in1():
        return '《' + func() + "》"
    return add_in1

def add_out2(func):
    print("装饰器开始装饰2")
    def add_in2():
        return '*' + func() + "*"
    return add_in2

@add_out1
#book_name = add_out1(book_name)
@add_out2
#book_name = add_out2(book_name)
def book_name():
    return '7个男人与1个女人的故事'

# book_name = add_out1(book_name)
# print(book_name())

print(book_name())