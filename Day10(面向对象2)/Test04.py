"""

v1.1
    新增功能：
        1.暴击伤害
            概率性的暴击
            伤害值*2
            暴击伤害打印的突出(颜色，字体加粗)

练习：
面向对象的封装练习：
回合制游戏：
    大话西游、梦幻西游、问道...

    角色：
        Hero：
            属性：
                名字、生命值、伤害值(浮动随机值)
            方法：
                攻击方法

        Boss：
            属性：
                名字、生命值、伤害值(浮动)
            方法：
                攻击方法

    Hero
    Boss
    while True:
        if Hero.活着：
            Hero.攻击(Boss)
            if Boss.生命值 <= 0:
                print(“You Win”)
                break
        if Boss.没挂:
            Boss.反击(Hero)
             if Hero.生命值 <= 0:
                print(“Boss Win”)
                break
"""
import random
import time
class Hero():
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    #英雄攻击boss的方法，boss做参数，传进来
    def attack_boss(self,boss):

        rand_num = random.randint(1,10)
        if rand_num == 1 or rand_num == 2:
            #调用暴击伤害
            self.attack2_boss(boss)
        else:
            #调用普通伤害
            self.attack1_boss(boss)
    #普通伤害
    def attack1_boss(self,boss):
        # 伤害值增加随机浮动伤害值
        rand_damge = random.randint(1, 99)
        boss.hp -= (self.damage + rand_damge)
        print("英雄:%s 攻击Boss:%s 伤害值:%d Boss剩余生命值:%d"
              % (self.name, boss.name, self.damage + rand_damge, boss.hp))
    #暴击伤害
    def attack2_boss(self,boss):
        # 伤害值增加随机浮动伤害值
        rand_damge = random.randint(1, 99)
        boss.hp -= (self.damage + rand_damge)*2
        print("英雄:%s 攻击Boss:%s \033[1;31m暴击伤害值:%d\033[0m Boss剩余生命值:%d"
              % (self.name, boss.name, (self.damage + rand_damge)*2, boss.hp))
    #技能伤害
    # def attack3_boss(self,boss):
    #     pass

class Boss():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # 英雄攻击boss的方法，boss做参数，传进来
    def attack_hero(self, hero):
        rand_damge = random.randint(1, 35)
        hero.hp -= (self.damage+rand_damge)
        print("Boss:%s 攻击英雄:%s 伤害值:%d 英雄剩余生命值:%d"
              % (self.name, hero.name, self.damage+rand_damge, hero.hp))

count = 1
#创建英雄
hero1 = Hero('至尊宝',1000,20)
#创建Boss
boss1 = Boss('白晶晶',3000,5)
while True:
    print("------------------【round%d】-----------------"%count)
    if hero1.hp > 0:
        hero1.attack_boss(boss1)
        if boss1.hp <= 0:
            print("至尊宝获胜")
            break
    if boss1.hp > 0:
        boss1.attack_hero(hero1)
        if hero1.hp <= 0:
            print("晶晶获胜")
            break
    count += 1
    time.sleep(0.8)
    print('\n'*5)