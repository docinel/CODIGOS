import pyautogui as pyg
import time

cont = 0
while cont < 10:

    pyg.PAUSE = 1.1
    time.sleep(3)

    pyg.click(x=502, y=744), pyg.click(x=67, y=245)
    pyg.hotkey("ctrl", "c"), pyg.click(x=463, y=748)
    pyg.click(x=72, y=365), pyg.press("del"), pyg.hotkey("ctrl", "v")
    pyg.press("tab"), pyg.click(x=502, y=744), pyg.rightClick(x=12, y=242)
    pyg.click(x=71, y=407), pyg.click(x=463, y=748)
    

    cont = cont + 1