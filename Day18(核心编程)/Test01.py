"""
位运算：
    位运算符：
    <<
        按位左移
            a << n
            等价于
                a * 2^n
    >>
        按位右移
            a >> n
            等价于
                a / 2^n
    &
        按位与

            5 & 4 =  4
            两个操作数都为1，结果为1，其他为0
    |
        按位或
            5 | 4 = 5
            两个操作数只要有一个为1，结果为1
    ^
        按位异或
            5 ^ 4 =  1
            两个操作数相同为0，不同为1
            加密：
                一个数字对同一个值异或两次，得到本身

    ~
        按位取反


    将2变成8，使用你认为最快的操作

"""
# print(2 << 2)
# print(2 << 3)
#
# print(8>>2)
# #16 / 2^3
# print(16>>3)
# print(16>>4)

# print(5 & 4)
# print(5 | 4)
# print(5 ^ 4)

# password = 123456
# sk = 5
# #加密
# s_password = password ^ sk
# print(s_password)
# #解密
# print(s_password^sk)

# print(~5)

PI = 3.14
_num = 100
def _test():
    print("我是_test")




