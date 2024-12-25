import pyautogui as pg
import time

print(pg.size())


time.sleep(3)
pg.keyDown("command")
pg.keyDown("space")

pg.keyUp("command")
pg.keyUp("space")

time.sleep(0.2)
pg.typewrite("arc")
pg.press("enter")

for i in range(8):

    pg.rightClick(244, 457)
    pg.leftClick(297, 711)

    time.sleep(1)  # Adjust pause duration as needed

