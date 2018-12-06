#coding=utf-8
#单行注释
"""
多行注释
"""
"""
需求：
    购物小票
        2瓶可乐            2.8 /瓶
        ---------------------------
        5个雪糕            2   /个
        ---------------------------
        1个酸奶            10  /瓶
    
        商品数量：   
        商品单价：
        
        
        总价：

变量：
    用来存储数据的值表示形式

"""
#count1用来记录可乐的瓶数
count1 = 2
# price1 用来存储可乐的单价
price1 = 2.8

#count2用来记录雪糕的个数
count2 = 5
#price2用来记录雪糕的单价
price2 = 2

#count3用来记录酸奶的个数
count3 = 1
# price3用来记录酸奶的单价
price3 = 10

# money用来存储花费的总钱数
money = count1 * price1 + count2 * price2 + count3 * price3

print("应付款￥:%g元"%money)

