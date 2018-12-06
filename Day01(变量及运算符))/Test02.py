"""
变量的定义以及使用
    count1 = 2
    print(count1)

\t： 表示制表符 一个tab键
\n： 表示换行

可以在双引号中的任意位置使用

标识符：
    变量名、类名、包名、方法名...

标识符命名的规则：
    组成部分：
        字母(包含汉字)、数字、下划线
        数字不能开头,大小写敏感
        不能使用系统的关键字
        驼峰命名
            1.大驼峰
                MaxNum = 100
            2.小驼峰
                maxNum = 100
            3.下划线连接
                max_num = 100

"""
count1 = 2
print(count1)
print("count1=%g"%count1)
count2 = 5
print("count1=%g\tcount2 = %g"%(count1,count2))
print("\ncount1 = %g\ncount2 = %g"%(count1,count2))



# shengao = 180
# print("身高:%gcm"%shengao)
# 身高 = 180
# print("身高:%gcm"%身高)
# sg = 180
# print("身高:%gcm"%sg)
shen_gao = 180
count1 = 10
#数字不能开头
# 1count = 10

height = 180



#大小写敏感
a = 100
A = 100
# 不能使用系统关键字作为标识符
# class = 10
# 导入获取关键字的包
import keyword
# 将所有的关键字存储到变量result中
result = keyword.kwlist
# 打印所有的关键字
print(result)
# 求result中关键字的个数
print(len(result))