def test(*args,a,b):
    print("哈哈哈，参数没用")
def test1(a,b,*args):
    print("哈哈哈，参数没用")

# test(1,2,3,4)
test1(1,2,3,4,5,6,7)
