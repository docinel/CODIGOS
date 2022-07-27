from multiprocessing.spawn import import_main_path
import pyautogui as pg
import time

cont = 0
while cont < 2:

    pg.PAUSE = 1.1
    time.sleep(3)

    pg.click(x=47, y=132)
    pg.click(x=57, y=299)
    pg.click(x=560, y=751)
    pg.click(x=61, y=256)
    pg.hotkey("ctrl","c")
    pg.click(x=511, y=742)
    pg.click(x=100, y=401)
    pg.hotkey("ctrl","v")
    pg.press("backspace")
    pg.press("tab")
    pg.write("3")
    # pg.press("tab")
    pg.click(x=577, y=538)
    # pg.click(x=556, y=506)
    # pg.click(x=562, y=749)
    pg.click(x=267, y=252)
    
    # pg.hotkey("ctrl","c")
    # pg.click(x=510, y=751)
    # pg.hotkey("ctrl","v")
    # pg.press("backspace",presses=2)
    pg.write("4")
    pg.press("enter")
    pg.click(x=205, y=302)
    pg.press("enter")
    pg.click(x=560, y=750)
    pg.rightClick(x=13, y=254)
    pg.press("e")
    pg.press("e")
    pg.press("enter")
    pg.click(x=517, y=752)
    cont = cont + 1