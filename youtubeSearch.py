import pyautogui as pg
import time

pg.keyDown("win")
pg.keyUp("win")

time.sleep(1)
pg.typewrite("arc",0.4)
pg.press("enter")
time.sleep(1)

pg.hotkey("ctrl","t")
time.sleep(1)
pg.typewrite("www.youtube.com/mrbeast",0.2)
pg.press("enter")
