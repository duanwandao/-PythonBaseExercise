"""
v1.11 新增功能：
    1.优化主逻辑中业务代码
    2.新增我方子弹与敌方坦克的碰撞
        子弹新增方法  hit_tank()
"""
import pygame,time,random
# 将pygame.display 简称为_display
_display = pygame.display
COLOR_RED = pygame.Color(255,0,0)
version= 'v1.8'
#游戏主逻辑类
class MainGame():
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 550
    #窗口对象
    window = None
    PI_TANK = None
    #v1.6新增 敌方坦克列表，用来存储所有的敌方坦克
    enemy_tank_list = []
    enemy_tank_count = 5

    #v1.10 新增存储敌方子弹的列表
    enemy_bullet_list = []

    #v1.8 新增我方子弹列表
    bullet_list = []
    #开始游戏
    def startGame(self):
        pygame.display.init()
        #加载游戏窗口()
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #设置游戏标题
        pygame.display.set_caption('坦克大战'+version)
        #创建一个坦克
        MainGame.PI_TANK = Tank(600,220)
        #v1.6 新增 创建敌方坦克
        self.creatEnemyTank()
        while True:
            #渲染背景
            MainGame.window.fill(pygame.Color(0,0,0))
            #调用事件处理的方法
            self.getEvent()
            #v1.11 修改文字展示数据(取决于敌方坦克列表长度)
            MainGame.window.blit(self.drawText('剩余敌方坦克%d辆'%len(MainGame.enemy_tank_list)),(5,5))
            #v1.11调用展示我方坦克的方法
            self.show_P1_TANK()
            #v1.11调用展示敌方坦克的方法
            self.show_enemy_tank()
            #v1.11调用展示我方子弹的方法
            self.show_bullet()
            #v1.11调用展示敌方子弹的方法
            self.show_enemy_bullet()
            #刷新屏幕
            _display.update()
            #v1.5新增 主逻辑休眠
            time.sleep(0.005)
    #v1.6 新增创建敌方坦克的方法
    def creatEnemyTank(self):
        for i in range(MainGame.enemy_tank_count):
            random_left = random.randint(1, 8)
            random_speed = random.randint(1, 2)
            # 创建敌方坦克
            enemy_tank = EnemyTank(random_left * 100, 150, random_speed)
            MainGame.enemy_tank_list.append(enemy_tank)
    # v1.11 优化之我方坦克展示
    def show_P1_TANK(self):
        # 加载我方坦克 display_tank()中实现了两件事：1.根据方向修改图片，2.将坦克重新加入到窗口中
        MainGame.PI_TANK.display_tank()
        # v1.5调用我方坦克的移动方法
        if not MainGame.PI_TANK.stop:
            MainGame.PI_TANK.move()
    # v1.11 优化之敌方坦克展示
    def show_enemy_tank(self):
        # v1.6 新增 遍历敌方坦克，加入到窗口中
        for eTank in MainGame.enemy_tank_list:
            # v1.7 移动方式更新
            eTank.random_move()
            # v1.11 根据坦克live属性，判断坦克是否应该渲染
            if eTank.live:
                eTank.display_enemy_tank()
            else:
                MainGame.enemy_tank_list.remove(eTank)
            # v1.10 敌方坦克调用射击方法
            eBullet = eTank.random_fire()
            # 在random_fire()返回值有可能为None，只有保证不是None的时候，再将子弹存储起来
            if eBullet:
                MainGame.enemy_bullet_list.append(eBullet)
    # v1.11 优化之我方子弹展示
    def show_bullet(self):
        # v1.8 新增子弹在屏幕上完成绘制
        for bullet in MainGame.bullet_list:
            # v1.9 新增调用子弹移动
            bullet.bullet_move()
            if bullet.live:
                bullet.display_bullet()
                #v1.11 调用子弹碰撞方法
                bullet.hit_tank()
            else:
                # 删除子弹待实现
                MainGame.bullet_list.remove(bullet)
    # v1.11 优化之敌方子弹展示
    def show_enemy_bullet(self):
        # v1.10 新增 敌方子弹的渲染
        for eBullet in MainGame.enemy_bullet_list:
            # v1.9 新增调用子弹移动
            eBullet.bullet_move()
            if eBullet.live:
                eBullet.display_bullet()
            else:
                # 删除子弹待实现
                MainGame.enemy_bullet_list.remove(eBullet)

    #事件处理方法
    def getEvent(self):
        #获取所有事件
        eventList = pygame.event.get()
        for event in eventList:
            #type属性
            if event.type == pygame.QUIT:
                print("退出游戏")
                self.gameOver()
            #判断事件类型如果为按键按下的时候，在进行具体点击哪个key的判断
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("向左移动")
                    #修改坦克的方向，因为坦克的图片取决于坦克的方向，修改方向意味着刷新时，坦克会换图片
                    MainGame.PI_TANK.direction = 'L'
                    #v1.5 新增，坦克移动的开关控制
                    MainGame.PI_TANK.stop = False
                    # MainGame.PI_TANK.move()
                elif event.key == pygame.K_RIGHT:
                    print("向右移动")
                    MainGame.PI_TANK.direction = 'R'
                    # MainGame.PI_TANK.move()
                    # v1.5 新增，坦克移动的开关控制
                    MainGame.PI_TANK.stop = False
                elif event.key == pygame.K_UP:
                    print("向上移动")
                    MainGame.PI_TANK.direction = 'U'
                    # MainGame.PI_TANK.move()
                    # v1.5 新增，坦克移动的开关控制
                    MainGame.PI_TANK.stop = False
                elif event.key == pygame.K_DOWN:
                    print("向下移动")
                    MainGame.PI_TANK.direction = 'D'
                    # MainGame.PI_TANK.move()
                    # v1.5 新增，坦克移动的开关控制
                    MainGame.PI_TANK.stop = False
                elif event.key == pygame.K_SPACE:
                    print("biu biu biu ~~%d"%len(MainGame.bullet_list))
                    # v1.8 我方坦克发射子弹
                    #v1.9新增我方坦克发射子弹的数量控制
                    if len(MainGame.bullet_list) < 3:
                        # v1.10 优化射击方案
                        bullet = MainGame.PI_TANK.fire()
                        MainGame.bullet_list.append(bullet)

            #v1.5 新增 按键松开事件处理
            if event.type == pygame.KEYUP:
                #v1.9优化   弹出的不是空格键再停止
                if event.key != pygame.K_SPACE:
                    MainGame.PI_TANK.stop = True

    # 给一个字符串，返回一个包含字符串内容的表面(Surface)
    def drawText(self,content):
        #字体模块初始化
        pygame.font.init()
        #创建字体对象
        font = pygame.font.SysFont('kaiti',18)
        # fonts_list = pygame.font.get_fonts()
        # print(fonts_list)
        #kalinga
        #使用字体渲染内容 render()
        text_sf = font.render(content,True,COLOR_RED)
        #返回包含内容的Surface
        return text_sf
    def gameOver(self):
        exit()

#继承精灵类的类，供其他类来继承
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Tank(BaseItem):
    def __init__(self,left,top):
        #坦克图片集(上下左右四个方向)
        self.images = {
            #key为'U'  value:为 pygame.image.load('img/p1tankU.gif')得到的一个surface
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        #坦克的方向
        self.direction = 'U'
        #坦克初始化时候的默认图片，根据坦克的方向从字典里去取
        self.image = self.images[self.direction]
        #坦克的区域(left,top,width,heigt) 坦克位置及坦克大小
        self.rect = self.image.get_rect()
        # 将坦克距左边的位置修改为参数指定的位置
        self.rect.left = left
        # 将坦克距上边的位置修改为参数指定的位置
        self.rect.top = top
        # 坦克的速度
        self.speed = 2
        #v1.5 新增 stop变量，用来控制坦克是否应该移动的开关
        self.stop = True
        #v1.11新增属性 live 用来判断坦克是否凉了
        self.live = True

    #展示坦克
    def display_tank(self):
        #设置坦克图片
        self.image = self.images[self.direction]
        #将坦克加入到窗口中
        MainGame.window.blit(self.image,self.rect)
    # v1.5 新增坦克移动方法
    def move(self):
        #修改tank的坐标：取决于坦克的方向
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT-MainGame.PI_TANK.rect.height:
                self.rect.top += self.speed
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH-MainGame.PI_TANK.rect.width:
                self.rect.left += self.speed
    #v1.8 新增射击方法
    def fire(self):
        # 创建子弹对象
        bullet = Bullet(self)
        # 加入到列表中
        # MainGame.bullet_list.append(bullet)
        return bullet

class MyTank(Tank):
    pass
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        #图片集
        self.images = {
            # key为'U'  value:为 pygame.image.load('img/p1tankU.gif')得到的一个surface
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif')
        }
        # 坦克的方向
        self.direction = self.random_directon()
        # 坦克初始化时候的默认图片，根据坦克的方向从字典里去取
        self.image = self.images[self.direction]
        # 坦克的区域(left,top,width,heigt) 坦克位置及坦克大小
        self.rect = self.image.get_rect()
        # 将坦克距左边的位置修改为参数指定的位置
        self.rect.left = left
        # 将坦克距上边的位置修改为参数指定的位置
        self.rect.top = top
        # 敌方坦克的速度
        self.speed = speed
        self.stop = False
        #v1.7 新增步数控制
        self.step = 10
        # v1.11新增属性 live 用来判断坦克是否凉了
        self.live = True

    # 生成随机方向
    def random_directon(self):
        num = random.randint(1,4)
        if num == 1:
            self.direction = 'U'
        elif num == 2:
            self.direction = 'D'
        elif num == 3:
            self.direction = 'L'
        elif num == 4:
            self.direction = 'R'
        return self.direction
    #v1.7 新增随机移动方法
    def random_move(self):
        if self.step == 0:
            self.random_directon()
            #  如果将step复位到10会怎么样？
            self.step = 50
        else:
            self.move()
            self.step -= 1

    # v1.10新增 随机射击方法
    def random_fire(self):
        num = random.randint(1,120)
        if num == 1:
            eBullet = self.fire()
            return eBullet

    #将敌方坦克加入到窗口中
    def display_enemy_tank(self):
        # 重新设置图片
        self.image = self.images[self.direction]
        # 将坦克加入到窗口中
        MainGame.window.blit(self.image,self.rect)
        # super().display_tank()

#v1.8 实现子弹类
class Bullet(BaseItem):
    def __init__(self,tank):
        self.image = pygame.image.load('img/bullet.gif')
        self.direction = tank.direction
        # 子弹速度
        self.speed = MainGame.PI_TANK.speed * 1.5
        self.rect = self.image.get_rect()
        #子弹初始化位置要根据坦克的方向进行调整
        if self.direction == 'U':
            # self.rect.left += (坦克宽度的一半-子弹的宽度的一半)
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        #v1.9新增属性 用来记录子弹是否碰撞到墙壁或者坦克
        self.live = True

    #v1.9 新增子弹的移动方法
    def bullet_move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False

    #v1.11 新增 子弹与敌方坦克的碰撞方法
    def hit_tank(self):
        for eTank in MainGame.enemy_tank_list:
            result = pygame.sprite.collide_rect(eTank,self)
            if result:
                self.live = False
                eTank.live = False
    # 将子弹加入到窗口中
    def display_bullet(self):
        MainGame.window.blit(self.image,self.rect)

class Explode():
    pass
class Musice():
    pass
game = MainGame()
game.startGame()