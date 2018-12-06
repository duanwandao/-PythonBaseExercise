"""
递归：
    概念： 直接或者间接的调用自己

练习：
    ∑100 = 100 + ∑99

    1 + 2 + ...+5
练习：
    分别使用循环以及递归完成  5！ 求阶乘  5 * 4 * 3 * 2 * 1

"""
# count  = 0
# def test():
#     global count
#     count += 1
#     print("递归%d次调用"%count)
#     if count > 3:
#         return
#     test()
#     # return
#
# test()

def get_sum1(num):
    result = 0
    for i in range(1,num+1):
        result += i
    return result

def get_sum2(num):
    if num == 1:
        return 1
    else:
        return num + get_sum2(num-1)

print(get_sum1(998))
print(get_sum2(998))
