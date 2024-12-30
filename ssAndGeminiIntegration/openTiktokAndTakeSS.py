import asyncio
import os
import pyautogui as pg
import time
from datetime import datetime
from apiCalls.callGemini import main
from pathlib import Path
import pyperclip


urls= ["https://www.tiktok.com/@gabrielegreco__/video/7441964267441491222",
       "https://www.tiktok.com/@foxsportsaus/video/7452542774521433345",'https://www.tiktok.com/@squidgamenetflix/video/7451770526692805918','https://www.tiktok.com/@gyemylesmultimedia0/video/7452636864864996614','https://www.tiktok.com/@shangxen783/video/7452090906628328722']

# urls=["https://www.tiktok.com/@sarai.dhologne/video/7452355691425156358"]

pg.keyDown("command")
pg.press("space")
pg.keyUp("command")

pg.write("arc",0.1)
pg.press("enter")
time.sleep(1.5)

# pg.keyDown("command")
# pg.press("t")
# pg.keyUp("command")

for _ in range(2):
    for url in urls:
        time.sleep(1.2)
        pg.moveTo(600,500,0.5)
        pg.leftClick(600,500)

        time.sleep(1)
        pg.keyDown("command")
        pg.press("t")
        pg.keyUp("command")

        pg.write(url,0.05)
        pg.press("enter")
        time.sleep(2)

        pg.moveTo(797,514,1)
        pg.doubleClick(797,514)

        time.sleep(2)

        # moves to comment button position and clicks
        pg.moveTo(1253,754,0.5)
        pg.leftClick(1253,754)

        # moves to comment input position and clicks
        pg.moveTo(765, 216, 1.5)
        pg.leftClick(765, 216)
        pg.write("Nice video!!👍", 0.1)
        pg.press("enter")

        pg.moveTo(765, 243, 0.5)
        pg.leftClick(765, 243)
        pg.write("Nice video!!👍", 0.1)
        pg.press("enter")

        pg.moveTo(780, 287, 0.5)
        pg.leftClick(780, 287)
        pg.write("Nice video!!👍", 0.1)
        pg.press("enter")

        time.sleep(1)
        pg.keyDown("command")
        pg.press("w")
        pg.keyUp("command")

        time.sleep(1)

    pg.keyDown("command")
    pg.keyDown("option")
    pg.press("right")
    pg.keyUp("option")
    pg.keyUp("command")



# pg.write("tiktok.com",0.1)
# pg.press("enter")
# time.sleep(4)
#
# # moves to comment button position and clicks
# pg.moveTo(1097,831,0.5)
# pg.leftClick(1097,831)
#
# # moves to comment input position and clicks
# pg.moveTo(1251,997,0.5)
# pg.leftClick(1251,997)
#
# # copies the url
# pg.keyDown("command")
# pg.keyDown("shift")
# pg.press("c")
# pg.keyUp("command")
# pg.keyUp("shift")
#
# copied_url = pyperclip.paste()
#
# print(copied_url)
#
# pg.write("Nice video!!👍",0.1)
# pg.press("enter")

async def take_screenshot_and_analyse():
    try:

        # define path to the screenshot
        image_dir = Path("./screenshots")
        image_dir.mkdir(exist_ok=True)

        # takes the screenshot
        screenshot = pg.screenshot()
        screenshot.save("./screenshots/screenshot.png")

        img_path = Path("./screenshots/screenshot.png").absolute()

        API_KEY = "AIzaSyC7zMsdpTT2JAEkjVtYkGIiOUbLtJUxAZg"

        result = await main(
            image_path= str(img_path),
            api_key=API_KEY,
        )

        if result:
            print("Analysis result:", result)
            return result
        else:
            print("Analysis failed")
            return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


# if __name__ == "__main__":
#     comment_pos= asyncio.run(take_screenshot_and_analyse())
#
#     comment_x_pos = int(comment_pos["comment_button_position"]['x'])
#     comment_y_pos = int(comment_pos["comment_button_position"]['y'])
#
#     pg.moveTo(comment_x_pos, comment_y_pos, 0.5)
#     pg.leftClick(comment_x_pos, comment_y_pos)
#
