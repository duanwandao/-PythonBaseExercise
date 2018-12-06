"""
函数的参数问题(形参):

1.缺省参数
    形式参数为缺省参数的时候，在函数调用的时候，可以不给实际参数，这时候，形参的值是给定的默认值
    如果在调用时，给出了新的实际参数，则形参的值为给的新值

2.可变参数
    *args
        如果函数定义的时候，形参是可变参数(*args)
        在函数调用时，可以给0个，1个，多个实参

"""
#结束程序
# exit(code=0)
# exit(0)
# exit(1)
# exit(-1)
#code默认为1，如果给定了新值，则code的值将不在是1，而是新的值
def test1(code=1):
    print('code=%d'%code)

# test1()
# test1(10)


def test2(*args):
    print(type(args))
    print(args)

test2()
test2(1)
test2(1,2,3)
test2([1,2])

def get_sum(a,b):
    return a + b
#求任意个整数的和
def get_sum1(*args):
    result = 0
    for i in args:
       result += i
    return result

print(get_sum1(1,2))
print(get_sum1(1,2,3))