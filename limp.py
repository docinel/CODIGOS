import pyautogui as pag
import time

time.sleep(3)
# pag.click(x=572, y=253)
contador = 0
while contador < 254:
    pag.press("f2")
    # time.sleep(1)
    pag.press("enter")
    contador = contador + 1