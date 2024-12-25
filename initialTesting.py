

import pyautogui as pg
import time

print(pg.size())

# pg.moveTo(100, 100, 1.5)
# pg.moveTo(800,200)
# pg.dragTo(800,500, 3,button="left")
# pg.mouseDown(800,300, button="left")
# pg.moveTo(900,500, 1.5)
# pg.mouseUp(900,500, button="left")

# pg.hotkey('command',"space")


pg.keyDown("command")
pg.keyDown("space")

pg.keyUp("command")
pg.keyUp("space")

# print(pg.isValidKey("space"))
pg.typewrite("brave")
# time.sleep(1)
pg.press("enter")

# time.sleep(2)
pg.leftClick(400,400)

# time.sleep(2)
pg.keyDown("command")
pg.press("t")
pg.keyUp("command")

# time.sleep(2)
pg.typewrite("tiktok.com/login")
pg.press("enter")

pg.moveTo(789, 793, 1)
pg.click()

pg.moveTo(1007, 738, 1.5)
pg.click()


time.sleep(3)
