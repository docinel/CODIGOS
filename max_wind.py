import pyautogui as pag
import pygetwindow as gw
import time

time.sleep(3)
pag.hotkey("win","d")
time.sleep(1)
# texto = "business_inteligence"
excel = gw.getWindowsWithTitle('business_inteligence')[0].maximize()
# if texto in excel:
#     print("Encontrado")
# else:
#     print("Nada")