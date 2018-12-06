import Test01
Test01.show()

# import D:2018教学/班级/4.18-6-25-212/Day16/Test18
import random
#哪些模块允许被导入
import sys
value = sys.path
print(type(value))
print(value)
for path in value:
    print(type(path))
    print(path)

sys.path.append('D:/2018教学/班级/4.18-6-25-212/Day16/Tank')
# import tank18
from tank18 import *
game = MainGame()
game.startGame()




