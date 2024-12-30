import pyautogui as pg
import time

print(pg.size())

time.sleep(4)

# time.sleep(0.2)
# pg.typewrite("arc")
# pg.press("enter")

# profiles =['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr']
profiles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for profile in reversed(profiles):
    #click at middle
    pg.moveTo(667,336,0.5)
    pg.leftClick(667,336)

    pg.scroll(-300, x=667 , y=336)

    #scroll
    # pg.scroll(-300, 1)

    #click at profile
    pg.moveTo(645,670,0.5)
    pg.leftClick(645,670)

    #click at - button
    pg.moveTo(615, 715,0.5)
    pg.leftClick(615, 715)

    pg.typewrite(profile,0.1)
    pg.press("enter")
    time.sleep(1.5)  # Adjust pause duration as needed

