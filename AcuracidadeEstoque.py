import pyautogui as pyg
import time

Tempo_ini = time.time()
cont = 0
while cont < 100:

    pyg.PAUSE = 1
    time.sleep(1)

    pyg.click(x=502, y=744), pyg.click(x=67, y=245)
    pyg.hotkey("ctrl", "c"), pyg.click(x=463, y=748) 
    pyg.press("del"), pyg.hotkey("ctrl", "v")
    pyg.press("tab"), pyg.click(x=502, y=744), pyg.rightClick(x=12, y=242)
    pyg.click(x=71, y=407), pyg.click(x=463, y=748)
    

    cont = cont + 1 

    Tempo_fin = time.time()


print(int(Tempo_fin - Tempo_ini) / 60)
