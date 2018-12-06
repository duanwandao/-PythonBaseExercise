"""
创建生成器的方式：
    1.
        列表推导式
        g = (列表推导式)
        generator
    2.
        yield
        定义任意一个方法，在方法中加入yield关键字

    生成器生成数据3中方式：
        next(g)
        g.__next__()
        g.send()
            如果使用send生成第一个数据的时候，必须有一个None参数

    yield：
        携程

"""
# def test():
#     for x in range(10):
#         print(x)
# g = test()
# print(type(g))

def test():
    for x in range(10):
        #加入yield关键字，函数调用变成生成器
        yield x
        print("----")
        # print(x)
g = test()
# print(type(g))
#生成一个数据
print(g.send(None))
print(next(g))
print(g.__next__())
print(g.send(""))


def save_money():
    while True:
        print("存入￥1999")
        yield None
def draw_money():
    while True:
        print("取出Y1999")
        yield None

g_save = save_money()
g_draw = draw_money()

while True:
    # save_money()
    # draw_money()
    g_save.__next__()
    g_draw.__next__()


