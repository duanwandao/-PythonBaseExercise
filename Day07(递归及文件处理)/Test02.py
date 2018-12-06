"""
水仙花数
水仙花数是指一个 3 位数，
它的每个位上的数字的 3次幂之和等于它本身
（例如：1^3 + 5^3+ 3^3 = 153）
"""
#判断一个数字是否为水仙花数
def isNarcissisticNumber(num):
    if num < 100 or num > 999:
        # 结束函数
        return False
    #将num 个位、十位、百位上的数字分别取出来
    a = num % 10
    b = num // 10 % 10
    c = num // 100

    return a ** 3 + b ** 3 + c ** 3 == num

print(isNarcissisticNumber(153))
print(isNarcissisticNumber(154))
print(isNarcissisticNumber(15490))


for i in range(100,1000):
    if isNarcissisticNumber(i):
        print(i,end="\t")