from platform import architecture

import pyautogui as pg
import time

pg.keyDown("command")
pg.keyDown("space")
pg.keyUp("command")
pg.keyUp("space")

pg.write("arc",0.1)
pg.press("enter")
time.sleep(1)

pg.keyDown("command")
pg.press("t")
pg.keyUp("command")
pg.write("mrbeast")

pg.moveTo(400,500)

pg.scroll(-50)
time.sleep(1)
# time.sleep(1)
# pg.typewrite("arc",0.4)
# pg.press("enter")
# time.sleep(1)

# pg.hotkey("ctrl","t")
# time.sleep(1)
# pg.typewrite("www.youtube.com/mrbeast",0.2)
# pg.press("enter")
