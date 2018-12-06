"""
v1.2 新增功能：
    1.实现左上角剩余敌方坦克提示
        a、选一个字体
        b、使用指定的字体绘制文字
        c、将小画布贴到窗口中

"""
import pygame
# 将pygame.display 简称为_display
_display = pygame.display
COLOR_RED = pygame.Color(255,0,0)
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
        pygame.display.set_caption('坦克大战v1.2')
        while True:
            #渲染背景
            MainGame.__window.fill(pygame.Color(0,0,0))
            #调用事件处理的方法
            self.getEvent()
            #将带有文字的surface绘制到窗口中
            MainGame.__window.blit(self.drawText('剩余敌方坦克%d辆'%5),(5,5))
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