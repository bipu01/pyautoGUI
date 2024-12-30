import pyautogui as pg
import time

# print(pg.size())

# Define a list of names to iterate through
# names = ["Alice", "Bob", "Charlie", "David"]  # Replace with your desired names
names = ["a",'b','c','d','e','f','g','h','i','j','k','l','m'] # 13
# names2 =['n','o','p','q','r','s','t','u','v','w','x','y','z']

# Height of one button on Windows
interval = 34

#Position of new profile button
newProfile = (360, 606)

pg.press("win")
time.sleep(0.5)

pg.typewrite("arc",0.1)
pg.press("enter")
time.sleep(1)

iteration = 0
# iteration2 = 13

# for name in names:
for name in names:
    #
    # Clicks on plus and new space
    pg.moveTo(413,987,0.5)  # position of plus icon
    pg.leftClick()

    time.sleep(1)
    pg.moveTo(367,854,0.5)   # position of "new space" button
    pg.leftClick()

    # Enters the name of space
    time.sleep(1)
    pg.moveTo(142,360,0.3)   # position of space name input
    pg.leftClick()

    pg.typewrite(f"{name}",0.1)
    pg.press("enter")

    # clicks on profile options bar
    time.sleep(0.5)
    pg.moveTo(295,423,0.2)   # position of profile options bar
    pg.leftClick()
    #
    #

    #
    # clicks on new profile button
    time.sleep(0.5)
    pg.leftClick(newProfile[0], iteration * interval + newProfile[1],0.5) #Pos of new profile button
    #
    #

    time.sleep(0.5)
    # enters the name of profile
    pg.typewrite(f"{name}",0.1)
    pg.press("enter")

    time.sleep(0.5)
    # # confirm enters the name of profile
    # pg.press("enter")

    #move to the Create space button and click
    pg.moveTo(210,914, 0.5)
    pg.leftClick()

    # clicks to the side
    pg.moveTo(789, 793, 0.5)
    pg.leftClick()

    iteration += 1
    time.sleep(3)  # Adjust pause duration as needed
