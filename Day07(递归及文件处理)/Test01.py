"""
判断一个数字是否为质数
一个数，大于1，只能被1跟本身整除



打印1-1000之间所有的质数，两个一排
封装函数：判断一个数字是否为水仙花数
打印所有的水仙花数
"""
# 判断整型数num是否为质数
def isPrimeNumber(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

# def isPrimeNumber(num):
#     result = True
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 result = False
#                 break
#     else:
#         result = False
#     return result

print(isPrimeNumber(3))
print(isPrimeNumber(4))
print(isPrimeNumber(1239))
print(isPrimeNumber(9873))

count = 0
for i in range(1,1001):
    if isPrimeNumber(i):
        count += 1
        print("%-3d"%i,end=" ")
        # 每两个质数打印换行操作
        if count % 5 == 0:
            print()