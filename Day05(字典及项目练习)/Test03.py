"""
字典：
    1.字典的定义形式
        {key：value，key:value}
        China
        CN
        Japan
        JP
        America
        US
        Canada
        CA
        {'CN':'China','JP':'Japan','CA':'Canada'}

        key 具有唯一性,一般情况下使用字符串表示


    2.元素的访问
        student['name']

    3.元素的常用方法

    4.元素的遍历

"""
countries =  {'CN':'China','JP':'Japan','CA':'Canada','JP':123}
print(type(countries))
print(countries)

student = {'name':'小黑','age':18,'id':'1001','gender':'男','score':19}
student1 = ['小黄',18,'男',19,'1001']

print("%s的分数为:%d"%(student['name'],student['score']))