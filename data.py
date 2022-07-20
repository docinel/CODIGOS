from datetime import datetime, timedelta

import pyautogui
import time

Tempo_ini = time.time()
pyautogui.PAUSE = 1.5

# DETERMINANDO A DATA MENOS UM DIA
data = datetime.today() - timedelta(days=1)
data_hoje = (data.strftime('%d-%m-%Y' + '-00:00:00'))
print(data_hoje)
pyautogui.write(data_hoje)


Tempo_fin = time.time()


print(int(Tempo_fin - Tempo_ini) / 60)
