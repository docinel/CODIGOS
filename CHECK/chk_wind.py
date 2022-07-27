import pyautogui as pag
import pygetwindow as gw
import time

# time.sleep(3)
# pag.hotkey("win","d")
time.sleep(1)
# texto = "business_inteligence"
if gw.getWindowsWithTitle('Touch Comp ERP')[0].minimize():
    print(True)
else:
    print(False)
    # gw.getWindowsWithTitle('Touch Comp ERP')[0].maximize()











# time.sleep(0.5)
# gw.getWindowsWithTitle('Touch Comp ERP')[0].minimize()
# time.sleep(2)
# gw.getWindowsWithTitle('business_inteligence')[0].maximize()
# if texto in excel:
#     print("Encontrado")
# else:
#     print("Nada")