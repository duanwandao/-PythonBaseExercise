"""
v1.1 新增功能：
    1.解决点击关闭按钮，程序未响应的bug
    2.事件处理，方向键控制，发射按键控制
"""
import pygame
# 将pygame.display 简称为_display
_display = pygame.display

#游戏主逻辑类
class MainGame():
    __SCREEN_WIDTH = 900
    __SCREEN_HEIGHT = 550
    #窗口对象
    __window = None
    #开始游戏
    def startGame(self):
        pygame.display.init()
        #加载游戏窗口()
        MainGame.__window = _display.set_mode([MainGame.__SCREEN_WIDTH,MainGame.__SCREEN_HEIGHT])
        #设置游戏标题
        pygame.display.set_caption('坦克大战v1.1')
        while True:
            #渲染背景
            MainGame.__window.fill(pygame.Color(0,0,0))
            #调用事件处理的方法
            self.getEvent()
            #刷新屏幕
            _display.update()
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
                elif event.key == pygame.K_RIGHT:
                    print("向右移动")
                elif event.key == pygame.K_UP:
                    print("向上移动")
                elif event.key == pygame.K_DOWN:
                    print("向下移动")
                elif event.key == pygame.K_SPACE:
                    print("biu biu biu ~~")
    def gameOver(self):
        exit()
class Tank():
    pass
class MyTank(Tank):
    pass
class EnemyTank(Tank):
    pass
class Bullet():
    pass
class Explode():
    pass
class Musice():
    pass

game = MainGame()
game.startGame()