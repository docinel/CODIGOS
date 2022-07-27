import pyautogui
import time
time.sleep(5)
# pyautogui.move(0, 400)       # move the mouse down 50 pixels.
# pyautogui.scroll(-30)  # scroll down 10 "clicks"
local = pyautogui.position()
print(local)
