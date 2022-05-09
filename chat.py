import pyautogui as pg
import sys

# 调试区域
# try:
#     while True:
#         x,y = pg.position()
#         positionStr = 'x:'+str(x).rjust(4) + ' y:'+str(y).rjust(4)
#         print(positionStr,end='')
#         print('\b'*len(positionStr),end='',flush=True)
# except KeyboardInterrupt:
#     print('\n')

# 屏幕位置
pg.moveTo(245,432,2)
pg.doubleClick(245,432) 

pg.moveTo(543,310,1)
pg.doubleClick(543,300)

pg.moveTo(543,300,1)
pg.click(543,300)

pg.hotkey('ctrl','c')

pg.keyDown('alt')
a = 0;
while a <= 1: #判断有多少个程序
    pg.press('tab')
    a += 1
pg.keyUp('alt')

pg.moveTo(1138,694,2)
pg.hotkey('ctrl','v')

pg.press('enter')

c = 0
while c < 50:
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    
    if c == 49:
        pg.moveTo(1143,20,1) #文件管理器关闭位置
        pg.doubleClick(1143,20) #文件管理器关闭位置
        break
    else:
        pg.press('down')
        pg.hotkey('ctrl','c')

        pg.keyDown('alt')
        pg.press('tab')
        pg.keyUp('alt')
        pg.hotkey('ctrl','v')
        pg.press('enter')
        c = c+1


