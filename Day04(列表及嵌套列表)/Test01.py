"""
1.嵌套循环的使用：
2.for循环
    for 变量  in range(start,end,step):
        循环体
3.for循环的嵌套
    for
        for
4.99乘法表的练习

    倒序99乘法表  for 循环.__reversed__():
5. 等腰三角形/菱形
      *
     ***
    *****
6.字符串的使用
    6.1定义
    6.2输出
    6.3输入
    6.4求长度
    6.5索引值范围
        [0，字符串长度-1]
    6.6切片操作
        字符串[start:end:step]
        start省略，默认从0开始
        end省略，默认到结尾(包含最后一个)
        step省略，默认为1
        step如果为负数，表示倒序
    6.7 方法：
        1.怎么看文档
            1.1 方法的意思
            1.2 通过方法你能得到什么

        2.index,rindex ,find,rfind,count,replace,capitalize

        title
            将所有单词的首字母大写

        startswith
            判断字符串以什么开头

        endswith
            判断字符串是以什么结尾

        upper()
            小写转大写
        lower()
            大写转小写

        ljust()
        center()
        rjust()

        lstrip
        strip
        rstrip

"""
# str1 = '12345'
# print(str1[2:])
# print(str1[2:10000])
str2 = 'you,can you up'

print(str2.title())


url1 = 'http://www.baidu.com'
print(url1.startswith("http://www"))

fileName = '123.txt'
print(fileName.endswith('.py'))


str3 = 'HelloWorld'
print(str3.upper())
print(str3.lower())


str4 = "123abc"
print(str4.ljust(10))
print(str4.rjust(10,'*'))
print(str4.center(10,'*'))


str5 = '   abc   '
print(str5.lstrip())
print(str5.rstrip())
print(str5.strip())
