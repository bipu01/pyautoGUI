import pyautogui as pg
import time

print(pg.size())


time.sleep(1)
pg.keyDown("command")
pg.keyDown("space")

pg.keyUp("command")
pg.keyUp("space")

time.sleep(0.2)
pg.typewrite("arc")
pg.press("enter")

# for i in range(8):
# profiles =['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr']
profiles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for profile in profiles:
#     pg.rightClick(244, 457)
#     pg.leftClick(297, 711)
#
#     time.sleep(2)  # Adjust pause duration as needed

