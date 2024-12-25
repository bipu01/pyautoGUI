import pyautogui as pg
import time

# print(pg.size())

# Define a list of names to iterate through
# names = ["Alice", "Bob", "Charlie", "David"]  # Replace with your desired names
names = ["a",'b','c','d','e','f','g','h','i','j','k','l','m'] # 13
# names2 =['n','o','p','q','r','s','t','u','v','w','x','y','z']

# Height of 22 on Mac
interval = 22

#indicates the pos of profile bar
profileBar = (335, 329)

#indicates the pos of new profile button
newProfile = (371, 443)

pg.keyDown("command")
pg.keyDown("space")

pg.keyUp("command")
pg.keyUp("space")

time.sleep(1)
pg.typewrite("arc")
pg.press("enter")

time.sleep(1)
iteration = 0
# iteration2 = 13

# for name in names:
for name in names:

    time.sleep(0.5)
    # Clicks on plus and new space
    pg.leftClick(481, 1020)
    pg.leftClick(386, 729)

    time.sleep(0.5)
    # Enters the name of profile
    pg.typewrite(f"{name}")
    pg.press("enter")

    # clicks on profile menu
    time.sleep(0.5)
    pg.leftClick(profileBar[0], profileBar[1])

    # clicks on new profile
    time.sleep(0.5)
    pg.leftClick(newProfile[0], iteration * interval + newProfile[1])
    # pg.leftClick(newProfile[0], iteration2 * interval + newProfile[1])


    # enters the name of profile
    pg.typewrite(f"{name}")
    pg.press("enter")

    # confirm enters the initial name entry
    pg.press("enter")
    # confirm enters Create new profile
    pg.press("enter")

    # clicks to the side
    pg.moveTo(789, 793)
    pg.click()

    # iteration2 += 1
    iteration += 1
    time.sleep(2)  # Adjust pause duration as needed
